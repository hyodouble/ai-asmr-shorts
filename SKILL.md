---
name: ai-asmr-shorts
description: 상품/쿠팡 없이 AI로 ASMR 영상을 만든다. 수면용 1시간 롱폼(10초 클립 루프)과 숏폼 둘 다 대응하고, 기획·씬 프롬프트·렌더 검수·롱폼 조립·배포 메타데이터까지 생성한다.
---

# AI ASMR — 수면용 롱폼

Google Flow의 **Omni 1.1 Flash**로 10초 클립을 여러 개 뽑아, 이어붙이고 반복해 1시간 수면용 영상을 만든다.
사람이 보다가 잠드는 게 목적이다. 그래서 규칙 하나가 다른 모든 규칙을 이긴다: **자던 사람을 깨우지 않는다.**

## 니치 — 스퀴시 ASMR (2026-09-01 확정)

두 갈래를 같은 채널에서 섞는다. 둘 다 "부드러운 물체를 천천히 누르면 잔 소리가 촘촘히 난다"는 한 가지 청각 경험이라 톤이 안 튄다.

1. **타바 스퀴시(taba squishy)** — 투명 필름에 말랑한 반죽을 봉하고 공기 방울을 주입한 장난감.
   누르면 방울이 밀려 다니며 뽀글거리고 작은 방울이 톡톡 터진다. TikTok·YouTube에 이미 1시간 수면 버전이 있을 만큼 검증된 포맷.
2. **왁뿌볼** — 말랑이 겉에 얇은 왁스 껍질을 굳힌 국내 유행 완구. 누르면 껍질이 잘게 깨지며 와그작거린다.

두 소재의 공통점이 채널 정체성이다: **잔 소리가 촘촘히 이어진다.** 큰 소리 하나로 터뜨리는 연출은 이 채널에 없다.

## 도구·계정

- 생성: Google Flow — https://labs.google/fx/tools/flow
- 계정: `hoohihi123123@gmail.com` (Google AI Pro). 브라우저 첫 프로필(`gksgytjr1027@gmail.com`)은 무료 티어라 모델이 안 나온다. 매번 로그인 계정 확인
- 모델: **Omni 1.1 Flash**. 720p / 10초 / x1 = **15크레딧**. Veo 3.1은 쓰지 않는다(같은 프롬프트에서 재질을 제멋대로 바꾼다)
- Flow UI가 자주 먹통이다. 프롬프트를 넣은 뒤 **스크린샷으로 텍스트가 박혔는지 확인하고 전송**할 것. 로딩 중 클릭은 씹힌다
- 후처리: ffmpeg, python(numpy). 스킬 폴더의 `detone.py` / `tonecheck.py`

## 1단계 — 프롬프트는 사용자 승인 후 입력한다

크레딧이 곧 돈이다. 씬 목록과 프롬프트 전문을 먼저 보여주고, 승인받은 뒤에 Flow에 넣는다.

## 2단계 — 프롬프트 구성

한 문단으로 쓴다. **A·D·E는 모든 클립에서 글자 그대로 고정**, B·C만 바꾼다. 고정 블록이 흔들리면 클립마다 톤이 튀어 루프에서 티가 난다.

**A. 카메라 (고정)**
```
Extreme close-up, macro lens, static locked-off camera, single continuous take, slow motion.
```

**B. 피사체 (변주)** — 재질을 반드시 명시한다. 안 쓰면 모델이 제 사전지식대로 다른 물건을 만든다.
```
Two human fingers slowly press a <색> <형태> <소재 설명> resting on <바닥>, <배경>.
```

**C. 동작 (변주하되 규칙 고정)** — 손이 **10초 내내 멈추지 않는다**고 반드시 쓴다. 안 쓰면 중간에 손이 멎고 무음 구간이 생긴다.
```
The fingers never stop moving for the entire clip: they press, roll and knead without pause,
so <잔 소리가 나는 현상> continues from the first frame to the last.
```

**D. 오디오 (고정)** — ASMR은 소리가 시청 이유의 70%다. 반드시 별도 문장으로.
```
Audio is the most important part of this video: <소재별 잔 소리>, hundreds of tiny overlapping
sounds at the same steady level from the first frame to the last, with no silent gaps.
Recorded very close, like an ASMR microphone right next to the object, soft and detailed.
Everything stays evenly loud the whole time - no single loud pop, no sudden burst, no impact,
no ringing, no bell, no chime. No music, no voice.
```

**E. 조명·금지 (고정)**
```
Soft diffused light from the upper left, even and steady.
No text, no on-screen captions, no faces, no speech, no jump cuts, no camera movement,
no morphing, no vanishing objects.
```

### 소리 원칙 (1번 규칙)

시청자는 자려고 트는 사람이다. 조용해서 볼륨을 올려둔 채 잠들었는데 피크가 한 번 터지면 그대로 깬다. 한 번 깨우면 그 채널은 다시 안 튼다.

- 좋은 소리 = **잔 소리가 촘촘히, 같은 크기로 이어지는 것**. 방울 뽀글거림, 왁스 사각거림, 반죽 눌리는 소리
- 나쁜 소리 = **레벨 점프**. 큰 파열음 하나, 종소리, 금속 울림, 정적 뒤의 갑작스런 소리
- 방울 터지는 소리는 넣는다. 단 `many tiny bubbles popping softly and continuously`처럼 **작고 촘촘하게** 지정한다
- **손바닥으로 내려누르는 동작**은 그림에 변화를 주니 몇 클립 섞는다. 단 타격이 아니라 압착으로 쓴다:
  `a slow cushioned press into the soft dough, not a hard hit` + `a broad soft muffled squelch of dough spreading, low and rounded, never a slap or a clap or a thud`
  이 문구 없이 "내려친다"만 쓰면 찰싹 소리가 붙어서 수면용으로 못 쓴다

## 3단계 — 씬 변주 (1시간 지루함 방지)

같은 그림이 반복되면 금방 이탈한다. 20~24클립을 아래 4축에서 조합이 안 겹치게 뽑는다.

| 축 | 값 |
|---|---|
| 소재 | 타바 스퀴시(방울) · 왁뿌볼(왁스 껍질) · 필름 속 반죽 · 젤리 코어 |
| 색 | 라벤더 · 민트 · 살구 · 크림 · 연회색 · 연분홍 |
| 바닥 | 린넨 천 · 대리석 · 자작나무 · 코르크 · 종이 · 벨벳 |
| 동작 | 두 손가락 누르기 · 손바닥 굴리기 · 손톱으로 눌러 밀기 · 방울 몰기 · 천천히 접기 · **손바닥으로 내려누르기** |

**바닥이 소리를 바꾼다.** 딱딱한 나무·대리석에 조각이 떨어지면 울린다. 조각이 떨어지는 소재는 **천 위에 놓는다.**

## 4단계 — 렌더 검수 (승인 전 필수)

- 손가락 개수 정상인가. 손이 프레임 안에 있는가
- 소재가 중간에 다른 물건으로 안 바뀌는가 (색·질감 유지)
- 손이 10초 내내 움직이는가. 무음 구간 없는가
- 마지막 2초에 물체가 사라지거나 다시 붙지 않는가
- 다음 클립 첫 프레임과 밝기 차가 심하지 않은가 (경계 YAVG 차 8 이하)

### 오디오 검수 — 귀로만 하지 말 것

**모델은 프롬프트 금지어를 무시하고 벨/차임 효과음을 넣는다.** `no chimes, no bells, no ringing`을 넣어도 3회 연속 들어갔다.
프롬프트를 손질해 재생성하지 말 것 — 크레딧만 나간다. **후처리로 지운다.**

```bash
ffmpeg -i clip.mp4 -ac 1 -ar 48000 -c:a pcm_s16le clip.wav -y
python tonecheck.py clip.wav        # 톤 프레임 수 / 최대 prominence
python detone.py clip.wav clean.wav # 톤 성분 제거
```

- 벨은 스펙트로그램에서 **좁고 긴 가로줄**(한 주파수가 0.1~0.6초 지속). 왁스 크랙·방울 소리는 광대역이라 줄이 안 생긴다
- 실측 제거량: 2109 Hz -36 dB, 6199 Hz -22 dB, 4805 Hz -25 dB. 광대역 RMS 변화 0.3 dB라 잔 소리는 안 깎인다
- 빈 3개 이상 넓게 솟은 피크는 안 건드린다. 벨이 아니라 진짜 파열음이다
- **라우드니스는 loudnorm 이후에 잰다.** 원본 LRA 12~21도 처리 후 2~6으로 내려온다. 처리 후 **LRA > 10 탈락**

## 5단계 — 후처리 (클립마다)

```bash
ffmpeg -i in.mp4 -i clean.wav -map 0:v -map 1:a \
  -vf "delogo=x=1130:y=570:w=60:h=56,scale=1920:1080:flags=lanczos" \
  -af "highpass=f=120:p=2,lowpass=f=11000:p=2,afftdn=nr=18:nf=-45,acompressor=threshold=-45dB:ratio=12:attack=5:release=500,loudnorm=I=-16:TP=-2:LRA=5,volume=<부족분>dB,alimiter=limit=0.89:level=disabled,afade=t=in:st=0:d=0.04,afade=t=out:st=9.96:d=0.04" \
  -c:v libx264 -crf 16 -preset medium -c:a aac -b:a 192k out.mp4
```

- **워터마크**: 한국 계정은 Flow 가시 워터마크가 강제다(토글 잠김). 720p 좌표가 위 `delogo` 값. 1080p 업스케일본은 `x=1695:y=855:w=90:h=84`
- **컴프레서는 loudnorm 앞에.** 원본이 -37~-48 LUFS로 작고 들쭉날쭉해 뒤에 걸면 못 잡는다
- **`alimiter`는 기본값이 `level=true`라 리밋 후 출력을 도로 올린다.** `limit=0.5`를 걸고도 피크가 +0.6 dBFS로 클리핑났다. 반드시 `level=disabled`
- loudnorm 단독으로는 -22 LUFS까지밖에 안 올라온다. 측정 → `volume` 보정 → 리미터 순서
- **소음 제거는 증폭 전에.** 원본이 -37~-48 LUFS라 20 dB씩 올려야 하는데, 그 전에 안 자르면 잡음도 같이 올라와서 "소음이 심하다"가 된다.
  실측 대역 분포: 신호는 **1~10 kHz**에만 있다. 20~200 Hz는 상시 럼블(조용한 구간과 큰 구간 차이가 8.7 dB뿐), 10 kHz 위는 히스(차이 11.2 dB).
  `highpass=f=120` + `lowpass=f=11000` + `afftdn=nr=18:nf=-45` 로 SNR 29 → 39 dB. 신호 피크는 그대로다
- **라우드니스 목표는 -20 ~ -24 LUFS.** 원본이 작아 -16까지 밀면 리미터가 계속 물려 소리가 뭉갠다.
  수면용은 시청자가 볼륨을 직접 맞추니 조용한 쪽이 낫다. 크게 만들려다 노이즈를 같이 키우지 말 것
- **이음새는 클립마다 40ms 페이드.** 없으면 경계에서 -37~-43 dBFS 샘플 점프(틱 소리), 페이드 후 -120 dBFS
- 개별 클립 원본은 전부 보관한다. 숏폼으로 재활용한다

## 6단계 — 1시간 조립

20클립 × 10초 = 200초 마스터. 순서를 섞은 마스터 2종(A·B)을 번갈아 붙여 6분 40초 사이클 → 9회 반복 = 1시간.

```bash
ffmpeg -f concat -safe 0 -i listA.txt -c copy masterA.mp4
ffmpeg -f concat -safe 0 -i listB.txt -c copy masterB.mp4
ffmpeg -f concat -safe 0 -i cycle.txt -c copy cycle.mp4
ffmpeg -i cycle.mp4 -af "loudnorm=I=-16:TP=-2:LRA=5" -c:v copy cycle_norm.mp4
ffmpeg -stream_loop -1 -i cycle_norm.mp4 -t 3600 -c copy 1hour.mp4
```

- `-c copy`는 클립 코덱/해상도/fps가 전부 같아야 동작한다
- YouTube 반복 콘텐츠 정책 리스크가 있으니 사이클은 5분 이상으로 간다
- 최종본도 한 번 더 loudnorm을 통과시킨다. 개별 클립이 통과해도 이어붙이면 편차가 생긴다

## 7단계 — 업로드

- **합성 콘텐츠 라벨 필수.** YouTube "변경되었거나 합성된 콘텐츠" 토글. 누락 적발 시 도달률 페널티·삭제 사례 있음
- 제목은 영어 하나로.
- **다국어는 설명란이 아니라 Studio "자막" 항목에서 처리한다** (2026-09-11 정정 — 예전에 있던
  "설명 하단 Keywords 한 줄" 규칙은 실제로 쓰인 적이 없어 폐기됨). Studio 좌측 자막 → 언어 추가 →
  언어별 "제목 및 설명" 번역을 게시. 자막 파일(SRT)은 안 올림 — 말이 없는 영상이라 불필요.
  고정 5개 언어: 영어(원본) · 한국어 · 일본어 · 스페인어 · 포르투갈어. 원본 영어 설명도 반드시 채울 것
  (안 채우면 영어권 시청자에게 설명 자체가 안 보임).

## 8단계 — 크레딧

| 항목 | 소모 |
|---|---|
| 10초 클립 1개 (720p, x1) | 15 |
| 20클립 1편 | 300 |
| 검수 탈락 재생성 30% 감안 | 약 390 |

Google AI Pro 월 1,000 크레딧. 이월 없이 결제 주기 끝에 소멸하니 월말에 남으면 다음 편 클립을 미리 뽑는다.
멤버십 만료일 확인(2026-09-22).

## 9단계 — 쇼츠 세로 변환 (가로 소스 구제 시, 2026-09-12 발견)

Flow에서 9:16으로 바로 안 뽑고 가로(16:9) 소스만 있을 때(옛 롱폼 클립 재활용 등) 살리는 법.

- **가로 그대로 올리면 유튜브가 "동영상"(롱폼)으로 분류함 — Shorts 탭에 안 걸림.** 반드시 9:16으로
  재렌더링 후 업로드. `youtube.com/shorts/...` 링크가 뜨는지로 확인 가능(가로면 `youtu.be/...`만 뜸).
- 변환 방식 둘 중 하나:
  - **블러 배경 패딩**(원본 전체 보존, 위아래 블러바) — 화면에 빈 공간 생겨 몰입감 낮음.
  - **풀블리드 센터크롭**(양옆 잘라 꽉 채움) — 몰입감·완주율 더 좋음. 단, 피사체가 화면 중앙에
    있는 구도(매크로 클로즈업류)에서만 안전. 양손 쓰는 씬은 반대쪽 손끝이 프레임 밖으로 걸릴 수 있음.
  - 크롭 예시(1280x720 소스 → 1080x1920): `crop=405:720:437:0,scale=1080:1920:flags=lanczos`
- 수요는 크롭이 더 높음 — 가능하면 크롭 우선, 손 잘리는 구도만 블러 패딩으로 예외 처리.

## Studio 업로드 함정

- **AI 사용(합성 콘텐츠) / 유료 프로모션 질문이 기본으로 숨어있음.** 세부정보 단계 "연령 제한" 아래
  "자세히 보기"를 펼쳐야 나옴 — 안 펼치면 그 질문 자체를 놓치고 넘어감.
- "다음" 버튼은 필수 항목 중 답 안 한 게 있으면 그 위치로 자동 스크롤해줌 — 놓쳤어도 복구 가능.
- 잘못 올린 영상 삭제: 체크박스 선택 → 추가 작업 → 완전삭제 → "되돌릴 수 없음" 체크 → 완전삭제.
  삭제 처리에 몇 초~십여 초 걸림, 목록 새로고침해서 확인.
