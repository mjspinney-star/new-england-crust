// Converts an ISO 8601 duration (e.g. "PT1H30M") into readable display text
// ("1 hr 30 min"). Display only — JSON-LD / Recipe schema must keep the raw
// ISO string. Returns "" for zero-length (PT0M, PT0S), empty, or unparseable
// input so callers can omit the segment entirely.
export function formatDuration(iso: string | undefined | null): string {
  if (!iso) return '';
  const match = iso.trim().match(/^P(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?)?$/i);
  if (!match) return '';
  const [, d, h, m, s] = match;
  const days = Number(d ?? 0);
  const hours = Number(h ?? 0);
  const minutes = Number(m ?? 0);
  const seconds = Number(s ?? 0);
  const parts: string[] = [];
  if (days) parts.push(`${days} ${days === 1 ? 'day' : 'days'}`);
  if (hours) parts.push(`${hours} hr`);
  if (minutes) parts.push(`${minutes} min`);
  if (seconds && !days && !hours && !minutes) parts.push(`${seconds} sec`);
  return parts.join(' ');
}
