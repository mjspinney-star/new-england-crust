# Affiliate Links — Cowork Handoff (Complete)

## What This Does

Sets up a central affiliate link system for New England Crust and applies real
Amazon affiliate links across three posts and the dough recipe. All 17 products
are pre-loaded with short (amzn.to) and full tagged URLs. Tag: `newenglandcru-20`.

---

## Step 1 — Add the data file

Copy the file `affiliateLinks.ts` from `/mnt/user-data/outputs/` to:

**Destination:** `src/data/affiliateLinks.ts`

---

## Step 2 — Add the component

Copy the file `AffiliateLink.astro` from `/mnt/user-data/outputs/` to:

**Destination:** `src/components/AffiliateLink.astro`

---

## Step 3 — Check MDX is installed

```bash
npm list @astrojs/mdx
```

If not installed:
```bash
npx astro add mdx
```

---

## Step 4 — Convert blog posts from .md to .mdx

Rename these files (content stays identical, only the extension changes):

- `src/content/blog/ninja-woodfire-accessories-worth-buying.md` → `.mdx`
- `src/content/blog/best-outdoor-pizza-ovens-under-500.md` → `.mdx`
- `src/content/blog/backyard-pizza-night-setup.md` → `.mdx`

---

## Step 5 — Add the import line to each .mdx blog post

After the closing `---` of the frontmatter in each of the three blog posts above,
add this import line:

```mdx
import AffiliateLink from '../../components/AffiliateLink.astro';
```

Adjust the relative path if needed based on actual folder depth.

---

## Step 6 — Replace placeholders in the accessories post

File: `src/content/blog/ninja-woodfire-accessories-worth-buying.mdx`

Use the replacement table below. Find each exact placeholder string and replace
with the component call shown.

| Find this exact text | Replace with |
|---|---|
| `*[[Affiliate link: Amazon — Ninja XSKOCVR Premium Cover]]*` | `<AffiliateLink id="ninja-cover" />` |
| `*[[Affiliate link: Amazon — third-party OO100 series cover]]*` | `<AffiliateLink id="third-party-cover" />` |
| `*[[Affiliate link: Amazon — 12-gauge 25-foot outdoor extension cord]]*` | `<AffiliateLink id="extension-cord" />` |
| `*[[Affiliate link: Amazon — Ninja XSKOPPL Perforated Pizza Peel]]*` | `<AffiliateLink id="ninja-peel" />` |
| `*[[Affiliate link: Amazon — generic 12-inch aluminum perforated peel]]*` | `<AffiliateLink id="generic-peel" />` |
| `*[[Affiliate link: Amazon — Etekcity infrared thermometer]]*` | `<AffiliateLink id="infrared-thermometer" />` |
| `*[[Affiliate link: Amazon — Ninja XSKUNSTAND Outdoor Stand]]*` | `<AffiliateLink id="ninja-stand" />` |
| `*[[Affiliate link: Amazon — Keter Unity XL Portable Folding Work Table]]*` | `<AffiliateLink id="keter-stand" />` |
| `*[[Affiliate link: Amazon — Ninja Cast Iron Tray]]*` | `<AffiliateLink id="outspark-griddle" />` |
| `*[[Affiliate link: Amazon — Ninja All-Purpose Blend pellets, 5-lb]]*` | `<AffiliateLink id="all-purpose-pellets" />` |
| `*[[Affiliate link: Amazon — Ninja Robust Blend pellets, 2-lb]]*` | `<AffiliateLink id="robust-blend-pellets" />` |
| `*[[Affiliate link: Amazon — Kona Pellets variety pack]]*` | `<AffiliateLink id="kona-pellets" />` |

**Also update the cast iron / griddle section copy.** Find the sentence:
> "Ninja sells a cast iron tray that drops into the accessory frame"

And update it to read:
> "Ninja sells a cast iron tray, though it's often out of stock — we link to the **Outspark** porcelain steel pan instead. Same size, same fit, non-stick, and usually cheaper."

---

## Step 7 — Replace placeholders in the other two blog posts

These posts have fewer links. Apply the same replacement table from Step 6 to
any matching placeholders found in:

- `best-outdoor-pizza-ovens-under-500.mdx`
- `backyard-pizza-night-setup.mdx`

---

## Step 8 — Add affiliate links to the dough recipe post

File: `src/content/recipes/72-hour-cold-ferment-dough.md`

This is a recipe file, not a blog post — check if it needs to be `.mdx` or if
the recipe content collection already supports components. If not, convert it
to `.mdx` and add the same import line:

```mdx
import AffiliateLink from '../../components/AffiliateLink.astro';
```

Then make these four targeted additions to the post content:

### 8a — Caputo 00 Flour

Find the first mention of "Caputo 00 flour" or "00 flour" in the ingredients
or introduction. After that mention, append:

```mdx
<AffiliateLink id="caputo-flour" label="Antimo Caputo 00 Flour" />
```

It should read naturally, like:
> "We use Caputo 00 flour — <AffiliateLink id="caputo-flour" label="Antimo Caputo 00 Flour" /> — for every batch."

Or if the ingredients list is formatted as a list, add a parenthetical:
> `500g Caputo 00 flour` → `500g Caputo 00 flour (<AffiliateLink id="caputo-flour" label="buy on Amazon" />)`

### 8b — Caputo Dry Yeast

Find the mention of "Caputo Lievita" or "Caputo dry yeast" or "dry yeast" in
the ingredients or technique sections. After that mention, append:

```mdx
<AffiliateLink id="caputo-yeast" label="Caputo Lievita dry yeast" />
```

### 8c — Baleine Sea Salt

Find the mention of "Baleine" or "sea salt" or "fine sea salt" in the
ingredients. After that mention, append:

```mdx
<AffiliateLink id="baleine-sea-salt" label="Baleine fine sea salt" />
```

### 8d — Cuisinart Bread Maker (notes section only)

Find the notes or tips section of the post. If there is already a mention of
the Cuisinart bread maker or CBK-110, add the link there:

```mdx
<AffiliateLink id="cuisinart-bread-maker" label="Cuisinart CBK-110" />
```

If there is NO mention of the bread maker yet, add this note at the end of
the notes section (before any Related Posts links):

> **Want to skip the hand-mixing?** The <AffiliateLink id="cuisinart-bread-maker" label="Cuisinart CBK-110" /> handles the mixing and first rise on the Dough cycle — pull the dough out, ball it, and cold-ferment overnight. Useful when you're making six or more balls at once.

---

## Step 9 — Verify disclosure is present on all posts

Amazon requires a clear affiliate disclosure on every page with affiliate links.

Check that each of these posts has this (or equivalent) at the top, visible
before any affiliate links:

> "This post contains affiliate links. If you click and buy something, we may
> earn a small commission at no extra cost to you."

The accessories post already has this. Confirm the other posts do too, and add
it to the dough recipe if missing.

---

## Step 10 — Spot-check in the browser

After all changes are made:

1. Load each updated post locally
2. Click one affiliate link per post
3. Confirm the Amazon URL contains `tag=newenglandcru-20`
4. Confirm the `→ Amazon` badge appears next to each link

---

## Amazon Compliance Summary

- ✅ `rel="noopener nofollow"` on every link
- ✅ Short amzn.to URLs are permitted — they redirect to tagged full URLs
- ✅ No Amazon product images used (text links only)
- ✅ Links open in new tab (`target="_blank"`)
- ✅ Per-page affiliate disclosure present on every post
- ❌ Do NOT use these links in email newsletters as direct purchase links

---

## Adding New Products Later

Open `src/data/affiliateLinks.ts` and append to the array:

```ts
{
  id: "your-product-id",
  name: "Product Display Name",
  short: "https://amzn.to/XXXXXX",
  full: "https://www.amazon.com/...linkCode=ll2&tag=newenglandcru-20...",
  category: "tool",
},
```

Then use `<AffiliateLink id="your-product-id" />` in any `.mdx` file.
