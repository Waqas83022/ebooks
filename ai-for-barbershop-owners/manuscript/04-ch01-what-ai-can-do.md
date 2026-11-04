# Chapter 1: What AI can and can't do in a barbershop

Dre Ellis opened Cedar Street Barbers eleven years ago with one chair, a secondhand Belmont and a cash box. He is good with people and better with clippers. He is not, by his own description, "a computer guy". His nephew set up the booking app. The shop's Instagram was run by whoever had a free minute, which meant nobody.

The first time Dre tried an AI chat assistant, he typed: *write me a post for my barbershop*. He got back three paragraphs about "elevating your grooming experience" in "the heart of the community", with five hashtags and an emoji of a pair of scissors. It sounded like a hotel brochure. He closed the app and did not open it again for a month.

That first attempt is where most barbers stop. The tool did exactly what it was asked, and what it was asked was nearly nothing. It did not know the shop's name, its prices, its street, its barbers, or what Dre wanted the post to achieve. So it filled the gaps with the most average barbershop post it could imagine.

This chapter explains, without jargon, what is happening when you type into one of these tools, which jobs in a barbershop it does well, which it does badly, and which ones it should never touch.

## What a chat assistant actually is

The tools this book uses are called large language models, but you can forget that name. In practice, a chat assistant is a program that has read an enormous amount of text and learned the patterns of how words follow each other. When you give it a request, it writes the response that best fits the patterns, one word after another.

That explains both its strength and its weakness.

The strength: it writes fast and it writes fluently. It knows what a friendly appointment reminder sounds like, what a polite reply to a bad review looks like, and how a price list is usually laid out. Give it your facts and a clear job, and it will draft in ten seconds what might take you twenty minutes on your phone.

The weakness: it does not *know* anything about your shop unless you tell it. It cannot see your calendar. It does not know that Tomás is off on Wednesdays or that you stopped doing designs last spring. And when it lacks a fact, it does not stop and say so unless you ask it to. It writes whatever would most plausibly come next. Sometimes that plausible guess is right. Sometimes it is a confident, made-up price.

Some assistants can now search the web, read files you upload, or connect to other apps. Those features help, but they do not change the basic rule. The assistant works from what it is given. Your job is to give it the right material and check what comes back.

## The main tools, briefly

You do not need all of them. Pick one and get comfortable.

**General chat assistants.** ChatGPT (from OpenAI), Claude (from Anthropic), Gemini (from Google) and Microsoft Copilot all do the work in this book. Each has a free version and a paid tier, which as I write usually costs around $20 a month. The free tiers are enough to start. Paid tiers usually give you more use per day, better models, and the ability to save instructions or upload files. If you already live in Google's apps, Gemini will feel familiar. If you use Outlook and Word, Copilot might. Otherwise, try two for a week and keep the one whose writing sounds most like you.

**AI features inside booking software.** Most booking platforms built for barbers and salons, such as Square Appointments, Booksy, Fresha, Vagaro, SQUIRE and others, have been adding AI features: automatic reminders, waitlists that fill cancellations, suggested replies, marketing campaigns and, in some cases, an AI receptionist that answers calls and messages. These can be useful because they can see your real calendar. Chapter 8 explains how to judge them.

**AI receptionists and phone agents.** These answer your shop's phone with a natural-sounding voice, answer basic questions and either book the client or send them a link. Some are built into booking platforms, others are separate services that connect to your calendar. They cost real money each month, so they belong in a later stage, after you have the basics in place.

**Design and photo tools.** Canva, the editing tools on your phone, and the features built into Instagram and TikTok can now remove backgrounds, fix lighting and suggest captions. Useful for posts, covered in Chapter 5.

You do not need anything else to use this book.

## Seven jobs AI does well in a barbershop

Here is where an assistant earns its keep. In each case, it does the first draft and you make the call.

**1. Writing messages.** Reminders, replies to "how much for a cut", missed-call texts, rebooking nudges, holiday-hours notices, the message to a regular you have not seen in two months. These are short, repetitive and need to be friendly and correct. That is the sweet spot.

**2. Writing for the public.** Instagram captions, Google Business Profile posts, the "About" section on your website, the service descriptions on your booking page, a flyer for the gym next door. AI is fast at turning your rough notes into clean copy, and at writing three versions so you can pick.

**3. Replying to reviews.** It can draft a warm thank-you to a five-star review in your voice, and, more usefully, help you write a calm reply to a harsh one at a moment when you are not calm.

**4. Making sense of numbers.** Paste in last month's appointment export (with client names removed) and ask which hours were empty, which services grew, and how many first-time clients came back. It will not replace your accountant, but it will turn a spreadsheet you have been avoiding into three plain sentences.

**5. Writing policies and checklists.** Late-arrival policy, no-show policy, opening and closing checklists, a new-barber onboarding sheet, a walk-in rule for Saturdays. You know the rules. AI writes them down clearly and consistently.

**6. Brainstorming.** Ideas for a back-to-school promotion, ten things to post when you have no new cuts to photograph, five ways to partner with the boxing gym down the road. Most ideas will be ordinary. One or two will be good, and that is enough.

**7. Practicing conversations.** Ask it to play an angry client who was overcharged, or a new client nervous about his first fade, and practice what you would say. This is surprisingly useful for training a new front-desk person or a junior barber.

## Five jobs it should not do alone

**Setting prices.** AI can lay out the arithmetic of a price change (Chapter 11 shows how), but it does not know your rent, your competitors' quality, or what your clients will tolerate. It should never quote a price that did not come from your menu.

**Promising appointments.** A chat assistant that is not connected to your live calendar cannot know what is free. Any message that offers a specific time must be checked against the calendar before it goes out. Even AI tools that *are* connected to your calendar need testing (Chapter 8).

**Handling client data carelessly.** Do not paste client names, phone numbers, photos, health details (scalp conditions, allergies) or payment information into a general chat assistant. Use placeholders such as [first name] and fill them in inside your booking system. The rule of thumb: if you would not write it on a sticky note and leave it on the counter, do not paste it into a chat window.

**Making legal or employment decisions.** AI can explain what a chair-rental agreement usually covers or draft questions for your lawyer. It is not a lawyer. The rules on worker classification, texting consent, tips and licensing vary by state and country.

**Faking anything.** Fake reviews, invented testimonials, "before" photos of someone else's work, a made-up deadline ("only 2 slots left!" when there are nine). Apart from being dishonest, much of this is illegal. In the United States, a Federal Trade Commission rule announced in 2024 specifically bans fake reviews, including AI-generated ones. Chapter 6 covers this in detail.

## Why your first attempt was disappointing

Go back to Dre's first try: *write me a post for my barbershop*. It failed because the request had no facts, no goal and no limits. Compare it with this:

::: prompt
Write an Instagram caption for Cedar Street Barbers, a three-chair barbershop at 412 Cedar Street. The photo shows a mid skin fade with a hard part, cut by Tomás. Goal: get people to book a weekday appointment with Tomás. A skin fade costs $40 and takes 45 minutes. Booking link: [booking link]. Tone: relaxed and confident, like a barber talking to a regular, not an advertisement. Keep it under 60 words. No emojis, no hashtags, no words like "elevate" or "experience". Do not invent any facts that are not in this message.
:::

Same tool, same thirty seconds. Here is the kind of thing it returns:

> Mid skin fade with a hard part, done by Tomás this morning. If you've been meaning to tighten things up, he has weekday openings this week. Skin fades are $40 and take about 45 minutes. Book with Tomás here: [booking link]

That is a post a barber would actually write. The difference was not the tool. It was the instructions.

Chapter 3 turns this into a habit with a one-page shop brief, so you do not have to retype your facts every time. For now, remember the shape of a good request, because every prompt in this book follows it.

![Figure 1. The five parts of a good AI request. Fill in each one and the draft improves immediately.](images/fig01-prompt-anatomy.png)

1. Who you are: the shop, the barber, the kind of clients.
2. The facts: prices, times, names and links, and only verified ones.
3. The job: what to write and what it should achieve.
4. The format: length, tone, and where it will be used.
5. The limits: what to avoid, plus the instruction to leave gaps in [brackets] and not invent anything.

## Talking to it like a new hire

The most useful mindset I know is this: treat the assistant like a bright new front-desk hire on their first morning. Smart, fast, eager, and knows nothing about your shop.

You would not tell a new hire "handle the messages" and walk off. You would say: here is the price list, here is how we handle late arrivals, here's how we talk to clients, don't promise anything you're not sure of, and show me your replies for the first week. Then you would correct them: "Too formal, we don't say 'Dear sir'." "Good, but always put the booking link at the end."

Do the same with AI. When a draft is off, do not start again from scratch. Tell it what is wrong:

- *Shorter. Half the length.*
- *Too salesy. Sound like a barber texting a regular.*
- *Remove the second sentence. We don't offer that.*
- *Write three more versions, each with a different first line.*

Each correction makes the next draft better. After a few rounds you will have a reply you can save as a template and reuse for months.

## What it costs, and what it saves

Let us be concrete. A paid chat assistant costs roughly $20 a month. At Cedar Street's prices, that is less than one standard cut.

Now count the time. Suppose Dre spends twenty minutes a day on messages, posts and replies. Six working days a week, that is two hours a week, or about eight and a half hours a month. If AI drafting cuts that in half, Dre gets back four hours a month. Four hours is eight standard cuts, or $280 at the register if those hours can be filled. Even if only some of them can, the tool pays for itself many times over.

But time saved is not the main prize. The main prize is the work that never gets done at all today: the review that never gets a reply, the overdue regular who never gets a text, the Tuesday that never gets promoted. AI makes those jobs small enough that they finally happen.

## A note on privacy you should read twice

Every chapter of this book will remind you of this, so let me explain it once properly.

When you type into a general chat assistant, your words are sent to the company that runs it. Depending on the product and your settings, they may be stored, reviewed by staff for safety, or used to improve future models. Business and team plans often have stricter protections. Either way, treat the chat window as a place for drafting, not for storing client records.

In practice:

- Use placeholders: [first name], [phone], [appointment time], [booking link].
- Remove names and phone numbers before pasting any export of appointments or sales. Replace them with a client number if you need to tell people apart.
- Never paste card details, home addresses or anything about a client's health.
- Get written permission before you post a client's photo, and never upload client photos to an AI tool without that permission.
- Keep your booking system and your payment system as the single source of truth. AI summaries are a view, not the record.

Your clients trust you with their faces, their time and their conversation. Keeping that trust is worth more than any shortcut.

## Before your next shift

- Pick one chat assistant and create an account. Use the free tier for now.
- Try the Instagram caption prompt from this chapter with a real cut from this week. Edit it once by telling the assistant what to change.
- Write down the three messages you type most often. You will turn them into templates in Chapter 3.
