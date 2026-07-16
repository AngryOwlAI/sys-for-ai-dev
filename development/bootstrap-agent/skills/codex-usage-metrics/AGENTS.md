# Codex Usage Metrics - Sys4AI-dev Runtime Adaptation

Canonical skill ID: `codex-usage-metrics`  
Canonical runtime path: `development/bootstrap-agent/skills/codex-usage-metrics`
Compatibility shim path: `.codex/skills/codex-usage-metrics/SKILL.md`  
Source import: `skills/codex-usage-metrics` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

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

# AGENTS.md

## Local Mission

Maintain `codex-usage-metrics` as a portable systems-engineering observability
template for collecting Codex app usage metrics without exporting conversation
content.

## Maintenance Rules

- Preserve the scope boundary: this skill is for Codex app rollout/session
  metrics, not API billing, ChatGPT usage reporting, or generic telemetry.
- Keep the collector stdlib-only.
- Keep the temp PRD archive helper stdlib-only.
- Keep `usage-metrics.txt` as a deterministic current receipt, not a history
  directory.
- Delete the previous metrics file before writing a new one.
- Keep context-45 archives confirmation-gated and collision-safe.
- Do not add code that dumps chat messages, reasoning content, secrets,
  credentials, or full rollout records.
- Do not hard-code one user's absolute paths into the reusable instructions.

## Portability Requirements

The template must work with placeholders for `<SESSION_FILE>`, `<SESSION_ID>`,
`<CODEX_HOME>`, and `<OUTPUT_FILE>`. Project-specific defaults belong in adapted
copies, not in this reusable template.

## Validation Requirements

Before finalizing changes, verify that:

- `SKILL.md`, `README.md`, and `AGENTS.md` exist.
- `scripts/collect_usage_metrics.py --help` runs successfully.
- `scripts/archive_temp_prd.py --help` runs successfully.
- A known rollout file produces a refreshed metrics text file.
- The output includes usage metrics and excludes conversation content.

## Adaptation Instructions

When adapting this skill, define how the target project selects the Codex
session, where the metrics receipt is stored, and how freshness is checked.
