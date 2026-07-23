# New England Crust — Cowork Pinterest Schedules

Three scheduled tasks to set up in Cowork. Together they keep a steady pipeline
of Pinterest pins flowing — enough to post 1-2 per day every day of the week.

---

## HOW THE SYSTEM WORKS

- **Wednesday 3:00 PM:** Cowork generates fresh headline ideas into the Ideas Bank (Schedule 1)
- **Wednesday 4:00 PM:** Cowork promotes 4 ideas into the Pin Queue, one per post, and reports the unposted buffer count (Schedule 3)
- **Thursday (you):** Review Wednesday's ideas, promote 6-10 more into the Pin Queue with full details filled in
- **Friday 3:15 PM:** Cowork generates all queued pins as PNGs in one batch (Schedule 2)
- **Daily:** You post 1-2 pins to Pinterest from the outputs folder

Schedule 3 draws from the Ideas Bank that Schedule 1 fills an hour earlier. If
Schedule 1 fails, Schedule 3 still runs using older unused ideas — it will not
error, it will just draw from a staler pool.

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

If git pull fails for any reason, stop immediately and report the failure. Do
not proceed using local content — a failed pull means the repo may be behind,
and "up to date with origin/main" is not reliable in that state.

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
only. Commit and push by running: bash run-git-commit.command "Added Pinterest headline ideas" Pinterest/pinterest-pin-queue.md

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

If git pull fails for any reason, stop immediately and report the failure. Do
not proceed using local content — a failed pull means the repo may be behind,
and "up to date with origin/main" is not reliable in that state.

For each `[ ]` item:
1. Add an entry to the PINS list in
   `/Users/michaelspinney/Desktop/new-england-crust/Pinterest/pinterest-pin-generator.py`
   using the photo, category, headline, descriptor, and output filename specified.
   If the item includes a `badge_position` value, add it to the entry as
   `"badge_position": "top_left"` (or `"top_right"`) — otherwise omit it and
   the script will default to top_right.
2. Make sure the photo file exists in the Pinterest folder before running —
   if a photo is missing, skip that pin and leave a note in the queue file

Run `python3 pinterest-pin-generator.py` from the
`/Users/michaelspinney/Desktop/new-england-crust/Pinterest/` folder.

After running:
- Confirm each expected PNG exists in the `outputs/` folder
- Mark each successfully generated pin as `[x]` in the queue file
- If any pin failed, mark it `[!]` and note the reason
- Commit and push: bash run-git-commit.command "Generated Pinterest pins — [date]" Pinterest/pinterest-pin-queue.md

If there are no `[ ]` items in the queue, stop and output this message:
"Pin queue is empty. Add items to the Pin Queue in pinterest-pin-queue.md
before Thursday so Friday's run has content to generate."

---

## SCHEDULE 3 — Pin Queue Prework

**Task name:** Pin Queue Prework
**Frequency:** Weekly — Wednesday 4:00 PM (runs one hour after Schedule 1)
**Goal:** Promote 4 ideas from the Ideas Bank into the Pin Queue automatically,
reducing Thursday's manual load and keeping the buffer topped up

**Prompt to paste into Cowork:**

First run git pull in /Users/michaelspinney/Desktop/new-england-crust to sync the latest files.

If git pull fails for any reason, stop immediately and report the failure. Do not proceed using local content — a failed pull means the repo may be behind, and "up to date with origin/main" is not reliable in that state.

Read /Users/michaelspinney/Desktop/new-england-crust/Pinterest/pinterest-pin-queue.md in full.

Read all live blog posts in /Users/michaelspinney/Desktop/new-england-crust/src/content/blog/ to understand the actual content of each post.

List the contents of /Users/michaelspinney/Desktop/new-england-crust/Pinterest/ so you know which photo files are actually available.

Find 4 unused headline ideas in the ## IDEAS BANK section — ideas that do not already appear anywhere in the ## PIN QUEUE section as [ ], [x], or [p] entries.

IMPORTANT: all 4 ideas must come from 4 DIFFERENT posts. Never take two ideas from the same post in one run. Work down the Ideas Bank and skip any post you have already drawn from this run.

For each idea, format it as a queue entry using this exact structure:

### [ ] [Short descriptive title] — [Category] (Pin [N])
- **photo:** [filename]
- **category:** [Category label]
- **headline:** [Headline from Ideas Bank]
- **descriptor:** [1-2 supporting sentences, max 44 chars per line, 3 lines max]
- **output:** NEC-[postslug]-pin[N].png
- **board:** [Board name]
- **link:** https://newenglandcrust.com/blog/[post-slug]/

To determine the correct values:

- Photo: choose the file in the Pinterest folder that best matches the subject of that specific post. If no photo in the folder relates to the post, use NinjaWoodfireHero.jpeg and add this line directly beneath the photo field: - **photo-note:** GENERIC — swap when a post-specific photo is available. Never assign the same photo to more than one of the 4 entries in a single run unless the folder gives you no alternative.
- Category label: use the category rules in the ## HEADLINE STYLE GUIDE section.
- Descriptor: write from the actual post content you read. Follow the voice rules in the ## HEADLINE STYLE GUIDE — first-person plural, specific over vague, honest over hype. Match the tone of existing [p] entries.
- Pin number N: find the highest pin number already used for that post slug in the PIN QUEUE, then increment by 1.
- Board name: Ninja Woodfire Oven for gear/accessory/oven posts, Backyard Pizza Night for pizza night and recipe posts.
- Post slug: derive from the Ideas Bank section heading.

Insert all 4 formatted entries into the ## PIN QUEUE section, above any existing entries, interleaved so that no two adjacent entries share a post. Do not remove or modify any existing entries.

Then count the total number of [ ] and [x] entries in the PIN QUEUE that are not yet marked [p]. Report that number at the end of your run as "Unposted buffer: N".

Commit and push by running:
bash run-git-commit.command "Pre-filled Pinterest pin queue — [date]" Pinterest/pinterest-pin-queue.md

Do not stage or commit any other file. If the script reports PUSH FAILED, stop and report the failure — do not retry with different git commands.

---

## THURSDAY CHECKLIST (your 5-minute job)

This is the only manual step in the system. Every Thursday:

1. Open `pinterest-pin-queue.md`
2. Review Wednesday's new ideas in the Ideas Bank
3. Pick your 6-10 favorites
4. For each one, copy the pin template and fill in all details:
   - photo (use existing photos or add a new one to the Pinterest folder)
   - category, headline, descriptor, output filename, board, link
5. Paste completed entries into the Pin Queue section marked `[ ]`
6. Save the file — Friday's run will handle the rest

**Minimum to promote each Thursday:** 6 items (Schedule 3 supplies 4 more)
**Target:** 10 items (gives you a 2-week buffer if you miss a week)

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

Schedule 3 reports this number at the end of every Wednesday run as
"Unposted buffer: N" — check that line before deciding whether to add
items mid-week.
