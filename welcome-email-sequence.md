# New England Crust — Welcome Email Sequence
## ConvertKit Setup Guide + 3-Email Copy

This document contains everything needed to configure the welcome automation in ConvertKit
and the copy for all three emails. Paste each email into ConvertKit exactly as written.
Personalization tags use ConvertKit's standard format.

---

## CONVERTKIT SETUP INSTRUCTIONS

### Step 1: Create the Sequence

1. Log into ConvertKit → click **Automations** in the left sidebar
2. Click **Create Sequence**
3. Name it: `New England Crust — Welcome Sequence`
4. Add three emails with the following send delays:
   - Email 1: Send **immediately** on signup
   - Email 2: Send **3 days** after signup
   - Email 3: Send **7 days** after signup

### Step 2: Create the Automation

1. Go to **Automations → Create Automation**
2. Set the trigger: **"Subscribes to a form"** → select your lead magnet opt-in form
3. Add action: **"Subscribe to sequence"** → select `New England Crust — Welcome Sequence`
4. Activate the automation

### Step 3: Opt-In Form Settings

- Form name: `Ninja Woodfire Quick-Start — Inline`
- Success message: *"Check your inbox — your guide is on its way."*
- Redirect after subscribe: leave as default (show success message inline)
- Double opt-in: **OFF** for now (reduces friction while building your first 500 subscribers;
  re-evaluate when you have traffic worth protecting)

---

## EMAIL 1 — DELIVER THE GUIDE
**Send: Immediately on signup**

---

**Subject line:** Your Ninja Woodfire Quick-Start Guide is here

**Preview text:** Four accessories, two pellet bags, and the stone temp trick.

---

Hey {{ subscriber.first_name | default: "there" }},

Your guide is attached — four pages covering the accessories worth buying first,
the pellet bags to keep stocked, and the stone temperature numbers that
actually produce a good crust.

The one thing I'd flag before you open it:

The infrared thermometer tip in Section 3 changed our results more than anything
else we've done. The oven display and the stone surface run differently —
sometimes by 100°F or more — and that gap is usually the difference between
a pale, underwhelming crust and one that puffs the way it's supposed to.
Worth reading that section twice.

**→ [Download Your Quick-Start Guide]**
*(button links to hosted PDF — upload to your ConvertKit file hosting
or Cloudflare Pages public folder and paste the direct URL here)*

Welcome to the list. We send one email a week — recipes, gear notes,
and whatever we've been cooking on the patio lately.

— Michael
New England Crust

---
*You're receiving this because you signed up at newenglandcrust.com.
[Unsubscribe] · [Manage preferences]*

---

**CONVERTKIT FORMATTING NOTES FOR EMAIL 1:**
- Button: label "Download Your Quick-Start Guide" — link to hosted PDF URL
- Send as plain-text style (no heavy HTML template) — feels more personal
- From name: Michael | New England Crust
- From email: hello@newenglandcrust.com (or your actual domain email)

---

## EMAIL 2 — BEST CONTENT
**Send: 3 days after signup**

---

**Subject line:** The one post to read before your next pizza night

**Preview text:** We learned this the slow way so you don't have to.

---

Hey {{ subscriber.first_name | default: "there" }},

Three days in — hoping you've had a chance to fire up the Woodfire at least once.

If you're still waiting on that cover or extension cord: you can start without them,
but the extension cord is genuinely the first thing to get. The 4.5-foot stock cord
catches almost everyone off guard.

The post I'd point you to right now:

**[Ninja Woodfire Accessories Worth Buying (And What's a Waste)]**
*(link to: newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying)*

It covers the full accessories picture — not just the essentials from the guide,
but the stuff that sounds good in marketing and underdelivers in real life.
The pellet scoop section alone has saved more than a few people from wasting $8.

If you've already read it: the cast iron tray note in the middle is the one
most people skip on a first read and then come back to later.

More soon.

— Michael
New England Crust · newenglandcrust.com

---
*[Unsubscribe] · [Manage preferences]*

---

**CONVERTKIT FORMATTING NOTES FOR EMAIL 2:**
- Keep this email short — one post, one link, one observation
- The linked post is: /blog/ninja-woodfire-accessories-worth-buying
- Do not include multiple post links — single focus outperforms roundups at this stage
- From name: Michael | New England Crust

---

## EMAIL 3 — THE PERSONAL EMAIL
**Send: 7 days after signup**

---

**Subject line:** The first pizza we made on the Woodfire

**Preview text:** It was not the pizza we expected.

---

Hey {{ subscriber.first_name | default: "there" }},

I want to tell you about the first pizza we made on the Ninja Woodfire.

We'd done the research. Read the forums. Watched the YouTube videos where
everything goes perfectly. Preheated the stone for 25 minutes, stretched a
decent dough ball, loaded it up with sauce and fresh mozzarella,
launched it onto the stone with a wooden cutting board because we didn't
have a peel yet.

The pizza cooked in about two minutes. Which sounds great until you realize
we weren't watching it closely enough and the front edge was overdone
while the back was perfect.

That was the night we learned the Woodfire runs hotter in the back.
You rotate at 45 seconds. Every cook. Without exception.

By pizza three we had it. By pizza six we were making the best pizza
we'd ever had at home — better, honestly, than most of what we order.

The learning curve on this oven is real but it's short. A few cooks and
the rhythm clicks. If you're in those first few cooks right now:
you're closer to good pizza than it probably feels.

A few things that helped us get there faster:

**The accessories post** (if you haven't read it yet):
newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying

**The dough we use** — a 72-hour cold ferment that we've been making
every weekend for two summers. Recipe coming to the site next month,
but the short version: 00 flour, 65% hydration, 72 hours in the fridge,
and an hour out to warm before you ball it. That's the whole formula.

Reply to this email if you have questions — I read every one.

— Michael
New England Crust · newenglandcrust.com

---
*[Unsubscribe] · [Manage preferences]*

---

**CONVERTKIT FORMATTING NOTES FOR EMAIL 3:**
- This is the most important email in the sequence — the one that makes people
  feel like they're hearing from a real person, not a content site
- Do NOT add multiple CTAs or product links — this email's job is relationship, not conversion
- Plain text only — no buttons, no images
- The reply invitation is intentional — even if 2-3 people reply, that's signal for
  future content topics and those replies count toward email deliverability reputation
- From name: Michael | New England Crust
- Subject line A/B test option: "What we got wrong on pizza night #1"

---

## ONGOING EMAIL RHYTHM (After the Sequence)

Once subscribers exit the welcome sequence on day 7, they should move to your
broadcast list for weekly sends. Target one email per week, roughly 200–350 words.

**Suggested format:**
- One thing we cooked lately (2–3 sentences with a photo if available)
- One post worth reading (link to your most recent publish)
- One quick tip or observation

**ConvertKit setup:**
- Tag subscribers as `welcome-complete` when the sequence finishes
  (add a tag action at the end of your automation)
- Send weekly broadcasts to all subscribers tagged `welcome-complete`
- Keep the from name and email identical to the sequence for recognition

---

## LEAD MAGNET HOSTING

The PDF from `generate_lead_magnet.py` needs to be publicly accessible.
Two easy options:

**Option A — Cloudflare Pages public folder:**
Add `ninja-woodfire-quickstart.pdf` to `/public/downloads/` in your
new-england-crust repo. After Cowork pushes to GitHub, it deploys to:
`https://newenglandcrust.com/downloads/ninja-woodfire-quickstart.pdf`
Use this URL as the button link in Email 1.

**Option B — ConvertKit file hosting:**
In ConvertKit → click your account name → Files → Upload.
ConvertKit generates a CDN URL you can use directly in the email button.

Option A is preferred — it keeps the asset on your domain, which is better
for brand trust and means you can update the file without changing the link.
