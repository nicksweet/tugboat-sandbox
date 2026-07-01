# Intake Checklist: Plan vs Split Workflow

## Comparison Table

| Aspect | tugboat plan (Frontier-Assisted Decomposition) | tugboat create-issue (Split Workflow) |
|--------|-----------------------------------------------|---------------------------------------|
| Purpose | Break down a feature into smaller tasks using frontier model assistance. | Split an existing issue into multiple issues for parallel work. |
| When to Use | When starting a new feature that requires decomposition. | When an existing issue is too large and needs to be split for better tracking. |
| Tier Implications | Typically used for Tier 1 and Tier 2 features that require careful planning. | Can be used for any tier when an issue becomes too large. |
| Approval Gates | Requires review of the generated plan by tech lead or architect. | Requires review of the split issues to ensure they are well-formed and independent. |
| Steps | 1. Run `tugboat plan <feature-description>` <br> 2. Review the generated plan <br> 3. Approve or iterate <br> 4. Create issues from the plan | 1. Identify a large issue <br> 2. Run `tugboat create-issue <issue-id> --split` <br> 3. Review the generated sub-issues <br> 4. Approve and create the sub-issues |

## Checklist

### When to Use Plan Workflow
- [ ] Starting a new feature with unclear requirements
- [ ] Need to break down work into smaller, estimable tasks
- [ ] Requires frontier model assistance for decomposition
- [ ] Tier 1 or Tier 2 feature (high priority, strategic)

### When to Use Split Workflow
- [ ] Existing issue is too large (more than 2 days of work)
- [ ] Need to assign different parts to different team members
- [ ] Issue spans multiple components or services
- [ ] Any tier, but only when the issue is already created and needs splitting

### Plan Workflow Steps
- [ ] Run `tugboat plan <feature-description>`
- [ ] Review the generated plan for completeness and accuracy
- [ ] Get approval from tech lead or architect
- [ ] Create issues from the approved plan

### Split Workflow Steps
- [ ] Identify the issue to split (must exist in the tracker)
- [ ] Run `tugboat create-issue <issue-id> --split`
- [ ] Review the generated sub-issues for independence and clarity
- [ ] Approve the split and create the sub-issues
- [ ] Update the original issue to reflect the split (e.g., add links to sub-issues)