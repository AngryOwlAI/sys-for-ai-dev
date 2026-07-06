# Portable Example: Clarifying Dashboard Decisions

## Scenario

A source analysis found that a release readiness dashboard is feasible, but the
team has not decided whether warning-level test failures should block release.

## Skill Role In The Chain

Use `decision-grilling` after initial analysis and before final PRD writing when
one unresolved decision could change scope, acceptance criteria, or risk.

## Example Inputs

- Plan under review: "Build a release readiness dashboard."
- Evidence: source analysis showing CI status, incidents, and release owner are
  existing source inputs.
- Decision criteria: avoid false release confidence and keep the first version
  small.

## Example Interaction

```text
Analysis:
The highest-leverage unresolved decision is whether warning-level test failures
should block the dashboard's release-ready state.

Question:
Should the dashboard treat warning-level test failures as release-blocking?

Recommendation:
No. Treat warnings as "attention required" in version 1 unless the release
policy explicitly defines them as blockers. This preserves source authority and
avoids inventing stricter governance than the project currently documents.
```

## Example Resolved Decision

```md
## Resolved Decision

Warning-level test failures will not mark a release as blocked in version 1.
They will appear in an "attention required" section with source links and owner
labels.
```

## Validation

- The question is singular and decision-relevant.
- The recommendation is tied to evidence and risk.
- The resolved decision can be carried into the PRD.

## Adaptation Notes

In a regulated or safety-critical target project, the recommended default may
change. Preserve the one-question-at-a-time method, then adapt the risk
tolerance from target-project authority.
