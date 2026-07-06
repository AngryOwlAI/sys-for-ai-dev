"""Command-line entry point for the Phase 1 sys-for-ai scaffold."""

from __future__ import annotations

import argparse
import importlib.util
import platform
import sys
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from .discovery import validate_discovery_record
from .derivative_generation import validate_generated_derivatives
from .memory import bootstrap_registries
from .validators import (
    ValidationResult,
    print_result,
    validate_agentjob,
    validate_config_sources,
    validate_control_records,
    validate_format_profiles,
    validate_jsonschema_contracts,
    validate_metrics_script,
    validate_registry_graph,
    validate_registry_headers,
    validate_requirement_trace,
    validate_skill_manifest,
    validate_toml_config,
    validate_validation_contract_registry,
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

    if importlib.util.find_spec("tomllib") is not None:
        messages.append("TOML parser: tomllib available")
    elif importlib.util.find_spec("tomli") is not None:
        messages.append("TOML parser: tomli available")
    else:
        ok = False
        messages.append("TOML parser: missing tomllib/tomli. Run: python -m pip install -r requirements.txt")

    jsonschema_spec = importlib.util.find_spec("jsonschema")
    if jsonschema_spec is None:
        ok = False
        messages.append("jsonschema: missing. Run: python -m pip install -r requirements.txt")
    else:
        try:
            jsonschema_version = version("jsonschema")
        except PackageNotFoundError:
            jsonschema_version = "unknown"
        messages.append(f"jsonschema: {jsonschema_version}")

    expected_dirs = [
        Path("configs"),
        Path("schemas"),
        Path("schemas/contracts"),
        Path("control_records"),
        Path("registries"),
        Path("skills"),
        Path("docs"),
        Path("docs/generated/configuration_control"),
        Path("docs/generated/validation_contracts"),
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
    validate.add_argument("--metrics", default="skills/core/codex-usage-metrics/scripts/collect_usage_metrics.py")
    validate.add_argument("--discovery-template", default="templates/system_definition/requirements-discovery-record-template.md")
    validate.add_argument("--registries", default="registries")
    validate.add_argument("--format-profiles", default="registries/format_profile_registry.csv")
    validate.add_argument("--config-sources", default="registries/config_source_registry.csv")
    validate.add_argument("--control-records", default="registries/control_record_registry.csv")
    validate.add_argument("--validation-contracts", default="registries/validation_contract_registry.csv")
    validate.add_argument("--requirement-trace", default="registries/requirement_trace_registry.csv")
    validate.add_argument("--contracts-root", default="schemas/contracts")
    validate.add_argument("--generated-docs", default="docs/generated")

    validate_agent = sub.add_parser("validate-agentjob", help="Validate one AgentJob YAML file")
    validate_agent.add_argument("path")

    validate_skills = sub.add_parser("validate-skills", help="Validate the core skill manifest")
    validate_skills.add_argument("path")

    validate_metrics = sub.add_parser("validate-metrics", help="Validate local Codex usage metrics script entry point")
    validate_metrics.add_argument(
        "path",
        default="skills/core/codex-usage-metrics/scripts/collect_usage_metrics.py",
        nargs="?",
    )

    validate_discovery = sub.add_parser("validate-discovery-record", help="Validate a requirements discovery record")
    validate_discovery.add_argument("path")

    bootstrap = sub.add_parser("bootstrap-memory", help="Create missing memory registry files")
    bootstrap.add_argument("registry_dir", default="registries", nargs="?")

    validate_formats = sub.add_parser("validate-format-profiles", help="Validate format-profile registry rows")
    validate_formats.add_argument("path", default="registries/format_profile_registry.csv", nargs="?")

    validate_configs = sub.add_parser("validate-config-sources", help="Validate configuration-source registry rows")
    validate_configs.add_argument("path", default="registries/config_source_registry.csv", nargs="?")

    validate_controls = sub.add_parser("validate-control-records", help="Validate control-record registry rows and examples")
    validate_controls.add_argument("path", default="registries/control_record_registry.csv", nargs="?")

    validate_contract_registry = sub.add_parser(
        "validate-validation-contract-registry",
        help="Validate validation-contract registry rows and schema files",
    )
    validate_contract_registry.add_argument("path", default="registries/validation_contract_registry.csv", nargs="?")

    validate_toml = sub.add_parser("validate-toml-config", help="Validate registered TOML configuration sources")
    validate_toml.add_argument("path", default="registries/config_source_registry.csv", nargs="?")

    validate_contracts = sub.add_parser("validate-jsonschema-contracts", help="Validate JSON Schema contract files")
    validate_contracts.add_argument("root", default="schemas/contracts", nargs="?")

    validate_graph = sub.add_parser("validate-registry-graph", help="Validate cross-registry path and contract references")
    validate_graph.add_argument("registry_dir", default="registries", nargs="?")

    validate_trace = sub.add_parser(
        "validate-requirement-trace",
        help="Validate PRD requirement IDs and Phase 0 to Phase 1 trace coverage",
    )
    validate_trace.add_argument("path", default="registries/requirement_trace_registry.csv", nargs="?")
    validate_trace.add_argument("--phase0-prd", default="PRDs/sys-for-ai_phase-0_product_system_design_prd.md")
    validate_trace.add_argument("--phase1-prd", default="PRDs/sys-for-ai_phase-1_implementation_initialization_prd.md")

    generate_cc = sub.add_parser("generate-config-control-wiki", help="Check generated Configuration and Control Wiki stubs")
    generate_cc.add_argument("--check", action="store_true", help="Check stubs without writing")

    generate_vc = sub.add_parser("generate-validation-contracts-catalog", help="Check generated Validation Contracts Catalog stubs")
    generate_vc.add_argument("--check", action="store_true", help="Check stubs without writing")

    validate_generated = sub.add_parser("validate-generated-derivatives", help="Validate generated derivative stubs")
    validate_generated.add_argument("docs_root", default="docs/generated", nargs="?")
    validate_generated.add_argument("derivative_registry", default="registries/derivative_registry.csv", nargs="?")

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

    if args.command == "validate-metrics":
        return print_result(validate_metrics_script(args.path))

    if args.command == "validate-discovery-record":
        return print_result(validate_discovery_record(args.path))

    if args.command == "bootstrap-memory":
        return print_result(bootstrap_registries(args.registry_dir))

    if args.command == "validate-format-profiles":
        return print_result(validate_format_profiles(args.path))

    if args.command == "validate-config-sources":
        return print_result(validate_config_sources(args.path))

    if args.command == "validate-control-records":
        return print_result(validate_control_records(args.path))

    if args.command == "validate-validation-contract-registry":
        return print_result(validate_validation_contract_registry(args.path))

    if args.command == "validate-toml-config":
        return print_result(validate_toml_config(args.path))

    if args.command == "validate-jsonschema-contracts":
        return print_result(validate_jsonschema_contracts(args.root))

    if args.command == "validate-registry-graph":
        return print_result(validate_registry_graph(args.registry_dir))

    if args.command == "validate-requirement-trace":
        return print_result(validate_requirement_trace(args.path, args.phase0_prd, args.phase1_prd))

    if args.command == "generate-config-control-wiki":
        return print_result(validate_generated_derivatives("docs/generated", "registries/derivative_registry.csv"))

    if args.command == "generate-validation-contracts-catalog":
        return print_result(validate_generated_derivatives("docs/generated", "registries/derivative_registry.csv"))

    if args.command == "validate-generated-derivatives":
        return print_result(validate_generated_derivatives(args.docs_root, args.derivative_registry))

    if args.command == "validate":
        result = _doctor()
        result.extend(validate_agentjob(args.agentjob))
        result.extend(validate_skill_manifest(args.skills))
        result.extend(validate_metrics_script(args.metrics))
        result.extend(validate_discovery_record(args.discovery_template))
        result.extend(validate_registry_headers(args.registries))
        result.extend(validate_format_profiles(args.format_profiles))
        result.extend(validate_config_sources(args.config_sources))
        result.extend(validate_control_records(args.control_records))
        result.extend(validate_validation_contract_registry(args.validation_contracts))
        result.extend(validate_toml_config(args.config_sources))
        result.extend(validate_jsonschema_contracts(args.contracts_root))
        result.extend(validate_registry_graph(args.registries))
        result.extend(validate_requirement_trace(args.requirement_trace))
        result.extend(validate_generated_derivatives(args.generated_docs, "registries/derivative_registry.csv"))
        return print_result(result)

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
