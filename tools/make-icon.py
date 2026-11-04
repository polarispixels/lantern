#!/usr/bin/env python3
"""Draw the web icons in site/ from a 16x16 grid, using PICO-8 colors.
Edit the grid and run: python3 tools/make-icon.py
"""
import math
import os
from PIL import Image

# PICO-8 palette entries the icon uses
COLORS = {
    "0": (0, 0, 0),         # black
    "2": (126, 37, 83),     # dark purple
    "4": (171, 82, 54),     # brown, the game's dirt color
    "5": (95, 87, 79),      # dark gray
    "6": (194, 195, 199),   # light gray
    "7": (255, 241, 232),   # white
    "9": (255, 163, 0),     # orange
    "a": (255, 236, 39),    # yellow
}

# "." lets the glow show through
LANTERN = [
    "................",
    "......6666......",
    ".....6....6.....",
    ".....6....6.....",
    "....66666666....",
    ".....5aaaa5.....",
    ".....5a77a5.....",
    ".....5a77a5.....",
    ".....5a77a5.....",
    ".....5a99a5.....",
    ".....5aaaa5.....",
    "....66666666....",
    "................",
    "................",
    "................",
    "................",
]


def glow(x, y):
    """A circle of light with a dithered edge, like the darkness in the game."""
    r = math.hypot(x - 7.5, y - 7)
    if r < 5.5:
        return "4"
    if r < 7.5 and (x + y) % 2 == 0:
        return "4"
    return "0"


icon = Image.new("RGB", (16, 16))
for y, row in enumerate(LANTERN):
    for x, c in enumerate(row):
        icon.putpixel((x, y), COLORS[glow(x, y) if c == "." else c])

site = os.path.join(os.path.dirname(__file__), "..", "site")
for size in (32, 192):
    icon.resize((size, size), Image.NEAREST).save(os.path.join(site, f"icon-{size}.png"))
