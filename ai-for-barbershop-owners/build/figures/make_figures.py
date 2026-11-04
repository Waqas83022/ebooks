"""Write one HTML file per book figure into build/figures/html/.
Rendered to PNG by build/render.js (mode "figure"), then optimized by optimize_images.py.
Designed at 1000 CSS px wide, rendered at 1.5x (1500 px) for Kindle.
Colors are chosen to stay distinct in grayscale on e-ink screens."""
import os

OUT = os.path.join(os.path.dirname(__file__), "html")
os.makedirs(OUT, exist_ok=True)

CSS = """
:root { --ink:#17202a; --muted:#56606c; --line:#c4cad3; --red:#a8322a; --navy:#1f3f63;
        --sand:#f4ede3; --sky:#e4ecf4; --paper:#ffffff; --pale:#f6f7f9; }
* { box-sizing:border-box; }
html,body { margin:0; padding:0; background:#fff; }
body { font-family:Inter, "Liberation Sans", sans-serif; color:var(--ink); width:1000px; }
#fig { width:1000px; padding:44px 48px 48px; background:#fff; }
h1 { font-size:34px; margin:0 0 6px; font-weight:700; letter-spacing:-0.01em; }
.sub { font-size:23px; color:var(--muted); margin:0 0 30px; }
.small { font-size:20px; color:var(--muted); }
"""


def page(name, body, extra_css=""):
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{extra_css}</style></head>
<body><div id="fig">{body}</div></body></html>"""
    with open(os.path.join(OUT, name + ".html"), "w", encoding="utf-8") as f:
        f.write(html)


# 1. Prompt anatomy ---------------------------------------------------------
parts = [
    ("1", "Who you are", "Cedar Street Barbers, a three-chair barbershop at 412 Cedar Street."),
    ("2", "The facts", "Skin fade with a hard part, cut by Tomás. $40, 45 minutes. Booking link: [booking link]."),
    ("3", "The job", "Write an Instagram caption that gets people to book a weekday appointment with Tomás."),
    ("4", "The format", "Under 60 words. Relaxed and confident, like a barber talking to a regular."),
    ("5", "The limits", "No emojis or hashtags. Don't invent any facts. Leave gaps in [brackets]."),
]
rows = "".join(
    f"""<div class="row"><div class="num">{n}</div><div class="lab">{l}</div><div class="ex">{e}</div></div>"""
    for n, l, e in parts)
page("fig01-prompt-anatomy", f"""
<h1>The five parts of a good request</h1>
<p class="sub">Each line from the example prompt in this chapter</p>
{rows}
<div class="out"><b>Result:</b> a caption a barber would actually post, not a hotel brochure.</div>
""", """
.row { display:grid; grid-template-columns:64px 230px 1fr; align-items:center; gap:22px;
       border:2px solid var(--line); border-radius:14px; padding:20px 24px; margin-bottom:14px; }
.row:nth-child(odd) { background:var(--pale); }
.num { width:56px; height:56px; border-radius:50%; background:var(--navy); color:#fff; font-weight:700;
       font-size:28px; display:flex; align-items:center; justify-content:center; }
.lab { font-size:28px; font-weight:700; }
.ex { font-size:23px; line-height:1.35; color:#2b333c; }
.out { margin-top:22px; font-size:24px; padding:18px 24px; border-left:8px solid var(--red); background:var(--sand); border-radius:6px; }
""")

# 2. Leak map ---------------------------------------------------------------
stages = [
    ("Found you", "Wrong hours on Google, no photos, not in search"),
    ("Chose you", "Old reviews, no prices, no way to book"),
    ("Reached you", "Unanswered calls, slow DMs, broken link"),
    ("Booked", "No times showing online, long booking form"),
    ("Showed up", "No reminder, no easy way to reschedule"),
    ("Paid, left happy", "Long waits, rushed cut, surprise price"),
    ("Came back", "Nobody offered the next visit"),
]
rows = []
for i, (s, leak) in enumerate(stages):
    w = 100 - i * 8
    rows.append(f"""<div class="st"><div class="barwrap"><div class="bar" style="width:{w}%">{s}</div></div>
<div class="leak"><span class="drop">▼</span> {leak}</div></div>""")
page("fig02-leak-map", f"""
<h1>The booking leak map</h1>
<p class="sub">From stranger to regular. Every stage loses some people.</p>
<div class="head"><span>Stage</span><span>Common leaks</span></div>
{''.join(rows)}
<div class="note">Leaks near the bottom are usually the cheapest to fix. Start at the chair and work outward.</div>
""", """
.head { display:grid; grid-template-columns:420px 1fr; gap:26px; font-size:20px; text-transform:uppercase;
        letter-spacing:0.08em; color:var(--muted); margin-bottom:8px; }
.st { display:grid; grid-template-columns:420px 1fr; gap:26px; align-items:center; margin-bottom:12px; }
.barwrap { display:flex; justify-content:center; }
.bar { background:var(--navy); color:#fff; font-size:26px; font-weight:700; padding:20px 18px; text-align:center;
       border-radius:8px; }
.st:last-of-type .bar { background:var(--red); }
.leak { font-size:23px; line-height:1.3; }
.drop { color:var(--red); font-size:18px; }
.note { margin-top:24px; font-size:23px; padding:18px 22px; background:var(--sand); border-radius:8px; }
""")

# 3. Weekly scorecard -------------------------------------------------------
sc = [
    ("Chair utilization", "Dre 64% (1,530 of 2,400 min)<br>Tomás 53% (1,260 of 2,400 min)", "Completed minutes ÷ sellable minutes"),
    ("Missed calls and messages answered", "40% (6 of 15)", "Answered or returned ÷ total"),
    ("No-shows / late cancels", "3.2% (4 of 124) / 2.4% (3 of 124)", "Each ÷ appointments due"),
    ("Checkout rebooking", "22% (24 of 108)", "Left with next visit booked ÷ eligible visits"),
    ("First visits completed", "13: Google 5, friend 4, Instagram 2, walk-by 2", "With source, every time"),
    ("Note", "Baseline week. Rain Thursday. Tomás off Saturday afternoon.", "What changed; anything unusual"),
]
rows = "".join(f"""<tr><td class="m">{a}</td><td class="v">{b}</td><td class="h">{c}</td></tr>""" for a, b, c in sc)
page("fig03-scorecard", f"""
<h1>Weekly scorecard</h1>
<p class="sub">Cedar Street Barbers · baseline week · Dre and Tomás</p>
<table><tr><th>Measure</th><th>This week</th><th>How it's counted</th></tr>{rows}</table>
<p class="small" style="margin-top:18px">Keep the count beside every rate. Compare the same weekdays.</p>
""", """
table { width:100%; border-collapse:collapse; font-size:22px; }
th { text-align:left; font-size:19px; text-transform:uppercase; letter-spacing:0.07em; color:var(--muted);
     border-bottom:3px solid var(--ink); padding:10px 12px; }
td { border-bottom:1.5px solid var(--line); padding:18px 12px; vertical-align:top; line-height:1.35; }
td.m { font-weight:700; width:280px; }
td.v { width:380px; }
td.h { color:var(--muted); font-size:20px; }
tr:nth-child(even) td { background:var(--pale); }
""")

# 4. Shop brief -------------------------------------------------------------
brief = [
    ("Basics", "412 Cedar St, next to Lopez Hardware · parking behind, entrance on Pine Alley · book: [booking link]"),
    ("Hours", "Tue–Fri 10–7 · Sat 8–5 · closed Sun, Mon · closed Thanksgiving + Friday after"),
    ("Barbers", "Dre (owner): fades, beards, hot towel · Tomás: skin fades, designs, kids · Keisha (renter): textured hair, own link and prices"),
    ("Menu", "Standard cut $35 / 30 min · Skin fade $40 / 45 · Beard $20 / 15 · Cut + beard $50 / 45 · Kids $25 / 30 · Hot towel $45 / 45 · Full service $75 / 75"),
    ("Booking rules", "Walk-ins Tue–Fri when free · Sat appointments only until 11 · cancel 12 h ahead · 10-min grace · 2 no-shows = $10 deposit"),
    ("How we talk", "Relaxed, direct, short, first names · avoid: experience, elevate, pamper, luxurious"),
    ("Never promise", "A time slot · a discount · a price not listed · anything medical"),
    ("Hand to Dre", "Complaints · refunds · injuries · Keisha's bookings (send her link) · anything not covered"),
]
rows = "".join(f"""<div class="sec"><div class="k">{a}</div><div class="t">{b}</div></div>""" for a, b in brief)
page("fig04-shop-brief", f"""
<div class="doc">
<div class="top"><div><div class="title">Cedar Street Barbers: shop brief</div>
<div class="meta">Updated 4 November · Owner: Dre · One page, one master copy</div></div></div>
{rows}
</div>
""", """
.doc { border:2px solid var(--line); border-radius:12px; padding:34px 38px; box-shadow:0 6px 0 var(--sand); }
.top { border-bottom:4px solid var(--red); padding-bottom:16px; margin-bottom:12px; }
.title { font-size:34px; font-weight:800; }
.meta { font-size:20px; color:var(--muted); margin-top:6px; }
.sec { display:grid; grid-template-columns:210px 1fr; gap:20px; padding:14px 0; border-bottom:1.5px solid var(--line); }
.sec:last-child { border-bottom:none; }
.k { font-size:22px; font-weight:700; color:var(--navy); }
.t { font-size:21px; line-height:1.4; }
""")

# 5. Local search -----------------------------------------------------------
page("fig05-local-search", """
<h1>How Google picks local results</h1>
<p class="sub">Three factors, according to Google's own help pages</p>
<div class="grid">
 <div class="card ctl"><div class="tag">You control</div><h2>Relevance</h2>
  <p>How well your profile matches the search.</p>
  <ul><li>Primary category: Barber shop</li><li>Services listed with prices</li><li>Plain, factual description</li><li>Correct hours and booking link</li></ul></div>
 <div class="card inf"><div class="tag">You influence</div><h2>Prominence</h2>
  <p>How well known the shop is.</p>
  <ul><li>Steady, honest reviews</li><li>A reply to every review</li><li>New photos of real cuts</li><li>Links and mentions from neighbors</li></ul></div>
 <div class="card fix"><div class="tag">Fixed</div><h2>Distance</h2>
  <p>How far you are from the person searching.</p>
  <ul><li>You can't move the shop</li><li>So spend your time on the other two</li></ul></div>
</div>
""", """
.grid { display:grid; grid-template-columns:1fr 1fr 1fr; gap:20px; }
.card { border-radius:14px; padding:24px 22px; border:2px solid var(--line); }
.ctl { background:var(--sky); border-color:var(--navy); }
.inf { background:var(--sand); border-color:var(--red); }
.fix { background:var(--pale); border-style:dashed; }
.tag { font-size:17px; text-transform:uppercase; letter-spacing:0.08em; font-weight:700; color:var(--muted); }
h2 { font-size:32px; margin:8px 0 8px; }
p { font-size:21px; margin:0 0 12px; line-height:1.35; }
ul { margin:0; padding-left:22px; font-size:21px; line-height:1.45; }
""")

# 6. Content calendar -------------------------------------------------------
weeks = [
    ["Real cut: skin fade (Tomás)", "Barber intro: Dre", "Real cut: cut and beard (Dre)", "Openings this week"],
    ["Question: taper or fade?", "Real cut: kids cut", "Before and after: home-cut rescue", "Openings this week"],
    ["Real cut: textured taper (Keisha, her link)", "Availability: Wed and Thu afternoons", "Shop moment: new chair", "Openings this week"],
    ["Barber intro: Tomás", "Real cut: hot towel shave (video)", "Seasonal: back-to-school kids cuts", "Openings this week"],
]
cells = "".join(
    f"<div class='wk'>Week {i+1}</div>" + "".join(f"<div class='c{' g' if j == 3 else ''}'>{t}</div>" for j, t in enumerate(w))
    for i, w in enumerate(weeks))
page("fig06-content-calendar", f"""
<h1>Four-week content calendar</h1>
<p class="sub">Three Instagram posts a week, plus a Google update every Friday</p>
<div class="cal"><div></div><div class="hd">Tuesday</div><div class="hd">Thursday</div><div class="hd">Saturday</div><div class="hd">Friday · Google</div>{cells}</div>
""", """
.cal { display:grid; grid-template-columns:110px repeat(4, 1fr); gap:10px; }
.hd { font-size:20px; font-weight:700; text-transform:uppercase; letter-spacing:0.05em; color:var(--muted); padding:4px 4px 6px; }
.wk { font-size:22px; font-weight:800; display:flex; align-items:center; }
.c { background:var(--sky); border-radius:10px; padding:16px 14px; font-size:20px; line-height:1.3; min-height:118px; border:1.5px solid #c8d6e6; }
.c.g { background:var(--sand); border-color:#e1cfb7; }
""")

# 7. Review flow ------------------------------------------------------------
page("fig07-review-flow", """
<h1>Handling a new review</h1>
<p class="sub">Every review gets a reply. Complaints also get a private conversation.</p>
<div class="start">New review arrives</div>
<div class="arrow">▼</div>
<div class="cols">
 <div class="col"><div class="hd pos">Positive</div>
  <div class="step">Batch weekly with AI</div><div class="step">Short, specific, names the barber</div><div class="step">Vary every opening line</div></div>
 <div class="col"><div class="hd neg">Negative</div>
  <div class="step">Wait until you're calm</div><div class="step">AI drafts; owner edits and approves</div><div class="step">Own the mistake, state policy plainly, no private details</div><div class="step">Invite them to call the owner</div><div class="step">Follow up privately; log it</div></div>
 <div class="col"><div class="hd fake">Not a real client</div>
  <div class="step">Report it to Google</div><div class="step">Short neutral reply: "We can't find a matching visit"</div><div class="step">No accusations, no threats</div></div>
</div>
<div class="rule">Never offer anything in exchange for a review, or for changing one.</div>
""", """
.start { margin:0 auto; width:420px; text-align:center; background:var(--ink); color:#fff; font-size:26px; font-weight:700; padding:18px; border-radius:40px; }
.arrow { text-align:center; font-size:26px; color:var(--muted); margin:8px 0; }
.cols { display:grid; grid-template-columns:1fr 1fr 1fr; gap:18px; }
.hd { font-size:25px; font-weight:800; color:#fff; padding:14px 16px; border-radius:10px 10px 0 0; }
.pos { background:var(--navy); } .neg { background:var(--red); } .fake { background:#5b6470; }
.step { font-size:20px; line-height:1.3; padding:13px 16px; border:1.5px solid var(--line); border-top:none; background:var(--pale); }
.step:last-child { border-radius:0 0 10px 10px; }
.rule { margin-top:24px; font-size:23px; font-weight:700; padding:16px 22px; border:3px solid var(--red); border-radius:10px; text-align:center; }
""")

# 8. Ad test card -----------------------------------------------------------
items = [
    ("One service", "Skin fade with Tomás ($40, 45 min)"),
    ("One audience", "About 3 miles around the shop"),
    ("One booking page", "Skin fade with Tomás, tracked ad link"),
    ("Two versions", "A leads with the cut · B leads with weekday openings (same photo)"),
    ("Spend cap and dates", "$100 over 14 days"),
    ("Primary measure", "Completed first visits from the ad"),
    ("Decision rule", "≤ $25 per completed first visit: run again with one change · > $40 or fewer than 2: stop"),
    ("Review date", "Four days after the ad ends; rebooking checked at six weeks"),
]
rows = "".join(f"<div class='r'><div class='k'>{a}</div><div class='v'>{b}</div></div>" for a, b in items)
page("fig08-ad-test-card", f"""
<h1>Ad test card</h1>
<p class="sub">Filled in before spending a dollar</p>
<div class="card">{rows}</div>
<div class="math"><div class="mh">Results</div>
<div class="eq">$100 spend ÷ 5 completed first visits = <b>$20 per new client</b></div>
<div class="eq">Shop's share per skin fade after 50% commission and $5 costs = <b>$15</b></div>
<div class="eq">Passes the rule, but only pays off if clients return. 3 of 5 rebooked.</div></div>
""", """
.card { border:2px solid var(--ink); border-radius:12px; overflow:hidden; }
.r { display:grid; grid-template-columns:250px 1fr; border-bottom:1.5px solid var(--line); }
.r:last-child { border-bottom:none; }
.k { background:var(--sky); font-size:21px; font-weight:700; padding:15px 18px; }
.v { font-size:21px; padding:15px 18px; line-height:1.35; }
.math { margin-top:22px; background:var(--sand); border-radius:12px; padding:20px 24px; }
.mh { font-size:19px; text-transform:uppercase; letter-spacing:0.08em; font-weight:700; color:var(--muted); margin-bottom:8px; }
.eq { font-size:22px; line-height:1.45; }
""")

# 9. Inquiry routing --------------------------------------------------------
page("fig09-inquiry-routing", """
<h1>Many ways in, one way to book</h1>
<p class="sub">Every reply ends with the booking link or a slot a person has confirmed</p>
<div class="flow">
 <div class="col"><div class="hd">Client reaches out</div>
  <div class="b">Phone call</div><div class="b">Text message</div><div class="b">Instagram or Facebook DM</div><div class="b">Booking app chat</div><div class="b">Walks in</div></div>
 <div class="ar">▶</div>
 <div class="col"><div class="hd">What happens</div>
  <div class="b">Missed? Auto-text within 2 minutes</div><div class="b">Saved reply, between clients</div><div class="b">Saved reply; renters' clients get their own link</div><div class="b">Saved reply or app message</div><div class="b">Walk-in board, honest wait, or the QR card</div></div>
 <div class="ar">▶</div>
 <div class="col end"><div class="hd">Ends with</div>
  <div class="big">Booking link</div><div class="or">or</div><div class="big">Slot confirmed in the calendar by a person</div>
  <div class="who">One named person checks every channel at opening, lunch and close.</div></div>
</div>
""", """
.flow { display:grid; grid-template-columns:1fr 40px 1.15fr 40px 0.95fr; align-items:stretch; gap:6px; }
.hd { font-size:19px; text-transform:uppercase; letter-spacing:0.07em; font-weight:700; color:var(--muted); margin-bottom:10px; }
.b { font-size:20px; line-height:1.3; background:var(--sky); border-radius:8px; padding:14px 14px; margin-bottom:10px; min-height:76px; display:flex; align-items:center; }
.col:nth-child(3) .b { background:var(--pale); border:1.5px solid var(--line); }
.ar { display:flex; align-items:center; justify-content:center; font-size:28px; color:var(--muted); }
.end { background:var(--sand); border-radius:12px; padding:16px; }
.big { font-size:24px; font-weight:800; background:var(--red); color:#fff; border-radius:10px; padding:20px 16px; text-align:center; }
.or { text-align:center; font-size:20px; color:var(--muted); margin:10px 0; }
.who { margin-top:18px; font-size:19px; line-height:1.35; }
""")

# 10. Quiet-slot heatmap ----------------------------------------------------
days = ["Tue", "Wed", "Thu", "Fri", "Sat"]
blocks_wd = ["10–12", "12–2", "2–4", "4–7"]
vals = {
    "Tue": [55, 30, 28, 72],
    "Wed": [52, 26, 24, 70],
    "Thu": [58, 41, 38, 80],
    "Fri": [62, 55, 66, 92],
    "Sat": [96, 94, 88, None],
}
sat_blocks = ["8–11", "11–2", "2–5"]


def shade(v):
    # sequential single hue (navy), light -> dark; text flips to white on dark cells
    stops = [(0, (236, 241, 247)), (40, (177, 197, 220)), (70, (91, 125, 164)), (100, (24, 50, 82))]
    for (a, ca), (b, cb) in zip(stops, stops[1:]):
        if v <= b:
            t = (v - a) / (b - a)
            c = tuple(round(ca[i] + (cb[i] - ca[i]) * t) for i in range(3))
            return "rgb(%d,%d,%d)" % c, ("#fff" if v >= 60 else "#17202a")
    return "rgb(24,50,82)", "#fff"


grid = "<div></div>" + "".join(f"<div class='ch'>{b}</div>" for b in blocks_wd)
for d in days:
    grid += f"<div class='rh'>{d}</div>"
    for i, v in enumerate(vals[d]):
        if v is None:
            grid += "<div class='cell na'>closed</div>"
            continue
        bg, fg = shade(v)
        lab = f"{v}%" + (f"<span>{sat_blocks[i]}</span>" if d == "Sat" else "")
        grid += f"<div class='cell' style='background:{bg};color:{fg}'>{lab}</div>"
page("fig10-quiet-slots-heatmap", f"""
<h1>When is the chair busy?</h1>
<p class="sub">Share of sellable time booked and completed, average of 8 weeks, both barbers</p>
<div class="hm">{grid}</div>
<div class="leg"><span>Quieter</span><div class="ramp"></div><span>Busier</span></div>
<p class="small">Saturday blocks are 8–11, 11–2 and 2–5. The midweek 12–4 gap repeats every week.</p>
""", """
.hm { display:grid; grid-template-columns:90px repeat(4, 1fr); gap:6px; }
.ch { font-size:21px; font-weight:700; color:var(--muted); text-align:center; padding-bottom:4px; }
.rh { font-size:24px; font-weight:800; display:flex; align-items:center; }
.cell { height:96px; border-radius:6px; display:flex; flex-direction:column; align-items:center; justify-content:center; font-size:28px; font-weight:700; }
.cell span { font-size:16px; font-weight:500; opacity:0.85; }
.cell.na { background:#fff; border:2px dashed var(--line); color:var(--muted); font-size:19px; font-weight:500; }
.leg { display:flex; align-items:center; gap:14px; margin:22px 0 6px; font-size:19px; color:var(--muted); }
.ramp { width:300px; height:18px; border-radius:4px; background:linear-gradient(90deg, rgb(236,241,247), rgb(177,197,220), rgb(91,125,164), rgb(24,50,82)); }
""")

# 11. Return cycle ----------------------------------------------------------
page("fig11-return-cycle", """
<h1>The return cycle</h1>
<p class="sub">Book the next visit while they're happy, then make coming back easy</p>
<svg viewBox="0 0 904 600" width="904" height="600" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
 <defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#56606c"/></marker></defs>
 <g transform="translate(20,40) scale(0.88)">
 <circle cx="300" cy="300" r="200" fill="none" stroke="#c4cad3" stroke-width="4"/>
 <path d="M 300 100 A 200 200 0 0 1 500 300" fill="none" stroke="#56606c" stroke-width="4" marker-end="url(#a)"/>
 <path d="M 500 300 A 200 200 0 0 1 300 500" fill="none" stroke="#56606c" stroke-width="4" marker-end="url(#a)"/>
 <path d="M 300 500 A 200 200 0 0 1 100 300" fill="none" stroke="#56606c" stroke-width="4" marker-end="url(#a)"/>
 <path d="M 100 300 A 200 200 0 0 1 300 100" fill="none" stroke="#56606c" stroke-width="4" marker-end="url(#a)"/>
 <g font-size="22" text-anchor="middle">
  <rect x="190" y="62" width="220" height="74" rx="14" fill="#1f3f63"/><text x="300" y="94" fill="#fff" font-weight="700">The visit</text><text x="300" y="121" fill="#fff" font-size="18">cut, chat, checkout</text>
  <rect x="385" y="262" width="260" height="76" rx="14" fill="#a8322a"/><text x="515" y="294" fill="#fff" font-weight="700">Rebook at the mirror</text><text x="515" y="321" fill="#fff" font-size="18">"Same time in 3 weeks?"</text>
  <rect x="190" y="462" width="220" height="76" rx="14" fill="#e4ecf4" stroke="#1f3f63" stroke-width="2"/><text x="300" y="494" fill="#17202a" font-weight="700">Reminders</text><text x="300" y="521" fill="#17202a" font-size="18">day before + 2 hours</text>
  <rect x="-10" y="262" width="220" height="76" rx="14" fill="#e4ecf4" stroke="#1f3f63" stroke-width="2"/><text x="100" y="294" fill="#17202a" font-weight="700">Shows up</text><text x="100" y="321" fill="#17202a" font-size="18">or reschedules by link</text>
 </g>
 </g>
 <g font-size="21" transform="translate(-30,0)">
  <text x="660" y="150" font-weight="800" fill="#17202a">If they don't rebook</text>
  <rect x="660" y="172" width="250" height="88" rx="12" fill="#f4ede3"/><text x="676" y="207" font-weight="700">"You're due" note</text><text x="676" y="237" font-size="18">at the usual interval</text>
  <text x="785" y="292" text-anchor="middle" font-size="24" fill="#56606c">▼</text>
  <rect x="660" y="308" width="250" height="88" rx="12" fill="#f4ede3"/><text x="676" y="343" font-weight="700">Win-back message</text><text x="676" y="373" font-size="18">past the overdue mark</text>
  <text x="660" y="440" font-size="18" fill="#56606c">Marketing messages go only</text><text x="660" y="464" font-size="18" fill="#56606c">to clients who opted in.</text>
 </g>
</svg>
""")

# 12. Contribution per chair hour (single-series bar chart, sorted, direct labels)
svc = [("Beard trim and line-up", 68.00), ("Standard cut", 60.00), ("Cut and beard", 57.33),
       ("Full service", 50.40), ("Hot towel shave", 49.33), ("Skin fade", 46.67), ("Kids cut", 42.00)]
maxv = 80
bars = ""
for i, (n, v) in enumerate(svc):
    y = 10 + i * 74
    w = v / maxv * 560
    col = "#a8322a" if n == "Skin fade" else "#1f3f63"
    bars += f"""<text x="300" y="{y+36}" text-anchor="end" font-size="23" fill="#17202a"{' font-weight="700"' if n=='Skin fade' else ''}>{n}</text>
<path d="M310 {y+12} h{w-4} a4 4 0 0 1 4 4 v28 a4 4 0 0 1 -4 4 h-{w-4} z" fill="{col}"/>
<text x="{310+w+12}" y="{y+36}" font-size="23" fill="#17202a" font-weight="700">${v:.2f}</text>"""
grid = "".join(f"""<line x1="{310+g/maxv*560}" y1="0" x2="{310+g/maxv*560}" y2="528" stroke="#e3e6ea" stroke-width="1.5"/>
<text x="{310+g/maxv*560}" y="556" text-anchor="middle" font-size="18" fill="#56606c">${g}</text>""" for g in (0, 20, 40, 60))
page("fig12-chair-hour", f"""
<h1>What each service earns per chair hour</h1>
<p class="sub">(Price − direct costs) ÷ booked minutes × 60 · owner's chair, before overhead</p>
<svg viewBox="0 0 904 570" width="904" height="570" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">{grid}{bars}</svg>
<p class="small">The skin fade ($40, 45 minutes) earns less per hour than a $35 standard cut.</p>
""")

# 13. Responsibility chart --------------------------------------------------
resp = [
    ("Shop Google profile, website, shop Instagram", "Dre", "o"),
    ("Replies to reviews of the shop", "Dre", "o"),
    ("Menu and prices for Dre and Tomás", "Dre", "o"),
    ("Keisha's prices, services and policies", "Keisha", "k"),
    ("Client records for Dre and Tomás's clients", "The shop", "s"),
    ("Keisha's client list and booking page", "Keisha", "k"),
    ("Shop-wide promotions", "Dre · Keisha opts in or out in writing", "o"),
    ("Questions about one barber on shop channels", "Sent to that barber's link", "s"),
    ("Saturday walk-in board", "Front desk (named on schedule)", "r"),
    ("Opening, closing, cleaning", "Rota on the wall", "r"),
]
rows = "".join(f"<div class='a'>{a}</div><div class='o {c}'>{b}</div>" for a, b, c in resp)
page("fig13-responsibility-chart", f"""
<h1>Who owns what</h1>
<p class="sub">Cedar Street's responsibility chart, agreed after a bad Saturday</p>
<div class="t">{rows}</div>
<div class="leg"><span class="o o">Owner</span><span class="o k">Chair renter</span><span class="o s">Shop rule</span><span class="o r">Rota</span></div>
""", """
.t { display:grid; grid-template-columns:1fr 360px; border-top:3px solid var(--ink); }
.a { font-size:21px; padding:14px 10px; border-bottom:1.5px solid var(--line); line-height:1.3; }
.t .o { margin:8px 0; }
.o { font-size:20px; font-weight:700; padding:10px 14px; border-radius:8px; display:inline-flex; align-items:center; }
.o.o { background:var(--navy); color:#fff; } .o.k { background:var(--red); color:#fff; }
.o.s { background:var(--sky); color:var(--ink); border:1.5px solid #9fb6cf; } .o.r { background:var(--sand); color:var(--ink); border:1.5px solid #d9c3a5; }
.leg { display:flex; gap:12px; margin-top:20px; }
.leg .o { font-size:18px; }
""")

# 14. Automation ladder -----------------------------------------------------
rungs = [
    ("4", "Automatic", "Runs on its own. Spot-check weekly, review the numbers monthly.", "Reminders that have run cleanly for months"),
    ("3", "Supervised", "Sends on its own; a person reads every message daily for the first weeks.", "A new review request after visits"),
    ("2", "Draft", "AI or the system prepares the message; a person reviews and sends.", "AI replies to Instagram DMs"),
    ("1", "Manual", "You send from a template and learn how clients respond.", "Win-back texts, first month"),
]
rows = "".join(
    f"<div class='rung' style='margin-left:{(4-int(n))*44}px'><div class='n'>{n}</div><div><div class='nm'>{nm}</div><div class='d'>{d}</div><div class='e'>Example: {e}</div></div></div>"
    for n, nm, d, e in rungs)
page("fig14-automation-ladder", f"""
<h1>The automation ladder</h1>
<p class="sub">Climb one rung at a time. Every rung has a pause switch.</p>
{rows}
<div class="pause"><b>Pause switch:</b> everyone on the team knows where it is. Pause first, fix second, explain third.</div>
""", """
.rung { display:grid; grid-template-columns:70px 1fr; gap:18px; align-items:center; border:2px solid var(--line); border-left:10px solid var(--navy);
        border-radius:10px; padding:18px 22px; margin-bottom:14px; background:var(--pale); }
.rung:first-of-type { border-left-color:var(--red); }
.n { font-size:40px; font-weight:800; color:var(--navy); text-align:center; }
.nm { font-size:27px; font-weight:800; }
.d { font-size:21px; line-height:1.35; margin-top:4px; }
.e { font-size:19px; color:var(--muted); margin-top:6px; }
.pause { margin-top:20px; font-size:22px; padding:16px 22px; border:3px solid var(--red); border-radius:10px; }
""")

# 15. 30-day plan -----------------------------------------------------------
wk = [
    ("Before day 1", "Shop brief", ["Write it", "Pass the 10 test questions"]),
    ("Week 1", "Baseline", ["Count sellable minutes", "Tally calls, messages, walk-ins", "Fill in the scorecard", "Pick ONE problem"]),
    ("Week 2", "One change", ["Write the test card", "Decide what counts as success", "Run it all week, no tweaks"]),
    ("Week 3", "Walk the journey", ["Book as a stranger would", "Find the worst friction", "Fix that one thing"]),
    ("Week 4", "Decide", ["Compare like with like", "Count completed visits and costs", "Keep, change or stop"]),
]
cols = "".join(
    f"<div class='w{' pre' if i == 0 else ''}'><div class='when'>{a}</div><div class='what'>{b}</div><ul>{''.join(f'<li>{x}</li>' for x in c)}</ul></div>"
    for i, (a, b, c) in enumerate(wk))
page("fig15-30-day-plan", f"""
<h1>Your first 30 days</h1>
<p class="sub">One baseline, one problem, one change, one honest review</p>
<div class="tl">{cols}</div>
<div class="foot">Every week: 30-minute owner review · same day, same time · scorecard, change, client voice, next week, one note</div>
""", """
.tl { display:grid; grid-template-columns:repeat(5, 1fr); gap:12px; }
.w { border-top:10px solid var(--navy); background:var(--pale); border-radius:8px; padding:16px 14px; }
.w.pre { border-top-color:var(--red); background:var(--sand); }
.when { font-size:18px; text-transform:uppercase; letter-spacing:0.06em; color:var(--muted); font-weight:700; }
.what { font-size:25px; font-weight:800; margin:6px 0 10px; line-height:1.15; }
ul { margin:0; padding-left:20px; font-size:19px; line-height:1.4; }
li { margin-bottom:6px; }
.foot { margin-top:20px; font-size:21px; padding:16px 20px; background:var(--sky); border-radius:8px; }
""")

print("wrote", len(os.listdir(OUT)), "figure pages to", OUT)
