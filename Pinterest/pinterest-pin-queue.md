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

### [x] Dough Starts Here — Recipe (Pin 3)
- **photo:** IMG_8372.jpeg
- **category:** Recipe
- **headline:** Our Dough Starts Here — Caputo 00, Lievito Yeast, La Baleine Salt
- **descriptor:** The exact three on our prep counter every cook — and why we've never swapped any of them out.
- **output:** NEC-00flour-pin3.png
- **board:** Backyard Pizza Night
- **link:** https://newenglandcrust.com/blog/2026-06-15-the-difference-between-00-flour-and-bread-flour-wh/

---

### [x] The 4 Accessories Before First Cook — Gear Guide (Pin 7)
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

### Fresh basil vs. dried — additional angles
- "Fresh or Dried Basil for a 90-Second Pizza Cook — Our Honest Answer"
- "Why Fresh Basil Burns Before Your Pizza Even Finishes Cooking"
- "The Dried Basil Trick We Use When Fresh Isn't Worth Buying"
- "When We Skip Fresh Basil Entirely — And Nobody Notices"
- "Our Rule for Adding Basil Before or After the Oven, Never During"
- "What a 900°F Oven Does to Fresh Basil in Under a Minute"
- "Save This Before You Buy Fresh Basil for Your Next Pizza Night"

### What yeast to buy — additional angles
- "Instant, Active Dry, or Fresh Yeast — What We Actually Use for Pizza"
- "The Yeast Mistake That Kept Our Dough From Rising Right"
- "Why We Switched to Instant Yeast After Years of Active Dry"
- "Fresh Yeast Is Worth It Once — Here's Why We Went Back to Instant"
- "Our Honest Answer to the Yeast Question We Get Every Pizza Night"
- "The Yeast Swap That Changed Our 72-Hour Cold Ferment for the Better"
- "Save This Before You Buy Yeast for Your Next Batch of Dough"

### Grilled corn and poblano pizza — additional angles
- "Our Late-Summer Pizza We Only Make Once a Season — And Why"
- "Grilled Corn and Poblano — The Pizza That Started as a Fridge Cleanout"
- "Why Charring the Poblano First Changes This Whole Pizza"
- "The August Pizza Our Guests Ask About Before It's Even in Season"
- "Sweet Corn, Charred Poblano, Melted Mozzarella — Our August Go-To"
- "Save This Recipe for the Last Good Corn of the Summer"

### Why salt timing matters — additional angles
- "Why We Never Add Salt to Our Dough Right Away — The Timing Matters"
- "The Salt Mistake That Made Our Dough Fight Us All Night"
- "What Actually Happens When You Add Salt Too Early to Pizza Dough"
- "Our Salt-Timing Rule for Every Batch of Cold-Fermented Dough"
- "Save This Before Your Next Mix — The Salt Step Most People Rush"
- "Why Salt Does More to Your Dough Than Just Add Flavor"

---

## NOTES & CONSTRAINTS

- All iPhone photos: 270° rotation is baked into the generator — don't pre-rotate
- Headline: ~20 characters per line for clean 4-line wrapping
- Descriptor: ~44 characters per line, 3 lines max
- Output filenames: NEC-[postname]-pin[#].png — increment the number for each new pin
- Target cadence: 2 new pins per week generated, posted 1-2 per day
- Analytics: check monthly — top performers get 2-3 more variation pins
- Skip Pinterest pins for "Welcome to New England Crust" (intro/about post) — intro posts don't drive Pinterest traffic and an underperforming pin can drag down account distribution. Revisit only if a dedicated "Story"/"About" category gets added later.
