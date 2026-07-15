# New England Crust — Project Context

> This file gives Claude persistent context for all Cowork sessions on this project.
> Update it as the site evolves — decisions made, content published, programs joined.

---

## Project Overview

**New England Crust** is a pizza-focused blog and content site built to grow an audience first, then monetize through affiliate marketing. The site is built with **Astro** and hosted on **Cloudflare**. The local project folder is `new-england-crust` on the desktop.

**Current status:** Active content and monetization phase. Amazon Associates links live across all content including ovens. Impact/Avantlink brand approvals pending.

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

### Track 1 — Pizza Ovens (Amazon interim → Impact/Avantlink when approved)
Amazon Associates links (tag newenglandcru-20) are the interim solution for pizza ovens. Ooni Koda 12, Solo Stove Pi, and Ninja Woodfire oven links are live via Amazon as of July 2026. If an oven has no Amazon listing (e.g., Ooni Fyra), leave it unlinked and ask Michael before adding any link.

When brand approvals come through, swap oven links to the direct programs — they pay higher commission on the same sale. Never remove a working amzn.to link without a replacement ready.

| Brand | Network | Est. Commission | Status |
|---|---|---|---|
| Ooni | Avantlink | 5–8% | Applied, awaiting approval |
| SharkNinja | Impact.com | 3–8% | Reapplying mid-August 2026 |
| Solo Stove | Impact.com | 8–10% | Applied, awaiting approval |

### Track 2 — Everything Else (Amazon Associates — LIVE)
Amazon affiliate links are active and already live in published content. All non-oven product recommendations (ingredients, tools, accessories, cookware, etc.) use Amazon Associates links.

**Content strategy:**
- Comparison articles (Ooni vs. Ninja vs. Solo Stove Pi) are the primary high-value affiliate driver
- Amazon links support all supporting content — dough tools, peels, flour, accessories, etc.
- Seasonal content pushes (summer grilling, holiday gifting)
- First-person reviews with honest pros/cons build trust before the ask

**Important rule:** Amazon links are live for all products, ovens included. Impact/Avantlink brand programs are NOT yet approved — never add links from those networks until explicitly instructed. When they approve, oven links get swapped from Amazon to the direct program.

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

1. Amazon Associates links are live for everything — ovens and non-oven products alike (tag newenglandcru-20)
2. Impact/Avantlink approvals pending (SharkNinja reapplication mid-August 2026) — do NOT add those links until instructed; when approved, swap oven links from Amazon to direct programs
3. Voice is **first-person and personal** — avoid generic blog tone
4. The three oven brands are the high-value monetization focus; Amazon covers everything else
5. Astro frontmatter is required on all `.md` posts
6. Update this file when major decisions are made or content is published
