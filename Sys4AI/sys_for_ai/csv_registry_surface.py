"""Focused verification for the bounded CSV registry-governance evidence family."""

from __future__ import annotations

from collections import Counter
import hashlib
from pathlib import Path

from .registry_io import RegistryLoadError, read_registry, read_registry_rows, resolve_registered_path
from .validators import (
    REGISTRY_HEADERS,
    ValidationResult,
    validate_registry_definitions,
    validate_registry_graph,
)


REQUIRED_DEFINITION_FIELDS = (
    "registry_id",
    "path",
    "registry_scope",
    "purpose",
    "owner",
    "authority_status",
    "expected_header",
    "row_id_field",
    "validation_method",
    "promotion_rule",
    "notes",
)
ALLOWED_SCOPES = {"core", "project_specific"}
ALLOWED_AUTHORITIES = {"registry_authority", "generated_derivative"}


def validate_csv_registry_surface(
    registry_dir: str | Path = "registries",
    definitions: str | Path = "registries/registry_definition_registry.csv",
) -> ValidationResult:
    """Verify the five implemented CSV registry requirements fail closed."""

    root = resolve_registered_path(str(registry_dir))
    definitions_path = resolve_registered_path(str(definitions))
    messages: list[str] = []

    structural = validate_registry_definitions(definitions_path)
    if not structural.ok:
        messages.extend(structural.messages)

    try:
        definition_rows = read_registry_rows(definitions_path)
    except RegistryLoadError as exc:
        return ValidationResult(False, [str(exc)])

    definition_ids = [row.get("registry_id", "") for row in definition_rows]
    definition_paths = [row.get("path", "") for row in definition_rows]
    messages.extend(_duplicate_messages(definitions_path, "registry_id", definition_ids))
    messages.extend(_duplicate_messages(definitions_path, "path", definition_paths))

    declared_files: set[str] = set()
    for row in definition_rows:
        registry_id = row.get("registry_id", "")
        label = f"{definitions_path}: {registry_id or '<missing-registry-id>'}"
        for field in REQUIRED_DEFINITION_FIELDS:
            if not row.get(field, "").strip():
                messages.append(f"{label}: {field} must be populated")

        scope = row.get("registry_scope", "")
        if scope not in ALLOWED_SCOPES:
            messages.append(f"{label}: invalid registry_scope {scope!r}")
        authority = row.get("authority_status", "")
        if authority not in ALLOWED_AUTHORITIES:
            messages.append(f"{label}: invalid registry authority class {authority!r}")
        expected_promotion = (
            "generated_derivative_no_promotion"
            if authority == "generated_derivative"
            else "registry_change_transaction"
        )
        if row.get("promotion_rule") != expected_promotion:
            messages.append(
                f"{label}: authority {authority!r} requires promotion_rule {expected_promotion!r}"
            )

        declared_path = Path(row.get("path", ""))
        filename = declared_path.name
        declared_files.add(filename)
        if declared_path.parent.as_posix() != "registries":
            messages.append(f"{label}: path must be directly under registries/")
        registry_path = root / filename
        if not registry_path.exists():
            messages.append(f"{label}: missing declared registry {registry_path}")
            continue

        try:
            header, rows = read_registry(registry_path)
        except RegistryLoadError as exc:
            messages.append(str(exc))
            continue

        expected_header = [part for part in row.get("expected_header", "").split(";") if part]
        if header != expected_header:
            messages.append(
                f"{label}: expected_header does not match {registry_path.name}: "
                f"expected {expected_header!r}, found {header!r}"
            )
        core_header = REGISTRY_HEADERS.get(filename)
        if scope == "core" and core_header is None:
            messages.append(f"{label}: core registry has no executable header contract")
        elif core_header is not None and header != core_header:
            messages.append(f"{label}: live header diverges from executable core contract")

        row_id_field = row.get("row_id_field", "")
        if row_id_field not in header:
            messages.append(f"{label}: row_id_field {row_id_field!r} is not in the expected header")
            continue
        row_ids = [item.get(row_id_field, "") for item in rows]
        blank_count = sum(not value.strip() for value in row_ids)
        if blank_count:
            messages.append(f"{registry_path}: {blank_count} rows have blank {row_id_field}")
        messages.extend(_duplicate_messages(registry_path, row_id_field, row_ids))

    actual_files = {path.name for path in root.glob("*.csv")}
    missing_definitions = sorted(actual_files - declared_files)
    missing_files = sorted(declared_files - actual_files)
    if missing_definitions:
        messages.append(
            f"{definitions_path}: registries without governed definitions: {', '.join(missing_definitions)}"
        )
    if missing_files:
        messages.append(
            f"{definitions_path}: definitions without registry files: {', '.join(missing_files)}"
        )
    missing_core = sorted(set(REGISTRY_HEADERS) - declared_files)
    if missing_core:
        messages.append(f"{definitions_path}: missing core registry definitions: {', '.join(missing_core)}")

    try:
        graph = validate_registry_graph(root)
    except RegistryLoadError as exc:
        messages.append(str(exc))
    else:
        if not graph.ok:
            messages.extend(graph.messages)

    messages.extend(_validate_populated_hashes(root))

    if messages:
        return ValidationResult(False, messages)
    return ValidationResult(
        True,
        [
            "CSV registry surface: 5/5 requirements verified across controlled registry definitions and graph checks.",
            f"Registry definitions: {len(definition_rows)} governed CSV files with stable headers and row IDs.",
            "Malformed rows, missing paths or contracts, orphan derivatives, stale populated hashes, invalid authority classes, and unregistered project-specific registries fail closed.",
        ],
    )


def _duplicate_messages(path: Path, field: str, values: list[str]) -> list[str]:
    duplicates = sorted(value for value, count in Counter(values).items() if value and count > 1)
    return [f"{path}: duplicate {field} {value!r}" for value in duplicates]


def _validate_populated_hashes(root: Path) -> list[str]:
    messages: list[str] = []
    for registry_path in sorted(root.glob("*.csv")):
        try:
            rows = read_registry_rows(registry_path)
        except RegistryLoadError as exc:
            messages.append(str(exc))
            continue
        for row in rows:
            source_hash = row.get("source_hash", "").strip()
            raw_path = row.get("path", "").strip()
            if source_hash in {"", "pending"} or not raw_path:
                continue
            source_path = resolve_registered_path(raw_path, root.parent)
            if not source_path.exists():
                continue
            actual = hashlib.sha256(source_path.read_bytes()).hexdigest()
            if source_hash not in {actual, f"sha256:{actual}"}:
                row_id = next((value for key, value in row.items() if key.endswith("_id") and value), "<row>")
                messages.append(
                    f"{registry_path}: {row_id}: stale populated source_hash for {raw_path}; expected {actual}"
                )
    return messages
