# Chapter 4: Make your shop easy to find locally

One Monday, Dre tried an experiment. He stood outside the boxing gym three blocks from his shop, took out his phone, and searched *barber near me*. Cedar Street did not appear in the three shops at the top of the map. The neon place did. So did a chain barbershop inside a supermarket a mile away. Cedar Street was fifth, below a salon that did not even cut men's hair.

Then he opened his own Google Business Profile, which he had not looked at properly in two years. The primary category was "Hair salon". Saturday hours said 9 to 5; the shop had opened at 8 for eighteen months. There were 23 photos, most of them of the storefront, several from the week the shop opened. No services were listed. No booking link. Thirty-eight reviews, the newest one seven months old, and not a single reply from the shop.

None of this was a disaster. All of it was costing him clients.

For most barbershops, the Google Business Profile is the most important page you have. It is often what a new client sees before they see your website, your Instagram or your front door. This chapter shows you how to fix it in an afternoon, how to keep it fresh with ten minutes a week, and how AI fits in.

## How Google decides who shows up

Google's own help pages say local results are based mainly on three things: relevance, distance and prominence.

**Relevance** is how well your profile matches what someone searched for. If your category is "Hair salon" and someone searches "barber", you are a weaker match than a shop listed as "Barber shop". If someone searches "skin fade" or "beard trim" and your profile lists those services, you look more relevant.

**Distance** is how far you are from the person searching, or from the place they searched for. You cannot move your shop, so forget this one.

**Prominence** is how well known your shop is. Google says this is based on information such as how many websites link to your business and how many reviews you have, and that more reviews and positive ratings can help your local ranking. A shop with 300 recent reviews and replies to most of them looks more established than one with 38 old ones.

There is no secret trick. You control relevance through an accurate, complete profile. You influence prominence through honest reviews, real photos and being mentioned around your neighborhood. That is the whole game.

![Figure 5. What decides local search, and what you control. Distance is fixed; relevance and prominence are yours to work on.](images/fig05-local-search.png)

## Step one: decide what you want to be known for

Before you touch the profile, answer one question: when someone in your area thinks of your shop, what should come to mind?

"A good barbershop" is not an answer. Every shop thinks it is a good barbershop. Look at your actual book. Who comes most? What do they ask for? What do your best reviews mention?

For Cedar Street, the answer came out of the Chapter 2 spreadsheet and a read through the reviews: skin fades and beard work, a relaxed shop where the same barber cuts you every time, kids welcome on weekdays, and Keisha for textured hair. That became a single line Dre could use everywhere:

*Neighborhood barbershop on Cedar Street for skin fades, beard work and textured hair. Same barber every visit. Kids welcome on weekdays.*

AI can help you find yours. Remove names, then paste in your twenty most recent reviews and your service list:

::: prompt
Here are 20 recent reviews of my barbershop and our service menu. Based only on what clients actually say, what are the three things we're best known for? Quote the review phrases that support each one. Then write three versions of a one-sentence description of the shop, under 25 words each, plain language, no words like "premier", "elevate" or "experience".
:::

Do not let the assistant invent a niche. If the reviews mention fades and friendly service, your line should too. If you want to be known for something your reviews never mention, that is a goal, and the work to get there is in the chair, not on Google.

## Step two: fix the profile

Sign in to your Google Business Profile (search for it while logged into the Google account that manages your shop). If you have never claimed your shop, Google will walk you through verification. Then work down this list. Most of it takes a couple of minutes per item.

**Name.** Use your real business name exactly as it appears on your sign. Do not add keywords ("Cedar Street Barbers Best Fades Downtown"). Google's guidelines forbid it, competitors can report it, and it can get your profile suspended.

**Primary category.** "Barber shop", if that is what you are. This is one of the strongest signals you control. You can add a few secondary categories if they are true, but do not pile them on.

**Hours, including special hours.** Check every day. Add holiday closures ahead of time; Google lets you set special hours for specific dates, and it is one of the most useful things you can do in November and December. Wrong hours lead to the worst kind of review: "drove 20 minutes and they were closed".

**Services.** List each service with its price, exactly as on your menu. This helps relevance ("skin fade" now appears on your profile) and answers the first question most people have.

**Booking link.** Add your online booking link as the appointment link. Some booking platforms connect directly to Google so people can book without leaving the search page; check whether yours does.

**Description.** You get 750 characters. Use them for facts: what you do, who you serve, where you are, how to book. Here is a prompt:

::: prompt
Using only the facts in my shop brief below, write a Google Business Profile description for my barbershop. Maximum 700 characters. Include: what we're known for (use this line: [your one-line positioning]), the main services, the area or landmark, parking, and how to book. Plain language, no keyword stuffing, no exaggerated claims, no prices (those go in the services list). Do not mention anything not in the brief.

[paste shop brief]
:::

Count the characters before you paste it in. Assistants are not reliable at counting characters; a phone notes app or a spreadsheet's LEN() formula is.

**Photos.** This matters more than most owners think. People choosing a barber want to see cuts, the inside of the shop, the barbers, and the front door so they can find it. Add:

- Ten or more photos of real cuts done in your shop, with good light and a clean background, shot with the client's permission.
- Three or four of the interior, taken when it is clean and not too crowded.
- One clear photo of the front door and sign from the street, and one of the parking entrance if it is hard to find.
- A photo of each barber at their chair, if they are happy to be shown.

Then add a few new photos every month. A profile whose newest photo is from 2019 tells a visitor the place might not have changed in five years.

Do not use AI-generated images of haircuts. It is tempting, because the generators make flawless fades. But a client who books because of a picture of a cut that never happened, in a shop that does not exist, will notice when they sit in your chair. Use AI to *improve* your real photos (fix the lighting, blur a messy background) if you like. Do not use it to invent them.

**Attributes and details.** Payment methods, accessibility (wheelchair-accessible entrance?), parking, whether you welcome kids, languages spoken. Fill in what is true.

**Updates.** Google lets you post short updates to your profile: a new barber, holiday hours, availability this week. They take two minutes, and AI can draft them. Chapter 5 turns them into a weekly habit.

## Step three: make every listing say the same thing

Your shop appears in more places than you think: Apple Maps (managed through Apple Business Connect), Bing Places, Yelp, Facebook, your booking platform's marketplace page, Instagram, your website, and a long tail of directories you never signed up for.

When those places disagree about your hours, phone number or address, two things happen. People get confused and some of them give up. And search engines are less confident they have the right information about you.

You do not need to chase every directory. Fix the big ones: Google, Apple, Bing, Yelp, Facebook, your booking page and your website. Use exactly the same business name, address format, phone number, hours and booking link in each.

AI is useful here as a checker. Copy the text from each listing into one chat:

::: prompt
Below are my barbershop's details as listed on six different sites. Compare them line by line against my shop brief. Make a table with one row per detail (name, address, phone, hours for each day, booking link, services and prices) and one column per site. Mark every place that differs from the brief.

[paste shop brief]\
[paste each listing, labeled with the site name]
:::

You will almost always find something: an old phone number on Yelp, last year's prices on Facebook, a closed-on-Tuesday that is no longer true.

## Step four: a first-visit page that does its job

If you have a website, its job is simple: help someone who has never been to your shop decide to book. If you do not have one, your booking page and Google profile do this job, and you can skip to the next section.

A first-time visitor wants answers to five questions, usually in this order:

1. Can they do the cut I want? (Photos of real cuts, the services list.)
2. How much will it cost? (Prices.)
3. Where is it, and can I park? (Address, a map, a photo of the door.)
4. What's it like? (A few lines about the shop and the barbers, a couple of real reviews.)
5. How do I book? (A booking button that is visible without scrolling on a phone.)

Here is a prompt to brief a web page, whether you build it yourself in Squarespace or Wix or hand the brief to someone else:

::: prompt
Write a brief for a one-page website for my barbershop, aimed at first-time clients who found us on their phone. Use only the facts in the shop brief below. Include:

1. A headline and one-sentence subheading.
2. The order of sections, with what goes in each.
3. Copy for each section, under 80 words per section.
4. A list of the photos I need to take, described specifically (for example: "close-up of a skin fade from the side, clean background").
5. Where the booking button should appear.\
Plain, friendly language. No claims we can't prove ("best in the city"). Mark anything you need from me as [MISSING].

[paste shop brief]
:::

Then open the finished page on your phone, standing outside, with one bar of signal. Can you see the booking button? Does the address tap through to the map? Does the page load before you lose patience? Most small-business websites fail this test, and nearly all of their visitors are on phones.

## Being found by AI assistants too

More people now ask an AI assistant for recommendations: *find me a barber near downtown who's good with curly hair and open on Saturday*. The assistant answers by pulling together what it can find, which typically means listings, reviews, websites and articles.

You cannot control those answers, and you should be wary of anyone selling a service that claims to. But the same work you have just done helps:

- Clear, factual text about what you do, in plain words, on your website and profile. "We cut textured and curly hair" is easy for a machine to understand. "Artistry for every crown" is not.
- Accurate hours, address and booking link everywhere.
- Plenty of recent, honest reviews. When clients mention specifics ("Keisha is great with curly hair", "they took my 5-year-old without drama"), those details travel.

In other words: describe your shop clearly and truthfully, and let your clients do the talking.

## Step five: borrow your neighbors' customers

Local visibility is not only online. The boxing gym, the tattoo studio, the coffee shop, the school uniform store, the wedding suit rental place: each has customers who need a barber and might ask the staff for a recommendation.

Give the businesses you trust the same thing you give Google: an accurate one-line description, your booking link, and, ideally, a link that shows the booking came from them. Many booking platforms let you create tracked links or add a "how did you hear about us" question. If yours does not, a simple code word ("Tell them Gus from the gym sent you") works.

Chapter 6 covers partnerships properly. For now, add the obvious neighbors to your list.

## How to tell if it worked

Your Google Business Profile shows performance numbers: how many people viewed it, called from it, asked for directions, clicked to your website or booking link. These are useful as a trend, especially after you fix the profile. Look at them monthly rather than daily.

But remember the rule from Chapter 2: views and clicks are not clients. The measure that matters is completed first visits that came from local search. The simplest way to count them is to ask every new client, at booking or at checkout, "How did you find us?", and record the answer the same way every time: Google, Instagram, friend, walked past, partner, other, unknown. Your booking system may have a field for this. If not, a tally sheet works.

After Dre fixed his category, hours, services, booking link and photos, and replied to every review from the previous year, he tracked first visits from Google for eight weeks against the eight weeks before. They went from 11 to 19. He could not be certain all of that was the profile; it was also the start of spring. But direction requests and booking-link clicks on the profile rose over the same weeks, and the "How did you find us?" answers pointed the same way. Good enough to keep going.

## Before your next shift

- Search for your services from three places around your neighborhood, and note where you appear.
- Fix your Google Business Profile: category, hours, special hours, services with prices, booking link, description.
- Take and upload ten real photos this week, with permission from the clients in them.
- Compare your main listings against your shop brief and correct anything that differs.
- Start asking every new client "How did you find us?" and record the answer.
