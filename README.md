# The Archer and the Wind

*Hard Work, Luck, Destiny, and the Hope That Holds Them Together*, by Muhammad Waqas.

A nonfiction book of about 46,000 words on how hard work, luck, destiny and hope (including prayer) fit together, and how to keep going when none of them can guarantee the result. It is written for Kindle (KDP) publication.

## What is here

`manuscript/` has the book in Markdown, one file per section, in reading order:

| Part | Chapters |
|---|---|
| Front matter and introduction | Copyright, dedication, epigraph, "Four words I could not put down" |
| One: The bow (hard work) | 1 The contract nobody signed · 2 Sweat is not a strategy · 3 The ground under the ladder |
| Two: The wind (luck) | 4 Why luck loves the hardworking · 5 The drowned do not paint pictures · 6 The old man at the frontier · 7 A good decision can lose |
| Three: The written page (destiny) | 8 If it is written, why write? · 9 Reading the page backward · 10 The room you have to act |
| Four: The breath (prayer and hope) | 11 Trust, and tie the camel · 12 The thing with feathers · 13 The optimists who did not come home |
| Five: The archer (living with all four) | 14 The job that did not come · 15 The person we hoped to marry · 16 Hold on, or let go · 17 The archer's discipline · 18 A life larger than the target |
| Back matter | Epilogue: Why try? · The lines worth keeping · Notes and sources · A small request · About the author |

`output/` has the finished files:

- `The-Archer-and-the-Wind.epub` is the file to upload to KDP. It passes EPUBCheck 5.1.0 with no errors or warnings.
- `The-Archer-and-the-Wind-cover.jpg` is the Kindle cover, 1600 x 2560 pixels.
- `The-Archer-and-the-Wind.docx` is the Word version, for editing.
- `The-Archer-and-the-Wind-proof.pdf` is a 6 x 9 inch proof for reading and review (about 190 pages).

`publishing/` has the KDP listing kit (`kdp-listing.md`: description, keywords, categories, price, checklist) and notes for the author (`author-notes.md`: what to personalize and check).

`build/` has the build script, stylesheets, cover design and fonts.

## Building

Requirements: pandoc 3, Python 3 with `python-docx` and `Pillow`, and Node.js with Playwright and Chromium.

```bash
./build/build.sh
```

The cover is designed in `build/cover.html` and uses Cormorant Garamond (SIL Open Font License) and Inter.
