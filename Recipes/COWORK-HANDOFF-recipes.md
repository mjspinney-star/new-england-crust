# Cowork Handoff — Five New Recipe Files

## What this is
Five new recipe files to add to the New England Crust site. Three complete the "Coming Soon" cards already showing on the Recipes page. Two are brand-new additions.

## Files to add
All five files live in `/mnt/user-data/outputs/`. Copy each into the recipe content collection directory (likely `src/content/recipes/` — use whatever path the existing `72-hour-cold-ferment-dough.md` lives in).

| File | Status on Recipes page |
|---|---|
| `roasted-heirloom-tomato-sauce.md` | Was "Coming Soon" — now complete |
| `new-hampshire-mushroom-taleggio.md` | Was "Coming Soon" — now complete |
| `clam-pie-new-england-way.md` | Was "Coming Soon" — now complete |
| `pesto-mozzarella-basil.md` | New — add to the Recipes page grid |
| `chicken-bacon-ranch.md` | New — add to the Recipes page grid |

## Instructions

1. **Add all five `.md` files** to the recipe content collection folder.

2. **Update the Recipes page** to:
   - Remove the "Coming Soon" badge from `roasted-heirloom-tomato-sauce`, `new-hampshire-mushroom-taleggio`, and `clam-pie-new-england-way` — replace with a live "Read recipe →" link matching the existing dough card style.
   - Add two new cards for `pesto-mozzarella-basil` and `chicken-bacon-ranch` in the same card format as the existing recipes.

3. **Match the existing card format exactly** — use the same CSS classes, card layout, and metadata display (prep time, cook time, yield) as the `72-hour-cold-ferment-dough` card. Each recipe's frontmatter contains `prepTime`, `cookTime`, and `yield` fields.

4. **No draft flag set to true** — all five are `draft: false` and ready to publish.

5. **Commit and deploy** once all files are added and the Recipes page is updated.

## Voice note
All recipes are written in "we" voice to match the rest of the site. Do not change the voice or edit the recipe prose.

## Internal links
Internal links in the recipe files use relative paths like `/recipes/72-hour-cold-ferment-dough` and `/blog/pizza-night-recipes-beyond-margherita`. Update these to match actual slugs in the site if they differ.
