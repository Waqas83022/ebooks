# AI for Bridal Makeup Artists

*A Practical Booking System for Faster Replies, Accurate Quotes and Calm Wedding Mornings*, by Muhammad Waqas.

A practical, tool-agnostic handbook of about 28,000 words for independent bridal makeup artists, written for Kindle (KDP) publication. It shows how to use any AI chat tool for booking admin while the artist approves every price, date and promise. One fictional wedding runs through the book.

## What is here

`manuscript/` has the book in Markdown, one file per section, in reading order:

| File | Contents |
|---|---|
| 00 | Copyright and dedication |
| 01 | Introduction: The booking happens before the brushes come out |
| 02 to 06 | Part I: 1 Give AI a one-page studio brief · 2 Turn a vague inquiry into a useful reply · 3 Send the quote and secure the booking · 4 Turn the bridal trial into a wedding-day brief |
| 07 to 10 | Part II: 5 Work backward from the ready-by time · 6 Handle late changes without overbooking · 7 Close the booking and track what works |
| 11 to 13 | Appendix A: 17 copy-ready templates · B: Three practice bookings · C: Troubleshooting |
| 14 | A last word · A small request · About the author |

`images/` has the 13 diagrams (1600 px wide PNG), generated from `build/figures.py`.

`output/` has the finished files:

- `AI-for-Bridal-Makeup-Artists.epub` is the file to upload to KDP.
- `AI-for-Bridal-Makeup-Artists-cover.jpg` is the Kindle cover, 1600 x 2560 pixels.
- `AI-for-Bridal-Makeup-Artists.docx` is the Word version, for editing.
- `AI-for-Bridal-Makeup-Artists-proof.pdf` is a 6 x 9 inch proof for reading and review (about 130 pages).

`publishing/` has the KDP listing kit (`kdp-listing.md`: description, keywords, categories, price, checklist) and notes for the author (`author-notes.md`: how the plan became the book, what to personalize, AI disclosure).

`build/` has the build script, stylesheets, figure and cover designs, and fonts.

## Building

Requirements: pandoc 3, Python 3 with `python-docx` and `Pillow`, and Node.js with Playwright and Chromium.

```bash
./build/build.sh
```
