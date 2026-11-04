# Chapter 13: Cut the admin and keep shop records straight

On a Saturday in March, at 10:40 a.m., with every chair full and three walk-ins on the board, Cedar Street ran out of neck strips. Jaylen ran to the beauty supply store two miles away. Dre cut with towels tucked into collars for forty minutes and apologized to every client.

The following Sunday night, doing the books at his kitchen table, Dre found that the week's card payments were $85 lower than the services marked as completed in the booking system. He spent an hour trying to work out why. He never found out. He suspected a refund that nobody had written down, or a cut marked as paid in cash that had actually been comped for a friend. He let it go, the way most owners let these things go, and felt vaguely uneasy about it for a week.

None of this is exciting. All of it costs time and money, and almost every shop has some version of it. This chapter is about getting the back office (stock, end-of-week checks, commission and rent records, and automations) down to about an hour a week, with AI doing the drafting and summarizing and your booking and payment systems remaining the source of truth.

## The source-of-truth rule

Before anything else, decide where the real records live, and say it out loud to your team.

At Cedar Street:

- **The booking system** is the record of appointments: who was booked, with whom, for what, and whether they showed up.
- **The payment system** (card reader and register) is the record of money taken: card, cash, tips, refunds.
- **The accounting software or the accountant** is the record of the business's finances.

AI summaries, spreadsheets you build, notes on your phone: those are views. They help you understand the records. They never replace them. If an AI summary says you took $4,120 last week and the payment system says $4,035, the payment system is right, and your job is to find out why the summary is wrong.

This sounds obvious. It stops being obvious at 11 p.m. on a Sunday when an AI tool has given you a tidy table and the real export is a mess.

## The stock sheet

Running out of something on a Saturday is a planning problem, not bad luck. The fix is a reorder point for every item you cannot work without.

A reorder point is the stock level at which you order more, so that the new stock arrives before you run out. The formula is simple:

**Reorder point = weekly use × weeks it takes to arrive + a safety buffer.**

Neck strips at Cedar Street: about 6 rolls a week across three chairs, delivery takes about one week from the supplier, and Dre wants a week of buffer for busy periods. Reorder point = 6 × 1 + 6 = 12 rolls. When the shelf drops to 12 rolls, order.

Make a list of the items that would stop the shop or embarrass you if they ran out: neck strips, disinfectant, towels (or laundry pickups), blades and guards, shaving cream, the products you use on every client, retail stock that sells well, receipt paper, cleaning supplies. For each, estimate weekly use and delivery time. You do not need precision. A reasonable guess beats running out.

::: prompt
Here's a list of supplies for my barbershop with my rough estimate of weekly use and how long each takes to arrive after I order it. For each item, calculate a reorder point using: weekly use × delivery time in weeks + one week of safety stock. Put it in a table with columns: item, weekly use, delivery time, reorder point, and a suggested order quantity of about 4 weeks' use. Flag any item where I've given a delivery time longer than 2 weeks, as those need extra attention.

[paste list]
:::

Put the table on the stockroom door. The rule: whoever opens the box that takes an item below its reorder point writes it on the order list. Dre places one order a week, on Tuesday morning, from the list. He has not run out of neck strips since.

## The weekly close

Once a week, on your quiet day, spend 20 minutes checking that what happened in the chairs matches what happened in the till. This is where a missing $85 gets caught while you can still remember the week.

The weekly close checks four things.

**1. Services against payments.** Total value of completed services in the booking system for the week, against total payments taken (card plus cash), allowing for tips and gift card redemptions. They should match closely. If they do not, look for the gaps: a service marked complete but never paid, a payment with no matching service, a discount applied at the register but not in the booking system.

**2. Refunds, voids and discounts.** List every refund and void, every discount, and every service marked as free. Each should have a reason and a name. A discount that is not on your approved list (the referral reward, the make-good after a complaint) needs a conversation.

**3. Booking changes after the fact.** Appointments edited after they happened, services changed after completion, no-shows changed to completed. Most will be innocent corrections. A pattern is worth a look.

**4. Cash.** Count the drawer against the cash recorded. Small differences happen. The same difference every week does not.

AI is helpful here as a summarizer, provided you remove client names and card details first. Export the week from both systems, strip the personal columns, and ask:

::: prompt
Below are two exports from my barbershop for the week of [dates], with client names and card details removed. Export 1 is completed services from the booking system (date, time, barber, service, price, discount, status). Export 2 is payments from the card reader and register (date, time, amount, tip, method, refund yes/no).

1. Total completed service value (after discounts) and total payments (excluding tips).
2. The difference between them.
3. Try to match services to payments by date, time and amount, and list any services with no matching payment and any payments with no matching service.
4. List every refund, void and discount with its date and amount.\
Show your working. If the data doesn't let you match something confidently, say so rather than guessing.
:::

Then check the AI's totals against the totals in each system. If they match, use its list of unmatched items as your starting point. If they do not, the AI made an error with the data, and you go back to the systems.

When Dre started doing this weekly, the first close found two cuts marked "completed" on a Friday that had been comped for Tomás's cousins without a note, and a $45 refund processed on the card reader for a hot towel shave that a client had complained about, which had never been recorded in the complaint log. Neither was a problem. Both had a reason. But now there was a rule: every comp and every refund gets a note with a reason and a name, the same day. The next month's closes matched to within a few dollars of tips.

## Commission and rent records

If your barbers are on commission, the weekly close is also where commission gets calculated. Use the booking system's completed services, not memory, and give each barber a short written statement: services completed, total value, commission rate, commission due, any adjustments with reasons. AI can draft the template; the numbers come from the system.

If your barbers rent their chairs, keep a simple record of rent due and rent paid, with dates. Agree in writing what happens when a payment is late. Renters run their own businesses, so their sales and their clients' payments are theirs to track, not yours.

Either way, a clear written statement every week or month prevents most money arguments before they start.

## Bookkeeping: what AI can and cannot do

AI chat tools can help with the edges of bookkeeping. They can sort a bank export into categories you choose (supplies, rent, utilities, marketing, equipment), turn a pile of receipts into a list, draft questions for your accountant, and explain a term you do not understand in your accountant's email.

They should not be your bookkeeper, file your taxes, or decide how to classify a payment for tax purposes. Use proper accounting software or a bookkeeper for the records, and an accountant for tax. Before you paste a bank export into a chat, remove account numbers and anything identifying other people.

A useful habit: once a quarter, ask AI to turn your notes into a list of questions for your accountant. Twenty minutes of preparation makes a one-hour meeting far more useful.

## Automations: start in draft, keep a pause switch

By now, a lot of the shop's routine messages could run automatically: reminders, missed-call texts, review requests after completed visits, waitlist offers when a slot opens, rebooking nudges when a client is due. Most booking platforms can do much of this. Some AI tools can go further, reading messages and drafting or sending replies.

Automation saves a great deal of time. It can also send the wrong message to two hundred people in a minute. So bring automations in slowly, one at a time, up a ladder.

![Figure 14. The automation ladder. Each new automation climbs one rung at a time, and every rung has a pause switch.](images/fig14-automation-ladder.png)

**Rung 1: Manual.** You send the message yourself, from a template. You learn what clients reply and which wording works.

**Rung 2: Draft.** The system or AI prepares the message; a person reviews and sends it. You check what it would have said.

**Rung 3: Supervised.** The automation sends on its own, and a person reads every message it sent, daily, for the first couple of weeks.

**Rung 4: Automatic.** It runs on its own. Someone spot-checks weekly and reviews the numbers monthly.

Do not skip rungs for anything that goes to clients. A reminder template that has been running on rung 4 for a year is fine. A new AI reply assistant on your Instagram DMs should start at rung 2.

### The automation test plan

For each new automation, write a short test plan before you switch it on. It fits on an index card:

- What it does: "Sends a review request 2 hours after a completed visit."
- Trigger: what makes it fire.
- Who it messages: and who it must not (clients who opted out, clients with an open complaint, renters' clients).
- The message: the exact template, approved.
- Test: three fake clients (yourself, a team member, a friend) run through every path before any real client.
- First 20 sends: read every one.
- Pause switch: where it is and who can use it. Everyone on the team should know how to pause it.
- Owner and review date: one person, one date.

Here is a prompt that drafts the card for you:

::: prompt
I want to set up this automation in my barbershop: [describe it]. Write a one-page test plan with these headings: What it does, Trigger, Who it messages, Who it must never message, Message template, How to test it before going live (with 3 test cases), What to check in the first 20 messages, How to pause it, Owner, Review date. Point out anything that could go wrong, for example sending to someone who opted out, sending twice, or sending at night.
:::

And when something goes wrong, which it will at some point, pause first, fix second, explain third. A short, honest apology to anyone affected ("Sorry, that message was sent by mistake, please ignore it") is enough in most cases.

## An hour a week, mapped out

Here is how Dre's back-office hour on Monday mornings breaks down now:

- 20 minutes: the weekly close (services against payments, refunds and discounts, cash).
- 10 minutes: the scorecard (Chapter 2), filled in from the booking system.
- 10 minutes: stock check against reorder points; order placed.
- 10 minutes: reply to the week's reviews (Chapter 6), batched with AI.
- 10 minutes: the quiet-slot routine (Chapter 9), messages drafted for the week.

It used to be three hours on a Sunday night, done badly. It is now one hour on Monday morning, with coffee, done properly.

## Before your next shift

- Write down your sources of truth: booking system, payment system, accounting.
- Make a stock sheet with reorder points for every item that would stop the shop, and put it on the stockroom door.
- Do one weekly close this week. Note every gap you find and its reason.
- Make a rule that every refund and comp gets a note with a reason and a name, the same day.
- List your current automations and decide which rung each one is on.
