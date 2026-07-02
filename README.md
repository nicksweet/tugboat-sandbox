# sandbox

## Mission
Tugboat is a fleet manager for internal LLM-related GitHub projects, covering Tier 1–2 intake and Phase 2 Feature 005.

## How to run tugboat plan
Use `tugboat plan` to decompose a feature into tasks with frontier model assistance.

**Prerequisites**
- Tugboat installed and configured
- Access to a frontier LLM API (e.g., OpenAI, Anthropic)
- A GitHub repository with feature description

**Command syntax**
```bash
tugboat plan --brief "..." --project <id>
```
or
```bash
tugboat plan --brief-file path/to/brief.md [--project <id>] [--plan-only] [--yes]
```

**Example usage**
```bash
# Plan a new feature using a brief string
tugboat plan --brief "Add OAuth2 to the API gateway" --project proj_123

# Plan a new feature using a brief file (with plan-only to generate plan without creating issues)
tugboat plan --brief-file ./docs/feature/brief.md --project proj_123 --plan-only
```

## How to run tugboat create-issue
Use `tugboat create-issue` to create agent-ready GitHub issues from a task plan.

**Prerequisites**
- Tugboat installed and configured
- Either a brief string or a body file (generated from `tugboat plan` or manually)
- Access to GitHub with permissions to create issues

**Command syntax**
```bash
tugboat create-issue --brief "..." [--split] [--dry-run] [--yes]
```
or
```bash
tugboat create-issue --body-file path/to/issue.md [--dry-run] [--title "..."]
```

**Example usage**
```bash
# Validate the plan and preview issues without creating them (dry run) using a brief
tugboat create-issue --brief "Fix login bug" --dry-run

# Validate the plan and preview issues without creating them (dry run) using a body file
tugboat create-issue --body-file drafts/issue.md --dry-run

# Create issues with a brief (non-dry run)
tugboat create-issue --brief "Add OAuth2 to the API gateway" --yes

# Create issues with a body file and a custom title
tugboat create-issue --body-file drafts/issue.md --title "Update API documentation"
```

## How to run tugboat queue
Use `tugboat queue` to process the intake queue and run feature tasks.

**Prerequisites**
- Tugboat installed and configured
- Access to GitHub with permissions to read queue items and update issues

**Command syntax**
```bash
tugboat queue [--dry-run] [--once]
```

**Example usage**
```bash
# Dry run to see what would be processed without making changes
tugboat queue --dry-run

# Process one item from the queue and then exit
tugboat queue --once

# Process the queue continuously (default behavior)
tugboat queue
```

## Tier expectations

Tugboat classifies incoming work into three tiers: simple, standard, and complex.
The tier determines the intake gate behavior and whether the agent-ready label can be applied.

### Tier classification

| Tier | Signals |
|------|---------|
| Simple | Well-defined task, minimal dependencies, clear acceptance criteria |
| Standard | Moderate complexity, may involve multiple components, requires coordination |
| Complex | High ambiguity, significant research or exploration needed, uncertain scope |

### Intake gate behavior

- Simple tiers are automatically admitted to the intake queue.
- Standard tiers require a brief review by a human lead before admission.
- Complex tiers are blocked at the intake gate and must be broken down into simpler tasks before being admitted.

### Agent-ready label blocking

Per the Constitution, the agent-ready label is blocked (i.e., not applied) for any task that:
- Is classified as complex and remains at the intake gate.
- Has outstanding dependencies that are not resolved.
- Lacks clear acceptance criteria or a definition of done.

However, note that the exact blocking conditions may be refined by the project's Constitution.

This blocking logic is referred to as `block_agent_ready` in the implementation.

## Fleet workspace E2E
See the [fleet workspace E2E marker](docs/fleet-workspace/e2e-marker.md) for end-to-end validation.


## Screenplay stress test

This section describes the stress test for the screenplay.
See [screenplay/script.md](screenplay/script.md) for details.