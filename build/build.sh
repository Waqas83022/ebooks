#!/usr/bin/env bash
# Builds the ebook files from manuscript/*.md into output/.
#   output/The-Archer-and-the-Wind.epub        Kindle upload (KDP accepts EPUB)
#   output/The-Archer-and-the-Wind.docx        Word manuscript (also accepted by KDP)
#   output/The-Archer-and-the-Wind-proof.pdf   6 x 9 inch reading proof
#   output/The-Archer-and-the-Wind-cover.jpg   1600 x 2560 Kindle cover
# Requires: pandoc, python3 with python-docx and Pillow, node with playwright.
set -euo pipefail
cd "$(dirname "$0")/.."

NAME="The-Archer-and-the-Wind"
OUT="output"
mkdir -p "$OUT"
CHAPTERS=(manuscript/*.md)
export NODE_PATH="${NODE_PATH:-$(npm root -g)}"

echo "Rendering cover..."
node build/render.js cover build/cover.html build/cover.png
python3 -c "from PIL import Image; Image.open('build/cover.png').convert('RGB').save('$OUT/$NAME-cover.jpg', quality=92, dpi=(300, 300))"
rm -f build/cover.png

echo "Building EPUB..."
pandoc --metadata-file=build/metadata.yaml "${CHAPTERS[@]}" \
  --lua-filter=build/frontmatter.lua \
  --toc --toc-depth=1 --split-level=1 \
  --css=build/epub.css \
  --epub-cover-image="$OUT/$NAME-cover.jpg" \
  -o "$OUT/$NAME.epub"

echo "Building DOCX..."
python3 build/make_reference_docx.py build/reference.docx
pandoc --metadata-file=build/metadata.yaml "${CHAPTERS[@]}" \
  --lua-filter=build/frontmatter.lua \
  --reference-doc=build/reference.docx \
  -o "$OUT/$NAME.docx"

echo "Building proof PDF..."
pandoc --metadata-file=build/metadata.yaml "${CHAPTERS[@]}" \
  --lua-filter=build/frontmatter.lua \
  --standalone --toc --toc-depth=1 --section-divs \
  --css=print.css \
  -V document-css=false \
  -o build/book.html
node build/render.js pdf build/book.html "$OUT/$NAME-proof.pdf"
rm -f build/book.html

echo "Done:"
ls -la "$OUT"
