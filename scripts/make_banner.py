"""Mochi YouTube banner (2048x1152, text inside the 1235x338 all-device safe area).
Usage: ffmpeg -ss 1 -i mochi_48.mp4 -frames:v 1 <dir>/f1.png; python3 scripts/make_banner.py <dir> characters/mochi/youtube-banner.jpg
"""
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import sys
S, out = sys.argv[1], sys.argv[2]
W, H = 2048, 1152
F = '/Users/hyo/issuecatch/fonts/'
# kitchen strip between the burned caption and the animals' heads, scaled to cover the banner
bg = Image.open(f'{S}/f1.png').convert('RGB').crop((0, 318, 1080, 820))
k = max(W / bg.width, H / bg.height)
bg = bg.resize((round(bg.width * k), round(bg.height * k)), Image.LANCZOS)
l, t = (bg.width - W) // 2, (bg.height - H) // 2
bg = bg.crop((l, t, l + W, t + H)).filter(ImageFilter.GaussianBlur(7))
bg = Image.blend(bg, Image.new('RGB', (W, H), (255, 244, 228)), 0.25)

# safe area for all devices: centre 1235x338
sx, sy, sw, sh = (W - 1235) // 2, (H - 338) // 2, 1235, 338
d = ImageDraw.Draw(bg, 'RGBA')
d.rounded_rectangle((sx - 10, sy - 10, sx + sw + 10, sy + sh + 10), 48, fill=(255, 250, 242, 225))

# Mochi portrait, round
p = Image.open('/Users/hyo/ai-asmr-shorts/characters/mochi/mochi_character_portrait.jpg').convert('RGB')
side = min(p.size); p = p.crop(((p.width - side) // 2, 0, (p.width + side) // 2, side)).resize((290, 290), Image.LANCZOS)
m = Image.new('L', p.size, 0); ImageDraw.Draw(m).ellipse((0, 0, 289, 289), fill=255)
px, py = sx + 30, sy + (sh - 290) // 2
d.ellipse((px - 8, py - 8, px + 298, py + 298), fill=(200, 40, 40, 255))   # red ring = Mochi's scarf
bg.paste(p, (px, py), m)

tx = px + 290 + 60
big = ImageFont.truetype(F + 'Pretendard-ExtraBold.ttf', 92)
mid = ImageFont.truetype(F + 'Pretendard-Medium.ttf', 52)
d.text((tx, sy + 88), 'Cozy Mochi Story', font=big, fill=(60, 38, 28))
d.text((tx + 4, sy + 204), 'Tiny heroes, big appetites', font=mid, fill=(170, 40, 40))
assert d.textbbox((tx, sy + 88), 'Cozy Mochi Story', font=big)[2] <= sx + sw - 20, 'title leaves safe area'
bg.save(out, quality=92)
print(out)
