# AI for Barbershop Owners

*Fill Empty Chairs, Cut No-Shows, and Win Back Your Time with ChatGPT and Simple AI Tools*, by Muhammad Waqas.

A practical handbook of about 47,000 words for independent barbershop owners (solo barbers, shops with employees and chair-rental shops), written for Kindle (KDP) publication. It follows a fictional three-chair shop, Cedar Street Barbers, through every technique, and includes 15 diagrams, 100 copy-and-paste prompts, scripts, worksheets and three worked cases.

## What is here

`manuscript/` has the book in Markdown, one file per section, in reading order:

| Part | Chapters |
|---|---|
| Front matter | Copyright, dedication, Start here: three ways through this book, Introduction: the phone rings mid-fade |
| One: Before you touch a tool | 1 What AI can and can't do in a barbershop · 2 Find where your shop is losing bookings · 3 Give AI the facts about your shop |
| Two: Get found and get chosen | 4 Make your shop easy to find locally · 5 Turn haircut photos into a local content plan · 6 Turn reviews and referrals into local discovery · 7 Test paid ads with a fixed budget |
| Three: Fill the book and keep it full | 8 Never lose a booking to a missed call · 9 Fill quiet weekday slots · 10 No-shows, rebooking and the regulars who drifted away |
| Four: Run a tighter shop | 11 Price for chair time, not just per cut · 12 Coordinate your team and manage walk-ins · 13 Cut the admin and keep shop records straight · 14 Your first 30 days |
| Back matter | Closing: the chair is still the point · A: The prompt library (100 prompts) · B: Scripts and messages · C: Worksheets · D: Three worked cases · Notes and sources · A small request · About the author |

`images/` has the 15 diagrams used in the book (rendered from `build/figures/make_figures.py`).

`output/` has the finished files:

- `AI-for-Barbershop-Owners.epub` is the file to upload to KDP.
- `AI-for-Barbershop-Owners-cover.jpg` is the Kindle cover, 1600 x 2560 pixels.
- `AI-for-Barbershop-Owners.docx` is the Word version, for editing.
- `AI-for-Barbershop-Owners-proof.pdf` is a 6 x 9 inch proof for reading and review (about 220 pages).

`publishing/` has the KDP listing kit (`kdp-listing.md`: description, keywords, categories, price, AI disclosure, checklist), notes for the author (`author-notes.md`) and a cover thumbnail test.

`build/` has the build script, stylesheets, cover design, figure source and fonts.

## Building

Requirements: pandoc 3, Python 3 with `python-docx` and `Pillow`, and Node.js with Playwright and Chromium.

```bash
./build/build.sh
```
