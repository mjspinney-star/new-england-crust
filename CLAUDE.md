# New England Crust — Project Context

> Durable project brief for Claude Code sessions. Update it as the site
> evolves — decisions made, content published, programs joined.
> Rewritten 2026-07-28 at the end of the fable5-seo-audit pass; that branch's
> PR (#3) and `AUDIT.md` hold the full history of how we got here.
> Updated 2026-08-26: PAT rotation resolved, Cowork sandbox constraints
> documented.

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
  `new-england-crust`, assets dir `./dist`). Deploy with `npm run deploy`.

  **Do not use `npx wrangler versions upload`.** It uploads a version but
  does NOT route traffic to it — the version sits unpromoted while the site
  continues serving whatever was promoted last. This silently served a stale
  build on 2026-08-17 (three unpromoted versions had accumulated). Promoting
  requires a separate `npx wrangler versions deploy`. `wrangler deploy`
  does both in one step, which is what `npm run deploy` runs.
- Content: markdown collections in `src/content/blog/` and
  `src/content/recipes/` (`.mdx` when a post uses components)
- Analytics: GA4 `G-3QBKJCC5F9` (tag in `BaseLayout.astro`)
- Search Console: sitemap is **`/sitemap-index.xml`** (there is no
  `sitemap.xml` — never point anything at that)
- Build: `npm run build` — run it after every change set, **from Terminal
  only** (see sandbox constraints below); fix what you broke

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
| Commit/push wrapper used by Cowork jobs | `run-git-commit.command` |
| Cowork job specs (mirror the live scheduler) | `Pinterest/COWORK-PINTEREST-SCHEDULES.md`, `Email/COWORK-NEWSLETTER-SCHEDULE.md` |

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

## Cowork sandbox constraints — read before writing any job spec

Cowork's sandbox **can create and overwrite files but cannot delete them.**
Every unlink fails with EPERM. This is the shape of the environment, not an
obstacle to route around.

- **No git commands in job specs.** Any git operation that writes a lock file
  (`HEAD.lock`, `index.lock`, `ORIG_HEAD.lock`) leaves it behind permanently
  and breaks every later run. `git pull` in job specs caused repeated silent
  failures from June through August 2026.
- **Read content via `git show origin/main:<path>`** when a job needs current
  content, rather than pulling into the working tree.
- **Never `npm run build` from the sandbox.** Astro and Vite delete files
  during cleanup, so the build exits non-zero even when output looks complete,
  and a partial build writes junk into `dist/` that later runs misread.
- **Auto-maintenance is disabled** on this repo (`maintenance.auto false`,
  `gc.auto 0`) because `git fetch` regenerated `.git/objects/maintenance.lock`
  on every run and the sandbox could not unlink it. Run `git gc` manually from
  Terminal every few weeks.
- **Lock checks use `find .git -maxdepth 1 -name "*.lock"`** — top level only.
  Locks inside `objects/` are routine maintenance artifacts, not dead
  operations.
- **Job specs exist in two places:** the Cowork scheduler (authoritative) and a
  mirrored `.md` file in the repo. If you edit one, edit both — drift between
  them hid the `git pull` problem for months.

## Known-open items (as of 2026-08-26)

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
6. **Security — RESOLVED 2026-08-26:** the git remote URL previously embedded a
   plaintext GitHub PAT. Two classic PATs with `repo` scope were found and
   revoked; the remote is now
   `https://github.com/mjspinney-star/new-england-crust.git` with no credential
   in the URL. Auth uses a fine-grained token scoped to this repo only
   (Contents: read/write), stored via `credential.helper osxkeychain`. Never
   put a token back in the remote URL.
7. **Job specs not yet audited** for the sandbox constraints above: reel kit,
   Search Console indexing check, headline generator, morning job digest, pin
   queue prework. The two carousel jobs and the newsletter job are clean; the
   pin generator was fixed 2026-08-26.
8. **`YOUR-AFFILIATE-LINK` placeholders** remain on some published recipes.
   The Pinterest carousel job can point traffic at a page showing a bare
   placeholder — fix before relying on that job.

## What to remember each session

1. Never add an Amazon-tagged link to an Ooni or Solo Stove product.
2. Never hand-write affiliate URLs in content — registry + component only.
3. Run `npm run build` after edits **from Terminal only** — never from a Cowork
   sandbox. The pubDate filter means future content staying hidden is correct
   behavior, not a bug.
4. Michael reviews per-step commits and wants judgment calls flagged, not
   guessed — pause on policy-shaped decisions.
5. Never `git add -A` — stage only named files. Verify commits by hash and
   GitHub diff URL, not by an agent's self-report.
6. Update this file when major decisions land.
