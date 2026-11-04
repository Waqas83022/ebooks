# Notes for the author

## How the book differs from the original plan

The plan document proposed a 28,000 to 35,000-word handbook with 12 chapters. The finished book keeps the plan's strongest ideas: the three paths (solo, employees, chair renters), the shop brief, counting completed visits rather than bookings, one change at a time, the quiet-slot sample chapter and the 30-day rollout. It changes these things:

- **Fourteen chapters in four parts**, about 47,000 words. The new chapters are Chapter 1 (what AI can and cannot do, with the "AI drafts, you decide" rule) and Chapter 13 (back office and automations, split out from the team chapter).
- **A running cast.** Cedar Street Barbers appears throughout, with Dre (owner), Tomás (commission barber) and Keisha (chair renter), so every technique is shown on a real-feeling shop. Each chapter opens with a scene from the shop.
- **Researched rules and benchmarks**: the FTC's 2024 fake-review rule, Google's review-incentive policy and local ranking factors, US texting consent and quiet hours, Zenoti's 2026 barbershop benchmarks, the Air Canada chatbot ruling and the barbershop blood-pressure study. Sources are in the Notes.
- **100 prompts** in Appendix A, plus scripts (Appendix B), 15 worksheets (Appendix C) and three worked cases (Appendix D).
- **15 diagrams**, designed to stay readable in grayscale on e-ink Kindles.
- **"Before your next shift"** checklists end every chapter.

## What to personalize

- **About the author** (`manuscript/27-about.md`). It is deliberately modest and makes no claims about your background. If you have real experience with barbershops, small business or AI, add it in one or two plain sentences. Do not add credentials you do not have.
- **Dedication** (`manuscript/00-front-matter.md`). Change it if you prefer something personal.
- **Prices and products.** Chapter 1 mentions roughly $20 a month for paid chat assistants; Chapter 8 discusses AI receptionists in general terms without prices. Check these before publishing, and again for any new edition.

## Things to check before publishing

- The legal sections (reviews in Chapter 6, texting consent in Chapter 10, gift cards and memberships in Chapter 11, worker classification in Chapter 12) describe US rules in general terms and tell readers to check their own situation. If you plan to market the book mainly outside the US, consider adding a short note for that country.
- **EPUBCheck.** The EPUB was checked for well-formed XHTML, complete manifest, working image references, alt text and cover metadata. The official EPUBCheck tool was not run in this session, because downloading it was not permitted here. To run it yourself: download EPUBCheck from https://github.com/w3c/epubcheck/releases, unzip it, and run `java -jar epubcheck.jar AI-for-Barbershop-Owners.epub`. KDP's own previewer also flags problems on upload.

## A paperback edition

The 6 x 9 inch proof PDF is for reading and review. For a KDP paperback you would need an interior PDF with KDP's margin and bleed settings and a full wraparound cover (front, spine and back), sized for the final page count. The worksheets in Appendix C make the book a good candidate for print, since owners can write in it.

## Rebuilding

From the `ai-for-barbershop-owners` folder:

```bash
./build/build.sh
```

Edit the chapters in `manuscript/`, the diagrams in `build/figures/make_figures.py`, and the cover in `build/cover.html`.
