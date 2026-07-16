"""Deterministic structural validation with explicit claim limits."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Mapping

import jsonschema
import yaml

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - exercised on Python 3.10 CI
    import tomli as tomllib

from .._resources import product_root as locate_product_root
from ..domain.models import ValidationIssue, ValidationResult


STRUCTURAL_LIMITATION = (
    "Structural validation does not establish domain truth, stakeholder "
    "acceptance, ethical correctness, production readiness, or operational authority."
)
REQUIRED_TARGET_FILES = (
    "target-system.yaml",
    "governance/mission.md",
    "governance/vision.md",
    "governance/values.md",
    "governance/authority.yaml",
    "requirements/discovery.md",
    "requirements/product-requirements.md",
    "requirements/system-requirements.md",
    "requirements/trace.csv",
    "architecture/context.md",
    "architecture/components.md",
    "architecture/interfaces.md",
    "architecture/deployment.md",
    "runtime/src/README.md",
    "runtime/config/README.md",
    "runtime/adapters/README.md",
    "skills/README.md",
    "contracts/README.md",
    "tests/README.md",
    "operations/runbook.md",
    "operations/monitoring.md",
    "operations/maintenance.md",
    "operations/retirement.md",
    "evidence/acceptance-summary.md",
)
TRACE_FIELDS = {"requirement_id", "artifact", "verification", "status"}


def validate_target_package(root: str | Path) -> ValidationResult:
    target = Path(root).resolve()
    issues: list[ValidationIssue] = []
    evidence: list[str] = []
    for relative in REQUIRED_TARGET_FILES:
        path = target / relative
        if not path.is_file():
            issues.append(
                ValidationIssue("missing_target_artifact", "required artifact missing", relative)
            )
        else:
            evidence.append(relative)
    manifest_path = target / "target-system.yaml"
    if manifest_path.exists():
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(manifest, Mapping):
            issues.append(ValidationIssue("manifest", "manifest must be a mapping"))
        else:
            if manifest.get("authority") != "derivative":
                issues.append(
                    ValidationIssue(
                        "authority",
                        "generated target manifest must remain derivative",
                        "target-system.yaml",
                    )
                )
            if manifest.get("production_ready") is not False:
                issues.append(
                    ValidationIssue(
                        "overclaim",
                        "generated target cannot claim production readiness",
                        "target-system.yaml",
                    )
                )
            try:
                schema_path = locate_product_root() / "contracts/schemas/target-system.schema.json"
                schema = json.loads(schema_path.read_text(encoding="utf-8"))
                for error in jsonschema.Draft202012Validator(schema).iter_errors(manifest):
                    issues.append(
                        ValidationIssue(
                            "manifest_contract",
                            error.message,
                            "target-system.yaml",
                        )
                    )
            except (FileNotFoundError, json.JSONDecodeError) as exc:
                issues.append(ValidationIssue("manifest_contract", str(exc)))
    trace_result = validate_trace(target)
    issues.extend(trace_result.issues)
    evidence.extend(trace_result.evidence)
    return ValidationResult(
        not issues,
        tuple(issues),
        (STRUCTURAL_LIMITATION,),
        tuple(dict.fromkeys(evidence)),
    )


def validate_trace(root: str | Path) -> ValidationResult:
    path = Path(root).resolve() / "requirements/trace.csv"
    if not path.exists():
        return ValidationResult(
            False,
            (ValidationIssue("trace", "trace file is missing", "requirements/trace.csv"),),
        )
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or set(reader.fieldnames) != TRACE_FIELDS:
            return ValidationResult(
                False,
                (
                    ValidationIssue(
                        "trace_contract",
                        "trace header does not match the target contract",
                        "requirements/trace.csv",
                    ),
                ),
            )
        rows = list(reader)
    issues: list[ValidationIssue] = []
    if not rows:
        issues.append(
            ValidationIssue("trace_coverage", "trace requires at least one row")
        )
    ids = [row["requirement_id"] for row in rows]
    if any(not requirement_id for requirement_id in ids):
        issues.append(ValidationIssue("trace_id", "requirement IDs cannot be blank"))
    if len(ids) != len(set(ids)):
        issues.append(ValidationIssue("trace_duplicate", "duplicate requirement IDs"))
    for row in rows:
        target = Path(root).resolve()
        artifact = (target / row["artifact"]).resolve()
        if artifact != target and target not in artifact.parents:
            issues.append(
                ValidationIssue(
                    "trace_artifact",
                    f"traced artifact escapes target workspace: {row['artifact']}",
                    "requirements/trace.csv",
                )
            )
            continue
        if not artifact.exists():
            issues.append(
                ValidationIssue(
                    "trace_artifact",
                    f"traced artifact is missing: {row['artifact']}",
                    "requirements/trace.csv",
                )
            )
    return ValidationResult(
        not issues,
        tuple(issues),
        evidence=("requirements/trace.csv",),
    )


def validate_contracts(product_root: str | Path | None = None) -> ValidationResult:
    root = (
        Path(product_root).resolve()
        if product_root is not None
        else locate_product_root()
    )
    contract_root = root / "contracts"
    issues: list[ValidationIssue] = []
    evidence: list[str] = []
    schemas: dict[str, Mapping[str, Any]] = {}
    for path in sorted(contract_root.rglob("*.schema.json")):
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
            jsonschema.Draft202012Validator.check_schema(value)
        except (json.JSONDecodeError, jsonschema.SchemaError) as exc:
            issues.append(
                ValidationIssue(
                    "schema",
                    f"invalid JSON Schema: {exc}",
                    path.relative_to(root).as_posix(),
                )
            )
            continue
        schemas[path.name] = value
        evidence.append(path.relative_to(root).as_posix())

    if not schemas:
        issues.append(ValidationIssue("schema", "no product schemas were found"))

    examples = {
        "examples/contracts/execution-transaction.example.yaml": "execution-transaction.schema.json",
        "examples/contracts/handoff.example.yaml": "handoff.schema.json",
        "examples/contracts/completion-evidence.example.yaml": "completion-evidence.schema.json",
        "examples/contracts/runtime-state.example.yaml": "runtime-state.schema.json",
        "examples/contracts/decision.example.yaml": "decision.schema.json",
    }
    for example_name, schema_name in examples.items():
        example_path = root / example_name
        schema = schemas.get(schema_name)
        if not example_path.exists() or schema is None:
            issues.append(
                ValidationIssue(
                    "contract_example",
                    f"missing example or schema pair: {example_name} -> {schema_name}",
                )
            )
            continue
        try:
            instance = yaml.safe_load(example_path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            issues.append(
                ValidationIssue("contract_example", str(exc), example_name)
            )
            continue
        errors = sorted(
            jsonschema.Draft202012Validator(schema).iter_errors(instance),
            key=lambda error: list(error.path),
        )
        for error in errors:
            issues.append(
                ValidationIssue(
                    "contract_example",
                    error.message,
                    example_name,
                )
            )
        evidence.append(example_name)

    profile_example = root / "examples/profiles/self-hosting-profile.example.toml"
    profile_schema = schemas.get("self-hosting-profile.schema.json")
    if not profile_example.exists() or profile_schema is None:
        issues.append(
            ValidationIssue(
                "contract_example",
                "missing self-hosting profile example or schema",
            )
        )
    else:
        try:
            instance = tomllib.loads(profile_example.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            issues.append(
                ValidationIssue(
                    "contract_example",
                    str(exc),
                    "examples/profiles/self-hosting-profile.example.toml",
                )
            )
        else:
            for error in jsonschema.Draft202012Validator(profile_schema).iter_errors(
                instance
            ):
                issues.append(
                    ValidationIssue(
                        "contract_example",
                        error.message,
                        "examples/profiles/self-hosting-profile.example.toml",
                    )
                )
            evidence.append("examples/profiles/self-hosting-profile.example.toml")
    return ValidationResult(not issues, tuple(issues), evidence=tuple(evidence))


def validate_assets(product_root: str | Path | None = None) -> ValidationResult:
    root = (
        Path(product_root).resolve()
        if product_root is not None
        else locate_product_root()
    )
    issues: list[ValidationIssue] = []
    evidence: list[str] = []
    catalog_path = root / "assets/skills/catalog.yaml"
    if not catalog_path.exists():
        return ValidationResult(
            False,
            (ValidationIssue("skill_catalog", "product skill catalog is missing"),),
        )
    catalog = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
    entries = catalog.get("skills", []) if isinstance(catalog, Mapping) else []
    if not isinstance(entries, list) or not entries:
        issues.append(
            ValidationIssue("skill_catalog", "product skill catalog has no skills")
        )
    else:
        seen: set[str] = set()
        for entry in entries:
            if not isinstance(entry, Mapping):
                issues.append(
                    ValidationIssue("skill_catalog", "skill entry must be a mapping")
                )
                continue
            skill_id = str(entry.get("skill_id", ""))
            version = str(entry.get("version", ""))
            relative = str(entry.get("path", ""))
            if not skill_id or skill_id in seen:
                issues.append(
                    ValidationIssue("skill_catalog", f"invalid or duplicate skill ID: {skill_id}")
                )
            seen.add(skill_id)
            if not version:
                issues.append(
                    ValidationIssue("skill_catalog", f"skill has no version: {skill_id}")
                )
            source = (root / relative / "SKILL.md").resolve()
            if source != root and root not in source.parents:
                issues.append(
                    ValidationIssue("skill_asset", f"skill path escapes product: {relative}")
                )
                continue
            if not source.is_file():
                issues.append(
                    ValidationIssue(
                        "skill_asset",
                        f"missing product skill source: {relative}/SKILL.md",
                    )
                )
            else:
                evidence.append(source.relative_to(root).as_posix())
    for relative in (
        "contracts/catalogs/artifact-types.yaml",
        "contracts/catalogs/role-types.yaml",
        "contracts/catalogs/skill-types.yaml",
        "assets/assurance/evaluation-protocol.yaml",
        "assets/assurance/self-change-holdout.yaml",
    ):
        path = root / relative
        if not path.is_file():
            issues.append(
                ValidationIssue("asset", f"missing required asset: {relative}")
            )
        else:
            try:
                value = yaml.safe_load(path.read_text(encoding="utf-8"))
            except yaml.YAMLError as exc:
                issues.append(ValidationIssue("asset", str(exc), relative))
                continue
            if not isinstance(value, Mapping):
                issues.append(
                    ValidationIssue("asset", "asset must be a mapping", relative)
                )
            evidence.append(relative)

    typed_catalogs = (
        (
            "assets/skills/catalog.yaml",
            "skills",
            "contracts/schemas/skill.schema.json",
        ),
        (
            "contracts/catalogs/role-types.yaml",
            "roles",
            "contracts/schemas/role.schema.json",
        ),
    )
    for catalog_name, entry_key, schema_name in typed_catalogs:
        catalog_path = root / catalog_name
        schema_path = root / schema_name
        if not catalog_path.exists() or not schema_path.exists():
            continue
        catalog_value = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
        schema_value = json.loads(schema_path.read_text(encoding="utf-8"))
        entries = catalog_value.get(entry_key, []) if isinstance(catalog_value, Mapping) else []
        for index, entry in enumerate(entries):
            for error in jsonschema.Draft202012Validator(schema_value).iter_errors(entry):
                issues.append(
                    ValidationIssue(
                        "asset_contract",
                        error.message,
                        f"{catalog_name}/{entry_key}/{index}",
                    )
                )
    return ValidationResult(not issues, tuple(issues), evidence=tuple(evidence))
