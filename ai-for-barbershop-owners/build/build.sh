#!/usr/bin/env bash
# Builds AI for Barbershop Owners from manuscript/*.md into output/.
#   output/AI-for-Barbershop-Owners.epub        Kindle upload (KDP accepts EPUB)
#   output/AI-for-Barbershop-Owners.docx        Word version (also accepted by KDP)
#   output/AI-for-Barbershop-Owners-proof.pdf   6 x 9 inch reading proof
#   output/AI-for-Barbershop-Owners-cover.jpg   1600 x 2560 Kindle cover
# Requires: pandoc 3, python3 with python-docx and Pillow, node with playwright.
set -euo pipefail
cd "$(dirname "$0")/.."

NAME="AI-for-Barbershop-Owners"
OUT="output"
mkdir -p "$OUT"
CHAPTERS=(manuscript/*.md)
export NODE_PATH="${NODE_PATH:-$(npm root -g)}"

echo "Rendering figures..."
python3 build/figures/make_figures.py
node build/render.js figures build/figures/html build/figures/png
python3 build/optimize_images.py build/figures/png images

echo "Rendering cover..."
node build/render.js cover build/cover.html build/cover.png
python3 -c "from PIL import Image; Image.open('build/cover.png').convert('RGB').save('$OUT/$NAME-cover.jpg', quality=90, dpi=(300, 300))"
rm -f build/cover.png

echo "Building EPUB..."
pandoc --metadata-file=build/metadata.yaml "${CHAPTERS[@]}" \
  --lua-filter=build/frontmatter.lua \
  --toc --toc-depth=1 --split-level=1 \
  --css=build/epub.css \
  --epub-cover-image="$OUT/$NAME-cover.jpg" \
  --resource-path=. \
  -o "$OUT/$NAME.epub"

echo "Building DOCX..."
python3 build/make_reference_docx.py build/reference.docx
pandoc --metadata-file=build/metadata.yaml "${CHAPTERS[@]}" \
  --lua-filter=build/frontmatter.lua \
  --reference-doc=build/reference.docx \
  --resource-path=. \
  -o "$OUT/$NAME.docx"

echo "Building proof PDF..."
pandoc --metadata-file=build/metadata.yaml "${CHAPTERS[@]}" \
  --lua-filter=build/frontmatter.lua \
  --standalone --toc --toc-depth=1 --section-divs \
  --css=build/print.css \
  -V document-css=false \
  -o book.html
node build/render.js pdf book.html "$OUT/$NAME-proof.pdf"
rm -f book.html

echo "Done:"
ls -la "$OUT"
