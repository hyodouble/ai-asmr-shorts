# ai-asmr-shorts

Claude 스킬로 AI ASMR 영상을 기획→프롬프트→렌더 검수→롱폼 조립→배포까지 자동화.
쇼핑/쿠팡 연동 없음, 상품 구매 없음, 얼굴/목소리 노출 없음.

주 배포물은 **수면용 1시간 롱폼**이다. 유니크 클립 20~40개를 이어붙여 마스터를 만들고
ffmpeg로 1시간까지 반복한다. 숏폼은 같은 클립을 재활용해서 나중에 낸다.

## 배경

[이 영상](https://www.youtube.com/watch?v=YEkNHXXIK_I)에서 소개된 "Claude + Topview MCP로
상품 링크 하나만 넣으면 쇼핑 쇼츠를 자동 생성"하는 워크플로우(MCP 연결 → 스킬 설치 →
기획/프롬프트/영상/음성 자동 생성 → 렌더 검수)를 뼈대로 가져오되, 목적을 쇼핑 쇼츠가 아닌
**AI ASMR 영상 제작/배포**로 바꿔 적용했다.

## 진행 상황 (2026-08-31)

- 니치: 물리법칙 파괴형 커팅 ASMR 확정 (`niche.md`)
- 워크플로우: `SKILL.md` 0~8단계 작성 완료. 롱폼 루프 조립(5단계)과 다국어 키워드(7단계) 포함
- 스킬 설치: 로컬 `~/.claude/skills/ai-asmr-shorts/` 설치 완료 → `/ai-asmr-shorts` 호출 가능
- 배포 채널: 유튜브 `SliceverseAI` (핸들 `@buy_guard`, 기존 쿠팡 파트너스 채널 재활용 — 채널명만 변경 완료,
  핸들/배너/프로필/설명은 아직 쿠팡 그대로라 정리 필요)
- 영상 생성 툴: **Veo 3.1 Fast (Google Flow)** 확정. 계정 `hoohihi123123@gmail.com` = Google AI Pro 보유 중이라 추가 결제 없음 (Kling 기각 사유는 `niche.md`)
- 제작한 영상: 0편
- 다음 단계: Google One 멤버십 갱신(2026-09-22 만료) → Flow에서 테스트 클립 1개 → 5개로 루프 파이프라인 검증 → 핸들·배너·설명 정리 → 40개 양산 → 1시간 1편 업로드

## 사용법

1. `SKILL.md` 0단계대로 니치 하나를 `niche.md`에 확정
2. 클로드에서 `/ai-asmr-shorts` 실행 → 소재 한 줄 + 포맷(롱폼/숏폼) 입력
3. 나머지는 클로드가 기획/프롬프트/검수/조립 명령/배포 메타데이터까지 진행
4. 영상 생성은 Google Flow에서 프롬프트를 붙여넣어 실행 (계정 `hoohihi123123@gmail.com` = Google AI Pro)

## 롱폼 조립 요약

```bash
ffmpeg -f concat -safe 0 -i list.txt -c copy master.mp4
ffmpeg -i master.mp4 -af "loudnorm=I=-20:TP=-2:LRA=7,afade=in:st=0:d=0.1,afade=out:st=299.9:d=0.1" -c:v copy master_norm.mp4
ffmpeg -stream_loop -1 -i master_norm.mp4 -t 3600 -c copy 1hour.mp4
```

앞뒤 페이드를 빼면 루프마다 클릭음이 난다. 수면용에서는 이것만으로 실패한다.

## 규칙 출처

`SKILL.md`의 니치 고정·오디오 우선·라벨링·완주율 규칙은 2026년 기준 AI ASMR 바이럴 포맷 조사 결과를 반영:

- [lensgo.ai — AI ASMR Videos: How Creators Are Making Viral ASMR with AI (2026)](https://lensgo.ai/blog/ai-asmr-videos-trending-2026)
- [virvid.ai — How to Go Viral with AI TikTok Videos in 2026](https://virvid.ai/blog/viral-ai-tiktok-videos-complete-guide-2026)
