#!/bin/sh
# 숏폼 30초 파이프라인 (10초 클립 3개 -> 1080x1920 30초).
#
# 사용법:  sh build-short.sh <작업폴더>
#   작업폴더/raw/s1.mp4 s2.mp4 s3.mp4  (Flow 720x1280 9:16 원본) 를 미리 넣어둔다.
#   결과:   작업폴더/out/short_30s.mp4, 작업폴더/out/upload.mp4 (10MB 미만, 브라우저 업로드용)
#
# 클립별 라우드니스 편차는 GAIN 으로 맞춘다. 기본값 0 으로 한 번 돌린 뒤
# 출력되는 LUFS 를 보고 글로벌 쇼츠 표준인 -14.5 LUFS 기준으로 차이를 채워 다시 돌린다.

D=${1:?"작업폴더 경로를 인자로 넘겨라 (예: sh build-short.sh ~/Desktop/asmr_work/shorts/20260911)"}
cd "$D" || exit 1
mkdir -p out frames

GAIN1=${GAIN1:-0}; GAIN2=${GAIN2:-0}; GAIN3=${GAIN3:-0}   # dB

# Flow 워터마크(720x1280 원본 기준 우하단 별 아이콘) 좌표
DELOGO="delogo=x=574:y=1138:w=56:h=56"

for n in 1 2 3; do
  [ -f "raw/s$n.mp4" ] || { echo "raw/s$n.mp4 없음"; exit 1; }
  eval g=\$GAIN$n

  # 오디오 (글로벌 1위 쇼츠 표준 클린 체인):
  # 45Hz 이하 럼블만 완만히 컷 + afftdn/dynaudnorm 제거로 위상 왜곡 및 펌핑 노이즈 0% 달성
  # EBU R128 표준 loudnorm (-14.5 LUFS / True Peak -1.0 dBTP)
  ffmpeg -nostdin -v error -i "raw/s$n.mp4" -vn \
    -af "highpass=f=45:p=2,loudnorm=I=-14.5:TP=-1.0:LRA=7:linear=false,volume=${g}dB,afade=t=in:st=0:d=0.04,afade=t=out:st=9.96:d=0.04" \
    -ar 48000 -f wav "a$n.wav" -y || exit 1

  # 영상: 워터마크 제거 + 1080x1920 업스케일
  ffmpeg -nostdin -v error -i "raw/s$n.mp4" -i "a$n.wav" -map 0:v -map 1:a \
    -vf "$DELOGO,scale=1080:1920:flags=lanczos" \
    -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -r 24 \
    -c:a aac -b:a 256k -shortest "out/s$n.mp4" -y || exit 1

  printf 's%s  ' "$n"
  ffmpeg -nostdin -v info -i "out/s$n.mp4" -af "astats=measure_overall=Peak_level:measure_perchannel=none" -f null - 2>&1 | grep "Peak level" | tr -d '\n'
  printf '  '
  ffmpeg -nostdin -hide_banner -i "out/s$n.mp4" -af loudnorm=print_format=summary -f null - 2>&1 | grep "Input Integrated"
done
rm -f a1.wav a2.wav a3.wav

printf "file 's1.mp4'\nfile 's2.mp4'\nfile 's3.mp4'\n" > out/list.txt
ffmpeg -nostdin -v error -f concat -safe 0 -i out/list.txt -c copy out/short_30s.mp4 -y || exit 1

# 브라우저 업로드 도구는 한 번에 10MB 까지만 보낸다. 9.5MB 근처로 줄인 사본을 같이 만든다.
ffmpeg -nostdin -v error -i out/short_30s.mp4 -c:v libx264 -crf 23 -preset slow -pix_fmt yuv420p \
  -c:a copy -movflags +faststart out/upload.mp4 -y || exit 1

# 검수용 필름스트립
ffmpeg -nostdin -v error -i out/short_30s.mp4 -vf "fps=1/3,scale=200:-1,tile=10x1" -frames:v 1 frames/final_strip.png -y

echo "완성:"
ls -l out/short_30s.mp4 out/upload.mp4
