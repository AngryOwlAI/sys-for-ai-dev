# Product Requirements Authority

This directory is the requirements control plane. It does not contain runtime
state, implementation evidence, generated readers, or historical transaction
records.

## Active

| Artifact | Authority | Purpose |
|---|---|---|
| [Sys4AI product baseline](active/Sys4AI_product_baseline_prd.md) | canonical | Durable product identity, lifecycle, governance, runtime, target, assurance, operations, and self-hosting requirements |
| [Repository reboot](active/Sys4AI_repository_reboot_prd.md) | controlled active change | One-time repository extraction and acceptance requirements |

Exactly one active change PRD is permitted. The product baseline is not counted
as a change PRD.

## Accepted baselines

- [Phase 1 initialization baseline](baselines/phase-1-initialization-baseline.md)
- [Phase 2 walking-skeleton baseline](baselines/phase-2-walking-skeleton-baseline.md)
- [Phase 2 strategic addendum](baselines/phase-2-strategic-addendum.md)

These preserve accepted intent and evidence context. They do not control the
new physical repository layout.

## Reference

- [Decomposition strategy](reference/decomposition-strategy.md)

Draft modular PRDs, the historical Phase 0 source, and superseded plan-era
requirements remain available through Git history and the frozen legacy
repository. They are intentionally absent from the active tree.
