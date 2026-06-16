#!/usr/bin/env python3
"""Annotate Ruelle app screenshots with circles / arrows / numbered badges and a
Korean legend panel. Usage is driven by per-image specs in make_overview.py."""
import math
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
PINK = (232, 101, 122)
WHITE = (255, 255, 255)
DARK = (20, 19, 22)
SHADOW = (0, 0, 0, 90)


def _font(size):
    return ImageFont.truetype(FONT_PATH, size)


def _arrow(draw, p0, p1, color, width=8):
    draw.line([p0, p1], fill=color, width=width)
    ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    L = 34
    for da in (math.radians(28), -math.radians(28)):
        x = p1[0] - L * math.cos(ang + da)
        y = p1[1] - L * math.sin(ang + da)
        draw.line([(x, y), p1], fill=color, width=width)


def _badge(draw, center, num, r=30):
    x, y = center
    draw.ellipse([x - r, y - r, x + r, y + r], fill=PINK, outline=WHITE, width=5)
    f = _font(34)
    t = str(num)
    bb = draw.textbbox((0, 0), t, font=f)
    draw.text((x - (bb[2] - bb[0]) / 2, y - (bb[3] - bb[1]) / 2 - bb[1]), t, font=f, fill=WHITE)


def annotate(src, dst, title, items):
    """items: list of dicts. Each has 'num','label' and a marker:
    - circle: 'box':[x1,y1,x2,y2]
    - arrow:  'from':[x,y], 'to':[x,y]
    A numbered badge is placed at 'badge':[x,y] (defaults near marker)."""
    base = Image.open(src).convert("RGB")
    W, H = base.size

    title_h = 110
    legend_h = 70 + 64 * len(items)
    canvas = Image.new("RGB", (W, H + title_h + legend_h), DARK)
    canvas.paste(base, (0, title_h))
    d = ImageDraw.Draw(canvas)

    # Title bar
    d.rectangle([0, 0, W, title_h], fill=DARK)
    tf = _font(54)
    d.text((40, 28), title, font=tf, fill=PINK)

    # Markers on the screenshot (offset by title_h)
    oy = title_h
    for it in items:
        color = PINK
        if it.get("type") == "circle":
            x1, y1, x2, y2 = it["box"]
            d.ellipse([x1, y1 + oy, x2, y2 + oy], outline=color, width=8)
            bx = it.get("badge", [x2, y1])
        elif it.get("type") == "arrow":
            fx, fy = it["from"]
            tx, ty = it["to"]
            _arrow(d, (fx, fy + oy), (tx, ty + oy), color)
            bx = it.get("badge", it["from"])
        else:
            bx = it.get("badge", [W // 2, 100])
        _badge(d, (bx[0], bx[1] + oy), it["num"])

    # Legend panel
    ly = title_h + H + 30
    lf = _font(40)
    for it in items:
        _badge(d, (66, ly + 26), it["num"], r=26)
        d.text((110, ly), it["label"], font=lf, fill=WHITE)
        ly += 64

    canvas.save(dst, "PNG")
    print("wrote", dst)
