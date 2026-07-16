# Codex Task Packet Template

Use this template for each implementation task. Keep every task scoped to one
branch or one draft PR where feasible.

```md
## Task N: <short action-oriented title>

### Goal

<One specific outcome.>

### Context

- PRD requirements: <REQ IDs>
- Relevant files or directories: <paths or editor references when known>
- Existing patterns to follow: <brief notes>

### Constraints

- <What not to change>
- <Architecture, dependency, style, or safety constraints>

### Implementation Notes

- <Suggested steps, not overly prescriptive>

### Acceptance Criteria

- [ ] <Observable criterion>
- [ ] <Observable criterion>

### Validation

- <Exact lint, typecheck, unit, integration, end-to-end, build, or manual
  commands when discovered>
- If a command is unknown, write `Discover and document the correct command
  before coding`.

### Done When

- <Tests pass, behavior works, docs updated, PR ready>
```

## Packet Quality Rules

- Make the task self-contained for the intended execution surface.
- Include setup assumptions and repository paths when known.
- Prefer vertical slices that can be reviewed independently.
- Include source PRD requirement IDs and validation commands.
- State any dependency on earlier tasks.
- Mark tasks that can run in parallel.
- Include expected output, branch or PR scope, and review checklist when useful.
- Require validation summaries before considering the task complete.
