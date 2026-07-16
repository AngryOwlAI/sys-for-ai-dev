"""Fail-closed validation for the Sys4AI development repository."""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


TEXT_SUFFIXES = {
    ".cfg",
    ".csv",
    ".ini",
    ".json",
    ".md",
    ".py",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}
SKIP_PARTS = {
    ".git",
    ".local",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "build",
    "dist",
}
FORBIDDEN_PRODUCT_TEXT = (
    "SFADEV",
    "Sys4AI-dev",
    "temp_handoff",
    "AJ-P1-",
    "TX-35",
    "../PRDs",
    "../scripts",
    ".agents/skills",
    "sys_for_ai",
)
FORBIDDEN_PRODUCT_PATH_PARTS = {
    "control_records",
    "registries",
    "sys_for_ai",
}
REQUIRED_ROOT_PATHS = (
    "README.md",
    "SYSTEM_MAP.md",
    "PROJECT_STATUS.md",
    "CHANGELOG.md",
    "PRDs/active/Sys4AI_product_baseline_prd.md",
    "PRDs/active/Sys4AI_repository_reboot_prd.md",
    "architecture/README.md",
    "decisions/README.md",
    "implementation_plans/active/repository-reboot-implementation-plan.md",
    "development/bootstrap-agent/skills",
    "development/state/current-work.yaml",
    "development/catalog/artifacts.yaml",
    "development/catalog/skills.yaml",
    "development/catalog/decisions.yaml",
    "development/trace/requirements.csv",
    "Sys4AI/pyproject.toml",
    "integration/tests",
)
TRACE_COLUMNS = {
    "trace_id",
    "requirement_id",
    "source_path",
    "implementation_paths",
    "validation_evidence",
    "coverage_status",
    "semantic_review",
    "notes",
}


@dataclass(frozen=True)
class Finding:
    check: str
    message: str


def _visible_files(root: Path) -> list[Path]:
    return [
        path
        for path in root.rglob("*")
        if path.is_file()
        and path.suffix.lower() in TEXT_SUFFIXES
        and not any(part in SKIP_PARTS for part in path.parts)
    ]


def validate_structure(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for relative in REQUIRED_ROOT_PATHS:
        if not (root / relative).exists():
            findings.append(Finding("structure", f"missing required path: {relative}"))

    active_plans = sorted((root / "implementation_plans/active").glob("*.md"))
    if len(active_plans) != 1:
        findings.append(
            Finding(
                "planning",
                f"expected exactly one active implementation plan; found {len(active_plans)}",
            )
        )
    active_prds = sorted((root / "PRDs/active").glob("*.md"))
    if len(active_prds) != 2:
        findings.append(
            Finding(
                "requirements",
                f"expected product baseline plus one active change PRD; found {len(active_prds)}",
            )
        )
    change_prds = [path for path in active_prds if "product_baseline" not in path.name]
    if len(change_prds) != 1:
        findings.append(
            Finding("requirements", "expected exactly one active change PRD")
        )

    allowed_plan_files = {
        root / "implementation_plans/README.md",
        root
        / "implementation_plans/active/repository-reboot-implementation-plan.md",
        root
        / "implementation_plans/templates/implementation-plan-template.md",
    }
    actual_plan_files = {
        path for path in (root / "implementation_plans").rglob("*") if path.is_file()
    }
    unexpected = sorted(actual_plan_files - allowed_plan_files)
    for path in unexpected:
        findings.append(
            Finding(
                "planning",
                f"historical or unindexed plan artifact in active tree: {path.relative_to(root)}",
            )
        )

    for forbidden in ("temp_handoff", "PRDs/drafts", "PRDs/modules"):
        if (root / forbidden).exists():
            findings.append(
                Finding("history", f"historical active-tree path remains: {forbidden}")
            )
    return findings


def validate_product_boundary(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    product_root = root / "Sys4AI"
    for path in _visible_files(product_root):
        relative = path.relative_to(product_root)
        if any(part in FORBIDDEN_PRODUCT_PATH_PARTS for part in relative.parts):
            findings.append(
                Finding("product-boundary", f"forbidden product path: {relative}")
            )
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for marker in FORBIDDEN_PRODUCT_TEXT:
            if marker in text:
                findings.append(
                    Finding(
                        "product-boundary",
                        f"{relative}: forbidden development reference {marker!r}",
                    )
                )

    pyproject = product_root / "pyproject.toml"
    if pyproject.exists():
        text = pyproject.read_text(encoding="utf-8")
        required = (
            'name = "sys4ai"',
            'sys4ai = "sys4ai.cli:main"',
            'where = ["src"]',
        )
        for marker in required:
            if marker not in text:
                findings.append(
                    Finding("packaging", f"pyproject missing {marker!r}")
                )
    if (product_root / "docs/generated").exists():
        findings.append(
            Finding("derivatives", "tracked product generated-doc directory exists")
        )
    return findings


def _catalog_paths(path: Path) -> list[str]:
    paths: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\s+path:\s*(\S+)\s*$", line)
        if match:
            paths.append(match.group(1))
    return paths


def validate_catalogs(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for relative in (
        "development/catalog/artifacts.yaml",
        "development/catalog/decisions.yaml",
    ):
        catalog = root / relative
        if not catalog.exists():
            continue
        for registered in _catalog_paths(catalog):
            if not (root / registered).exists():
                findings.append(
                    Finding(
                        "catalog",
                        f"{relative}: registered path does not exist: {registered}",
                    )
                )

    skill_index = root / "development/catalog/skills.yaml"
    if skill_index.exists():
        match = re.search(
            r"^canonical_source:\s*(\S+)\s*$",
            skill_index.read_text(encoding="utf-8"),
            re.MULTILINE,
        )
        if not match or not (root / match.group(1)).exists():
            findings.append(
                Finding("catalog", "skill index has no resolvable canonical source")
            )
    return findings


def validate_trace(root: Path) -> list[Finding]:
    path = root / "development/trace/requirements.csv"
    findings: list[Finding] = []
    if not path.exists():
        return [Finding("trace", "missing development requirement trace")]
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or set(reader.fieldnames) != TRACE_COLUMNS:
            return [Finding("trace", "requirement trace header does not match contract")]
        rows = list(reader)
    ids = [row["trace_id"] for row in rows]
    if len(ids) != len(set(ids)):
        findings.append(Finding("trace", "duplicate trace IDs"))
    requirement_ids = {row["requirement_id"] for row in rows}
    expected = {f"RB-{index:03d}" for index in range(1, 25)}
    expected.update({f"RNFR-{index:03d}" for index in range(1, 7)})
    missing = sorted(expected - requirement_ids)
    if missing:
        findings.append(Finding("trace", f"missing requirement coverage: {missing}"))
    for row in rows:
        label = row["trace_id"]
        source = root / row["source_path"]
        if not source.exists():
            findings.append(Finding("trace", f"{label}: source path missing"))
        elif row["requirement_id"] not in source.read_text(encoding="utf-8"):
            findings.append(
                Finding("trace", f"{label}: requirement ID absent from source")
            )
        for implementation in row["implementation_paths"].split(";"):
            if implementation and not (root / implementation).exists():
                findings.append(
                    Finding(
                        "trace",
                        f"{label}: implementation path missing: {implementation}",
                    )
                )
        if row["coverage_status"] not in {"implemented", "partial", "gap"}:
            findings.append(
                Finding("trace", f"{label}: invalid coverage status")
            )
        if row["semantic_review"] not in {"pass", "pending", "gap"}:
            findings.append(Finding("trace", f"{label}: invalid semantic review"))
    return findings


def validate_legal_baseline(root: Path) -> list[Finding]:
    if not (root / ".git").exists():
        return []
    result = subprocess.run(
        [
            "git",
            "diff",
            "--quiet",
            "pre-reboot-2026-07-15",
            "--",
            "LICENSE",
            "NOTICE",
        ],
        cwd=root,
        check=False,
    )
    if result.returncode == 0:
        return []
    return [Finding("legal", "LICENSE or NOTICE differs from pre-reboot baseline")]


def _run_tool(root: Path, relative: str, *arguments: str) -> list[Finding]:
    result = subprocess.run(
        [sys.executable, str(root / relative), "--root", str(root), *arguments],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode == 0:
        return []
    output = (result.stdout + result.stderr).strip()
    return [Finding("tool", f"{relative} failed: {output}")]


def validate_tools(root: Path) -> list[Finding]:
    findings = _run_tool(
        root, "development/tools/generate_host_bindings.py", "--check"
    )
    findings.extend(
        _run_tool(root, "development/tools/validate_skill_catalog.py")
    )
    return findings


def validate_all(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for validator in (
        validate_structure,
        validate_catalogs,
        validate_trace,
        validate_product_boundary,
        validate_legal_baseline,
        validate_tools,
    ):
        findings.extend(validator(root))
    return findings
