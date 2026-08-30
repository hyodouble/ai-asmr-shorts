# ai-asmr-shorts

Claude 스킬로 AI ASMR 숏폼(유리 과일 커팅류) 기획→프롬프트→렌더 검수→배포까지 자동화.
쇼핑/쿠팡 연동 없음, 상품 구매 없음, 얼굴/목소리 노출 없음.

## 배경

[이 영상](https://www.youtube.com/watch?v=YEkNHXXIK_I)에서 소개된 "Claude + Topview MCP로
상품 링크 하나만 넣으면 쇼핑 쇼츠를 자동 생성"하는 워크플로우(MCP 연결 → 스킬 설치 →
기획/프롬프트/영상/음성 자동 생성 → 렌더 검수)를 뼈대로 가져오되, 목적을 쇼핑 쇼츠가 아닌
**AI ASMR 영상 제작/배포**로 바꿔 적용했다.

## 사용법

1. `SKILL.md` 0단계대로 니치 하나를 `niche.md`에 확정
2. 영상 생성 MCP를 클로드에 연결 (`SKILL.md` 맨 아래 참고)
3. 클로드에서 `/ai-asmr-shorts` 실행 → 소재 한 줄만 입력 → 나머지는 클로드가 기획/프롬프트/검수까지 진행

## 규칙 출처

`SKILL.md`의 니치 고정·오디오 우선·라벨링·완주율 규칙은 2026년 기준 AI ASMR 바이럴 포맷 조사 결과를 반영:

- [lensgo.ai — AI ASMR Videos: How Creators Are Making Viral ASMR with AI (2026)](https://lensgo.ai/blog/ai-asmr-videos-trending-2026)
- [virvid.ai — How to Go Viral with AI TikTok Videos in 2026](https://virvid.ai/blog/viral-ai-tiktok-videos-complete-guide-2026)
