## Problem

Root README lacks a mission statement section required for doc standards.

## File map

| File | Role |
|------|------|
| `README.md` | **Write** |

## Deliverable

Add a `## Mission` section with one sentence describing the sandbox repo purpose.

## Requirements

- [ ] README contains `## Mission` heading
- [ ] Mission text mentions intake testing

## Agent execution protocol

1. Diagnose — read `README.md`
2. Change — add `## Mission` section
3. Self-check — grep for `## Mission` in README
4. Stop — ## Summary

## Verification

```bash
grep -q '## Mission' README.md
grep -q 'intake' README.md
```

## Out of scope

- AGENTS.md, MERMAID.mmd (Tier 3 doc audit)
- Code changes beyond README
