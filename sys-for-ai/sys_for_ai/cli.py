"""Command-line entry point for the Phase 1 sys-for-ai scaffold."""

from __future__ import annotations

import argparse
import importlib.util
import platform
import sys
from pathlib import Path

from .memory import bootstrap_registries
from .validators import (
    ValidationResult,
    print_result,
    validate_agentjob,
    validate_registry_headers,
    validate_skill_manifest,
)


def _doctor() -> ValidationResult:
    messages: list[str] = []
    ok = True

    messages.append(f"Python: {platform.python_version()} at {sys.executable}")

    yaml_spec = importlib.util.find_spec("yaml")
    if yaml_spec is None:
        ok = False
        messages.append("PyYAML: missing. Run: python -m pip install -r requirements.txt")
    else:
        import yaml  # type: ignore

        messages.append(f"PyYAML: {getattr(yaml, '__version__', 'unknown')}")

    expected_dirs = [
        Path("schemas"),
        Path("control_records"),
        Path("registries"),
        Path("skills"),
        Path("docs"),
        Path("templates"),
    ]
    for directory in expected_dirs:
        if directory.exists():
            messages.append(f"Directory: {directory} present")
        else:
            ok = False
            messages.append(f"Directory: {directory} missing")

    return ValidationResult(ok, messages)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sys-for-ai", description="Phase 1 sys-for-ai scaffold commands")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("doctor", help="Check Python, dependencies, imports, and expected folders")

    validate = sub.add_parser("validate", help="Run all default Phase 1 validations")
    validate.add_argument("--agentjob", default="control_records/examples/phase1_smoke_agentjob.yaml")
    validate.add_argument("--skills", default="skills/core_skill_manifest.yaml")
    validate.add_argument("--registries", default="registries")

    validate_agent = sub.add_parser("validate-agentjob", help="Validate one AgentJob YAML file")
    validate_agent.add_argument("path")

    validate_skills = sub.add_parser("validate-skills", help="Validate the core skill manifest")
    validate_skills.add_argument("path")

    bootstrap = sub.add_parser("bootstrap-memory", help="Create missing memory registry files")
    bootstrap.add_argument("registry_dir", default="registries", nargs="?")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "doctor":
        return print_result(_doctor())

    if args.command == "validate-agentjob":
        return print_result(validate_agentjob(args.path))

    if args.command == "validate-skills":
        return print_result(validate_skill_manifest(args.path))

    if args.command == "bootstrap-memory":
        return print_result(bootstrap_registries(args.registry_dir))

    if args.command == "validate":
        result = _doctor()
        result.extend(validate_agentjob(args.agentjob))
        result.extend(validate_skill_manifest(args.skills))
        result.extend(validate_registry_headers(args.registries))
        return print_result(result)

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
