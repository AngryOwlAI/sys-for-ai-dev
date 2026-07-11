"""Focused verification for the bounded YAML control/state evidence family."""

from __future__ import annotations

import ast
from pathlib import Path
import tempfile

from .registry_io import read_registry_rows, resolve_registered_path
from .toml_io import load_toml
from .validators import ValidationResult, validate_control_records
from .yaml_io import YamlLoadError, load_yaml


REQUIRED_CONTROL_FIELDS = (
    "control_record_id",
    "path",
    "record_type",
    "execution_profile",
    "authority_status",
    "owner",
    "validation_contract_id",
    "allowed_writers",
    "allowed_readers",
)
REQUIRED_RECORD_GROUPS = {
    "bounded transactions": {"execution_transaction"},
    "handoffs": {"handoff", "handoff_v0_2"},
    "completion receipts": {"completion_receipt", "completion_receipt_v0_2"},
    "skill/import manifests": {"skill_import_manifest"},
    "portable tracked state": {"program_state"},
    "bounded state snapshots": {"state_snapshot"},
}
REQUIRED_POLICY_TERMS = (
    "ExecutionTransactions",
    "task packets",
    "skill manifests",
    "state snapshots",
    "initialization manifests",
)
UNSAFE_YAML_CALLS = {"load", "full_load", "unsafe_load", "full_load_all", "unsafe_load_all"}


def validate_yaml_control_surface(
    pyproject: str | Path = "pyproject.toml",
    format_profiles: str | Path = "registries/format_profile_registry.csv",
    control_records: str | Path = "registries/control_record_registry.csv",
    policy: str | Path = "docs/configuration_control_wiki_policy.md",
    python_root: str | Path = "sys_for_ai",
) -> ValidationResult:
    """Verify the implemented YAML control/state surface without granting runtime authority."""

    pyproject_path = resolve_registered_path(str(pyproject))
    format_path = resolve_registered_path(str(format_profiles))
    control_path = resolve_registered_path(str(control_records))
    policy_path = resolve_registered_path(str(policy))
    python_path = resolve_registered_path(str(python_root))
    messages: list[str] = []

    try:
        project = load_toml(pyproject_path).get("project", {})
    except RuntimeError as exc:
        return ValidationResult(False, [str(exc)])
    dependencies = project.get("dependencies", []) if isinstance(project, dict) else []
    if not isinstance(dependencies, list) or "PyYAML>=6.0,<7.0" not in dependencies:
        messages.append(f"{pyproject_path}: bounded PyYAML dependency is missing")

    try:
        format_rows = read_registry_rows(format_path)
        control_rows = read_registry_rows(control_path)
    except RuntimeError as exc:
        return ValidationResult(False, [str(exc)])

    yaml_rows = [row for row in format_rows if row.get("format_id") == "fmt_yaml_control"]
    if len(yaml_rows) != 1:
        messages.append(f"{format_path}: expected exactly one fmt_yaml_control row")
    else:
        row = yaml_rows[0]
        expected = {
            "extension": ".yaml",
            "format_family": "YAML",
            "primary_role": "agent_control_state",
            "registry_required": "true",
            "validator_required": "true",
            "default_authority_class": "control_record",
            "secrets_allowed": "false",
        }
        for field, value in expected.items():
            if row.get(field) != value:
                messages.append(f"{format_path}: fmt_yaml_control {field} must be {value!r}")

    record_types = {row.get("record_type", "") for row in control_rows}
    for label, allowed_types in REQUIRED_RECORD_GROUPS.items():
        if not record_types.intersection(allowed_types):
            messages.append(f"{control_path}: missing registered YAML coverage for {label}")

    for index, row in enumerate(control_rows, start=2):
        label = f"{control_path}:{index}"
        for field in REQUIRED_CONTROL_FIELDS:
            if not row.get(field, "").strip():
                messages.append(f"{label}: {field} must be populated for registered YAML control/state artifacts")
        record_path = resolve_registered_path(row.get("path", ""))
        if record_path.suffix.lower() not in {".yaml", ".yml"}:
            messages.append(f"{label}: registered control path must be YAML")
        elif record_path.exists():
            try:
                data = load_yaml(record_path)
            except YamlLoadError as exc:
                messages.append(str(exc))
            else:
                if not isinstance(data, dict):
                    messages.append(f"{record_path}: control/state document root must be a mapping")

    control_result = validate_control_records(control_path)
    if not control_result.ok:
        messages.extend(control_result.messages)

    try:
        policy_text = policy_path.read_text(encoding="utf-8")
    except OSError as exc:
        messages.append(f"Cannot read YAML assignment policy {policy_path}: {exc}")
    else:
        for term in REQUIRED_POLICY_TERMS:
            if term not in policy_text:
                messages.append(f"{policy_path}: missing YAML control/state assignment for {term}")
        if "not canonical" not in policy_text or "Do not hand-edit" not in policy_text:
            messages.append(f"{policy_path}: generated Configuration and Control Wiki boundary is incomplete")

    messages.extend(_unsafe_parser_findings(python_path))
    messages.extend(_probe_unsafe_object_rejection())

    if messages:
        return ValidationResult(False, messages)
    return ValidationResult(
        True,
        [
            "YAML control/state surface: 11/11 requirements verified against registered records, contracts, policy, and safe parsing.",
            f"Registered YAML records: {len(control_rows)}; every row has ownership, authority, writer, contract, and source-path metadata.",
            "Unsafe YAML object construction was rejected and no unsafe PyYAML loader call exists in the reference package.",
        ],
    )


def _unsafe_parser_findings(root: Path) -> list[str]:
    messages: list[str] = []
    for path in sorted(root.glob("**/*.py")):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (OSError, SyntaxError) as exc:
            messages.append(f"{path}: cannot inspect YAML parser calls: {exc}")
            continue
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
                continue
            owner = node.func.value
            if isinstance(owner, ast.Name) and owner.id == "yaml" and node.func.attr in UNSAFE_YAML_CALLS:
                messages.append(f"{path}:{node.lineno}: unsafe yaml.{node.func.attr} call is prohibited")
    return messages


def _probe_unsafe_object_rejection() -> list[str]:
    with tempfile.TemporaryDirectory() as temporary:
        path = Path(temporary) / "unsafe.yaml"
        path.write_text("!!python/object/apply:builtins.str ['unsafe']\n", encoding="utf-8")
        try:
            load_yaml(path)
        except YamlLoadError:
            return []
    return ["yaml.safe_load probe accepted an unsafe Python object-construction tag"]
