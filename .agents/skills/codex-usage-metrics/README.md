# Codex Usage Metrics - sys-for-ai-dev Runtime Adaptation

Canonical skill ID: `codex-usage-metrics`  
Canonical runtime path: `.agents/skills/codex-usage-metrics`  
Compatibility shim path: `.codex/skills/codex-usage-metrics/SKILL.md`  
Source import: `skills/codex-usage-metrics` from `/Volumes/P-SSD/AngryOwl/ai-skills-for-sys`

## sys-for-ai-dev Authority Rules

- Root PRDs, implementation plans, source registries, validators, and git-tracked files outrank generated outputs.
- `sys-for-ai/` is the product scaffold being developed; it is not the full development workspace.
- `.agents/skills/<skill-id>/` is the active runtime skill surface for this repository.
- `.codex/skills/<skill-id>/SKILL.md` is compatibility-only and must point back to this canonical path.
- Existing `sys-for-ai/skills/core/` files are scaffold and product-reference adapters, not the active runtime authority.
- Do not import local receipts, caches, generated `usage-metrics.txt`, or private operational state as skill source.
- Treat generated PRDs, plans, diagrams, warnings, and handoffs as derivative work until accepted by the relevant project authority.

The imported source guidance below remains valid where it does not conflict with these sys-for-ai-dev rules.

---

# codex-usage-metrics

## Purpose

Reusable systems-engineering observability skill for saving Codex context,
token, and rate-limit metrics to a text receipt.

## Codex App Scope

This skill is specifically scoped to the Codex app. It reads Codex app
rollout/session data and should not be used as a general OpenAI API billing,
ChatGPT usage, or non-Codex telemetry tool.

## When To Use

Use this skill when a user asks for current Codex status metrics, or when a
workflow needs a saved point-in-time usage receipt before continuing.

## What It Produces

- `usage-metrics.txt` in this skill folder by default.
- Context window, context used, context left, token totals, plan type, primary
  rate limit, secondary rate limit, and reset times.
- No conversation transcript or message content.

## Required Files

- `SKILL.md`: executable workflow.
- `README.md`: human-facing summary.
- `AGENTS.md`: maintenance and adaptation rules.
- `scripts/collect_usage_metrics.py`: metrics collector.

## Basic Usage

```sh
python3 scripts/collect_usage_metrics.py --session-file <SESSION_FILE>
```

If no session file is supplied, the script searches `~/.codex/sessions` and uses
the newest rollout JSONL file it can find.

## Output Refresh Rule

The collector deletes the previous output file before writing the new receipt.
When the output filename stays `usage-metrics.txt`, this keeps one current
metrics file in the skill folder.

## Adaptation Summary

Replace `<SESSION_FILE>`, `<SESSION_ID>`, `<CODEX_HOME>`, and `<OUTPUT_FILE>` as
needed. Add project-specific freshness checks or handoff rules only when they
are required by the target project.

## Validation Summary

Run the collector against a known Codex rollout file and confirm that the output
contains usage metrics but no conversation text.
