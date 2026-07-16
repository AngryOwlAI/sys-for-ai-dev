---
artifact_id: SFA-ARCH-TARGET-SYSTEM-001
artifact_type: architecture
subject: target-template
subject_layer: target-template
authority: controlled
status: active
owner: system_architect
supersedes: null
source_trace:
  - SFA-PRD-PRODUCT-BASELINE-001
---

# Target-System Model

## Package contract

A generated target package separates:

    target-system.yaml
    governance/
    requirements/
    architecture/
    runtime/
    skills/
    contracts/
    tests/
    operations/
    evidence/

Governance covers mission, vision, values, authority, and decisions.
Requirements cover discovery, product/system requirements, and trace.
Operations cover runbooks, monitoring, maintenance, improvement, and
retirement.

## Authority

Generated packages are derivative proposals. Target owners accept requirements,
permissions, deployment, data use, production status, and operations. Sys4AI
cannot grant those authorities.

## Integration fixture

`integration/fixtures/target-systems/repo-steward/` is a local smoke fixture.
It demonstrates structural flow and traceability only. It does not establish
semantic correctness, domain acceptance, or production readiness.
