const https = require('https');
const fs = require('fs');

// ── TOPIC BANK ─────────────────────────────────────────────────────────────
const topics = [

  // ── TECHNIQUE ────────────────────────────────────────────────────────────
  { type: 'technique', topic: 'How to stretch dough without tearing it — and what to do when you do tear it' },
  { type: 'technique', topic: 'Why your pizza bottom comes out soggy and how to fix it' },
  { type: 'technique', topic: 'Reading your stone with an infrared thermometer — what the numbers actually mean' },
  { type: 'technique', topic: 'How to manage a two-pizza rotation so nothing gets cold' },
  { type: 'technique', topic: 'Cold fermentation explained — what actually happens in the fridge overnight' },
  { type: 'technique', topic: 'How to build a cornicione that puffs — what most home cooks skip' },
  { type: 'technique', topic: 'Launching a pizza without a peel — the methods that actually work and the ones that do not' },
  { type: 'technique', topic: 'How to sauce a pizza properly — thickness, spread, and why less is almost always more' },
  { type: 'technique', topic: 'Preheating your outdoor oven in cold weather — what changes and what to watch for' },
  { type: 'technique', topic: 'How to tell when your dough is actually ready to open — the signs most beginners miss' },
  { type: 'technique', topic: 'Why rotating the pizza during the cook matters and when to do it' },
  { type: 'technique', topic: 'Shaping by hand vs. rolling pin — what you actually lose when you roll' },

  // ── INGREDIENT ───────────────────────────────────────────────────────────
  { type: 'ingredient', topic: 'The difference between 00 flour and bread flour — which to use when' },
  { type: 'ingredient', topic: 'San Marzano vs. regular canned tomatoes — is the price difference worth it' },
  { type: 'ingredient', topic: 'Which mozzarella actually melts right and which ones pool water on your pizza' },
  { type: 'ingredient', topic: 'Finishing with good olive oil — when it matters and when it does not' },
  { type: 'ingredient', topic: 'Fresh basil vs. dried — the honest answer for outdoor pizza cooking' },
  { type: 'ingredient', topic: 'What yeast to buy for pizza dough — instant, active dry, or fresh' },
  { type: 'ingredient', topic: 'Why salt timing matters in pizza dough — and what happens if you rush it' },
  { type: 'ingredient', topic: 'The case for semolina on the peel — what it does that flour cannot' },
  { type: 'ingredient', topic: 'Pecorino vs. Parmigiano — when each belongs on a pizza and when neither does' },
  { type: 'ingredient', topic: 'Hot honey on pizza — when it works and when it overwhelms everything else' },
  { type: 'ingredient', topic: 'Canned vs. fresh clams for New England white clam pizza — an honest comparison' },
  { type: 'ingredient', topic: 'Buying good canned tomatoes without overthinking it — what to look for on the label' },

  // ── RECIPE ───────────────────────────────────────────────────────────────
  { type: 'recipe', topic: 'A no-cook tomato sauce that does not need simmering' },
  { type: 'recipe', topic: 'White pizza with ricotta, garlic, and lemon' },
  { type: 'recipe', topic: 'A same-day pizza dough for nights when you forgot to plan ahead' },
  { type: 'recipe', topic: 'Grilled corn and poblano pizza — a late-summer backyard pie worth making once a season' },
  { type: 'recipe', topic: 'Hot honey pepperoni — the simplest pizza worth making twice a week' },
  { type: 'recipe', topic: 'Fig, prosciutto, and arugula pizza — how to balance the sweet and the bitter' },
  { type: 'recipe', topic: 'Mushroom pizza with thyme and fontina — a fall patio pizza' },
  { type: 'recipe', topic: 'A smash-style sausage and fennel pizza for cold October nights' },
  { type: 'recipe', topic: 'Breakfast pizza for the morning after pizza night — what to do with leftover dough' },
  { type: 'recipe', topic: 'A simple anchovy and olive pizza that skeptics end up eating most of' },
  { type: 'recipe', topic: 'Pesto base pizza — how to keep it from burning at high heat' },
  { type: 'recipe', topic: 'Apple, gorgonzola, and walnut pizza — a fall flavor combination worth trying' },

  // ── GEAR ─────────────────────────────────────────────────────────────────
  { type: 'gear', topic: 'Why a cheap pizza stone still beats an expensive pan' },
  { type: 'gear', topic: 'Cover vs. no cover — what actually happens to an outdoor oven left uncovered in New England' },
  { type: 'gear', topic: 'Extension cord basics for the Ninja Woodfire — because the included cord is too short' },
  { type: 'gear', topic: 'The Ninja Woodfire vs. a gas oven — what the smoke flavor difference actually tastes like' },
  { type: 'gear', topic: 'Which pellet blends we actually use on the Ninja Woodfire — and which ones we stopped buying' },
  { type: 'gear', topic: 'Infrared thermometers for pizza — what to look for and what you can ignore on the spec sheet' },
  { type: 'gear', topic: 'A dough scraper is the most underrated tool on the prep table — here is why' },
  { type: 'gear', topic: 'Pizza steel vs. pizza stone — the actual difference for outdoor oven cooking' },
  { type: 'gear', topic: 'The grill cart question — official Ninja stand vs. a third-party cart for the OO101' },
  { type: 'gear', topic: 'Heat-resistant gloves worth buying — and what makes a bad pair dangerous' },
  { type: 'gear', topic: 'Storing your outdoor oven through a New England winter — what we do and what we skip' },
];

// Pick topic based on number of existing posts (cycles through the list)
const existingPosts = fs.readdirSync('src/content/blog').filter(f => f.endsWith('.md') || f.endsWith('.mdx'));
const topicIndex = existingPosts.length % topics.length;
const selected = topics[topicIndex];

console.log(`Selected topic (${topicIndex}): ${selected.topic}`);

// ── PROMPTS ───────────────────────────────────────────────────────────────
const systemPrompt = `You are the writer behind New England Crust, a pizza and outdoor cooking blog run by a small team of backyard cooks based in New England. You write in first-person plural — always "we," never "I." The voice is casual and direct, like explaining something to a friend who is genuinely curious but does not want to be lectured.

VOICE & TONE — FOLLOW THESE PATTERNS EXACTLY:

Short declarative sentences land the important stuff. Use them alone for emphasis, then follow with context. Example: "The bench scraper is the most underrated tool on this table."

Be honest about downsides upfront — do not bury them. Readers trust honesty more than polish. Example: "We want to be upfront about something: the Ninja Woodfire is not a Neapolitan pizza oven. But if you want..."

Second-person address is natural and specific. "You will learn this after two or three cooks." Not "one will notice."

Use em dashes for asides and punchy qualifiers. Example: "A bench scraper — it costs about eight dollars — lifts stuck dough, portions off pieces, and cleans the board in one swipe."

New England is the lens, not just the location. Cold winters, short outdoor seasons, October sessions with a hoodie on, nor'easters, backyard patios that get maybe five good months a year. Reference this naturally where it fits.

Verdicts and takeaways close sections. Each major section ends with a single clear statement. No hedging at the close.

Lists read like real notes, not ad copy. No "amazing," no "perfect for." Just what it does and why it matters.

WORDS AND PHRASES TO NEVER USE:
game changer, next level, elevate, elevated, amazing, absolutely, perfect (as filler), simple (when describing something requiring skill), delicious, "it's that easy", "you won't be disappointed"

PUNCTUATION AND FORMATTING:
- Short paragraphs: 2 to 4 sentences maximum
- Em dashes over parentheses for asides
- One exclamation point maximum per post — use sparingly
- Subheadings for each major section
- Bold for key terms or tools introduced for the first time
- Affiliate link placeholders formatted as: *[Affiliate link: Product name — Retailer]*

POST STRUCTURE — FOLLOW THIS EVERY TIME:
1. Open with a specific situation, observation, or honest statement — not a definition or history lesson
2. Build into main content using short sections with subheadings
3. Where relevant, include a real-world quirks or honest assessment section
4. Close each major section with a clear verdict or takeaway
5. End with a practical next step or a brief related posts block

FRONTMATTER — REQUIRED ON EVERY POST — FORMAT EXACTLY AS FOLLOWS:
---
title: "Post title here"
description: "One sentence SEO summary under 155 characters, written for a human not a robot"
pubDate: DATE_PLACEHOLDER
category: CATEGORY_PLACEHOLDER
tags: [tag1, tag2, tag3]
draft: false
---

AFFILIATE MENTIONS — ONLY WHEN GENUINELY RELEVANT:
Mention these products the way you would recommend something to a friend — briefly and honestly, never like an ad:
- Ooni Koda 12: portable propane oven, 60 to 90 second Neapolitan cooks, ~950F max
- Ooni Fyra 12: wood pellet version of the Koda, best for wood-fire purists
- Solo Stove Pi: forgiving cook, good for families and beginners, ~900F max
- Ninja Woodfire OO101: electric plus wood pellets, 700F max, best for outdoor cooking generalists who want pizza AND a smoker
Always include a placeholder affiliate link: *[Affiliate link: Product name — Retailer]*

LENGTH: 400 to 600 words total including frontmatter.
OUTPUT: Markdown only. No preamble. No explanation. Start with the frontmatter block and end with the last line of post content.`;

const today = new Date().toISOString().split('T')[0];
const userPrompt = `Write a publish-ready blog post for New England Crust.

Post type: ${selected.type}
Topic: ${selected.topic}

Use ${today} as the pubDate value in the frontmatter.
Use ${selected.type} as the category value in the frontmatter.

Follow all voice, structure, length, and frontmatter rules exactly. Output only the Markdown post — nothing else.`;

// ── API CALL ──────────────────────────────────────────────────────────────
const payload = JSON.stringify({
  model: 'claude-sonnet-4-6',
  max_tokens: 1500,
  system: systemPrompt,
  messages: [{ role: 'user', content: userPrompt }]
});

const options = {
  hostname: 'api.anthropic.com',
  path: '/v1/messages',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'x-api-key': process.env.ANTHROPIC_API_KEY,
    'anthropic-version': '2023-06-01',
    'Content-Length': Buffer.byteLength(payload)
  }
};

const req = https.request(options, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    const response = JSON.parse(data);

    if (response.error) {
      console.error('API error:', response.error);
      process.exit(1);
    }

    const postContent = response.content[0].text;

    // Filename: YYYY-MM-DD-post-type-topic-slug.md
    const slug = selected.topic
      .toLowerCase()
      .replace(/[^a-z0-9\s-]/g, '')
      .replace(/\s+/g, '-')
      .slice(0, 50);

    const filename = `src/content/blog/${today}-${slug}.md`;
    fs.writeFileSync(filename, postContent);
    console.log('Post saved to: ' + filename);

    fs.appendFileSync(process.env.GITHUB_ENV, `POST_FILENAME=${filename}\n`);
  });
});

req.on('error', (err) => {
  console.error('Request error:', err);
  process.exit(1);
});

req.write(payload);
req.end();
