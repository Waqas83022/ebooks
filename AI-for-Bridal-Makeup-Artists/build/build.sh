#!/usr/bin/env bash
# Builds the ebook files from manuscript/*.md into output/.
#   output/AI-for-Bridal-Makeup-Artists.epub        Kindle upload (KDP accepts EPUB)
#   output/AI-for-Bridal-Makeup-Artists.docx        Word manuscript (also accepted by KDP)
#   output/AI-for-Bridal-Makeup-Artists-proof.pdf   6 x 9 inch reading proof
#   output/AI-for-Bridal-Makeup-Artists-cover.jpg   1600 x 2560 Kindle cover
# Requires: pandoc, python3 with python-docx and Pillow, node with playwright.
set -euo pipefail
cd "$(dirname "$0")/.."

NAME="AI-for-Bridal-Makeup-Artists"
OUT="output"
mkdir -p "$OUT" images
CHAPTERS=(manuscript/*.md)
export NODE_PATH="${NODE_PATH:-$(npm root -g)}"
COMMON=(--metadata-file=build/metadata.yaml --lua-filter=build/frontmatter.lua --resource-path=.:images)

echo "Rendering figures..."
python3 build/figures.py
node build/render.js figures build/figures images

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
  --standalone --toc --toc-depth=1 --section-divs \
  --css=build/print.css -V document-css=false \
  -o book.html
node build/render.js pdf book.html "$OUT/$NAME-proof.pdf"
rm -f book.html

echo "Done:"
ls -la "$OUT"
