#!/usr/bin/env bash
# Bootstrap Feature 008 E2E fleet workspace when plan gates fail on frontier file-map format.
# Creates features/003-fleet-workspace-e2e/ with promoted specs and tracker issue.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNS="${TUGBOAT_RUNS:-/home/nick/tugboat/runs}"
PROJECT="tugboat-sandbox"
NUM="003"
SLUG="fleet-workspace-e2e"
WS="$RUNS/$PROJECT/features/${NUM}-${SLUG}"
PLAN_RUN_ID="2026-07-02T03-40-00Z"
BRANCH="feature/${NUM}-${SLUG}"
SPEC_ROOT="features/${NUM}-${SLUG}/specs"
REPO="nicksweet/tugboat-sandbox"

mkdir -p "$WS/plan/runs/$PLAN_RUN_ID/branch_artifacts/$SPEC_ROOT/tasks"
mkdir -p "$WS/specs/tasks"

cat > "$WS/specs/spec.md" <<'EOF'
# Spec: fleet-workspace-e2e

Feature 008 fleet workspace E2E validation marker.

## Acceptance

- [ ] Feature acceptance per task gates
EOF

cat > "$WS/specs/plan.md" <<'EOF'
# Plan: fleet-workspace-e2e

Manual bootstrap for T062 when frontier file-map uses table headers.
EOF

cat > "$WS/specs/tasks.md" <<'EOF'
# Tasks: fleet-workspace-e2e

| ID | Title | Tier | Depends |
|----|-------|------|--------|
| T001 | Create e2e-marker doc | simple | — |
| T002 | Add README fleet E2E section | simple | T001 |
EOF

cat > "$WS/specs/tasks/T001.md" <<'EOF'
## Problem

Missing docs/fleet-workspace/e2e-marker.md for Feature 008 E2E validation.

## File map

- **Write** `docs/fleet-workspace/e2e-marker.md`

## Deliverable

Create e2e-marker.md with title and fleet workspace validation paragraph.

## Requirements

- [ ] File docs/fleet-workspace/e2e-marker.md exists
- [ ] Contains heading Feature 008 E2E

## Agent execution protocol

1. **Diagnose** — confirm file missing
2. **Change** — write docs/fleet-workspace/e2e-marker.md
3. **Self-check** — grep verify
4. **Stop** — ## Summary

## Verification

```bash
grep -q 'Feature 008 E2E' docs/fleet-workspace/e2e-marker.md && grep -qi 'fleet workspace' docs/fleet-workspace/e2e-marker.md
```

## Out of scope

README changes (T002)
EOF

cat > "$WS/specs/tasks/T002.md" <<'EOF'
## Problem

README lacks pointer to fleet workspace E2E marker doc.

## File map

- **Write** `README.md`

## Deliverable

Add ## Fleet workspace E2E section with link to docs/fleet-workspace/e2e-marker.md.

## Requirements

- [ ] README mentions Fleet workspace E2E
- [ ] README references e2e-marker.md

## Agent execution protocol

1. **Diagnose** — read README.md
2. **Change** — append fleet E2E section
3. **Self-check** — grep verify
4. **Stop** — ## Summary

## Verification

```bash
grep -qi 'Fleet workspace E2E' README.md && grep -q 'e2e-marker.md' README.md
```

## Out of scope

Other files
EOF

cp -a "$WS/specs/." "$WS/plan/runs/$PLAN_RUN_ID/branch_artifacts/$SPEC_ROOT/"

cat > "$WS/feature.json" <<EOF
{
  "feature_num": "$NUM",
  "short_name": "$SLUG",
  "branch_name": "$BRANCH",
  "project_id": "$PROJECT",
  "tracker_issue_number": null,
  "tracker_issue_url": null,
  "status": "planned",
  "approved_plan_run_id": "$PLAN_RUN_ID",
  "workspace_path": "$PROJECT/features/${NUM}-${SLUG}"
}
EOF

BRIEF="$(cat "$ROOT/drafts/008-e2e-brief.md")"
BODY=$(cat <<EOF
## Problem

${BRIEF}

## Branch

${BRANCH}

## Spec root

${SPEC_ROOT}/

## Tasks

2 tasks — see ${SPEC_ROOT}/tasks.md and ${SPEC_ROOT}/tasks/T001.md, ${SPEC_ROOT}/tasks/T002.md

## Status

planned
EOF
)

ISSUE_URL=$(gh issue create --repo "$REPO" --title "Plan: ${SLUG}" --body "$BODY" --label P2)
ISSUE_NUM=$(echo "$ISSUE_URL" | grep -oE '[0-9]+$')
echo "Created issue #$ISSUE_NUM: $ISSUE_URL"

python3 <<PY
import json
from pathlib import Path
p = Path("$WS/feature.json")
d = json.loads(p.read_text())
d["tracker_issue_number"] = int("$ISSUE_NUM")
d["tracker_issue_url"] = "$ISSUE_URL"
p.write_text(json.dumps(d, indent=2) + "\n")
PY

echo "Workspace: $WS"
echo "Issue: #$ISSUE_NUM"
