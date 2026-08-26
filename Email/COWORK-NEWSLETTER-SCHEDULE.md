# COWORK SCHEDULED TASK — Weekly Newsletter Draft

**This file mirrors the live task prompt in Cowork → Scheduled → "New England Crust — Weekly Newsletter Draft."**
**The scheduler is authoritative. If you edit one, edit both.**

Runs Monday 9:00 AM. Review and send via ConvertKit same day or Tuesday morning.

---

REPO: /Users/michaelspinney/Desktop/new-england-crust

## Step 0 — Sync the repo view

From the repo directory:

    git fetch origin
    git rev-parse --short origin/main
    find .git -maxdepth 1 -name "*.lock"

If `find .git -maxdepth 1 -name "*.lock"` returns any paths, STOP and report them. Do not attempt to delete them — file deletion is blocked in this sandbox and the attempt will fail. Do not proceed with the rest of the job. A stale lock means a prior run died mid-operation and the repo state cannot be trusted.

Read ALL repo content in this job from `origin/main`, never from the working
tree or local `main`. This checkout is routinely behind.

    git ls-tree --name-only origin/main src/content/blog/
    git show origin/main:src/content/blog/<filename>.mdx
    git show origin/main:email/newsletter-broadcast-template.md

Do NOT run `git pull`, `git reset`, `git checkout`, or any command that writes
to the working tree. File deletion is blocked in this sandbox and these will
fail or leave a stale .git/index.lock behind.

Then create the output directory:

    mkdir -p email/drafts

## Step 1 — Find the source post

Find the most recently published post in src/content/blog/ on origin/main,
using the pubDate frontmatter field. Ignore any post with `draft: true` or a
pubDate in the future.

Before drafting anything, print:
- the source post filename
- its pubDate
- the short SHA from Step 0

## Step 2 — Read the template

Read email/newsletter-broadcast-template.md from origin/main for formatting
and voice guidance.

## Step 3 — Draft the broadcast email

Use the template structure:

- Subject line (under 50 characters, one of the three formats in the template)
- Preview text (one sentence extending the subject)
- Opening paragraph (2-3 sentences — what we cooked or tried, specific and sensory)
- The Thing (3-5 sentences — a genuine tip or lesson pulled from the post,
  useful on its own without clicking)
- Post link line (post title, one-sentence description, full URL with trailing slash)
- Optional affiliate mention (only if a product with a natural fit appears in
  the post — one sentence max, never forced)
- Ember's Pick of the Week (see below)
- Sign-off in the standard format

### Ember's Pick of the Week

A recurring segment between the affiliate mention and the sign-off. 2-3
sentences recommending one product, tool, or recipe from this week's content,
in the blog's plain-spoken first-person-plural voice with light humor about
Ember (mini goldendoodle, self-appointed quality control). Include one relevant
affiliate link where natural.

AFFILIATE LINK RULES — HARD RULE
Amazon Associates links with tag `newenglandcru-20` are permitted ONLY for
non-oven-brand products (accessories, ingredients, unbranded tools) and for
Ninja. NEVER link Ooni or Solo Stove products through Amazon, anywhere in this
email. If the week's natural pick is an Ooni or Solo Stove item, either mention
it in plain text with no link at all, or choose a different pick.

### Voice notes

First-person plural throughout (we/our/us). Short sentences. Sounds like
telling a friend what we cooked, not writing a newsletter. The tip should be
useful on its own without clicking the link.

## Step 4 — Save the draft

Save to email/drafts/newsletter-YYYY-MM-DD.md using today's date.

## Step 5 — Print a summary

- Source post used (filename and pubDate)
- Repo SHA read from
- Subject line chosen
- One sentence on why that tip was picked as "the thing"
- Affiliate links used, with the brand of each, confirming none are Ooni or
  Solo Stove on Amazon
- Lock file check result (none found, or the paths found)

## FACT ACCURACY — HARD RULE

Every number, temperature, time, price, or spec must be traceable to the source
post, WITH its attribution intact. If the post attributes a figure to a specific
oven, the output must name that oven. Never render a bare temperature stripped
of the oven it belongs to.

Reference ceilings: Ninja Woodfire ~700°F air temp, stone surface lower.
Ooni Koda 12 / Fyra ~950°F. Solo Stove Pi ~900°F. Cuisinart 3-in-1 ~900°F.

A figure above 700°F is correct ONLY if attributed to a non-Woodfire oven. If
the source attributes anything above 700°F to the Woodfire, STOP and report.

The same fact must use the same number across every asset in a batch.
Cross-check before rendering. If two disagree, stop and report rather than
picking one.

List every numeric claim used and its source post line at the end of the draft,
so it can be checked before sending.

## Repo settings note

Auto-maintenance is disabled on this repo (`maintenance.auto false`, `gc.auto 0`)
because `git fetch` was regenerating `.git/objects/maintenance.lock` on every run
and the sandbox cannot unlink it. Run `git gc` manually from Terminal every few
weeks to keep loose objects in check.