"""스토리 영상 마지막 몇 초에 얹는 팔로우 유도 자막 PNG (2026-10-25).

사용법: python3 make_endcard.py <작업폴더> <다음 회차 번호>
결과:   <작업폴더>/out/endcard.png (1080x1920 투명 PNG). build-story.sh 가 있으면 끝 ENDSEC 초에 얹는다.

조회수에 비해 팔로우가 안 늘어서, 연재물이라는 걸 영상 안에서 알린다.
이모지는 넣지 않는다. PIL이 컬러 이모지 폰트를 렌더링하지 못한다.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    workdir, nxt = sys.argv[1], int(sys.argv[2])
    lines = [f"To be continued in #{nxt}", "Follow so you don't miss it"]
    fonts = [ImageFont.truetype(FONT, 70), ImageFont.truetype(FONT, 56)]

    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # 장면 자막(위쪽)과 겹치지 않게 아래 1/3, 틱톡·릴스 하단 UI 위에 둔다.
    y = 1380
    boxes = [d.textbbox((W // 2, 0), t, font=f, anchor="ma") for t, f in zip(lines, fonts)]
    hs = [b[3] - b[1] for b in boxes]
    width = max(b[2] - b[0] for b in boxes) + 100
    height = sum(hs) + 30 + 80
    d.rounded_rectangle(((W - width) // 2, y - 40, (W + width) // 2, y - 40 + height), radius=40, fill=(0, 0, 0, 150))
    for t, f, h in zip(lines, fonts, hs):
        d.text((W // 2, y), t, font=f, fill="white", anchor="ma")
        y += h + 30

    out = Path(workdir) / "out"
    out.mkdir(parents=True, exist_ok=True)
    img.save(out / "endcard.png")
    print(f"wrote {out / 'endcard.png'}")


if __name__ == "__main__":
    main()
