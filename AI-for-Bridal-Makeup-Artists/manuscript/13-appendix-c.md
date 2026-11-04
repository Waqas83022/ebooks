# Appendix C: Troubleshooting {#appendix-c}

Sooner or later an AI draft will go wrong in a way that matters. Most of the problems fall into a handful of patterns, and each has a quick fix for the draft in front of you and a longer-term fix for your brief or your prompts. This appendix covers the three you'll meet most often, then a few smaller ones.

## When an AI draft invents a price

**What it looks like.** A quote or reply contains a figure you didn't give it. Bridal at $180. A "travel fee of $1 per mile." A "10% discount for parties of six or more." Sometimes it's subtle: your attendant rate is $95, but the draft says "from $95," which suggests some services cost more.

**Why it happens.** The tool fills gaps with whatever is most likely. If your brief doesn't cover a situation, or the conversation has gone on long enough that the brief has drifted out of its attention, it reaches for typical industry prices.

**Fix the draft.** Don't edit the number and send. Check every other number too, because a draft with one invented figure may have more. Then regenerate it with a tighter instruction: "Use only these figures: [list]. If any figure you need isn't here, leave a bracket."

**Fix it for next time.**

- Make sure every service you sell is in your brief with a price. If you sometimes do something that isn't listed (a tattoo cover, a male groom's grooming), add it or add "Not offered."
- Add this line to your brief if it isn't there: "Never invent, estimate or round a price. Use only the rates above."
- Start a fresh conversation for each quote. Long conversations are where most invented figures come from.
- Calculate the total yourself before you prompt, and give it the total. Then any difference jumps out at you.

## When an AI draft confirms a date too early

**What it looks like.** "You're all booked!" "I've reserved October 10 for you." "Your date is secured." "Consider it done!" Any wording that tells the client the date is hers before you've checked the agreement and the payment yourself.

**Why it happens.** The tool is trained to be helpful and positive. When a client says "I've paid," the most helpful-sounding reply is a confirmation. It has no way of checking your payment system, so it takes the client's word.

**Fix the draft.** Replace any confirmation wording with the holding reply:

> Thank you! I'll check the agreement and payment on my side and send your confirmation as soon as both are through.

If the message has already gone out, act quickly. Check your records. If both are in, there's no harm done. If not, send a short, friendly correction: "Just to clarify my last message, I haven't yet received the [deposit / signed agreement]. As soon as I have, I'll confirm your date." It's awkward, but much less awkward than the alternative, which is a client who believes she's booked a date that you've given to someone else.

**Fix it for next time.**

- In your brief: "Never state that a booking is confirmed, a date is held or a payment is received. I will tell you when it is."
- Never draft a confirmation until you've run the deposit checklist. Make it a habit to open your payment system before you open the AI.
- Watch for the words "reserve," "hold," "secure," "lock in" and "all set." Cut them from any draft sent before a booking is confirmed.

## When a schedule has overlapping appointments

**What it looks like.** The schedule looks tidy, but a bridesmaid is in your chair from 8:25 to 9:05 and in the hair chair from 8:45. Or your associate's setup starts before she arrives. Or a row ends at 9:15 and the next starts at 9:10. Or the totals add up only because a 40-minute service has become 35 minutes.

**Why it happens.** Chat tools are weaker at keeping track of time across several people than they are at writing. They'll often produce a schedule that's correct row by row but impossible when you look at a single person's morning.

**Fix the draft.** Don't patch individual rows. Go back to the five-step worksheet from Chapter 5 and do the sum by hand. Then ask the AI for the person view, with the instruction "Don't move any appointments. Only report." Resolve clashes yourself, with the hair stylist where needed.

**Fix it for next time.**

- Always include "Do not shorten any service" and "Do not change the buffer" in your schedule prompts.
- Ask the AI to show the total minutes needed and available before it lays out the schedule. If its totals don't match yours, stop there.
- For two-artist or two-team mornings, build each artist's column separately, then combine. It's easier for you and for the tool.
- Never send a schedule to the bridal party until you've done the person check yourself. This is the one step in the book that should never be skipped.

## Smaller problems

**The draft is too long or too gushing.** Add a word limit to every prompt ("under 70 words") and put your "Never say" list in your brief. If a draft is still overwritten, ask: "Cut this by half. Keep every fact."

**The draft mixes up details from another booking.** This happens in long conversations, or when you've discussed two leads in the same chat. Start a fresh conversation for each booking task, and use the lead ID in every prompt.

**The tool won't do the arithmetic, or does it wrong.** Do the arithmetic yourself (you should be anyway) and give the tool the results. Its job is to present your numbers clearly, not to calculate them.

**The draft sounds like everyone else's.** Add three real messages you've sent to your brief as examples of your voice, with names removed. Ask the tool to match them. Then edit the first line and the last line of every draft yourself. Those are the lines clients notice most.

**A client's message looks AI-written, and it's confusing.** It happens. Long, formal messages with lots of headings, from a client whose earlier messages were short and chatty. Ask the AI to summarize what the client is actually asking for, in one line per request. Then reply to those requests, in your own short style.

**The tool refuses or adds a disclaimer.** Some tools are cautious about anything that sounds like legal or financial advice. If it won't draft something about your terms, that's a good sign it shouldn't: refer the client to your agreement instead.

**You've pasted something you shouldn't have.** It happens to everyone once. Delete the conversation, check your tool's data settings, and if the information was sensitive (health details, payment details), think about whether your data protection obligations mean you need to do anything more. Then make your placeholder habit stronger, so it doesn't happen again.
