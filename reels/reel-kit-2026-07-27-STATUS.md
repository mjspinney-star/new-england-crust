# Reel Content Kit — Weekly Run, 2026-07-27

## No new reel kit generated this run

**Finding:** The most recent blog post by `pubDate` is still
`2026-07-20-canned-vs-fresh-clams-for-new-england-white-clam-p.md`
("Canned vs. Fresh Clams for New England White Clam Pizza"). No post has
published since then.

That's the same source post last week's run already used —
`reel-kit-2026-07-21.md` and `reel-canned-vs-fresh-clams-2026-07-21.mp4`
already exist for it. Regenerating another kit from the same post would
just duplicate that content, so I stopped short of writing new scripts
or rendering a new MP4 rather than ship a repeat.

## Likely cause: the publishing pipeline has stalled

Per `CLAUDE.md`, the GitHub + Claude API automation is supposed to
publish a new post every Monday and Thursday. Git history shows the
last auto-generated post landed 2026-07-20 (a Monday) — two scheduled
publish dates have been missed since:

- Thursday, 2026-07-23 — no post
- Monday, 2026-07-27 (today) — no post

## Recommended next step

Check the GitHub Action / Claude API publishing pipeline for a stalled
run or failed job before the next scheduled reel-kit run (next Tuesday).
Once a new post lands, the following week's run will pick it up
normally.

No files were created or modified in `src/content/blog/`,
`hyperframes/nec-reel/content/`, or as new `.mp4` / `.command` outputs
this run.
