#!/usr/bin/env bash
# setup-fonts.sh
# Downloads Anton and Barlow Condensed woff2 files for local @font-face use.
# Run once from the nec-reel/ directory before rendering.

set -e
mkdir -p fonts

echo "⬇  Fetching Anton woff2 URL from Google Fonts..."
ANTON_CSS=$(curl -s -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36" \
  "https://fonts.googleapis.com/css2?family=Anton&display=swap")
ANTON_URL=$(echo "$ANTON_CSS" | grep -o 'https://fonts.gstatic.com/[^)]*\.woff2' | head -1)

if [ -z "$ANTON_URL" ]; then
  echo "  ✗ Could not fetch Anton URL — check network and retry"
  exit 1
fi
echo "  → $ANTON_URL"
curl -s "$ANTON_URL" -o fonts/Anton-Regular.woff2
echo "  ✓ Anton saved"

echo ""
echo "⬇  Fetching Barlow Condensed woff2 URLs from Google Fonts..."
BARLOW_CSS=$(curl -s -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36" \
  "https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&display=swap")

BARLOW600_URL=$(echo "$BARLOW_CSS" | grep -B5 "font-weight: 600" | grep -o 'https://fonts.gstatic.com/[^)]*\.woff2' | head -1)
BARLOW700_URL=$(echo "$BARLOW_CSS" | grep -B5 "font-weight: 700" | grep -o 'https://fonts.gstatic.com/[^)]*\.woff2' | head -1)

if [ -z "$BARLOW600_URL" ] && [ -z "$BARLOW700_URL" ]; then
  echo "  ✗ Could not fetch Barlow Condensed URLs — check network and retry"
  exit 1
fi

if [ -n "$BARLOW600_URL" ]; then
  echo "  → $BARLOW600_URL"
  curl -s "$BARLOW600_URL" -o fonts/BarlowCondensed-SemiBold.woff2
  echo "  ✓ Barlow Condensed 600 saved"
fi

if [ -n "$BARLOW700_URL" ]; then
  echo "  → $BARLOW700_URL"
  curl -s "$BARLOW700_URL" -o fonts/BarlowCondensed-Bold.woff2
  echo "  ✓ Barlow Condensed 700 saved"
fi

echo ""
echo "✅  Fonts ready in fonts/"
ls -lh fonts/
