# Skill Import Generalizer - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `skill-import-generalizer`  
Canonical runtime path: `.agents/skills/skill-import-generalizer`  
Compatibility shim path: `.codex/skills/skill-import-generalizer/SKILL.md`  
Source import: `.codex/skills/skill-import-generalizer` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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
name: skill-import-generalizer
description: Analyze a project-specific AI skill, remove non-portable assumptions, and rewrite it as a reusable project-agnostic skill template.
---

# Skill Import Generalizer

## Purpose

Use this skill to convert an AI skill from another project into a reusable template suitable for storage in this repository.

This skill is for import and generalization. It does not preserve project-specific behavior unchanged. It extracts the transferable method, removes or parameterizes local assumptions, and prepares the result for later adaptation inside another project.

## When To Use

Use this skill when:

- A skill is being imported from another repository, project, workflow, or local skill directory.
- A skill contains useful behavior but appears tied to one project.
- A user asks to make a skill agnostic, portable, reusable, or template-based.
- A project-specific skill should be prepared for storage under `skills/<skill-name>/`.

Do not use this skill when the user wants to keep an exact project-specific skill unchanged. In that case, ask whether the source should be archived separately or adapted inside the target project.

## Inputs

- Source skill content or source skill path.
- Intended reusable purpose.
- Any known target use cases.
- Any explicit user constraints about what must be preserved or removed.

## Outputs

- A generalized `SKILL.md` suitable for `skills/<skill-name>/SKILL.md`.
- A human-facing `README.md` suitable for `skills/<skill-name>/README.md`.
- A local `AGENTS.md` suitable for `skills/<skill-name>/AGENTS.md`.
- Optional neutral import note when provenance or design rationale should be recorded.
- A short verification summary describing portability, sensitivity, and usability checks.

## Workflow

Follow this sequence in order.

### 1. Source Skill Analysis

Read the source skill completely before rewriting it.

Identify:

- The skill name and stated purpose.
- Trigger conditions.
- Required inputs.
- Expected outputs.
- Procedure.
- Validation behavior.
- Tool, script, model, API, or environment dependencies.
- Any hidden assumptions.

If the source is incomplete, state what is missing before generalizing it.

### 2. Project-Specific Dependency Extraction

List all non-portable dependencies, including:

- Absolute paths.
- Repository names.
- Branch names.
- Issue, ticket, task, or deployment identifiers.
- Private terminology.
- Organization-specific authorities.
- Project-specific validation commands.
- Environment variables.
- Secrets, tokens, credentials, or private URLs.
- Assumptions about framework, package manager, operating system, or file layout.

Remove sensitive material. Replace portable-but-specific material with placeholders.

Preferred placeholders include:

```text
<PROJECT_ROOT>
<SOURCE_SKILL_PATH>
<TARGET_SKILL_PATH>
<SOURCE_REPOSITORY>
<TARGET_REPOSITORY>
<VALIDATION_COMMAND>
<OUTPUT_DIRECTORY>
<PROJECT_AUTHORITY>
```

### 3. Generalization Plan

Before drafting the new skill, define:

- The reusable capability.
- What should be preserved.
- What should be removed.
- What should become a parameter.
- What should become an adaptation note.
- What validation is possible without the original project.

Keep the plan brief and evidence-based.

### 4. Generalized Skill Draft

Write the generalized skill folder as a template.

The required files are:

- `SKILL.md`: executable instructions for AI agents.
- `README.md`: human-facing summary, purpose, usage notes, and adaptation summary.
- `AGENTS.md`: local maintenance and validation rules for the skill.

The `SKILL.md` draft should normally include:

- YAML frontmatter with `name` and `description`.
- Purpose.
- When to use.
- Inputs.
- Outputs.
- Procedure.
- Validation.
- Failure modes.
- Provenance.
- Adaptation guide.

Use clear imperative instructions. Avoid references that only make sense in the source project.

The `README.md` draft should normally include:

- Skill name.
- Purpose.
- When to use.
- What the skill produces.
- Required files.
- Adaptation summary.
- Validation summary.

The `AGENTS.md` draft should normally include:

- Local mission.
- Maintenance rules.
- Portability requirements.
- Validation requirements.
- Instructions for adapting the skill in a target project.

### 5. Portability And Sensitivity Review

Review the draft for:

- Hard-coded local paths.
- Project-specific names.
- Private terminology.
- Hidden dependencies.
- Secrets or sensitive material.
- Unexplained acronyms.
- Unsupported claims.
- Validation steps that cannot run outside the source project.

If any item remains intentionally, explain why and mark it as an adaptation point.

### 6. Validation

Validate the generalized skill by checking:

- It can be understood without the original project.
- It defines when to use it.
- It defines required inputs and expected outputs.
- It explains how to adapt it to a specific project.
- It includes practical verification steps.
- It avoids sensitive or non-portable material.
- Its folder includes `SKILL.md`, `README.md`, and `AGENTS.md`.

When possible, inspect the repository after writing the skill and confirm the file path and content are correct.

### 7. Optional Neutral Import Note

Create an import note only when useful for traceability or design history.

The note should be neutral and non-sensitive. It may describe the source category and generalization decisions, but it should not preserve private source content verbatim.

## Required Provenance Section

Each generalized skill should include a neutral provenance section:

```markdown
## Provenance

Derived from a project-specific skill and generalized as a reusable template. Original project-specific names, paths, assumptions, and private operational details were removed or replaced with parameters.
```

## Required Adaptation Guide

Each generalized skill should include:

```markdown
## Adaptation Guide

When adapting this skill to a specific project:

- Replace placeholders with project-specific paths, commands, and authorities.
- Add project-specific validation commands.
- Add domain-specific constraints only when they are required.
- Preserve the reusable procedure unless local evidence shows a better structure.
- Document any project-specific assumptions introduced during adaptation.
```

## Failure Modes

- The source skill is copied instead of generalized.
- Project-specific details remain hidden in examples or validation commands.
- The generalized skill becomes too abstract to be useful.
- Sensitive material is preserved in provenance or examples.
- The skill lacks enough structure for a future agent to apply it consistently.

## Verification Checklist

Before finalizing, confirm:

- The skill is stored under `skills/<skill-name>/`.
- The skill folder contains `SKILL.md`, `README.md`, and `AGENTS.md`.
- The name describes the reusable capability, not the source project.
- The skill does not require access to the original project.
- All placeholders are understandable.
- The adaptation guide is present.
- The provenance section is neutral and non-sensitive.

## Provenance

Created for this repository as a project-native skill. It defines the standard workflow for converting project-specific AI skills into reusable templates.

## Adaptation Guide

When adapting this skill to a specific project:

- Replace placeholders with project-specific paths, commands, and authorities.
- Add project-specific validation commands.
- Add domain-specific constraints only when they are required.
- Preserve the reusable procedure unless local evidence shows a better structure.
- Document any project-specific assumptions introduced during adaptation.
