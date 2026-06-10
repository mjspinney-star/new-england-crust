# New England Crust — Cowork Pinterest Schedules

Two scheduled tasks to set up in Cowork. Together they keep a steady pipeline
of Pinterest pins flowing — enough to post 1-2 per day every day of the week.

---

## HOW THE SYSTEM WORKS

- **Wednesday:** Cowork generates fresh headline ideas into the Ideas Bank
- **Thursday (you):** Review Wednesday's ideas, pick your favorites, promote
  10-14 of them into the Pin Queue with full details filled in
- **Friday:** Cowork generates all queued pins as PNGs in one batch
- **Daily:** You post 1-2 pins to Pinterest from the outputs folder

Target: always have at least 14 pins ready to post (2 weeks of daily content).
If the buffer drops below 7, add more items to the queue mid-week.

---

## SCHEDULE 1 — Headline Generator

**Task name:** Pinterest Headline Ideas
**Frequency:** Weekly — Wednesday
**Goal:** Fill the Ideas Bank with enough fresh angles to support 10-14 pins per week

**Prompt to paste into Cowork:**

First run `git pull` in `/Users/michaelspinney/Desktop/new-england-crust` to
sync the latest posts. Then read all blog posts in
`/Users/michaelspinney/Desktop/new-england-crust/src/content/blog/` to
understand what posts are currently live. Then read
`/Users/michaelspinney/Desktop/new-england-crust/Pinterest/pinterest-pin-queue.md`
in full — pay close attention to the Headline Style Guide section, the existing
Ideas Bank, and any items already in the Pin Queue so you don't duplicate them.

Generate 5-7 new Pinterest headline ideas for EACH live blog post. Write them
as bullets under the correct post heading in the Ideas Bank section of the queue
file. Follow the voice rules, headline patterns, and avoid list in the Headline
Style Guide exactly — every idea must sound like New England Crust, not a
generic affiliate blog.

Requirements for each headline idea:
- First-person plural voice ("we", "our")
- Specific and honest — no vague superlatives
- Uses one of the proven patterns from the style guide
- Different angle from any idea already in the Ideas Bank for that post
- Suitable for a Pinterest vertical image pin

Do not touch the Pin Queue section. Do not generate full pin details — ideas
only. Commit the updated queue file with the message "Added Pinterest headline ideas".

---

## SCHEDULE 2 — Pin Generator

**Task name:** Pinterest Pin Generator
**Frequency:** Weekly — Friday
**Goal:** Generate all queued pins as PNGs in one batch — enough for a full week of daily posting

**Prompt to paste into Cowork:**

First run `git pull` in `/Users/michaelspinney/Desktop/new-england-crust` to
sync the latest files. Then read
`/Users/michaelspinney/Desktop/new-england-crust/Pinterest/pinterest-pin-queue.md`
and find ALL items marked `[ ]` in the Pin Queue section.

For each `[ ]` item:
1. Add an entry to the PINS list in
   `/Users/michaelspinney/Desktop/new-england-crust/Pinterest/pinterest-pin-generator.py`
   using the photo, category, headline, descriptor, and output filename specified
2. Make sure the photo file exists in the Pinterest folder before running —
   if a photo is missing, skip that pin and leave a note in the queue file

Run `python3 pinterest-pin-generator.py` from the
`/Users/michaelspinney/Desktop/new-england-crust/Pinterest/` folder.

After running:
- Confirm each expected PNG exists in the `outputs/` folder
- Mark each successfully generated pin as `[x]` in the queue file
- If any pin failed, mark it `[!]` and note the reason
- Commit all changes with the message "Generated Pinterest pins — [date]"

If there are no `[ ]` items in the queue, stop and output this message:
"Pin queue is empty. Add items to the Pin Queue in pinterest-pin-queue.md
before Thursday so Friday's run has content to generate."

---

## THURSDAY CHECKLIST (your 5-minute job)

This is the only manual step in the system. Every Thursday:

1. Open `pinterest-pin-queue.md`
2. Review Wednesday's new ideas in the Ideas Bank
3. Pick your 10-14 favorites
4. For each one, copy the pin template and fill in all details:
   - photo (use existing photos or add a new one to the Pinterest folder)
   - category, headline, descriptor, output filename, board, link
5. Paste completed entries into the Pin Queue section marked `[ ]`
6. Save the file — Friday's run will handle the rest

**Minimum to promote each Thursday:** 10 items (keeps daily posting on track)
**Target:** 14 items (gives you a 2-week buffer if you miss a week)

---

## POSTING SCHEDULE (daily, done by you)

Pinterest rewards accounts that post consistently every day over accounts
that post in bursts. Stick to this:

- Post 1-2 pins per day, every day
- Spread them out — morning and evening if posting twice
- Never post more than 3 in one day
- Use the title, description, and link copy from the queue file for each pin
- Mark each pin `[p]` in the queue file after posting

**Boards to rotate through:**
- Ninja Woodfire Oven
- Backyard Pizza Night
- Outdoor Pizza Ovens
- Pizza Night Recipes
- (add more boards as your content grows)

---

## BUFFER HEALTH CHECK

Check this weekly — if your buffer drops below 7 unposted pins, add more
items to the Pin Queue mid-week and run the generator manually in Cowork:

> "Run the Pinterest pin generator now — read pinterest-pin-queue.md, generate
> all [ ] items, save PNGs to the outputs folder, and mark them [x]."
