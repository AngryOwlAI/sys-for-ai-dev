# Portable Example: Resolving Readiness Terminology

## Scenario

The team uses "ready," "approved," and "green" interchangeably when discussing
release status. Repository evidence shows these terms are not equivalent.

## Skill Role In The Chain

Use `domain-grilling-with-docs` when terminology affects the PRD, dashboard
labels, or future architecture decisions.

## Example Inputs

- Plan under review: "Show whether a release is ready."
- `<CONTEXT_FILE>`: glossary, domain-language document, or context map.
- `<ADR_DIRECTORY>`: optional location for architecture decision records.
- Repository evidence: release policy and CI status conventions.

## Example Interaction

```text
Analysis:
The term "ready" is ambiguous. The release policy distinguishes technical
checks from approval, while the proposed dashboard label collapses them.

Question:
Should "release ready" mean "technical checks passed" or "approved to deploy"?

Recommendation:
Use "checks passed" for the dashboard state unless the approval source is also
integrated. Reserve "approved" for an explicit human or policy approval record.
```

## Example Documentation Update

```md
## Glossary Entry

`checks passed`: Automated required checks are passing according to configured
source systems.

`approved`: A human or policy approval record permits deployment. This is not
implied by `checks passed`.
```

## Validation

- The glossary records domain language, not implementation detail.
- Any ADR is created only if the term choice is hard to reverse or materially
  affects architecture.
- Contradictions between user wording and source documents are explicit.

## Adaptation Notes

Replace `<CONTEXT_FILE>` and `<ADR_DIRECTORY>` with the target project's
documentation locations only during adaptation.
