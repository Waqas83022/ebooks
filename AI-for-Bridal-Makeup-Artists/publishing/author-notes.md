# Notes for the author

How the book was built from your plan, what to personalize, and what to check before you publish.

## How the plan became the book

1. Structure. The book follows your outline exactly: Part I (chapters 1 to 4), Part II (chapters 5 to 7) and Appendices A, B and C. An introduction sets up the two rules that run through every chapter (you approve every commitment; client details stay out of the chat) and explains how to set up any AI tool in twenty minutes. A short closing page, "A last word," brings the fictional wedding to an end.
2. Your sample chapter. Chapter 3 keeps your sample almost word for word, including the opening, the 255-minute timing check, the quote prompt, the reviewed quote, the follow-up and the confirmation. Additions: a short section on what to look for in a draft quote, how many follow-ups to send, a script for "Can you hold the date?" and the deposit checklist.
3. The running example. Your sample's booking (October 10, bride plus four, access 7:00, ready by 11:15, $640 total, $160 deposit) is now Amara's wedding and runs through every chapter. The bride is Amara, the hair stylist is Jess, the planner is Dana, the photographer is Theo and the associate artist is Nadia. All are fictional.
4. The numbers. Every figure was checked by hand and stays consistent from chapter to chapter. The running total goes $640 (quote), $655 (maid of honor's lashes, Chapter 4), $790 (mother of the bride plus second-artist travel, Chapter 6) and $805 (lashes added on the morning, Chapter 7). The deposit stays $160. The three practice bookings in Appendix B each have worked answers with their own arithmetic.
5. Your reader toolkit. The intake questions, tracker record, monthly cohort measure, wedding-morning worksheet, schedule prompt and release checklist from your document are all in the book, in Chapters 2, 5 and 7 and in Appendix A.
6. Kindle formatting. Block paragraphs (no indents), shaded boxes for prompts, dashed boxes for templates, gold-bordered boxes for checklists, short lists instead of wide tables, and diagrams designed to read on e-ink and on phones.

## The images

There are 13 diagrams, all drawn for this book from the book's own numbers: the booking path, the "what goes where" brief, the three reply paths, the tracker, the timing window, the anatomy of a quote, the booking status flow, the trial recap, the solo and two-artist timelines, the change impact chart, the revised timeline and the monthly scorecard. Their source is `build/figures.py`, so if you change a number in the text, change it there too and rebuild.

The cover is designed in `build/cover.html` (plum, ivory and blush, with two brushes, two chat bubbles and a five-step timeline) and rendered to a 1600 x 2560 JPG.

A photographic flat lay (brushes, compact, white roses, phone and a paper schedule) was also generated in your Canva account during this session. It couldn't be downloaded into the book because this environment's network blocks Canva's image server. If you'd prefer a photographic cover, you'll find it in Canva's uploads. Check Canva's licence terms for AI-generated images before using it commercially.

## Please personalize

1. About the author. It currently says only that you wrote *The Archer and the Wind* and states the idea behind this book. Add a line about yourself: where you live, what you do and why you wrote a book for bridal artists. If you've worked with makeup artists, say so, because it builds trust. Don't add experience you don't have.
2. The studio's prices. They're the fictional studio's, taken from your sample ($220 bridal, $95 attendants, $40 travel). They're labelled as examples throughout. If you're aiming at a market outside the US, you could add a sentence in the introduction for your readers' currency.
3. Dedication. It's original to this book and yours to change.

## Facts to be aware of

The book avoids statistics and named studies, so there's little to fact-check. Statements that rest on outside facts:

- ChatGPT, Claude, Gemini and Microsoft Copilot are named as examples of chat tools. The book describes settings in general terms ("look for data controls," "look for saved instructions") because menus change often.
- Chapter 7 says that fake or ghost-written reviews are illegal in a growing number of countries, including the United States and the United Kingdom (the US Federal Trade Commission's rule on fake reviews and testimonials, 2024; the UK's Digital Markets, Competition and Consumers Act 2024). It also says that in most countries the photographer owns the copyright in their photos.
- The book tells readers it isn't legal, tax or financial advice, and points them to their own agreements and local data protection rules.

## AI disclosure on KDP

KDP asks whether a book contains AI-generated text, images or translations. This manuscript, its diagrams and its cover were drafted with an AI assistant from your outline and sample chapter. Answer KDP's questions truthfully. Reading the whole book, changing anything that doesn't sound like you, and adding your own experience will make it stronger and make the answer easier to give.

## Rebuilding after edits

Edit the Markdown files in `manuscript/` (or the figures in `build/figures.py`), then run:

```bash
./build/build.sh
```

This regenerates the diagrams, the cover, the EPUB, the DOCX and the proof PDF.
