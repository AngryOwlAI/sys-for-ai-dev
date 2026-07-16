"""Repository-specific development CLI for Sys4AI-dev."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml

from . import __version__
from .validation import (
    Finding,
    validate_all,
    validate_product_boundary,
    validate_structure,
)


DEFAULT_ROOT = Path(__file__).resolve().parents[2]


def _print_findings(findings: list[Finding]) -> int:
    if not findings:
        print("sfadev validation passed")
        return 0
    for finding in findings:
        print(f"FAIL {finding.check}: {finding.message}", file=sys.stderr)
    return 1


def _run_tool(root: Path, name: str, check: bool = False) -> int:
    command = [
        sys.executable,
        str(root / "development/tools/generate_host_bindings.py"),
        "--root",
        str(root),
    ]
    if check:
        command.append("--check")
    return subprocess.run(command, cwd=root, check=False).returncode


def _status(root: Path, as_json: bool) -> int:
    path = root / "development/state/current-work.yaml"
    if not path.exists():
        print("current work state is missing", file=sys.stderr)
        return 1
    text = path.read_text(encoding="utf-8")
    if not as_json:
        print(text, end="")
        return 0
    try:
        values = yaml.safe_load(text)
    except yaml.YAMLError as error:
        print(f"current work state is invalid YAML: {error}", file=sys.stderr)
        return 1
    if not isinstance(values, dict):
        print("current work state must be a YAML mapping", file=sys.stderr)
        return 1
    print(json.dumps(values, indent=2, sort_keys=True, default=str))
    return 0


def _release_evidence(root: Path, version: str) -> int:
    if not version or any(character in version for character in "/\\"):
        print("version must be a path-safe identifier", file=sys.stderr)
        return 2
    target = root / "development/evidence/releases" / version
    if target.exists():
        print(f"release evidence already exists: {target}", file=sys.stderr)
        return 1
    target.mkdir(parents=True)
    files = {
        "release-manifest.yaml": (
            f"version: {version}\nstatus: candidate\n"
            "promotion_authority: accountable_human_release_owner\n"
        ),
        "requirement-coverage.csv": (
            "requirement_id,status,evidence_path,notes\n"
        ),
        "validation-summary.md": "# Validation Summary\n\nNot yet executed.\n",
        "security-summary.md": "# Security Summary\n\nNot yet reviewed.\n",
        "test-results.json": "{}\n",
        "unresolved-risks.md": "# Unresolved Risks\n\nNot yet reviewed.\n",
    }
    for name, content in files.items():
        (target / name).write_text(content, encoding="utf-8")
    print(f"created candidate release evidence scaffold: {target}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument("--root", default=str(DEFAULT_ROOT))
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="Run all development checks")
    subparsers.add_parser(
        "validate-authority", help="Validate active PRDs plans state and history hygiene"
    )
    subparsers.add_parser(
        "check-boundary", help="Check the product for development dependencies"
    )
    bindings = subparsers.add_parser(
        "generate-host-bindings", help="Generate or check host bindings"
    )
    bindings.add_argument("--check", action="store_true")
    status = subparsers.add_parser("status", help="Show current work state")
    status.add_argument("--json", action="store_true")
    release = subparsers.add_parser(
        "release-evidence", help="Create an unapproved release-evidence scaffold"
    )
    release.add_argument("version")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(args.root).resolve()
    if args.command == "validate":
        return _print_findings(validate_all(root))
    if args.command == "validate-authority":
        return _print_findings(validate_structure(root))
    if args.command == "check-boundary":
        return _print_findings(validate_product_boundary(root))
    if args.command == "generate-host-bindings":
        return _run_tool(root, args.command, args.check)
    if args.command == "status":
        return _status(root, args.json)
    if args.command == "release-evidence":
        return _release_evidence(root, args.version)
    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
