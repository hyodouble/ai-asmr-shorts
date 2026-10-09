from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FONT = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 76)
# One caption per scene (Tofu rule 2026-10-08), top of frame; wrap past 960 px.
CAPTIONS = ("A baby seal was crying all alone...", "Tofu promised to help her.",
            "Where is her mom?", "Let's call her together!",
            "Someone called back!", "Thank you, Tofu.")

def wrap(text):
    words, lines = text.split(), [""]
    for w in words:
        t = (lines[-1] + " " + w).strip()
        if FONT.getlength(t) > 960 and lines[-1]:
            lines.append(w)
        else:
            lines[-1] = t
    return "\n".join(lines)

out = Path(__file__).parent / "out"
out.mkdir(exist_ok=True)
for i, text in enumerate(CAPTIONS, 1):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(img).multiline_text((W // 2, 230), wrap(text), font=FONT, fill="white", anchor="ma",
                                       align="center", stroke_width=8, stroke_fill=(0, 0, 0, 220), spacing=12)
    img.save(out / f"overlay{i}.png")
