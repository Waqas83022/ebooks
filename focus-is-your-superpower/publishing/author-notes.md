# Notes for the author

## How the book differs from the sample

The sample document was treated as a starting idea, not a fixed plan. The finished book keeps its strongest parts: the title and subtitle, the five-part structure, the FOCUS framework (Find, Organize, Control, Use, Sustain), the reader diagnostic, the 30-day challenge and your product description. It changes these things:

- **Every chapter is fully written.** The sample had an introduction and one chapter. The book now has twenty chapters, an introduction, a "Start here" guide and a closing, about 47,000 words in all. The introduction and Chapter 1 were rewritten from scratch in a plainer voice.
- **Four running characters.** Sana (a pharmacy student), Daniel (a project manager working from home), Amira (a freelance designer with an online shop) and Tariq (an accountant learning to code). Every technique is shown in a real-feeling life. The copyright page says they are composites.
- **"Hallucination" is handled carefully.** Your brief asked for help avoiding hallucination. Chapter 4 covers what most readers mean by that (vivid daydreams about the future, mind-wandering, worry loops and overthinking) and explains, in two sentences, that true hallucinations are a medical matter. The copyright page and introduction also say when to see a doctor.
- **Every chapter ends with "Try this today" and three reflection questions.**
- **The 30-day challenge is written out in full**, one instruction per day, each pointing to its chapter.
- **A toolkit of 13 worksheets**, such as the daily plan, procrastination log, screen-time audit, if-then planner, WOOP sheet, weekly review and a "which technique should I try?" guide.
- **Research checked against sources.** About forty studies and books are described, and the Notes list them by chapter. Two popular claims are corrected in the text: the "phone on the desk drains your brain" study failed a pre-registered replication in 2022, and the "21 days to form a habit" figure has no good basis (the best study found a median of 66 days, with a range of 18 to 254).
- **Black and white throughout.** The interior has no color. The cover is also black, white and gray, so it matches a black-and-white paperback and stays readable as a small thumbnail (see `cover-thumbnail-test.png`).

## What to personalize

- **About the author** (`manuscript/32-about.md`). It names your other two books and says nothing about your background, because I didn't want to invent anything. If you have real experience with studying, work, teaching or coaching, add one or two plain sentences. Don't add credentials you don't have.
- **Dedication** (`manuscript/00-front-matter.md`). Change it if you'd prefer something personal.
- **A personal story.** The book is written in a warm second-person voice without first-person anecdotes. If you have a true story about your own struggle with focus or procrastination, one or two paragraphs of it in the introduction would make the opening stronger.

## Things to check

- **Phone settings.** Chapter 6 names the screen-time menus on iPhone and Android in general terms. Phone makers rename these menus from time to time; check them against a current phone before publishing.
- **EPUBCheck.** The EPUB was checked here for well-formed XHTML, a complete manifest, working internal links, a navigation file and cover metadata. The official EPUBCheck tool couldn't be run in this session because downloading it wasn't permitted. To run it yourself: download EPUBCheck from https://github.com/w3c/epubcheck/releases, unzip it, and run `java -jar epubcheck.jar Focus-Is-Your-Superpower.epub`. KDP's own previewer also flags problems on upload.

## Rebuilding

From the `focus-is-your-superpower` folder:

```bash
./build/build.sh
```

Edit the chapters in `manuscript/` and the cover in `build/cover.html`, then rebuild. The script regenerates the EPUB, DOCX, proof PDF and cover in `output/`.
