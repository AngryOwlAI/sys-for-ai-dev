# Requirement Trace Schema 2.0 Migration Profile

## Authority and boundary

This controlled profile prepares `TX-11-TRACE-SCHEMA`. It defines the generalized row contract and a deterministic migration dry-run. It does not modify `registries/requirement_trace_registry.csv`, complete `TX-12-TRACE-DATA`, perform semantic review, or satisfy the broader `TX-13-VALIDATORS` obligations.

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

Every dry-run row is provisionally `requirement_lifecycle=proposed`, `applicability_status=not_reviewed`, `verification_status=not_run`, `evidence_status=missing`, and `semantic_review_verdict=not_reviewed`. These values prevent mechanical migration from overstating current authority, optional-profile treatment, implementation, verification, or evidence. TX-12 must replace provisional values through accountable semantic review.

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

## TX-12 promotion obligations

TX-12 must migrate the CSV header and every row atomically, preserve all existing trace and requirement IDs, review all provisional states, add exact implementation and validation evidence where claimed, and report state-dimension counts. It must not leave an old row under the new header or a new row under the old header.

## Rollback

Before TX-12 writes data, retain the TX-11 SHA-256 baseline and deterministic reverse mapping. Rollback must restore the schema, header, all rows, validator behavior, tests, registries, and generated readers as one packet. Activated historical evidence is never rewritten as part of either direction.
