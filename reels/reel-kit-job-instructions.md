# Reel Content Kit — Scheduled Job Instructions

This is a reference copy of the live Tuesday 3:00 PM Cowork scheduled job.
If you edit the job in Cowork's settings, update this file to match.
Last synced: 2026-07-21

---

PART 1 — REEL SCRIPTS

Find the most recent markdown file by pubDate frontmatter field in:
/Users/michaelspinney/Desktop/new-england-crust/src/content/blog/

Read that file only. Write 3 Reel scripts using this exact structure:

---
REEL [N] — "[Short Title]"
Source post: [post title]
Blog URL: newenglandcrust.com/blog/[slug]
Hook style: [mistake/reveal | list/budget | contrarian]
Best posting time: [day and time]

SLIDES
1. [Hook — 2-3 sec] — [slide text]
2. [2-4 sec] — [slide text, headline + subline where appropriate]
3. [2-4 sec] — [slide text, headline + subline where appropriate]
4. [2-4 sec] — [slide text, headline + subline where appropriate]
5. [Close — 3 sec] — Full breakdown → newenglandcrust.com /
   🔥 New England Crust

For list or skip-item slides, format as:
HEADLINE: [list item or skip item]
SUBLINE: [supporting detail or reason]

For hook and payoff slides, format as:
HEADLINE: [single punchy line, no subline]

CAPTION
[2-3 sentence Instagram caption, first person plural,
conversational, no hashtags in caption body]

HASHTAGS
[9-10 hashtags, mix of niche and broad, always end with
#NewEnglandCrust]
---

Keep tone conversational and honest — never promotional.
Headline text should be one punchy sentence, under 10 words
where possible. Hook slide must create curiosity or signal
a mistake.

BEFORE FINALIZING REEL 3 (contrarian): compare its core argument
against Reel 1 (mistake/reveal). If Reel 3's central claim just
restates Reel 1's fact with different wording — even if the hook
sentence sounds different — rewrite Reel 3 around a genuinely
separate angle instead: cost, time/effort, mess/logistics,
ingredient sourcing, availability, or a real counter-argument to
the "obvious" choice. Reel 3 should teach the viewer something
Reel 1 didn't, not just repeat it with more attitude.

Save all 3 scripts to:
/Users/michaelspinney/Desktop/new-england-crust/reels/reel-kit-YYYY-MM-DD.md

Use today's actual date in the filename.

PART 2 — GENERATE REEL

Using Reel 1 from the scripts above, generate an MP4 using
HyperFrames with these exact brand specs:

BRAND SPECS

Colors
- Background: #1B2A3B (deep navy)
- Primary text: #F5F0E8 (warm cream)
- Accent / number highlights: #C4622D (burnt orange)
- Accent line: #C4622D

Typography — two-layer system
- Headline layer: Anton, large, cream, centered
  - For numbered list items: number in #C4622D,
    rest of headline in cream
  - Example: "3." in orange + "A perforated pizza peel." in cream
- Subline layer: Barlow Condensed, smaller, cream, centered
  - Supporting detail or reason
  - Fades in underneath headline after 0.3 sec delay
  - Used on slides with a skip item / list item structure

Single-layer slides (no subline)
- Hook slides (slide 1) — Anton full width, cream
- Payoff/closing slides — Anton full width, cream, no subline
  - Example: "Spend the money on pellets instead."
    gets full Anton, no detail line underneath

Animation
- Headline: fast fade or slide-up
- Subline: fade in 0.3 sec after headline lands
- Background: subtle Ken Burns zoom, scale 1.0 to 1.08
  over full video duration
- Transitions between slides: smooth crossfade 0.5 sec

End card (every Reel, always)
- "FULL BREAKDOWN" small caps #C4622D at top
- Down arrow in cream
- "newenglandcrust.com" large, #C4622D
- Accent line #C4622D
- "NEW ENGLAND CRUST" small caps cream at bottom

Font files are local — reference these paths in @font-face:
/Users/michaelspinney/Desktop/new-england-crust/hyperframes/nec-reel/fonts/Anton-Regular.woff2
/Users/michaelspinney/Desktop/new-england-crust/hyperframes/nec-reel/fonts/BarlowCondensed-SemiBold.woff2
/Users/michaelspinney/Desktop/new-england-crust/hyperframes/nec-reel/fonts/BarlowCondensed-Bold.woff2

Format
- 9:16 vertical, 1080x1920
- 15 seconds for tips Reels
- 20 seconds for brand/launch Reels

OUTPUT
- Save MP4 to:
  /Users/michaelspinney/Desktop/new-england-crust/reels/
- Filename format: reel-[post-slug]-YYYY-MM-DD.mp4
- Use today's actual date in the filename
- Clean up any .mkv or temp files after successful export

Print a summary when done showing:
- Post processed (title and slug)
- Scripts written
- MP4 filename and location
- Any errors encountered
