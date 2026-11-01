#!/usr/bin/env python3
"""Sandboxed-Brave-Browser wordmark banner: dusk on a stone bridge over a narrow gorge
river. The bridge fills the width, one arch, a low parapet, and at the far end a gate
post where the toll bell hangs in its frame. A troll sits on the parapet with a ledger
open on his knees, big hands, patient face, a ring of iron keys on a belt loop, arguing
politely with a goat who stands mid span with one hoof raised. A second goat waits at
the near end beside a hand painted toll board carrying the name Sandboxed-Brave-Browser
in cream capitals in Anek Malayalam, as if generations of toll keepers had repainted it.
Lanterns hang from the parapet at intervals, just lit. Below, the river runs dark green
between rocks; on the near bank a ring of red capped mushrooms closes a circle."""
import sys, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
random.seed(83)
W, H = 2560, 640
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
GREEN = (26, 54, 36); GOLD = (216, 168, 74); CREAM = (240, 232, 200); RED = (178, 44, 36)
img = Image.new("RGB", (W, H), GREEN); d = ImageDraw.Draw(img, "RGBA")
for y in range(0, 210):
    t = y / 210
    d.line([(0, y), (W, y)], fill=(int(24 + 60 * t), int(38 + 62 * t), int(44 + 30 * t)))
for _ in range(150):
    x, y = random.randint(0, W), random.randint(0, 120)
    d.ellipse([x - 1, y - 1, x + 1, y + 1], fill=(240, 238, 210, random.randint(120, 230)))
d.polygon([(0, 210), (2560, 170), (2560, 300), (0, 300)], fill=(20, 42, 28))
for x in range(6, 2560, 62):
    h = random.randint(70, 140)
    d.rectangle([x, 300 - h, x + 9, 300], fill=(14, 30, 20))
    d.polygon([(x - 14, 300 - h + 24), (x + 4, 300 - h - 22), (x + 22, 300 - h + 24)], fill=(16, 36, 24))
# river and gorge below
d.polygon([(0, 470), (760, 470), (640, 640), (0, 640)], fill=(30, 34, 30))
d.polygon([(1800, 470), (2560, 470), (2560, 640), (1920, 640)], fill=(30, 34, 30))
d.rectangle([640, 520, 1920, 640], fill=(16, 44, 32))
for i in range(18):
    x, y = random.randint(680, 1860), random.randint(540, 624)
    d.line([(x, y), (x + random.randint(36, 120), y)], fill=(216, 168, 74, random.randint(50, 120)), width=3)
# bridge body, deck, parapet, arch
d.rectangle([0, 372, 2560, 520], fill=(104, 96, 82))
d.ellipse([830, 300, 1730, 700], fill=(14, 40, 30))
d.arc([830, 300, 1730, 700], 0, 180, fill=(140, 132, 114), width=9)
d.rectangle([0, 330, 2560, 376], fill=(116, 108, 94))
d.rectangle([0, 296, 2560, 332], fill=(132, 124, 108))
for x in range(0, 2560, 104):
    d.line([(x, 296), (x, 376)], fill=(96, 88, 74), width=2)
# lanterns just lit along the parapet
for lx in (420, 900, 1660, 2140):
    d.rectangle([lx - 9, 236, lx + 15, 278], fill=(30, 28, 24), outline=GOLD, width=2)
    d.ellipse([lx - 2, 246, lx + 8, 268], fill=(255, 196, 96))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
    gd.ellipse([lx - 44, 208, lx + 50, 300], fill=(255, 190, 90, 42))
    img = Image.alpha_composite(img.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(15))).convert("RGB")
    d = ImageDraw.Draw(img, "RGBA")
# toll bell frame at the far gate
bx = 2380
d.rectangle([bx - 46, 128, bx - 30, 298], fill=(74, 54, 34)); d.rectangle([bx + 46, 128, bx + 62, 298], fill=(74, 54, 34))
d.rectangle([bx - 58, 112, bx + 74, 132], fill=(74, 54, 34))
d.polygon([(bx + 8 - 30, 226), (bx + 8 - 17, 168), (bx + 8, 150), (bx + 8 + 17, 168), (bx + 8 + 30, 226)], fill=GOLD)
d.rectangle([bx - 24, 226, bx + 40, 236], fill=(188, 142, 54))
d.ellipse([bx + 2, 236, bx + 14, 250], fill=RED)
# the troll on the parapet, ledger open on his knees, keys on a belt loop
tx, ty = 1750, 176
d.ellipse([tx - 34, ty - 58, tx + 34, ty + 14], fill=(122, 138, 96))  # head, patient face
d.ellipse([tx - 12, ty - 34, tx - 5, ty - 26], fill=(30, 34, 26)); d.ellipse([tx + 6, ty - 34, tx + 13, ty - 26], fill=(30, 34, 26))
d.arc([tx - 12, ty - 22, tx + 13, ty - 6], 20, 160, fill=(30, 34, 26), width=3)  # polite mouth
d.polygon([(tx - 56, ty + 108), (tx - 44, ty + 8), (tx + 44, ty + 8), (tx + 56, ty + 108)], fill=(84, 92, 62))  # torso seated
d.rectangle([tx - 58, ty + 62, tx + 58, ty + 76], fill=(52, 44, 32))  # belt
for k in range(4):  # ring of iron keys
    d.ellipse([tx + 34 + k * 3, ty + 76, tx + 46 + k * 3, ty + 90], outline=(168, 168, 160), width=3)
d.polygon([(tx - 66, ty + 96), (tx, ty + 82), (tx, ty + 128), (tx - 66, ty + 132)], fill=CREAM)  # ledger, left page
d.polygon([(tx + 66, ty + 96), (tx, ty + 82), (tx, ty + 128), (tx + 66, ty + 132)], fill=(228, 220, 186))  # right page
for ly in range(ty + 94, ty + 122, 9):
    d.line([(tx - 56, ly), (tx - 10, ly - 6)], fill=(140, 132, 108), width=2)
    d.line([(tx + 10, ly - 6), (tx + 56, ly)], fill=(140, 132, 108), width=2)
d.ellipse([tx - 84, ty + 84, tx - 58, ty + 106], fill=(122, 138, 96))  # big hands
d.ellipse([tx + 58, ty + 84, tx + 84, ty + 106], fill=(122, 138, 96))
d.rectangle([tx - 50, ty + 108, tx - 18, ty + 150], fill=(70, 76, 54)); d.rectangle([tx + 18, ty + 108, tx + 50, ty + 150], fill=(70, 76, 54))  # legs over the parapet edge
# goat mid span, one hoof raised in mid point
def goat(x, y, s, raised=True, facing=1):
    d.polygon([(x, y), (x + 74 * s * facing, y + 6 * s), (x + 80 * s * facing, y + 30 * s), (x + 6 * s * facing, y + 34 * s)], fill=(232, 226, 206))  # body
    hx = x + 84 * s * facing
    d.ellipse([hx - 14 * s, y - 20 * s, hx + 12 * s, y + 8 * s], fill=(238, 232, 214))  # head
    d.arc([hx - 16 * s, y - 30 * s, hx + 4 * s, y - 8 * s], 200, 330, fill=(150, 140, 118), width=int(4 * s))  # horn
    d.ellipse([hx - 2 * s, y - 8 * s, hx + 3 * s, y - 3 * s], fill=(30, 30, 26))
    for lx2, bend in ((10, 0), (30, 0), (52, 0), (68, 1 if raised else 0)):
        gx = x + lx2 * s * facing
        lw = int(6 * s) if v == "v1" else int(9 * s)
        if bend:
            d.line([(gx, y + 32 * s), (gx + 10 * s * facing, y + 48 * s)], fill=(232, 226, 206), width=lw)
            d.line([(gx + 10 * s * facing, y + 48 * s), (gx + 22 * s * facing, y + 48 * s)], fill=(232, 226, 206), width=lw)
        else:
            d.line([(gx, y + 32 * s), (gx, y + 62 * s)], fill=(232, 226, 206), width=lw)
    d.polygon([(x - 4 * s * facing, y + 2 * s), (x - 14 * s * facing, y - 8 * s), (x - 10 * s * facing, y + 12 * s)], fill=(232, 226, 206))  # tail
goat(1150, 232, 1.05, raised=True, facing=1)
# second goat waiting at the near end, beside the toll board (clear of it from v2 on)
goat(560 if v == "v1" else 830, 240, 0.95, raised=False, facing=1)
# hand painted toll board at the near end carrying the name
bw = 700 if v == "ship" else 560
bx0, by0 = 60, 176
d.rectangle([bx0 + 30, by0 + 96, bx0 + 44, by0 + 150], fill=(74, 54, 34)); d.rectangle([bx0 + bw - 44, by0 + 96, bx0 + bw - 30, by0 + 150], fill=(74, 54, 34))
d.rectangle([bx0, by0, bx0 + bw, by0 + 100], fill=GREEN, outline=GOLD, width=3)
f = ImageFont.truetype("fonts/AnekMalayalam.ttf", 44 if v == "ship" else 36)
txt = "Sandboxed-Brave-Browser"; tw = d.textlength(txt, font=f)
scale = min(1.0, (bw - 30) / tw)
if scale < 1.0:
    f = ImageFont.truetype("fonts/AnekMalayalam.ttf", int(44 * scale)); tw = d.textlength(txt, font=f)
d.text((bx0 + (bw - tw) / 2, by0 + 28), txt, font=f, fill=CREAM)
# mushroom ring on the near bank
for ang in range(0, 360, 36):
    import math
    x = 2260 + int(120 * math.cos(math.radians(ang))); y = 590 + int(26 * math.sin(math.radians(ang)))
    d.rectangle([x - 2, y, x + 2, y + 10], fill=CREAM)
    d.pieslice([x - 12, y - 12, x + 12, y + 12], 180, 360, fill=RED)
rng = np.random.default_rng(6); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 4, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "banner.png" if v == "ship" else f"scratch/banner-{v}.png"
img.save(out); print(out)
