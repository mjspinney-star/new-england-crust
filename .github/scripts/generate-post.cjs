// New England Crust — weekly draft post generator.
//
// What changed (2026-09-28 rewrite, after the indexing audit):
//   * Posts are written as DRAFTS (draft: true). Nothing publishes until a
//     human reviews it and flips draft to false.
//   * Topics come from an explicit queue with fixed slugs. A topic is skipped
//     if its file already exists or its slug was retired (merged/redirected),
//     so a merged post can never be regenerated at a redirected URL.
//   * The prompt carries the owner's real facts (one oven, real routine) and
//     forbids invented first-hand experience and other-oven directions.
//   * Every post must link to 2+ existing pages given per topic.
//   * Hard-stop validation: if the output fails the checks twice, the script
//     exits non-zero, nothing is committed, and GitHub emails a failed run.
//
// Local dry run (no API call, prints the selected topic and prompt):
//   DRY_RUN=1 node .github/scripts/generate-post.cjs

const https = require('https');
const fs = require('fs');
const path = require('path');

const BLOG_DIR = 'src/content/blog';
const RECIPE_DIR = 'src/content/recipes';

// ── RETIRED SLUGS ──────────────────────────────────────────────────────────
// Posts that were merged into other pages and now 301-redirect (see
// public/_redirects). Never regenerate these.
const RETIRED = new Set([
  'white-pizza-with-ricotta-garlic-and-lemon',
  'hot-honey-pepperoni-the-simplest-pizza-worth-making-twice-a-week',
  'fig-prosciutto-and-arugula-pizza-how-to-balance-the-sweet-and',
  'mushroom-pizza-with-thyme-and-fontina-a-fall-patio-pizza',
  'breakfast-pizza-for-the-morning-after-pizza-night-what-to-do',
  'pesto-base-pizza-how-to-keep-it-from-burning-at-high-heat',
  'apple-gorgonzola-and-walnut-pizza-a-fall-flavor-combination',
  'a-same-day-pizza-dough-for-nights-when-you-forgot-to-plan-ahead',
]);

// ── TOPIC QUEUE ────────────────────────────────────────────────────────────
// Worked top to bottom. Each topic: a fixed slug, a type, the brief, and the
// existing pages the post MUST link to. Only add topics that (1) no existing
// page already covers and (2) can be written honestly from OWNER FACTS or as
// general guidance — never topics that need experience the owner hasn't had.
const topics = [
  {
    slug: 'how-we-cook-pizza-on-the-ninja-woodfire',
    type: 'technique',
    topic: 'How we cook pizza on the Ninja Woodfire: 550°F, a par-baked crust, and about five minutes — and why each step matters',
    links: ['/blog/72-hour-cold-ferment-dough/', '/blog/pizza-night-recipes-beyond-margherita/', '/blog/best-outdoor-pizza-ovens-under-500/'],
  },
  {
    slug: 'gifts-for-ninja-woodfire-owners',
    type: 'gear',
    topic: 'Gifts for a Ninja Woodfire owner — the accessories that are actually useful, based on what we use and recommend',
    links: ['/blog/ninja-woodfire-accessories-worth-buying/', '/blog/best-pizza-accessories-under-50/', '/gear/'],
  },
  {
    slug: 'pizza-stocking-stuffers-under-25',
    type: 'gear',
    topic: 'Stocking stuffers under $25 for a backyard pizza cook',
    links: ['/blog/best-pizza-accessories-under-50/', '/blog/ninja-woodfire-accessories-worth-buying/'],
  },
  {
    slug: 'how-to-host-a-holiday-pizza-night',
    type: 'hosting',
    topic: 'How to host a holiday pizza night — dough timing, a toppings bar, and keeping pizzas coming when it is cold out',
    links: ['/blog/backyard-pizza-night-setup/', '/blog/pizza-night-recipes-beyond-margherita/', '/blog/72-hour-cold-ferment-dough/'],
  },
  {
    slug: 'new-england-pizza-styles-guide',
    type: 'guide',
    topic: 'A guide to New England pizza styles — New Haven apizza, South Shore bar pizza, Greek pizza, Rhode Island bakery pizza, beach pizza, and the clam pie — what makes each one distinct',
    links: ['/recipes/new-haven-plain-tomato-pie/', '/recipes/south-shore-bar-pizza/', '/recipes/greek-pizza/', '/recipes/rhode-island-bakery-pizza/', '/recipes/beach-pizza/', '/recipes/clam-pie-new-england-way/'],
  },
  {
    slug: 'extension-cord-for-ninja-woodfire',
    type: 'gear',
    topic: 'Choosing an extension cord for the Ninja Woodfire — why the gauge and outdoor rating matter, and what length to buy',
    links: ['/blog/ninja-woodfire-accessories-worth-buying/', '/gear/'],
  },
  {
    slug: 'why-pizza-bottoms-come-out-soggy',
    type: 'technique',
    topic: 'Why pizza bottoms come out soggy and how to fix it — stone temperature, sauce, toppings, and par-baking',
    links: ['/blog/2026-06-16-reading-your-stone-with-an-infrared-thermometer/', '/blog/a-no-cook-tomato-sauce-that-does-not-need/', '/blog/72-hour-cold-ferment-dough/'],
  },
  {
    slug: 'which-mozzarella-for-pizza',
    type: 'ingredient',
    topic: 'Which mozzarella to use on pizza — low-moisture vs. fresh, and how to keep fresh mozzarella from pooling water',
    links: ['/blog/pizza-night-recipes-beyond-margherita/', '/recipes/neapolitan-margherita/'],
  },
  {
    slug: 'how-to-sauce-a-pizza',
    type: 'technique',
    topic: 'How to sauce a pizza — how much, how thin, and why less is almost always more',
    links: ['/blog/a-no-cook-tomato-sauce-that-does-not-need/', '/blog/buying-good-canned-tomatoes-without-overthinking/'],
  },
  {
    slug: 'heat-resistant-gloves-for-pizza-ovens',
    type: 'gear',
    topic: 'Heat-resistant gloves for an outdoor pizza oven — what the temperature ratings mean and what makes a bad pair dangerous',
    links: ['/gear/', '/blog/ninja-woodfire-accessories-worth-buying/'],
  },
];

// ── OWNER FACTS ────────────────────────────────────────────────────────────
// The ONLY first-hand experience the writer may claim. Update this list when
// something new is true; never let the model fill gaps.
const OWNER_FACTS = `
- We own exactly one outdoor oven: a Ninja Woodfire OO101 (electric, 105–700°F, wood pellets add smoke flavor only — they do not heat the oven). We have owned it for over a year and have had no real problems with it.
- We chose it over gas and wood-pellet pizza ovens for ease of use: it plugs in, with no propane and no fire to tend.
- Our pizza routine: preheat to 550°F (about 20 minutes); confirm the stone reads about 540°F with an infrared thermometer; brush the stretched dough with oil and par-bake it for about 1 minute 30 seconds; add toppings; bake about 5 minutes. We do NOT rotate, turn, or flip the pizza.
- The Ninja also has a 700°F setting: we have measured the stone at about 695°F on it, and a pizza cooks in about 3 minutes. We typically use 550°F. (Do not say whether we par-bake on the 700°F setting.)
- Fully preheated, the stone reads close to the set temperature (about 540°F at 550°F; about 695°F at 700°F).
- The result is an evenly golden crust with some blistering on the edge — not leopard-spotted Neapolitan char.
- Our dough: Caputo Pizzeria 00 flour 500 g, cool water 325 g, Baleine fine sea salt 13 g, Caputo Lievito dry yeast 1.5 g, optional olive oil; mixed on the Dough cycle of a Cuisinart CBK-110 bread maker; divided into 250–300 g balls, set in a floured proofing tray, covered, and cold-fermented in the fridge for 24–48 hours.
- We have smoked pulled pork and chicken on the Ninja; both came out tender. (No times or temperatures are known — do not state any.)
- We rotate three pellet flavors: oak, maple, and a cherry blend.
- The oven sits on a Keter Unity cart on our deck. We use the Ninja perforated pizza peel and an infrared thermometer; we also own a turning peel.
- We tested a third-party heavy-duty cover for the Ninja through two months of rain and wind; it held up fine.
- Before owning an infrared thermometer we occasionally got pale bottoms; with it, consistent results.
- We have cooked pizza on many surfaces over the years (cast iron, perforated pans, and others) before settling on the stone.
- Recipes we have made: chicken bacon ranch, pesto mozzarella basil, New Hampshire mushroom taleggio, the clam pie, Salisbury beach pizza, and the grandma pie.
- We are based in coastal New England.`;

// ── SITE PAGES (for linking) ───────────────────────────────────────────────
function readFrontmatter(file) {
  const s = fs.readFileSync(file, 'utf8');
  const m = s.match(/^---\n([\s\S]*?)\n---/);
  if (!m) return null;
  const fm = m[1];
  const title = (fm.match(/^title:\s*"?(.*?)"?\s*$/m) || [])[1];
  const draft = /^draft:\s*true/m.test(fm);
  return title ? { title, draft } : null;
}
function listPages(dir, prefix) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir)
    .filter((f) => /\.mdx?$/.test(f) && !f.startsWith('_'))
    .map((f) => {
      const slug = f.replace(/\.mdx?$/, '');
      const fm = readFrontmatter(path.join(dir, f));
      return fm && !fm.draft ? { slug, url: `${prefix}${slug}/`, title: fm.title } : null;
    })
    .filter(Boolean);
}
const blogPages = listPages(BLOG_DIR, '/blog/');
const recipePages = listPages(RECIPE_DIR, '/recipes/');
const sitePages = [...blogPages, ...recipePages, { url: '/gear/', title: 'Gear — what we actually use' }];
const siteUrls = new Set(sitePages.map((p) => p.url));
const existingBlogSlugs = new Set(
  fs.readdirSync(BLOG_DIR).filter((f) => /\.mdx?$/.test(f)).map((f) => f.replace(/\.mdx?$/, '')),
);

// ── PICK THE NEXT TOPIC ────────────────────────────────────────────────────
const selected = topics.find((t) => !existingBlogSlugs.has(t.slug) && !RETIRED.has(t.slug));
if (!selected) {
  console.log('Topic queue is empty — every topic has been written. Add new topics to generate-post.cjs. Nothing generated.');
  process.exit(0);
}
const missingLinks = selected.links.filter((u) => !siteUrls.has(u));
if (missingLinks.length) {
  console.error(`HARD STOP: topic "${selected.slug}" requires links to pages that don't exist: ${missingLinks.join(', ')}`);
  process.exit(1);
}
console.log(`Selected topic: ${selected.slug}`);

// ── PROMPTS ───────────────────────────────────────────────────────────────
const systemPrompt = `You write for New England Crust, a backyard pizza blog written by a household in coastal New England. Always first-person plural ("we"), never "I". Casual and direct, like explaining something to a curious friend.

HONESTY RULES — THESE OVERRIDE EVERYTHING ELSE:
1. The ONLY first-hand experience you may claim is in OWNER FACTS below. Do not invent anything else we did, saw, cooked, tasted, bought, stopped buying, or learned "the hard way."
2. No invented anecdotes: no friends or guests who did something, no specific nights, parties, or events, no "every time we make this," no "honest quirks" from experience we don't have.
3. Beyond OWNER FACTS, write general guidance in second person ("you"), or clearly general statements ("most cooks," "the usual advice"). Never dress general advice up as our experience.
4. We own only the Ninja Woodfire. Never write cooking directions for, or claim experience with, any other oven. Do not mention Ooni, Koda, Fyra, Solo Stove, Gozney, or any other oven brand at all.
5. Any cooking directions for the Ninja must match OWNER FACTS exactly: our usual 550°F routine, or the 700°F setting described there. Never tell the reader to rotate, turn, or flip the pizza on the Ninja.
6. Do not state prices, product specs, or statistics you are not certain of. If unsure, leave it out.

OWNER FACTS:${OWNER_FACTS}

VOICE:
- Short paragraphs (2–4 sentences). Short declarative sentences for the important points.
- Be upfront about downsides and limits.
- New England is the lens where it fits naturally — short outdoor seasons, cold falls — without inventing specific events.
- Close each major section with a clear takeaway.
- Never use: game changer, next level, elevate, elevated, amazing, absolutely, delicious, "it's that easy", "you won't be disappointed", "perfect" as filler.
- One exclamation point maximum. Em dashes over parentheses.

LINKS — REQUIRED:
- Include EVERY URL in REQUIRED LINKS as a markdown link inside the body text, with natural descriptive anchor text (not "click here"), where it genuinely helps the reader.
- You may also link other pages from SITE PAGES if genuinely relevant. Never link any URL that is not in those lists. No external links. No affiliate links or placeholder tokens — affiliate links are added editorially.
- Do not write a "Related posts" section.

STRUCTURE:
1. Open with a specific, honest statement of the problem or question — not a definition or a history lesson.
2. Short sections with ## subheadings.
3. End with a short "Try this next" section that points to one of the linked pages.

FRONTMATTER — EXACTLY THIS FORMAT:
---
title: "Post title here"
description: "One sentence summary under 155 characters, written for a person"
pubDate: DATE
category: CATEGORY
tags: [tag1, tag2, tag3]
relatedPosts: []
draft: true
---

LENGTH: 500 to 800 words of body text.
OUTPUT: Markdown only. Start with the frontmatter and end with the last line of the post. No preamble.`;

const today = new Date().toISOString().split('T')[0];
const pageList = sitePages.map((p) => `- ${p.url} — ${p.title}`).join('\n');
const userPrompt = `Write a draft post for New England Crust.

Type: ${selected.type}
Topic: ${selected.topic}
pubDate: ${today}
category: ${selected.type}

REQUIRED LINKS (every one must appear in the body as a markdown link):
${selected.links.map((u) => `- ${u}`).join('\n')}

SITE PAGES (the only other URLs you may link; also the only slugs allowed in relatedPosts, using the part after /blog/ without slashes):
${pageList}

Follow the honesty rules above all else. Output only the Markdown post.`;

if (process.env.DRY_RUN) {
  console.log('\n--- SYSTEM PROMPT ---\n' + systemPrompt + '\n\n--- USER PROMPT ---\n' + userPrompt);
  process.exit(0);
}

// ── VALIDATION (hard stops) ────────────────────────────────────────────────
const BANNED = /\b(ooni|koda|fyra|solo stove|gozney|roccbox)\b/i;
const ROTATE = /\b(rotat(e|ing|ion)|turn(ing)? (it|the pizza|the pie)|flip(ping)? (it|the pizza|the pie))\b/i;
const NEGATED_ROTATE = /\b(no|not|never|don't|do not|without)\b[^.]{0,40}\b(rotat|turn|flip)/i;

function validate(text) {
  const problems = [];
  const fmMatch = text.match(/^---\n([\s\S]*?)\n---\n/);
  if (!fmMatch) return { ok: false, problems: ['missing or malformed frontmatter'] };
  const fm = fmMatch[1];
  const body = text.slice(fmMatch[0].length);
  if (!/^title:\s*".+"/m.test(fm)) problems.push('frontmatter title missing');
  if (!/^description:\s*".+"/m.test(fm)) problems.push('frontmatter description missing');
  if (BANNED.test(text)) problems.push(`mentions another oven brand: "${text.match(BANNED)[0]}"`);
  for (const sentence of body.split(/(?<=[.!?])\s+/)) {
    if (ROTATE.test(sentence) && !NEGATED_ROTATE.test(sentence)) {
      problems.push(`tells the reader to rotate/turn/flip: "${sentence.trim().slice(0, 120)}"`);
      break;
    }
  }
  if (/YOUR-AFFILIATE|amzn\.to|amazon\.com/i.test(text)) problems.push('contains an affiliate link or placeholder');
  for (const u of selected.links) {
    if (!body.includes(`](${u})`)) problems.push(`required link missing: ${u}`);
  }
  const linked = [...body.matchAll(/\]\((\/[^)\s]*)\)/g)].map((m) => m[1]);
  const unknown = linked.filter((u) => !siteUrls.has(u));
  if (unknown.length) problems.push(`links to pages that don't exist: ${unknown.join(', ')}`);
  if (/\]\(https?:\/\//.test(body)) problems.push('contains an external link');
  const words = body.split(/\s+/).filter(Boolean).length;
  if (words < 400 || words > 1000) problems.push(`body is ${words} words (expected 500–800)`);
  return { ok: problems.length === 0, problems };
}

// Force the fields we never want the model to control.
function normalize(text) {
  const fmMatch = text.match(/^---\n([\s\S]*?)\n---\n/);
  let fm = fmMatch[1];
  const set = (key, value) => {
    const re = new RegExp(`^${key}:.*$`, 'm');
    fm = re.test(fm) ? fm.replace(re, `${key}: ${value}`) : `${fm}\n${key}: ${value}`;
  };
  set('pubDate', today);
  set('category', selected.type);
  set('draft', 'true');
  const rel = (fm.match(/^relatedPosts:\s*\[(.*)\]/m) || [])[1] || '';
  const validRel = rel.split(',').map((s) => s.trim().replace(/^["']|["']$/g, ''))
    .filter((s) => s && existingBlogSlugs.has(s) && !RETIRED.has(s));
  set('relatedPosts', `[${validRel.map((s) => `"${s}"`).join(', ')}]`);
  return `---\n${fm}\n---\n${text.slice(fmMatch[0].length)}`;
}

// ── API ────────────────────────────────────────────────────────────────────
function callClaude(messages) {
  const payload = JSON.stringify({
    model: 'claude-sonnet-4-6',
    max_tokens: 3000,
    system: systemPrompt,
    messages,
  });
  return new Promise((resolve, reject) => {
    const req = https.request({
      hostname: 'api.anthropic.com',
      path: '/v1/messages',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': process.env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01',
        'Content-Length': Buffer.byteLength(payload),
      },
    }, (res) => {
      let data = '';
      res.on('data', (c) => (data += c));
      res.on('end', () => {
        try {
          const r = JSON.parse(data);
          if (r.error) return reject(new Error(JSON.stringify(r.error)));
          resolve(r.content.filter((b) => b.type === 'text').map((b) => b.text).join('').trim());
        } catch (e) { reject(e); }
      });
    });
    req.on('error', reject);
    req.write(payload);
    req.end();
  });
}

(async () => {
  const messages = [{ role: 'user', content: userPrompt }];
  let text = await callClaude(messages);
  let result = validate(text);
  if (!result.ok) {
    console.log('First draft failed validation, retrying once:\n- ' + result.problems.join('\n- '));
    messages.push({ role: 'assistant', content: text });
    messages.push({ role: 'user', content: `That draft failed these checks:\n- ${result.problems.join('\n- ')}\n\nRewrite the full post fixing every problem. Output only the Markdown post.` });
    text = await callClaude(messages);
    result = validate(text);
  }
  if (!result.ok) {
    console.error('HARD STOP: draft failed validation twice. Nothing written.\n- ' + result.problems.join('\n- '));
    process.exit(1);
  }
  const filename = `${BLOG_DIR}/${selected.slug}.mdx`;
  if (fs.existsSync(filename)) {
    console.error(`HARD STOP: ${filename} already exists.`);
    process.exit(1);
  }
  fs.writeFileSync(filename, normalize(text) + '\n');
  console.log(`Draft saved: ${filename}`);
  if (process.env.GITHUB_ENV) fs.appendFileSync(process.env.GITHUB_ENV, `POST_FILENAME=${filename}\n`);
})().catch((err) => {
  console.error('HARD STOP: API request failed:', err.message);
  process.exit(1);
});
