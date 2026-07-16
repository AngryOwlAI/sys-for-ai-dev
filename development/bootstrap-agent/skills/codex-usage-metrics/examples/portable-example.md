# Portable Example

## Scenario

A systems-engineering agent is about to continue a long implementation-planning
thread. The user asks for a saved usage receipt before the next packet begins.

## Command

```sh
python3 scripts/collect_usage_metrics.py \
  --session-file <CODEX_HOME>/sessions/YYYY/MM/DD/rollout-<timestamp>-<SESSION_ID>.jsonl
```

## Expected Receipt Shape

```text
Codex Usage Metrics
Generated at: 2026-07-03 03:38:59 PM MDT
Metrics event: 2026-07-03 03:38:59 PM MDT
Session: <SESSION_ID>

Context:
  Window: 258,400 tokens
  Used: 65,718 tokens
  Left: 74.6%

Rate Limits:
  Primary: 82% left, resets 2026-07-03 03:52:08 PM MDT
  Secondary: 90% left, resets 2026-07-09 07:44:22 PM MDT

Token Usage:
  Cumulative total: 639,609 tokens
  Last request total: 67,386 tokens
```

## Validation

The receipt is acceptable when it gives a point-in-time metrics summary and does
not include the conversation transcript.
