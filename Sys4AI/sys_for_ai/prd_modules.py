"""Validators for governed PRD module decomposition."""

from __future__ import annotations

from collections import defaultdict
import hashlib
from pathlib import Path
import re

from .registry_io import read_registry, read_registry_rows, resolve_registered_path
from .validators import ValidationResult, _validate_rows_against_contract


EXPECTED_HEADER = [
    "prd_module_id",
    "path",
    "title",
    "status",
    "subject_layer",
    "authority_scope",
    "owns_requirement_prefixes",
    "references_source_prds",
    "supersedes",
    "source_authority_status",
    "owner_role",
    "validation_status",
    "source_hash",
    "last_validated_at",
    "notes",
]

VALID_STATUSES = {"planned", "draft", "controlled", "canonical_draft", "canonical", "superseded"}
VALID_SOURCE_AUTHORITY_STATUSES = {
    "derivative_draft",
    "controlled",
    "canonical_draft",
    "canonical",
    "superseded",
    "historical_reference",
}
CANONICAL_STATUSES = {"canonical", "canonical_draft"}
PLANNED_TRACE_STATUSES = {"planned", "todo", "not_run", "pending"}
NONOWNING_STATUSES = {"superseded"}
PHASE1_REQUIREMENT_RE = re.compile(r"\bSFA-P1-INIT-[A-Z0-9-]+-\d{3}\b")
NORMATIVE_DEFINITION_RE = re.compile(r"(?m)^`(SFA-(?:CORE|P0|P1|P2)-[^`]+)`:\s")
TX19_SOURCE_PRDS = {
    "PRDs/Sys4AI_phase-0_product_system_design_prd.md",
    "PRDs/Sys4AI_phase-1_implementation_initialization_prd.md",
    "PRDs/Sys4AI_phase-2_walking_skeleton_prd.md",
    "PRDs/Sys4AI_phase-2_strategic_baseline_addendum.md",
}
TX19_COMMON_PROVENANCE_RELATIONSHIPS = {
    ("derives_from", "SRC-PRD-P0"),
    ("derives_from", "SRC-PRD-P1"),
    ("derives_from", "SRC-PRD-P2-WALKING-SKELETON"),
    ("derives_from", "SRC-PRD-P2-STRATEGIC-BASELINE-ADDENDUM"),
    ("supported_by", "SRC-DDR-STRATEGIC-BASELINE-G08-001"),
    ("traces_to", "SRC-PRD-DECOMPOSITION-STRATEGY"),
    ("traces_to", "SRC-STRATEGIC-BASELINE-MIGRATION-PLAN"),
}
TX19_G02_MODULE_IDS = {
    "PRD-MOD-AGENTJOB-CONTINUE",
    "PRD-MOD-SYSTEM-LAYERS-SELF-HOSTING",
    "PRD-MOD-ROLE-GOVERNANCE",
    "PRD-MOD-SKILL-LIFECYCLE",
    "PRD-MOD-VALIDATION-TRACEABILITY",
    "PRD-MOD-TARGET-SYSTEM-GENERATION",
}
TX19_MODULE_MARKERS = {
    "PRD-MOD-INIT-DISCOVERY": (
        "candidate",
        "approval",
        "waiver",
        "brownfield",
        "missing stakeholder",
        "conflict",
    ),
    "PRD-MOD-AGENTJOB-CONTINUE": (
        "historical compatibility",
        "executiontransaction",
        "resume operation",
        "retired",
    ),
    "PRD-MOD-SOURCE-FIRST-MEMORY": (
        "source hash",
        "freshness",
        "ghost authority",
        "approval",
        "version",
    ),
    "PRD-MOD-SYSTEM-LAYERS-SELF-HOSTING": (
        "framework product",
        "meta-agent runtime",
        "host harness",
        "target-system",
    ),
    "PRD-MOD-ROLE-GOVERNANCE": (
        "facilitator",
        "custodian",
        "verifier",
        "approver",
        "impact analyst",
        "evaluator",
        "acceptance",
    ),
    "PRD-MOD-SKILL-LIFECYCLE": (
        "vision-and-values-facilitator",
        "candidate",
        "promotion",
    ),
    "PRD-MOD-VALIDATION-TRACEABILITY": (
        "strategic trace",
        "approval evidence",
        "stale",
        "superseded",
        "capability state",
        "package",
        "structural validation",
    ),
    "PRD-MOD-TARGET-SYSTEM-GENERATION": (
        "target vision",
        "target core values",
        "approval",
        "source hash",
        "coordination pattern",
        "host",
        "trace",
    ),
    "PRD-MOD-OPERATIONS-MAINTENANCE": (
        "design",
        "develop",
        "implement",
        "test",
        "run",
        "maintain",
        "improve",
        "retire",
        "value drift",
        "rollback",
    ),
    "PRD-MOD-INTERFACE-INTEGRATION": (
        "host",
        "tool",
        "data",
        "external service",
        "connector",
        "sub-agent",
        "target runtime",
    ),
    "PRD-MOD-SECURITY-SAFETY-ASSURANCE": (
        "values shall not",
        "sensitive",
        "permission expansion",
    ),
    "PRD-MOD-DOMAIN-PACK": (
        "domain values",
        "evidence",
        "approval",
        "governance floor",
    ),
}
RETIRED_ACTIVE_PHRASES = {
    "define bounded agentjob execution",
    "one-agentjob continuation loop",
    "perform one agentjob per invocation",
}


def validate_prd_modules(path: str | Path = "registries/prd_module_registry.csv") -> ValidationResult:
    """Validate the PRD module registry and active module file metadata."""

    target = Path(path)
    messages: list[str] = []
    if not target.exists():
        return ValidationResult(False, [f"{target}: missing PRD module registry"])

    header, rows = read_registry(target)
    if header != EXPECTED_HEADER:
        messages.append(f"{target}: header mismatch. Expected {EXPECTED_HEADER!r}, found {header!r}")

    row_result = _validate_rows_against_contract(
        target,
        "schemas/contracts/prd_module_registry_row.schema.json",
        "prd_module_id",
    )
    if not row_result.ok:
        messages.extend(row_result.messages)

    known_layers = _known_values(target.parent / "system_layer_registry.csv", "layer_id")
    known_roles = _known_values(target.parent / "role_registry.csv", "role_id")
    trace_path = target.parent / "requirement_trace_registry.csv"
    requirement_trace_blob = _requirement_trace_blob(trace_path)
    canonical_owners: dict[str, list[str]] = defaultdict(list)
    intended_rows: list[tuple[str, list[str]]] = []
    referenced_source_prds: set[str] = set()
    strategic_module_ids: set[str] = set()
    seen_ids: set[str] = set()

    for index, row in enumerate(rows, start=2):
        module_id = row.get("prd_module_id", "")
        label = f"{target}:{index}: {module_id or '<missing>'}"
        if not module_id:
            messages.append(f"{label}: missing prd_module_id")
        elif module_id in seen_ids:
            messages.append(f"{label}: duplicate prd_module_id")
        else:
            seen_ids.add(module_id)

        for field in EXPECTED_HEADER:
            if field in {"supersedes", "notes"}:
                continue
            if not row.get(field, "").strip():
                messages.append(f"{label}: missing required field {field}")

        status = row.get("status", "")
        authority_status = row.get("source_authority_status", "")
        if status not in VALID_STATUSES:
            messages.append(f"{label}: unknown status {status!r}")
        if authority_status not in VALID_SOURCE_AUTHORITY_STATUSES:
            messages.append(f"{label}: unknown source_authority_status {authority_status!r}")
        if status in {"planned", "draft"} and authority_status in CANONICAL_STATUSES:
            messages.append(f"{label}: {status} module cannot claim {authority_status} authority")

        subject_layer = row.get("subject_layer", "")
        if known_layers and subject_layer not in known_layers:
            messages.append(f"{label}: unknown subject_layer {subject_layer!r}")
        owner_role = row.get("owner_role", "")
        if known_roles and owner_role not in known_roles:
            messages.append(f"{label}: unknown owner_role {owner_role!r}")

        source_prds = _split_list(row.get("references_source_prds", ""))
        referenced_source_prds.update(source_prds)
        if not source_prds:
            messages.append(f"{label}: references_source_prds must name at least one source PRD")
        for source_prd in source_prds:
            if not resolve_registered_path(source_prd).exists():
                messages.append(f"{label}: source PRD not found: {source_prd}")

        supersedes = _split_list(row.get("supersedes", ""))
        for superseded_path in supersedes:
            if superseded_path not in source_prds:
                messages.append(f"{label}: superseded source must remain in references_source_prds: {superseded_path}")

        prefixes = _split_list(row.get("owns_requirement_prefixes", ""))
        if not prefixes:
            messages.append(f"{label}: owns_requirement_prefixes must name at least one prefix")
        if status not in NONOWNING_STATUSES:
            intended_rows.append((module_id, prefixes))
        if authority_status in CANONICAL_STATUSES and status != "superseded":
            for prefix in prefixes:
                canonical_owners[prefix].append(module_id)

        module_path = resolve_registered_path(row.get("path", ""))
        if status == "planned":
            if row.get("validation_status") != "planned":
                messages.append(f"{label}: planned modules must have validation_status planned")
            if module_path.exists():
                messages.extend(_validate_module_file(module_path, row, label))
        else:
            if not module_path.exists():
                messages.append(f"{label}: module file not found: {row.get('path')}")
            else:
                messages.extend(_validate_module_file(module_path, row, label))

        if module_id in TX19_MODULE_MARKERS:
            strategic_module_ids.add(module_id)
            messages.extend(_validate_tx19_module(module_path, row, label, source_prds))

        provenance_messages = _validate_registered_provenance(target.parent, row, label)
        if module_id in TX19_MODULE_MARKERS:
            messages.extend(provenance_messages)
        if (
            row.get("validation_status") not in PLANNED_TRACE_STATUSES
            and module_id not in requirement_trace_blob
            and provenance_messages
        ):
            messages.append(
                f"{label}: neither requirement trace nor complete registered provenance supports validated module"
            )

    for prefix, owners in sorted(canonical_owners.items()):
        if len(owners) > 1:
            messages.append(
                f"{target}: requirement prefix {prefix!r} has multiple canonical owners: {', '.join(sorted(owners))}"
            )

    if strategic_module_ids:
        expected_ids = set(TX19_MODULE_MARKERS)
        missing_ids = sorted(expected_ids - strategic_module_ids)
        unexpected_ids = sorted(strategic_module_ids - expected_ids)
        if missing_ids:
            messages.append(f"{target}: missing TX-19 module rows: {', '.join(missing_ids)}")
        if unexpected_ids:
            messages.append(f"{target}: unexpected TX-19 module rows: {', '.join(unexpected_ids)}")
        if len(rows) != len(expected_ids):
            messages.append(
                f"{target}: TX-19 narrow route requires exactly {len(expected_ids)} module rows; found {len(rows)}"
            )
        missing_sources = sorted(TX19_SOURCE_PRDS - referenced_source_prds)
        if missing_sources:
            messages.append(
                f"{target}: TX-19 modules omit controlling source PRDs: {', '.join(missing_sources)}"
            )

    active_requirements = _active_requirement_ids(trace_path, referenced_source_prds)
    for requirement_id in sorted(active_requirements):
        owners = sorted(
            module_id
            for module_id, prefixes in intended_rows
            if any(_prefix_owns_requirement(prefix, requirement_id) for prefix in prefixes)
        )
        if not owners:
            messages.append(f"{target}: orphan active requirement prefix: {requirement_id}")
        elif len(owners) > 1:
            messages.append(
                f"{target}: active requirement {requirement_id} has multiple intended owners: "
                f"{', '.join(owners)}"
            )

    return ValidationResult(not messages, messages or [f"{target}: PRD module registry validation passed"])


def _validate_module_file(path: Path, row: dict[str, str], label: str) -> list[str]:
    content = path.read_text(encoding="utf-8")
    lower = content.lower()
    messages: list[str] = []
    if "authority notice" not in lower:
        messages.append(f"{label}: module file missing authority notice")
    if "source prds" not in lower:
        messages.append(f"{label}: module file missing Source PRDs metadata")
    if row.get("subject_layer", "") not in content:
        messages.append(f"{label}: module file missing subject layer {row.get('subject_layer')!r}")
    if row.get("source_authority_status", "") not in content:
        messages.append(
            f"{label}: module file missing source authority status {row.get('source_authority_status')!r}"
        )
    module_id = row.get("prd_module_id", "")
    if module_id and module_id not in content:
        messages.append(f"{label}: module file missing module ID {module_id!r}")

    metadata_prefixes = _metadata_values(content, "Owns requirement prefixes")
    row_prefixes = _split_list(row.get("owns_requirement_prefixes", ""))
    if metadata_prefixes != row_prefixes:
        messages.append(
            f"{label}: module ownership metadata does not match registry row: "
            f"{metadata_prefixes!r} != {row_prefixes!r}"
        )

    metadata_sources = _metadata_values(content, "Source PRDs")
    row_sources = _split_list(row.get("references_source_prds", ""))
    if metadata_sources != row_sources:
        messages.append(
            f"{label}: module Source PRDs metadata does not match registry row: "
            f"{metadata_sources!r} != {row_sources!r}"
        )

    definitions = NORMATIVE_DEFINITION_RE.findall(content)
    if definitions:
        messages.append(
            f"{label}: derivative module restates requirements as normative definitions: "
            f"{', '.join(sorted(set(definitions)))}"
        )

    source_hash = row.get("source_hash", "")
    if source_hash and source_hash != "pending":
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if source_hash != actual_hash:
            messages.append(f"{label}: source_hash does not match module file SHA-256")
    if row.get("validation_status") == "validated" and source_hash == "pending":
        messages.append(f"{label}: validated module cannot retain a pending source_hash")
    return messages


def _validate_tx19_module(
    path: Path,
    row: dict[str, str],
    label: str,
    source_prds: list[str],
) -> list[str]:
    messages: list[str] = []
    if not path.exists():
        return messages
    content = path.read_text(encoding="utf-8")
    lower = content.lower()

    if row.get("status") != "draft" or row.get("source_authority_status") != "derivative_draft":
        messages.append(f"{label}: TX-19 modules must remain draft and derivative_draft")
    if row.get("validation_status") != "validated":
        messages.append(f"{label}: TX-19 module row must record validation_status validated")
    if "tx-19-modules" not in lower:
        messages.append(f"{label}: module file missing TX-19-MODULES regeneration provenance")
    if "ddr-sfadev-strategic-baseline-g08-001" not in lower:
        messages.append(f"{label}: module file missing G-08 approval provenance")
    missing_sources = sorted(TX19_SOURCE_PRDS - set(source_prds))
    if missing_sources:
        messages.append(f"{label}: module row missing TX-19 source PRDs: {', '.join(missing_sources)}")
    for marker in TX19_MODULE_MARKERS[row["prd_module_id"]]:
        if marker not in lower:
            messages.append(f"{label}: module file missing required TX-19 content marker {marker!r}")

    if row["prd_module_id"] == "PRD-MOD-AGENTJOB-CONTINUE":
        for phrase in RETIRED_ACTIVE_PHRASES:
            if phrase in lower:
                messages.append(f"{label}: retired execution phrase remains active: {phrase!r}")
    return messages


def _known_values(path: Path, field: str) -> set[str]:
    if not path.exists():
        return set()
    return {row.get(field, "") for row in read_registry_rows(path) if row.get(field)}


def _requirement_trace_blob(path: Path) -> str:
    if not path.exists():
        return ""
    return "\n".join(";".join(row.values()) for row in read_registry_rows(path))


def _active_requirement_ids(trace_path: Path, source_prds: set[str]) -> set[str]:
    requirement_ids: set[str] = set()
    if trace_path.exists():
        for row in read_registry_rows(trace_path):
            if row.get("requirement_lifecycle") != "active":
                continue
            if row.get("applicability_status") != "required":
                continue
            requirement_id = row.get("requirement_id", "").strip()
            if requirement_id:
                requirement_ids.add(requirement_id)

    for source_prd in source_prds:
        if not source_prd.endswith("Sys4AI_phase-1_implementation_initialization_prd.md"):
            continue
        source_path = resolve_registered_path(source_prd)
        if source_path.exists():
            requirement_ids.update(PHASE1_REQUIREMENT_RE.findall(source_path.read_text(encoding="utf-8")))
    return requirement_ids


def _prefix_owns_requirement(prefix: str, requirement_id: str) -> bool:
    normalized = prefix.rstrip("*").rstrip("-")
    return requirement_id == normalized or requirement_id.startswith(f"{normalized}-")


def _metadata_values(content: str, label: str) -> list[str]:
    match = re.search(rf"^\*\*{re.escape(label)}:\*\*\s*(.+)$", content, re.MULTILINE)
    return _split_list(match.group(1).strip()) if match else []


def _validate_registered_provenance(registry_root: Path, row: dict[str, str], label: str) -> list[str]:
    source_path = registry_root / "source_registry.csv"
    relationships_path = registry_root / "object_relationship_registry.csv"
    if not source_path.exists() or not relationships_path.exists():
        return [f"{label}: source or object-relationship registry is missing"]

    module_path = row.get("path", "")
    source_row = next(
        (item for item in read_registry_rows(source_path) if item.get("path") == module_path),
        None,
    )
    if source_row is None:
        return [f"{label}: module path is not registered in source_registry.csv"]
    if source_row.get("authority_status") != "derivative_draft":
        return [f"{label}: registered module source must remain derivative_draft"]

    source_id = source_row.get("source_id", "")
    provenance_relationships = {
        (item.get("predicate", ""), item.get("object_id", ""))
        for item in read_registry_rows(relationships_path)
        if item.get("subject_id") == source_id
    }
    required_relationships = set(TX19_COMMON_PROVENANCE_RELATIONSHIPS)
    if row.get("prd_module_id") in TX19_G02_MODULE_IDS:
        required_relationships.add(("supported_by", "SRC-DDR-STRATEGIC-BASELINE-001"))
    missing = sorted(required_relationships - provenance_relationships)
    if missing:
        formatted = ", ".join(f"{predicate} -> {object_id}" for predicate, object_id in missing)
        return [f"{label}: registered module provenance omits {formatted}"]
    return []


def _split_list(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]
