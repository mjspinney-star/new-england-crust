# New England Crust — Project Context

> This file gives Claude persistent context for all Cowork sessions on this project.
> Update it as the site evolves — decisions made, content published, programs joined.

---

## Project Overview

**New England Crust** is a pizza-focused blog and content site built to grow an audience first, then monetize through affiliate marketing. The site is built with **Astro** and hosted on **Cloudflare**. The local project folder is `new-england-crust` on the desktop.

**Current status:** Active content and monetization phase. Amazon Associates links are live in published content. Impact.com account created and verification tag is live — awaiting brand approvals for Ooni, Ninja, and Solo Stove Pi.

---

## Tech Stack

- **Framework:** Astro (static site generator)
- **Hosting:** Cloudflare Pages
- **Local dev:** Localhost
- **Content format:** Markdown (.md) with Astro frontmatter
- **Blog content folder:** `src/content/blog/`
- **Analytics:** Google Analytics 4 — Measurement ID `G-3QBKJCC5F9` — tag live in `src/layouts/BaseLayout.astro`
- **Search Console:** Set up June 2026 — sitemap submitted at `newenglandcrust.com/sitemap.xml`

All blog posts are `.md` files and need proper Astro frontmatter (title, description, date, etc.) to integrate correctly.

---

## Brand Voice

- First-person, personal, and authentic — written like a real pizza enthusiast, not a content farm
- Conversational but knowledgeable; the reader should feel like they're getting advice from a friend who really knows pizza
- New England roots inform the perspective — regional pride without being exclusionary
- No filler, no fluff; every sentence earns its place
- Opinions are expressed clearly ("my pick is…", "I personally enjoy…")

---

## Affiliate Strategy

**Dual-track approach:**

### Track 1 — Pizza Ovens (Via Impact.com — Awaiting Brand Approval)
Impact.com affiliate network account is created and the verification tag is live in `src/layouts/Layout.astro`. Awaiting brand approval from pizza oven partners. Do NOT add these affiliate links until brand approvals are confirmed.

| Brand | Network | Est. Commission | Cookie | Status |
|---|---|---|---|---|
| Ooni | Impact.com | 5–8% | ~30 days | Awaiting approval |
| Ninja | Impact.com | 3–8% | ~30 days | Awaiting approval |
| Solo Stove Pi (Gas) | Impact.com | 8–10% | ~30 days | Awaiting approval |

### Track 2 — Everything Else (Amazon Associates — LIVE)
Amazon affiliate links are active and already live in published content. All non-oven product recommendations (ingredients, tools, accessories, cookware, etc.) use Amazon Associates links.

**Content strategy:**
- Comparison articles (Ooni vs. Ninja vs. Solo Stove Pi) are the primary high-value affiliate driver
- Amazon links support all supporting content — dough tools, peels, flour, accessories, etc.
- Seasonal content pushes (summer grilling, holiday gifting)
- First-person reviews with honest pros/cons build trust before the ask

**Important rule:** Amazon links are live and can be included in content. Impact.com brand programs are NOT yet approved — do not add those affiliate links until explicitly instructed.

---

## Content Published / In Progress

### Live Blog Posts
- `best-outdoor-pizza-ovens-under-500.md` — Reviews multiple ovens; three picks: Ooni and Ninja as top picks, Solo Stove Pi as "Also Worth Considering." Heading reads "My Picks."
- Two Peels vs One
- Ninja Woodfire Accessories Worth Buying
- 9 Pizza Night Recipes That Aren't Margherita
- Backyard Pizza Night Setup
- Storing Pellets Through a Humid NE Summer
- Our 72-Hour Cold Fermented Dough (blog post version)

### Live Recipes
- Our 72-Hour Cold Fermented Dough
- Caputo 00 (dough/flour focused)
- Chicken Bacon Ranch
- Pesto, Fresh Mozzarella & Basil
- Clam Pie
- Roasted Heirloom and NH Mushroom

### Publishing Schedule
A GitHub + Claude API (Console subscription) automation is set up to publish new posts automatically every **Monday and Thursday**. This pipeline is active — account for it when planning content so the queue stays filled.

---

## Workflow Notes

- Files are authored here locally and dropped into `src/content/blog/` manually
- Cowork is the preferred tool for file creation, editing, and folder management
- Claude.ai chat is used for drafting, strategy, and research
- Google Drive is used as backup storage only — HTML files do not render there, and DOCX conversions have been unreliable. Direct download → manual upload is the most reliable workflow.

---

## What to Remember Each Session

1. **Amazon Associates links are live** — include them in content for non-oven products
2. **Impact.com account is live** — verification tag in Layout.astro; awaiting brand approvals for Ooni, Ninja, Solo Stove Pi — do NOT add those links until instructed
3. Voice is **first-person and personal** — avoid generic blog tone
4. The three oven brands are the high-value monetization focus; Amazon covers everything else
5. Astro frontmatter is required on all `.md` posts
6. Update this file when major decisions are made or content is published
