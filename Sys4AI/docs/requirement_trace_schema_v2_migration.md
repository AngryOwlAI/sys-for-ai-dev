# Requirement Trace Schema 2.0 Migration Profile

## Authority and boundary

This controlled profile records the `TX-11-TRACE-SCHEMA` preparation and the completed `TX-12-TRACE-DATA` migration. The generalized row contract, deterministic dry-run, atomic writer, exact reverse mapping, reviewed CSV, and row-by-row review evidence are current. The broader `TX-13-VALIDATORS` obligations remain open.

The live pre-migration baseline is the registry content at TX-11 execution time. The dry-run records its SHA-256 digest, row count, trace-ID set, and requirement-ID set rather than relying on the plan's older row-count estimate.

## Versioned row shapes

`schemas/contracts/requirement_trace_registry_row.schema.json` accepts exactly two mutually exclusive shapes during the bounded transition:

1. The legacy ten-column Phase 0-to-Phase 1 row.
2. The generalized `schema_version=2.0.0` row.

The generalized shape separates:

- requirement lifecycle;
- required, optional-profile, and not-applicable applicability;
- trace coverage;
- capability state;
- verification state and waiver evidence;
- evidence freshness;
- implementation artifacts;
- validation evidence;
- semantic-review owner, date, and verdict;
- supersession; and
- one-version legacy compatibility fields.

Schema validation is structural. It does not prove that an evidence path establishes a capability, that an implementation is operational, or that a semantic review is correct.

## Deterministic dry-run mapping

The TX-11 dry-run uses the following conservative provisional mappings:

| Legacy field | Generalized field | Mapping |
|---|---|---|
| `phase0_selector` | `requirement_id` | Exact copy |
| `phase0_source` | `requirement_source_id` | Exact copy |
| `coverage_status` | `coverage_status` | `covered -> covered`, `partial -> partial`, `deferred -> missing`, `not_applicable -> not_applicable` |
| `trace_class` | `capability_status` | `implemented -> scaffolded`, `scaffolded -> scaffolded`, `deferred -> absent`, `out_of_phase -> absent` |
| `evidence_paths` | `evidence_paths` | Exact copy; existence alone does not establish current evidence |

Every TX-11 dry-run row was provisionally `requirement_lifecycle=proposed`, `applicability_status=not_reviewed`, `verification_status=not_run`, `evidence_status=missing`, and `semantic_review_verdict=not_reviewed`. Those values prevented mechanical migration from overstating current authority, optional-profile treatment, implementation, verification, or evidence. TX-12 replaced all five provisional dimensions through accountable semantic review.

The legacy selector, source, coverage, trace class, semantic justification, semantic-review verdict, Phase 1 selectors, evidence paths, and notes remain recoverable. The dry-run reverses every generalized row and compares it to the exact legacy input.

## Generalized invariants

- `coverage_status=covered` does not imply implementation.
- Optional-profile applicability is independent of requirement lifecycle, coverage, and capability state.
- Implemented or operational capability requires an implementation artifact.
- Operational capability requires current evidence, passing verification, and exact validation evidence.
- Removed capability rejects an active implementation path and requires historical or current removal evidence.
- Passing verification requires exact validation evidence.
- Waived verification requires a waiver ID.
- Deprecated, superseded, or retired requirements cannot be classified operational.
- A completed semantic review requires an owner and date; `not_reviewed` requires an empty date.
- Generated derivatives cannot become sole canonical or operational evidence merely by satisfying the row schema.

## TX-12 semantic-review result

TX-12 migrated the CSV header and every row atomically. All 214 trace IDs, requirement IDs, legacy fields, evidence paths, and row order are preserved. Compatibility columns reconstruct the exact TX-11 SHA-256 `95e59cf5befc4f9fd29d857d1f609a4c0d2c321c1b3adf1efca1a69cdb01b28c`; the reviewed generalized CSV SHA-256 is `b76dd57a8e5be11703213e57661690d7219e3a62eec9971fea633328e9003f97`.

Reviewed counts:

- lifecycle: 214 `active`;
- applicability: 214 `required`;
- coverage: 79 `covered`, 135 `partial`;
- capability: 72 `implemented`, 137 `scaffolded`, 5 `absent`, and zero `operational`;
- verification: 14 `pass`, 200 `planned`;
- evidence: 214 `current`;
- semantic review: 207 `sufficient`, 7 `needs_evidence`, zero `not_reviewed`; and
- retired-runtime compatibility evidence: 32 rows, classified as historical evidence only.

`docs/requirement_trace_semantic_review_tx12.md` records the review method, explicit gaps, state counts, and all 214 row dispositions. Exact implementation and validation paths remain in the controlled trace row rather than being duplicated as a second authority source.

The seven `needs_evidence` rows were legacy `implemented` mappings with no exact current implementation artifact. They were demoted to `scaffolded` and `planned`. File existence, generated output, and historical AgentJob or `/continue` evidence were not treated as operational proof.

## Rollback

The TX-11 SHA-256 baseline and deterministic reverse mapping remain retained after the write. Rollback must restore the schema, header, all rows, validator behavior, tests, registries, and generated readers as one packet. Activated historical evidence is never rewritten as part of either direction.
