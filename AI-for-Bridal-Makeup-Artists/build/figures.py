#!/usr/bin/env python3
"""Writes one HTML file per figure into build/figures/. render.js turns each into a PNG in images/.
Figures are designed at 1000 CSS px wide and rendered at 1.6x (1600 px), with large type and
high contrast so they read on e-ink and on phones. Every element is labelled in text, so the
diagrams still work in greyscale."""
import os, html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)

CSS = """
@font-face { font-family: "Cormorant"; font-weight: 600; src: url("../fonts/CormorantGaramond-600.woff2") format("woff2"); }
:root { --ink:#2b2230; --soft:#5d5360; --line:#cbbfc2; --rose:#b06f68; --rose-l:#f2dfdb; --gold:#9a7440;
        --gold-l:#f1e6d3; --sage:#5f7a63; --sage-l:#dfe9df; --bg:#fffdfb; --grey:#ece8e6; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: var(--bg); font-family: Inter, "DejaVu Sans", sans-serif; color: var(--ink); }
#fig { width: 1000px; padding: 44px 44px 40px; background: var(--bg); }
h1 { font-family: Cormorant, Georgia, serif; font-weight: 600; font-size: 46px; line-height: 1.1; margin-bottom: 8px; }
.sub { font-size: 23px; color: var(--soft); margin-bottom: 30px; line-height: 1.35; }
.small { font-size: 20px; color: var(--soft); }
"""

def page(name, body, extra_css=""):
    with open(os.path.join(OUT, name + ".html"), "w") as f:
        f.write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}{extra_css}</style></head>"
                f"<body><div id='fig'>{body}</div></body></html>")

def e(s): return html.escape(s)

def mins(t):
    h, m = t.split(":"); return int(h) * 60 + int(m)

# ---------------------------------------------------------------- 0. booking path
stations = [
    ("1", "Studio brief", "Your rates, rules and voice on one page"),
    ("2", "First reply", "Ask only what changes price or timing"),
    ("3", "Quote and deposit", "Check timing first, confirm from records"),
    ("4", "Trial", "Turn decisions into a written brief"),
    ("5", "Timeline", "Work backward from the ready-by time"),
    ("6", "Late changes", "Timing, staffing, cost, approval"),
    ("7", "Closeout", "Money, thanks, review, lessons"),
]
rows = ""
for i, (n, t, d) in enumerate(stations):
    part = "Part I · Build your booking process" if i == 0 else ("Part II · Run the wedding morning" if i == 4 else "")
    if part:
        rows += f"<div class='part'>{e(part)}</div>"
    last = i == len(stations) - 1
    rows += (f"<div class='st'><div class='rail'><div class='dot'>{n}</div>{'' if last else '<div class=bar></div>'}</div>"
             f"<div class='txt'><div class='t'>{e(t)}</div><div class='d'>{e(d)}</div></div></div>")
page("fig-00-booking-path",
     "<h1>The booking path</h1><div class='sub'>One wedding, from the first message to the closeout. Each stop is a chapter.</div>" + rows,
     """.part{font-size:20px;letter-spacing:.08em;text-transform:uppercase;color:var(--rose);font-weight:700;margin:14px 0 10px 4px}
        .st{display:flex;gap:26px;min-height:96px}.rail{display:flex;flex-direction:column;align-items:center;width:64px}
        .dot{width:64px;height:64px;border-radius:50%;background:var(--ink);color:#fff;font-size:30px;font-weight:700;display:flex;align-items:center;justify-content:center}
        .bar{flex:1;width:6px;background:var(--line);margin:4px 0}.txt{padding-top:6px}
        .t{font-size:31px;font-weight:700}.d{font-size:23px;color:var(--soft);margin-top:4px;margin-bottom:18px}""")

# ---------------------------------------------------------------- 1. traffic light
cols = [
    ("GO", "The AI may use", "var(--sage)", "var(--sage-l)",
     ["Your service rates", "Service and setup times", "Travel zones", "Deposit and minimum rules", "The five intake questions", "Your tone of voice"]),
    ("ASK ME", "AI drafts, you decide", "var(--gold)", "var(--gold-l)",
     ["Whether a date is available", "Discounts or price matches", "Second artist or early start", "Anything outside your zones", "Confirming a booking or payment", "Any exception to your terms"]),
    ("STOP", "Never goes in the chat", "var(--rose)", "var(--rose-l)",
     ["Full names", "Phone numbers and emails", "Venue or home addresses", "Photos of clients", "Health or skin details", "Payment details"]),
]
body = "<h1>What goes where</h1><div class='sub'>Split your studio brief into rules, decisions and private details.</div><div class='cols'>"
for tag, title, c, cl, items in cols:
    li = "".join(f"<li>{e(x)}</li>" for x in items)
    body += (f"<div class='col' style='border-color:{c};background:{cl}'><div class='tag' style='background:{c}'>{tag}</div>"
             f"<div class='ct'>{e(title)}</div><ul>{li}</ul></div>")
body += "</div>"
page("fig-01-traffic-light", body,
     """.cols{display:flex;gap:18px}.col{flex:1;border:4px solid;border-radius:18px;padding:20px 18px 14px}
        .tag{color:#fff;font-weight:800;font-size:22px;letter-spacing:.08em;display:inline-block;padding:6px 14px;border-radius:999px}
        .ct{font-size:25px;font-weight:700;margin:14px 0 10px;line-height:1.2}
        ul{list-style:none}li{font-size:21px;line-height:1.3;padding:9px 0;border-top:2px solid rgba(0,0,0,.08)}""")

# ---------------------------------------------------------------- 2. reply paths
page("fig-02-reply-paths", """
<h1>Three ways to answer</h1><div class='sub'>The calendar decides which reply you send. Every path ends in the tracker.</div>
<div class='box start'>New inquiry arrives</div><div class='arrow'>&#8595;</div>
<div class='box q'>Is there a date to check?</div>
<div class='branches'>
  <div class='br'><div class='lab'>No date yet</div><div class='arrow'>&#8595;</div>
    <div class='box out' style='border-color:var(--gold)'><b>Too uncertain to quote</b><span>Share current rates. Ask for the date, venue and headcount.</span></div></div>
  <div class='br'><div class='lab'>Date given</div><div class='arrow'>&#8595;</div>
    <div class='box q2'>Check your calendar</div>
    <div class='two'>
      <div class='br'><div class='lab'>Open</div><div class='arrow'>&#8595;</div>
        <div class='box out' style='border-color:var(--sage)'><b>Date is open</b><span>Say it's open, not held. Ask venue, ready-by, headcount.</span></div></div>
      <div class='br'><div class='lab'>Booked</div><div class='arrow'>&#8595;</div>
        <div class='box out' style='border-color:var(--rose)'><b>Date is booked</b><span>Decline kindly. Refer a colleague if you choose.</span></div></div>
    </div></div>
</div>
<div class='arrow'>&#8595;</div><div class='box end'>Add a tracker row with a status and a next action</div>
""", """.box{border:3px solid var(--ink);border-radius:16px;padding:16px 20px;font-size:25px;font-weight:600;text-align:center;background:#fff}
.start,.end{background:var(--ink);color:#fff}.q,.q2{background:var(--grey)}
.arrow{text-align:center;font-size:34px;line-height:1.1;color:var(--soft)}
.branches{display:flex;gap:22px;align-items:flex-start;margin-top:4px}.br{flex:1;display:flex;flex-direction:column}
.branches>.br:first-child{flex:.8}.two{display:flex;gap:16px}
.lab{text-align:center;font-size:21px;color:var(--soft);font-weight:700;margin-top:8px}
.out{text-align:left;font-weight:400;font-size:21px;line-height:1.3;border-width:4px;min-height:190px}
.out b{display:block;font-size:24px;margin-bottom:6px}.out span{display:block}""")

# ---------------------------------------------------------------- 2b. tracker
trows = [
    ("L-029", "Website", "Sep 12", "Bride + 2", "Awaiting deposit", "Check payment, Thu"),
    ("L-031", "Instagram", "Oct 10", "Bride + 4", "Needs details", "Quote when venue known"),
    ("L-032", "Form", "Jun 6", "Bride + 2", "Declined", "None (date booked)"),
    ("L-033", "Instagram", "Not set", "Unknown", "Needs details", "Follow up in 3 weeks"),
    ("L-034", "Instagram", "Aug 22", "Bride", "New", "Reply re price match, today"),
]
th = "".join(f"<th>{h}</th>" for h in ["Lead", "Source", "Wedding", "Services", "Status", "Next action"])
tb = ""
for r in trows:
    tb += "<tr>" + "".join(f"<td>{'<span class=st>' + e(c) + '</span>' if i == 4 else e(c)}</td>" for i, c in enumerate(r)) + "</tr>"
page("fig-02-tracker", f"<h1>One tracker for every inquiry</h1><div class='sub'>Lead IDs, not names, whenever you work with AI. One status and one dated next action per row.</div><table><tr>{th}</tr>{tb}</table>",
     """table{border-collapse:collapse;width:100%;font-size:20px}th{background:var(--ink);color:#fff;text-align:left;padding:12px 10px;font-size:19px}
        td{padding:14px 10px;border-bottom:2px solid var(--line);vertical-align:top}tr:nth-child(odd) td{background:#f8f3f1}
        .st{display:inline-block;background:var(--rose-l);border:2px solid var(--rose);border-radius:999px;padding:2px 10px;font-weight:700;font-size:18px}""")

# ---------------------------------------------------------------- Gantt helper
def gantt(start, end, lanes, tick=30, width=912, label_w=150, h=74):
    """lanes: list of (lane_label, [(t0, t1, text, kind)]); kind: setup|svc|bride|buffer|free"""
    s0, s1 = mins(start), mins(end)
    span = s1 - s0
    plot = width - label_w
    px = lambda t: label_w + (mins(t) - s0) / span * plot
    out = f"<div class='g' style='width:{width}px'>"
    # ticks
    t = s0 - (s0 % tick) + (tick if s0 % tick else 0)
    out += "<div class='ticks'>"
    while t <= s1:
        x = label_w + (t - s0) / span * plot
        out += f"<div class='tk' style='left:{x}px'><span>{t // 60}:{t % 60:02d}</span></div>"
        t += tick
    out += "</div>"
    for lab, blocks in lanes:
        out += f"<div class='lane' style='height:{h}px'><div class='ll' style='width:{label_w}px'>{e(lab)}</div>"
        for a, b, txt, kind in blocks:
            x0, x1 = px(a), px(b)
            out += f"<div class='blk {kind}' style='left:{x0 + 2}px;width:{x1 - x0 - 4}px'><span>{e(txt)}</span></div>"
        out += "</div>"
    out += "</div>"
    return out

GCSS = """.g{position:relative;margin-top:50px}.ticks{position:absolute;inset:-42px 0 0 0}
.tk{position:absolute;top:0;bottom:0;border-left:2px dashed #ddd2d0}.tk span{position:absolute;top:0;left:-28px;width:56px;text-align:center;font-size:18px;color:var(--soft);font-weight:600}
.lane{position:relative;margin-bottom:16px}.ll{position:absolute;left:0;top:0;bottom:0;display:flex;align-items:center;font-size:21px;font-weight:700;line-height:1.15;padding-right:8px}
.blk{position:absolute;top:0;bottom:0;border-radius:10px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:17px;font-weight:700;line-height:1.1;overflow:hidden;padding:0 3px}
.setup{background:#d9d3d4;color:var(--ink)}.svc{background:var(--rose-l);border:3px solid var(--rose)}
.bride{background:var(--ink);color:#fff}.buffer{background:repeating-linear-gradient(135deg,#f1e6d3 0 10px,#e4d3b6 10px 20px);border:3px solid var(--gold)}
.hair{background:var(--sage-l);border:3px solid var(--sage)}.free{background:#fff;border:3px dashed var(--line);color:var(--soft);font-weight:600}
.legend{display:flex;flex-wrap:wrap;gap:12px 22px;margin-top:22px;font-size:19px;color:var(--soft)}
.legend i{display:inline-block;width:30px;height:20px;border-radius:5px;vertical-align:-4px;margin-right:8px}
.note{margin-top:18px;font-size:21px;line-height:1.35;background:var(--grey);border-radius:12px;padding:14px 18px}"""

def legend(items):
    return "<div class='legend'>" + "".join(f"<span><i class='{k}'></i>{e(t)}</span>" for k, t in items) + "</div>"

# ---------------------------------------------------------------- 3. timing window
blocks = [("7:00", "7:15", "Set", "setup"), ("7:15", "7:55", "Att 1", "svc"), ("7:55", "8:35", "Att 2", "svc"),
          ("8:35", "9:15", "Att 3", "svc"), ("9:15", "9:55", "Att 4", "svc"), ("9:55", "10:55", "Bride", "bride"),
          ("10:55", "11:15", "Buffer", "buffer")]
body = ("<h1>255 minutes of work, 255 minutes of window</h1><div class='sub'>Amara's morning as quoted: room access 7:00, everyone ready by 11:15, one artist.</div>"
        + gantt("7:00", "11:15", [("Makeup", blocks)], tick=30, label_w=110)
        + "<div class='sum'><div><b>15</b> setup</div><div>+</div><div><b>160</b> four attendants</div><div>+</div><div><b>60</b> bride</div><div>+</div><div><b>20</b> buffer</div><div>=</div><div><b>255</b> needed</div></div>"
        + "<div class='note'><b>0 minutes spare.</b> It fits only if the makeup room really opens at 7:00. If access slips to 7:30, the morning is 30 minutes short.</div>")
page("fig-03-timing-window", body, GCSS + """.sum{display:flex;justify-content:space-between;align-items:center;margin-top:22px;font-size:20px;color:var(--soft)}
.sum b{display:block;font-size:32px;color:var(--ink);text-align:center}""")

# ---------------------------------------------------------------- 3b. quote anatomy
qlines = [
    ("A", "Hi Amara, I'd love to help you get ready on October 10."),
    ("B", "Bridal makeup: $220<br>Four bridesmaid services at $95 each: $380<br>Travel: $40"),
    ("C", "Your wedding-day total is $640. The $160 deposit goes toward that total, leaving a $480 balance, due a week before the wedding."),
    ("D", "If you'd like a trial, it's $110 and billed separately."),
    ("E", "I've penciled in a 7:00 a.m. setup and an 11:15 a.m. finish. Could you confirm room access at 7:00?"),
    ("F", "I'll email your confirmation once the agreement is accepted and I've verified the deposit. This quote is valid for 14 days."),
]
notes = [("A", "Date and greeting, with the name added by you"), ("B", "Each service on its own line, with the rate"),
         ("C", "Total, deposit and balance, all checked by hand"), ("D", "Optional extras kept separate"),
         ("E", "Schedule described as proposed, with what to confirm"), ("F", "How the booking is confirmed, and for how long the price stands")]
left = "".join(f"<div class='ql'><span class='k'>{k}</span><div>{t}</div></div>" for k, t in qlines)
right = "".join(f"<div class='nl'><span class='k'>{k}</span><div>{e(t)}</div></div>" for k, t in notes)
page("fig-03-quote-anatomy", f"<h1>What a clear quote contains</h1><div class='sub'>Every figure comes from your rate sheet. Nothing is invented.</div><div class='wrap'><div class='mail'>{left}</div><div class='notes'>{right}</div></div>",
     """.wrap{display:flex;gap:22px}.mail{flex:1.45;background:#fff;border:3px solid var(--line);border-radius:16px;padding:18px 18px 8px;box-shadow:0 6px 0 #efe7e4}
        .ql{display:flex;gap:12px;font-size:22px;line-height:1.35;margin-bottom:14px}.notes{flex:1}
        .nl{display:flex;gap:12px;font-size:21px;line-height:1.3;margin-bottom:22px;font-weight:600}
        .k{flex:none;width:34px;height:34px;border-radius:50%;background:var(--rose);color:#fff;font-weight:800;font-size:19px;display:flex;align-items:center;justify-content:center;margin-top:-2px}""")

# ---------------------------------------------------------------- 3c. status flow
page("fig-03-status-flow", """
<h1>Booked means both checks pass</h1><div class='sub'>"I've paid" is not a check. Open your own records.</div>
<div class='box start'>Client says she has booked</div><div class='arrow'>&#8595;</div>
<div class='checks'><div class='box chk'>Check 1<br><b>Agreement accepted?</b><span>In your contract system</span></div>
<div class='box chk'>Check 2<br><b>Deposit verified?</b><span>Received, not pending, right amount</span></div></div>
<div class='arrow'>&#8595;</div>
<div class='res'>
<div class='box r' style='border-color:var(--gold)'><b>Agreement yes<br>Deposit not yet</b><span class='pill' style='background:var(--gold)'>Awaiting deposit</span></div>
<div class='box r' style='border-color:var(--gold)'><b>Deposit yes<br>Agreement not yet</b><span class='pill' style='background:var(--gold)'>Awaiting agreement</span></div>
<div class='box r' style='border-color:var(--sage);border-width:5px'><b>Both yes</b><span class='pill' style='background:var(--sage)'>Booked</span><span class='sm'>Now send the confirmation and block the calendar</span></div>
</div>""", """.box{border:3px solid var(--ink);border-radius:16px;padding:16px 18px;font-size:23px;text-align:center;background:#fff}
.start{background:var(--ink);color:#fff;font-weight:700}.arrow{text-align:center;font-size:34px;color:var(--soft);line-height:1.15}
.checks{display:flex;gap:20px}.chk{flex:1;background:var(--grey);color:var(--soft);font-size:20px}.chk b{display:block;color:var(--ink);font-size:26px;margin:4px 0}
.chk span{font-size:19px}.res{display:flex;gap:16px}.r{flex:1;border-width:4px;display:flex;flex-direction:column;align-items:center;gap:12px}
.r b{font-size:22px;line-height:1.25}.pill{color:#fff;font-weight:800;border-radius:999px;padding:6px 14px;font-size:20px}.sm{font-size:18px;color:var(--soft);line-height:1.3}""")

# ---------------------------------------------------------------- 4. trial recap
secs = [("What we agreed", "var(--sage)", ["Soft, skin-focused look", "Warm bronze eye, deeper crease", "Half lashes", "Brows brushed up, tails filled", "Rosy blush, light powder"]),
        ("What I'll adjust on the day", "var(--gold)", ["Shorter liner, softened outer corner", "Shimmer in the center of the lid only", "Blush one step deeper for outdoor photos"]),
        ("What I'd like you to confirm", "var(--rose)", ["Lip: Rose Clay or Petal?", "Lashes for any bridesmaids? $15 each, by September 26"])]
b = "<h1>The trial recap</h1><div class='sub'>Three separate sections, so the bride can see what is settled and what is still open.</div>"
for t, c, items in secs:
    b += f"<div class='sec' style='border-left-color:{c}'><div class='st' style='color:{c}'>{e(t)}</div><ul>" + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul></div>"
b += "<div class='foot'>Not in the recap: skin details, allergies and foundation shades. They stay in the client record.</div>"
page("fig-04-trial-recap", b, """.sec{background:#fff;border:2px solid var(--line);border-left:14px solid;border-radius:14px;padding:16px 22px;margin-bottom:16px}
.st{font-size:27px;font-weight:800;margin-bottom:8px}ul{margin-left:26px}li{font-size:22px;line-height:1.45}
.foot{font-size:20px;color:var(--soft);background:var(--grey);border-radius:12px;padding:12px 18px;margin-top:6px}""")

# ---------------------------------------------------------------- 5. solo timeline with hair
mk = [("6:45", "7:00", "Set", "setup"), ("7:00", "7:45", "MOH", "svc"), ("7:45", "8:25", "B2", "svc"), ("8:25", "9:05", "B3", "svc"),
      ("9:05", "9:45", "B4", "svc"), ("9:45", "10:45", "Bride", "bride"), ("10:45", "11:15", "Buffer", "buffer")]
hr = [("6:45", "7:00", "Set", "setup"), ("7:00", "7:40", "B2", "hair"), ("7:45", "8:25", "MOH", "hair"), ("8:25", "9:25", "Bride", "bride"),
      ("9:25", "10:05", "B3", "hair"), ("10:05", "10:45", "B4", "hair"), ("10:45", "11:15", "Veil", "buffer")]
body = ("<h1>Amara's morning, hair and makeup</h1><div class='sub'>Version 3. Room access 6:45, everyone ready by 11:15. Nobody is in two chairs at once.</div>"
        + gantt("6:45", "11:15", [("Makeup (you)", mk), ("Hair (Jess)", hr)], tick=30, label_w=150, h=84)
        + legend([("setup", "Setup"), ("svc", "Makeup"), ("hair", "Hair"), ("bride", "Bride"), ("buffer", "Buffer / finishing")])
        + "<div class='note'>MOH = maid of honor (45 minutes with lashes). B2 to B4 = bridesmaids. The bride has hair first, then a 20-minute break, so her makeup is the freshest thing in the photos.</div>")
page("fig-05-solo-timeline", body, GCSS)

# ---------------------------------------------------------------- 5b. two-artist
a = [("8:00", "8:15", "Set", "setup"), ("8:15", "8:55", "MOB", "svc"), ("8:55", "9:35", "BM1", "svc"), ("9:35", "10:15", "BM2", "svc"),
     ("10:15", "11:15", "Bride", "bride"), ("11:15", "12:00", "Buffer 45", "buffer")]
bb = [("8:00", "8:30", "Arrives 8:30", "free"), ("8:30", "8:45", "Set", "setup"), ("8:45", "9:25", "BM3", "svc"), ("9:25", "10:05", "BM4", "svc"), ("10:05", "10:45", "BM5", "svc"),
      ("10:45", "11:25", "MOG", "svc"), ("11:25", "12:00", "Buffer 35", "buffer")]
body = ("<h1>A two-artist morning</h1><div class='sub'>Lead L-044: eight services, room access 8:00, ready by 12:00. Each artist works backward from the deadline on their own.</div>"
        + gantt("8:00", "12:00", [("You (lead)", a), ("Associate", bb)], tick=30, label_w=150, h=84)
        + legend([("setup", "Setup"), ("svc", "Attendant or family"), ("bride", "Bride"), ("buffer", "Buffer"), ("free", "Not yet on site")])
        + "<div class='note'>Your latest arrival: 12:00 minus 30, 180 and 15 = 8:15. The associate's: 12:00 minus 30, 160 and 15 = 8:35, so she can come at 8:30.</div>")
page("fig-05-two-artist", body, GCSS)

# ---------------------------------------------------------------- 6. change impact
scen = [("Version 3, as booked", 260, 270), ("A: add mother of the bride", 310, 270), ("B: ready by 10:45", 260, 240), ("A and B together", 310, 240)]
mx = 330
rows = ""
for name, need, have in scen:
    diff = have - need
    tag = f"{diff} min spare" if diff >= 0 else f"{-diff} min short"
    col = "var(--sage)" if diff >= 0 else "var(--rose)"
    rows += (f"<div class='sc'><div class='nm'>{e(name)}<span style='color:{col}'>{tag}</span></div>"
             f"<div class='bars'><div class='b need' style='width:{need / mx * 100}%'><span>Needed {need}</span></div>"
             f"<div class='b have' style='width:{have / mx * 100}%'><span>Available {have}</span></div></div></div>")
page("fig-06-change-impact", "<h1>What the two changes do</h1><div class='sub'>Minutes needed (setup, services and buffer) against minutes available from 6:45 access, for one artist.</div>" + rows
     + "<div class='note'>Six services raise the buffer from 20 to 30 minutes, so adding one person costs 50 minutes, not 40. The fix for A and B together: a second artist.</div>",
     GCSS + """.sc{margin-bottom:24px}.nm{font-size:25px;font-weight:700;display:flex;justify-content:space-between;margin-bottom:8px}
.nm span{font-weight:800}.b{height:40px;border-radius:8px;margin-bottom:6px;display:flex;align-items:center;padding-left:12px;font-size:19px;font-weight:700}
.need{background:var(--ink);color:#fff}.have{background:#fff;border:3px solid var(--ink)}""")

# ---------------------------------------------------------------- 6b. revised timeline v4
you = [("6:45", "7:00", "Set", "setup"), ("7:00", "7:45", "MOH", "svc"), ("7:45", "8:25", "B2", "svc"), ("8:25", "9:15", "Bride in hair", "free"),
       ("9:15", "10:15", "Bride", "bride"), ("10:15", "10:45", "Buffer", "buffer")]
nad = [("6:45", "8:00", "Arrives 8:00", "free"), ("8:00", "8:15", "Set", "setup"), ("8:15", "8:55", "B3", "svc"), ("8:55", "9:35", "B4", "svc"),
       ("9:35", "10:15", "MOB", "svc"), ("10:15", "10:45", "Buffer", "buffer")]
body = ("<h1>Version 4: two artists, ready by 10:45</h1><div class='sub'>Updated October 2, after Amara approved the change in writing.</div>"
        + gantt("6:45", "10:45", [("You (lead)", you), ("Nadia", nad)], tick=30, label_w=150, h=84)
        + legend([("setup", "Setup"), ("svc", "Attendant or family"), ("bride", "Bride"), ("buffer", "Buffer"), ("free", "Not in your chair")])
        + "<div class='note'>Added: makeup for the mother of the bride (MOB), $95, and Nadia's travel, $40. New total $790, balance $630.</div>")
page("fig-06-revised-timeline", body, GCSS)

# ---------------------------------------------------------------- 7. scorecard
data = [("January", 18, 6, 12, 0, "33%"), ("February", 20, 6, 13, 1, "30%"), ("March", 22, 5, 10, 7, "23% so far"), ("April", 15, 2, 3, 10, "not ready")]
mxq = 22
rows = ""
for m, sent, bk, cl, op, rate in data:
    w = lambda n: n / mxq * 100
    rows += (f"<div class='mr'><div class='mn'>{m}<span>{sent} quotes</span></div><div class='stack'>"
             f"<div class='s bk' style='width:{w(bk)}%'>{bk}</div><div class='s cl' style='width:{w(cl)}%'>{cl}</div>"
             + (f"<div class='s op' style='width:{w(op)}%'>{op}</div>" if op else "") +
             f"</div><div class='rt'>{rate}</div></div>")
page("fig-07-scorecard", "<h1>Quotes, grouped by the month they were sent</h1><div class='sub'>Booked, closed without booking, and still open. Rate = booked ÷ quotes sent.</div>" + rows
     + "<div class='legend'><span><i class='bk2'></i>Booked</span><span><i class='cl2'></i>Closed, no booking</span><span><i class='op2'></i>Still open</span></div>"
     + "<div class='note'>March and April still have open leads, so their rates may still rise. Compare months only once they've had similar time to respond.</div>",
     GCSS + """.mr{display:flex;align-items:center;gap:16px;margin-bottom:20px}.mn{width:150px;font-size:24px;font-weight:700;line-height:1.1}
.mn span{display:block;font-size:18px;color:var(--soft);font-weight:500}.stack{flex:1;display:flex;height:56px}
.s{display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:800;border-right:3px solid #fff}
.bk{background:var(--ink);color:#fff;border-radius:8px 0 0 8px}.cl{background:#d9d3d4}.op{background:repeating-linear-gradient(135deg,#fff 0 9px,#e9dfdd 9px 18px);border:3px solid var(--rose)}
.rt{width:140px;font-size:22px;font-weight:800;text-align:right}
.bk2{background:var(--ink)}.cl2{background:#d9d3d4}.op2{background:#fff;border:3px solid var(--rose)}""")

print("figures written:", len([f for f in os.listdir(OUT) if f.endswith('.html')]))
