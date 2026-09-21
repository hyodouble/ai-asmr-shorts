#!/bin/sh
# 씬별 오버레이 합성 -> concat -> 1.7배속 17.6초 (SKILL 알고리즘 규칙 #4, #5)
# 체인 overlay+enable 은 두 번째 이후 오버레이가 통째로 빠지는 일이 있어, 씬마다 따로 굽는다.
set -e
D=${1:?"작업폴더 경로를 인자로 넘겨라 (예: sh finish-short.sh ~/Desktop/asmr_work/shorts/20260921)"}
cd "$D" || exit 1
SP=${SP:-1.7}
G=${GFIN:-0}
LIMIT=${LIMIT:-0.5}

for n in 1 2 3; do
  ffmpeg -nostdin -v error -i "out2/s$n.mp4" -i "out/overlay$n.png" \
    -filter_complex "[0:v][1:v]overlay=0:0[v]" -map "[v]" \
    -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -r 24 -an -t 10 \
    "out2/t$n.mp4" -y
done

printf "file 't1.mp4'\nfile 't2.mp4'\nfile 't3.mp4'\n" > out2/tlist.txt
ffmpeg -nostdin -v error -f concat -safe 0 -i out2/tlist.txt -c copy out2/master_txt.mp4 -y

# AAC 스트림을 그대로 atempo 에 물리면 배속이 덜 먹는다(1.7 지정에 실측 1.38). PCM 으로 뽑아 쓴다.
ffmpeg -nostdin -v error -i out2/master_30s.mp4 -map 0:a -c:a pcm_s16le out2/master.wav -y

ffmpeg -nostdin -v error -i out2/master_txt.mp4 -i out2/master.wav \
  -filter_complex "[0:v]setpts=PTS/$SP,fps=24[v];[1:a]atempo=$SP,volume=${G}dB,alimiter=limit=${LIMIT}:level=disabled[a]" \
  -map "[v]" -map "[a]" \
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p \
  -c:a aac -b:a 256k -movflags +faststart out/short_final.mp4 -y

echo "duration: $(ffprobe -v error -show_entries format=duration -of csv=p=0 out/short_final.mp4)"
ffmpeg -nostdin -hide_banner -i out/short_final.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I:|LRA:|Peak:)"
