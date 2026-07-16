---
artifact_id: ADR-0004
artifact_type: decision
subject: sys4ai
subject_layer: framework
authority: controlled
status: accepted
owner: system_director
supersedes: DDR-SYS4AI-DEV-NAME-MIGRATION-001
source_trace:
  - SFA-PRD-PRODUCT-BASELINE-001
---

# ADR-0004: Product Packaging

## Context

The distribution was named `Sys4AI`, the package `sys_for_ai`, and the CLI
`Sys4AI`. The split added permanent migration semantics to a pre-release
product.

## Decision

Use `sys4ai` for the distribution, Python package, and product CLI. Use
`sfadev` for repository-specific development commands. Do not ship a
`sys_for_ai` compatibility package because no external compatibility
requirement is registered.

## Consequences

Imports and tests change once. Product code uses a src layout and capability
names rather than phase or transaction identifiers.

## Verification

Wheel/sdist build, isolated import, CLI help, and absence checks for
`sys_for_ai`.
