# Bootstrap Development Plane

This directory contains the development system used to build Sys4AI. It is not
part of the distributable product.

## Contents

- `bootstrap-agent/`: canonical stage-0 skills, skill catalog, profiles,
  policies, and host adapters.
- `tools/`: development-only generators and validators.
- `schemas/`: development artifact contracts.
- `sfadev/`: repository-specific development CLI.
- `state/`: small current-work and backlog sources.
- `catalog/`: current controlled-artifact navigation.
- `trace/`: requirement-to-implementation and validation trace.
- `tests/`: development-tool tests.
- `evidence/current/`: evidence for the active change.
- `evidence/releases/`: immutable release evidence bundles.

## Boundary

Development may import or invoke the product. Product code must not import or
read this directory. Historical transactions, receipts, and generated readers
belong to the tagged legacy baseline, not this active plane.
