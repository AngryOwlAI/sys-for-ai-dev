---
plan_id: SFA-PLAN-REPOSITORY-REBOOT-001
status: active
subject: development-system
source_prd: PRDs/active/Sys4AI_repository_reboot_prd.md
architecture_baseline: architecture/README.md
owner: system_director
created: 2026-07-15
last_updated: 2026-07-16
implementation: complete
validation: pass
promotion: pending_human_review
supersedes: null
acceptance_criteria:
  - one-way dependency boundary passes
  - development product and integration validation pass
  - product builds independently
  - source planning state and derivative hygiene pass
---

# Repository Reboot Implementation Plan

## Product summary

Rebuild the active repository as five explicit planes, retain portable product
and bootstrap assets, and eliminate development-history coupling from the
product.

## Repository context

- Pre-reboot baseline: `5a6aaf7652661e094cdfa40be55a380e9bc0cd8c`.
- Rollback tag: `pre-reboot-2026-07-15`.
- Legacy history: Git history and the dedicated archived repository.
- Initial aggregate validation: passed on 2026-07-16 UTC.
- Current uncommitted guide work: retained as post-baseline product
  documentation input.

## Requirement trace

The detailed requirement-to-evidence matrix is
`development/trace/requirements.csv`. No requirement may be marked verified
without an exact implementation and validation path.

## Work packets

### RP-01 — Freeze and classify

- Record the baseline commit and tag.
- Classify every retained family by development, product, target, or derivative
  layer.
- Record migration and rollback evidence.

Acceptance: baseline and archive references are inspectable; user work is
preserved.

### RP-02 — Rebuild the control plane

- Create the human front doors, two active PRDs, architecture set, ADRs, and
  single active plan.
- Remove stale active planning and derivative PRD surfaces.

Acceptance: authority and current state are obvious from root navigation.

### RP-03 — Extract bootstrap development

- Move canonical skills, catalogs, schemas, tools, profiles, state, and current
  evidence under `development/`.
- Generate and validate host bindings.
- Provide the `sfadev` development CLI.

Acceptance: hidden host directories contain bindings only; canonical skill
sources are visible and validated.

### RP-04 — Extract the portable product

- Normalize packaging and CLI names.
- Implement the host-neutral package structure and product-local contracts,
  assets, adapters, examples, and tests.
- Remove development state, history, and parent dependencies.

Acceptance: `Sys4AI/` builds and tests independently.

### RP-05 — Establish integration and evidence

- Move and sanitize the target fixture.
- Add end-to-end integration tests.
- Add current and release evidence tiers without transaction-event sediment.

Acceptance: installed product behavior validates the derivative fixture and
reports explicit limitations.

### RP-06 — Retire operational sediment

- Remove old plans, reports, receipts, audits, temporary handoffs, generated
  readers, historical control records, oversized registries, and completed
  migration validators from the active tree.

Acceptance: all retained history remains reachable through rollback sources;
active source hygiene passes.

### RP-07 — Verify and review

- Run narrow tests first, then all root and product gates.
- Run forbidden-reference, active-plan, active-PRD, binding, source-authority,
  build, whitespace, and final-diff checks.
- Record residual risks and exact verification level.

Acceptance: every reboot PRD criterion has executed evidence or an explicit
gap; any gap blocks completion.

## Security, privacy, and reliability

- No new production, network, secret, or external-system authority is granted.
- Tool execution remains host- and permission-envelope-dependent.
- Candidate self-hosting work occurs in a separate workspace.
- Generated or candidate artifacts cannot approve themselves.
- Rollback remains available throughout the migration.

## Out of scope

- Production deployment.
- Publication or push.
- Autonomous release promotion.
- Claims of stakeholder, domain, operational, or production acceptance.

## Validation commands

    make validate-development
    make validate-product
    make validate-integration
    make validate
    cd Sys4AI && make lint test validate-contracts validate-assets build

## Candidate closure

All seven work packets and every reboot-PRD requirement have implementation
and executed validation evidence in `development/trace/requirements.csv` and
`development/evidence/current/validation-summary.md`.

The plan remains `active` because the repository is an uncommitted reboot
candidate awaiting accountable human review. Marking it completed while it
remained in `implementation_plans/active/` would violate planning hygiene, and
candidate output cannot promote itself.
