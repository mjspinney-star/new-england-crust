import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

import cloudflare from "@astrojs/cloudflare";

// https://astro.build/config
export default defineConfig({
  // Update this to your production domain before deploying.
  site: 'https://newenglandcrust.com',

  output: "hybrid",

  integrations: [
    mdx(),
    tailwind({
      applyBaseStyles: true,
    }),
    sitemap(),
  ],

  build: {
    // Cloudflare Pages serves /dist by default; this matches the deploy config.
    format: 'directory',
  },

  adapter: cloudflare()
});