# New England Crust — Project Context

> Durable project brief for Claude Code sessions. Update it as the site
> evolves — decisions made, content published, programs joined.
> Rewritten 2026-07-28 at the end of the fable5-seo-audit pass; that branch's
> PR (#3) and `AUDIT.md` hold the full history of how we got here.

---

## What this site is

**New England Crust** (newenglandcrust.com) is a first-person pizza blog —
backyard outdoor-oven cooking from a New England point of view — built to grow
an audience and monetize through affiliate links. The high-value focus is
outdoor pizza ovens (Ooni, Ninja Woodfire, Solo Stove); everything else
(tools, ingredients, accessories) supports it via Amazon Associates.

## Tech stack

- **Astro** static site (`output: 'static'`, trailing-slash directory URLs)
- **Cloudflare Workers Builds project with static assets** (not Pages) —
  `Assets → ASSETS` binding, config in `wrangler.jsonc` at repo root (name
  `new-england-crust`, assets dir `./dist`), deployed via
  `npx wrangler versions upload --assets=./dist`. Confirmed working:
  production deployed successfully from `main` after PR #3 merged.
- Content: markdown collections in `src/content/blog/` and
  `src/content/recipes/` (`.mdx` when a post uses components)
- Analytics: GA4 `G-3QBKJCC5F9` (tag in `BaseLayout.astro`)
- Search Console: sitemap is **`/sitemap-index.xml`** (there is no
  `sitemap.xml` — never point anything at that)
- Build: `npm run build` — run it after every change set; fix what you broke

## Conventions — read CONTRIBUTING-SEO.md first

`CONTRIBUTING-SEO.md` at repo root is the rulebook (affiliate link rules, FTC
disclosure placement, publishing model, frontmatter limits, heading/link
hygiene, redirect procedure, brand-program swap runbook). Don't restate it
here; read it before editing content or components.

## Affiliate policy (summary — details in CONTRIBUTING-SEO.md)

- **Amazon Associates tag: `newenglandcru-20`** on every Amazon link. All
  affiliate links render through `<AffiliateLink id="..." />` backed by the
  registry — never hand-written in content.
- **Ooni & Solo Stove: NO Amazon-tagged links anywhere.** Impact/Avantlink
  reapplications are in flight (denied once for Ooni; clean outbound profile
  is critical). Their registry entries carry `pendingProgram` and render
  untracked brand-direct links until programs approve — then it's a one-line
  registry swap per brand.
- **Ninja: stays on Amazon** (direct rate not clearly better). Revisit after
  Ooni/Solo approvals land.
- Product not in the registry? Plain text + log it in `REGISTRY-GAPS.md`.

## Where things live

| What | Where |
|---|---|
| Affiliate registry (single source of truth) | `src/data/affiliateLinks.ts` |
| Affiliate link component (rel, badges, brand policy) | `src/components/AffiliateLink.astro` |
| Publish filter (draft AND pubDate ≤ now) | `src/data/publishing.ts` — used by all routes, indexes, RSS |
| Layouts (SEO meta, Recipe JSON-LD, gear cards) | `src/layouts/BaseLayout.astro`, `src/layouts/RecipeLayout.astro`, `src/components/SEO.astro` |
| Mon/Thu post generator (GitHub Actions + Claude API) | `.github/workflows/generate-weekly-blog-post.yml`, `.github/scripts/generate-post.cjs` |
| Redirects (301s live forever) | `public/_redirects` |
| Social/OG fallback image | `public/og-image.jpg` (1200×630) |
| Audit history + Ooni/Solo link inventory | `AUDIT.md` |
| Product gaps + voice-mix log | `REGISTRY-GAPS.md` |

## Publishing model

Content publishes when `draft: false` **and** `pubDate` has arrived (first
build on/after the date). The recipe queue is armed through 2026-09-28
(master-dough 07-30, south-shore 08-03, beach 08-06, greek 08-10, same-day
08-13, new-haven 08-17, ri-bakery 08-31, margherita 09-07, ny-slice 09-14,
detroit 09-21, grandma 09-28). The generator must never emit affiliate
placeholders or suggest Ooni/Solo links (prompt-enforced — keep it that way).

## Voice

First-person, personal, no content-farm tone. Two registers, never mixed on
one page: **"I"** for story/experience pieces and all newly generated content;
**"we"** stays in legacy instructional bodies (don't rewrite them). Within-page
clashes get logged in `REGISTRY-GAPS.md` for Michael to fix by hand.

## Known-open items (as of 2026-07-28)

1. **Registry gaps** (see `REGISTRY-GAPS.md`): turning peel (two posts link a
   launching peel under "turning peel" text pending this), finishing olive
   oil, semolina, pellet bucket + silica packs.
2. **Restore after 08-01:** the "Roasted Heirloom Tomato Sauce" link in
   `caputo-breadmaker-dough.mdx` "See Also" (removed while target was hidden).
3. **Voice-mix pages** logged in `REGISTRY-GAPS.md` (RecipeLayout "Gear I
   used" over "we" recipe bodies; /gear/ mixes both) — Michael fixes by hand.
4. **Parked work** (deliberately deferred until post-deploy GSC data): rest of
   Task B title/meta rewrites, Task C schema markup (Article/ItemList/FAQ/
   Breadcrumb), Task E internal linking, Task F component extraction +
   deleting `sample-recipe-schema-demo.md` (kept `draft: true` on purpose).
5. **Etekcity model nuance:** the infrared post names the "Lasergrip 1080" but
   the registry ASIN is a newer Etekcity IR gun — swap ASIN or prose someday.
6. **Security:** git remote URL embeds a plaintext GitHub PAT — rotate and
   move to a credential helper.

## What to remember each session

1. Never add an Amazon-tagged link to an Ooni or Solo Stove product.
2. Never hand-write affiliate URLs in content — registry + component only.
3. Run `npm run build` after edits; the pubDate filter means future content
   staying hidden is correct behavior, not a bug.
4. Michael reviews per-step commits and wants judgment calls flagged, not
   guessed — pause on policy-shaped decisions.
5. Update this file when major decisions land.
