# New England Crust — SEO / Affiliate / Content Audit (Task A)

**Date:** 2026-07-28 · **Branch:** `fable5-seo-audit` · **Baseline:** `npm run build` passes, 39 pages built.

This is a read-only inventory. Nothing has been changed yet. Items marked **[B]–[F]** map to the task letters in the work plan; **[?]** means I need your call before acting.

---

## 1. Content inventory

### 1.1 Blog posts (24 — all published, none draft)

Word counts are rendered body text (frontmatter, code, and component markup stripped). No post has an `updatedDate`. No blog post has a `heroImage` (see §6.4). "Kw guess" = the query I believe the post targets, inferred from title/headings.

| Slug | Title | Meta desc (chars) | Pub | Words | Kw guess |
|---|---|---|---|---|---|
| `welcome-to-new-england-crust` | Welcome to New England Crust | 106 | 03-05 | 353 | (brand/none) |
| `72-hour-cold-ferment-dough` | Our 72-hour cold-ferment dough | 132 | 03-11 | 463 | 72 hour cold ferment pizza dough |
| `storing-pellets-new-england-summer` | Storing pellets through a humid New England summer | 99 | 03-19 | 385 | storing wood pellets humidity |
| `best-outdoor-pizza-ovens-under-500` | The Best Outdoor Pizza Ovens Under $500: Honest Comparison | 129 | 04-02 | 2,823 | best outdoor pizza oven under $500 |
| `backyard-pizza-night-setup` | Backyard Pizza Night Setup — Everything You Need | 115 | 04-16 | 2,070 | backyard pizza night / pizza party setup |
| `pizza-night-recipes-beyond-margherita` | 9 Pizza Night Recipes That Aren't Just Margherita | 133 | 04-25 | 1,827 | pizza topping ideas |
| `ninja-woodfire-accessories-worth-buying` | Ninja Woodfire Accessories Worth Buying (And What's a Waste) | 162 ⚠ | 05-24 | 1,651 | ninja woodfire accessories |
| `best-pizza-accessories-under-50` | The Best Pizza & Outdoor Cooking Accessories Under $50 | 141 | 06-09 | 1,218 | pizza accessories under $50 |
| `prime-day-pizza-oven-deals-2026` | Prime Day Pizza Oven Deals 2026 — What's Worth Watching | 173 ⚠ | 06-16 | 867 | prime day pizza oven deals |
| `2026-06-01-two-peels-vs-one…` | Two Peels vs. One — Is a Turning Peel Worth Owning? | 121 | 06-01 | 491 ⚠ | turning peel worth it |
| `2026-06-05-preheating…` | Cold-Weather Pizza Oven Preheating: What Actually Changes | 110 | 06-05 | 523 | pizza oven cold weather preheat |
| `2026-06-08-…dough-ready` | How to Tell When Your Dough Is Actually Ready to Open | 108 | 06-08 | 542 | when is pizza dough ready |
| `2026-06-11-shaping…` | Why Hand-Stretching Pizza Dough Beats Using a Rolling Pin | 112 | 06-11 | 506 | hand stretch vs rolling pin |
| `2026-06-15-…00-flour` | 00 Flour vs. Bread Flour for Pizza: The Baker's Guide | 118 | 06-15 | 551 | 00 flour vs bread flour pizza |
| `2026-06-16-reading-your-stone…` | How to Read Your Pizza Stone with an Infrared Thermometer | 132 | 06-16 | 777 ⚠ | pizza stone infrared thermometer |
| `2026-06-22-…olive-oil` | Finishing with Good Olive Oil: When It Matters and When It Does Not | 105 | 06-22 | 602 | finishing olive oil pizza |
| `2026-06-25-fresh-basil…` | Fresh Basil vs. Dried: The Honest Answer for Outdoor Pizza Cooking | 101 | 06-25 | 504 | fresh vs dried basil pizza |
| `2026-06-29-…yeast` | What Yeast to Buy for Pizza Dough: Instant, Active Dry, or Fresh | 108 | 06-29 | 568 | best yeast for pizza dough |
| `2026-07-02-grilled-corn…` | Grilled Corn and Poblano Pizza: A Late-Summer Backyard Pie… | 116 | 07-02 | 546 | grilled corn poblano pizza |
| `2026-07-06-…salt-timing` | Why Salt Timing Matters in Pizza Dough — And What Happens If You Rush It | 107 | 07-06 | 564 | salt timing pizza dough |
| `2026-07-09-…semolina` | Why We Use Semolina on the Peel (And What Flour Can't Do) | 111 | 07-09 | 556 | semolina on pizza peel |
| `2026-07-13-pecorino…` | Pecorino vs. Parmigiano on Pizza: When Each Belongs and When Neither Does | 103 | 07-13 | 562 | pecorino vs parmigiano pizza |
| `2026-07-16-hot-honey…` | Hot Honey on Pizza: When It Works and When It Overwhelms Everything Else | 122 | 07-16 | 564 | hot honey pizza |
| `2026-07-20-canned-vs-fresh-clams…` | Canned vs. Fresh Clams for New England White Clam Pizza | 121 | 07-20 | 538 | canned vs fresh clams pizza |

Title-length check: three titles exceed 60 chars (`ninja-woodfire-accessories` 60, salt-timing 72, pecorino 73, hot-honey 72, olive-oil 67, yeast 64, fresh-basil 66, hand-stretching 57 ok). Meta descriptions: two exceed 155 (⚠ above). **[B]**

### 1.2 Recipes — live (6)

Structured recipes carry most content in frontmatter (`ingredients`/`instructions`), so "body words" understates real length; "≈total" adds frontmatter content.

| Slug | Title | Pub | Body words | ≈Total | Schema JSON-LD? |
|---|---|---|---|---|---|
| `chicken-bacon-ranch` | Chicken, Bacon & Ranch | 06-01 | 322 | ~900 | ✅ Recipe (structured) |
| `pesto-mozzarella-basil` | Pesto, Fresh Mozzarella & Basil | 06-01 | 376 | ~950 | ✅ Recipe (structured) |
| `caputo-breadmaker-dough` | Caputo 00 Breadmaker Dough | 05-31 | 387 | ~700 | ✅ Recipe (structured) |
| `clam-pie-new-england-way` | Clam Pie, the New England Way | 06-15 | 450 | ~1,000 | ✅ Recipe (structured) |
| `roasted-heirloom-tomato-sauce` | Roasted Heirloom Tomato Sauce | **08-01 (future)** ⚠ | 350 | ~800 | ✅ Recipe (structured) |
| `new-hampshire-mushroom-taleggio` | New Hampshire Mushroom & Taleggio | **09-15 (future)** ⚠ | 325 | ~850 | ✅ Recipe (structured) |

⚠ **Future-dated but already built and public.** Astro only filters `draft: true`, not future `pubDate`. These two pages are live today showing dates that haven't happened. Decide: mark them `draft: true` until their dates, or accept early publication. **[?]**

### 1.3 Recipes — drafts (13, not built; queue for the Mon/Thu automation)

`beach-pizza` (07-13), `same-day-pizza-dough` (07-27), `master-cold-ferment-dough` (07-20), `south-shore-bar-pizza` (08-03), `greek-pizza` (08-10), `new-haven-plain-tomato-pie` (08-17), `rhode-island-bakery-pizza` (08-31), `neapolitan-margherita` (09-07), `ny-style-slice` (09-14), `detroit-style-pizza` (09-21), `grandma-pie` (09-28), plus `sample-recipe-schema-demo` (test file — recommend deleting **[F]**).

Two time bombs in this queue:

1. **Every draft references a hero image that doesn't exist** (`/images/recipes/*.jpg` — the `public/images/recipes/` directory isn't there). The moment one publishes, its hero 404s and its JSON-LD `image` points at a 404. Needs images (yours to supply) or the `heroImage` fields removed before their dates. **[?]**
2. **Three drafts have `pubDate`s that have already passed** (beach-pizza 07-13, master-dough 07-20, same-day-dough 07-27) but are still `draft: true`. Either the automation stalled or the dates need moving. Worth checking the pipeline. **[?]**

### 1.4 Static pages

`/` (home), `/blog/`, `/recipes/`, `/gear/`, `/about/`, `/quick-start-guide`, `/pizza-party-kit`, `/disclosure`, `/privacy-policy`, `/rss.xml`, sitemap.

---

## 2. Keyword cannibalization

| Risk | Pages | Assessment |
|---|---|---|
| **High** | `72-hour-cold-ferment-dough` (blog, live) vs. `master-cold-ferment-dough` (recipe, drafts as "48-Hour Cold Ferment… one dough to rule the site") | Both target *cold ferment pizza dough*. When the draft publishes, they'll compete directly. Options: (a) make the recipe canonical and 301 the blog post, (b) reposition the blog post as the "why/story" piece linking to the recipe as the canonical how-to, (c) merge. My lean is (b) — no URL dies, intent splits cleanly. **Needs your call before Task B.** **[?]** |
| **Medium** | `best-pizza-accessories-under-50` vs. `ninja-woodfire-accessories-worth-buying` | Both list peels, IR thermometer, pellets, proofing box, mitts. Salvageable by differentiation: under-$50 = generic/any-oven angle; Ninja post = Ninja-specific. Task B/E would sharpen titles and cross-link with distinct anchors rather than merge. |
| **Medium** | `prime-day-pizza-oven-deals-2026` vs. `best-outdoor-pizza-ovens-under-500` | Same four ovens, same links. Acceptable as seasonal satellite → pillar, but the Prime Day page is now stale (see §3) which makes it dead weight competing on "pizza oven deals". |
| **Low** | `2026-06-16 infrared thermometer` vs. both accessories posts | Technique post vs. list posts — fine; fix the absolute-URL internal link (§5.3). |
| **Low (future)** | `same-day-pizza-dough` (draft) vs. dough-readiness/yeast technique posts | Different intents; watch anchors when it publishes. |

## 3. Stale content

- **`prime-day-pizza-oven-deals-2026`** — Prime Day (June 23–26) is over a month past. Page still says "Prime Day runs June 23–26 this year… this is the window worth paying attention to," with 22 price references. Recommend: reframe as an evergreen "pizza oven deals" page (or annual update pattern + note "next event"), keep URL for next year. **[B] [?]** on the approach.
- **Price mentions elsewhere** (best-ovens: 21 price refs; ninja-accessories: 16; best-accessories: 6; backyard-setup: 4; infrared post: "about $20"). Prices drift; not urgent, but Task B should soften exact prices to ranges where the copy allows without rewriting voice.
- **No "2024"/"2025" references anywhere** — clean.
- **No post has `updatedDate`** — worth adopting once Task B edits land (Google shows freshness from schema/meta).

---

## 4. Affiliate link audit

### 4.1 The good news

**All 36 unique `amzn.to` short links across the repo resolve to `tag=newenglandcru-20`.** I followed every redirect; every destination carries the correct tag (`linkCode=sl2`, per-link `linkId`s). No missing, wrong, or malformed tags found. Nothing needs a tag fix.

### 4.2 Systemic issues (every affiliate link on the site)

| Issue | Where | Fix task |
|---|---|---|
| `rel` is `noopener nofollow` — **missing `sponsored`** | `AffiliateLink.astro:30` → every component-rendered link | **[D]** |
| Raw markdown Amazon links have **no `rel` at all** (and no `target`) | `best-outdoor-pizza-ovens-under-500.mdx` (13 links, 4 of them inside H3 headings), `prime-day-…-2026.mdx` (7 links, 4 inside H3 headings), `best-pizza-accessories-under-50.md` (10 links) | **[D]** — route through `AffiliateLink`; links inside headings also get pulled into body per **[B]** heading hygiene |
| Links inside `<h3>` headings | best-ovens, prime-day | **[B]/[D]** |

### 4.3 Per-post link → disclosure map

FTC disclosure = the standard "This post contains affiliate links…" block. "Above" = appears before the first affiliate link.

| Page | Affiliate links | Disclosure above first link? |
|---|---|---|
| best-outdoor-pizza-ovens-under-500 | 13 raw amzn.to + 2 components | ✅ |
| prime-day-pizza-oven-deals-2026 | 7 raw amzn.to | ✅ (unbolded variant — normalize **[D]**) |
| best-pizza-accessories-under-50 | 10 raw amzn.to | ✅ |
| ninja-woodfire-accessories-worth-buying | 12 components | ✅ |
| backyard-pizza-night-setup | 2 components | ✅ |
| 72-hour-cold-ferment-dough | 2 components | ✅ |
| caputo-breadmaker-dough (recipe) | 4 components | ✅ |
| /gear/ | 19 components | ✅ (page-level disclosure above list) |
| Recipe "Gear I used" cards (5 live recipes) | components via `gear:` frontmatter | ⚠ card's own disclosure sits **below** the links (`RecipeLayout.astro:272`); acceptable as a card caption but **[D]** should move it above or add a page-top line |

### 4.4 Broken / defective links found

1. **`clam-pie` blog post has a literal placeholder in published copy** — `2026-07-20-canned-vs-fresh-clams…md:33` renders "*an Ooni Koda 12 \*[Affiliate link: Ooni Koda 12 — Ooni]\**" as visible text on the live page. Looks like the automation emitted an unresolved token. Fix: replace with an `AffiliateLink`/tagged link or plain text. **[D]** — also worth checking the automation's template so it doesn't recur. **[?]**
2. ~~`chicken-bacon-ranch` gear card never renders its link.~~ **Correction (2026-07-28):** misdiagnosed — the entry does carry `affiliateId` (the initial read was truncated). The real finding: four live recipes carry intentional "Ooni Pizza Oven — pending approval" gear placeholders rendering as "Pending affiliate link" even though the interim-Amazon policy and a live `ooni-koda-12` registry entry exist. Fixed in Task D step 1 by pointing them at the interim Amazon link. **[D]**
3. **Two different Ooni Koda 12 destinations in circulation:** the registry (`affiliateLinks.ts` `ooni-koda-12`) short link resolves to a **Koda 12 bundle** (ASIN B0FLDRWD4F), while the ovens/prime-day posts' raw links resolve to the **standard Koda 12** (ASIN B07PN5R5WY). Same for no other product. Which ASIN do you want canonical? **[?]**
4. Duplicate short links for the same product with different `linkId`s (e.g., two OXO scraper shorts, two Chef Pomodoro shorts, two Etekcity scale shorts, two XSKOPPL shorts). Harmless for tracking, but Task D's component refactor would collapse each product to one registry entry.
5. **Found during Task D step 1 — three wrong-product links in `best-pizza-accessories-under-50`:** the "Perforated Aluminum Pizza Peel" section linked to the OXO bench scraper, and both the "Etekcity Infrared Thermometer" and "Kona Wood Pellets" sections linked to Ninja Robust Blend pellets. All three now point at the correct products via the component.
6. `RecipeLayout.astro:285` — the email-capture form has `action="TODO"`; submitting it errors. Not affiliate, but it's a live broken form on every structured recipe. **[F]**

### 4.5 Direct-program candidates (for when Ooni/Solo Stove/SharkNinja approve)

Per your instruction these are flagged only — no links changed. Amazon links currently pointing at these brands' products:

- **Ooni:** `ooni-koda-12` (registry; bundle ASIN) · raw links in best-ovens ×3 and prime-day ×1 (standard ASIN)
- **Solo Stove:** `solo-stove-pi` (registry) · raw links in best-ovens ×3, prime-day ×1 (both → ASIN B0CG2MB8YB)
- **Ninja (SharkNinja):** `ninja-woodfire-oven`, `ninja-cover`, `ninja-peel`, `ninja-stand`, `robust-blend-pellets`, `all-purpose-pellets` (registry, used across ninja-accessories, gear, backyard-setup, best-ovens, chicken-bacon-ranch gear) · raw links in best-ovens ×3, prime-day ×1

Because nearly all of these flow through `affiliateLinks.ts`, the eventual swap is mostly a one-file change — one more reason to route the remaining raw links through the component in Task D.

### 4.6 Missed monetization (observation only — your call whether Task D adds links)

The automated June/July technique posts contain **zero affiliate links**, including posts with explicit buy-guidance sections: yeast ("What to Actually Buy"), olive oil ("What to Actually Buy"), 00-flour, two-peels (peel post with no peel link), storing-pellets (no pellet link), infrared post (names the Etekcity, price and all, no product link — `infrared-thermometer` exists in the registry). All the matching products are already in `affiliateLinks.ts`. Flagging because it's the difference between the content queue compounding revenue or not — but adding links to published posts is an editorial decision. **[?]**

---

## 5. Technical SEO

### 5.1 Working correctly

- Canonical tag on every page (`SEO.astro:27`, absolute, from `Astro.site`) ✅
- Sitemap generated (`sitemap-index.xml`) ✅ · robots.txt points to it ✅
- RSS at `/rss.xml`, drafts excluded ✅
- Meta description, OG, Twitter cards on every page ✅
- GA4 + Search Console verification tags present ✅
- Single H1 per page from layout ✅ (one exception below)

### 5.2 Issues

| Issue | Detail | Task |
|---|---|---|
| **Default OG image 404s site-wide** | `SEO.astro` defaults to `/og-image.jpg`; no such file in `public/`. Every blog post (none set `heroImage`) shares this broken image — social shares render imageless. Need a real default OG image (I can generate a branded one, or you supply a photo). | **[B] [?]** |
| **Sitemap URL mismatch with Search Console** | Project notes say `sitemap.xml` was submitted; the site only emits `sitemap-index.xml`. If GSC has `sitemap.xml`, it's fetching a 404. Verify/resubmit after merge. | **[G]** next-actions |
| Duplicate H1 | `2026-06-25-fresh-basil…` repeats its title as a `#` heading in the body → two H1s on the page | **[B]** |
| No Article/BlogPosting schema on blog posts | Only structured recipes emit JSON-LD | **[C]** |
| No Product/Review/ItemList/FAQPage/BreadcrumbList anywhere | best-ovens has a real FAQ section; ninja-accessories has "A Few Questions We Get Asked" — both FAQPage candidates. best-ovens + best-accessories are ItemList candidates | **[C]** |
| Legacy recipes (none currently live-and-unstructured — all 6 live recipes are structured) | The legacy render path in `recipes/[...slug].astro` emits **no** JSON-LD; fine today, matters if an unstructured recipe ever ships | **[C]** |

### 5.3 Internal-link hygiene (full fix in Task E)

- Absolute internal URL: infrared post links `https://newenglandcrust.com/blog/ninja-woodfire-accessories-worth-buying/` instead of a relative path.
- Trailing-slash inconsistency: ninja-accessories, prime-day, caputo-breadmaker, chicken-bacon-ranch etc. link `/blog/foo` (no slash) → 308 redirect under `format: 'directory'`; others use `/blog/foo/`. Normalize to trailing slash.
- Mislabeled anchor: chicken-bacon-ranch links to backyard-setup with the text "How to Throw a Pizza Party for 12 Without Losing Your Mind" — not that page's title.
- `/gear` vs `/gear/` both used in best-accessories.
- **Orphan-ish pages** (no inbound links from other content found): all 15 automated technique posts link out to nothing (13 of 15 have zero internal links) and receive links only from listing pages; `welcome-to-new-england-crust`, `storing-pellets` (1 inbound), `/quick-start-guide` (1 inbound), `/pizza-party-kit` (0 inbound from content). The money pages (best-ovens, accessories posts) have decent inbound; the technique-post cluster is where Task E adds the most value — they're the future authority feeding the money pages.

---

## 6. Image audit

### 6.1 Existing images

| Image | Alt text | Filename quality |
|---|---|---|
| `/images/NinjaWoodfireHero.jpeg` (home hero) | ✅ descriptive | ⚠ CamelCase, non-descriptive-ish (`ninja-woodfire-oven-front.jpg` better; rename only with redirect care) |
| `/images/caputo-dough-ingredients.jpeg` (caputo recipe hero) | ✅ (alt = recipe title) | ✅ |
| `/assets/recipes/pesto-mozzarella-basil/…hero.jpg` + 5 step photos | ✅ hero (alt = title); step photos have real, descriptive alts in frontmatter — 2 of 5 step photos (`ninja-woodfire-oven`, `slice-detail`) appear defined but unused in the published steps; verify | ✅ excellent kebab-case names |
| `/assets/ember/*` (Ember badge ×3 pages) | ✅ | ✅ |

### 6.2–6.4 Gaps

- **Blog posts contain zero body images.** All 24. Not a "fix" I can do without your photos, but it caps both SEO (image search, engagement) and social sharing.
- Recipe hero alt text = recipe title everywhere (`RecipeLayout.astro:142`, `[...slug].astro:69`). Acceptable, not descriptive. Task B can pass real alts where we have them.
- 4 of 6 live recipes have **no hero image** (chicken-bacon-ranch, clam-pie, mushroom-taleggio, roasted-heirloom) → their JSON-LD lacks `image`, which weakens rich-result eligibility (Google strongly prefers `image` on Recipe).
- All 12 queued draft recipes point at nonexistent hero files (§1.3).

---

## 7. Voice & editorial observations (not acting without you)

- The site alternates between "we/our" (dominant) and "I/my" (gear page copy, "Gear I used" card, RecipeLayout disclosure). Project notes describe the voice as first-person singular; the corpus is overwhelmingly "we." Task B will match the corpus ("we") unless you say otherwise. **[?]**
- Project notes also say the ovens post has three picks under "My Picks"; the live post has five ovens reviewed and a "## Our two picks" section. No action needed — just noting the drift so the notes can be updated.

---

## 8. Proposed commit grouping for Tasks B–G (per ground rule 4)

1. `B:` titles/metas, H1 fixes, OG default image, stale-content updates
2. `C:` JSON-LD (Article, ItemList, FAQPage, BreadcrumbList, Product/Review)
3. `D:` affiliate rel/sponsored, raw-link → component refactor, disclosure normalization, placeholder + gear-card fixes
4. `E:` internal-link plan execution
5. `F:` frontmatter standardization, component extraction, CONTRIBUTING-SEO.md, delete schema-demo
6. `G:` PR body

## 9. Questions needing your answer before Task B *(the [?] items in one place)*

1. Cold-ferment cannibalization: reposition blog post as story piece linking to the recipe (my recommendation), redirect, or merge?
2. Future-dated live recipes (roasted-heirloom, mushroom-taleggio): hide until their dates, or leave live?
3. Draft-recipe hero images: will you supply photos, or should I strip the `heroImage` fields from the queue for now?
4. Three drafts have past `pubDate`s — is the Mon/Thu automation stalled, or should I re-date them?
5. Prime Day page: convert to evergreen deals page, or leave and update next June?
6. Ooni Koda 12: canonical ASIN — bundle (registry) or standard (posts)?
7. Default OG image: I can build a branded one from existing assets, or you provide a photo.
8. Add affiliate links to the published technique posts (§4.6), or leave published posts untouched?
9. Voice for rewritten titles/metas: "we" (matches corpus) or "I" (matches project notes)?

---

## Appendix — Ooni + Solo Stove Amazon inventory (2026-07-28)

Per the oven-brand affiliate policy: no Amazon-tagged links to Ooni or Solo Stove products anywhere (clean outbound profile for Impact/Avantlink reapplication); Ninja stays on Amazon. This is every Amazon-tagged Ooni/Solo Stove link on the site after the step-1 reverts (recipe gear cards restored to "pending"; clam post link removed). Every entry below renders through `AffiliateLink` + the registry, so each fix is a registry flip and/or a one-line edit.

**Decision key: (a) remove entirely · (b) swap to untracked brand-direct URL · (c) leave, accept reapplication risk**

### Ooni — all Ooni Koda 12, full oven (registry `ooni-koda-12` → amzn.to/44cJ3sE → ASIN B07PN5R5WY)

| # | Source | Context | Decision |
|---|---|---|---|
| O1 | `best-outdoor-pizza-ovens-under-500.mdx:46` | comparison-table row | |
| O2 | `best-outdoor-pizza-ovens-under-500.mdx:60` | "the benchmark" review section, first mention | |
| O3 | `best-outdoor-pizza-ovens-under-500.mdx:216` | "Pick 1: Ooni Koda 12" | |
| O4 | `prime-day-pizza-oven-deals-2026.mdx:32` | deals section (page converts to evergreen in step 7) | |
| O5 | `src/pages/gear/index.astro:18` | /gear/ "The ovens" card | |
| O6 | registry `affiliateLinks.ts` `ooni-koda-12` | source entry all of the above resolve through | |

### Solo Stove — all Solo Stove Pi (gas), full oven (registry `solo-stove-pi` → amzn.to/4fiw9yD → ASIN B0CG2MB8YB)

| # | Source | Context | Decision |
|---|---|---|---|
| S1 | `best-outdoor-pizza-ovens-under-500.mdx:48` | comparison-table row | |
| S2 | `best-outdoor-pizza-ovens-under-500.mdx:102` | "the forgiving one" review section, first mention | |
| S3 | `best-outdoor-pizza-ovens-under-500.mdx:226` | "Also worth considering" pick | |
| S4 | `prime-day-pizza-oven-deals-2026.mdx:38` | deals section (page converts to evergreen in step 7) | |
| S5 | `src/pages/gear/index.astro:27` | /gear/ "The ovens" card | |
| S6 | registry `affiliateLinks.ts` `solo-stove-pi` | source entry all of the above resolve through | |

**Verified absent:** Ooni Fyra (mentioned, never linked — correct), Ooni/Solo accessories or branded gear (none exist on the site), draft-queue recipes (Ooni gear entries are inert `YOUR-AFFILIATE-LINK` placeholders), clam post (link reverted to plain text), live recipe gear cards (restored to "pending"). Ninja links: excluded per policy, unchanged.

---

*Method notes: word counts strip frontmatter/components/code; structured-recipe totals estimated including frontmatter ingredients/instructions. Affiliate tags verified by following every `amzn.to` redirect on 2026-07-28. No content, links, or code were modified in this pass.*
