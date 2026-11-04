# The Archer and the Wind

*How to Keep Going When Hard Work Isn't Enough*, by Muhammad Waqas.

A nonfiction book of about 41,500 words (plus notes) on how hard work, luck, destiny and hope fit together, and how to keep going when none of them can guarantee the result. It is written for Kindle (KDP) publication.

## What is here

`manuscript/` has the book in Markdown, one file per section, in reading order:

| Part | Chapters |
|---|---|
| Front matter and introduction | Copyright, dedication, epigraph, "Four words I could not put down" (ends with a short archer's card) |
| One: The bow (hard work) | 1 The contract nobody signed · 2 Sweat is not a strategy · 3 The ground under the ladder |
| Two: The wind (luck) | 4 Why luck loves the hardworking · 5 The planes that came back · 6 The old man at the frontier · 7 A good decision can lose |
| Three: The written page (destiny) | 8 If the future is fixed, why try? · 9 Reading the page backward · 10 The room you have to act |
| Four: The breath (hope) | 11 When the future you imagined disappears · 12 The thing with feathers · 13 The optimists who did not come home |
| Five: The archer (living with all four) | 14 The door that did not open · 15 Two yeses · 16 Hold on, or let go · 17 The archer's discipline · 18 A life larger than the target |
| Back matter | Epilogue: Why try? · The lines worth keeping · Notes and sources · A small request · About the author |

`output/` has the finished files:

- `The-Archer-and-the-Wind.epub` is the file to upload to KDP. It passes EPUBCheck 5.1.0 with no errors or warnings.
- `The-Archer-and-the-Wind-cover.jpg` is the Kindle cover, 1600 x 2560 pixels.
- `The-Archer-and-the-Wind.docx` is the Word version, for editing.
- `The-Archer-and-the-Wind-proof.pdf` is a 6 x 9 inch proof for reading and review (about 180 pages).

`publishing/` has the KDP listing kit (`kdp-listing.md`: description, back-cover copy, keywords, categories, price, checklist), notes for the author (`author-notes.md`: what changed and what to personalize) and the cover thumbnail test (`cover-thumbnail-test.png`).

`build/` has the build script, stylesheets, cover design and fonts.

## Building

Requirements: pandoc 3, Python 3 with `python-docx` and `Pillow`, and Node.js with Playwright and Chromium.

```bash
./build/build.sh
```

The cover is designed in `build/cover.html` and uses Cormorant Garamond (SIL Open Font License) and Inter.

## Other books in this repository

`AI-for-Bridal-Makeup-Artists/` has *AI for Bridal Makeup Artists: A Practical Booking System for Faster Replies, Accurate Quotes and Calm Wedding Mornings*, with its own manuscript, diagrams, build script, finished Kindle files and KDP listing kit. See its README.
