# New England Crust — Pinterest Pin Queue

This file drives the weekly Pinterest pin generator. Cowork reads it every week,
generates any pending pins, and marks them done. All you need to do is add new
ideas below and drop photos into the Pinterest folder.

---

## WEEKLY WORKFLOW — READ THIS FIRST

**To add a new pin idea (takes 2 minutes):**
1. Think of a new headline angle for any of your live blog posts
2. Copy the template block from the "How to Add a Pin" section below
3. Paste it into the Pin Queue section and fill in the details
4. If it needs a new photo, drop the photo into this Pinterest folder
5. That's it — Cowork handles the rest on its weekly run

**To add a headline idea without full details yet:**
Just drop it in the Ideas Bank at the bottom. When you're ready to make it
a real pin, promote it to the Pin Queue with full details filled in.

**Posting cadence:**
- Generate: weekly (Cowork runs automatically)
- Post to Pinterest: 1-2 pins per day, spread through the week
- Don't post everything at once — Pinterest rewards consistency

**Tracking:**
- `[ ]` = ready to generate
- `[x]` = PNG created by Cowork
- `[p]` = posted to Pinterest

---

## HOW TO ADD A PIN

Copy this block, paste it into the Pin Queue section, and fill it in:

```
### [ ] YOUR TITLE HERE (just for your reference)
- **photo:** filename.jpeg  ← must be in this Pinterest folder
- **category:** Gear Guide  ← short label: Gear Guide, Pizza Night, Recipe, Tips
- **headline:** Your headline here  ← keep each line ~20 chars for clean wrapping
- **descriptor:** One or two supporting sentences, max 44 chars per line.
- **badge_position:** top_right  ← OPTIONAL — top_right (default) or top_left
- **flag:** FREE  ← OPTIONAL — adds a small ember/glow "FREE" corner badge, for lead-magnet pins only
- **output:** NEC-postname-pin#.png  ← e.g. NEC-accessories-pin7.png
- **board:** Pinterest Board Name  ← exact board name on your Pinterest profile
- **link:** https://newenglandcrust.com/blog/your-post-slug/
```

**badge_position notes:**
- Every pin now carries the New England Crust logo badge (flame + ring) in
  the top corner of the photo.
- Leave `badge_position` out entirely (or set to `top_right`) for the normal
  case — that's the default.
- Set it to `top_left` only if the photo's main subject sits in the top-right
  corner and the badge would otherwise overlap or cover it.

**Tips for good headlines (from your best performers):**
- Lead with the product name: "Ninja Woodfire Accessories..."
- Use tension: "Worth Buying (And What's a Waste)"
- Be specific: "After Months on the Patio..."
- Save language works well: "Save This Before You Buy"

**Available photos in this folder:**
- `NinjaWoodfireHero.jpeg` — oven on the Keter cart, blue siding background
- `IMG_8372.jpeg` — Caputo flour, yeast, La Baleine salt on white counter
- Add new photos here anytime — drop them in this folder and reference by filename

---

## COWORK INSTRUCTIONS

When the weekly scheduled task runs:
1. Read all `[ ]` items in the Pin Queue below
2. For each, add an entry to the PINS list in `pinterest-pin-generator.py`
3. Run `python3 pinterest-pin-generator.py` from this Pinterest folder
4. Confirm PNGs were saved to the `outputs/` folder
5. Mark each completed pin `[x]` in this file
6. Commit changes: bash run-git-commit.command "Generated Pinterest pins — [date]" Pinterest/pinterest-pin-queue.md

**Status markers:**
- `[ ]` — queued, ready to generate and post
- `[x]` — completed and posted
- `[p]` — previously posted / in the posted backlog (do not regenerate)
- `[!]` — held: link target not yet live (e.g. recipe committed but undeployed).
  Do not post. Revert to `[ ]` once the linked page is confirmed live.

If there are no `[ ]` items, do nothing and note the queue is empty.

---

## PIN QUEUE

---

### [ ] Nine Combos, Not Just Margherita — Pizza Night (Pin 1)
- **photo:** IMG_8372.jpeg
- **category:** Pizza Night
- **headline:** 9 Pizza Night Recipes That Aren't Just Margherita
- **descriptor:** Hot honey pepperoni to fig and
prosciutto — nine combos we
actually make on repeat.
- **output:** NEC-beyondmargherita-pin1.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/blog/pizza-night-recipes-beyond-margherita/

---

### [ ] Pellets Dry All Summer — Tips (Pin 1)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Tips
- **headline:** How We Keep Our Pellets Dry Through a Humid NE Summer
- **descriptor:** Coastal humidity ruins pellets
fast — our sealed-bucket,
silica-pack fix that works.
- **output:** NEC-pelletstorage-pin1.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/storing-pellets-new-england-summer/

---

### [ ] Why We Switched to 72 Hours — Recipe (Pin 1)
- **photo:** Photos/2026-07-17-dough-shots/dough-ball-machine.jpg
- **category:** Recipe
- **headline:** Why We Switched to 72-Hour Cold-Ferment Dough
- **descriptor:** Tuesday mix, Friday bake —
the schedule that fixed
our fighting, warm dough.
- **output:** NEC-72hourdough-pin1.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/blog/72-hour-cold-ferment-dough/

---

### [!] South Shore Bar Pizza — Recipe (Pin 1)
- **photo:** IMG_8372.jpeg
- **category:** Recipe
- **headline:** South Shore Bar Pizza — Cheese to the Very Edge
- **descriptor:** Cheese pushed to the pan
wall is what makes the
famous South Shore lace.
- **output:** NEC-southshore-pin1.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/recipes/south-shore-bar-pizza/

---

### [ ] Chicken, Bacon & Ranch — Recipe (Pin 1)
- **photo:** Chicken_Bacon_Ranch.jpg
- **category:** Recipe
- **headline:** Chicken, Bacon & Ranch — The Pie That Disappears First
- **descriptor:** Scratch ranch, crispy bacon,
650°F stone — the white pizza
guests reach for over margherita.
- **output:** NEC-chickenbaconranch-pin1.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/recipes/chicken-bacon-ranch/

---

### [x] Accessory We Regret Buying — Gear Guide (Pin 12)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Gear Guide
- **headline:** The Ninja Woodfire Accessory We Regret Buying
- **descriptor:** We bought a $25 cheat sheet and a
cleaning kit we never opened —
here's what we'd skip instead.
- **output:** NEC-accessories-pin12.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying/

---

### [x] What We'd Tell a New Owner — Gear Guide (Pin 13)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Gear Guide
- **headline:** Months In — Here's What We'd Tell a New Ninja Woodfire Owner
- **descriptor:** Months of pizza, pulled pork, and
dehydrated apple chips later —
here's our honest gear verdict.
- **output:** NEC-accessories-pin13.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying/

---

### [x] What's In the Box — Gear Guide (Pin 10)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Gear Guide
- **headline:** What's Already in the Box — And What We Bought Anyway
- **descriptor:** The OO101 comes with more than you'd
think — here's what's included and
what we still bought on day one.
- **output:** NEC-accessories-pin10.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying/

---

### [x] Buy-Immediately List — Gear Guide (Pin 11)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Gear Guide
- **headline:** Our Buy-Immediately List for the Ninja Woodfire (Under $80)
- **descriptor:** Cover, cord, peel, thermometer — the
four we bought before our first
cook, all in for under $80.
- **output:** NEC-accessories-pin11.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying/

---

### [p] Cover Before First Cook — Gear Guide (Pin 8)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Gear Guide
- **headline:** Don't Buy a Ninja Woodfire Cover Until You Read This
- **descriptor:** Official or third-party — we tested both through two months of New England rain and wind to see which held up.
- **output:** NEC-accessories-pin8.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying/

---

### [p] The $20 Stone Fix — Gear Guide (Pin 9)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Gear Guide
- **headline:** The $20 Accessory That Changed Every Pizza We Make
- **descriptor:** This $20 thermometer reads stone temp, not air temp — the 100°F gap that used to leave us with pale bottoms.
- **output:** NEC-accessories-pin9.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying/
- **note:** live twice on Pinterest as of 2026-07-18 — do not post again

---

### [p] Dough Starts Here — Recipe (Pin 3)
- **photo:** IMG_8372.jpeg
- **category:** Recipe
- **headline:** Our Dough Starts Here — Caputo 00, Lievito Yeast, La Baleine Salt
- **descriptor:** The exact three on our prep counter every cook — and why we've never swapped any of them out.
- **output:** NEC-00flour-pin3.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/blog/2026-06-15-the-difference-between-00-flour-and-bread-flour-wh/

---

### [p] The 4 Accessories Before First Cook — Gear Guide (Pin 7)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Gear Guide
- **headline:** The 4 Ninja Woodfire Accessories You Need Before Your First Cook
- **descriptor:** Cover, cord, peel, thermometer — the four we'd grab before your first cook. Under $80 total.
- **output:** NEC-accessories-pin7.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying/

---

### [x] Three Ingredients We Stock — Recipe (Pin 1)
- **photo:** IMG_8372.jpeg
- **category:** Recipe
- **headline:** The Three Ingredients We Always Have On Hand
- **descriptor:** Three ingredients, same every time — Caputo 00 is the foundation. Here's why we never switch.
- **output:** NEC-00flour-pin1.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/blog/2026-06-15-the-difference-between-00-flour-and-bread-flour-wh/

---

### [x] Why We Use Caputo 00 Flour — Tips (Pin 2)
- **photo:** IMG_8372.jpeg
- **category:** Tips
- **headline:** Why We Use Caputo 00 Flour for Every Pizza We Make
- **descriptor:** Finer grind, faster hydration, cleaner blistered edge. Here's why we landed on 00 and stayed.
- **output:** NEC-00flour-pin2.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/blog/2026-06-15-the-difference-between-00-flour-and-bread-flour-wh/

---

### [p] Accessories — Gear Guide (Pin 6)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Gear Guide
- **headline:** Ninja Woodfire Accessories Worth Buying (And What's a Waste)
- **descriptor:** After months on the patio — here's what earns its place and what's still sitting in a drawer.
- **output:** NEC-accessories-pin6.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying/

---

### [p] Pizza Night Setup — Pizza Night (Pin 5)
- **photo:** IMG_8372.jpeg
- **category:** Pizza Night
- **headline:** Your Backyard Pizza Night Starts Here
- **descriptor:** The exact setup we use every time — gear, stations, and the details that make it effortless.
- **output:** NEC-pizzanight-pin5.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/blog/backyard-pizza-night-setup/

---

### [p] Prime Day Pizza Oven Deals 2026 (Pin 1)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Oven Review
- **headline:** Prime Day Pizza Oven Deals — What's Worth Watching
- **descriptor:** Ooni, Ninja Woodfire, Solo Stove Pi — what to buy, what to skip, and when to check back.
- **layout:** primeday
- **badge_position:** top_right
- **output:** NEC-primeday-pin1.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/best-pizza-oven-deals/

---

### [p] Prime Day Accessories 2026 (Pin 1)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Gear Guide
- **headline:** Prime Day Pizza Accessories Worth Adding to Your Cart
- **descriptor:** The under-$50 picks we actually use — all on Amazon, all worth watching June 23–26.
- **layout:** primeday
- **badge_position:** top_right
- **output:** NEC-primeday-accessories-pin1.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/best-pizza-accessories-under-50/

---

### [p] Pizza Ovens Under $500 — Variation Pin 2
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Oven Review
- **headline:** Our Pizza Oven Buying Guide — Save This Before You Shop
- **descriptor:** Five ovens under $500 tested honestly — here's how we'd rank them and the one spec that matters most.
- **layout:** fullbleed
- **badge_position:** top_right
- **output:** NEC-ovens-pin2.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/best-outdoor-pizza-ovens-under-500/
- **note:** live twice on Pinterest as of 2026-07-18 — do not post again

---

### [p] Pizza Ovens Under $500 — Variation Pin 3
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Oven Review
- **headline:** Propane vs Pellets vs Electric — Which Outdoor Pizza Oven Is Actually Worth It
- **descriptor:** We tested all three fuel types. Here's the honest answer before you spend $300–$500.
- **layout:** split
- **badge_position:** top_right
- **output:** NEC-ovens-pin3.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/best-outdoor-pizza-ovens-under-500/
- **note:** live twice on Pinterest as of 2026-07-18 — do not post again

---

### [p] Infrared Thermometer — Accessory Pin Rework
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Tips
- **headline:** The $20 Tool That Fixed Every Pizza We Were Making Wrong
- **descriptor:** Your oven display shows air temp — not stone temp. This is the gap that ruins pizza. Here's what we use.
- **layout:** split
- **badge_position:** top_left
- **output:** NEC-thermometer-pin1.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/best-pizza-accessories-under-50/

---

### [p] Save Before You Spend $500 — Oven Review (Pin 4)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Oven Review
- **headline:** Save This Pizza Oven Guide Before You Spend $500
- **descriptor:** Our honest outdoor pizza oven comparison — Ninja Woodfire vs Ooni, tested side by side before you spend $500.
- **layout:** fullbleed
- **badge_position:** top_right
- **output:** NEC-ovens-pin4.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/best-outdoor-pizza-ovens-under-500/

---

### [x] 5 Tested, Only 2 Worth It — Oven Review (Pin 5)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Oven Review
- **headline:** 5 Outdoor Pizza Ovens Tested — Only 2 Were Worth It
- **descriptor:** Five ovens, real cooks — the pizza oven buying guide we wish we'd had before our first purchase.
- **layout:** split
- **badge_position:** top_left
- **output:** NEC-ovens-pin5.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/best-outdoor-pizza-ovens-under-500/

---

### [x] The Buying Mistake — Oven Review (Pin 6)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Oven Review
- **headline:** The Pizza Oven Buying Mistake Everyone Makes
- **descriptor:** The one spec most shoppers skip when picking the best outdoor pizza oven — it matters more than price or brand.
- **layout:** split
- **badge_position:** top_right
- **output:** NEC-ovens-pin6.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/best-outdoor-pizza-ovens-under-500/

---

### [x] Read This Before You Buy — Oven Review (Pin 7)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Oven Review
- **headline:** Read This Before You Buy an Outdoor Pizza Oven
- **descriptor:** Propane, pellets, or electric — our pizza oven buying guide covers what we'd buy again and skip.
- **layout:** fullbleed
- **badge_position:** top_left
- **output:** NEC-ovens-pin7.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/best-outdoor-pizza-ovens-under-500/

---

### [x] Pin This Checklist First — Oven Review (Pin 8)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Oven Review
- **headline:** Pizza Oven Shopping? Pin This Checklist First
- **descriptor:** Our best outdoor pizza oven picks under $500, plus the Ninja Woodfire vs Ooni question we get asked most.
- **layout:** split
- **badge_position:** top_left
- **output:** NEC-ovens-pin8.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/best-outdoor-pizza-ovens-under-500/

---

### [p] Don't Buy Until You've Seen This — Quick-Start Guide (Pin 1)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Gear Guide
- **headline:** Don't Buy Ninja Woodfire Accessories Until You've Seen This Free Checklist
- **descriptor:** The four accessories worth buying —
free, one page, no guessing
before you shop.
- **flag:** FREE
- **output:** NEC-quickstart-pin1.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/quick-start-guide/

---

### [p] The Only 4 Worth Buying — Quick-Start Guide (Pin 2)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Gear Guide
- **headline:** The Only 4 Ninja Woodfire Accessories Worth Buying — Free One-Page Cheat Sheet
- **descriptor:** Our exact buy-immediately list,
pellet picks, and setup —
free and printable.
- **flag:** FREE
- **output:** NEC-quickstart-pin2.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/quick-start-guide/

---

### [x] New Owner? Start Here — Quick-Start Guide (Pin 3)
- **photo:** Photos/2026-07-17-dough-shots/dough-ball-machine.jpg
- **category:** Gear Guide
- **headline:** New Ninja Woodfire Owner? Start With This Free Printable Shopping List
- **descriptor:** Skip the trial and error. Our
free quick-start guide covers
what to buy first.
- **flag:** FREE
- **output:** NEC-quickstart-pin3.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/quick-start-guide/

---

### [x] Setup Under $100 — Quick-Start Guide (Pin 4)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Gear Guide
- **headline:** Ninja Woodfire Setup Under $100 — The Free Quick-Start Guide
- **descriptor:** The exact accessories we bought
under $100 — grab the free
one-page guide.
- **flag:** FREE
- **output:** NEC-quickstart-pin4.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/quick-start-guide/

---

### [x] What's in the Box vs. What You Need — Quick-Start Guide (Pin 5)
- **photo:** Photos/2026-07-17-dough-shots/dough-ball-machine.jpg
- **category:** Gear Guide
- **headline:** What's in the Box vs. What You Actually Need to Buy (Free Ninja Woodfire Guide)
- **descriptor:** Free printable breakdown of
what Ninja includes and what
we bought anyway.
- **flag:** FREE
- **output:** NEC-quickstart-pin5.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/quick-start-guide/

---

### [p] Hosting? This Kit Plans It — Pizza Party Kit (Pin 1)
- **photo:** illustration:checklist  ← flat page/checklist illustration, no photo (see generator's draw_checklist_illustration)
- **category:** Pizza Night
- **headline:** Hosting Pizza Night? This Free Printable Kit Does the Planning for You
- **descriptor:** Timeline, dough math, and the
toppings list — free and
ready to print.
- **flag:** FREE
- **output:** NEC-partykit-pin1.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/pizza-party-kit/

---

### [x] Dough Math for a Crowd — Pizza Party Kit (Pin 2)
- **photo:** illustration:checklist  ← flat page/checklist illustration, no photo (see generator's draw_checklist_illustration)
- **category:** Pizza Night
- **headline:** How Much Pizza Dough for 12 People? The Free Party Kit Has the Math
- **descriptor:** Dough quantities by guest count,
free and printable — no more
guessing before guests arrive.
- **flag:** FREE
- **output:** NEC-partykit-pin2.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/pizza-party-kit/

---

### [x] The 48-Hour Timeline — Pizza Party Kit (Pin 3)
- **photo:** illustration:checklist  ← flat page/checklist illustration, no photo (see generator's draw_checklist_illustration)
- **category:** Pizza Night
- **headline:** The 48-Hour Pizza Party Timeline — Free Printable Planning Kit
- **descriptor:** Our exact 48-hour countdown,
free and printable — so party
day isn't a scramble.
- **flag:** FREE
- **output:** NEC-partykit-pin3.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/pizza-party-kit/

---

<!-- Backfilled 2026-07-18: the 13 entries below were found live on Pinterest but were
     never in this queue (posted outside the queue workflow). Board and link recorded
     exactly as verified on each live pin. -->

### [p] Clam Pie, New England Way — Backfilled from live profile
- **photo:** unknown — posted outside queue
- **category:** Recipe
- **headline:** Clam Pie, New England Way
- **descriptor:** No mozzarella. The clam liquor is the sauce.
- **output:** none — posted outside queue
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/recipes/clam-pie-new-england-way?utm_source=Pinterest&utm_medium=organic

---

### [p] Caputo 00 Bread Machine Dough — Backfilled from live profile
- **photo:** unknown — posted outside queue
- **category:** Recipe
- **headline:** Caputo 00 Pizza Dough in a Bread Machine — 3 Ingredients
- **output:** none — posted outside queue
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/recipes/caputo-breadmaker-dough/?utm_source=Pinterest&utm_medium=organic

---

### [p] Nobody Tells You This — Backfilled from live profile
- **photo:** unknown — posted outside queue
- **category:** Gear Guide
- **headline:** Nobody Tells You This Before You Buy a Ninja Woodfire
- **descriptor:** Four things we wish we'd known on day one.
- **output:** none — posted outside queue
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying?utm_source=Pinterest&utm_medium=organic

---

### [p] What Comes in the Box — Backfilled from live profile
- **photo:** unknown — posted outside queue
- **category:** Gear Guide
- **headline:** What Comes in the Ninja Woodfire Box (And What You Still Need)
- **output:** none — posted outside queue
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying?utm_source=Pinterest&utm_medium=organic

---

### [p] Realistic Accessory Budget — Backfilled from live profile
- **photo:** unknown — posted outside queue
- **category:** Gear Guide
- **headline:** The Realistic Ninja Woodfire Accessory Budget (Not the $600 Version)
- **output:** none — posted outside queue
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying?utm_source=Pinterest&utm_medium=organic

---

### [p] Accessories Actually Worth Buying — Backfilled from live profile
- **photo:** unknown — posted outside queue
- **category:** Gear Guide
- **headline:** The Ninja Woodfire Accessories Actually Worth Buying
- **output:** none — posted outside queue
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying?utm_source=Pinterest&utm_medium=organic

---

### [p] Half Are a Waste — Backfilled from live profile
- **photo:** unknown — posted outside queue
- **category:** Gear Guide
- **headline:** Half of Ninja Woodfire Accessories Are a Waste — Here's Which Half
- **output:** none — posted outside queue
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying/?utm_source=Pinterest&utm_medium=organic

---

### [p] Ninja Woodfire vs Ooni — Backfilled from live profile
- **photo:** unknown — posted outside queue
- **category:** Oven Review
- **headline:** Ninja Woodfire vs Ooni — Which One Should You Buy?
- **output:** none — posted outside queue
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/best-outdoor-pizza-ovens-under-500?utm_source=Pinterest&utm_medium=organic

---

### [p] Which Oven Is Actually Worth It — Backfilled from live profile
- **photo:** unknown — posted outside queue
- **category:** Oven Review
- **headline:** Which Outdoor Pizza Oven Is Actually Worth It?
- **output:** none — posted outside queue
- **board:** Outdoor Pizza Ovens
- **link:** https://newenglandcrust.com/blog/best-outdoor-pizza-ovens-under-500?utm_source=Pinterest&utm_medium=organic

---

### [p] Best Ovens Under $500 — Backfilled from live profile
- **photo:** unknown — posted outside queue
- **category:** Oven Review
- **headline:** The Best Outdoor Pizza Ovens Under $500
- **output:** none — posted outside queue
- **board:** Outdoor Pizza Ovens
- **link:** https://newenglandcrust.com/blog/best-outdoor-pizza-ovens-under-500/?utm_source=Pinterest&utm_medium=organic

---

### [p] Host Without the Stress — Backfilled from live profile
- **photo:** unknown — posted outside queue
- **category:** Pizza Night
- **headline:** How to Host a Backyard Pizza Night Without the Stress
- **output:** none — posted outside queue
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/blog/backyard-pizza-night-setup?utm_source=Pinterest&utm_medium=organic

---

### [p] Everything You Need for Pizza Night — Backfilled from live profile
- **photo:** unknown — posted outside queue
- **category:** Pizza Night
- **headline:** Everything You Need for the Perfect Backyard Pizza Night
- **output:** none — posted outside queue
- **board:** Backyard Pizza Night
- **link:** https://www.newenglandcrust.com/blog/backyard-pizza-night-setup/?utm_source=Pinterest&utm_medium=organic

---

### [p] Our Pizza Night Formula — Backfilled from live profile
- **photo:** unknown — posted outside queue
- **category:** Pizza Night
- **headline:** Our Backyard Pizza Night Formula
- **descriptor:** New England evenings, a hot stone, and wood smoke. The exact setup we use every time — gear, prep, and the details that make it effortless.
- **output:** none — posted outside queue
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/blog/backyard-pizza-night-setup/?utm_source=Pinterest&utm_medium=organic

---

### [x] Pesto, Fresh Mozzarella & Basil — Recipe
- **photo:** pesto-pizza-spreading-sauce-pin-1000x1500.jpg
- **category:** Recipe
- **headline:** Pesto, Fresh Mozzarella & Basil
- **descriptor:** Fresh pesto, torn mozzarella, basil laid on after the bake. The summer pie we make more than any other.
- **note:** photo-pin eligible — real photos now exist for this recipe, no illustration workaround needed. Pre-cropped 1000×1500 spreading-sauce shot used above; hero, dough-prep, topped-prebake, ninja-woodfire-oven, and slice-detail shots also live in the recipe's photo set if a different angle is wanted. Hero shot (pesto-mozzarella-basil-pizza-hero.jpg) is now also ready in Pin-kits/Pesto-mozzarella-basil/ as of 2026-07-21, for use as the source image in the next pin batch.
- **output:** NEC-pesto-pin1.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/recipes/pesto-mozzarella-basil?utm_source=Pinterest&utm_medium=organic

---

## IDEAS BANK — Not Yet Scheduled

### Caputo flour / ingredient photo (IMG_8372.jpeg) — future pin angles
- "The Three Ingredients We Always Have On Hand"
- "Why We Use Caputo 00 Flour for Every Pizza We Make"
- "Our Dough Starts Here — Caputo 00, Lievito Yeast, La Baleine Salt"
- Best paired with: 72-hour cold ferment dough post, or 00 flour vs bread flour post
- Photo: IMG_8372.jpeg — clean white counter, products clearly readable, no cropping needed

---

Park headline ideas here. When ready to produce, move them up to the Pin Queue
with full details filled in.

---

## HEADLINE STYLE GUIDE — FOR COWORK

Use this section when generating new headline ideas. Every headline must feel
like it came from a real person who cooks pizza in their backyard in New England
— not a generic affiliate blog.

### Voice rules
- Always first-person plural: "we tested", "our patio", "we use every time"
- Specific over vague: "after 6 months on the patio" beats "after extensive testing"
- Honest over hype: "what's a waste" and "what we'd skip" outperform "best ever"
- Coastal New England identity: salt air, deck, patio, backyard — not "outdoor kitchen"

### Headline patterns that work on Pinterest
Use these as formulas — fill in the specifics for each post:

**The honest verdict:**
- "Ninja Woodfire Accessories Worth Buying (And What's a Waste)"
- "[Product] — What We'd Buy Again and What We Wouldn't"
- "The [Topic] Guide Nobody Else Will Give You"

**The specific number:**
- "The 4 Accessories You Need Before Your First Cook"
- "9 Pizza Recipes That Aren't Margherita"
- "One Thermometer, Under $20, Changed Everything"

**The tension/contrast:**
- "Worth Buying. Worth Skipping."
- "Don't Buy [X] Until You Read This"
- "What the Box Includes — And What It Doesn't"

**The save signal:**
- "Save This Before You Buy Your First Accessory"
- "Pin This Before Your Next Pizza Night"
- "Bookmark This Before You Fire Up the Oven"

**The experience hook:**
- "After Months on the Patio — Here's What Actually Matters"
- "We Made This Mistake. You Don't Have To."
- "Your Backyard Pizza Night Starts Here"

**The comparison:**
- "Ninja Woodfire vs Ooni — Which One Is Actually Worth It"
- "We Tested Both. Here's the Honest Answer."
- "Why We Chose the Ninja Woodfire (And What We'd Change)"

### What to avoid
- Clickbait without payoff: "You Won't Believe This Pizza Oven"
- Vague superlatives: "The Best Pizza Ever"
- Generic affiliate tone: "Top 10 Must-Have Accessories"
- Exclamation points
- All caps headlines

### Descriptor rules (the gray text under the headline)
- One or two sentences max
- Sets up what they'll learn, not what the post contains
- End with a soft action: "save this", "here's what we use", "before your next cook"
- Max 44 characters per line, 3 lines total

### Category labels (coral text above headline)
Use exactly one of these:
- `Gear Guide` — accessories, equipment, setup
- `Pizza Night` — hosting, setup, entertaining
- `Recipe` — any food or dough recipe
- `Oven Review` — comparison or review content
- `Tips` — technique, troubleshooting, how-to

---

### Accessories post — additional angles
- "The 4 Ninja Woodfire Accessories You Need Before Your First Cook"
- "Don't Buy a Ninja Woodfire Cover Until You Read This"
- "The $20 Accessory That Changed Every Pizza We Make"
- "What's Already in the Box — And What We Bought Anyway"
- "Our Buy-Immediately List for the Ninja Woodfire (Under $80)"
- "The Ninja Woodfire Accessory We Regret Buying"
- "Months In — Here's What We'd Tell a New Ninja Woodfire Owner"
- "Our Ninja Woodfire Accessory Breakdown — Updated June 2026"
- "Our Final Verdict: Ninja Woodfire Accessories Worth Keeping"
- "Save This List Before You Over-Buy — Our Ninja Woodfire Picks"
- "What's Still in a Drawer After 6 Months — The Accessories We Skip"
- "Our Buy vs. Skip List for the Ninja Woodfire — Updated June 2026"
- "The Ninja Woodfire Accessories That Earned Permanent Patio Spots"
- "Why We Spent $80 on Accessories Before Our First Ninja Woodfire Cook"
- "Our Short List: Three Ninja Woodfire Accessories Worth Buying First"
- "The Ninja Woodfire Add-On That Replaced Something We Already Owned"
- "What Our Amazon Cart Looked Like Before Our First Ninja Woodfire Delivery"
- "The Accessories Still Going Strong After a Full Season on the Patio"
- "What We'd Buy for Someone Who Just Got a Ninja Woodfire as a Gift"
- "Our Revised Buy List — A Full Season of Cooks Later"
- "Before You Return It — These Three Accessories Make the Ninja Woodfire Click"
- "Our Three No-Regret Buys for the Ninja Woodfire Patio Setup"
- "The Ninja Woodfire Accessory We Bought Twice After Losing the First One"
- "Our Off-Season Storage Routine for Every Ninja Woodfire Accessory"
- "What We Pack in Our Ninja Woodfire Bag for a Cook at Someone Else's House"
- "The Accessory Question We Get Most From New Ninja Woodfire Owners"
- "Our Updated Accessory List Now That We've Owned the Oven a Full Year"
- "Why We Upgraded One Accessory Twice Before Getting It Right"
- "The Accessory We Almost Skipped That Turned Out to Be the Best Buy"
- "Our Ninja Woodfire Cart Setup — What Lives Where and Why"
- "The Accessory List We'd Hand a Neighbor Who Just Bought the Same Oven"
- "What We Learned Returning One Ninja Woodfire Accessory We Never Used"
- "Our Ninja Woodfire Cleaning Kit — The Three Things We Reach For"
- "The Accessory Upgrade Path We'd Follow If Starting Over Today"

### Pizza night setup — additional angles
- "How to Set Up a Pizza Night Station in Under 30 Minutes"
- "The Backyard Pizza Night Checklist We Use Every Time"
- "Pizza Night for a Crowd — The Setup That Actually Works"
- "Our Four-Station Pizza Night Setup, Explained"
- "What's Always on Our Toppings Bar"
- "The Oven Station Gear We Never Skip"
- "How We Turn Pizza Night Into a Hands-Off Dinner Party"
- "Our Ambiance Tricks for Backyard Pizza Nights"
- "The One Setup Step We Used to Forget (Until Now)"
- "Why Pizza Night Beats a Dinner Party for Us"
- "The Four-Station Pizza Setup We Use Every Single Time"
- "Our Dough Station Setup — Everything in Arm's Reach Before Guests Arrive"
- "What Our Toppings Bar Looks Like Before Anyone Gets Here"
- "How We Host Pizza Night for 10 People With One Oven and Two Peels"
- "The Host Trick That Keeps Us at the Oven, Not Stuck in the Kitchen"
- "What We Set Up the Night Before Pizza Night So Saturday Isn't a Scramble"
- "The Station Setup That Lets Our Kids Customize Their Own Pies"
- "What We Reset Between Each Pie — Our Quick-Turn Routine at the Oven"
- "Why Our Pizza Night Prep Starts 90 Minutes Before Guests Get Here"
- "The One Station Our Guests Always Drift Toward First"
- "What Our Backyard Looks Like at 4 PM Before a 6 PM Pizza Night"
- "Our Pre-Pizza Night Checklist — Everything Done Before We Fire the Oven"
- "The One Station We Added This Year That We Should've Had From Day One"
- "How We Set Up Pizza Night When It's Just the Two of Us, Not a Crowd"
- "Our Rainy-Day Backup Plan for Pizza Night We Never Cancel"
- "What We Moved Closer to the Oven After One Too Many Trips Inside"
- "The Lighting Setup That Keeps Pizza Night Going Past Sunset"
- "Our Cleanup Routine That Takes Less Time Than the Cook Itself"
- "What We Prep in the Kitchen So the Patio Stays Clear"
- "Our Music and Lighting Setup for a Pizza Night That Runs Late"
- "The Folding Table Trick That Freed Up Our Whole Patio"
- "What We Do Differently When Pizza Night Includes Kids"
- "Our Drink Station Setup So Nobody's in the Kitchen Twice"
- "The One Thing We Always Forget to Set Up Until Guests Arrive"

### Pizza oven comparison — additional angles
- "Ninja Woodfire vs Ooni — Which One Should You Actually Buy?"
- "The Best Outdoor Pizza Oven Under $500 (After Testing Several)"
- "Why We Chose the Ninja Woodfire Over the Ooni Koda"
- "The One Number We Check Before Buying Any Pizza Oven"
- "Our Honest Take on the Ooni Koda 12 — Worth the Hype?"
- "5 Pizza Ovens Under $500 — Here's How We'd Rank Them"
- "Propane vs. Pellets — What We'd Tell a First-Time Buyer"
- "Our $20 Tool for Checking Any Pizza Oven Is Actually Ready"
- "The Pizza Oven Mistakes We Made Before We Knew Better"
- "Our Pizza Oven Buying Guide — Save This Before You Shop"
- "The Spec We Check Before Any Pizza Oven Purchase (It's Not Wattage)"
- "Why We'd Tell a First-Time Buyer to Start With the Ooni Koda 12"
- "The Honest Pizza Oven Comparison Nobody Else Seems to Give"
- "Our Shortlist After Testing Five Pizza Ovens Under $500"
- "The First Three Pizzas From Every Oven We've Ever Tested"
- "What Most Pizza Oven Reviews Don't Tell You Before You Buy"
- "The Oven We'd Buy for Someone Who's Never Made Outdoor Pizza Before"
- "Our Second Oven Story — Why We Didn't Trade Up When We Could Have"
- "Which Pizza Oven Actually Made Us Better Cooks"
- "The Pizza Oven We'd Skip Even on Sale — And Why"
- "Before You Pull the Trigger: The One Question Every Pizza Oven Buyer Should Ask"
- "Our No-Return Rule for Pizza Ovens Under $500 — Read This First"
- "What We'd Ask an Oven Brand Before Buying If We Could Do It Again"
- "The Fuel Type We'd Choose First If New England Weather Wasn't a Factor"
- "Our Honest Answer on Resale Value After a Full Season of Ovens"
- "The Oven That Surprised Us Most After Testing All Five Side by Side"
- "What We Wish the Spec Sheets Told Us Before We Bought Our First Oven"
- "Our Honest Take on the Solo Stove Pi After a Full Season"
- "The Oven We'd Recommend for Small Patios and Tight Decks"
- "Why Wind Direction Changed Which Oven We Reached For"
- "Our Answer to 'Which Oven Cooks the Fastest' — We Timed It"
- "The One Oven Feature We Didn't Care About Until We Owned It"
- "What Changed About Our Ranking After a Full Year, Not Just a Season"

### Two Peels vs. One — additional angles
- "Do We Actually Need a Second Pizza Peel? Here's Our Answer"
- "One Peel Got Us Started — Here's When We Added a Second"
- "Turning Peel: Worth $30–$60? Our Honest Take"
- "The Pizza Peel Mistake We Made So You Don't Have To"
- "Metal vs. Wood Turning Peels — Why We Switched"
- "Our Rule: Buy One Peel First, Add a Second Later"
- "What a Turning Peel Actually Changed in Our Cooks"
- "The Second Peel We Debated Buying for Three Months — Worth It"
- "Why Our Turning Peel Lives on the Prep Table, Not in a Drawer"
- "What We Learned After 20 Cooks With Just One Peel"
- "Our Launch and Turn Setup — After a Full New England Season"
- "The Peel Upgrade We'd Make Again, Every Time"
- "The Cook That Finally Convinced Us a Second Peel Was Worth It"
- "Which Pizza Peel to Buy First — Our Recommendation by Oven Type"
- "The Peel Mistake That Burned Two Pizzas Before We Fixed It"
- "What a Perforated Launch Peel Changed About Our First Slide"
- "If We Could Only Own One Peel — Here's Which One We'd Choose"
- "Why Our Second Peel Cost Less Than Our First and Works Better"
- "Our Launch-and-Turn Peel Workflow, Step by Step"
- "The Peel Length We Wish We'd Known to Buy the First Time"
- "Why We Store Our Two Peels Differently — And It Matters"
- "One Peel for the Ooni, One for the Ninja — Here's Why We Split Them"
- "The Turning Peel Gift We'd Buy for Any New Backyard Pizza Cook"
- "Our Honest Price Breakdown: One Peel vs. Two, Total Cost Compared"
- "The Warped Wood Peel That Convinced Us to Switch to Metal"
- "How Long Our First Peel Lasted Before We Bought a Second"
- "The Peel We'd Buy First If We Only Had $30 to Spend"
- "Why Our Turning Peel Finally Earned a Hook Near the Oven"
- "The Peel Length Question We Get Asked Most Often"
- "What Changed the First Time We Used a Turning Peel Mid-Bake"
- "Our Honest Take: Is a Turning Peel Worth It for Home Ovens Under 700°F"
- "The Peel Combo We'd Recommend for a Ninja Woodfire Owner"
- "The Peel We'd Tell a Beginner to Skip Buying First"
- "Why Our Turning Peel Almost Went Back the Week We Bought It"
- "The One Peel Habit That Saves Us From Burnt Knuckles"
- "What We Do When We Only Have One Peel and Guests Are Waiting"
- "Our Peel Shopping Regret — And What We'd Buy Instead Now"
- "The Peel Question Every First-Time Oven Buyer Asks Us"
- "Why a Second Peel Didn't Fix Our Timing Problem — Practice Did"

### Cold-weather preheating — additional angles
- "Our Cold-Weather Pizza Oven Rule: Add 15–20 Minutes"
- "Why Our Propane Tank Comes Inside Before a Cold Cook"
- "Wind or Cold — Which Hurts Our Pizza Oven More?"
- "The Mistake That Burns Our First Pizza Every Cold Cook"
- "How We Keep Cooking Pizza Through a New England October"
- "Our Honest Take on Cold-Weather Wood Pellet Ovens"
- "Our Cold-Weather Pizza Checklist — Save This for Later"
- "Why Our Pizza Oven Takes 40 Minutes to Preheat on a 38°F Night"
- "The Cold-Weather Preheat Trick We Use Before Every Fall Cook"
- "Why We Bring the Propane Tank Inside Before a Cold-Night Cook"
- "How We Keep the Oven Hot When the Wind Picks Up"
- "What Changes About Our Pizza Cooks After Columbus Day"
- "Our First Cold-Weather Pizza Cook Was a Mess — Here's What We Fixed"
- "The Outside Temp Where We Stop Using Wood Pellets and Switch to Propane"
- "How Our Cold-Night Pizza Routine Differs From Our July Routine"
- "What 28°F Does to Your Pizza Oven's Preheat Time (We Timed It)"
- "Our Honest Answer: Is Cold-Weather Backyard Pizza Worth the Effort?"
- "The Wind Shield Setup We Use When the October Gusts Hit the Patio"
- "Why We Check the Stone Temp Twice on Cold Nights Before We Launch"
- "The Temperature Where We Just Call It and Cook Inside Instead"
- "Why Our Dough Behaves Differently in a Cold Kitchen, Not Just a Cold Oven"
- "Ninja Woodfire vs. Ooni in Cold Weather — Which Holds Heat Better"
- "The Insulated Cover That Cut Our Cold-Weather Preheat Time in Half"
- "What We Wear to the Patio for a 20°F Pizza Night (And Why It Matters)"
- "Our Per-Pie Cook Time Changes Once It Drops Below Freezing"
- "The One Gauge We Watch Closer Once the Temperature Drops"
- "The One Question We Get Every October About Cold-Weather Pizza"
- "Why We Skip Pizza Night Below a Certain Temperature — Our Cutoff"
- "What Changes About Our Dough Timing Once the Cold Sets In"
- "Our Cold-Weather Fuel Choice — What We Reach for After Halloween"
- "The Preheat Shortcut We Use When It's Too Cold to Wait 40 Minutes"
- "What We Wish We'd Known Before Our First November Pizza Night"
- "The Frost Morning That Taught Us to Respect Cold-Weather Preheating"
- "Why We Don't Trust the Ready Light in November"
- "Our Layered Clothing Rule for a Cold-Weather Pizza Night"
- "What Changes First When Temps Drop Below 40°F"
- "The Cold-Weather Cook We Almost Called Off — And Didn't"
- "Why We Add a Second Preheat Check Once Frost Hits the Deck"

### Dough readiness post — additional angles
- "The Poke Test We Use Every Time Before Opening Dough"
- "Our Dough Wasn't Ready — Here's What We Were Missing"
- "Cold Dough Needs 90 Minutes. Here's Why We Wait."
- "The Sign Our Dough Is Ready (And the One That Fooled Us)"
- "Gluten Relaxation, Explained the Way We Wish We'd Heard It"
- "Our Beginner Dough Mistake — and How We Fixed It"
- "Save This: How We Know Our Dough Is Ready to Stretch"
- "Our Two-Finger Poke Test — The Only Check We Do Before Shaping"
- "The Dough Signals We Missed Our First Six Months of Cooking Pizza"
- "Why Our Dough Fights Back on Cold Kitchen Days (And What We Do)"
- "What Over-Proofed Dough Looks Like — And How We Salvage It"
- "The 90-Minute Counter Rule We Follow Every Time We Cold-Ferment"
- "The Way Our Dough Feels When It's Not Ready — And When It Is"
- "What We Look for When We Open the Dough Container After 72 Hours"
- "Why Our Dough Is Always Tacky, Never Sticky — And What That Means"
- "The Moment Our Dough Started Behaving Better — It Wasn't the Recipe"
- "Our Three-Minute Dough Check Before Every Cook — No Guessing Involved"
- "Why the Poke Test Fails in a Cold Kitchen (And What We Do Instead)"
- "What Our Dough Smells Like When the Fermentation Is Right"
- "Same-Day Dough vs. Cold-Fermented — The Readiness Signs Are Different"
- "What Room Temperature Does to How Fast Our Dough Gets Ready"
- "The Bench Scraper Trick We Use Before We Even Touch the Dough"
- "Why We Let Our Guests Do the Poke Test Before They Stretch"
- "The Difference Between 'Ready' and 'Rushed' — We Learned This the Hard Way"
- "What Our Caputo 00 Dough Feels Like at the Ready Stage vs. Bread Flour"
- "What Our Dough Looks Like When It's Underproofed, Not Just Overproofed"
- "The Stretch Test We Do Right Before the Poke Test"
- "Why We Trust Our Fingers Over a Timer for Dough Readiness"
- "What a Cold Kitchen Does to Our 'Ready' Timeline"
- "Our Readiness Checklist for Guests Who Want to Help Shape"
- "The Dough Readiness Sign We Almost Always Get Wrong First"
- "The Dough Readiness Question We Answer the Same Way Every Time"
- "Why We Stopped Trusting the Clock and Started Trusting Our Hands"
- "What a Torn Edge Tells Us About Dough That Wasn't Ready"
- "Our Quick Fix When Dough Snaps Back Anyway"
- "The Readiness Test We Teach First-Time Guests in Thirty Seconds"
- "Why Two Dough Balls From the Same Batch Aren't Always Ready Together"

### Accessories under $50 — additional angles
- "10 Pizza Accessories Under $50 We Actually Use on Our Patio"
- "The $15 Scale That Fixed Our Dough Once and For All"
- "Our 5 Pizza Night Essentials, All Under $75 Combined"
- "What's in Our Pizza Toolkit — Nothing Over $50"
- "Our Honest Picks: Pizza Gear Under $50 That Earned a Spot"
- "Our Pizza Gear Picks — Save This Before You Buy"
- "The Pizza Tools We'd Buy Again for Under $50"
- "Our Patio Pizza Toolkit — Every Piece Under $50 and Actually Used"
- "What We'd Buy First for a Ninja Woodfire Setup Under $75 Total"
- "Our Short List: Pizza Night Gear That Earns Its Spot on the Shelf"
- "The Perforated Peel We Recommend Before Any Other Accessory"
- "Under $50 Pizza Accessories That Outperform $100 Options"
- "What We'd Buy With $50 If We Were Starting a Pizza Setup From Scratch"
- "The Accessories That Look Cheap and Actually Aren't"
- "Our Pizza Night Gift Ideas — All Under $50 and All Actually Used"
- "Three Pizza Accessories That Replaced Something We Spent More On"
- "The Pizza Tools We're Still Recommending Two Years In — All Under $50"
- "Our Go-To Amazon Picks for Pizza Night Under $25"
- "What Comes in the Oven Box — And the $30 Accessory We Always Add First"
- "The $12 Tool We Reach for More Than Anything Else on the Patio"
- "Why We Stopped Buying Cheap Peels and Started Buying Cheap Everything Else"
- "Our Winter vs. Summer Accessory Kit — What Changes Under $50"
- "The Kid-Safe Pizza Tools We Actually Trust Our Kids to Use"
- "What We'd Replace First If Our Whole Toolkit Broke Tomorrow"
- "The $50 Accessory Bundle That Replaced Three Separate Purchases"
- "Our Under-$25 Starter Kit for a Brand-New Pizza Oven Owner"
- "The Cheap Tool We Almost Didn't Buy That We Now Use Every Cook"
- "What We'd Skip Even Though It's Under $50"
- "Our Honest Ranking of Every Under-$50 Tool We Own"
- "The Accessory Bundle We'd Gift Someone New to Backyard Pizza"
- "Why We Still Reach for the Cheapest Tool in Our Kit Most Often"
- "The Cheapest Tool on This List That We Use the Most"
- "Our Answer to Which of These Accessories to Buy First"
- "What We'd Cut From This List If We Had to Pick Five"
- "Why We Still Recommend This List a Year Later"
- "The Accessory Under $50 We Almost Left Off This List"
- "Our Honest Take on Which of These Are Actually Necessary"

### 9 pizza night recipes — additional angles
- "9 Pizza Topping Combos We Keep Coming Back To"
- "Hot Honey Pepperoni — Our Pizza That Converts Skeptics"
- "The Korean BBQ Pizza Our Guests Talk About for Days"
- "Our Go-To Breakfast Pizza for the Morning After Pizza Night"
- "Beyond Margherita — 9 Pizzas We Actually Make on Repeat"
- "Our Fall Favorite: Apple, Gorgonzola, and Walnut Pizza"
- "Save These 9 Pizza Combos — Our Go-Tos for Pizza Night"
- "Our 9 Go-To Topping Combos When We're Tired of Playing It Safe"
- "The Pizza We Always Make for First-Time Backyard Pizza Guests"
- "9 Pizza Topping Ideas Worth Repeating All Summer Long"
- "The White Pizza Combo Our Guests Request a Second Slice Of"
- "Why We Make Hot Honey Pepperoni at Every Single Pizza Night"
- "The Pizza That Started Our Beyond-Margherita Obsession"
- "Our Summer Pizza Rotation — 9 Combos That Work Best on the Patio"
- "The Nine Pizza Topping Combos Our Crowd Always Finishes First"
- "The Pizza Our Kids Request Every Single Pizza Night — It's Not Margherita"
- "Our Most Debated Pizza Combo — and Why It Made the List Anyway"
- "Nine Pizzas We've Made Enough Times to Finally Write Down the Recipe"
- "The Seasonal Pizza Swap We Make at the Start of Every Fall"
- "The Vegetarian Pizza From Our List That Even the Carnivores Request"
- "What We Pair With Each of Our 9 Go-To Pizza Combos"
- "The Topping Combo We Almost Left Off the List — And Regretted"
- "Our Leftover-Ingredient Pizza — Built From Whatever's Left in the Fridge"
- "Which of Our 9 Combos Takes the Least Prep on a Busy Weeknight"
- "The Pizza From Our List We Make Exclusively in the Fall"
- "The Pizza From Our List That's Ready in Under 15 Minutes of Prep"
- "Our Kid-Approved Pick From the List — No Substitutions Needed"
- "The Combo We Add When We Have Extra Basil to Use Up"
- "Which of Our 9 Pizzas Pairs Best With a Cold Beer on the Patio"
- "The Recipe From Our List We Almost Cut for Being Too Simple"
- "Our Go-To Pick When We're Cooking for Someone With a Picky Palate"
- "The Combo From This List Our Neighbors Ask Us to Make Again"
- "Why This List Exists — We Got Tired of Making the Same Pizza"
- "Our Answer to Which of These Nine Takes the Most Effort"
- "What We Serve Alongside These Nine Pizzas"
- "The Recipe on This List That Surprised Us Most"
- "Why Margherita Still Makes the Cut Even With This List"

### Pellet storage — additional angles
- "How We Keep Our Pellets Dry Through a Humid NE Summer"
- "The $5 Trick That Saves Our Pellets All Summer"
- "Our Pellet Storage Setup: One Bucket, One Blend, One Label"
- "Signs Our Pellets Have Gone Bad (And What We Do Next)"
- "Oak, Maple, or Cherry — How We Choose Our Pellets"
- "Save This Before Your Pellets Get Damp — Our Setup Inside"
- "Our Rule: Pellets Out of the Bag the Day They Arrive"
- "Our Summer Pellet System — One Sealed Bucket Per Blend"
- "The Pellet Smell That Tells Us Something Went Wrong"
- "How Our Pellets Survive Coastal New England Humidity All Summer"
- "The $8 Lid That Saved Our Pellet Stash Last July"
- "Why We Label Every Bucket Before It Goes on the Shelf"
- "How We Store Pellets Through a New England Winter — Same System, Different Stakes"
- "Why We Stopped Buying Pellets One Bag at a Time"
- "The Pellet Blend That Stores Best Through Humidity — In Our Experience"
- "What Happens When You Let Moisture In — We Found Out the Hard Way"
- "Our Full Pellet Inventory System: Three Buckets, Three Blends, One Shelf"
- "The Storage Mistake That Cost Us an Entire Bag of Apple Pellets Last August"
- "When to Buy Pellets in Bulk and When to Hold Off — Our New England Logic"
- "Garage, Shed, or Basement — Where We Actually Store Our Pellets"
- "The Moisture Reading That Told Us Our Pellets Were Already Ruined"
- "Why We Buy Pellets in October, Not Just Before Grilling Season"
- "Our Off-Season Pellet Storage Setup for the New England Winter"
- "The Pellet Brand We Keep Coming Back to After Testing a Few"
- "The Bucket Size We Actually Recommend for a Season's Worth of Pellets"
- "Why We Check Our Pellets Before Every Single Cook, Not Just Storage Day"
- "Our Answer to Whether Pellets Really Go Bad or Just Get Worse"
- "What We Do With Pellets That Got a Little Damp But Aren't Ruined"
- "The Storage Setup That Finally Stopped Our Pellets From Clumping"
- "Why We Buy Two Blends Instead of Stocking Up on Just One"
- "The Storage Mistake We Won't Make Twice"
- "Why Humidity Sneaks Up on Pellet Storage Every Summer"
- "Our Answer to How Long Sealed Pellets Actually Last"
- "What We Check Before Every Bag Goes Into Storage"
- "The Bucket System That Finally Solved Our Pellet Problem"
- "Why We Buy Pellets Differently Than We Did Our First Season"

### 72-hour cold-ferment dough — additional angles
- "Our 72-Hour Dough Recipe — The One We Always Come Back To"
- "Our Dough Survives a Humid July and a Cold Ninja Stone"
- "66% Hydration, 3 Days — Our Go-To Pizza Dough Numbers"
- "One Dough, Two Ovens — How We Adjust for Ooni vs. Ninja"
- "Why We Cold-Ferment Our Pizza Dough for 72 Hours"
- "Our Pizza Dough Recipe Worth Sleeping On (Literally)"
- "Our Shortcut for Mixing Six Dough Balls at Once"
- "Why We Mixed a Full Batch of Dough the Night Before Last Friday"
- "The Dough We Make Every Thursday for the Weekend"
- "Our Friday-Night Dough Recipe — Made Over 50 Times and Still Our Go-To"
- "Why Cold Fermentation Made Our Crust Better Without Changing Our Oven"
- "What Our Dough Looks Like After 3 Days in the Fridge (And Why It's Ready)"
- "What We Tell Someone Who's Never Tried Cold-Fermented Pizza Dough"
- "48 Hours vs. 72 Hours vs. 96 Hours — What We've Tasted and What Changed"
- "Why Our Pizza Dough Takes 3 Days and Still Takes Less Than 30 Minutes of Work"
- "What We'd Tell Ourselves Before Our First Cold Ferment Attempt"
- "The One Dough Recipe We Come Back to After Every Experiment"
- "Why We Make a Full Batch of Six Dough Balls Every Single Thursday"
- "How Our Cold-Ferment Dough Changed After We Switched to 00 Flour"
- "What We Do With Dough Balls We Don't Use by Sunday"
- "Our Exact Mixing Schedule — Thursday Night to Saturday Pizza Night"
- "What Happens If You Let This Dough Go Past 96 Hours"
- "Store-Bought Dough vs. Our 72-Hour Recipe — We Tested Both Side by Side"
- "Why We Let Our Kids Help Mix the Dough Every Thursday"
- "The Freezer Trick That Saves Our Extra Dough Balls for Next Week"
- "What We Do Differently When We Only Have 48 Hours, Not 72"
- "Our Answer to Whether This Dough Freezes Well — We Tested It"
- "The Container We Switched to That Made Our Dough Rise More Evenly"
- "Why We Weigh Every Dough Ball Instead of Eyeballing It"
- "What Happens to This Recipe When the Kitchen Runs Warm"
- "Our Go-To Answer for Scaling This Recipe Up for a Crowd"
- "The Recipe We Trust Enough to Make Blind, No Notes"
- "Why This Dough Forgives Mistakes Ours Made in Year One"
- "Our Answer to Whether This Recipe Works in a Home Oven Too"
- "What Changed the First Time We Doubled This Recipe"
- "The Dough Timeline We Never Skip, Even When We're Busy"
- "Why We Recommend This Recipe to Every New Oven Owner"

### 00 flour vs. bread flour — additional angles
- "00 Flour vs. Bread Flour — What We Actually Use and Why"
- "Why We Switched to Caputo 00 for High-Heat Pizza Cooks"
- "The Flour Question We Get Every Pizza Night: What Do You Use?"
- "Bread Flour or 00 for Your Pizza Oven? Here's Our Honest Answer"
- "Why Flour Protein Percentage Actually Matters for Pizza Dough"
- "Our Rule: 00 Flour for the Ooni, Bread Flour for the Ninja"
- "The Flour Swap We Made After Our First Cold-Ferment Batch"
- "What Caputo 00 Actually Does to Your Crust That Bread Flour Doesn't"
- "The Crust Blister We Couldn't Get Until We Switched Flour"
- "Where We Buy Our Caputo 00 — And Why We Stopped Getting It at the Store"
- "The Hydration Adjustment We Make When We Switch Between Flours"
- "Why We Keep Both Flours on the Shelf — And Which One We Reach For First"
- "Our 00 Flour First-Bag Recommendation — What to Buy Before You Commit"
- "The Texture Difference Between Caputo 00 and Bread Flour — In One Bite"
- "All-Purpose, Bread, or 00 — Where Each One Actually Belongs in Pizza Dough"
- "How We Store Our Caputo 00 So It Doesn't Go Stale Between Bakes"
- "The Price Difference Between 00 and Bread Flour, Per Pizza"
- "Why We Keep a Bag of Bread Flour on Hand Even Though We Prefer 00"
- "The Protein Percentage Gap That Actually Changes Your Crust"
- "What Happens When You Use Bread Flour in a 900°F Oven"
- "Our Answer to Whether All-Purpose Flour Can Work in a Pinch"
- "The Bag Size We Actually Buy Now That We Go Through Flour Fast"
- "Why We Don't Sift Our 00 Flour and Never Have"
- "What We Noticed the First Time We Ran Out of 00 Mid-Batch"
- "Our Flour Shelf Life Answer After Storing Bags Through a Humid Summer"
- "The Flour We'd Recommend to Someone Who Just Bought Their First Oven"
- "The Bag We Grab Without Thinking Anymore — And Why"
- "What Happens When a Guest Brings the Wrong Flour to Pizza Night"
- "Our Answer to Which Flour Ages Better in New England Humidity"
- "The Flour Debate We Had in Our Own Backyard More Than Once"
- "Why Ten Minutes of Flour Talk Always Delays Pizza Night"
- "What We Tell Someone Buying Their First Bag of 00"

### Hand stretching vs. rolling pin — additional angles
- "Why We Banned the Rolling Pin From Our Pizza Setup"
- "What a Rolling Pin Does to Your Dough Bubbles (It's Not Good)"
- "The Hand-Stretch Move That Finally Clicked After Months of Tearing Dough"
- "What We Tell Every Guest Before They Touch Our Dough Table"
- "Why We Still Tear Dough Sometimes — And Why That's Fine"
- "The One Pizza Technique That Changed Our Crust More Than Any Oven Setting"
- "Our Gravity-and-Knuckle Method — The Stretch We Use Every Cook"
- "The Guest Hand-Stretch Lesson We Give Before Anyone Touches Our Dough Table"
- "What to Do When Your Dough Tears Mid-Stretch — Our Fix"
- "Our First Successful Hand Stretch — What Finally Made It Click"
- "What the Dough Is Telling You When It Won't Stretch Out"
- "Hand Position, Speed, and the One Thing We Did Wrong for Six Months"
- "Why We Use the Counter and Our Knuckles — Not a Peel — to Stretch Dough"
- "What Your Stretch Tells You About Whether the Dough Was Ready to Open"
- "How High-Hydration Dough Changes the Way We Hand-Stretch"
- "Teaching Our Kids to Hand-Stretch Without Tearing the Dough"
- "The Crust Difference Is Obvious the Moment It Hits the Stone"
- "Why Our Wrists Used to Ache Until We Fixed Our Stretch Technique"
- "What We Do the Moment the Dough Starts Springing Back"
- "The One Cue That Tells Us the Dough Is Stretched Thin Enough"
- "The Rolling Pin We Still Keep in the Drawer for One Specific Use"
- "Why Thin-Crust Lovers Might Actually Prefer the Rolling Pin"
- "Our Answer to Whether High-Hydration Dough Can Handle a Rolling Pin"
- "What We Tell Beginners Who Are Scared to Hand-Stretch"
- "The Difference in Bake Time Between Hand-Stretched and Rolled Dough"
- "Why We Changed Our Minds About the Rolling Pin After Years of Avoiding It"
- "The Guest Who Reached for the Rolling Pin Before We Could Stop Her"
- "Why Our Hands Do a Better Job Than Any Tool We've Tried"
- "What We Say When Someone Insists a Rolling Pin Is Easier"
- "The First Stretch That Actually Felt Right — What Changed"
- "Our Answer to Whether Beginners Should Start With a Rolling Pin Anyway"
- "Why We Keep Teaching This the Same Way Every Single Time"

### Infrared thermometer / reading the stone — additional angles
- "Why We Never Launch a Pizza Without an Infrared Reading First"
- "The 100°F Gap Between Your Oven Display and Your Stone — It Matters"
- "Why the Ninja Woodfire Display Doesn't Tell You What You Think It Does"
- "Stone Temp vs. Air Temp: The Number We Check Before Every Cook"
- "Our Pre-Launch Checklist — One Tool, One Number, No More Pale Bottoms"
- "How We Know the Stone Is Ready Before We Commit the Dough"
- "The $20 Thermometer Fix That Changed Our Stone-Reading Routine"
- "Our Target Stone Temp for Neapolitan Style vs. NY Style — Different Every Time"
- "How We Use the Infrared Thermometer Mid-Cook, Not Just Before Launch"
- "The Stone Temp Reading That Made Us Wait an Extra 10 Minutes — And Why It Mattered"
- "Which Infrared Thermometer We Actually Own and Use Every Cook"
- "What Undertemped Stone Looks Like on the Bottom of a Pizza Crust"
- "Our Pre-Cook Temperature Sequence — Stone, Dome, Wait, Check Again"
- "Why We Point the Thermometer at the Center of the Stone, Not the Edge"
- "The Hot Spot on Our Stone We Didn't Know Existed Until We Checked"
- "Using an Infrared Thermometer on the Ooni vs. the Ninja Woodfire"
- "Why We Check Three Spots on the Stone, Not Just the Center"
- "The Infrared Reading That Told Us to Rotate Instead of Wait"
- "What We Wish We'd Known About Stone Temp Before Our First Cook"
- "Why We Bought a Second Infrared Thermometer After Losing the First"
- "What Our Infrared Reads on the Coldest Spot of the Stone"
- "Our Answer to Whether a $10 Thermometer Works as Well as a $30 One"
- "The Reading We Wait for Before We Even Open the Dough Container"
- "Why We Trust the Thermometer Over the Oven's Built-In Gauge"
- "What Changed in Our Bake Once We Started Checking Stone Temp Mid-Cook"
- "The Thermometer We Almost Didn't Buy — And Wish We'd Bought Sooner"
- "Why the Display Number Stopped Mattering to Us Entirely"
- "Our One-Tool Rule Before Every Single Launch"
- "What a $20 Gadget Taught Us About Trusting Numbers Over Guesses"
- "The Reading That Changed How We Judge Every Cook Now"
- "Why We Recommend This Tool Before Any Other Pizza Purchase"

### Prime Day pizza oven deals 2026 — additional angles
- "Our Prime Day Watch List for Pizza Gear — June 23–26"
- "The Ovens Worth Tracking on Prime Day (And What to Skip)"
- "How We're Approaching Prime Day 2026 for Our Pizza Setup"
- "Why We're Watching the Ooni Koda 12 During Amazon Prime Day"
- "Prime Day Pizza Accessories — The Under-$50 Picks Worth Tracking"
- "Our Prime Day Strategy: One Oven, A Few Accessories, One Hard Budget"
- "The Price Drop We Need to See Before We Pull the Trigger on Prime Day"
- "When Prime Day Pizza Oven Deals Actually Go Live — Our Timing Guide"
- "Oven or Accessories First? How We'd Spend $300 on Prime Day"
- "The Prime Day Pizza Bundle Deals Worth Adding to Cart vs. Buying Separately"
- "If Prime Day Prices Disappoint — Our Backup Shopping Strategy"
- "The Prime Day Deal We Actually Pulled the Trigger On (And Why)"
- "Our Amazon Pizza Wishlist Going Into Prime Day 2026 — Saved and Ready"
- "Why We Check the Price History Before Any Prime Day Pizza Purchase"
- "What We Actually Bought During Prime Day 2026 — And What We Skipped"
- "How This Year's Prime Day Pizza Discounts Compared to Last Year's"
- "Our Backup Plan If the Ooni Koda 12 Doesn't Drop Enough on Prime Day"
- "Prime Day vs. Black Friday — Which One Actually Has Better Pizza Oven Deals"
- "The Prime Day Discount Percentage We Consider Worth Waiting For"
- "Our Live Notes From Prime Day 2026 — What Actually Dropped"
- "The Prime Day Deal We Watched All Week and Still Didn't Buy"
- "Why We Waited Until Day Two of Prime Day to Buy Anything"
- "Our Prime Day Regret — The Deal We Should Have Grabbed"
- "What We're Telling Friends Who Ask About Prime Day Pizza Deals"
- "The Prime Day Accessory Deal That Beat the Oven Discounts"
- "Our Answer to Whether Prime Day Deals Are Actually Worth Waiting For"
- "What We Learned Comparing This Year's Prime Day to Last Year's"
- "The Prime Day Purchase We're Glad We Waited On"
- "Why We Check Three Retailers, Not Just Amazon, During Prime Day"
- "Our Prime Day Rule: Never Buy the First Day's Price"
- "What We'd Tell Someone Tempted to Buy Full Price Before Prime Day"

### Finishing with good olive oil — additional angles
- "The Drizzle That Changed Our Margherita — And Why We Skip It on Loaded Pies"
- "Our Two-Bottle Olive Oil System for Pizza Night"
- "When Finishing Oil Actually Tastes Like Something on Pizza (And When It Doesn't)"
- "The Pizzas That Deserve Good Olive Oil — Our Running List"
- "What to Look for on an Olive Oil Label Before You Buy It for Pizza"
- "Why We Never Drizzle Finishing Oil Before the Launch — The Heat Kills It"
- "The White Pie Drizzle Move That Earned a Permanent Spot in Our Rotation"
- "The Olive Oil Brand We Keep Buying Back, Bottle After Bottle"
- "Why We Stopped Using Our Everyday Cooking Oil to Finish Pizza"
- "How We Store Our Finishing Oil So It Doesn't Turn Before We Use It"
- "The Pizza Where a Cheap Olive Oil Actually Ruined the Bite"
- "What a $25 Bottle of Olive Oil Does That a $10 Bottle Doesn't"
- "Our Answer to Whether Olive Oil Should Go on Before or After the Bake"
- "The Bottle We Keep Just for Pizza and Nothing Else"
- "Why a Peppery Finish Works on Some Pies and Ruins Others"
- "What We Learned Testing Three Olive Oils Side by Side on the Same Pizza"
- "Our Rule for How Much Oil Is Too Much on a Finished Pie"
- "The Pizza Where Skipping the Oil Was the Right Call"
- "The Oil We Reserve Only for Pies That Earn It"
- "Why Some Nights We Skip the Good Bottle Entirely"
- "Our Rule for Which Pies Get the Expensive Drizzle"
- "What We Learned Wasting Good Oil on the Wrong Pizza"
- "The Bottle Test That Settled This Debate for Us"
- "Why Timing the Drizzle Matters More Than the Brand"

### Fresh basil vs. dried — additional angles
- "Fresh or Dried Basil for a 90-Second Pizza Cook — Our Honest Answer"
- "Why Fresh Basil Burns Before Your Pizza Even Finishes Cooking"
- "The Dried Basil Trick We Use When Fresh Isn't Worth Buying"
- "When We Skip Fresh Basil Entirely — And Nobody Notices"
- "Our Rule for Adding Basil Before or After the Oven, Never During"
- "What a 900°F Oven Does to Fresh Basil in Under a Minute"
- "Save This Before You Buy Fresh Basil for Your Next Pizza Night"
- "Our Answer to Whether Basil Chiffonade Actually Matters Here"
- "The One Pizza Where We Always Insist on Fresh Basil, No Exceptions"
- "What Dried Basil Actually Tastes Like on a Wood-Fired Crust"
- "Why We Grow Our Own Basil Just for Pizza Season"
- "Our Test: Fresh Basil Added Pre-Bake vs. Post-Bake"
- "The Basil Mistake That Taught Us to Always Add It Last"
- "The Basil Call We Make Before Every Single Bake"
- "Why We Stopped Overthinking Basil and Started Trusting the Oven"
- "Our Backyard Basil Patch and What It's Actually For"
- "What We Tell Guests Who Bring Basil to Pizza Night"
- "The Pie Where Dried Basil Actually Won the Taste Test"
- "Why Timing Beats Fresh vs. Dried as the Real Question"

### What yeast to buy — additional angles
- "Instant, Active Dry, or Fresh Yeast — What We Actually Use for Pizza"
- "The Yeast Mistake That Kept Our Dough From Rising Right"
- "Why We Switched to Instant Yeast After Years of Active Dry"
- "Fresh Yeast Is Worth It Once — Here's Why We Went Back to Instant"
- "Our Honest Answer to the Yeast Question We Get Every Pizza Night"
- "The Yeast Swap That Changed Our 72-Hour Cold Ferment for the Better"
- "Save This Before You Buy Yeast for Your Next Batch of Dough"
- "Our Answer to Whether Yeast Expiration Dates Actually Matter"
- "The Yeast Storage Mistake That Cost Us a Flat Batch of Dough"
- "Why We Keep Two Types of Yeast in the Fridge at Once"
- "What Happens When You Use Too Much Yeast in a Cold Ferment"
- "Our Honest Take on Sourdough Starter vs. Commercial Yeast for Pizza"
- "The Yeast Brand We Keep Buying Back After Trying Cheaper Options"
- "The Yeast Shelf Confusion We Finally Settled for Good"
- "Why We Buy Yeast in Bulk Once We Found the Right One"
- "Our Answer to Whether Grocery Store Yeast Is Good Enough"
- "What We Tell Someone Making Their First Batch of Dough Ever"
- "The Yeast Question That Comes Up at Every Backyard Pizza Night"
- "Why Fresh Yeast Isn't Worth Chasing Down for Most Home Cooks"

### Grilled corn and poblano pizza — additional angles
- "Our Late-Summer Pizza We Only Make Once a Season — And Why"
- "Grilled Corn and Poblano — The Pizza That Started as a Fridge Cleanout"
- "Why Charring the Poblano First Changes This Whole Pizza"
- "The August Pizza Our Guests Ask About Before It's Even in Season"
- "Sweet Corn, Charred Poblano, Melted Mozzarella — Our August Go-To"
- "Save This Recipe for the Last Good Corn of the Summer"
- "Our Answer to Whether Frozen Corn Works When Fresh Isn't in Season"
- "The Cheese Pairing That Finally Made This Pizza Click"
- "Why We Char the Poblano on the Grill, Not Under the Broiler"
- "What We Add for Heat When the Poblano Isn't Spicy Enough"
- "Our Prep Shortcut for This Pizza on a Busy Weeknight"
- "The Leftover Corn Trick That Started This Whole Recipe"
- "Why This Pizza Only Shows Up on Our Menu Once a Year"
- "The Farm Stand Trip That Inspired This Whole Recipe"
- "Our Answer to Whether This Pizza Works Without a Grill"
- "What Guests Say the First Time They Try This Combo"
- "The One Ingredient Swap That Would Ruin This Pizza"
- "Why August Corn Makes or Breaks This Recipe"

### Why salt timing matters — additional angles
- "Why We Never Add Salt to Our Dough Right Away — The Timing Matters"
- "The Salt Mistake That Made Our Dough Fight Us All Night"
- "What Actually Happens When You Add Salt Too Early to Pizza Dough"
- "Our Salt-Timing Rule for Every Batch of Cold-Fermented Dough"
- "Save This Before Your Next Mix — The Salt Step Most People Rush"
- "Why Salt Does More to Your Dough Than Just Add Flavor"
- "Our Answer to Whether Fine Salt and Coarse Salt Behave Differently Here"
- "What We Noticed Comparing Dough Salted Early vs. Salted Late"
- "The Salt Amount We Actually Use Per Dough Ball, By Weight"
- "Why We Weigh Our Salt Instead of Measuring by Spoon"
- "Our Rule for Adjusting Salt When We Switch Flour Types"
- "What Happens to Fermentation Speed When Salt Timing Goes Wrong"
- "The Salt Habit We Broke After One Ruined Batch"
- "Why We Time Salt to the Minute During Cold Ferments"
- "What We Tell Beginners Before They Touch the Salt Jar"
- "Our Answer to Whether Sea Salt Changes This Timing at All"
- "The Batch That Convinced Us Salt Timing Isn't Optional"
- "Why This Small Step Fixes More Dough Problems Than People Think"

### Semolina on the peel — additional angles
- "Why We Keep a Small Bowl of Semolina Next to Every Peel"
- "The Peel Test That Proved Semolina Beats Flour, Every Time"
- "Our Answer to How Much Semolina Is Too Much on the Bottom Crust"
- "What Semolina Does That Flour Can't — We Tested Both Side by Side"
- "The Sticking Mistake That Made Us Switch to Semolina for Good"
- "Why We Never Use Semolina on the Stone, Only the Peel"
- "The Bowl of Semolina That Lives Permanently on Our Prep Table"
- "Why We Buy Semolina by the Bag, Not the Small Container"
- "Our Answer to Whether Cornmeal Works as a Semolina Substitute"
- "What Convinced a Skeptical Friend to Switch to Semolina"
- "The One Peel Disaster That Semolina Would Have Prevented"
- "Why Semolina Earned a Permanent Spot in Our Pizza Setup"

### Pecorino vs. Parmigiano — additional angles
- "Pecorino or Parmigiano? Our Rule for Reading the Pie First"
- "The Pizza Where We Skip Both Cheeses Entirely — And Why"
- "Why We Buy Pecorino in Small Amounts and Parmigiano in Bulk"
- "Our Honest Take on Pre-Grated Cheese vs. Fresh Off the Wedge"
- "What Pecorino Does to a Pizza That Parmigiano Never Could"
- "The Cheese Mistake That Muddied Our Best White Pie"
- "The Cheese Debate We Have Every Time We Build a White Pie"
- "Why We Keep Both Wedges in the Fridge at Once"
- "Our Answer to Which Cheese Wins on a Simple Margherita"
- "What We Tell Guests Confused by the Two Cheese Wedges"
- "The Pizza Where Using the Wrong Cheese Cost Us the Bite"
- "Why We Grate Fresh Every Time, No Shortcuts"

### Hot honey on pizza — additional angles
- "The Pizza Where Hot Honey Actually Earns Its Spot"
- "Why We Stopped Drizzling Hot Honey on Everything"
- "Our Rule for How Much Hot Honey Is Too Much"
- "What Hot Honey Ruins When It's Used on the Wrong Pie"
- "The Brand of Hot Honey We Keep Coming Back To"
- "Why Sweet and Heat Together Isn't Always the Right Call"

### Canned vs. fresh clams for white clam pizza — additional angles
- "Canned or Fresh Clams for White Clam Pizza — Our Honest Answer"
- "The Clam Pizza Where Canned Actually Won"
- "Why Fresh Clams Overcook Fast in a 900°F Oven"
- "Our Rule for Judging Good Canned Clams at the Store"
- "What We Learned Testing Both Clams Back to Back"
- "The New England Clam Pizza Mistake We See Most Often"

### Backyard pizza night setup — additional angles
- "The Setup Mistake We Made Our First Season Hosting"
- "Why Four Stations Beat Just Winging It"
- "Our Answer to Setting This Up Solo Without Help"
- "What We'd Change About Our Setup If We Started Over Today"
- "The Station Guests Notice First When They Walk Into the Backyard"
- "Why This Setup Works Just as Well for Four People as for Twelve"

### Pizza oven comparison (best outdoor pizza ovens under $500) — additional angles
- "The Question We Get Asked More Than Any Other About Ovens"
- "Why We Don't Regret Owning Two Different Ovens"
- "Our Answer to Whether Cheaper Ovens Are Actually Worth It"
- "What We'd Tell Someone Buying Their Very First Pizza Oven"
- "The Oven Feature We Didn't Know to Ask About Until We Owned One"
- "Why Price Isn't the First Thing We Check Anymore"

### Ninja Woodfire accessories worth buying — additional angles
- "The Accessory Question We Still Get a Year After Our First Post"
- "Why Our List Changed After a Full Year of Cooks"
- "Our Answer to Whether Off-Brand Accessories Are Worth the Savings"
- "What We'd Tell Someone Who Just Unboxed Their Ninja Woodfire"
- "The Accessory We Didn't Trust Until We Tried It Ourselves"
- "Why We Keep Revisiting This List Every Few Months"

### Q4 gift-guide / holiday buying angles — cross-post batch (generated 2026-07-29)
- "The Best Outdoor Pizza Ovens Under $500 — Our Holiday Buying Guide" (best-outdoor-pizza-ovens-under-500)
- "Ninja Woodfire vs. Ooni — Which One to Buy Before the Holidays" (best-outdoor-pizza-ovens-under-500)
- "Ooni vs. Solo Stove Pi — Our Honest Take Before You Buy One as a Gift" (best-outdoor-pizza-ovens-under-500)
- "Save This Before You Buy Anyone a Pizza Oven This Holiday Season" (best-outdoor-pizza-ovens-under-500)
- "Best Pizza Accessories Under $50 — Our Stocking Stuffer Picks" (best-pizza-accessories-under-50)
- "One Peel or Two — What We'd Tell Someone Buying Their First Oven This Winter" (2026-06-01-two-peels-vs-one-is-a-turning-peel-worth-owning)
- "The Turning Peel Question Every Holiday Shopper Asks Us" (2026-06-01-two-peels-vs-one-is-a-turning-peel-worth-owning)
- "Best Pizza Oven Deals This Black Friday — What We're Actually Watching" (best-pizza-oven-deals)
- "Pin This Before Black Friday — Our Pizza Gear Watch List" (best-pizza-oven-deals)
- "What We'd Actually Put on a Pizza Person's Holiday Wish List" (ninja-woodfire-accessories-worth-buying)
- "Before You Buy the Cover as a Gift — What We Wish We'd Known First" (ninja-woodfire-accessories-worth-buying)
- "Hosting Pizza Night Indoors This Winter — Our Honest Setup Notes" (backyard-pizza-night-setup)

### Q4 gift-guide / holiday buying angles — cross-post batch 2 (generated 2026-08-12)
- "Ooni Koda 12 vs. Ninja Woodfire — Save This Before You Buy Someone a Pizza Oven" (best-outdoor-pizza-ovens-under-500)
- "Ninja Woodfire vs. Solo Stove Pi — The Match-Up We Haven't Covered Yet" (best-outdoor-pizza-ovens-under-500)
- "Ooni, Ninja, or Solo Stove — Our Answer Before You Buy Someone's First Oven" (best-outdoor-pizza-ovens-under-500)
- "Save This: Our Under-$500 Oven Picks for Holiday Shopping" (best-outdoor-pizza-ovens-under-500)
- "Save This: Our Under-$50 Gift Picks for Anyone Who Cooks Outside All Winter" (best-pizza-accessories-under-50)
- "Our Under-$25 Stocking Stuffers for Pizza People — Worth Saving Before You Shop" (best-pizza-accessories-under-50)
- "Peel Bundle or Single Peel — What We'd Wrap Up as a Gift" (2026-06-01-two-peels-vs-one-is-a-turning-peel-worth-owning)
- "The Ninja Woodfire Accessory We'd Never Give as a Gift (And What We'd Give Instead)" (ninja-woodfire-accessories-worth-buying)
- "Our Under-$60 Ninja Woodfire Gift Bundle — Pin This Before Gift Season" (ninja-woodfire-accessories-worth-buying)
- "Before You Buy Anyone an Infrared Thermometer, Read This" (2026-06-16-reading-your-stone-with-an-infrared-thermometer)
- "Cyber Monday or Christmas Eve — When Pizza Oven Prices Actually Bottom Out" (best-pizza-oven-deals)
- "Hosting Pizza Night for the Holidays — What We're Making Instead of Margherita" (pizza-night-recipes-beyond-margherita)

---

## NOTES & CONSTRAINTS

- All iPhone photos: 270° rotation is baked into the generator — don't pre-rotate
- Headline: ~20 characters per line for clean 4-line wrapping
- Descriptor: ~44 characters per line, 3 lines max
- Output filenames: NEC-[postname]-pin[#].png — increment the number for each new pin
- Target cadence: 2 new pins per week generated, posted 1-2 per day
- Analytics: check monthly — top performers get 2-3 more variation pins
- Skip Pinterest pins for "Welcome to New England Crust" (intro/about post) — intro posts don't drive Pinterest traffic and an underperforming pin can drag down account distribution. Revisit only if a dedicated "Story"/"About" category gets added later.