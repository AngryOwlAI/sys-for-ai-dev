# Technical Writing Quality Gate - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `technical-writing-quality-gate`
Canonical runtime path: `development/bootstrap-agent/skills/technical-writing-quality-gate`
Compatibility shim path: `.codex/skills/technical-writing-quality-gate/SKILL.md`
Source import: `skills/technical-writing-quality-gate` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

## Sys4AI-dev Authority Rules

- Root PRDs, implementation plans, source registries, validators, and git-tracked files outrank generated outputs.
- `Sys4AI/` is the product scaffold being developed; it is not the full development workspace.
- `development/bootstrap-agent/skills/<skill-id>/` is the active runtime skill surface for this repository.
- `.codex/skills/<skill-id>/SKILL.md` is compatibility-only and must point back to this canonical path.
- Existing `Sys4AI/assets/skills/` files are scaffold and product-reference adapters, not the active runtime authority.
- Do not import local receipts, caches, generated `usage-metrics.txt`, or private operational state as skill source.
- Treat generated PRDs, plans, diagrams, warnings, and handoffs as derivative work until accepted by the relevant project authority.

The imported source guidance below remains valid where it does not conflict with these Sys4AI-dev rules.

---

---
name: technical-writing-quality-gate
description: Draft, revise, and evaluate source-grounded technical or system prose with a pass / repair / block gate, explicit claim boundaries, and optional warning-pattern checks.
---

# technical-writing-quality-gate

## Purpose

Use this skill to produce or evaluate claim-bearing technical prose that is
specific, source-grounded, and proportionate to the available evidence.

The skill is designed for descriptions, explanations, summaries, release notes,
project pages, architecture notes, research summaries, operational documents,
and promotional text about software, engineering, scientific, financial,
organizational, or other structured systems.

This skill is not a detector for human authorship and does not prove factual
correctness by style alone. It is a quality gate for grounding, specificity,
tone, and claim discipline.

## When To Use

- The user asks to draft, revise, or review technical prose.
- A document needs to explain what a system is, what it does, how it works, and
  what evidence supports its claims.
- A project needs a `pass`, `repair`, or `block` decision before publishing or
  accepting claim-bearing text.
- Generated prose sounds generic, inflated, vague, or unsupported.
- A dataset or reference set is being used to improve writing guidance through
  blind comparison.

Do not use this skill as a substitute for domain validation, security review,
scientific peer review, legal review, or source-of-truth approval. It can
surface claim risks; it cannot establish truth without the relevant evidence.

## Inputs

- Draft text, outline, prompt, or requested writing task.
- Source authority, such as `<PROJECT_AUTHORITY>`, source documents, code,
  requirements, tickets, research notes, data dictionaries, or design records.
- Target audience, purpose, and publication surface.
- Required citation standard, if citations are needed.
- Optional target path, such as `<PROJECT_ROOT>/<TARGET_DOCUMENT_PATH>`.
- Optional project terminology, tone, or style guidance.
- Optional validation command, such as `<VALIDATION_COMMAND>`.
- Optional dataset row with topic, source brief, and human reference for blind
  comparison.
- Optional output path, such as `<OUTPUT_DIRECTORY>`.

## Outputs

- A revised or newly drafted text artifact, when enough source evidence exists.
- A gate result: `pass`, `repair`, or `block`.
- A concise source-grounding summary identifying important facts used.
- A list of unsupported or overextended claims when found.
- A validation summary with commands run, checks skipped, and remaining risk.
- Optional warning-pattern report from `scripts/technical_writing_warning_gate.py`.

## Authority Boundaries

- Treat source materials as authority; treat style, fluency, and warning
  patterns as review signals only.
- Separate source facts from inference. Label necessary inference explicitly.
- Do not add capabilities, performance, safety, reliability, security, business
  outcomes, scientific claims, or operational effects that are not supported by
  the source.
- Do not strengthen uncertainty into certainty.
- Do not treat a clean warning-pattern scan as proof of factual correctness,
  source coverage, originality, or human authorship.
- Use APA 7 format when citing documents or materials unless the target project
  explicitly requires a different citation format.

## Procedure

1. Identify the system-under-work, audience, purpose, publication surface, and
   source authority.
2. Inspect the source material before drafting or revising. If the source is
   absent or insufficient for the requested claim, return `block`.
3. Extract concrete facts:
   - system class and purpose;
   - actors, users, maintainers, or stakeholders;
   - inputs, outputs, interfaces, and data flows;
   - workflows, control loops, decisions, constraints, and failure modes;
   - scale, limits, dependencies, and known uncertainty;
   - named mechanisms, constructs, comparisons, or evidence.
4. Rank defining source facts before secondary background. Preserve names,
   expansions, project-specific terms, interfaces, and scope limits when they
   matter to reader understanding.
5. Draft or revise with specific nouns, active verbs, and visible mechanics.
   Prefer mechanism over praise and causal sequence over slogan-like claims.
6. Remove or repair generic marketing texture unless the source material
   provides concrete support.
7. Check claims against the source:
   - mark supported claims as usable;
   - mark inferred claims as inference;
   - remove or repair unsupported claims;
   - block claims that cannot be responsibly evaluated from available context.
8. Apply the gate:
   - `pass`: the text is concrete, accurate relative to supplied sources,
     audience-fit, and proportional to the evidence.
   - `repair`: the text has fixable problems such as vague wording, inflated
     tone, weak sequence, missing concrete system nouns, or unsupported benefit
     language that can be corrected from available context.
   - `block`: source facts, audience, authority, intent, or comparison data are
     missing enough that responsible writing or evaluation is not possible.
9. For substantial or public-facing text, use
   `references/system-writing-quality.md` as the review checklist.
10. When a target project permits optional script checks, run:

   ```sh
   python3 scripts/technical_writing_warning_gate.py <TARGET_FILES> \
     --report <OUTPUT_DIRECTORY>/technical-writing-quality-gate.md
   ```

   Use `--strict` only when warning-pattern hits should fail CI or a local
   validation gate. Treat script output as proxy evidence requiring human or
   source-aware review.
11. Report the gate result, source facts used, material changes, validation
    performed, skipped checks, and unresolved risks.

## Dataset Comparison Mode

Use this mode only when a target project intentionally evaluates writing
against human reference examples or approved editorial references.

1. Generate or revise the candidate from the topic and source brief only.
2. Do not inspect the human reference before candidate generation.
3. Compare the candidate against the reference after generation for source
   coverage, tone, vocabulary, sentence shape, specificity, and unsupported
   claims.
4. Treat metrics as proxies. They can guide review but do not prove semantic
   equivalence, factual correctness, or human authorship.
5. Revise the skill or local style guidance only when a gap is repeated,
   explainable, and likely to generalize.
6. Avoid overfitting to one writer, one dataset row, one domain, or one model.

## Warning Patterns

Treat these as warning signs, not automatic errors:

- vague praise: `seamless`, `robust`, `cutting-edge`, `transformative`,
  `revolutionary`, `game-changing`, `next-generation`;
- abstract benefit verbs: `unlock`, `empower`, `harness`, `leverage`,
  `streamline`;
- unsupported scale or completeness claims: `at scale`, `holistic`,
  `dynamic`, `comprehensive solution`;
- claims of efficiency, trust, safety, security, reliability, performance,
  insight, productivity, or innovation without a named mechanism or evidence;
- polished introductions that delay the concrete subject.

Domain projects may extend this list, but should avoid banning ordinary words
when the source uses them precisely.

## Validation

Use the strongest validation available in the target project:

- Confirm the source authority exists and supports the main claims.
- Confirm concrete system content is visible.
- Confirm unsupported claims were removed, repaired, or marked as blockers.
- Confirm citations use APA 7 when citations are required by the task.
- Run the optional warning-pattern script when useful.
- Run `<VALIDATION_COMMAND>` when the target project defines one.
- Compare against human references only after source-only candidate generation
  when using dataset comparison mode.

If domain truth, legal sufficiency, security, safety, or scientific validity is
outside the available evidence, state that limitation directly.

## Failure Modes

- Rewriting vague prose into smoother vague prose.
- Treating style as proof of truth.
- Adding capabilities or outcomes not present in the source.
- Dropping exact names, interfaces, constraints, or scope limits that define the
  system.
- Overfitting writing guidance to one reference sample.
- Using warning-word matches as automatic failure without reading context.
- Importing project-specific dataset commands, calibration numbers, paths,
  repository names, or model claims into the reusable template.

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
