# New England Crust

A backyard pizza site for New England nights — built with [Astro](https://astro.build) and Tailwind CSS, designed to deploy to Cloudflare Pages.

## Stack

- **Framework:** Astro 4 (static output)
- **Styling:** Tailwind CSS 3 + `@tailwindcss/typography`
- **Content:** Markdown via Astro Content Collections
- **SEO:** per-page meta, Open Graph, Twitter cards, RSS, sitemap, robots.txt
- **Hosting:** Cloudflare Pages

## Getting started

```bash
npm install
npm run dev      # http://localhost:4321
```

Build a production bundle:

```bash
npm run build    # outputs to ./dist
npm run preview  # serve the built site locally
```

## Project structure

```
.
├── public/                 # static assets copied as-is into dist/
│   ├── favicon.svg
│   ├── robots.txt
│   ├── _headers            # Cloudflare Pages headers
│   └── _redirects          # Cloudflare Pages redirects
├── src/
│   ├── components/         # Header, Footer, SEO, PizzaOvenScene
│   ├── content/
│   │   ├── config.ts       # blog collection schema
│   │   └── blog/           # Markdown posts
│   ├── layouts/
│   │   └── BaseLayout.astro
│   ├── pages/
│   │   ├── index.astro
│   │   ├── about/index.astro
│   │   ├── blog/index.astro
│   │   ├── blog/[...slug].astro
│   │   ├── recipes/index.astro
│   │   ├── gear/index.astro
│   │   └── rss.xml.js
│   └── styles/global.css
├── astro.config.mjs
├── tailwind.config.mjs
├── tsconfig.json
└── package.json
```

## Writing a new post

Drop a Markdown file into `src/content/blog/`:

```markdown
---
title: "Your post title"
description: "One- or two-sentence summary."
pubDate: 2026-05-01
tags: ["dough", "fire"]
draft: false
---

Your post body here.
```

Posts with `draft: true` are excluded from the listing, RSS, and sitemap. Slug
defaults to the filename, e.g. `my-post.md` → `/blog/my-post/`.

## Deploying to Cloudflare Pages

Connect your Git repository to Cloudflare Pages and use these settings:

| Setting              | Value           |
| -------------------- | --------------- |
| Framework preset     | Astro           |
| Build command        | `npm run build` |
| Build output directory | `dist`        |
| Root directory       | `/` (default)   |
| Node version         | `20` (or newer) |

The `public/_headers` and `public/_redirects` files are picked up automatically
by Cloudflare Pages and applied at the edge.

Before going live, update `site` in `astro.config.mjs` to your production
domain so canonical URLs, the sitemap, and RSS feed point to the right place.

## SEO notes

- Per-page `<title>` and meta description via `BaseLayout`.
- Open Graph + Twitter card tags (`SEO.astro`).
- Auto-generated `sitemap-index.xml` (via `@astrojs/sitemap`).
- RSS feed at `/rss.xml`.
- `robots.txt` references the sitemap.

For the social sharing image, drop a 1200×630 file at `public/og-image.jpg`.

## License

Code: MIT. Words and recipes: please ask before reproducing.
