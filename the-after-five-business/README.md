# The After-Five Business

*Build a Small AI-Assisted Service Business on Five Hours a Week Without Risking Your Day Job*, by Muhammad Waqas.

A practical nonfiction book of about 38,000 words for employees who want to earn extra income from a skill they already use at work: one fixed-scope service, AI tools for the repetitive middle of the job, a clean line between the business and the employer, and a six-week paid pilot that ends in a decision. Written for Kindle (KDP) publication, with 17 diagrams.

## What is here

`manuscript/` has the book in Markdown, one file per section, in reading order, plus `manuscript/images/` with the rendered figures.

| Part | Chapters |
|---|---|
| Front matter and introduction | Copyright, dedication, "Five hours after five" |
| One: Clear the ground | 1 What AI changed, and what it didn't · 2 Find five hours and protect them · 3 Your employer, your contract and the clean line |
| Two: Shape the offer | 4 The skill you already sell every day · 5 Twelve services that fit an evening schedule · 6 Package it: the fixed-scope offer |
| Three: Build it and prove it | 7 A small tool kit, kept separate · 8 Pilot one: a process manual · 9 Pilot two: a research brief · 10 Pilot three: a small automation |
| Four: Find and serve clients | 11 Find your first three buyers · 12 The discovery call and the one-page proposal · 13 Price it without guessing · 14 Deliver work you can sign your name to |
| Five: Run it like a business | 15 Money, tax and the boring paperwork · 16 Measure the job you actually did · 17 The six-week pilot and the decision · 18 Grow without breaking |
| Back matter | Afterword · Questions readers ask · The toolkit (worksheets and templates A–M) · Notes and sources · A small request · About the author |

`output/` has the finished files:

- `The-After-Five-Business.epub`: the file to upload to KDP. It passes EPUBCheck (EPUB 3.3 rules) with no errors or warnings.
- `The-After-Five-Business-cover.jpg`: the Kindle cover, 1600 × 2560 pixels.
- `The-After-Five-Business.docx`: the Word version, for editing.
- `The-After-Five-Business-proof.pdf`: a 6 × 9 inch proof for reading and review.

`publishing/` has the KDP listing kit (`kdp-listing.md`: description in plain text and HTML, seven keywords, categories, price, AI-disclosure guidance, checklist), notes for the author (`author-notes.md`) and the cover thumbnail test.

`build/` has the build script, stylesheets, cover design and figure definitions.

## Building

Requirements: pandoc 3, Python 3 with `python-docx` and `Pillow`, and Node.js with Playwright and Chromium.

```bash
./build/build.sh
```
