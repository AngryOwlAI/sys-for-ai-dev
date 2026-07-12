"""Focused verification for the bounded JSON Schema contract evidence family."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from .derivatives import check_validation_contracts_catalog
from .jsonschema_io import JsonSchemaLoadError, check_schema, load_json
from .registry_io import RegistryLoadError, read_registry_rows, resolve_registered_path
from .validators import (
    ValidationResult,
    validate_jsonschema_contracts,
    validate_validation_contract_registry,
)


DRAFT_2020_12 = "https://json-schema.org/draft/2020-12/schema"
JSONSCHEMA_PROFILE = {
    "extension": ".schema.json",
    "format_family": "JSON Schema",
    "primary_role": "validation_contract",
    "canonical_roots": "schemas/contracts/",
    "derivative_surfaces": "validation_contracts_catalog",
    "registry_required": "true",
    "validator_required": "true",
    "default_authority_class": "validation_contract",
    "promotion_rule": "contract_change_transaction",
    "secrets_allowed": "false",
}
REQUIRED_CONTRACT_FIELDS = (
    "contract_id",
    "path",
    "dialect",
    "target_format",
    "target_artifact_type",
    "target_glob",
    "authority_status",
    "lifecycle_status",
    "owner",
    "validator_command",
)
REQUIRED_TARGET_FORMATS = {"json", "yaml", "toml", "csv", "markdown"}
REQUIRED_FORMAT_POLICY_TERMS = (
    "JSON Schema is for executable validation contracts.",
    "JSON Schema contracts require schema checks against the declared dialect.",
    "JSON Schema contracts are surfaced through the generated Validation Contracts Catalog.",
)
REQUIRED_CATALOG_POLICY_TERMS = (
    "JSON Schema is a validation-contract format, not a narrative memory format.",
    "Phase 1 creates a Validation Contracts Catalog, not a standalone JSON wiki.",
    "JSON Schema validation proves structural admissibility only.",
    "Schema changes that affect existing controlled artifacts require supersession notes and migration evidence",
)


def validate_jsonschema_contract_surface(
    format_profiles: str | Path = "registries/format_profile_registry.csv",
    validation_contracts: str | Path = "registries/validation_contract_registry.csv",
    derivatives: str | Path = "registries/derivative_registry.csv",
    schemas_root: str | Path = "schemas/contracts",
    format_policy: str | Path = "docs/format_profile_policy.md",
    catalog_policy: str | Path = "docs/validation_contracts_catalog_policy.md",
    generated_index: str | Path = "docs/generated/validation_contracts/index.md",
    generated_by_target: str | Path = "docs/generated/validation_contracts/contracts-by-target.md",
    product_root: str | Path = ".",
) -> ValidationResult:
    """Verify seven core JSON Schema requirements and three Phase 0 assignments."""

    root = Path(product_root).resolve()
    format_path = resolve_registered_path(str(format_profiles), root)
    contract_path = resolve_registered_path(str(validation_contracts), root)
    derivative_path = resolve_registered_path(str(derivatives), root)
    schema_root = resolve_registered_path(str(schemas_root), root)
    format_policy_path = resolve_registered_path(str(format_policy), root)
    catalog_policy_path = resolve_registered_path(str(catalog_policy), root)
    generated_paths = (
        resolve_registered_path(str(generated_index), root),
        resolve_registered_path(str(generated_by_target), root),
    )
    messages: list[str] = []

    try:
        format_rows = read_registry_rows(format_path)
        contract_rows = read_registry_rows(contract_path)
        derivative_rows = read_registry_rows(derivative_path)
    except RegistryLoadError as exc:
        return ValidationResult(False, [str(exc)])

    profiles = [row for row in format_rows if row.get("format_id") == "fmt_jsonschema_contract"]
    if len(profiles) != 1:
        messages.append(f"{format_path}: expected exactly one fmt_jsonschema_contract row")
    else:
        for field, value in JSONSCHEMA_PROFILE.items():
            if profiles[0].get(field) != value:
                messages.append(f"{format_path}: fmt_jsonschema_contract {field} must be {value!r}")

    contract_ids = [row.get("contract_id", "") for row in contract_rows]
    contract_paths = [row.get("path", "") for row in contract_rows]
    messages.extend(_duplicates(contract_path, "contract_id", contract_ids))
    messages.extend(_duplicates(contract_path, "path", contract_paths))
    if not contract_rows:
        messages.append(f"{contract_path}: no registered JSON Schema contracts")

    rows_by_id = {row.get("contract_id", ""): row for row in contract_rows}
    schema_ids: list[str] = []
    registered_paths: set[Path] = set()
    for index, row in enumerate(contract_rows, start=2):
        contract_id = row.get("contract_id", "") or f"row-{index}"
        label = f"{contract_path}:{index}: {contract_id}"
        for field in REQUIRED_CONTRACT_FIELDS:
            if not row.get(field, "").strip():
                messages.append(f"{label}: {field} must be populated")
        if row.get("dialect") != "2020-12":
            messages.append(f"{label}: dialect must be '2020-12'")
        if row.get("target_format") not in REQUIRED_TARGET_FORMATS:
            messages.append(f"{label}: unsupported target_format {row.get('target_format')!r}")

        schema_path = resolve_registered_path(row.get("path", ""), root)
        registered_paths.add(schema_path.resolve())
        if not schema_path.name.endswith(".schema.json"):
            messages.append(f"{label}: contract path must end with .schema.json")
            continue
        try:
            schema = load_json(schema_path)
        except JsonSchemaLoadError as exc:
            messages.append(str(exc))
            continue
        for error in check_schema(schema):
            messages.append(f"{schema_path}: invalid Draft 2020-12 schema: {error}")
        if schema.get("$schema") != DRAFT_2020_12:
            messages.append(f"{schema_path}: $schema must declare Draft 2020-12")
        schema_id = schema.get("$id")
        if not isinstance(schema_id, str) or not schema_id.strip():
            messages.append(f"{schema_path}: $id must be populated")
        else:
            schema_ids.append(schema_id)
            if not schema_id.endswith(f"/{schema_path.name}"):
                messages.append(f"{schema_path}: $id must end with /{schema_path.name}")

        supersedes = row.get("supersedes", "").strip()
        if supersedes:
            predecessor = rows_by_id.get(supersedes)
            if predecessor is None:
                messages.append(f"{label}: supersedes unknown contract {supersedes!r}")
            else:
                if predecessor.get("lifecycle_status") != "superseded":
                    messages.append(f"{label}: superseded contract {supersedes} must have lifecycle_status 'superseded'")
                if row.get("lifecycle_status") != "current":
                    messages.append(f"{label}: successor contract must have lifecycle_status 'current'")
            messages.extend(_migration_evidence_errors(label, row.get("notes", ""), root))

    messages.extend(_duplicates(contract_path, "$id", schema_ids))
    discovered_paths = {path.resolve() for path in schema_root.glob("*.schema.json")}
    for path in sorted(discovered_paths - registered_paths):
        messages.append(f"{path}: JSON Schema contract is not registered")
    for path in sorted(registered_paths - discovered_paths):
        messages.append(f"{path}: registered contract is outside or absent from {schema_root}")

    missing_formats = REQUIRED_TARGET_FORMATS - {row.get("target_format", "") for row in contract_rows}
    if missing_formats:
        messages.append(f"{contract_path}: missing governed target formats {sorted(missing_formats)}")

    structural = validate_validation_contract_registry(contract_path)
    if not structural.ok:
        messages.extend(structural.messages)
    schemas = validate_jsonschema_contracts(schema_root)
    if not schemas.ok:
        messages.extend(schemas.messages)

    messages.extend(_policy_errors(format_policy_path, REQUIRED_FORMAT_POLICY_TERMS))
    messages.extend(_policy_errors(catalog_policy_path, REQUIRED_CATALOG_POLICY_TERMS))
    messages.extend(_json_wiki_errors(derivative_path, derivative_rows, root))
    messages.extend(_catalog_errors(generated_paths, contract_rows))
    generated = check_validation_contracts_catalog(root)
    if not generated.ok:
        messages.extend(generated.messages)

    if messages:
        return ValidationResult(False, sorted(dict.fromkeys(messages)))
    return ValidationResult(
        True,
        [
            "JSON Schema contract surface: 10/10 requirements verified across assignment, registration, dialect, target metadata, structural limits, cataloging, no-wiki policy, and migration controls.",
            f"Registered JSON Schema: {len(contract_rows)} unique Draft 2020-12 contracts with complete governed metadata and one-to-one source registration.",
            "Profile drift, missing metadata, duplicate IDs or paths, dialect and schema errors, stale catalogs, standalone JSON wikis, and unproved supersession fail closed.",
        ],
    )


def _duplicates(path: Path, field: str, values: list[str]) -> list[str]:
    duplicates = sorted(value for value, count in Counter(values).items() if value and count > 1)
    return [f"{path}: duplicate {field} {value!r}" for value in duplicates]


def _policy_errors(path: Path, terms: tuple[str, ...]) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"Cannot read JSON Schema policy {path}: {exc}"]
    return [f"{path}: missing JSON Schema policy term {term!r}" for term in terms if term not in text]


def _migration_evidence_errors(label: str, notes: str, root: Path) -> list[str]:
    marker = "migration_evidence="
    if marker not in notes:
        return [f"{label}: supersession requires migration_evidence=path[;path]"]
    value = notes.split(marker, 1)[1].split()[0]
    paths = [item for item in value.split(";") if item]
    if not paths:
        return [f"{label}: supersession migration evidence is empty"]
    return [
        f"{label}: missing migration evidence path {path}"
        for path in paths
        if not resolve_registered_path(path, root).exists()
    ]


def _json_wiki_errors(path: Path, rows: list[dict[str, str]], root: Path) -> list[str]:
    messages: list[str] = []
    for index, row in enumerate(rows, start=2):
        identity = " ".join(
            (row.get("derivative_id", ""), row.get("derivative_type", ""), row.get("path", ""))
        ).lower()
        if "json_wiki" in identity or "json-wiki" in identity or "/json/" in identity:
            messages.append(f"{path}:{index}: standalone JSON wiki is outside the approved Phase 1 surface")
    json_root = root / "docs/generated/json"
    if json_root.exists():
        messages.append(f"{json_root}: standalone JSON wiki is outside the approved Phase 1 surface")
    return messages


def _catalog_errors(paths: tuple[Path, Path], rows: list[dict[str, str]]) -> list[str]:
    messages: list[str] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            messages.append(f"Cannot read generated Validation Contracts Catalog {path}: {exc}")
            continue
        if "generated reader surface. It is not canonical" not in text:
            messages.append(f"{path}: catalog lacks noncanonical authority notice")
        if "structural" not in text.lower() or "semantic truth" not in text.lower():
            messages.append(f"{path}: catalog lacks structural-only limitation")
        for row in rows:
            if row.get("contract_id", "") not in text or row.get("path", "") not in text:
                messages.append(f"{path}: stale catalog omits {row.get('contract_id')} at {row.get('path')}")
    return messages
