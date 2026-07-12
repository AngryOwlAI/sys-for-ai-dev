# TX-32 Local Evidence: JSON Schema Validation Contracts

## Decision

`TX-32-LOCAL-EVIDENCE-JSON-SCHEMA` verifies exactly `SFA-CORE-JSONSCHEMA-001` through `SFA-CORE-JSONSCHEMA-007`, `SFA-P0-FR-035`, `SFA-P0-FR-039`, and `SFA-P0-FR-042`. Their verification states advance from `planned` to `pass`; capability remains `implemented`, coverage remains `covered`, semantic review remains `sufficient`, and no waiver is used.

External evidence, cross-version CI, `G-10`, production readiness, and operational authority remain later evidence-dependent work. Authorization permits bounded execution; it is not evidence and does not make those claims true inside TX-32.

## Authority and baseline

- Accountable authorization: the user explicitly authorized the quoted ten-row JSON Schema family on 2026-07-12.
- Scope decision: `DDR-SFADEV-STRATEGIC-BASELINE-G11-009`.
- Input handoff: `HANDOFF-SFADEV-STRATEGIC-BASELINE-TX31-001`.
- Memory preflight: `MEMPREFLIGHT-TX-32-LOCAL-EVIDENCE-JSON-SCHEMA-20260712T132623Z`, `PASS_WITH_WARNINGS`, zero authority inversions.
- Frozen TX-23 SHA-256: `1e9e2b2a0a7bc4f589addd65b8d34642899a3f812e7ce35be6e62a2c0fcc6138`.
- Frozen TX-25 SHA-256: `9ed89d6ff5872ee2fb2b740791c268d9048e97f31eae8ff7d3b4d2d8929d5f38`.
- Canonical Phase 0 and Phase 1 PRDs remain unchanged.

## Verification design

The focused validator requires the exact JSON Schema format profile, complete unique contract registration, one-to-one `.schema.json` source coverage, Draft 2020-12 declarations, unique contract identifiers, governed target metadata, executable validator commands, explicit structural-only policy, current noncanonical generated catalog coverage, no standalone JSON wiki, and fail-closed supersession with existing migration evidence paths.

Negative probes reject profile drift, duplicate contract IDs, missing ownership, declared-dialect drift, missing schema IDs, invalid schemas, supersession without migration evidence, stale generated catalog content, and standalone JSON-wiki registration.

The source-first closeout check also repaired generalized trace-row lookup in the memory-preflight validator: `requirement_trace_registry.csv` is now indexed by `trace_id`, not its leading `schema_version` column. This validates both the new TX-32 receipt and the unchanged activated TX-31 receipt without rewriting either trace or prior control history.

## Requirement dispositions

| Requirement | Evidence method | Disposition |
| --- | --- | --- |
| `SFA-CORE-JSONSCHEMA-001` | Exact profile registry and one-to-one contract audit | JSON Schema is verified as the governed preferred validation-contract format. |
| `SFA-CORE-JSONSCHEMA-002` | Registered target-format and artifact metadata review | Contracts govern JSON, parsed YAML, TOML-normalized, CSV/registry, control, manifest, discovery, and configuration objects. |
| `SFA-CORE-JSONSCHEMA-003` | Registry-field, Draft declaration, `$id`, owner, authority, and validator checks | Every contract declares the required metadata. |
| `SFA-CORE-JSONSCHEMA-004` | Policy and generated structural-warning checks | Structural admissibility is not semantic truth, domain correctness, or acceptance. |
| `SFA-CORE-JSONSCHEMA-005` | Deterministic generated-page freshness and coverage check | Every registered contract is indexed in the noncanonical Validation Contracts Catalog. |
| `SFA-CORE-JSONSCHEMA-006` | Policy, derivative-registry, and generated-root negative checks | No standalone JSON wiki exists by default. |
| `SFA-CORE-JSONSCHEMA-007` | Supersession lifecycle and migration-evidence negative checks | Contract changes fail closed without known predecessors and concrete migration evidence. |
| `SFA-P0-FR-035` | Exact format assignment, dialect, target mapping, and validator evidence | JSON Schema is assigned to validation contracts. |
| `SFA-P0-FR-039` | Catalog-not-wiki policy and filesystem verification | The approved reader surface is the Validation Contracts Catalog, not a JSON wiki. |
| `SFA-P0-FR-042` | Policy, validator, derivative, and retained walking-skeleton limitation checks | Schema validation remains process/structure evidence only. |

## Executed validation

- Focused validator: 10/10 requirements passed.
- Focused positive/negative tests: 11/11 passed.
- Full product tests: 318/318 passed.
- Trace: 227 rows; `pass=80`, `planned=147`; semantic review `sufficient=227`.
- Local evidence: 60 accepted rows; 14 local verification obligations remain.
- Product and repository-root `make validate`: passed.
- Memory: `PASS_WITH_WARNINGS`; 1,211 objects, 545 known pending-hash warnings, zero derivative authority inversions.
- Frozen TX-23 and TX-25 hashes: unchanged.
- Accepted waivers: zero.

## Limitations

These checks prove current local JSON Schema assignment, registration, Draft validity, metadata, structural-only policy, generated catalog freshness, no-wiki boundary, and supersession/migration controls. They do not prove external truth, target-runtime operations, production fitness, stakeholder consensus, cross-version Python execution, or operational readiness.

## Rollback and next gate

Before publication, revert the complete TX-32 packet. After publication, preserve G-11-009, the ten additive evidence rows, trace verification evidence, report, transaction, receipt, and handoff as activated history; use a new bounded transaction for any later evidence family.

The earliest dependency-ready family among the 14 remaining local obligations must be selected from the live frozen ledger and trace order. `G-10` remains deferred until retained evidence closure is complete.
