#!/usr/bin/env bash
# Validate Feature 008 T062 E2E artifacts (run after plan and/or build).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FLEET_RUNS="${TUGBOAT_RUNS:-/home/nick/tugboat/runs}"
PROJECT="${TUGBOAT_PROJECT:-tugboat-sandbox}"
ISSUE="${1:-}"
PR="${2:-}"

FEATURES_DIR="$FLEET_RUNS/$PROJECT/features"
fail() { echo "FAIL: $*" >&2; exit 1; }
ok() { echo "OK: $*"; }

echo "=== T062 validation: $PROJECT ==="

# Scenario 1: managed repo clean after plan (on main)
cd "$ROOT"
branch="$(git rev-parse --abbrev-ref HEAD)"
if [[ "$branch" != "main" ]]; then
  echo "WARN: not on main (on $branch); skipping clean-tree check"
else
  if [[ -n "$(git status --porcelain)" ]]; then
    git status --short
    fail "managed repo working tree not clean on main after plan"
  fi
  ok "managed repo clean on main"
fi

# Fleet workspace exists
if [[ ! -d "$FEATURES_DIR" ]]; then
  fail "no fleet features dir: $FEATURES_DIR"
fi
latest="$(ls -1 "$FEATURES_DIR" 2>/dev/null | sort | tail -1)"
[[ -n "$latest" ]] || fail "no feature workspaces under $FEATURES_DIR"
ws="$FEATURES_DIR/$latest"
ok "fleet workspace: $ws"

[[ -f "$ws/feature.json" ]] || fail "missing feature.json"
grep -q '"approved_plan_run_id"' "$ws/feature.json" || fail "feature.json missing approved_plan_run_id"
[[ -f "$ws/specs/tasks.md" ]] || fail "missing specs/tasks.md"
ok "promoted specs/ present"

# Tracker issue (optional arg)
if [[ -n "$ISSUE" ]]; then
  spec_root="$(gh issue view "$ISSUE" --repo nicksweet/tugboat-sandbox --json body -q .body \
    | python3 -c "import sys,re; b=sys.stdin.read(); m=re.search(r'(?ms)^## Spec root\s*\n+\s*(\S+)', b); print(m.group(1).rstrip('/') if m else '')")"
  [[ -n "$spec_root" ]] || fail "could not parse tracker Spec root for issue #$ISSUE"
  [[ "$spec_root" == features/* ]] || fail "tracker Spec root not fleet path: $spec_root"
  ok "tracker #$ISSUE Spec root: $spec_root"
fi

# Build audit under workspace
build_runs="$ws/build/runs"
if [[ -d "$build_runs" ]]; then
  count="$(find "$build_runs" -name audit.json 2>/dev/null | wc -l)"
  [[ "$count" -ge 1 ]] || fail "no build audit under $build_runs"
  ok "build audit(s): $count under workspace"
else
  echo "WARN: no build/runs yet (run run-feature first)"
fi

# Scenario 3: deliverable-only PR (optional arg)
if [[ -n "$PR" ]]; then
  bad="$(gh pr diff "$PR" --repo nicksweet/tugboat-sandbox --name-only 2>/dev/null \
    | grep -E '^(specs/|features/)' || true)"
  if [[ -n "$bad" ]]; then
    echo "$bad"
    fail "PR #$PR contains plan/fleet paths"
  fi
  # Also verify git merge-base diff (gh pr files can include base-branch files)
  if git rev-parse "origin/feature/003-fleet-workspace-e2e" >/dev/null 2>&1; then
    extra="$(git diff origin/main...origin/feature/003-fleet-workspace-e2e --name-only 2>/dev/null \
      | grep -E '^(specs/|features/)' || true)"
    [[ -z "$extra" ]] || fail "branch diff contains plan/fleet paths: $extra"
  fi
  ok "PR #$PR deliverable-only (no specs/ or features/ paths)"
fi

echo "=== T062 validation passed ==="
