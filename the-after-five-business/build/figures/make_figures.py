"""Write figures.html: every book figure as a <div class="fig" id="figNN-name">.

Rendered to PNG by render.js (mode "figures"). Each figure is drawn in HTML/CSS
at 800 CSS px wide and captured at 2x, so the PNGs are 1600 px wide.
Colors are chosen to stay legible in grayscale on e-ink Kindles.
Usage: python3 build/figures/make_figures.py build/figures/figures.html
"""
import sys

F = []


def fig(fid, html):
    F.append(f'<div class="fig" id="{fid}">{html}</div>')


# 1. Ten-week roadmap ---------------------------------------------------------
prep = [("1", "Protect five hours. Check your contract and draw the clean line.", "Ch 2–3"),
        ("2", "List your skills, run the four filters, choose one service.", "Ch 4–5"),
        ("3", "Write the offer card, set up your tools, build a sample.", "Ch 6–10"),
        ("4", "Price it, write the proposal, list fifty warm contacts.", "Ch 11–16")]
pilot = [("5", "Send thirty personal messages. Share the sample.", ""),
         ("6", "Discovery calls. Send proposals. Take deposits.", ""),
         ("7", "Deliver project one: intake and drafting.", ""),
         ("8", "Review, quality gates, client check. Start project two.", ""),
         ("9", "Final delivery, sign-off, testimonial, invoices.", ""),
         ("10", "Review the evidence and decide.", "")]


def weeks(items, cls):
    out = ""
    for w, txt, ch in items:
        tag = f'<span class="small" style="float:right">{ch}</span>' if ch else ""
        out += (f'<div class="box {cls}" style="padding:9px 12px"><div class="lbl {"a" if cls=="a" else "n"}">Week {w}{tag}</div>'
                f'<div class="p" style="margin-top:2px">{txt}</div></div>')
    return out


fig("fig01-roadmap", f'''
<div class="t">Ten weeks from this page to a decision</div>
<div class="st">Five hours a week. Four weeks to prepare, six weeks to run a paid pilot.</div>
<div class="row">
 <div class="col" style="flex:1"><div class="h" style="margin-bottom:2px">Prepare</div>{weeks(prep, "")}</div>
 <div class="col" style="flex:1"><div class="h" style="margin-bottom:2px">Pilot</div>{weeks(pilot, "a")}</div>
</div>
<div class="note">At the end of week 10 you choose one of four outcomes: repeat, reprice, redesign or retire the offer (Chapter 17).</div>
''')

# 2. AI vs you ----------------------------------------------------------------
stages = [("You", "Scope", "Find the real problem and the outcome."),
          ("You", "Inputs", "Ask the right questions, gather the right material."),
          ("AI", "Draft and sort", "Transcribe, summarize, draft, compare, reformat."),
          ("You", "Check", "Catch what is wrong, missing or made up."),
          ("You", "Fit and sign", "Make it work for this client. Stand behind it.")]
cells = ""
for who, h, p in stages:
    cls = "a" if who == "AI" else ""
    cells += (f'<div class="box {cls}" style="flex:1;padding:12px 10px">'
              f'<div class="lbl {"a" if cls else "n"}">{"AI tools" if who=="AI" else "You"}</div>'
              f'<div class="h" style="font-size:18px;margin-top:4px">{h}</div><div class="p" style="font-size:15px">{p}</div></div>')
fig("fig02-ai-vs-you", f'''
<div class="t">Where AI helps, and where you are paid</div>
<div class="st">The tools make the middle of the job fast. The ends of the job need your judgment, and that is what clients pay for.</div>
<div class="row" style="gap:8px">{cells}</div>
<div class="row" style="gap:8px;margin-top:10px">
 <div style="flex:2;border-top:4px solid var(--navy);padding-top:6px" class="small"><b style="color:var(--navy)">Your judgment</b></div>
 <div style="flex:1;border-top:4px solid var(--amber);padding-top:6px" class="small"><b style="color:var(--amber)">Cheap and fast</b></div>
 <div style="flex:2;border-top:4px solid var(--navy);padding-top:6px" class="small"><b style="color:var(--navy)">Your judgment</b></div>
</div>
<div class="note">The one-sentence test: if a client typed one sentence into a chatbot, how close would they get to what you sell? The further away, the stronger the offer.</div>
''')

# 3. Five-hour week ------------------------------------------------------------
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
bands = ["Morning", "Daytime", "Evening"]
plan = {("Tue", "Evening"): ("a", "Session A", "7:30–9:30 pm"),
        ("Thu", "Evening"): ("n", "Admin hour", "8:00–9:00 pm"),
        ("Sat", "Morning"): ("a", "Session B", "8:00–10:00 am")}
grid = '<div style="display:grid;grid-template-columns:96px repeat(7,1fr);gap:5px">'
grid += '<div></div>' + "".join(f'<div class="lbl m" style="text-align:center;padding-bottom:4px">{d}</div>' for d in days)
for b in bands:
    grid += f'<div class="lbl m" style="display:flex;align-items:center">{b}</div>'
    for d in days:
        if (d, b) in plan:
            c, h, tm = plan[(d, b)]
            bg = "var(--amber)" if c == "a" else "var(--navy)"
            grid += (f'<div style="background:{bg};color:#fff;border-radius:8px;padding:8px 6px;min-height:78px">'
                     f'<div style="font-size:15px;font-weight:800">{h}</div><div style="font-size:13px;margin-top:3px">{tm}</div></div>')
        elif b == "Daytime" and d not in ("Sat", "Sun"):
            grid += '<div style="background:var(--soft);border:1px solid var(--line);border-radius:8px;min-height:78px;display:flex;align-items:center;justify-content:center" class="small">Day job</div>'
        else:
            grid += '<div style="border:1px dashed var(--line);border-radius:8px;min-height:78px"></div>'
grid += "</div>"
fig("fig03-five-hour-week", f'''
<div class="t">A five-hour week</div>
<div class="st">Two two-hour work sessions and one admin hour, placed around a full-time job.</div>
{grid}
<div class="row" style="margin-top:16px;gap:18px">
 <div class="small"><span style="display:inline-block;width:14px;height:14px;background:var(--amber);border-radius:3px;vertical-align:-2px"></span> Focused work: 2 × 2 hours</div>
 <div class="small"><span style="display:inline-block;width:14px;height:14px;background:var(--navy);border-radius:3px;vertical-align:-2px"></span> Email, outreach, invoices: 1 hour</div>
</div>
<div class="note">Capacity cap: one active client project at a time, two if one is a repeat.</div>
''')

# 4. Clean line ----------------------------------------------------------------
emp = ["Working hours", "Company laptop, phone and network", "Company accounts and software licenses",
       "Company data, documents and templates", "Clients, suppliers and colleagues", "Confidential information"]
biz = ["Your evenings and weekends", "Your own laptop and phone", "Accounts you pay for yourself",
       "Templates you build from scratch", "Your own network and new buyers", "Your general skill and experience"]
li = lambda xs: "".join(f'<div class="p" style="padding:7px 0;border-bottom:1px solid var(--line)">{x}</div>' for x in xs)
fig("fig04-clean-line", f'''
<div class="t">The clean line</div>
<div class="st">Your business is built only from what is on the right. Nothing crosses the line, in either direction.</div>
<div class="row" style="gap:0">
 <div style="flex:1;padding-right:22px"><div class="lbl m">Belongs to your employer</div>{li(emp)}</div>
 <div style="width:6px;background:var(--amber);border-radius:3px"></div>
 <div style="flex:1;padding-left:22px"><div class="lbl n">Your business uses</div>{li(biz)}</div>
</div>
<div class="note">Check your contract for outside-work, IP, confidentiality, conflict and non-solicitation clauses, and any visa or professional rules, before your first client.</div>
''')

# 5. Offer filter ----------------------------------------------------------------
levels = [("100%", "g", "Your skill list", "15–20 lines: “I can take X and turn it into Y for Z.”"),
          ("90%", "", "Filter 1", "It is clearly mine, and clear of my employer."),
          ("78%", "", "Filter 2", "AI speeds up the middle, but cannot do the whole job."),
          ("66%", "", "Filter 3", "A buyer feels the pain often and can pay to fix it."),
          ("54%", "", "Filter 4", "A first project fits in 6–12 hours of evening sessions."),
          ("42%", "a", "What is left", "One or two strong service ideas.")]
lv = ""
for w, c, h, p in levels:
    lv += (f'<div class="box {c}" style="width:{w};margin:0 auto 7px;padding:10px 14px;text-align:center">'
           f'<div class="lbl {"a" if c=="a" else ("m" if c=="g" else "n")}">{h}</div><div class="p" style="margin-top:2px">{p}</div></div>')
fig("fig05-offer-filter", f'''
<div class="t">The offer filter</div>
<div class="st">Run every skill through all four questions. Keep only the ideas that pass every one.</div>
{lv}
''')

# 6. Offer anatomy -----------------------------------------------------------------
parts = [("Name", "Starter Process Manual"),
         ("Buyer", "Trade businesses with 5 to 30 staff"),
         ("Outcome", "Three jobs a new hire can do without calling you"),
         ("Deliverables", "3 procedures + one-page checklists, editable file"),
         ("Inputs", "60-minute recorded interview within 5 days"),
         ("Timeline", "10 working days from the interview"),
         ("Revisions", "One round, within 7 days"),
         ("Not included", "Legal, insurance or safety compliance review"),
         ("Price and terms", "$450 · half on booking, half on delivery"),
         ("How I work", "AI transcribes and drafts; I review every step")]
rows = "".join(f'<div style="display:flex;border-bottom:1px solid var(--line);padding:9px 0">'
               f'<div class="lbl n" style="width:190px;padding-top:3px">{k}</div><div class="p" style="flex:1;margin:0">{v}</div></div>'
               for k, v in parts)
fig("fig06-offer-anatomy", f'''
<div class="t">Anatomy of a fixed-scope offer</div>
<div class="st">Ten parts, one page. Dana's offer as the example.</div>
<div style="border:2px solid var(--navy);border-radius:12px;padding:6px 20px 8px;border-left:10px solid var(--amber)">{rows}</div>
''')

# 7. Six-part brief ---------------------------------------------------------------
brief = [("1", "Context", "Who it is for, their situation, why it matters."),
         ("2", "Task", "Exactly what you want done."),
         ("3", "Inputs", "The material to work from, clearly marked."),
         ("4", "Constraints", "Rules: use only the inputs, mark gaps, no guessing."),
         ("5", "Format", "What the output should look like, section by section."),
         ("6", "Checks", "What the assistant should flag for you to verify.")]
tiles = "".join(f'<div class="box {"a" if n in ("4","6") else ""}" style="padding:14px">'
                f'<div class="lbl {"a" if n in ("4","6") else "n"}">Part {n}</div><div class="h" style="margin-top:3px">{h}</div><div class="p">{p}</div></div>'
                for n, h, p in brief)
fig("fig07-six-part-brief", f'''
<div class="t">The six-part brief</div>
<div class="st">Brief an AI assistant the way you would brief a fast new colleague who knows nothing about the client.</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px">{tiles}</div>
<div class="note">Parts 4 and 6 do the most to prevent invented facts and missing steps.</div>
''')

# 8. Manual pipeline --------------------------------------------------------------
steps = [("You", "Interview", "65 minutes, recorded with consent. Chase every “obviously.”"),
         ("AI", "Transcript", "Remove names that slipped in. Mark where each job starts."),
         ("AI", "First draft", "Six-part brief: only what the owner said; gaps as questions."),
         ("You", "Line-by-line review", "Missing steps, invented steps, wrong order, wrong words."),
         ("Client", "Owner check", "Answers the questions; confirms every safety step."),
         ("You", "Final and checklists", "Corrections, one-page checklists, delivery.")]
cells = ""
for i, (who, h, p) in enumerate(steps, 1):
    cls = "a" if who == "AI" else ("g" if who == "Client" else "")
    lab = {"AI": "AI tools", "You": "You", "Client": "The client"}[who]
    cells += (f'<div class="box {cls}" style="padding:12px"><div class="lbl {"a" if cls=="a" else ("m" if cls=="g" else "n")}">{i} · {lab}</div>'
              f'<div class="h" style="margin-top:3px">{h}</div><div class="p" style="font-size:15px">{p}</div></div>')
fig("fig08-manual-pipeline", f'''
<div class="t">From one conversation to a process manual</div>
<div class="st">Dana's six steps. The AI saves hours of typing; the review is what the client pays for.</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px">{cells}</div>
''')

# 9. Provenance --------------------------------------------------------------------
tbl = [("Annual price, 60 volunteers", "From vendor pricing page", "Pricing page link", "14 Mar"),
       ("Training expiry tracking", "Yes, with reminders", "Help article link", "14 Mar"),
       ("Mobile sign-up", "Web page, no app", "Feature page + own test", "15 Mar")]
trs = "".join(f'<tr>{"".join(f"<td>{c}</td>" for c in r)}</tr>' for r in tbl)
fig("fig09-provenance", f'''
<style>#fig09-provenance table{{width:100%;border-collapse:collapse;font-size:16px}}
#fig09-provenance th{{text-align:left;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--navy);border-bottom:3px solid var(--navy);padding:8px 8px}}
#fig09-provenance td{{border-bottom:1px solid var(--line);padding:10px 8px;vertical-align:top}}</style>
<div class="t">Every fact has a source and a date</div>
<div class="st">Ravi's fact sheet. Each row traces back to a page he opened himself.</div>
<table><tr><th>Fact</th><th>Value</th><th>Source</th><th>Checked</th></tr>{trs}</table>
<div class="row" style="margin-top:18px">
 <div class="box g" style="flex:1"><div class="lbl m">Never</div><div class="p">A price, feature or statistic taken from an AI model's memory.</div></div>
 <div class="box a" style="flex:1"><div class="lbl a">Always</div><div class="p">Facts extracted from a source you opened, then re-checked against it.</div></div>
</div>
''')

# 10. Automation loop -----------------------------------------------------------
flow = [("", "1. Enquiry form", "A couple fills in the photographer's form."),
        ("", "2. Log", "New row in a spreadsheet, with a timestamp."),
        ("", "3. Date check", "Booked-dates calendar: free, booked or unknown."),
        ("a", "4. AI draft", "Gets only the message, first names, date status, package guide."),
        ("", "5. Owner approves", "Draft goes to her phone: approve, or edit first."),
        ("", "6. Send and update", "Sent from her own email; log updated.")]
fl = ""
for i, (c, h, p) in enumerate(flow):
    fl += (f'<div class="box {c}" style="padding:9px 14px"><div class="h" style="font-size:17px">{h}</div>'
           f'<div class="p" style="font-size:15px;margin-top:1px">{p}</div></div>')
    if i < len(flow) - 1:
        fl += '<div class="arrow" style="font-size:18px">▼</div>'
fig("fig10-automation-loop", f'''
<div class="t">An enquiry system with a person in charge</div>
<div class="st">Nothing reaches a customer until the owner approves it.</div>
<div class="row" style="gap:18px">
 <div class="col" style="flex:1.25;gap:4px">{fl}</div>
 <div class="col" style="flex:1;gap:12px">
  <div class="lbl m" style="margin-top:4px">If anything fails</div>
  <div class="box g"><div class="h" style="font-size:16px">AI error or timeout</div><div class="p" style="font-size:15px">Enquiry still lands in the inbox. Reply by hand.</div></div>
  <div class="box g"><div class="h" style="font-size:16px">Calendar unreadable</div><div class="p" style="font-size:15px">Status “unknown.” The draft does not mention availability.</div></div>
  <div class="box g"><div class="h" style="font-size:16px">No approval in 24 hours</div><div class="p" style="font-size:15px">Reminder to the owner. Nothing is ever sent automatically.</div></div>
  <div class="box g"><div class="h" style="font-size:16px">Spam or out of scope</div><div class="p" style="font-size:15px">No reply drafted. Flagged “for review.”</div></div>
 </div>
</div>
''')

# 11. Outreach funnel ---------------------------------------------------------------
fun = [(40, "personal messages sent"), (24, "replies"), (9, "introductions offered"),
       (6, "conversations"), (2, "paid projects")]
bars = ""
for n, lab in fun:
    w = n / 40 * 100
    col = "var(--amber)" if n == 2 else "var(--navy)"
    bars += (f'<div style="display:flex;align-items:center;margin-bottom:10px">'
             f'<div style="width:62%"><div style="width:{w:.1f}%;min-width:14px;height:34px;background:{col};border-radius:0 4px 4px 0"></div></div>'
             f'<div style="flex:1;padding-left:14px"><span style="font-size:24px;font-weight:800">{n}</span> <span class="p">{lab}</span></div></div>')
fig("fig11-outreach-funnel", f'''
<div class="t">What forty personal messages can do</div>
<div class="st">Dana's first two weeks of warm-network outreach, about three hours of admin time.</div>
<div style="border-left:2px solid var(--line);padding:6px 0">{bars}</div>
<div class="note">Illustrative numbers from one warm-network start. Messages to strangers get far fewer replies. Track your own figures from the first message.</div>
''')

# 12. Price build ---------------------------------------------------------------------
def x(v):  # 0..2000 -> 0..100%
    return v / 2000 * 100


fig("fig12-price-build", f'''
<div class="t">Building a price</div>
<div class="st">Find the floor, check the market, judge the value. The price sits between the floor and the value. Dana's numbers for a three-procedure manual.</div>
<div style="position:relative;height:250px;margin:6px 10px 0">
 <div style="position:absolute;left:0;right:0;top:150px;height:2px;background:var(--muted)"></div>
 {''.join(f'<div style="position:absolute;left:{x(v)}%;top:146px;width:2px;height:10px;background:var(--muted)"></div><div class="small" style="position:absolute;left:{x(v)}%;top:162px;transform:translateX(-50%)">${v:,}</div>' for v in (0,500,1000,1500,2000))}
 <div style="position:absolute;left:{x(200)}%;width:{x(1800)}%;top:110px;height:26px;background:var(--navysoft);border:2px solid var(--navy);border-radius:6px"></div>
 <div class="small" style="position:absolute;left:{x(820)}%;top:84px;color:var(--navy);font-weight:700">Market range: about $200 to $2,000+</div>
 <div style="position:absolute;left:{x(480)}%;top:62px;width:3px;height:88px;background:var(--ink)"></div>
 <div style="position:absolute;left:{x(480)}%;top:10px;transform:translateX(-50%);font-size:15px;font-weight:800;text-align:center;line-height:1.2">Floor<br>~$480</div>
 <div style="position:absolute;left:{x(1000)}%;width:{x(1000)}%;top:200px;height:12px;background:var(--amber);border-radius:6px"></div>
 <div class="small" style="position:absolute;left:{x(1000)}%;top:218px;color:var(--amber);font-weight:700">Value to the buyer: well over $1,000 a year</div>
 <div style="position:absolute;left:{x(450)}%;top:118px;width:14px;height:14px;border-radius:7px;background:var(--amber);transform:translate(-50%,-2px);border:2px solid #fff"></div>
 <div style="position:absolute;left:{x(600)}%;top:118px;width:14px;height:14px;border-radius:7px;background:var(--amber);transform:translate(-50%,-2px);border:2px solid #fff"></div>
 <div style="position:absolute;left:{x(900)}%;top:118px;width:14px;height:14px;border-radius:7px;background:var(--amber);transform:translate(-50%,-2px);border:2px solid #fff"></div>
</div>
<div class="row" style="gap:10px;margin-top:4px">
 <div class="box" style="flex:1"><div class="lbl n">1 · Floor</div><div class="p">(Target income ÷ (1 − tax rate) + costs) ÷ delivery hours. About $60 an hour × 8 hours.</div></div>
 <div class="box" style="flex:1"><div class="lbl n">2 · Market</div><div class="p">Similar freelancers, the buyer's alternatives, budgets heard on calls.</div></div>
 <div class="box a" style="flex:1"><div class="lbl a">3 · Value</div><div class="p">Owner hours saved on training, fewer callbacks. Dots: $450 pilot, $600 standard, $900 larger package.</div></div>
</div>
''')

# 13. Quality gates ---------------------------------------------------------------------
gates = [("1", "Faithful to the inputs", "Nothing added that the inputs don't support. Nothing important missing."),
         ("2", "Correct about the world", "Every fact sourced and dated. Every link works."),
         ("3", "Fit for the client", "Their words, their tools, their reader."),
         ("4", "Safe and complete", "Unqualified points flagged. No stray personal data. All deliverables.")]
g = ""
for n, h, p in gates:
    g += (f'<div class="box" style="flex:1;padding:12px;border-top:8px solid var(--navy)"><div class="lbl n">Gate {n}</div>'
          f'<div class="h" style="font-size:18px;margin-top:3px">{h}</div><div class="p" style="font-size:15px">{p}</div></div>')
fig("fig13-quality-gates", f'''
<div class="t">Four gates before the client sees anything</div>
<div class="st">Every deliverable passes all four, in order, every time. The fifth project is when people start skipping them.</div>
<div class="row" style="gap:8px">{g}<div class="box a" style="width:92px;display:flex;align-items:center;justify-content:center;text-align:center"><div class="h" style="font-size:17px">To the client</div></div></div>
''')

# 14. Where money goes -----------------------------------------------------------------
parts = [(30, "Payment fees", "var(--line)", "#1b2430"), (60, "Tools", "#8b95a3", "#fff"),
         (255, "Tax set-aside (28% of profit)", "var(--navy)", "#fff"), (655, "Yours to keep", "var(--amber)", "#fff")]
seg = "".join(f'<div style="flex:{v};background:{c};height:70px;display:flex;align-items:center;justify-content:center;color:{tc};font-weight:800;font-size:18px">{"" if v<100 else "$"+str(v)}</div>' for v, l, c, tc in parts)
legend = "".join(f'<div style="display:flex;align-items:center;gap:10px;padding:7px 0;border-bottom:1px solid var(--line)"><span style="width:18px;height:18px;border-radius:4px;background:{c};display:inline-block"></span><span class="p" style="flex:1;margin:0">{l}</span><span style="font-size:18px;font-weight:800">${v}</span></div>' for v, l, c, tc in parts)
fig("fig14-where-money-goes", f'''
<div class="t">Where $1,000 of revenue goes</div>
<div class="st">An example month: card fees of 3 percent, $60 of tools, and 28 percent of profit set aside for tax.</div>
<div style="display:flex;gap:2px;border-radius:6px;overflow:hidden">{seg}</div>
<div style="margin-top:14px">{legend}</div>
<div class="note">Your tax rate depends on your country, bracket and deductions. Set aside a percentage of every payment on the day it arrives (Chapter 15).</div>
''')

# 15. Effective rate chart ------------------------------------------------------------------
proj = [("1", 38.18, "First client"), ("2", 44.21, "Second client"), ("3", 71.88, "Repeat"),
        ("4", 64.07, "Scope creep"), ("5", 87.00, "Larger package")]
H = 300
mx = 100
bars = ""
for n, v, note in proj:
    h = v / mx * H
    col = "var(--amber)" if n == "4" else "var(--navy)"
    bars += (f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:{H}px">'
             f'<div style="font-size:20px;font-weight:800;margin-bottom:6px">${v:.0f}</div>'
             f'<div style="width:62%;height:{h:.0f}px;background:{col};border-radius:4px 4px 0 0"></div></div>')
grid = "".join(f'<div style="position:absolute;left:0;right:0;bottom:{v/mx*H:.0f}px;border-top:1px solid #e3e6ea"></div><div class="small" style="position:absolute;left:-46px;bottom:{v/mx*H-9:.0f}px">${v}</div>' for v in (25, 50, 75, 100))
labels = "".join(f'<div style="flex:1;text-align:center"><div style="font-size:16px;font-weight:700">Project {n}</div><div class="small">{note}</div></div>' for n, v, note in proj)
fig("fig15-effective-rate", f'''
<div class="t">Dana's effective hourly rate, first five projects</div>
<div class="st">(Price − direct costs) ÷ every hour spent, including finding the client. Before tax.</div>
<div style="position:relative;margin-left:50px;border-bottom:2px solid var(--muted)">{grid}<div style="position:relative;display:flex">{bars}</div></div>
<div style="display:flex;margin:10px 0 0 50px">{labels}</div>
<div class="note">Templates and repeat work pushed the rate up. On project 4, two unpriced extra procedures and a second interview pulled it down.</div>
''')

# 16. Six-week pilot ---------------------------------------------------------------------------
acts = [("Outreach messages", [1, 1, .4, .4, 0, 0], "n"),
        ("Calls and proposals", [0, 1, .4, 0, 0, 0], "n"),
        ("Project one", [0, 0, 1, 1, 1, 0], "a"),
        ("Project two", [0, 0, 0, 1, 1, .5], "a"),
        ("Logs and invoices", [0, 0, 0, 0, 1, 1], "n"),
        ("Review and decide", [0, 0, 0, 0, 0, 1], "a")]
gg = '<div style="display:grid;grid-template-columns:190px repeat(6,1fr);gap:6px;align-items:center">'
gg += "<div></div>" + "".join(f'<div class="lbl m" style="text-align:center">Week {i}</div>' for i in range(1, 7))
for name, ws, c in acts:
    gg += f'<div class="p" style="margin:0;font-weight:600">{name}</div>'
    for w in ws:
        if w == 0:
            gg += '<div style="height:34px;border-radius:6px;background:var(--soft)"></div>'
        else:
            col = "var(--amber)" if c == "a" else "var(--navy)"
            op = "1" if w == 1 else ".45"
            gg += f'<div style="height:34px;border-radius:6px;background:{col};opacity:{op}"></div>'
gg += "</div>"
fig("fig16-six-week-pilot", f'''
<div class="t">The six-week pilot</div>
<div class="st">Two sessions and one admin hour each week. Lighter bars mean a smaller share of that week.</div>
{gg}
<div class="note">The plan will slip. Keep the end date and adjust what you expect to have finished by then.</div>
''')

# 17. Decision tree --------------------------------------------------------------------------------
def q(text):
    return f'<div class="box" style="flex:1.1;padding:12px 14px"><div class="h" style="font-size:18px">{text}</div></div>'


def no(lbl, text):
    return (f'<div style="width:52px;text-align:center" class="lbl m">No →</div>'
            f'<div class="box g" style="flex:1;padding:12px 14px"><div class="lbl n">{lbl}</div><div class="p" style="font-size:15px">{text}</div></div>')


yes = '<div class="lbl m" style="padding:6px 0 6px 18px">Yes ▼</div>'
fig("fig17-decision-tree", f'''
<div class="t">The week-six decision</div>
<div class="st">Answer three questions from your logs, not your hopes.</div>
<div class="row" style="align-items:center">{q("Did people buy, after real outreach?")}{no("Redesign or retire", "Change the buyer or the offer and run again. Retire after a second failed pilot.")}</div>
{yes}
<div class="row" style="align-items:center">{q("Is the effective rate at or near your floor?")}{no("Reprice", "Raise the price, add a larger option, or cut the scope so it takes fewer hours.")}</div>
{yes}
<div class="row" style="align-items:center">{q("Did it fit your hours, your energy and your job?")}{no("Redesign or retire", "Fewer hours per project, longer timelines, or stop if it is harming you.")}</div>
{yes}
<div class="box a" style="padding:14px"><div class="lbl a">Repeat</div><div class="h" style="margin-top:2px">Run another six weeks with the same offer, moving toward your standard price.</div></div>
''')

html = ('<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"></head><body>'
        + "\n".join(F) + "</body></html>")
open(sys.argv[1], "w", encoding="utf-8").write(html)
print("wrote", len(F), "figures")
