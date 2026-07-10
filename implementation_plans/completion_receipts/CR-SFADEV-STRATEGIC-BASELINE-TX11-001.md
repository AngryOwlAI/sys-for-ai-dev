# Completion Receipt: TX-11 Trace Schema

- Receipt ID: `CR-SFADEV-STRATEGIC-BASELINE-TX11-001`
- Execution transaction: `TX-11-TRACE-SCHEMA`
- Entry dependencies: accepted `TX-06-P1-BASELINE`, completed `TX-09-EXECUTION-CONTRACT`, and shared `TX-10` closeout
- Subject system: `Sys4AI-dev` development system and `Sys4AI` framework product
- Subject layers: `development_system`, `framework_product`, and regenerated `derivative_surface`
- Result: `PASS`

## Outcome

TX-11 generalized the requirement-trace row contract without migrating trace data. The registered JSON Schema now admits the exact legacy row and a mutually exclusive `2.0.0` row that separates requirement lifecycle, applicability including optional profiles, coverage, capability, verification, waiver, evidence freshness, implementation, validation, semantic review, and supersession state.

The migration implementation maps rows only in memory. It preserves every legacy field in compatibility columns, reverses each generalized row to the exact input, checks duplicate and missing IDs, validates every draft row against the generalized schema, and verifies that the source digest is unchanged.

## Migration dry-run evidence

- Live legacy baseline: 214 rows, 214 trace IDs, and 214 requirement IDs.
- Legacy SHA-256 before and after dry-run: `95e59cf5befc4f9fd29d857d1f609a4c0d2c321c1b3adf1efca1a69cdb01b28c`.
- Coverage draft counts: 79 `covered`; 135 `partial`.
- Applicability draft count: 214 `not_reviewed`.
- Capability draft counts: 5 `absent`; 209 `scaffolded`.
- Verification draft count: 214 `not_run`.
- Evidence draft count: 214 `missing`.
- Semantic-review draft count: 214 `not_reviewed`.
- Writes to `Sys4AI/registries/requirement_trace_registry.csv`: zero.

The provisional counts are migration staging values, not accepted semantic verdicts. In particular, legacy `implemented` trace classes map conservatively to `scaffolded` until TX-12 identifies exact implementation artifacts and accountable evidence.

## Validation evidence

- Generalized schema and migration tests: 18/18 passed.
- Current legacy trace validation: passed for 214 explicit Phase 0 rows and 128 indexed Phase 1 requirements.
- Migration dry-run: passed with row, trace-ID, requirement-ID, reverse-mapping, and hash parity.
- Product unit suite: 137/137 passed.
- Product aggregate validation: passed.
- Root aggregate validation: passed.
- Capability boundary, program state, registry graph, JSON Schemas, generated derivatives, compilation, and diff integrity: passed.
- Memory preflight: `PASS_WITH_WARNINGS`; one generated catalog hit was rejected as authority and controlled source rows were inspected.

## Rollback

Revert the complete TX-11 schema, mapping, validator preparation, tests, documentation, registries, control records, and generated-reader packet. The legacy trace CSV already remains unchanged and must not be paired with only part of the generalized contract. Activated historical evidence remains unchanged in either direction.

## Handoff

`HANDOFF-SFADEV-STRATEGIC-BASELINE-TX11-001` routes only to `TX-12-TRACE-DATA`. TX-12 must migrate all 214 rows atomically, preserve exact row and ID parity, and replace provisional values through accountable semantic review. TX-13 and all later transactions remain out of scope.
