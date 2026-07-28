# Registry Gaps — Product Intake Queue

Products the content recommends but `src/data/affiliateLinks.ts` can't link yet.
Log a gap here when writing; fill them in batches (find the listing, verify the
tag resolves, add the registry entry, then link the waiting posts).

_Last updated: 2026-07-28 (fable5-seo-audit branch)._

## Open gaps

| Product | Needed by | Notes |
|---|---|---|
| **Turning peel** (small round metal, 9–10") | `2026-06-01-two-peels…` ("What we recommend" — the post's whole subject); `2026-07-02-grilled-corn…` ("a turning peel makes this much easier") | Registry only has launching peels. Related mislabel: best-ovens accessories and the deals page currently link `ninja-peel` (a launching peel) under the text "metal turning peel" — swap those to the real turning peel once added. |
| **Finishing olive oil** | `2026-06-22-finishing-with-good-olive-oil…` ("What to Actually Buy" section is unlinked) | Post describes the product class; pick a brand you'd genuinely stand behind. |
| **Semolina flour** | `2026-07-09-the-case-for-semolina…` | Whole post is about it; no registry entry. |
| **Pellet storage: 5-gal bucket + Gamma Seal lid** | `storing-pellets-new-england-summer` ("The setup" step 2) | Named specifically in the post. |
| **Food-safe silica gel packs** | `storing-pellets-new-england-summer` ("The setup" step 3) | "Cheapest insurance you can buy" — easy add. |

Filled this session (pattern reference): `saf-instant-yeast` (B0001CXUHW), `mikes-hot-honey` (B085B1YZ8Q), `hans-grill-brush`, `thermopop-2`, `vollum-banneton`.

## Voice-mix log (pages where we/I clash within one page — fix by hand)

- **All live structured recipes** (chicken-bacon-ranch, pesto, clam-pie, caputo-breadmaker, + queue as it publishes): recipe bodies/steps are "we"-voiced ("We always make a double batch") but the layout renders "Gear **I** used" and "**I** earn a small commission" (`RecipeLayout.astro`). One-line-each fix in the layout, or migrate recipe prose — your call.
- **/gear/ page**: intro notes say "**We** use the Ninja Woodfire as our daily driver" while product blurbs say "**I** buy the 2.2-pound bag… **I** run 62–65% hydration." Same page, both voices.
- Blog corpus is consistently "we" per page and the two rewritten pages (cold-ferment story, deals) are consistently "I" — no within-page clash there.
