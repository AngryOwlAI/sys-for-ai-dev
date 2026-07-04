# Phase 1 Environment Decision Record

**Decision ID:** SFA-EDR-001  
**Status:** Proposed  
**Date:** 2026-07-04  
**Decision owner:** Implementation initialization agent  
**Scope:** Development environment for the `sys-for-ai` reference implementation

---

## Decision

Use a repo-local Python virtual environment as the required Phase 1 development environment.

Docker is deferred as an optional reproducibility or target-runtime layer.

---

## Rationale

Phase 1 needs a small Python implementation spine: scripts, YAML control records, validators, memory registries, skill manifests, and documentation scaffolding. These are naturally supported by Python and `PyYAML` without requiring a container.

A local `.venv` gives contributors a fast and transparent baseline while the framework is still mostly scripts and source-controlled records. Docker can be added later when the project has concrete OS-level dependencies or service orchestration needs.

---

## Required Phase 1 environment

```bash
cd sys-for-ai
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
make doctor
make validate
```

---

## Docker triggers

Add a development Dockerfile or devcontainer only when at least one trigger becomes true:

1. Validation requires OS-level packages such as LaTeX, Graphviz, PlantUML Java runtime, Chromium, or native PDF tooling.
2. The framework becomes a multi-service runtime with API, worker, database, vector index, or web UI.
3. CI must exactly mirror local development.
4. Contributors report recurring environment drift.
5. The product begins generating Docker templates for target systems and needs local validation of those templates.

---

## Development environment vs target runtime

The development environment builds `sys-for-ai` itself.

The target runtime is a generated or recommended environment for systems built by `sys-for-ai`.

These shall remain separate artifacts:

```text
sys-for-ai/
  .venv/                         # local dev only, ignored
  templates/
    target_runtime/
      Dockerfile.template        # generated target-system template, not dev default
      compose.yaml.template      # optional target-system orchestration template
```

---

## Consequences

Positive:

- Faster bootstrap.
- Fewer moving parts.
- Simple offline validation after dependency installation.
- Clear separation between framework development and generated target-system runtime.

Negative:

- OS-specific issues may appear later if rendering or native tooling is added.
- CI parity is not solved yet.
- Docker documentation must be added later if triggers are met.

---

## Revisit condition

Revisit this decision when Phase 2 adds any heavy rendering dependency, multi-service component, hosted runtime, CI workflow, or target-system Docker template validator.
