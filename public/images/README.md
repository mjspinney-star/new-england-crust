# /public/images/

Drop static image assets here. Files in this folder are copied into the
build as-is and served at `/images/<filename>`.

## Hero photo

The homepage hero expects a photo named **`NinjaWoodfireHero.jpeg`** in this
folder. Recommended source dimensions: at least **2400 × 1600 px** (3:2 or
16:9 landscape works best). The dark navy wall and the warm oven glow will
both be preserved by the navy scrim and warm-glow overlay applied in
`src/pages/index.astro`.

If you'd rather have Astro auto-optimize the photo (WebP/AVIF, srcset),
move it to `src/assets/images/NinjaWoodfireHero.jpeg` and swap the
`<img>` tag in the hero for the `<Image>` component — see the comment in
`src/pages/index.astro` for the drop-in snippet.
