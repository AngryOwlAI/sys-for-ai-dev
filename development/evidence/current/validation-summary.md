# Repository Reboot Validation Summary

Status: pass for the repository reboot candidate.

## Baseline

The pre-reboot aggregate `make validate` passed at commit `5a6aaf` with the
post-baseline documentation changes present.

## Reboot candidate

Executed on 2026-07-16 UTC with Python 3.12:

- `make validate` passed.
  - `sfadev` development validation passed.
  - Development tests: 3 passed.
  - Product contract validation: 20 evidence paths, 0 issues.
  - Product asset validation: 33 evidence paths, 0 issues.
  - Product tests: 16 passed.
  - Product source distribution and wheel built successfully.
  - Integration tests: 3 passed.
- A clean copy of `Sys4AI/` outside the monorepo installed its own development
  environment, ran its complete `make validate`, and built both distribution
  formats without a parent repository.
- A fresh environment outside the repository installed only the built wheel,
  ran `doctor`, validated packaged contracts and assets, generated a target,
  and validated that target successfully.
- `sfadev validate-authority`, `sfadev check-boundary`, and generated-host-
  binding checks passed.
- Active-shape checks found two active PRDs, one active plan, and no retired
  product control, registry, generated-reader, or legacy-package directories.
- Root `LICENSE` and `NOTICE` match the frozen baseline; product-local copies
  match the root files.
- Wheel and product-source scans found no prohibited development references,
  legacy package paths, generated caches, or platform metadata.
- The final post-closure `make validate` and `git diff --check` passed.

## Review scope and limitations

The semantic trace review passed for RB-001 through RB-024 and RNFR-001 through
RNFR-006. Structural and runtime evidence does not establish stakeholder
acceptance, domain truth, ethical correctness, operational authorization, or
production readiness. The local environment exercised Python 3.12; the
Python 3.10 through 3.14 matrix is defined in CI but was not executed locally.

Two early isolated-wheel harness runs produced false negatives because the
harness expected JSON from `generate` and then expected the wrong manifest
filename. The product commands in those runs succeeded; the corrected harness
used the documented path output and `target-system.yaml`, then passed.
