#!/bin/sh
# 쇼츠 표준 체인(SKILL #9): highpass=45 + 2패스 loudnorm(linear) -14.5 LUFS / TP -1.0 + 안전 리미터.
# 입력 rawfx/sN.mp4 (foley 레이어 완료) -> out2/sN.mp4
set -e
D=${1:?"작업폴더 경로를 인자로 넘겨라 (예: sh build-short2.sh ~/Desktop/asmr_work/shorts/20260921)"}
cd "$D" || exit 1
mkdir -p out2
DELOGO="delogo=x=574:y=1138:w=56:h=56"

# 조용한 원본은 16 dB 넘게 올려야 해서 크레스트를 줄여야 -14.5에 닿는다.
# 트랜지언트 보존을 위해 ratio 2.5:1 / attack 20ms 로만 건다 (10:1 라디오 압축 금지 규칙 준수).
# 원본이 -44 ~ -48 LUFS로 매우 조용하면 컴프레서 스레숄드에 신호가 닿지 않는다.
# 클립별로 -20 LUFS 근처까지 선형 프리게인을 먼저 먹인 뒤 압축한다.
lufs() { ffmpeg -nostdin -hide_banner -i "$1" -af loudnorm=print_format=summary -f null - 2>&1 | awk '/Input Integrated/{print $3}'; }

for n in 1 2 3; do
  ci=$(lufs "rawfx/s$n.mp4")
  PG=$(python3 -c "print(round(-20-($ci),2))")
  PRE="volume=${PG}dB,highpass=f=45:p=2,acompressor=threshold=-26dB:ratio=3:attack=20:release=250"
  echo "s$n pre-gain=$PG dB"
  json=$(ffmpeg -nostdin -hide_banner -i "rawfx/s$n.mp4" -vn \
    -af "$PRE,loudnorm=I=-14.5:TP=-1.0:LRA=7:print_format=json" -f null - 2>&1 \
    | sed -n '/^{/,/^}/p')
  set -- $(python3 -c "
import json,sys
d=json.loads('''$json''')
print(d['input_i'],d['input_tp'],d['input_lra'],d['input_thresh'],d['target_offset'])")
  I=$1; TP=$2; LRA=$3; TH=$4; OFF=$5
  eval g=\${GAIN$n:-0}
  echo "s$n measured I=$I TP=$TP LRA=$LRA"
  ffmpeg -nostdin -v error -i "rawfx/s$n.mp4" -vn \
    -af "$PRE,loudnorm=I=-14.5:TP=-1.0:LRA=7:measured_I=$I:measured_TP=$TP:measured_LRA=$LRA:measured_thresh=$TH:offset=$OFF:linear=true,volume=${g}dB,alimiter=limit=${LIMIT:-0.75}:level=disabled,afade=t=in:st=0:d=0.04,afade=t=out:st=9.965:d=0.04" \
    -ar 48000 -f wav "out2/a$n.wav" -y

  ffmpeg -nostdin -v error -i "rawfx/s$n.mp4" -i "out2/a$n.wav" -map 0:v -map 1:a \
    -vf "$DELOGO,scale=1080:1920:flags=lanczos" \
    -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -r 24 \
    -c:a aac -b:a 256k -shortest "out2/s$n.mp4" -y

  printf 's%s  ' "$n"
  ffmpeg -nostdin -v info -i "out2/s$n.mp4" -af "astats=measure_overall=Peak_level:measure_perchannel=none" -f null - 2>&1 | grep "Peak level" | tr -d '\n'
  printf '  '
  ffmpeg -nostdin -hide_banner -i "out2/s$n.mp4" -af loudnorm=print_format=summary -f null - 2>&1 | grep "Input Integrated"
done

printf "file 's1.mp4'\nfile 's2.mp4'\nfile 's3.mp4'\n" > out2/list.txt
ffmpeg -nostdin -v error -f concat -safe 0 -i out2/list.txt -c copy out2/master_30s.mp4 -y
echo "마스터: out2/master_30s.mp4 (다음 단계 scripts/finish-short.sh)"
