#!/usr/bin/env bash
# Builds The After-Five Business from manuscript/*.md into output/.
#   output/The-After-Five-Business.epub        Kindle upload (KDP accepts EPUB)
#   output/The-After-Five-Business.docx        Word manuscript (also accepted by KDP)
#   output/The-After-Five-Business-proof.pdf   6 x 9 inch reading proof
#   output/The-After-Five-Business-cover.jpg   1600 x 2560 Kindle cover
# Requires: pandoc, python3 with python-docx and Pillow, node with playwright.
set -euo pipefail
cd "$(dirname "$0")/.."

NAME="The-After-Five-Business"
OUT="output"
mkdir -p "$OUT" manuscript/images
CHAPTERS=(manuscript/*.md)
export NODE_PATH="${NODE_PATH:-$(npm root -g)}"
COMMON=(--metadata-file=build/metadata.yaml --resource-path=manuscript --lua-filter=build/frontmatter.lua)

echo "Rendering figures..."
python3 build/figures/make_figures.py build/figures/figures.html
node build/render.js figures build/figures/figures.html manuscript/images
rm -f build/figures/figures.html

echo "Rendering cover..."
node build/render.js cover build/cover.html build/cover.png
python3 -c "from PIL import Image; Image.open('build/cover.png').convert('RGB').save('$OUT/$NAME-cover.jpg', quality=92, dpi=(300, 300))"
rm -f build/cover.png

echo "Building EPUB..."
pandoc "${COMMON[@]}" "${CHAPTERS[@]}" \
  --toc --toc-depth=1 --split-level=1 \
  --css=build/epub.css \
  --epub-cover-image="$OUT/$NAME-cover.jpg" \
  -o "$OUT/$NAME.epub"

echo "Building DOCX..."
python3 build/make_reference_docx.py build/reference.docx
pandoc "${COMMON[@]}" "${CHAPTERS[@]}" \
  --reference-doc=build/reference.docx \
  -o "$OUT/$NAME.docx"

echo "Building proof PDF..."
pandoc "${COMMON[@]}" "${CHAPTERS[@]}" \
  --standalone --embed-resources --toc --toc-depth=1 --section-divs \
  --css=build/print.css \
  -V document-css=false \
  -o build/book.html
node build/render.js pdf build/book.html "$OUT/$NAME-proof.pdf"
rm -f build/book.html

echo "Done:"
ls -la "$OUT"
