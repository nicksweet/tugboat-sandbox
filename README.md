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
tugboat plan --feature <feature-name> [--output <output-dir>]
```

**Example usage**
```bash
# Plan a new feature called "feature/auth"
tugboat plan --feature feature/auth --output ./plan
```