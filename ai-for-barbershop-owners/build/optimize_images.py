"""Copy rendered figures into images/ as small palette PNGs (keeps the EPUB light for KDP delivery fees).
Usage: python3 build/optimize_images.py build/figures/png images"""
import glob, os, sys
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
os.makedirs(dst, exist_ok=True)
for f in sorted(glob.glob(os.path.join(src, "*.png"))):
    im = Image.open(f).convert("RGB")
    q = im.quantize(colors=64, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    out = os.path.join(dst, os.path.basename(f))
    q.save(out, optimize=True)
    print(f"{os.path.basename(f)}: {os.path.getsize(f)//1024} KB -> {os.path.getsize(out)//1024} KB")
