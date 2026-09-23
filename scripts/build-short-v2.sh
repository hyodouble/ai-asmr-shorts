#!/bin/sh
# 숏폼 v2 파이프라인 (10초 클립 N개 -> 1080x1920, 질문/번호/CTA 자막 굽기).
#
# 사용법:  QUESTION="Which bed would you sleep in?" LABELS="Bubble Wrap|Clam Shell|..." sh build-short-v2.sh <작업폴더>
#   작업폴더/raw/s1.mp4 ... sN.mp4 (Flow 720x1280 9:16 원본) 를 미리 넣어둔다.
#   결과:   작업폴더/out/short.mp4, 작업폴더/out/upload.mp4 (10MB 미만)
#
# 30초 3클립 버전은 build-short.sh. v2는 60~90초 6~9클립용이고 자막을 굽는다는 점이 다르다.
# 클립마다 -14.5 LUFS 로 자동 게인한다(SKILL 규칙 9). 편차가 1 dB 넘으면 GAIN1..GAIN9 로 미세 보정.
# 손잡이: LIMIT(리미터, 기본 0.75, TP -1 넘으면 0.7) / QSIZE(질문 글자, 40자면 42) / UPCRF(업로드본, 60초면 28)

D=${1:?"작업폴더 경로를 인자로 넘겨라"}
cd "$D" || exit 1
mkdir -p out frames

QUESTION=${QUESTION:-"Which one would you choose?"}
CTA=${CTA:-"COMMENT YOUR PICK"}
FONT=${FONT:-"C\\:/Windows/Fonts/arialbd.ttf"}

DELOGO="delogo=x=574:y=1138:w=56:h=56"

N=0
for f in raw/s*.mp4; do N=$((N+1)); done
[ "$N" -gt 0 ] || { echo "raw/s*.mp4 없음"; exit 1; }

: > out/list.txt
for n in $(seq 1 "$N"); do
  [ -f "raw/s$n.mp4" ] || { echo "raw/s$n.mp4 없음"; exit 1; }
  eval g=\${GAIN$n:-0}

  # SKILL 규칙 9: afftdn 금지, -14.5 LUFS 목표. 컴프 뒤 실측해서 게인 자동 계산, GAINn 은 미세 보정
  PRE="highpass=f=45:p=2,acompressor=threshold=-26dB:ratio=2.5:attack=20:release=250"
  m=$(ffmpeg -nostdin -hide_banner -i "raw/s$n.mp4" -vn -af "$PRE,loudnorm=print_format=summary" -f null - 2>&1 | awk '/Input Integrated/{print $3}')
  auto=$(python -c "print(round(-14.5-($m)+($g),2))")
  ffmpeg -nostdin -v error -i "raw/s$n.mp4" -vn \
    -af "$PRE,volume=${auto}dB,alimiter=limit=${LIMIT:-0.75}:attack=5:release=60:level=disabled,afade=t=in:st=0:d=0.04,afade=t=out:st=9.96:d=0.04" \
    -ar 48000 -f wav "a$n.wav" -y || exit 1

  # 질문(상단 고정) + 번호(질문 아래) + 마지막 클립 뒤 2초에 CTA
  TXT="drawtext=fontfile='$FONT':text='$QUESTION':fontcolor=white:fontsize=${QSIZE:-58}:box=1:boxcolor=black@0.55:boxborderw=22:x=(w-text_w)/2:y=150"
  TXT="$TXT,drawtext=fontfile='$FONT':text='$n. $(echo "$LABELS" | cut -d'|' -f$n)':fontcolor=white:fontsize=84:box=1:boxcolor=black@0.55:boxborderw=26:x=(w-text_w)/2:y=270"
  if [ "$n" = "$N" ]; then
    TXT="$TXT,drawtext=fontfile='$FONT':text='$CTA':fontcolor=white:fontsize=62:box=1:boxcolor=black@0.6:boxborderw=24:x=(w-text_w)/2:y=h-380:enable='gte(t,8)'"
  fi

  ffmpeg -nostdin -v error -i "raw/s$n.mp4" -i "a$n.wav" -map 0:v -map 1:a \
    -vf "$DELOGO,scale=1080:1920:flags=lanczos,$TXT" \
    -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -r 24 \
    -c:a aac -b:a 256k -shortest "out/s$n.mp4" -y || exit 1

  printf 's%s  ' "$n"
  ffmpeg -nostdin -hide_banner -i "out/s$n.mp4" -af loudnorm=print_format=summary -f null - 2>&1 | grep "Input Integrated"
  echo "file 's$n.mp4'" >> out/list.txt
  rm -f "a$n.wav"
done

ffmpeg -nostdin -v error -f concat -safe 0 -i out/list.txt -c copy out/short.mp4 -y || exit 1
ffmpeg -nostdin -v error -i out/short.mp4 -c:v libx264 -crf ${UPCRF:-28} -preset slow -pix_fmt yuv420p \
  -c:a copy -movflags +faststart out/upload.mp4 -y || exit 1
ffmpeg -nostdin -v error -i out/short.mp4 -vf "fps=1/5,scale=200:-1,tile=12x1" -frames:v 1 frames/final_strip.png -y

echo "완성:"
ls -l out/short.mp4 out/upload.mp4
