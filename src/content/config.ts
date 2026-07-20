import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    heroImage: z.string().optional(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    relatedPosts: z.array(z.string()).optional(),
  }),
});

// Optional inline photo attached to an instruction step.
const instructionImage = z.object({
  src: z.string(),
  alt: z.string(),
});

// Structured instruction step used by the newer recipe schema (see below).
const instructionStep = z.object({
  step: z.string().optional(),
  text: z.string(),
  images: z.array(instructionImage).optional(),
});

// A single piece of affiliate/owned gear referenced from a recipe
// (e.g. the oven, peel, or tool used to make it).
const gearItem = z.object({
  name: z.string(),
  url: z.string(),
  note: z.string().optional(),
  // Optional id matching src/data/affiliateLinks.ts. When present, the gear
  // card renders the shared <AffiliateLink> component (same styling/badge
  // as the /gear/ page) instead of a plain link to `url`.
  affiliateId: z.string().optional(),
});

const recipes = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    draft: z.boolean().default(false),
    heroImage: z.string().optional(),

    // --- Legacy fields (existing published recipes use these — keep
    // optional so older content keeps validating and rendering as-is) ---
    tags: z.array(z.string()).default([]),
    yield: z.string().optional(),
    oven: z.string().optional(),
    category: z.string().optional(),

    // --- Newer structured schema (recipe card + JSON-LD support) ---
    // "style" is the regional/format label, e.g. "beach-pizza", "bar-pizza",
    // "greek", "new-haven", "neapolitan".
    style: z.string().optional(),
    // ISO 8601 durations, e.g. "PT30M". (Legacy recipes may still use
    // freeform strings like "30 min" in prepTime/cookTime — both are
    // accepted here since this field is shared with the legacy schema.)
    prepTime: z.string().optional(),
    cookTime: z.string().optional(),
    totalTime: z.string().optional(),
    // Dough ferment / rest time, e.g. "P3D" for a 72-hour cold ferment.
    restTime: z.string().optional(),
    servings: z.string().optional(),
    calories: z.number().optional(),
    ingredients: z.array(z.string()).default([]),
    instructions: z.array(instructionStep).default([]),
    // Affiliate/owned gear used in the recipe (Ooni, Ninja Artisan, Solo
    // Stove Pi, etc.). Rendered as a disclosed "Gear I used" callout.
    gear: z.array(gearItem).default([]),
    keywords: z.array(z.string()).default([]),
  }),
});

export const collections = { blog, recipes };
