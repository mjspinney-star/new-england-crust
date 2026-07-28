# CONTRIBUTING-SEO — Conventions for New England Crust

The rules established in the 2026-07 SEO/affiliate audit (`fable5-seo-audit`).
Follow these for every new post, recipe, and code change so the site stays
consistent without re-auditing.

## Affiliate links

1. **Never hand-write an Amazon link in content.** Every affiliate link goes
   through `<AffiliateLink id="..." />` backed by `src/data/affiliateLinks.ts`.
   The component owns `rel`, tracking, badges, and brand policy — content that
   uses it inherits every future fix automatically. (Posts using components
   must be `.mdx`; renaming `.md` → `.mdx` keeps the slug.)
2. **Registry entries** use tag `newenglandcru-20`. Preferred URL shape when no
   `amzn.to` short exists: `https://www.amazon.com/dp/ASIN/?tag=newenglandcru-20`.
   Verify the ASIN is the exact product the copy describes before adding —
   we've shipped wrong-product links before.
3. **Oven-brand policy** (until direct programs approve):
   - **Ooni & Solo Stove:** never Amazon-tagged, anywhere, any product. Their
     registry entries carry `pendingProgram: { brand, brandUrl }` which makes
     the component render an untracked brand-site link (`rel="noopener nofollow"`,
     "→ Ooni"/"→ Solo Stove" badge) instead of Amazon. On approval: replace the
     Amazon URLs with the program's tracked URL and remove `pendingProgram`.
   - **Ninja:** stays on Amazon Associates (Impact rate not clearly better).
   - Everything else: Amazon Associates as normal.
4. **Product with no registry entry?** Don't improvise a link — log it in
   `REGISTRY-GAPS.md` and name the product in plain text.
5. **Never emit placeholder tokens** like `*[Affiliate link: …]*`. The post
   generator is prompt-forbidden from doing this; don't reintroduce it.

## FTC disclosure

- Any page with at least one affiliate link gets the standard line **above the
  first affiliate link** (in practice: right under the frontmatter/imports):
  `**Disclosure:** This post contains affiliate links. If you click and buy
  something, we may earn a small commission at no extra cost to you.`
  (Use "I may earn" on "I"-voiced pages.)
- Recipe gear cards get their disclosure above the link list (already in
  `RecipeLayout.astro`). A page with no affiliate links carries no disclosure.

## Publishing model

- A page is public only when `draft: false` **and** `pubDate` ≤ build time
  (`src/data/publishing.ts` — used by routes, indexes, and RSS). It is safe to
  set `draft: false` on future-dated queue entries in advance; each appears on
  the first build on/after its date.
- Queue cadence is Mon/Thu. Check existing queue dates before scheduling.
- `heroImage` may only reference a file that exists in `public/`. No image yet?
  Omit the field — JSON-LD and social fall back to `/og-image.jpg`.

## Frontmatter & metadata

- `title` ≤ 60 chars; `description` ≤ 155 chars, written for humans.
- `pubDate` required; add `updatedDate` on meaningful content updates.
- Dates are `YYYY-MM-DD`.
- Voice: instructional/how-to content is "we"; story/experience pieces and
  newly generated pages are "I". Don't mix voices within one page — log
  clashes in `REGISTRY-GAPS.md`.

## Structure & links

- One H1 per page — the layout renders it from `title`. Never open the body
  with a `#` heading.
- **No links inside headings.** Link the product/page at its first natural
  mention in the section body instead.
- Internal links: relative paths with trailing slash (`/blog/some-post/`).
  Never absolute `https://newenglandcrust.com/...`.
- Changing a slug? Add both slash variants to `public/_redirects` as 301s and
  keep the old URL redirecting forever.

## Images

- Descriptive kebab-case filenames (`pesto-pizza-spreading-sauce.jpg`) and
  real, specific alt text — the pesto recipe's step images are the model.
- Site-wide social fallback is `/og-image.jpg` (1200×630, brand palette).

## When brand programs approve (the swap runbook)

1. Get the tracked product URL from Impact/Avantlink.
2. In `affiliateLinks.ts`: set it as `short`/`full`, remove `pendingProgram`.
3. Nothing else — every page renders from the registry. Verify with a build:
   `grep -rl "amzn.to\|amazon.com" dist` should show no Ooni/Solo hits.
