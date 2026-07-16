"""Headshot -> ASCII self-portrait (the one in my profile README).

Pipeline: rembg person segmentation -> largest-blob mask -> histogram
equalization over face pixels only -> brightness-to-character-density ramp,
then a few hand patches for the eyes and mouth.

Usage:  pip install pillow rembg
        python generate.py path/to/headshot.jpg [width]
"""
import sys
from PIL import Image

RAMP = " .:-=+*#%@"  # sparse -> dense; bright pixel -> dense char (dark-theme tuned)
CHAR_ASPECT = 0.5    # mono char width/height ratio
FLOOR = 1            # never blank inside the silhouette
BOTTOM_CROP = 0.85   # drop the jacket strip below the collar

# hand retouch: (line 1-indexed, col 0-indexed, replacement) — tuned for width 60
PATCHES = [
    (15, 21, ".:*-.."),     # lit-side eye: slit + catchlight
    (16, 20, "=++=-."),     # cheek under it, so the slit has an edge
    (15, 36, "-*-.."),      # shadow-side eye: dimmer catchlight
    (15, 28, ":-=+=-:"),    # dim nose-bridge highlight so the eyes dominate
    (16, 36, "-==-."),      # cheek under shadow eye
    (23, 26, "=--------="),  # continuous dark smile line
    (24, 28, "+*##*+"),     # lower-lip highlight
]


def cutout(src):
    from rembg import remove
    print(f"segmenting {src} (first run downloads the u2net model)")
    return remove(Image.open(src))


def gen(rgba, width):
    rgba = rgba.crop(rgba.getchannel("A").getbbox())
    rgba = rgba.crop((0, 0, rgba.width, round(rgba.height * BOTTOM_CROP)))
    rows = max(1, round(rgba.height / rgba.width * width * CHAR_ASPECT))
    rgba = rgba.resize((width, rows), Image.LANCZOS)
    gray, alpha = rgba.convert("L").load(), rgba.getchannel("A").load()

    inside = {(x, y) for y in range(rows) for x in range(width) if alpha[x, y] >= 128}

    # histogram-equalize using only in-person pixels: spreads the midtones across the ramp
    hist = [0] * 256
    for c in inside:
        hist[gray[c]] += 1
    cdf, total, acc = [0] * 256, len(inside), 0
    for v in range(256):
        acc += hist[v]
        cdf[v] = acc * 255 // total

    # keep only the largest connected blob (drops stray segmentation flecks)
    seen, best = set(), set()
    for start in inside:
        if start in seen:
            continue
        comp, stack = set(), [start]
        while stack:
            c = stack.pop()
            if c in seen or c not in inside:
                continue
            seen.add(c); comp.add(c)
            x, y = c
            stack += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        if len(comp) > len(best):
            best = comp

    lines = []
    for y in range(rows):
        line = ""
        for x in range(width):
            if (x, y) not in best:
                line += " "
            else:
                v = cdf[gray[x, y]]
                line += RAMP[max(FLOOR, min(len(RAMP) - 1, v * len(RAMP) // 256))]
        lines.append(line.rstrip())
    while lines and not lines[0]: lines.pop(0)
    while lines and not lines[-1]: lines.pop()
    return lines


def retouch(lines):
    for ln, col, rep in PATCHES:
        s = lines[ln - 1].ljust(col + len(rep))
        lines[ln - 1] = (s[:col] + rep + s[col + len(rep):]).rstrip()
    return lines


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    lines = gen(cutout(sys.argv[1]), width)
    if width == 60:
        lines = retouch(lines)
    else:
        print(f"note: hand patches skipped (tuned for width 60, got {width})")
    art = "\n".join(lines)
    open("portrait.txt", "w").write(art)
    print(art)
    print("-> portrait.txt")
