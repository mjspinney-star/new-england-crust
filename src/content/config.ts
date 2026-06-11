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

const recipes = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
    prepTime: z.string().optional(),
    cookTime: z.string().optional(),
    yield: z.string().optional(),
    oven: z.string().optional(),
    category: z.string().optional(),
    heroImage: z.string().optional(),
  }),
});

export const collections = { blog, recipes };
