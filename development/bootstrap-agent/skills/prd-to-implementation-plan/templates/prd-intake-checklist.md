# PRD Intake Checklist

Use this checklist when extracting requirements from a PRD, product spec,
feature brief, issue, ticket, RFC, or pasted requirements document.

## Product Intent

- Product goal.
- Users and personas.
- Jobs to be done.
- Success criteria and acceptance criteria.
- Primary user flows.
- Explicit out-of-scope items.

## Functional Requirements

- User-visible behaviors.
- Inputs, outputs, and state transitions.
- Data creation, reading, updating, deletion, and retention.
- API, contract, integration, or routing changes.
- Admin, moderation, or permission behavior.
- Error states, empty states, loading states, and retry behavior.

## Non-Functional Requirements

- Accessibility.
- Performance.
- Security and privacy.
- Reliability and failure handling.
- Observability, analytics, logging, and auditability.
- Compatibility, deployment, and rollback.
- Compliance, localization, or content governance.

## Requirement Normalization

- Assign stable IDs such as `REQ-001`, `REQ-002`, and `NFR-001` when the PRD
  lacks IDs.
- Convert vague statements into testable statements where possible.
- Keep inferred behavior under `Assumptions`; do not present it as PRD fact.
- Classify uncertainty as `Blocking`, `Planning assumption`, or
  `Implementation detail`.
- Preserve explicit exclusions and constraints.

## Repository Scan Targets

- `AGENTS.md`, local agent instructions, or repository contribution rules.
- Package manifests, Makefiles, CI configs, README files, and docs.
- Existing routes, components, layouts, services, stores, models, schemas,
  migrations, fixtures, and tests.
- Similar prior features.
- Validation commands already used by the repository.

## Authority And Provenance

- Identify any claim, policy, data, or domain rule that depends on
  `<PROJECT_AUTHORITY>`.
- Map authority-sensitive work to source material rather than inventing local
  truth in the implementation plan.
- Mark unavailable source material as a blocker or planning assumption.
