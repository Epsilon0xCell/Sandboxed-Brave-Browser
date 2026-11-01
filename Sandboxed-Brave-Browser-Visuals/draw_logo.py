#!/usr/bin/env python3
"""Sandboxed-Brave-Browser logo: a toll bell hanging in a wooden frame, two posts, a
crossbar, and a bell swung between them, a blunt silhouette with a single notch cut out
of the bell mouth so the shape survives shrinking. Forest green timber, gold bell, one
mushroom red dot for the clapper. Below the frame the name is set in Anek Malayalam,
letterspaced wide like words chalked across a toll board, cream on green, with a hairline
of gold under the whole name. No goat head, no bridge arch, no shield, no lion."""
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np
W = H = 1024
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
GREEN = (26, 54, 36); TIMBER = (96, 70, 42); GOLD = (216, 168, 74); CREAM = (240, 232, 200); RED = (198, 52, 40)
img = Image.new("RGB", (W, H), GREEN); d = ImageDraw.Draw(img, "RGBA")
# frame: two posts and a crossbar
d.rectangle([268, 120, 316, 660], fill=TIMBER)
d.rectangle([708, 120, 756, 660], fill=TIMBER)
d.rectangle([228, 96, 796, 152], fill=TIMBER)
d.rectangle([228, 96, 796, 110], fill=(116, 86, 52))
for px in (292, 732):  # pegs
    d.ellipse([px - 9, 200, px + 9, 218], fill=(60, 42, 24))
# bell swung between the posts, notch cut out of the mouth
cx = 512
d.line([(cx, 152), (cx, 196)], fill=TIMBER, width=14)
bell = [(cx - 148, 452), (cx - 108, 300), (cx - 52, 224), (cx, 196), (cx + 52, 224), (cx + 108, 300), (cx + 148, 452)]
d.polygon(bell, fill=GOLD)
mouth_w = 168 if v != "v1" else 150
d.rectangle([cx - mouth_w, 452, cx + mouth_w, 486], fill=GOLD)
d.rectangle([cx - mouth_w, 452, cx + mouth_w, 464], fill=(188, 142, 54))
if v != "v1":  # the notch: a bite cut from the mouth's right corner, in ground green
    d.polygon([(cx + mouth_w - 44, 486), (cx + mouth_w, 486), (cx + mouth_w, 442)], fill=GREEN)
r = 21 if v != "v1" else 15
d.ellipse([cx - r, 492, cx + r, 492 + 2 * r], fill=RED)  # clapper dot
d.line([(cx, 486), (cx, 496)], fill=(120, 88, 30), width=8)
# wordmark, letterspaced wide, chalked toll board style
def spaced(draw, cx, y, text, font, fill, tracking):
    widths = [draw.textlength(ch, font=font) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=font, fill=fill); x += w + tracking
if v != "v1":
    f = ImageFont.truetype("fonts/AnekMalayalam.ttf", 62)
    spaced(d, W / 2, 736, "Sandboxed-Brave-Browser", f, CREAM, 6)
    tw = d.textlength("Sandboxed-Brave-Browser", font=f) + 6 * 22
    d.line([(W / 2 - tw / 2, 838), (W / 2 + tw / 2, 838)], fill=GOLD, width=4)
rng = np.random.default_rng(4); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 3, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "logo.png" if v == "ship" else f"scratch/logo-{v}.png"
img.save(out); print(out)
img.resize((64, 64), Image.LANCZOS).save(f"scratch/logo64-{v}.png"); print("64px saved")
