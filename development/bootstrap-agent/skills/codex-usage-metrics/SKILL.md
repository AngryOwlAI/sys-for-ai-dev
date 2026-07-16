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

---
name: codex-usage-metrics
description: Capture the latest Codex app context, token, and rate-limit metrics from a session rollout file into a deterministic text receipt.
---

# codex-usage-metrics

## Purpose

Create a point-in-time text receipt of Codex usage metrics for the current or
selected session.

The skill is intended for systems-engineering observability: it records context
window usage, token usage, plan/rate-limit metadata, and reset times without
dumping conversation content.

## Codex App Scope

This skill is specifically for use within the Codex app, or within an adapted
workflow that has access to Codex app rollout/session files. It is not a
general OpenAI API billing tool, ChatGPT usage reporter, or generic telemetry
collector.

## When To Use

- The user asks for current Codex `/status` metrics or a saved metrics file.
- A systems-engineering workflow needs a lightweight usage receipt before a
  long task, handoff, or context-budget decision.
- A target project wants repeatable collection of context-window and rate-limit
  data from Codex session logs.

Do not use this skill to export message content, secrets, credentials, or
private session text.

## Inputs

- Optional `<SESSION_FILE>`: path to a Codex rollout JSONL session file.
- Optional `<SESSION_ID>`: session identifier used to find a rollout file under
  `<CODEX_HOME>/sessions`.
- Optional `<CODEX_HOME>`: Codex state directory. Defaults to `~/.codex`.
- Optional `<OUTPUT_FILE>`: metrics receipt path. Defaults to
  `<TARGET_SKILL_PATH>/usage-metrics.txt`.
- Optional `<CONTEXT45_SKILL_DIR>`: context-45 skill folder checked by the
  archive helper before a fresh session.

## Outputs

- A refreshed text file at `<OUTPUT_FILE>`.
- The default output is `usage-metrics.txt` inside this skill folder.
- The previous output file is deleted before the new file is created.
- For context-45 callers, a confirmed prior checkpoint archive at
  `<CONTEXT45_SKILL_DIR>/archived_temp_prd/temp_prd_date_yyyy-mm-dd-hh-mm-ss.md`.

## Procedure

1. Identify the intended Codex session.
   - Prefer `<SESSION_FILE>` when the session file is known.
   - Use `<SESSION_ID>` when a stable session identifier is known.
   - Otherwise allow the script to select the newest rollout file under
     `<CODEX_HOME>/sessions`.
2. Run the collector from the skill folder:

   ```sh
   python3 scripts/collect_usage_metrics.py --session-file <SESSION_FILE>
   ```

   Or, when adapting the skill:

   ```sh
   python3 scripts/collect_usage_metrics.py \
     --codex-home <CODEX_HOME> \
     --session-id <SESSION_ID> \
     --output <OUTPUT_FILE>
   ```

3. Confirm that the script reports the output path it wrote.
4. Read `usage-metrics.txt` when the user needs the metrics summarized.
5. Treat the receipt as point-in-time data. Any later model turn can change the
   live context and token totals.

## Script Behavior

The collector parses only `token_count` events from the selected rollout JSONL
file. It also reads the session metadata line when present. It does not export
chat messages, tool arguments, reasoning content, or full session logs.

Before writing the metrics file, the script removes the previous file at the
same path if one exists. This keeps the skill folder to one current receipt
rather than a pile of stale snapshots.

The archive helper checks or archives a context-45 skill folder's `temp_prd.md`
without reading conversation transcript content. `--check` is non-mutating.
`--confirm-archive` moves a regular file to
`archived_temp_prd/temp_prd_date_yyyy-mm-dd-hh-mm-ss.md`. It rejects symlinks,
non-files, and archive target collisions.

## Validation

- Run:

  ```sh
  python3 scripts/collect_usage_metrics.py --help
  python3 scripts/archive_temp_prd.py --help
  ```

- Run against a known rollout file and confirm:
  - The command exits with status `0`.
  - `usage-metrics.txt` exists in the skill folder or at `<OUTPUT_FILE>`.
  - The receipt includes session id, context window, context used, context left,
    primary and secondary rate limits, reset times, plan type, and token totals.
  - The receipt does not include conversation text.

## Failure Modes

- No rollout file can be found under `<CODEX_HOME>/sessions`.
- The selected rollout file has no `token_count` events yet.
- The newest rollout file is not the intended session when multiple Codex
  sessions are active.
- The file is generated correctly but becomes stale after subsequent messages.
- Rate-limit fields are absent or `null` in older or different Codex versions.

## Adaptation Notes

For project-specific adaptation, decide whether the target project should:

- Always pass an explicit `<SESSION_FILE>`.
- Select by `<SESSION_ID>`.
- Use a project-local output path instead of the skill-folder default.
- Add a validation command that checks receipt freshness before handoff.

Keep output deterministic unless the target project explicitly needs historical
snapshots.

## Provenance

Created as a reusable systems-engineering observability template for recording
Codex usage metrics. No project-specific private message content is required or
preserved.

## Adaptation Guide

When adapting this skill to a specific project:

- Replace placeholders with project-specific paths, commands, and authorities.
- Add project-specific validation commands.
- Preserve the rule that stale metrics output is removed before a new receipt is
  created.
- Preserve the rule that context-45 `temp_prd.md` archives require explicit
  caller confirmation and never overwrite an existing archive target.
- Do not expand the script into a session-content exporter.
- Document any project-specific assumptions introduced during adaptation.
