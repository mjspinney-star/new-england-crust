#!/bin/bash
# HyperFrames render — Reel 1 from 2026-06-17 scripts

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
REEL_DIR="$PROJECT_DIR/hyperframes/nec-reel"
OUTPUT="$SCRIPT_DIR/reel-reading-your-stone-with-an-infrared-thermometer-2026-06-17.mp4"

echo "=== New England Crust — Reel Render ==="
echo "Source:  $REEL_DIR"
echo "Output:  $OUTPUT"
echo ""

# Extend PATH to cover common npm install locations
export PATH="$HOME/.npm-global/bin:/usr/local/bin:/opt/homebrew/bin:$PATH"

# Find hyperframes (local → global → npx)
HF=""
for p in \
    "$PROJECT_DIR/node_modules/.bin/hyperframes" \
    "$HOME/.npm-global/bin/hyperframes" \
    "/usr/local/bin/hyperframes" \
    "/opt/homebrew/bin/hyperframes" \
    "$(which hyperframes 2>/dev/null)"; do
  if [ -x "$p" ]; then HF="$p"; break; fi
done

if [ -z "$HF" ]; then
  echo "hyperframes not found in PATH — trying via npx..."
  HF="npx --yes hyperframes"
fi

echo "Using: $HF"
echo ""

cd "$REEL_DIR"
$HF render \
  --output "$OUTPUT" \
  --fps 30 \
  --quality standard \
  .

if [ $? -eq 0 ]; then
  echo ""
  echo "✅ Done: $OUTPUT"
  rm -rf "$SCRIPT_DIR"/work-* 2>/dev/null
else
  echo ""
  echo "✗ Render failed — check output above"
fi

echo ""
read -p "Press Enter to close..."
