# Configuration And Control Wiki Policy

## Generated Derivative Authority Notice

The Configuration and Control Wiki is a generated reader surface. It is not canonical. Canonical authority remains with registered YAML control/state records, registered TOML configuration sources, registry rows, validation contracts, and PRDs.

## Covered Formats

Phase 1 covers YAML and TOML.

## Covered Artifact Types

Covered YAML artifacts include AgentJobs, handoffs, completion receipts, task packets, skill manifests, state snapshots, and initialization manifests. Covered TOML artifacts include project, package, framework, tool, runtime, and target-project configuration.

## Required Source Trace

Each generated page must identify source paths, source IDs where available, source hashes where available, and the registry rows that justify inclusion.

## Required Registry Trace

Each generated page must link to the control-record registry, configuration-source registry, derivative registry, and format-profile registry rows that govern the page.

## Required Validation Trace

Each generated page must state validation status and the contract IDs used for structural validation where applicable.

## Page Templates

Phase 1 commits simple generated stubs. A later generator may replace them with fully rendered pages if it preserves the authority notice and metadata block.

## Stale And Orphan Detection

A generated page is invalid if it omits source trace, omits registry trace, points to missing sources, or claims canonical authority.

## Obsidian Mirror Policy

Obsidian mirrors are optional derivatives and do not outrank the generated page or canonical source files.

## Non-Canonical Warning

Do not hand-edit generated wiki pages as source authority.
