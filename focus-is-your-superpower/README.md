# Focus Is Your Superpower

*Beat Procrastination, Escape Digital Distractions, and Get More Done Without Burning Out*, by Muhammad Waqas.

A practical self-help book of about 47,000 words on attention, procrastination, phone and social media distraction, planning, habits and energy, written for Kindle (KDP) publication with a black-and-white interior. Four composite characters (a student, a remote-working manager, a freelancer and a father changing careers) carry the techniques through the book. It ends with a 30-day focus challenge and a toolkit of 13 worksheets.

## What is here

`manuscript/` has the book in Markdown, one file per section, in reading order:

| Part | Chapters |
|---|---|
| Front matter | Copyright, dedication, Start here (with the FOCUS method and a two-minute focus check), Introduction: the life you keep postponing |
| One: Why your attention keeps slipping | 1 Busy is not the same as productive · 2 Why you put things off · 3 The feed is built to keep you · 4 The daydream and the loop |
| Two: Take back your attention | 5 Train your focus · 6 The digital reset · 7 Build a room that helps you work · 8 Deep work and single-tasking |
| Three: Plan time that holds | 9 Decide what matters · 10 Plan the day you'll actually live · 11 Start before you feel ready · 12 Work sessions and breaks · 13 Do the right things |
| Four: Keep going when motivation fades | 14 Goals you can act on · 15 Discipline without self-punishment · 16 Habits that carry you · 17 Protect your energy |
| Five: Focus in real life | 18 Focus for students · 19 Focus at work, in business and at home · 20 Your focus system for life |
| Back matter | Closing: the next ordinary day · The 30-day focus challenge · The focus toolkit · Notes and sources · A small request · About the author |

`output/` has the finished files:

- `Focus-Is-Your-Superpower.epub` is the file to upload to KDP.
- `Focus-Is-Your-Superpower-cover.jpg` is the Kindle cover, 1600 x 2560 pixels, in black and white.
- `Focus-Is-Your-Superpower.docx` is the Word version, for editing.
- `Focus-Is-Your-Superpower-proof.pdf` is a 6 x 9 inch proof for reading and review (about 215 pages).

`publishing/` has the KDP listing kit (`kdp-listing.md`: description, keywords, categories, price, AI disclosure, checklist), notes for the author (`author-notes.md`) and a cover thumbnail test.

`build/` has the build script, stylesheets and cover design.

## Building

Requirements: pandoc 3, Python 3 with `python-docx` and `Pillow`, and Node.js with Playwright and Chromium.

```bash
./build/build.sh
```
