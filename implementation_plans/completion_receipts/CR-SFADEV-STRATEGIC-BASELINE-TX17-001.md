# Completion Receipt: TX-17 Meta-Agent Safety Evaluation

- Receipt ID: `CR-SFADEV-STRATEGIC-BASELINE-TX17-001`
- Execution transaction: `TX-17-SAFETY-EVALUATION`
- Entry dependencies: completed and shared `TX-09-EXECUTION-CONTRACT`, `TX-13-VALIDATORS`, and `TX-16-WALKING-SKELETON`
- Subject system: `Sys4AI` framework product in the `Sys4AI-dev` development system
- Baseline change class: additive self-change safety and evaluation control baseline
- Result: `PASS`

## Outcome

TX-17 adds an integrated controlled packet for Meta-Agent self-change safety. The
packet contains separately identified threat-model, permission-scope,
verification-and-validation, evaluation-harness, assurance-case, baseline-and-
rollback, and operations-and-maintenance evidence. It binds those artifacts to a
24-scenario reference holdout suite and a fail-closed evaluator.

The reference holdouts are protected by an exact digest, mutation authority,
immutable acceptance thresholds, full regression, and accountable approval
requirements. They are deliberately described as integrity-protected rather than
secret. External rotated holdouts and accountable human acceptance remain absent.

## Changes made

- Added registered schemas and artifact contracts for the integrated safety packet
  and protected holdout suite.
- Added exact separation between proposal, approval, execution, evaluation, and
  acceptance duties. The security reviewer, verification engineer, maintenance
  planner, and baseline/rollback owner now have explicit execution bindings.
- Added 13 threat families with owners, controls, verification probes, and residual
  dispositions.
- Enforced the complete permission-envelope field set, exact permission precedence,
  least privilege, model self-approval rejection, evaluator independence, and
  human-reserved acceptance.
- Enforced default reflection depth one, bounded expansion requirements, prohibition
  of unbounded recursion, cross-layer and cross-target isolation, hostile-input
  handling, cancellation, emergency stop, and rollback evidence.
- Added positive, negative, and conflict probe coverage for all eight candidate
  value IDs. Candidate values remain unapproved pending `G-08`.
- Added a direct validator CLI and Make target and integrated the safety gate into
  aggregate product validation.
- Added exact TX-17 evidence to the additive Phase 2 safety trace row without
  changing any reviewed TX-12 disposition or count.
- Advanced program state only to a human-gated `TX-18-HUMAN-APPROVAL` handoff.

## Verification

- Focused safety suite: 27/27 passed.
- Protected reference holdouts: 24/24 matched exact expected results; 3 positive,
  17 negative, and 4 conflict scenarios.
- All eight candidate values have positive, negative, and conflict probe coverage.
- JSON Schemas, safety validator, artifact-contract rows, validation-contract rows,
  and role registry rows passed focused validation.
- Product unit suite: 232/232 passed.
- Product and repository-root `make validate`: passed.
- Direct safety, role, artifact-contract, validation-contract, JSON Schema,
  program-state, control-record, registry-graph, trace, trace-migration,
  capability-migration, and generated-derivative validators: passed.
- Generated derivatives and `git diff --check`: passed.
- Memory: `PASS_WITH_WARNINGS`; 947 objects, 411 pending-hash warnings, and zero
  derivative-authority inversions.
- Requirement trace remains 227 rows with exactly 7 `needs_evidence` and 200
  `planned` states.
- Accepted Phase 2 SHA-256 remains
  `98567cf4f4af8ca99650a6220a78d840dae5e11195891fc808c69c4828528038`.
- Accepted Phase 2 draft SHA-256 remains
  `9e290964200137329827a0164f50c2d3e97dc194fac65dd086c8b1dd7e57d84f`.
- Both protected sources have zero Git diff.
- Generalized trace SHA-256 is
  `b868e4d201bf1a5908cd87357f51214be9081684e56c04f9cd48850653958138`;
  the reversible TX-12 legacy baseline hash remains unchanged.

Passing TX-17 proves a bounded structural and local behavioral safety-control
slice. It does not prove strategic quality, ethical correctness, stakeholder
consensus, external evaluator independence, behavioral alignment, production
readiness, operational authority, autonomous capability, or domain truth.

## System-layer and authority record

The packet, schemas, evaluator, role bindings, tests, trace, and portable control
records are `framework_product` changes inside the `development_system` workspace.
Generated catalogs and role pages remain noncanonical `derivative_surface`
outputs. No target-system source gains framework authority.

`G-07`, `G-08`, accountable self-change acceptance, production readiness,
operational authority, stakeholder consensus, and domain acceptance remain open.
TX-18 has not started and no approval is inferred from this receipt.

## Rollback

Revert the complete TX-17 assurance, holdout, schema, evaluator, CLI, Make, test,
role, trace, program-state, control-record, registry, and generated-reader packet.
Retain both protected Phase 2 sources and all activated TX-16 and earlier evidence.
After downstream dependency, supersede TX-17 through a new bounded change rather
than rewriting activated records.

## Handoff

`HANDOFF-SFADEV-STRATEGIC-BASELINE-TX17-001` is human-gated and routes only to
`TX-18-HUMAN-APPROVAL`. The accountable human may approve, reject, or request
revision there. TX-19 and later work remain blocked until `G-08` is accepted.

## References

AngryOwlAI. (2026, July 9). *Sys4AI strategic-baseline identity and execution-model
decision* [Director Decision Record].
`Sys4AI/control_records/director_decisions/DDR-SFADEV-STRATEGIC-BASELINE-001.yaml`.

Sys4AI-dev. (2026a). *Sys4AI Phase 1 implementation initialization product
requirements document* [Product requirements document].
`PRDs/Sys4AI_phase-1_implementation_initialization_prd.md`.

Sys4AI-dev. (2026b). *Strategic baseline migration full implementation plan*
[Implementation plan].
`implementation_plans/Sys4AI-dev_strategic_baseline_migration_full_implementation_plan.md`.
