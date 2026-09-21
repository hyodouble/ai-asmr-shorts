#!/bin/sh
# AI 원본 오디오 위에 CC0 foley를 깐다 (SKILL #6). 기본 -16 dB, FOLEY_DB 로 조절한다.
# BED 는 소재에 맞춰 고른다: 슬라이드/입수면 물 흐름, 스퀴시 프레스면 젖은 천 짜기.
# 소스: archive.org Designers-Choice-Collection-Water (CC0)
set -e
D=${1:?"작업폴더 경로를 인자로 넘겨라 (예: sh mix-foley.sh ~/Desktop/asmr_work/shorts/20260921)"}
cd "$D" || exit 1
mkdir -p rawfx
BED=${BED:-foley/wet_wring.wav}
FOLEY_DB=${FOLEY_DB:--16}
lufs() { ffmpeg -nostdin -hide_banner -i "$1" -af loudnorm=print_format=summary -f null - 2>&1 | awk '/Input Integrated/{print $3}'; }
bi=$(lufs "$BED")

for n in 1 2 3; do
  ci=$(lufs raw/s$n.mp4)
  bg=$(python3 -c "print(round($ci-$bi+($FOLEY_DB),2))")
  st=$(python3 -c "print([2.0,12.0,22.0][$n-1])")
  echo "s$n clip=$ci bed_gain=$bg"
  ffmpeg -nostdin -v error -i raw/s$n.mp4 -ss $st -t 10.005 -i "$BED" \
    -filter_complex "[1:a]volume=${bg}dB,afade=t=in:st=0:d=0.3,afade=t=out:st=9.7:d=0.3[bed];\
[0:a][bed]amix=inputs=2:normalize=0:duration=first[a]" \
    -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 256k -ar 48000 rawfx/s$n.mp4 -y
done
ls -l rawfx/
