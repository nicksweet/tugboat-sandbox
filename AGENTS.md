# AGENTS.md

## Project Overview

This repository is the sandbox for Tugboat, a fleet manager for internal LLM-related GitHub projects. The mission is to cover Tier 1–2 intake and Phase 2 Feature 005. Tugboat helps decompose features into tasks and create agent-ready GitHub issues.

## tooling

- **Tugboat CLI**: Primary tool for planning and issue creation.
  - `tugboat plan` – Decompose a feature into tasks.
    - Required: exactly one of `--brief` or `--brief-file`.
    - When using `--brief`: required `--project <id>`.
    - When using `--brief-file`: optional `--project <id>`, and optional flags `[--plan-only] [--yes]`.
    - Example: `tugboat plan --brief "Add user login" --project proj123`
    - Example: `tugboat plan --brief-file path/to/brief.md --project proj123 [--plan-only] [--yes]`
  - `tugboat create-issue` – Create GitHub issues from a task plan.
    - Use `--brief` or `--body-file` with optional `--split` for complex bodies.
    - Optional flags: `[--dry-run] [--yes]` for both, and `[--title "..."]` when using `--body-file`.
    - Example: `tugboat create-issue --brief "Implement login endpoint" --split`
    - Example: `tugboat create-issue --body-file drafts/issue.md --title "My Title" [--dry-run] [--yes]`
  - `tugboat run-feature` – Run an approved feature.
    - Required flags: `--project <id> --issue <N>`
    - Optional flags: `[--dry-run] [--continue] [--yes]`
    - Example: `tugboat run-feature --project proj123 --issue 5`
- **uv**: Python package manager for setting up development environments.
- **pytest**: Testing framework used for verifying code changes.

## contribution workflow

1. **Plan a feature**
   - Use `tugboat plan` with a brief description or brief file to generate a task plan.
   - Ensure the plan is reviewed and approved according to tier classification (simple, standard, complex).

2. **Create issues**
   - Use `tugboat create-issue` to turn the plan into GitHub issues.
   - For complex bodies, use `--split` to break into multiple issues.

3. **Run features**
   - Once issues are created and agent-ready, agents can work on tasks.
   - Use `tugboat run-feature` to start working on an approved issue.

4. **Testing**
   - Write tests using pytest.
   - Run tests locally to verify changes before submission.

5. **Submission**
   - Follow standard GitHub flow: create a branch, commit changes, open a pull request.
   - Ensure all checks pass, including pytest.

## Agent Instructions

- Always consult this AGENTS.md for project-specific conventions.
- Use the exact tugboat command flags as documented; do not invent new flags.
- For tier classification, refer to the repository's documentation (see README.md) for details on simple, standard, and complex tasks.
- Complex tasks may be blocked at intake; break them down if necessary.