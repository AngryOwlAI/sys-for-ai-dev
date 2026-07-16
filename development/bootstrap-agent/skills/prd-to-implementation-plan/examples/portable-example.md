# Portable Example: Dashboard Implementation Plan

## Scenario

A PRD exists for a release readiness dashboard. The next step is to produce a
Codex-ready implementation plan with small task packets and validation.

## Skill Role In The Chain

Use `prd-to-implementation-plan` after the PRD is written and before coding.
The plan maps requirements to repository evidence, tasks, risks, and checks.

## Example Inputs

- PRD path: `<PROJECT_ROOT>/<prd-path>/release-readiness-dashboard.md`.
- `<PROJECT_ROOT>` and repository instructions.
- Optional constraints: avoid policy changes, use existing frontend stack, no
  new production dependencies without approval.

## Example Output Excerpt

```md
# Release Readiness Dashboard Implementation Plan

## Requirement Traceability Matrix

| ID | Requirement | Likely Work Area | Validation |
| --- | --- | --- | --- |
| REQ-001 | Show required check status | `<status-source>` and dashboard view | Existing or discovered UI test |
| REQ-002 | Separate warnings from blockers | Status normalization layer | Fixture states for blocked, warning, pass |
| REQ-003 | Show unknown state for missing inputs | Error and empty-state handling | Missing-source fixture |

## Task Packet 1: Discover Existing Patterns

Goal: Identify dashboard routes, data-loading conventions, tests, and
validation commands.

Acceptance Criteria:
- Existing stack and test commands are documented from repository evidence.
- Unknown validation commands are marked, not invented.

## Task Packet 2: Add Source-Backed Status Model

Goal: Represent `blocked`, `attention required`, `checks passed`, and
`unknown` without changing release policy.

Acceptance Criteria:
- Warning-level items do not become blockers.
- Missing inputs render `unknown`.

## Task Packet 3: Build Dashboard View

Goal: Display status, blockers, attention items, owners, and provenance links.

Acceptance Criteria:
- View follows existing design system.
- Accessibility basics are covered.
```

## Validation

- Every PRD requirement maps to a task or explicit deferral.
- Commands are discovered from the repository or marked unknown.
- Rollout and rollback notes exist for user-visible changes.

## Adaptation Notes

Replace placeholders only after inspecting the target repository. Do not assume
a framework, test runner, or route pattern from this template.
