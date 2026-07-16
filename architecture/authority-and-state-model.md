---
artifact_id: SFA-ARCH-AUTHORITY-STATE-001
artifact_type: architecture
subject: sys4ai-ecosystem
subject_layer: framework
authority: controlled
status: active
owner: system_architect
supersedes: null
source_trace:
  - SFA-PRD-PRODUCT-BASELINE-001
---

# Authority and State Model

## Controlled artifact metadata

A controlled artifact carries only the metadata needed to classify it:

| Field | Purpose |
|---|---|
| artifact_id | Stable identity |
| artifact_type | PRD, architecture, decision, plan, state, evidence, template, or contract |
| subject | System or target governed |
| subject_layer | Development, framework, target template, target instance, or derivative |
| authority | Canonical, controlled, reference, generated, or historical |
| status | Draft, proposed, accepted, active, completed, or superseded |
| owner | Accountable maintainer or decision owner |
| supersedes | Prior artifact identity, when applicable |
| source_trace | Exact upstream authority |

Execution and evidence may additionally record actor, authorization, permission
scope, timestamps, and validation result.

## Independent dimensions

Authority, lifecycle, approval, implementation, validation, capability, and
evidence freshness are never collapsed into one status. A canonical artifact
may be unapproved; an implemented capability may be unvalidated; a validated
capability may lack operational authority.

## Promotion rules

- Generated material remains generated until an accountable authority accepts
  a new controlled source.
- Development skills are generalized and reviewed before becoming product
  assets.
- Target observations become product input only through an approved
  requirement or architecture change.
- Activated history is superseded with explicit evidence, not rewritten.

## One-fact rule

One authoritative fact has one source. Catalogs link to that source; status
files summarize it; generated readers navigate it. None duplicates its
authority.
