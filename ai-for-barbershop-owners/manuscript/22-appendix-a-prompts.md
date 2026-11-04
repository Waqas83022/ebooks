# Appendix A: The prompt library {.unnumbered}

Here are 100 prompts, grouped by job, ready to copy and adapt. Most are short versions of prompts explained in the chapters; others cover jobs the chapters only mention.

Two habits make every one of them work better.

First, start each chat with your shop brief (Chapter 3) and this line:

::: prompt
Use only the facts in this brief. Where you need a fact that isn't in it, write [CHECK] instead of guessing. Never invent prices, times, availability, offers, reviews or client details.
:::

Second, never paste client names, phone numbers, photos, health details or payment information. Use placeholders such as [first name], [time], [barber] and [booking link], and fill them in inside your booking system.

Words in [square brackets] are for you to fill in or for the AI to leave as placeholders.

## Setting up

**1. Draft the shop brief from a voice note**

::: prompt
Turn my rambling description below into a one-page shop brief with these headings: Basics, Hours, Barbers, Menu (price and booked minutes per service), Booking rules, Payments, How we talk, Never promise, Always hand to the owner. Short lines. Write [MISSING] for any fact I haven't given. Finish with the five most important questions I haven't answered. [paste description]
:::

**2. Find gaps in an existing brief**

::: prompt
Read my shop brief and list every question a client commonly asks a barbershop that this brief can't answer. Group them by topic. Don't answer them; I'll fill them in.
:::

**3. Describe my writing voice**

::: prompt
Here are six messages I've sent to clients, names removed. Describe my style in five bullet points (sentence length, punctuation, greetings, common words, things I never do). Then write a 30-word reminder in that style. [paste messages]
:::

**4. Write the ten test questions**

::: prompt
Write ten test questions a client might ask my barbershop, to check that an AI assistant answers correctly from my brief. Include three about prices, three about rules, two about closed days, and two trick questions where the right answer is "I'm not sure" or "we don't offer that".
:::

**5. Grade the answers**

::: prompt
Here are the ten test questions and the answers an assistant gave. Compare each answer with my shop brief. Mark each Correct, Wrong or Invented, and explain any problem in one line. [paste questions and answers]
:::

**6. Write a renter's own brief**

::: prompt
I rent a chair in a barbershop. Turn my notes into a one-page brief for my own business: my services, prices, booked minutes, booking link, deposit and cancellation rules, hours, how I talk to clients, and what I never promise. Mark [MISSING] gaps. [paste notes]
:::

**7. Shop AI policy**

::: prompt
Write a five-line AI policy for staff at my barbershop. Cover: AI drafts and a person approves; no client personal data in AI chats; facts come only from the shop brief; templates need owner approval; chair renters decide what is said about their business. Plain language, fits on an index card.
:::

**8. Update everything after a change**

::: prompt
I've changed this in my shop brief: [describe change]. List every place a barbershop usually shows this information (booking page, Google profile, website, saved replies, signs, reminders) so I can update them all today.
:::

## Numbers and planning

**9. Baseline from an appointment export**

::: prompt
Here's two weeks of appointments, names removed. Columns: [list]. Sellable time per barber is [minutes] per week. Calculate each barber's utilization from completed minutes, the no-show rate, and the checkout rebooking rate, with the counts behind each. Tell me the biggest single problem in two sentences. Show your arithmetic. [paste]
:::

**10. Sellable minutes**

::: prompt
Calculate sellable minutes per week for each barber. Hours in the shop: [per barber, per day]. Subtract lunch of [ ] minutes per day and [ ] minutes per day for cleaning and admin. Show it per day and per week.
:::

**11. Quiet-hours heatmap**

::: prompt
From 8 weeks of appointment data (names removed), make a table for each barber of weekdays by 2-hour blocks, showing the average share of sellable time that was booked and completed. List the three emptiest blocks for each barber with average empty hours per week. [paste]
:::

**12. Return intervals by service**

::: prompt
From this year of appointments (client IDs, no names), calculate the median days between visits for each service among clients with at least 3 visits. Suggest an "overdue" threshold for each service. Show the counts. [paste]
:::

**13. First-visit return rate**

::: prompt
From this data (client IDs, no names), find all first visits between [date] and [date], then count how many of those clients completed another visit within [ ] weeks. Give the rate with counts, by barber and by first service booked. [paste]
:::

**14. Weekly scorecard summary**

::: prompt
Here's this week's scorecard and the last four weeks. In two short paragraphs, tell me what changed, what stayed flat, and one question I should be asking. Don't recommend more than one action. [paste]
:::

**15. Pick this month's problem**

::: prompt
Here are my baseline numbers. For each possible problem (missed calls, quiet slots, no-shows, rebooking, first-visit returns, local visibility), estimate how many bookings it costs per week, how cheap it is to fix, and how close it is to the chair. Then recommend one problem to work on this month, with your reasoning. [paste]
:::

**16. Compare like with like**

::: prompt
I changed [what] on [date]. Here are completed services for the four weeks before and the four weeks after, by weekday and time block. Compare only matching weekdays and windows. Tell me whether the change looks like it helped, and what else could explain the difference (season, holidays, staffing). [paste]
:::

**17. Count sources of new clients**

::: prompt
Here are the answers to "How did you find us?" for new clients over the last 3 months, with completed yes/no. Group them into Google, Instagram, friend or referral, partner, walked past, ad, other, unknown. Give booked and completed counts for each. [paste]
:::

**18. Explain a number simply**

::: prompt
Explain in plain words, as if to a barber with no business training, what [metric] means, how to calculate it, and one mistake people make when measuring it.
:::

## Google and local search

**19. One-line positioning from reviews**

::: prompt
Here are 20 recent reviews (names removed) and my menu. What three things are we best known for, based only on what clients say? Quote supporting phrases. Then write three one-sentence descriptions of the shop under 25 words, plain language. [paste]
:::

**20. Google Business Profile description**

::: prompt
Write a Google Business Profile description, maximum 700 characters, using only my brief: what we're known for, main services, area or landmark, parking, how to book. No keyword stuffing, no claims we can't prove, no prices.
:::

**21. Services list for Google**

::: prompt
Turn my menu into a Google Business Profile services list: service name, price, and a one-sentence plain description of each, under 120 characters. Don't add services that aren't on my menu.
:::

**22. Listing consistency check**

::: prompt
Here are my shop details from [list sites]. Compare each line by line with my shop brief and make a table showing every difference: name, address, phone, hours for each day, booking link, services and prices. [paste]
:::

**23. Holiday hours update**

::: prompt
Write a Google Business Profile update and an Instagram post announcing our hours for [holiday period]: [list dates and hours]. Include the booking link. Under 50 words each.
:::

**24. Weekly Google update**

::: prompt
Write a Google Business Profile update for this week. Topic: [openings this week / new barber / real cut / seasonal]. Under 60 words, includes the booking link, no hashtags, no emojis.
:::

**25. First-visit web page brief**

::: prompt
Write a brief for a one-page website for first-time clients on their phones: headline, subheading, section order, copy for each section under 80 words, the photos I need, and where the booking button goes. Use only my brief. Mark [MISSING] gaps.
:::

**26. "What to expect on your first visit"**

::: prompt
Write a short "First time here?" section for my website and booking page: how to book, where to park and enter, what happens when you arrive, how long the service takes, how to pay, and our late policy. Under 120 words, friendly.
:::

**27. Photo list for the profile**

::: prompt
List the 20 photos my barbershop's Google profile should have, described specifically (angle, subject, lighting), covering real cuts, interior, exterior and entrance, parking, and the team. Note which need client permission.
:::

**28. Local partner list**

::: prompt
I run a barbershop at [area description]. List 15 kinds of nearby businesses whose customers might need a barber, with one line on why each fits and one idea for a simple, fair swap with them.
:::

## Social content

**29. Shot list**

::: prompt
Make a photo and video shot list for my barbershop: three specific shots for each of [services], plus five video ideas under 20 seconds with no talking to camera. One line per item.
:::

**30. Weekly caption batch**

::: prompt
Write Instagram captions for these four photos using my brief and notes. First line describes the cut plainly. Mention the barber and the shop. Include the price from the menu and end with [booking link]. Under 50 words, at most one emoji, no hashtags in the caption. Then suggest 8 hashtags for the first comment: 4 local using only [neighborhood] and [city], 4 about the service. [notes]
:::

**31. Barber introduction**

::: prompt
Write an Instagram post introducing [barber] at my shop: how long they've cut, what they love cutting, the days they work, one human detail from my notes, and how to book them. Under 70 words. [notes]
:::

**32. Client question post**

::: prompt
Write an Instagram post answering this question clients ask us: "[question]". Plain, accurate, under 80 words, ending with how to book. Don't give medical advice.
:::

**33. Before-and-after caption**

::: prompt
Write a caption for a before-and-after photo of [service]. Describe what we changed in plain terms, without making fun of the "before". Name the barber, the price, and [booking link]. Under 45 words.
:::

**34. Reel script**

::: prompt
Write a 15-second vertical video script for [service]. No talking to camera. Give four shots with timings, on-screen text for each (max 6 words), and a 30-word caption with the price and [booking link].
:::

**35. Talking-head tip**

::: prompt
Write a 30-second script for [barber] to say to camera answering "[question]". Conversational, no jargon, ends with one line about booking. Under 80 words when spoken.
:::

**36. Four-week calendar**

::: prompt
Build a four-week content calendar: three Instagram posts a week plus a Google update every Friday. Formats: real cut, barber intro, client question, availability post, shop moment, seasonal. Local dates: [list]. Table with day, format, barber, idea, and the photo I need.
:::

**37. Seasonal ideas**

::: prompt
List ten post ideas for my barbershop for [season or month], tied to real events that happen every year (school, holidays, sports seasons, weddings, graduations). For each, one line and the service it promotes.
:::

**38. New barber launch posts**

::: prompt
Write three posts announcing a new barber, [name], starting [date]: an announcement a week before, a first-week post with a real cut, and an introduction after two weeks. Keep the facts consistent across all three: [facts].
:::

**39. Shop move or change announcement**

::: prompt
We're changing [what] on [date]. Write a short Instagram post, a Google update, a text for opted-in clients with [opt-out wording], and a door sign. Every version must give the same date and details: [facts].
:::

**40. Caption rewrite**

::: prompt
Rewrite this caption so it sounds like a barber talking to a regular, not an advert. Keep all the facts. Cut it by a third. Remove any word like "elevate", "experience" or "premier". [paste caption]
:::

**41. Repurpose one cut five ways**

::: prompt
From this one note about a cut, write: an Instagram caption, a Google update, a 15-second reel script, a story text overlay, and a short line for the shop's window board. [note]
:::

**42. Monthly content review**

::: prompt
Here are last month's posts with views, likes, link clicks, and new clients who said they found us through each post. Which formats brought clients, not just likes? Recommend one change for next month. [paste]
:::

## Reviews, referrals and partners

**43. Review request message**

::: prompt
Write a short thank-you text sent two hours after a completed visit, asking for an honest Google review with [review link]. Under 35 words. Must not offer anything in return or suggest what rating to give.
:::

**44. Review request card**

::: prompt
Write the text for a small counter card with a QR code asking clients for an honest review. Under 25 words. No incentives, no "5 stars" language.
:::

**45. Reply to a positive review**

::: prompt
Draft a reply to this review: under 40 words, mention one specific thing they said, thank the barber they named by first name, no more than one exclamation mark, no client details beyond the review. "[review]"
:::

**46. Batch replies**

::: prompt
Write a reply to each of these positive reviews, each under 35 words, each with a different opening line, each mentioning something specific from that review. [paste reviews]
:::

**47. Reply to a negative review**

::: prompt
Draft a calm reply under 80 words to this negative review. Take responsibility for what we got wrong, explain our policy plainly where there was a misunderstanding, say what we've changed, invite them to contact [owner] at [phone]. No arguing, no private details, no offer of anything free in public. Review: "[ ]". What happened: [ ].
:::

**48. Reply to a suspected fake review**

::: prompt
Draft a short, neutral reply to a review we believe isn't from a real client. Say we can't find a matching visit and invite them to call [phone]. No accusations, no threats, under 40 words.
:::

**49. Monthly feedback themes**

::: prompt
Here are last month's reviews and complaints, names removed. Group them into themes with counts and two short quotes each. Separate the haircut itself from booking, waiting, price and communication. Suggest one change to test for each theme. [paste]
:::

**50. Complaint handoff procedure**

::: prompt
Turn these notes into a six-step complaint procedure for my barbershop staff: what to say in the moment, what to record and where, who gets told and when, how fast the owner responds, the standard fixes, and the monthly review. [notes]
:::

**51. Referral program wording**

::: prompt
Write a referral counter card (under 40 words) and an opted-in client text (under 35 words, with [opt-out wording]) for this offer: [new client reward], [referrer reward after the friend completes a visit], how it's recorded, 90-day expiry, monthly cap of [ ]. Plain and friendly.
:::

**52. Referral program check**

::: prompt
Check this referral offer: first visit price [ ], direct cost per visit [ ], new client discount [ ], referrer reward [ ]. Calculate the contribution from the first visit and the total discount cost per completed new client. List two risks.
:::

**53. Partnership pitch**

::: prompt
Draft a short message to [business] near my shop proposing a one-month trial swap: [what each side does]. Each side gets a tracked link or code: [ ]. At the end we compare results. Under 90 words, friendly, no pressure. Signed [name], [shop].
:::

**54. Partner one-pager**

::: prompt
Write a one-page sheet for a partner business's front desk: who we are in one line, what we're good at, address and parking, prices for our three most popular services, and our booking link with their code. Under 120 words.
:::

## Paid ads

**55. Ad test card**

::: prompt
Help me fill in an ad test card: one service [ ], one audience [ ], one booking page [ ], two versions differing only in [ ], spend cap [ ], end date [ ], primary measure (completed first visits), decision rule, review date. Point out anything I've left vague.
:::

**56. What can I pay for a new client?**

::: prompt
Price [ ], direct costs [ ], commission [ ]%. About [ ]% of first-time clients become regulars who return [ ] more times a year. Calculate the contribution from a first visit for the shop, the average contribution per new client over a year, and a cautious maximum acquisition cost. Show the arithmetic.
:::

**57. Two ad versions**

::: prompt
Write two Facebook and Instagram ads for [service, barber, price]. Goal: book [days/times]. Same photo and link; they differ only in the first line (A leads with the cut, B with availability). Primary text under 40 words, headline under 8 words. No "best in town", no fake urgency.
:::

**58. Ad results review**

::: prompt
Ad test results: spend [ ], clicks [ ], attributed bookings [ ], completed first visits [ ] (A: [ ], B: [ ]), no-shows [ ]. Service price [ ], commission [ ]%, direct costs [ ]. My decision rule: [ ]. Calculate cost per completed first visit and first-visit contribution, say whether A versus B is meaningful at these numbers, apply my rule, and suggest one change. Show the arithmetic.
:::

**59. Diagnose a failed ad**

::: prompt
My ad got [clicks] clicks, [bookings] bookings and [completed] completed visits on [spend]. Walk through where the leak most likely is (ad, audience, booking page, reminders, the visit itself), and suggest the one cheapest thing to check first.
:::

**60. Marketplace fee check**

::: prompt
A booking marketplace charges [fee or %] for each new client it sends. With my price [ ], direct costs [ ] and commission [ ], what does each new client cost me and what does the shop keep on the first visit? How many return visits does it take to cover the fee?
:::

## Calls, messages and the front desk

**61. Missed-call text-back**

::: prompt
Write a missed-call auto-text for my barbershop: who we are, that we're probably mid-cut, the booking link, and that they can reply with questions. Under 40 words. No promotions.
:::

**62. Voicemail greeting**

::: prompt
Write a voicemail greeting under 50 words: shop name, we're probably cutting, the fastest way to book is the link we'll text you, our hours, leave a message if you have a question. Natural, not corporate.
:::

**63. Top ten saved replies**

::: prompt
Write saved replies for these 10 questions, under 40 words each, from my brief. Each ends with [booking link], or a renter's own link for questions about that barber. Never name a specific available time. Write [CHECK] where the brief has no answer. [questions]
:::

**64. After-hours auto-reply**

::: prompt
Write an after-hours auto-reply for Instagram and text: we're closed, our hours, book any time at [link], we'll answer questions from [opening time]. Under 35 words.
:::

**65. Offering a held slot**

::: prompt
Write a short message offering a specific open slot ([barber], [time], [service]) and saying we'll hold it for 15 minutes. Under 30 words. Then write the follow-up if they don't reply in time.
:::

**66. Barber is full**

::: prompt
Write a reply for when a client asks for [barber], who is fully booked. Offer the waitlist and, as an alternative, [other employee barber] by name with their next opening [ ]. Under 40 words.
:::

**67. Fully booked walk-in**

::: prompt
Write what front-desk staff should say to a walk-in when we're fully booked for the next two hours, and the text for a small card with a QR code to book. Honest, friendly, and steer them toward [quiet days].
:::

**68. Running late, client side**

::: prompt
Write a reply to a client who texts that they're running [ ] minutes late. Our grace period is 10 minutes. Offer a shorter service in the time left or the next opening. Under 35 words, friendly.
:::

**69. Front-desk script sheet**

::: prompt
Using my brief, write a one-page front-desk script sheet with short replies for: missed-call text, "anything today?", fully booked walk-in, barber is full, client running late, reschedule request. Under 40 words each.
:::

**70. AI receptionist test calls**

::: prompt
Write 20 test calls to check an AI phone receptionist for my barbershop. Include ordinary bookings, price questions, closed days, a service we don't offer, an angry client, a parent booking for a child, a request for a barber who left, and a question about a scalp condition. For each, write what a correct response looks like.
:::

## Quiet slots, reminders and rebooking

**71. Who's free when we're quiet**

::: prompt
My quiet window is [days, times]. My area is [description]. List the kinds of people likely to be free then and one message idea for each. Leave out groups who can't come then (for example kids during school hours).
:::

**72. Three quiet-slot messages**

::: prompt
Draft three messages: a text to an opted-in overdue regular, a reply to someone on the waitlist for [day], and a public availability post. Facts: [service, price, minutes, window, barber]. Placeholders [first name], [barber], [verified slot], [booking link], [opt-out wording if required]. Under 45 words each. No invented offers or deadlines.
:::

**73. Update a filling availability post**

::: prompt
Rewrite this availability post to show that [slots] are now taken and [slots] are still open. Keep it short and accurate. [paste post]
:::

**74. Quiet-week review**

::: prompt
Here are the results for [number] target openings: booked, completed, cancelled, no-show and source for each. Calculate fill rates with counts, revenue and contribution at [price] and [costs], and compare with the average for the same window over the previous four weeks. [paste]
:::

**75. Day-before and same-day reminders**

::: prompt
Rewrite my reminders: one the day before, one 2 hours before. Use [first name], [day], [time], [barber], [service], [reschedule link]. Include our cancellation and late policy in one friendly line: [policy]. Under 40 words each.
:::

**76. No-show recovery**

::: prompt
Write a friendly same-day message to a client who missed their appointment: no guilt, easy rebooking with [booking link]. Under 30 words.
:::

**77. Deposit policy wording**

::: prompt
Explain this deposit and no-show policy for my booking page (under 70 words) and in two sentences for reminders: [policy]. Say why without guilt-tripping.
:::

**78. Rebooking line for the mirror**

::: prompt
Give me five ways a barber could offer to book the next visit at the end of a cut, each under 20 words, natural and low-pressure. Include the interval for [service].
:::

**79. "When you're due" reminder**

::: prompt
Write a reminder sent when an opted-in client reaches their usual return interval for [service]. Under 30 words, from [barber], with [booking link] and [opt-out wording].
:::

**80. Win-back text**

::: prompt
Write three versions of a win-back text for regulars who've gone longer than usual and opted in to marketing. Under 35 words, warm, from [barber], with [booking link] and [opt-out wording]. No discount, no guilt, no fake urgency.
:::

**81. Win-back results with a holdout group**

::: prompt
I messaged [ ] lapsed regulars and held back [ ] at random. Within 30 days, [ ] messaged and [ ] held-back clients completed a visit. Calculate both return rates, the difference, and what it suggests the message actually did. Explain the uncertainty with numbers this small.
:::

**82. Marketing consent wording**

::: prompt
Write a short, clear opt-in line for my booking form and a paper sign-up sheet that asks clients if they'd like texts about openings and offers, says how to opt out (reply STOP), and is separate from appointment reminders. Under 30 words. Flag that I should check it against the rules where I operate.
:::

## Pricing and offers

**83. Contribution per chair hour**

::: prompt
For each service on my menu, calculate contribution per chair hour = (price − direct costs) ÷ booked minutes × 60. Sort highest to lowest. Repeat assuming [ ]% commission. Show the arithmetic for two rows. [menu with prices, minutes, costs]
:::

**84. Price rise break-even**

::: prompt
I want to raise [service] from [old price] to [new price]. Direct costs are [ ]. How many of these services can I lose and still earn the same total contribution? Show the formula and the arithmetic.
:::

**85. Price change announcement**

::: prompt
Write a price change announcement: [service] goes from [ ] to [ ] on [date]; everything else stays the same. A counter sign under 30 words, a post under 50 words, and a text under 30 words with [opt-out wording]. Confident, not apologetic.
:::

**86. Bundle check**

::: prompt
Compare selling [service A] and [service B] separately with selling them as a bundle at [price]. Prices, minutes and direct costs: [ ]. Calculate contribution and contribution per chair hour for each option, and tell me what share of bundle clients would need to be "extra" for the bundle to pay off.
:::

**87. Offer break-even**

::: prompt
Check whether this offer can pay for itself. Price [ ], direct costs [ ], offer [ ], usual visits in this window [ ], open slots [ ]. Calculate contribution per visit before and after, visits needed to break even, and whether the open slots can hold them. List two risks. Show the arithmetic.
:::

**88. Membership design check**

::: prompt
I'm considering a membership: [price] per month for [what's included]. Normal price of those services [ ], direct costs [ ]. If [ ] members join, how many chair hours per month will they use, what's the contribution per visit, and what questions should I answer about unused visits, cancellations and peak times before launching?
:::

**89. Product shelf cards**

::: prompt
Write a shelf card for each product: name, what it does in one plain sentence, which hair it suits, how to use it in one sentence, and price. Under 35 words each. No claims I can't back up. [products and notes]
:::

## Team and training

**90. Responsibility chart**

::: prompt
Turn our meeting notes into a one-page responsibility chart with one owner per row. Then list important areas my notes don't cover, and flag anything that sounds like the shop controlling a chair renter's prices, hours or clients. [notes]
:::

**91. Walk-in board rules and sign**

::: prompt
Write rules for our walk-in board (first come first served, "next available" option, booked clients first, walk-in cutoff time [ ], honest wait estimates) and a door sign under 60 words.
:::

**92. Running-late text, shop side**

::: prompt
Write a text to send a client when their barber is running [ ] minutes behind: an honest new estimate and a choice of a later time or [other barber] at the original time. Under 40 words.
:::

**93. Closing checklist**

::: prompt
Write a closing checklist for a [ ]-chair barbershop, grouped by station, shared areas, front desk and back room. Under 25 items, each starting with a verb and specific. Add a sign-off line with a space to note restocking needs.
:::

**94. Role description and job ad**

::: prompt
Write a role description, a job ad under 120 words, and six interview questions (including two scenarios) for this role at my barbershop: [hours, tasks, pay]. Keep the ad free of language that could discourage applicants based on protected characteristics.
:::

**95. Trial cut scoring sheet**

::: prompt
Create a scoring sheet for a barber's trial cut at my shop. Cover consultation, sanitation, technique for [service], finishing, timing against our booked minutes, and how they talk to the client. Score each 1 to 4 with a one-line description of what each score looks like.
:::

**96. Role-play training**

::: prompt
Using the shop brief, play a client in each situation one at a time: [list situations]. Stay in character and be realistic. After each, step out and give the trainee three points of feedback based only on the brief.
:::

## Back office

**97. Reorder points**

::: prompt
For each supply, calculate a reorder point = weekly use × delivery time in weeks + one week of safety stock, and suggest an order quantity of about four weeks' use. Flag items with delivery over two weeks. [list with weekly use and delivery time]
:::

**98. Weekly close**

::: prompt
Two exports for [dates], names and card details removed: completed services (date, time, barber, service, price, discount, status) and payments (date, time, amount, tip, method, refund). Give total completed service value after discounts, total payments excluding tips, the difference, unmatched services and payments, and every refund, void and discount. Show your working; don't guess matches. [paste]
:::

**99. Commission statement template**

::: prompt
Create a weekly commission statement template for a barber: services completed (count and value from the booking system), commission rate, commission due, adjustments with reasons, and a line for both signatures. Then fill it in with this week's numbers: [ ].
:::

**100. Automation test plan**

::: prompt
I want to set up this automation: [describe]. Write a one-page test plan: what it does, trigger, who it messages, who it must never message, the message template, three test cases before going live, what to check in the first 20 sends, how to pause it, owner, review date. Point out anything that could go wrong.
:::
