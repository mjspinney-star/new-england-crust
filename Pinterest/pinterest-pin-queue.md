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
- **output:** NEC-postname-pin#.png  ← e.g. NEC-accessories-pin7.png
- **board:** Pinterest Board Name  ← exact board name on your Pinterest profile
- **link:** https://newenglandcrust.com/blog/your-post-slug/
```

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

## IDEAS BANK — Not Yet Scheduled

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

### Two Peels vs. One — additional angles
- "Do We Actually Need a Second Pizza Peel? Here's Our Answer"
- "One Peel Got Us Started — Here's When We Added a Second"
- "Turning Peel: Worth $30–$60? Our Honest Take"
- "The Pizza Peel Mistake We Made So You Don't Have To"
- "Metal vs. Wood Turning Peels — Why We Switched"
- "Our Rule: Buy One Peel First, Add a Second Later"
- "What a Turning Peel Actually Changed in Our Cooks"

### Cold-weather preheating — additional angles
- "Our Cold-Weather Pizza Oven Rule: Add 15–20 Minutes"
- "Why Our Propane Tank Comes Inside Before a Cold Cook"
- "Wind or Cold — Which Hurts Our Pizza Oven More?"
- "The Mistake That Burns Our First Pizza Every Cold Cook"
- "How We Keep Cooking Pizza Through a New England October"
- "Our Honest Take on Cold-Weather Wood Pellet Ovens"
- "Our Cold-Weather Pizza Checklist — Save This for Later"

### Dough readiness post — additional angles
- "The Poke Test We Use Every Time Before Opening Dough"
- "Our Dough Wasn't Ready — Here's What We Were Missing"
- "Cold Dough Needs 90 Minutes. Here's Why We Wait."
- "The Sign Our Dough Is Ready (And the One That Fooled Us)"
- "Gluten Relaxation, Explained the Way We Wish We'd Heard It"
- "Our Beginner Dough Mistake — and How We Fixed It"
- "Save This: How We Know Our Dough Is Ready to Stretch"

### Accessories under $50 — additional angles
- "10 Pizza Accessories Under $50 We Actually Use on Our Patio"
- "The $15 Scale That Fixed Our Dough Once and For All"
- "Our 5 Pizza Night Essentials, All Under $75 Combined"
- "What's in Our Pizza Toolkit — Nothing Over $50"
- "Our Honest Picks: Pizza Gear Under $50 That Earned a Spot"
- "Our Pizza Gear Picks — Save This Before You Buy"
- "The Pizza Tools We'd Buy Again for Under $50"

### 9 pizza night recipes — additional angles
- "9 Pizza Topping Combos We Keep Coming Back To"
- "Hot Honey Pepperoni — Our Pizza That Converts Skeptics"
- "The Korean BBQ Pizza Our Guests Talk About for Days"
- "Our Go-To Breakfast Pizza for the Morning After Pizza Night"
- "Beyond Margherita — 9 Pizzas We Actually Make on Repeat"
- "Our Fall Favorite: Apple, Gorgonzola, and Walnut Pizza"
- "Save These 9 Pizza Combos — Our Go-Tos for Pizza Night"

### Pellet storage — additional angles
- "How We Keep Our Pellets Dry Through a Humid NE Summer"
- "The $5 Trick That Saves Our Pellets All Summer"
- "Our Pellet Storage Setup: One Bucket, One Blend, One Label"
- "Signs Our Pellets Have Gone Bad (And What We Do Next)"
- "Oak, Maple, or Cherry — How We Choose Our Pellets"
- "Save This Before Your Pellets Get Damp — Our Setup Inside"
- "Our Rule: Pellets Out of the Bag the Day They Arrive"

### Welcome / intro post — additional angles
- "Why We Run Two Pizza Ovens at Every Backyard Pizza Night"
- "Our Friday Night Ritual: Two Ovens, One Backyard"
- "Ooni for Showpieces, Ninja for Everything Else — Our Setup"
- "What We're Building at New England Crust (And Why)"
- "Our Pizza Philosophy: The Dough Is the Project, the Fire Is the Season"
- "Why We Cook Pizza on a Deck in New England, Not Naples"
- "Our Backyard Pizza Story — Come Pull Up a Chair"

### 72-hour cold-ferment dough — additional angles
- "Our 72-Hour Dough Recipe — The One We Always Come Back To"
- "Our Dough Survives a Humid July and a Cold Ninja Stone"
- "66% Hydration, 3 Days — Our Go-To Pizza Dough Numbers"
- "One Dough, Two Ovens — How We Adjust for Ooni vs. Ninja"
- "Why We Cold-Ferment Our Pizza Dough for 72 Hours"
- "Our Pizza Dough Recipe Worth Sleeping On (Literally)"
- "Our Shortcut for Mixing Six Dough Balls at Once"

---

## NOTES & CONSTRAINTS

- All iPhone photos: 270° rotation is baked into the generator — don't pre-rotate
- Headline: ~20 characters per line for clean 4-line wrapping
- Descriptor: ~44 characters per line, 3 lines max
- Output filenames: NEC-[postname]-pin[#].png — increment the number for each new pin
- Target cadence: 2 new pins per week generated, posted 1-2 per day
- Analytics: check monthly — top performers get 2-3 more variation pins
