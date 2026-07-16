# Sys4AI

Sys4AI is an extractable framework product and host-neutral runtime for
designing, building, verifying, operating, improving, and retiring governed
AI agents and agentic systems. It supplies domain rules, application services,
contracts, reusable assets, target-package generation, source-first workspace
navigation, and bounded execution checks.

The product is currently an alpha framework baseline. Its validators establish
only the claims named by their contracts; they do not establish stakeholder
acceptance, domain fitness, security, production readiness, or operational
authority.

## Boundary

This directory is self-contained. It neither imports nor reads its parent
development repository. Runtime state belongs in a target workspace under
`.sys4ai/`, never in the installed source package. Generated target packages
remain derivative until an accountable target authority reviews and promotes
them.

The stable naming is:

- distribution: `sys4ai`
- Python package: `sys4ai`
- command: `sys4ai`
- source directory: `Sys4AI/`

## Quick start

```bash
python -m pip install -e '.[dev]'
sys4ai doctor
sys4ai generate /tmp/repo-steward \
  --system-id repo-steward \
  --name "Repository Steward" \
  --intent "Propose bounded repository maintenance"
sys4ai validate /tmp/repo-steward
```

`sys4ai execute` validates and records an authorized transaction. The
standalone CLI deliberately does not execute arbitrary tools; a declared host
adapter must perform permitted actions.

## Product surfaces

- `src/sys4ai/` — host-neutral domain, services, runtime, ports, adapters,
  generation, assurance, memory, governance, and CLI
- `contracts/` — portable schemas, policies, catalogs, and profiles
- `assets/` — generalized skills, templates, assurance assets, and domain-pack
  contracts
- `adapters/` — documentation for reference adapter boundaries
- `examples/` — non-authoritative contract and profile examples
- `docs/` — product concepts and usage guidance
- `tests/` — product-local behavioral and boundary tests

## Independent verification

From this directory:

```bash
make validate
python -m pytest
python -m build
```

No parent path, root skill binding, root PRD, development ledger, or repository
workflow is required by these commands.
