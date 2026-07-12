"""Focused verification for the bounded Markdown source-authority evidence family."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from .csv_registry_surface import validate_csv_registry_surface
from .registry_io import RegistryLoadError, read_registry_rows, resolve_registered_path
from .validators import ValidationResult


MARKDOWN_PROFILE = {
    "extension": ".md",
    "format_family": "Markdown",
    "primary_role": "human_authored_source",
    "registry_required": "true",
    "default_authority_class": "source_document",
    "promotion_rule": "source_promotion_transaction",
}
CSV_PROFILE = {
    "extension": ".csv",
    "format_family": "CSV",
    "primary_role": "registry_ledger",
    "canonical_roots": "registries/",
    "registry_required": "true",
    "validator_required": "true",
    "default_authority_class": "registry_row",
    "promotion_rule": "registry_change_transaction",
}
REQUIRED_MARKDOWN_SOURCES = {
    "SRC-PRD-P0": "PRD",
    "SRC-SYSTEM-DOCUMENT-SPINE": "policy",
    "SRC-ROOT-README": "guide",
    "SRC-RDR-STRATEGIC-BASELINE-001": "requirements artifact",
    "SRC-TEMPLATE-RDR": "template",
    "SRC-SKILL-SOURCE-FIRST-MEMORY-RUNTIME": "source documentation",
}
SOURCE_AUTHORITY_CLASSES = {"canonical", "canonical_draft", "controlled", "derivative_draft"}
DERIVATIVE_AUTHORITY_CLASSES = {"derivative_draft", "generated_derivative"}
MARKDOWN_POLICY_TERMS = (
    "Markdown is for human-authored PRDs, policies, guides, templates, and source documentation.",
    "Generated derivatives, local vault notes, semantic caches, and summaries do not become canonical",
    "unless a future ExecutionTransaction explicitly promotes them through a source-authority workflow.",
)


def validate_markdown_source_surface(
    format_profiles: str | Path = "registries/format_profile_registry.csv",
    sources: str | Path = "registries/source_registry.csv",
    derivatives: str | Path = "registries/derivative_registry.csv",
    policy: str | Path = "docs/format_profile_policy.md",
    generated_root: str | Path = "docs/generated",
    registry_dir: str | Path = "registries",
    registry_definitions: str | Path = "registries/registry_definition_registry.csv",
    product_root: str | Path = ".",
) -> ValidationResult:
    """Verify three Markdown requirements and the CSV role assignment fail closed."""

    root = Path(product_root).resolve()
    format_path = resolve_registered_path(str(format_profiles), root)
    source_path = resolve_registered_path(str(sources), root)
    derivative_path = resolve_registered_path(str(derivatives), root)
    policy_path = resolve_registered_path(str(policy), root)
    generated_path = resolve_registered_path(str(generated_root), root)
    messages: list[str] = []

    try:
        format_rows = read_registry_rows(format_path)
        source_rows = read_registry_rows(source_path)
        derivative_rows = read_registry_rows(derivative_path)
    except RegistryLoadError as exc:
        return ValidationResult(False, [str(exc)])

    formats_by_id = {row.get("format_id", ""): row for row in format_rows}
    _check_profile(format_path, formats_by_id.get("fmt_markdown_source"), MARKDOWN_PROFILE, messages)
    _check_profile(format_path, formats_by_id.get("fmt_csv_registry"), CSV_PROFILE, messages)

    try:
        policy_text = policy_path.read_text(encoding="utf-8")
    except OSError as exc:
        messages.append(f"Cannot read Markdown policy {policy_path}: {exc}")
    else:
        for term in MARKDOWN_POLICY_TERMS:
            if term not in policy_text:
                messages.append(f"{policy_path}: missing Markdown authority term {term!r}")

    source_ids = [row.get("source_id", "") for row in source_rows]
    messages.extend(_duplicates(source_path, "source_id", source_ids))
    sources_by_id = {row.get("source_id", ""): row for row in source_rows}

    markdown_rows = [row for row in source_rows if row.get("path", "").endswith(".md")]
    messages.extend(
        _duplicates(source_path, "Markdown path", [row.get("path", "") for row in markdown_rows])
    )
    if not markdown_rows:
        messages.append(f"{source_path}: no registered Markdown source artifacts")
    for row in markdown_rows:
        source_id = row.get("source_id", "") or "<missing-source-id>"
        authority = row.get("authority_status", "")
        if authority not in SOURCE_AUTHORITY_CLASSES:
            messages.append(f"{source_path}: {source_id}: invalid or missing Markdown authority {authority!r}")
        registered = resolve_registered_path(row.get("path", ""), root)
        if not registered.is_file():
            messages.append(f"{source_path}: {source_id}: missing registered Markdown source {registered}")
        if _is_within(registered, generated_path):
            messages.append(
                f"{source_path}: {source_id}: generated Markdown cannot be registered as source authority"
            )

    for source_id, role in REQUIRED_MARKDOWN_SOURCES.items():
        row = sources_by_id.get(source_id)
        if row is None:
            messages.append(f"{source_path}: missing representative registered Markdown {role} {source_id}")
            continue
        if not row.get("path", "").endswith(".md"):
            messages.append(f"{source_path}: {source_id}: representative {role} must be Markdown")
        if row.get("authority_status", "") not in SOURCE_AUTHORITY_CLASSES:
            messages.append(f"{source_path}: {source_id}: representative {role} lacks governed authority")

    derivative_ids = [row.get("derivative_id", "") for row in derivative_rows]
    derivative_paths = [row.get("path", "") for row in derivative_rows]
    messages.extend(_duplicates(derivative_path, "derivative_id", derivative_ids))
    messages.extend(_duplicates(derivative_path, "path", derivative_paths))

    markdown_derivatives = [row for row in derivative_rows if row.get("path", "").endswith(".md")]
    registered_derivative_paths: set[Path] = set()
    for row in markdown_derivatives:
        derivative_id = row.get("derivative_id", "") or "<missing-derivative-id>"
        status = row.get("status", "")
        if status not in DERIVATIVE_AUTHORITY_CLASSES:
            messages.append(
                f"{derivative_path}: {derivative_id}: generated Markdown has invalid authority {status!r}"
            )
        if not row.get("source_ids", "").strip():
            messages.append(f"{derivative_path}: {derivative_id}: generated Markdown lacks source trace")
        if not row.get("generation_method", "").strip():
            messages.append(f"{derivative_path}: {derivative_id}: generated Markdown lacks generation method")
        registered = resolve_registered_path(row.get("path", ""), root)
        registered_derivative_paths.add(registered.resolve())
        if not registered.is_file():
            messages.append(f"{derivative_path}: {derivative_id}: missing generated Markdown {registered}")

    actual_generated_paths = (
        {path.resolve() for path in generated_path.rglob("*.md")} if generated_path.is_dir() else set()
    )
    unregistered = sorted(actual_generated_paths - registered_derivative_paths)
    outside_root = sorted(
        path for path in registered_derivative_paths if not _is_within(path, generated_path)
    )
    if unregistered:
        messages.append(
            f"{generated_path}: unregistered generated Markdown: "
            + ", ".join(str(path) for path in unregistered)
        )
    if outside_root:
        messages.append(
            f"{derivative_path}: generated Markdown registered outside {generated_path}: "
            + ", ".join(str(path) for path in outside_root)
        )

    csv_result = validate_csv_registry_surface(registry_dir, registry_definitions)
    if not csv_result.ok:
        messages.extend(f"CSV role assignment: {message}" for message in csv_result.messages)

    if messages:
        return ValidationResult(False, messages)
    return ValidationResult(
        True,
        [
            "Markdown source surface: 4/4 requirements verified across source authority, derivative classification, and CSV role assignment.",
            f"Registered Markdown: {len(markdown_rows)} source rows with explicit authority; {len(markdown_derivatives)} generated derivative rows are noncanonical and source-traced.",
            "Generated Markdown source inversions, missing authority, missing source trace, unregistered generated pages, and CSV assignment drift fail closed.",
        ],
    )


def _check_profile(
    path: Path,
    row: dict[str, str] | None,
    expected: dict[str, str],
    messages: list[str],
) -> None:
    format_id = "fmt_markdown_source" if expected is MARKDOWN_PROFILE else "fmt_csv_registry"
    if row is None:
        messages.append(f"{path}: missing required format profile {format_id}")
        return
    for field, value in expected.items():
        if row.get(field) != value:
            messages.append(f"{path}: {format_id} {field} must be {value!r}")


def _duplicates(path: Path, field: str, values: list[str]) -> list[str]:
    duplicates = sorted(value for value, count in Counter(values).items() if value and count > 1)
    return [f"{path}: duplicate {field} {value!r}" for value in duplicates]


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True
