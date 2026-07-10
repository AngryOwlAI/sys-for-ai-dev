"""Deterministic TX-11 preparation for requirement-trace schema migration."""

from __future__ import annotations

from collections import Counter
import csv
import hashlib
from pathlib import Path
from typing import Mapping

from .jsonschema_io import load_json, validate_instance
from .registry_io import resolve_registered_path
from .validators import ValidationResult


TRACE_SCHEMA_VERSION = "2.0.0"
DEFAULT_TRACE_REGISTRY = Path("registries/requirement_trace_registry.csv")
DEFAULT_TRACE_SCHEMA = Path("schemas/contracts/requirement_trace_registry_row.schema.json")

LEGACY_HEADER = (
    "trace_id",
    "phase0_selector",
    "phase0_source",
    "coverage_status",
    "trace_class",
    "semantic_justification",
    "semantic_review_verdict",
    "phase1_selectors",
    "evidence_paths",
    "notes",
)

GENERALIZED_HEADER = (
    "schema_version",
    "trace_id",
    "requirement_id",
    "requirement_source_id",
    "requirement_lifecycle",
    "applicability_status",
    "coverage_status",
    "capability_status",
    "verification_status",
    "verification_waiver_id",
    "evidence_status",
    "implementation_artifacts",
    "validation_evidence",
    "evidence_paths",
    "semantic_review_owner",
    "semantic_review_date",
    "semantic_review_verdict",
    "supersedes",
    "phase0_selector",
    "phase0_source",
    "legacy_coverage_status",
    "trace_class",
    "semantic_justification",
    "legacy_semantic_review_verdict",
    "phase1_selectors",
    "notes",
)

_COVERAGE_MAP = {
    "covered": "covered",
    "partial": "partial",
    "deferred": "missing",
    "not_applicable": "not_applicable",
}

_CAPABILITY_MAP = {
    "implemented": "scaffolded",
    "scaffolded": "scaffolded",
    "deferred": "absent",
    "out_of_phase": "absent",
}


def migrate_legacy_trace_row(row: Mapping[str, str]) -> dict[str, str]:
    """Map one legacy row to a conservative, reversible generalized draft row.

    The mapping is intentionally provisional. It preserves legacy fields exactly,
    makes no implemented or current-evidence claim, and leaves semantic promotion
    to TX-12 review.
    """

    missing = [field for field in LEGACY_HEADER if field not in row]
    if missing:
        raise ValueError(f"legacy row missing fields: {', '.join(missing)}")

    coverage_status = row["coverage_status"]
    trace_class = row["trace_class"]
    if coverage_status not in _COVERAGE_MAP:
        raise ValueError(f"unsupported legacy coverage_status {coverage_status!r}")
    if trace_class not in _CAPABILITY_MAP:
        raise ValueError(f"unsupported legacy trace_class {trace_class!r}")

    migrated = {
        "schema_version": TRACE_SCHEMA_VERSION,
        "trace_id": row["trace_id"],
        "requirement_id": row["phase0_selector"],
        "requirement_source_id": row["phase0_source"],
        "requirement_lifecycle": "proposed",
        "applicability_status": "not_reviewed",
        "coverage_status": _COVERAGE_MAP[coverage_status],
        "capability_status": _CAPABILITY_MAP[trace_class],
        "verification_status": "not_run",
        "verification_waiver_id": "",
        "evidence_status": "missing",
        "implementation_artifacts": "",
        "validation_evidence": "",
        "evidence_paths": row["evidence_paths"],
        "semantic_review_owner": "requirements_verifier",
        "semantic_review_date": "",
        "semantic_review_verdict": "not_reviewed",
        "supersedes": "",
        "phase0_selector": row["phase0_selector"],
        "phase0_source": row["phase0_source"],
        "legacy_coverage_status": coverage_status,
        "trace_class": trace_class,
        "semantic_justification": row["semantic_justification"],
        "legacy_semantic_review_verdict": row["semantic_review_verdict"],
        "phase1_selectors": row["phase1_selectors"],
        "notes": row["notes"],
    }
    if tuple(migrated) != GENERALIZED_HEADER:
        raise RuntimeError("generalized trace mapping header drift")
    return migrated


def reverse_generalized_trace_row(row: Mapping[str, str]) -> dict[str, str]:
    """Recover the exact legacy row fields retained by the v2 compatibility layer."""

    return {
        "trace_id": row["trace_id"],
        "phase0_selector": row["phase0_selector"],
        "phase0_source": row["phase0_source"],
        "coverage_status": row["legacy_coverage_status"],
        "trace_class": row["trace_class"],
        "semantic_justification": row["semantic_justification"],
        "semantic_review_verdict": row["legacy_semantic_review_verdict"],
        "phase1_selectors": row["phase1_selectors"],
        "evidence_paths": row["evidence_paths"],
        "notes": row["notes"],
    }


def validate_requirement_trace_migration(
    trace_registry: str | Path = DEFAULT_TRACE_REGISTRY,
    schema_path: str | Path = DEFAULT_TRACE_SCHEMA,
) -> ValidationResult:
    """Dry-run the TX-12 row transform without writing the trace registry."""

    target = resolve_registered_path(str(trace_registry))
    schema_target = resolve_registered_path(str(schema_path))
    if not target.exists():
        return ValidationResult(False, [f"{target}: missing requirement trace registry"])
    if not schema_target.exists():
        return ValidationResult(False, [f"{schema_target}: missing requirement trace row schema"])

    before_hash = _sha256(target)
    try:
        with target.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            fieldnames = tuple(reader.fieldnames or ())
            rows = list(reader)
    except (OSError, csv.Error) as exc:
        return ValidationResult(False, [f"{target}: unable to read trace registry: {exc}"])

    messages: list[str] = []
    if fieldnames != LEGACY_HEADER:
        messages.append(
            f"{target}: TX-11 dry-run requires the exact legacy header; "
            f"expected {','.join(LEGACY_HEADER)}, found {','.join(fieldnames)}"
        )
        return ValidationResult(False, messages)
    if not rows:
        return ValidationResult(False, [f"{target}: trace migration input is empty"])

    trace_ids = [row["trace_id"] for row in rows]
    requirement_ids = [row["phase0_selector"] for row in rows]
    messages.extend(_duplicate_messages(target, "trace ID", trace_ids))
    messages.extend(_duplicate_messages(target, "requirement ID", requirement_ids))

    try:
        schema = load_json(schema_target)
    except RuntimeError as exc:
        return ValidationResult(False, [str(exc)])

    migrated_rows: list[dict[str, str]] = []
    for index, legacy_row in enumerate(rows, start=2):
        if legacy_row.get(None):
            messages.append(f"{target}:{index}: row contains unexpected extra CSV values")
            continue
        missing_values = [field for field in LEGACY_HEADER if legacy_row.get(field) is None]
        if missing_values:
            messages.append(
                f"{target}:{index}: row is missing CSV values for: {', '.join(missing_values)}"
            )
            continue
        try:
            migrated = migrate_legacy_trace_row(legacy_row)
        except (KeyError, ValueError, RuntimeError) as exc:
            messages.append(f"{target}:{index}: migration failed: {exc}")
            continue
        errors = validate_instance(migrated, schema)
        messages.extend(
            f"{target}:{index}: generalized row invalid: {error}" for error in errors
        )
        reversed_row = reverse_generalized_trace_row(migrated)
        expected_legacy = {field: legacy_row[field] for field in LEGACY_HEADER}
        if reversed_row != expected_legacy:
            messages.append(f"{target}:{index}: generalized row is not exactly reversible")
        migrated_rows.append(migrated)

    migrated_trace_ids = [row["trace_id"] for row in migrated_rows]
    migrated_requirement_ids = [row["requirement_id"] for row in migrated_rows]
    if len(migrated_rows) != len(rows):
        messages.append(
            f"{target}: row-count parity failed: legacy={len(rows)} migrated={len(migrated_rows)}"
        )
    if set(migrated_trace_ids) != set(trace_ids):
        messages.append(f"{target}: trace-ID parity failed")
    if set(migrated_requirement_ids) != set(requirement_ids):
        messages.append(f"{target}: requirement-ID parity failed")
    if _sha256(target) != before_hash:
        messages.append(f"{target}: source registry changed during dry-run")

    if messages:
        return ValidationResult(False, messages)

    return ValidationResult(
        True,
        [
            f"{target}: TX-11 requirement trace migration dry-run passed",
            f"legacy_sha256={before_hash}",
            f"rows={len(rows)} trace_ids={len(set(trace_ids))} "
            f"requirement_ids={len(set(requirement_ids))}",
            f"coverage_status: {_format_counts(migrated_rows, 'coverage_status')}",
            f"applicability_status: {_format_counts(migrated_rows, 'applicability_status')}",
            f"capability_status: {_format_counts(migrated_rows, 'capability_status')}",
            f"verification_status: {_format_counts(migrated_rows, 'verification_status')}",
            f"evidence_status: {_format_counts(migrated_rows, 'evidence_status')}",
            f"semantic_review_verdict: {_format_counts(migrated_rows, 'semantic_review_verdict')}",
            "dry-run only: wrote no trace rows; TX-12 semantic review and data migration remain required",
        ],
    )


def _duplicate_messages(target: Path, label: str, values: list[str]) -> list[str]:
    counts = Counter(values)
    return [
        f"{target}: duplicate {label} {value!r}"
        for value, count in sorted(counts.items())
        if not value or count > 1
    ]


def _format_counts(rows: list[dict[str, str]], field: str) -> str:
    counts = Counter(row[field] for row in rows)
    return ", ".join(f"{key}={counts[key]}" for key in sorted(counts))


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()
