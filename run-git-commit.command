#!/bin/bash
set -euo pipefail

REPO="/Users/michaelspinney/Desktop/new-england-crust"
cd "$REPO"

if [ $# -lt 2 ]; then
  echo "Usage: $0 \"commit message\" <file> [file...]"
  exit 1
fi

MSG="$1"
shift

if pgrep -x git > /dev/null; then
  echo "ABORT: a git process is running. Not touching lock files."
  exit 1
fi

find .git -name "*.lock" -delete

git status
echo "--- staging: $* ---"
git add -- "$@"
git commit -m "$MSG"
git push origin main

if [ -z "$(git log origin/main..HEAD --oneline)" ]; then
  echo "--- PUSHED OK: $(git rev-parse --short HEAD) ---"
  echo "https://github.com/mjspinney-star/new-england-crust/commit/$(git rev-parse HEAD)"
else
  echo "--- PUSH FAILED: commit is still local ---"
  exit 1
fi
