import { readdirSync, statSync, existsSync, readFileSync, writeFileSync } from 'node:fs';
import { join, relative, sep } from 'node:path';

const DIST = 'dist';
const rules = [];

function walk(dir) {
  for (const name of readdirSync(dir)) {
    const full = join(dir, name);
    if (!statSync(full).isDirectory()) continue;
    if (existsSync(join(full, 'index.html'))) {
      const p = '/' + relative(DIST, full).split(sep).join('/');
      rules.push(`${p} ${p}/ 301`);
    }
    walk(full);
  }
}

walk(DIST);

if (rules.length === 0) {
  console.error('gen-redirects: HARD STOP — zero pages found in dist/. Did astro build run?');
  process.exit(1);
}
if (rules.length > 1900) {
  console.error(`gen-redirects: HARD STOP — ${rules.length} rules, near Cloudflare's 2,000 static redirect cap.`);
  process.exit(1);
}

const file = join(DIST, '_redirects');
const existing = existsSync(file) ? readFileSync(file, 'utf8').trimEnd() + '\n' : '';
writeFileSync(file, existing + rules.sort().join('\n') + '\n');
console.log(`gen-redirects: wrote ${rules.length} rules to ${file}`);
