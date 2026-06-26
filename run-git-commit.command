#!/bin/bash
# Remove all git lock files
find /Users/michaelspinney/Desktop/new-england-crust/.git -name "*.lock" -delete 2>/dev/null
cd /Users/michaelspinney/Desktop/new-england-crust
git add -A
git commit -m "Generated Pinterest pins — 2026-06-26"
echo "--- DONE ---"
