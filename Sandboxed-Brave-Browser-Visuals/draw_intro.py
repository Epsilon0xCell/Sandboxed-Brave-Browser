#!/usr/bin/env python3
"""Sandboxed-Brave-Browser introduction banner: a troll bridge at dusk, nothing written
anywhere. Foreground: the near end of a stone bridge, parapet worn smooth, a coil of rope
and an empty collecting bowl on the stones, a ring of red capped toadstools in the grass
at the bridge foot. Midground: the span over a gorge, one round arch, the toll bell
hanging motionless in its timber frame at the far gate, its rope dangling down the post,
a lantern burning on each parapet post. Under the arch a thick shadow with two pale
points that might be eyes or river shine; the picture does not settle which. Background:
the far bank climbing into dark forest, a path switching back up the hill, early stars.
No lettering, numerals, carved signs, logos, or interface shapes of any kind."""
import sys, random
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
random.seed(41)
W, H = 1600, 900
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
GREEN = (26, 54, 36); GOLD = (216, 168, 74); CREAM = (240, 232, 200); RED = (178, 44, 36)
img = Image.new("RGB", (W, H), GREEN); d = ImageDraw.Draw(img, "RGBA")
# dusk sky over the ridge, gold sinking at the horizon line
for y in range(0, 300):
    t = y / 300
    d.line([(0, y), (W, y)], fill=(int(24 + 60 * t), int(38 + 62 * t), int(44 + 30 * t)))
for _ in range(120):  # early stars over the ridge
    x, y = random.randint(0, W), random.randint(0, 170)
    d.ellipse([x - 1, y - 1, x + 1, y + 1], fill=(240, 238, 210, random.randint(120, 230)))
# far bank forest, trunks in deep green ranks, a path switching back up the hill
d.polygon([(0, 300), (1600, 240), (1600, 430), (0, 430)], fill=(20, 42, 28))
for x in range(10, 1600, 46):
    h = random.randint(90, 190)
    d.rectangle([x, 430 - h, x + 10, 430], fill=(14, 30, 20))
    d.polygon([(x - 16, 430 - h + 30), (x + 5, 430 - h - 26), (x + 26, 430 - h + 30)], fill=(16, 36, 24))
d.line([(1420, 428), (1180, 372), (1300, 318), (1120, 272)], fill=(96, 84, 54), width=5)
# gorge walls and the dark green river with lantern streaks
d.polygon([(0, 560), (520, 560), (420, 900), (0, 900)], fill=(30, 34, 30))
d.polygon([(1080, 560), (1600, 560), (1600, 900), (1180, 900)], fill=(30, 34, 30))
d.rectangle([420, 640, 1180, 900], fill=(16, 44, 32))
for i in range(16):
    x, y = random.randint(450, 1120), random.randint(670, 870)
    ln = random.randint(30, 110)
    d.line([(x, y), (x + ln, y)], fill=(216, 168, 74, random.randint(50, 120)), width=3)
for i in range(10):  # black rocks
    x, y = random.randint(450, 1100), random.randint(690, 860)
    d.ellipse([x, y, x + random.randint(40, 90), y + 22], fill=(10, 14, 12))
# the span: deck, parapet, one round arch
d.rectangle([0, 470, 1600, 560], fill=(116, 108, 94))
d.rectangle([0, 430, 1600, 472], fill=(132, 124, 108))
for x in range(0, 1600, 80):
    d.line([(x, 430), (x, 560)], fill=(96, 88, 74), width=2)
d.rectangle([0, 560, 1600, 790], fill=(104, 96, 82))  # bridge body below the deck
d.ellipse([520, 470, 1080, 830], fill=(14, 40, 30))  # the arch opening, punched through
d.arc([520, 470, 1080, 830], 0, 180, fill=(140, 132, 114), width=10)  # arch ring stones
d.rectangle([0, 470, 1600, 560], fill=(116, 108, 94))  # deck redrawn over the opening top
d.rectangle([0, 430, 1600, 472], fill=(132, 124, 108))
# the shadow under the arch, and two pale points left unsettled
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(shadow)
sd.ellipse([600, 520, 1000, 800], fill=(6, 10, 8, 150))
img = Image.alpha_composite(img.convert("RGBA"), shadow.filter(ImageFilter.GaussianBlur(24))).convert("RGB")
d = ImageDraw.Draw(img, "RGBA")
eye_a = 200 if v == "v1" else (110 if v == "v2" else 84)
for ex in (742, 838):
    ey = 618 if v != "ship" else 652
    d.ellipse([ex, ey, ex + (16 if v != "ship" else 13), ey + (8 if v != "ship" else 5)], fill=(238, 232, 196, eye_a))
# lanterns on each parapet post, flames small and steady
for lx in (180, 560, 940, 1330):
    d.rectangle([lx, 392, lx + 10, 432], fill=(52, 44, 32))
    d.rectangle([lx - 8, 356, lx + 18, 394], fill=(30, 28, 24), outline=GOLD, width=2)
    d.ellipse([lx - 1, 366, lx + 11, 386], fill=(255, 196, 96))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
    gd.ellipse([lx - 42, 330, lx + 52, 420], fill=(255, 190, 90, 44))
    img = Image.alpha_composite(img.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(16))).convert("RGB")
    d = ImageDraw.Draw(img, "RGBA")
# the toll bell in its timber frame at the far gate, motionless, rope dangling
bx = 1452
bell_s = 1.0 if v == "v1" else 1.3
d.rectangle([bx - 52, 268, bx - 36, 432], fill=(74, 54, 34))
d.rectangle([bx + 52, 268, bx + 68, 432], fill=(74, 54, 34))
d.rectangle([bx - 64, 250, bx + 80, 272], fill=(74, 54, 34))
top = 286
d.polygon([(bx + 8 - 34 * bell_s, top + 74 * bell_s), (bx + 8 - 20 * bell_s, top + 18 * bell_s),
           (bx + 8, top), (bx + 8 + 20 * bell_s, top + 18 * bell_s), (bx + 8 + 34 * bell_s, top + 74 * bell_s)], fill=GOLD)
d.rectangle([bx + 8 - 38 * bell_s, top + 74 * bell_s, bx + 8 + 38 * bell_s, top + 84 * bell_s], fill=(188, 142, 54))
d.ellipse([bx + 1, top + 84 * bell_s, bx + 15, top + 98 * bell_s], fill=RED)  # clapper
d.line([(bx + 60, 272), (bx + 60, 400)], fill=(196, 168, 116), width=4)  # bell rope down the post
# foreground near end: worn parapet, coil of rope, empty collecting bowl
d.polygon([(0, 560), (430, 560), (430, 900), (0, 900)], fill=(104, 96, 82))
d.polygon([(0, 560), (430, 560), (380, 640), (0, 640)], fill=(124, 116, 100))
for r in (44, 33, 22):
    d.ellipse([120 - r, 700 - r // 2, 120 + r, 700 + r // 2 + 10], outline=(178, 152, 104), width=6)
d.pieslice([252, 660, 372, 730], 0, 180, fill=(96, 88, 74))  # collecting bowl, empty
d.ellipse([252, 660, 372, 688], fill=(70, 62, 50), outline=(150, 140, 120), width=3)
# grass at the bridge foot and the ring of red capped toadstools
d.polygon([(430, 760), (430, 900), (0, 900), (0, 760)], fill=(24, 52, 30))
ring = [(60, 806), (120, 786), (196, 780), (268, 792), (322, 818), (268, 846), (190, 856), (118, 844), (66, 830)]
for x, y in ring:
    d.rectangle([x - 3, y, x + 3, y + 15], fill=CREAM)
    if v == "ship":
        d.pieslice([x - 17, y - 17, x + 17, y + 17], 180, 360, fill=RED)
    else:
        d.arc([x - 15, y - 14, x + 15, y + 12], 180, 360, fill=RED)
    d.ellipse([x - 4, y - 10, x, y - 6], fill=(250, 240, 220))
rng = np.random.default_rng(8); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 4, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "intro-banner.png" if v == "ship" else f"scratch/intro-{v}.png"
img.save(out); print(out)
