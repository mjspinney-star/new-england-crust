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
6. Commit changes: `git add -A && git commit -m "Generated Pinterest pins"`

If there are no `[ ]` items, do nothing and note the queue is empty.

---

## PIN QUEUE

---

### [ ] Dough Starts Here — Recipe (Pin 3)
- **photo:** IMG_8372.jpeg
- **category:** Recipe
- **headline:** Our Dough Starts Here — Caputo 00, Lievito Yeast, La Baleine Salt
- **descriptor:** The exact three on our prep counter every cook — and why we've never swapped any of them out.
- **output:** NEC-00flour-pin3.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/blog/2026-06-15-the-difference-between-00-flour-and-bread-flour-wh/

---

### [ ] The 4 Accessories Before First Cook — Gear Guide (Pin 7)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Gear Guide
- **headline:** The 4 Ninja Woodfire Accessories You Need Before Your First Cook
- **descriptor:** Cover, cord, peel, thermometer — the four we'd grab before your first cook. Under $80 total.
- **output:** NEC-accessories-pin7.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying/

---

### [ ] Three Ingredients We Stock — Recipe (Pin 1)
- **photo:** IMG_8372.jpeg
- **category:** Recipe
- **headline:** The Three Ingredients We Always Have On Hand
- **descriptor:** Three ingredients, same every time — Caputo 00 is the foundation. Here's why we never switch.
- **output:** NEC-00flour-pin1.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/blog/2026-06-15-the-difference-between-00-flour-and-bread-flour-wh/

---

### [ ] Why We Use Caputo 00 Flour — Tips (Pin 2)
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

### [x] Prime Day Pizza Oven Deals 2026 (Pin 1)
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Oven Review
- **headline:** Prime Day Pizza Oven Deals — What's Worth Watching
- **descriptor:** Ooni, Ninja Woodfire, Solo Stove Pi — what to buy, what to skip, and when to check back.
- **layout:** primeday
- **badge_position:** top_right
- **output:** NEC-primeday-pin1.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/prime-day-pizza-oven-deals-2026/

---

### [x] Prime Day Accessories 2026 (Pin 1)
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

### [x] Pizza Ovens Under $500 — Variation Pin 2
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Oven Review
- **headline:** Our Pizza Oven Buying Guide — Save This Before You Shop
- **descriptor:** Five ovens under $500 tested honestly — here's how we'd rank them and the one spec that matters most.
- **layout:** fullbleed
- **badge_position:** top_right
- **output:** NEC-ovens-pin2.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/best-outdoor-pizza-ovens-under-500/

---

### [x] Pizza Ovens Under $500 — Variation Pin 3
- **photo:** NinjaWoodfireHero.jpeg
- **category:** Oven Review
- **headline:** Propane vs Pellets vs Electric — Which Outdoor Pizza Oven Is Actually Worth It
- **descriptor:** We tested all three fuel types. Here's the honest answer before you spend $300–$500.
- **layout:** split
- **badge_position:** top_right
- **output:** NEC-ovens-pin3.png
- **board:** Ninja Woodfire Oven
- **link:** https://newenglandcrust.com/blog/best-outdoor-pizza-ovens-under-500/

---

### [x] Infrared Thermometer — Accessory Pin Rework
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

### 00 flour vs. bread flour — additional angles
- "00 Flour vs. Bread Flour — What We Actually Use and Why"
- "Why We Switched to Caputo 00 for High-Heat Pizza Cooks"
- "The Flour Question We Get Every Pizza Night: What Do You Use?"
- "Bread Flour or 00 for Your Pizza Oven? Here's Our Honest Answer"
- "Why Flour Protein Percentage Actually Matters for Pizza Dough"
- "Our Rule: 00 Flour for the Ooni, Bread Flour for the Ninja"
- "The Flour Swap We Made After Our First Cold-Ferment Batch"

### Hand stretching vs. rolling pin — additional angles
- "Why We Banned the Rolling Pin From Our Pizza Setup"
- "What a Rolling Pin Does to Your Dough Bubbles (It's Not Good)"
- "The Hand-Stretch Move That Finally Clicked After Months of Tearing Dough"
- "What We Tell Every Guest Before They Touch Our Dough Table"
- "Why We Still Tear Dough Sometimes — And Why That's Fine"
- "The One Pizza Technique That Changed Our Crust More Than Any Oven Setting"
- "Our Gravity-and-Knuckle Method — The Stretch We Use Every Cook"

### Infrared thermometer / reading the stone — additional angles
- "Why We Never Launch a Pizza Without an Infrared Reading First"
- "The 100°F Gap Between Your Oven Display and Your Stone — It Matters"
- "Why the Ninja Woodfire Display Doesn't Tell You What You Think It Does"
- "Stone Temp vs. Air Temp: The Number We Check Before Every Cook"
- "Our Pre-Launch Checklist — One Tool, One Number, No More Pale Bottoms"
- "How We Know the Stone Is Ready Before We Commit the Dough"
- "The $20 Thermometer Fix That Changed Our Stone-Reading Routine"

### Prime Day pizza oven deals 2026 — additional angles
- "Our Prime Day Watch List for Pizza Gear — June 23–26"
- "The Ovens Worth Tracking on Prime Day (And What to Skip)"
- "How We're Approaching Prime Day 2026 for Our Pizza Setup"
- "Why We're Watching the Ooni Koda 12 During Amazon Prime Day"
- "Prime Day Pizza Accessories — The Under-$50 Picks Worth Tracking"
- "Our Prime Day Strategy: One Oven, A Few Accessories, One Hard Budget"
- "The Price Drop We Need to See Before We Pull the Trigger on Prime Day"

---

## NOTES & CONSTRAINTS

- All iPhone photos: 270° rotation is baked into the generator — don't pre-rotate
- Headline: ~20 characters per line for clean 4-line wrapping
- Descriptor: ~44 characters per line, 3 lines max
- Output filenames: NEC-[postname]-pin[#].png — increment the number for each new pin
- Target cadence: 2 new pins per week generated, posted 1-2 per day
- Analytics: check monthly — top performers get 2-3 more variation pins
- Skip Pinterest pins for "Welcome to New England Crust" (intro/about post) — intro posts don't drive Pinterest traffic and an underperforming pin can drag down account distribution. Revisit only if a dedicated "Story"/"About" category gets added later.
