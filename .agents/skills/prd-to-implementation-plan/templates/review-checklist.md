# Final Plan Review Checklist

Use this checklist before presenting or writing the final implementation plan.

## Completeness

- [ ] The source PRD path, issue, pasted content, or selection is identified.
- [ ] Planning status is `Ready`, `Ready with assumptions`, or `Blocked`.
- [ ] Every PRD requirement is mapped to at least one task or explicitly
  deferred.
- [ ] Functional and non-functional requirements are both represented.
- [ ] Explicit exclusions and constraints are preserved.
- [ ] Open questions are classified by impact.

## Engineering Fit

- [ ] Repository architecture was inspected before planning.
- [ ] Existing patterns are preferred over new abstractions.
- [ ] New dependencies, migrations, or broad refactors are justified or avoided.
- [ ] Likely affected files and directories are named when known.
- [ ] Data, API, UI, accessibility, error handling, and state implications are
  covered when relevant.
- [ ] Security, privacy, reliability, observability, rollout, and rollback are
  considered.

## Task Packet Quality

- [ ] Every task has `Goal`, `Context`, `Constraints`, `Implementation notes`,
  `Acceptance criteria`, `Validation`, and `Done when`.
- [ ] Tasks are small enough for one branch or one draft PR where feasible.
- [ ] Tasks are ordered by dependency and mark parallelizable work.
- [ ] Each task references PRD requirement IDs.
- [ ] Validation guidance uses discovered commands or explicitly says to
  discover the command before coding.
- [ ] Risky tasks include review or rollback notes.

## Execution Surface Fit

- [ ] Tasks are self-contained and do not depend on hidden local state.
- [ ] Editor-specific references are used only when the intended execution
  surface supports them.
- [ ] Task prompts require validation summaries before completion.
- [ ] The plan does not perform direct coding unless the user asked to code.

## Authority And Provenance

- [ ] Authority-sensitive claims map to `<PROJECT_AUTHORITY>`.
- [ ] Source links or source records are treated as provenance when relevant.
- [ ] Missing authority material is marked as a blocker or assumption.
