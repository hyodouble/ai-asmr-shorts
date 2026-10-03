#!/bin/sh
# Character story Shorts (2026-10-04). Replaces every older audio chain.
# Audio rule: keep Flow's stereo 48 kHz track; per clip, denoise only when it is quiet, then one linear gain.
# No speed change, notch, compressor, loudnorm or foley: lifting quiet Flow audio with those raised the
# noise floor to signal level and is what made every past video sound broken.
#
# Usage: sh build-story.sh <workdir>
#   workdir/raw/s1.mp4 .. sN.mp4  Flow 720x1280 clips, played in order
#   CUTS="0.5-9 1-7.5 ..."         optional in-out seconds per clip (default: whole clip)
#   workdir/out/overlayN.png        optional 1080x1920 transparent caption PNG per clip
#   SPEED=1.2                       optional playback speed (atempo keeps pitch); default 1
#   DN=0.001                        NLM denoise strength for boosted clips (higher = cleaner but duller)
# Output: workdir/out/story.mp4 at about -17 LUFS. Limiter ceiling 0.7 (-3 dB) because AAC overshoots limited peaks by ~2-3 dB.
set -eu
D=${1:?workdir}
cd "$D"
mkdir -p out frames
SPEED=${SPEED:-1}; TARGET=-16; MAXCLEAN=6; PEAKROOM=${PEAKROOM:-12}; DN=${DN:-0.001}
DELOGO="delogo=x=574:y=1138:w=56:h=56"
# Any clip that needs more than MAXCLEAN dB of gain gets denoised first: Flow's hiss and the rumble band
# under ~300 Hz rise with the gain (Mochi #1: -26..-30 LUFS clips boosted 10-14 dB showed a hiss bed).
# Cut the rumble, then non-local-means denoise (beat afftdn and gates in 2026-10-04 tests: SNR 0.8 -> 5.7 dB).
DENOISE="highpass=f=300:p=2,anlmdn=s=$DN:p=0.01:r=0.006"

lufs() { ffmpeg -nostdin -hide_banner -i "$1" -af ebur128=peak=true -f null - 2>&1 | awk '/^ +I:/{i=$2} /^ +Peak:/{p=$2} END{print i, p}'; }

N=$(ls raw/s*.mp4 | wc -l | tr -d ' ')
inputs=""; fc=""; cat_in=""; k=0
for n in $(seq 1 "$N"); do
  src="raw/s$n.mp4"
  cut=$(echo "${CUTS:-}" | awk -v n="$n" '{print $n}')
  a=${cut%-*}; b=${cut#*-}; [ -n "$cut" ] || { a=0; b=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$src"); }
  d=$(echo "scale=4; ($b - $a) / $SPEED" | bc)
  set -- $(lufs "$src")
  af="atrim=$a:$b,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  if awk -v i="$1" -v t="$TARGET" -v m="$MAXCLEAN" 'BEGIN{exit !(t - i > m)}'; then af="$af,$DENOISE"; tag=denoised; else tag=clean; fi
  af="$af,atempo=$SPEED"  # after anlmdn: atempo before it segfaults ffmpeg 9.0.1
  ffmpeg -nostdin -v error -i "$src" -vn -af "$af" -c:a pcm_s24le "out/a${n}_pre.wav" -y
  # Per-clip linear gain to TARGET; peaks above -1 dBTP are left to the final limiter, at most PEAKROOM dB.
  # Flow peaks are isolated spikes (1-2% of 10 ms windows, Mochi #1), so 12 dB of limiting on them is inaudible.
  set -- $(lufs "out/a${n}_pre.wav")
  g=$(awk -v i="$1" -v p="$2" -v t="$TARGET" -v r="$PEAKROOM" 'BEGIN{g=t-i; if(g>-1-p+r)g=-1-p+r; printf "%.2f", g}')
  # 20 ms fades only remove cut clicks.
  ffmpeg -nostdin -v error -i "out/a${n}_pre.wav" -af "volume=${g}dB,afade=t=in:d=0.02,afade=t=out:st=$(echo "$d - 0.02" | bc):d=0.02" -c:a pcm_s24le "out/a$n.wav" -y
  rm "out/a${n}_pre.wav"
  echo "s$n $tag $1 LUFS peak $2 -> gain $g dB, cut $a-$b"
  inputs="$inputs -i $src -i out/a$n.wav"
  vf="trim=$a:$b,setpts=(PTS-STARTPTS)/$SPEED,$DELOGO,scale=1080:1920:flags=lanczos,fps=24,format=yuv420p"
  if [ -f "out/overlay$n.png" ]; then
    inputs="$inputs -loop 1 -i out/overlay$n.png"
    fc="$fc[$k:v]$vf[b$n];[$((k+2)):v]format=rgba[o$n];[b$n][o$n]overlay=0:0:shortest=1[v$n];"
    ai=$((k+1)); k=$((k+3))
  else
    fc="$fc[$k:v]$vf[v$n];"; ai=$((k+1)); k=$((k+2))
  fi
  fc="$fc[$ai:a]anull[a$n];"
  cat_in="$cat_in[v$n][a$n]"
done
fc="$fc${cat_in}concat=n=$N:v=1:a=1[outv][outa0];[outa0]alimiter=limit=0.7:attack=1:release=50:level=disabled[outa]"

# shellcheck disable=SC2086
ffmpeg -nostdin -v error $inputs -filter_complex "$fc" -map '[outv]' -map '[outa]' \
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 256k -ar 48000 -ac 2 -movflags +faststart out/story.mp4 -y

set -- $(lufs out/story.mp4)
echo "final $1 LUFS peak $2 dBFS"
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 out/story.mp4
ffmpeg -nostdin -v error -i out/story.mp4 -vf "fps=1,scale=216:-1,tile=6x5" -frames:v 1 frames/story_grid.png -y
