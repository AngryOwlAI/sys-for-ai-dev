# Validation Contracts Catalog Policy

## Generated Derivative Authority Notice

The Validation Contracts Catalog is a generated reader surface for validation contracts. It is not canonical. Canonical authority remains with registered JSON Schema files, registry rows, PRDs, and controlled source files.

## Covered Format

Phase 1 covers JSON Schema contracts under `schemas/contracts/`.

## No JSON Wiki By Default

JSON Schema is a validation-contract format, not a narrative memory format. Phase 1 creates a Validation Contracts Catalog, not a standalone JSON wiki.

## Required Contract Metadata

Each catalog entry must identify contract ID, path, dialect, target format, target artifact type, target glob, owner, authority status, validator command, supersession relation, and known limitations.

## Required Target Artifact Metadata

The catalog must link contracts to registry rows, control records, configuration sources, templates, or registries that declare the contract.

## Required Validator Command

Each registered contract must declare the command or validator family responsible for checking it.

## Supersession And Migration Policy

Schema changes that affect existing controlled artifacts require supersession notes and migration evidence in a later implementation pass.

## Structural Versus Semantic Validation

JSON Schema validation proves structural admissibility only. It does not prove domain correctness, semantic truth, operational readiness, or user acceptance.

## Catalog Generation And Validation Rules

Generated catalog pages must include a derivative notice, metadata block, source trace, registry trace, validation status, and stale/orphan status.
