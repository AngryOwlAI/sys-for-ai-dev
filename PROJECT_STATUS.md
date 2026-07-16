---
project: Sys4AI-dev
project_status: active
product_status: repository_reboot_candidate
active_product_prd: PRDs/active/Sys4AI_product_baseline_prd.md
active_change_prd: PRDs/active/Sys4AI_repository_reboot_prd.md
active_plan: implementation_plans/active/repository-reboot-implementation-plan.md
active_work_item: null
pre_reboot_baseline: 5a6aaf7652661e094cdfa40be55a380e9bc0cd8c
pre_reboot_tag: pre-reboot-2026-07-15
last_verified_commit: 5a6aaf7652661e094cdfa40be55a380e9bc0cd8c
last_validation: 2026-07-16T04:38:07Z
---

# Current State

## What exists

- A frozen pre-reboot Git baseline and a separate historical repository.
- Two active PRDs: the portable product baseline and the one-time repository
  reboot change.
- One active implementation plan.
- A canonical bootstrap development plane under `development/`.
- An extractable product boundary under `Sys4AI/`.
- Integration fixtures outside the product boundary.

## What is implemented

- The mixed development/product/history layout has been replaced by five
  explicit planes with executable one-way dependency checks.
- Canonical bootstrap skills live under `development/`; `.agents/` and
  `.codex/` contain generated bindings only.
- `Sys4AI/` is an independently buildable `sys4ai` distribution with a
  host-neutral domain kernel, application services, ports, adapters, contracts,
  assets, examples, tests, and product CLI.
- `sfadev` owns repository-specific validation, state, host-binding, and release
  evidence concerns.
- The repository-steward derivative fixture and installed-wheel target flow are
  validated outside the product source boundary.
- Historical controls, superseded plans, generated readers, receipts, handoffs,
  oversized registries, and completed migration machinery are absent from the
  active tree and remain recoverable at the rollback tag.

## What is not implemented

- Production deployment, release publication, and operational authorization.
- Autonomous candidate promotion or self-approval.
- Stakeholder, domain, ethical, or production acceptance of Sys4AI or any
  generated target.

## What is not claimed

The reboot does not prove production readiness, stakeholder consensus, domain
fitness, operational authorization, or safe autonomous self-improvement.

## Current objective

Preserve the verified reboot candidate for accountable human review. The
change PRD and implementation plan remain active until that review decides
whether to accept, correct, or supersede the candidate.

## Current blockers

None recorded. The local verification suite passes; a future failed boundary,
build, integration, or hygiene check becomes a fail-closed blocker.

## Next authorized decision

An accountable human may review the reboot candidate for commit, release
planning, further correction, or supersession. The candidate cannot promote
itself.
