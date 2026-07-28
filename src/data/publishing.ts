// Single source of truth for whether a content entry is publicly visible.
// An entry publishes only when it isn't a draft AND its pubDate has arrived.
// The site is statically built (Cloudflare Pages + the Mon/Thu publishing
// automation), so a future-dated entry stays hidden until the first build
// on or after its date — no build means no early publication.
export function isPublished(data: { draft: boolean; pubDate: Date }): boolean {
  return !data.draft && data.pubDate.valueOf() <= Date.now();
}
