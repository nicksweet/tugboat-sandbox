#!/usr/bin/env bash
# Create three plan tracker issues for tugboat queue E2E (Features 003–005).
# Requires: OPENROUTER_API_KEY, gh auth, tugboat on PATH.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
  echo "OPENROUTER_API_KEY is not set" >&2
  exit 1
fi

git checkout main
git pull --ff-only

plan_one() {
  local brief_file="$1"
  local labels="$2"
  echo "=== tugboat plan --brief-file $brief_file --labels $labels --yes ==="
  tugboat plan --brief-file "$brief_file" --labels "$labels" --yes
  echo
}

plan_one drafts/003-fix-readme-cli-examples.md P1
plan_one drafts/004-add-contributing-md.md P2
plan_one drafts/005-add-queue-runbook-docs.md P2

echo "Done. Open trackers:"
gh issue list --repo nicksweet/tugboat-sandbox --label P1 --label P2 --state open
