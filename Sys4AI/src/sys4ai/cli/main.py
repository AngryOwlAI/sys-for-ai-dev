"""Product CLI for target workspaces and portable product validation."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

from .. import __version__
from ..adapters.read_only_filesystem import ReadOnlyFilesystemHostAdapter
from ..application.services import (
    ArchitectureService,
    DiscoveryService,
    ExecutionService,
    KnowledgeService,
    OperationsService,
    PlanningService,
    SpecificationService,
    TargetFactory,
    VerificationService,
)
from ..assurance.validation import validate_assets, validate_contracts, validate_trace
from ..domain.models import SystemDefinition, ValidationResult
from ..runtime.workspace import initialize_workspace


def _definition(args: argparse.Namespace) -> SystemDefinition:
    return SystemDefinition(
        system_id=args.system_id,
        name=args.name,
        intent=args.intent,
        target_kind=args.target_kind,
        coordination_pattern=args.coordination_pattern,
        operational_maturity=args.operational_maturity,
    )


def _print_result(result: ValidationResult, as_json: bool = True) -> int:
    if as_json:
        print(json.dumps(result.to_dict(), indent=2, sort_keys=True))
    else:
        for issue in result.issues:
            print(f"FAIL {issue.code}: {issue.message}", file=sys.stderr)
        for warning in result.warnings:
            print(f"WARNING: {warning}")
        if result.ok:
            print("validation passed")
    return 0 if result.ok else 1


def _load_mapping(path: str | Path) -> dict[str, object]:
    value = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a mapping")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="version", version=__version__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor = subparsers.add_parser("doctor", help="Inspect the product runtime")
    doctor.add_argument("--json", action="store_true")

    for command, help_text in (
        ("init", "Initialize a target discovery workspace"),
        ("generate", "Generate a derivative target package"),
    ):
        target = subparsers.add_parser(command, help=help_text)
        target.add_argument("path")
        target.add_argument("--system-id", required=True)
        target.add_argument("--name", required=True)
        target.add_argument("--intent", required=True)
        target.add_argument("--target-kind", default="agentic-system")
        target.add_argument("--coordination-pattern", default="linear_workflow")
        target.add_argument("--operational-maturity", default="concept")
        target.add_argument("--allow-existing", action="store_true")

    discover = subparsers.add_parser("discover", help="Record derivative discovery intent")
    discover.add_argument("path")
    discover.add_argument("--intent", required=True)

    plan = subparsers.add_parser("plan", help="Create a proposed target plan")
    plan.add_argument("path")
    for command, help_text in (
        ("specify", "Create candidate target requirement artifacts"),
        ("architect", "Create candidate target architecture artifacts"),
        ("operations", "Create candidate target operations artifacts"),
    ):
        lifecycle = subparsers.add_parser(command, help=help_text)
        lifecycle.add_argument("path")

    execute = subparsers.add_parser(
        "execute",
        help="Validate and record a transaction for a permitted host adapter",
    )
    execute.add_argument("path")
    execute.add_argument("transaction")
    execute.add_argument(
        "--apply-read-only",
        action="store_true",
        help="execute declared read actions through the bounded filesystem host",
    )

    validate = subparsers.add_parser("validate", help="Validate a target package")
    validate.add_argument("path")
    verify = subparsers.add_parser("verify", help="Run product-level target verification")
    verify.add_argument("path")
    trace = subparsers.add_parser("trace", help="Validate target requirement trace")
    trace.add_argument("path")

    memory = subparsers.add_parser("memory", help="Navigate target workspace sources")
    memory_subparsers = memory.add_subparsers(dest="memory_command", required=True)
    search = memory_subparsers.add_parser("search")
    search.add_argument("path")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=10)
    lookup = memory_subparsers.add_parser("lookup")
    lookup.add_argument("path")
    lookup.add_argument("query")

    subparsers.add_parser("contracts", help="Validate product-local contracts")
    subparsers.add_parser("assets", help="Validate product-local assets")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "doctor":
        payload = {
            "product": "Sys4AI",
            "version": __version__,
            "package": "sys4ai",
            "status": "available",
        }
        print(json.dumps(payload, indent=2) if args.json else payload)
        return 0
    if args.command == "init":
        initialize_workspace(
            args.path, _definition(args), allow_existing=args.allow_existing
        )
        print(Path(args.path).resolve())
        return 0
    if args.command == "generate":
        path = TargetFactory().generate(
            _definition(args), args.path, allow_existing=args.allow_existing
        )
        print(path)
        return 0
    if args.command == "discover":
        print(DiscoveryService().record(args.path, args.intent))
        return 0
    if args.command == "plan":
        print(PlanningService().create(args.path))
        return 0
    if args.command == "specify":
        print("\n".join(str(path) for path in SpecificationService().create(args.path)))
        return 0
    if args.command == "architect":
        print("\n".join(str(path) for path in ArchitectureService().create(args.path)))
        return 0
    if args.command == "operations":
        print("\n".join(str(path) for path in OperationsService().create(args.path)))
        return 0
    if args.command == "execute":
        host = (
            ReadOnlyFilesystemHostAdapter(args.path)
            if args.apply_read_only
            else None
        )
        return _print_result(
            ExecutionService().process(
                args.path,
                _load_mapping(args.transaction),
                host,
            )
        )
    if args.command in {"validate", "verify"}:
        return _print_result(VerificationService().verify(args.path))
    if args.command == "trace":
        return _print_result(validate_trace(args.path))
    if args.command == "memory":
        service = KnowledgeService()
        if args.memory_command == "search":
            print(json.dumps(service.search(args.path, args.query, args.limit), indent=2))
            return 0
        result = service.lookup(args.path, args.query)
        print(json.dumps(result, indent=2))
        return 0 if result else 1
    if args.command == "contracts":
        return _print_result(validate_contracts())
    if args.command == "assets":
        return _print_result(validate_assets())
    raise AssertionError(f"unhandled command: {args.command}")
