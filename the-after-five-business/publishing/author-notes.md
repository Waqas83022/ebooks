# Notes for the author

These notes explain the choices behind *The After-Five Business* and list what you should personalize or check before publishing.

## How the book differs from the sample plan

The sample plan was used for ideas only. What changed:

1. **Title.** *AI Side Hustles After Work* became *The After-Five Business*. "After five" works twice: after five o'clock, and the five-hour week. The subtitle carries the search phrases (AI-assisted, service business, five hours a week, day job). "Side hustle" goes in the keywords and description, where buyers search for it.
2. **Structure.** Ten chapters became eighteen in five parts, plus an introduction, afterword, a "Questions readers ask" section, a toolkit and notes. The sample's ideas are all here: the five-hour schedule, employer boundaries, turning a skill into an offer, the three pilots (process documentation, public research brief, workflow setup), finding buyers and pricing, protecting client data, measuring real hours, and the six-week pilot with a repeat/reprice/redesign/close decision ("close" became "retire").
3. **Added material the sample did not have:** what the research says AI changes about paid work (Chapter 1); a catalogue of twelve services with honest "watch for" notes and a list of services to avoid (Chapter 5); a tool kit and the six-part brief for any AI assistant (Chapter 7); taxes and paperwork for the US and UK (Chapter 15); growth, burnout and the "should I quit?" question (Chapter 18); and a complete toolkit of templates.
4. **Worked examples run through the whole book.** Dana (process manuals), Ravi (research briefs) and Teresa (enquiry automation) are composites, and the copyright page says so. Their numbers are consistent from chapter to chapter: Dana's first project is 11 hours for $450, her five-project chart in Chapter 16 matches the pricing in Chapter 13, and so on. The sample's "$200 project, $30 costs, six hours = $28.33 an hour" example is used in Chapter 13.
5. **Images.** Seventeen diagrams, drawn in HTML/CSS and rendered at 1600 pixels wide. They use dark navy and amber, which stay distinct in grayscale on e-ink Kindles. Each has a caption and alt text.

## Please personalize

1. **About the author.** It currently says only what is safe to say without your input: that you write practical nonfiction and that you wrote *The Archer and the Wind*. Add your own details: your work, where you live, and why this subject matters to you. If you have run a side business yourself, one or two sentences about it will make the book more credible.
2. **The afterword.** It is written in a neutral first person. If you have a short story of your own about starting something on the side, it would fit well before the final paragraph.
3. **Contact.** The "small request" page asks readers how their pilot went but gives no contact address. Add an email address or website if you want to hear from readers.

Do not add anyone else's private story without their permission.

## Facts to re-check before publishing

These were checked in November 2026 but change often:

- US 1099-NEC/MISC threshold ($2,000 from 2026) and 1099-K threshold ($20,000 and 200 transactions), from the One Big Beautiful Bill Act.
- US self-employment tax (15.3 percent), the $400 filing threshold and the $1,000 estimated-tax rule.
- UK trading allowance (£1,000), Class 4 National Insurance rates (6 and 2 percent for 2025–26) and the Making Tax Digital thresholds (£50,000 from April 2026, £30,000 from April 2027, £20,000 from April 2028).
- Upwork's variable freelancer fee (0 to 15 percent) and Fiverr's 20 percent seller fee.
- The status of the FTC non-compete rule (vacated; appeal dropped September 2025) and of FINRA's proposed Rule 3290.
- UK Skilled Worker supplementary-work rules and US H-1B guidance (the book tells readers to take advice rather than stating a rule).
- The AI-hallucination court database count (about 1,600 cases in mid-2026).

Studies cited and checked against published summaries: Noy and Zhang (*Science*, 2023); Brynjolfsson, Li and Raymond (*QJE*, 2025); Dell'Acqua et al. on the "jagged frontier"; Hui, Reshef and Zhou (*Organization Science*, 2024); Gollwitzer and Sheeran (2006); the Bankrate 2025 side-hustle survey; *Mata v. Avianca* (2023); *Moffatt v. Air Canada* (2024); Samsung's 2023 restriction on generative AI; the New York State and Illinois freelancer-protection laws; the FTC's fake-reviews rule.

The pilot prices in Chapter 5 are the author's estimates, and the notes say so.

## Disclosure to KDP

KDP asks whether a book's text, images or translations are AI-generated. This manuscript was drafted with an AI assistant, so answer "Yes" for text. Answering truthfully is required by KDP's content guidelines, and it is consistent with the book's own advice about being open with clients.

## Rebuilding after edits

Edit the Markdown files in `manuscript/` (figures are defined in `build/figures/make_figures.py`, the cover in `build/cover.html`), then run from the `the-after-five-business` folder:

```bash
./build/build.sh
```

This regenerates the figures, cover, EPUB, DOCX and proof PDF in `output/`. To validate the EPUB:

```bash
pip install epubcheck && epubcheck output/The-After-Five-Business.epub
```
