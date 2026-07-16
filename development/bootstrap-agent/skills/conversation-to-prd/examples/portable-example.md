# Portable Example: Release Readiness Dashboard PRD

## Scenario

Conversation and source analysis have established that the team needs a
dashboard showing release readiness from existing project evidence.

## Skill Role In The Chain

Use `conversation-to-prd` after source analysis and decision clarification. The
PRD captures user value, scope, boundaries, and test expectations without
inventing implementation details.

## Example Inputs

- Current conversation: dashboard goal, resolved terminology, warning behavior.
- `<PROJECT_ROOT>`: target repository root.
- `<OUTPUT_DIRECTORY>`: local PRD directory.
- Repository evidence: source analysis, release policy, CI configuration,
  ownership documentation.

## Example Output Excerpt

```md
# Release Readiness Dashboard PRD

## Problem Statement

Release coordinators need one source-grounded view of whether the current
release is blocked, attention-required, or checks-passed before handoff.

## Solution

Create an internal dashboard that reads existing release evidence and displays
release state, blockers, warning-level attention items, and assigned owners.

## User Stories

1. As a release coordinator, I want to see required check status, so that I can
   identify release blockers quickly.
2. As an engineering owner, I want warning-level items separated from blockers,
   so that I can prioritize follow-up without changing release policy.

## Implementation Decisions

- Use source-backed status labels: `blocked`, `attention required`, and
  `checks passed`.
- Do not display "approved" unless an approval source is integrated.
- Keep policy changes out of scope.

## Testing Decisions

- Validate that blocked, warning, and passing fixture states render distinct
  labels.
- Validate that missing source inputs show an explicit unknown state.

## Authority And Provenance

- Dashboard claims must trace to release policy, CI configuration, deployment
  records, and ownership documentation.
```

## Validation

- Product requirements reflect the source analysis and resolved decisions.
- Open questions are listed only when material.
- Testing decisions describe observable behavior.

## Adaptation Notes

Do not publish externally unless the target project has configured an external
tracker and the user requests that publication.
