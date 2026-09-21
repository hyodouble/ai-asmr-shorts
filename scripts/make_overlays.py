"""후크 텍스트 + 씬 넘버링 오버레이 PNG 3장 생성 (ffmpeg 빌드에 drawtext가 없어서 PIL로 그린다).

사용법: python3 make_overlays.py <작업폴더> "<후크>" "<씬1>" "<씬2>" "<씬3>"
결과:   <작업폴더>/out/overlay1.png ~ overlay3.png (1080x1920 투명 PNG)

이모지는 넣지 않는다. PIL이 컬러 이모지 폰트를 렌더링하지 못한다 - 이모지는 제목과 첫 댓글에만 쓴다.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def stroked(draw, xy, text, font, stroke=8):
    draw.text(xy, text, font=font, fill="white", stroke_width=stroke,
              stroke_fill=(0, 0, 0, 220), anchor="ma")


def main():
    if len(sys.argv) != 6:
        sys.exit(__doc__)
    workdir, hook, *labels = sys.argv[1:]
    out = Path(workdir) / "out"
    out.mkdir(parents=True, exist_ok=True)

    for i, label in enumerate(labels, 1):
        img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        stroked(d, (W // 2, 210), hook, ImageFont.truetype(FONT, 72))
        stroked(d, (W // 2, 330), label, ImageFont.truetype(FONT, 58))
        img.save(out / f"overlay{i}.png")
    print(f"wrote {len(labels)} overlays to {out}")


if __name__ == "__main__":
    main()
