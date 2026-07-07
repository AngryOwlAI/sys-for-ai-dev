# Mermaid Diagrams - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `mermaid-diagrams`  
Canonical runtime path: `.agents/skills/mermaid-diagrams`  
Compatibility shim path: `.codex/skills/mermaid-diagrams/SKILL.md`  
Source import: `skills/mermaid-diagrams` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

## Sys4AI-dev Authority Rules

- Root PRDs, implementation plans, source registries, validators, and git-tracked files outrank generated outputs.
- `Sys4AI/` is the product scaffold being developed; it is not the full development workspace.
- `.agents/skills/<skill-id>/` is the active runtime skill surface for this repository.
- `.codex/skills/<skill-id>/SKILL.md` is compatibility-only and must point back to this canonical path.
- Existing `Sys4AI/skills/core/` files are scaffold and product-reference adapters, not the active runtime authority.
- Do not import local receipts, caches, generated `usage-metrics.txt`, or private operational state as skill source.
- Treat generated PRDs, plans, diagrams, warnings, and handoffs as derivative work until accepted by the relevant project authority.

The imported source guidance below remains valid where it does not conflict with these Sys4AI-dev rules.

---

---
name: mermaid-diagrams
description: Create, review, render, and validate source-controlled Mermaid diagrams with explicit visual grammar, portable styling, and derivative-output checks.
---

# mermaid-diagrams

## Purpose

Create and maintain Mermaid diagrams as portable, source-controlled
documentation artifacts.

This skill treats Mermaid text as the canonical source. Rendered SVG, PNG, PDF,
HTML, or slide outputs are derivatives that must remain traceable to the
source diagram.

## When To Use

- The user asks for a Mermaid diagram, diagram review, diagram migration, or
  diagram rendering workflow.
- Documentation needs flowcharts, sequence diagrams, state diagrams, ER
  diagrams, class diagrams, timelines, Gantt charts, or Git graphs.
- A project needs governed diagram sources with stable IDs, visual grammar,
  accessibility checks, and derivative-output validation.
- Existing diagrams need restyling without changing their meaning.

Do not use this skill as a substitute for source evidence. A diagram may
explain a system, plan, or claim, but it must not create authority that the
underlying project sources do not support.

## Inputs

- Diagram purpose, audience, and target publication surface.
- Source material to explain, such as architecture notes, code, requirements,
  process documentation, or data-model references.
- Target source path, such as `<PROJECT_ROOT>/<DIAGRAM_SOURCE_PATH>`.
- Optional rendered output path, such as `<OUTPUT_DIRECTORY>`.
- Optional project authority source, such as `<PROJECT_AUTHORITY>`.
- Optional style or palette contract, such as `<DIAGRAM_STYLE_GUIDE>`.
- Optional validation command, such as `<VALIDATION_COMMAND>`.

## Outputs

- Mermaid source block or `.mmd` file.
- Stable diagram ID when the target project requires one.
- Visual grammar summary explaining node shapes, borders, colors, arrows,
  groups, and edge labels.
- Optional rendered derivative output, such as SVG, PNG, HTML, PDF, or slide
  media.
- Validation summary with commands run, checks skipped, and remaining risk.

## Procedure

1. Inspect the source material before drawing the diagram.
2. Define the diagram purpose, audience, target surface, and claim boundary.
3. Select the simplest Mermaid diagram type that represents the content.
4. Define visual grammar before writing the diagram:
   - shapes encode node type;
   - borders encode status, authority, or risk;
   - arrows encode relationship type;
   - edge labels clarify non-obvious relationships;
   - groups encode scope only when the boundary matters;
   - color supports meaning but is never the only meaning carrier.
5. Assign stable node IDs and concise labels. Quote labels containing spaces,
   punctuation, or line breaks.
6. Use `<br/>` for Mermaid flowchart line breaks when line breaks are needed.
7. Use reusable `classDef` classes or a project style contract instead of
   repeated ad hoc inline styles.
8. Preserve existing diagram IDs, topology, node IDs, and reader-facing labels
   unless the source material requires correction.
9. Keep Mermaid source canonical. Generate rendered outputs only from that
   source.
10. Validate syntax, source-to-output parity, accessibility, and target-surface
    requirements.
11. Report the source path, diagram ID, diagram type, grammar summary,
    validation results, and any unchecked assumptions.

## Diagram Type Selection

- `flowchart TD`: processes, pipelines, architecture maps, agent workflows, and
  control flow. Prefer top-down for complex diagrams.
- `flowchart LR`: short linear flows with few nodes.
- `sequenceDiagram`: interactions between users, services, agents, tools, or
  scripts.
- `stateDiagram-v2`: lifecycle, routing, validation, and state transitions.
- `classDiagram`: software modules, classes, interfaces, and relationships.
- `erDiagram`: metadata stores, registries, schemas, and ledgers.
- `gantt`: schedules and phased delivery plans.
- `timeline`: historical or roadmap sequencing.
- `gitGraph`: branch, merge, release, and review-flow explanations.

If a diagram exceeds readable Mermaid density, split it into a high-level
overview plus a table, companion prose, or smaller follow-up diagrams.

## Source And ID Rules

- Treat Mermaid source as canonical.
- Treat inline SVG, images, exported HTML, and slide media as generated
  derivatives.
- Use stable diagram IDs when diagrams are registered, referenced, rendered, or
  embedded in downstream outputs.
- Prefer lowercase kebab-case IDs:

```text
^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$
```

- Preserve existing IDs during edits unless the ID itself is incorrect and the
  downstream references are also updated.
- Keep generated hashes, manifests, or provenance metadata deterministic when
  the target project supports them.

## Styling Guidance

Use the target project's diagram style guide when one exists. If none exists,
define a small style contract before drawing:

- background and text colors;
- node fill, stroke, and label colors;
- edge color and edge label background;
- class names and meanings;
- font family and minimum readable size;
- accessibility contrast expectations.

A style contract constrains readability and consistency. It must not flatten
semantic grammar. Shape, border, arrow, group, and label choices should remain
available to explain meaning.

## Rendering Guidance

For governed or published documentation, prefer build-time rendering to static
SVG or image outputs when the target surface does not require live Mermaid.

If the target project permits browser-side Mermaid, initialize it with explicit
configuration, a known version, and strict security settings where supported.
Do not rely on implicit page-load rendering for governed documentation unless
the target project has accepted that runtime dependency.

If producing inline SVG:

- sanitize generated SVG with an allowlist;
- reject scripts, event handlers, external references, remote URLs,
  `javascript:` URLs, and unexpected `foreignObject` usage;
- rewrite generated IDs deterministically when multiple diagrams share a page;
- preserve accessible titles, descriptions, or surrounding captions where
  practical;
- include width, height, or viewBox information sufficient for reliable layout.

## Validation

Use the strongest validation available in the target project:

- Parse Mermaid fences or `.mmd` files and confirm each diagram is non-empty.
- Confirm the first semantic line is a supported Mermaid diagram type.
- Run Mermaid CLI or the project renderer when available.
- Confirm stable IDs are present where required.
- Confirm rendered derivatives match normalized source, such as through a
  source hash, manifest, or registry check.
- Confirm published outputs do not include unapproved Mermaid runtime imports.
- Visually inspect reader-facing output at relevant sizes.
- Run `<VALIDATION_COMMAND>` when the target project defines one.

If a renderer, CLI, browser check, or project validator is unavailable, report
the skipped check explicitly.

## Failure Modes

- Drawing from assumptions instead of source material.
- Using color as the only meaning carrier.
- Restyling a diagram while changing its topology or claim boundary.
- Treating generated SVG, PNG, or HTML as canonical source.
- Leaving stale derivatives after changing Mermaid source.
- Introducing browser runtime dependencies where static output is required.
- Copying project-specific palettes, paths, manifests, or validators into a
  reusable template.
- Creating diagrams too dense to read.

## Provenance

Derived from a project-specific skill and generalized as a reusable template.
Original project-specific names, paths, assumptions, and private operational
details were removed or replaced with parameters.

## Adaptation Guide

When adapting this skill to a specific project:

- Replace placeholders with project-specific paths, commands, and authorities.
- Add project-specific validation commands.
- Add domain-specific constraints only when they are required.
- Preserve the reusable procedure unless local evidence shows a better
  structure.
- Document any project-specific assumptions introduced during adaptation.
