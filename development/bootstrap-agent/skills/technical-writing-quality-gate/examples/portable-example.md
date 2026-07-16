# Portable Example: Release Readiness Copy Repair

## Scenario

A project team is preparing a short description of a release-readiness
dashboard. The draft must be checked before publication.

## Source Boundary

In a real adaptation, replace this section with the target project's source
documents, code paths, requirements, or authority records.

Example source facts:

- The dashboard reads CI status, deployment checklist state, and reviewer
  approvals.
- It shows blocking items before a release manager approves deployment.
- It writes an audit record when approval is granted or denied.
- The source does not claim automated deployment, improved security, or reduced
  incident rates.

## Draft

```text
Our next-generation dashboard unlocks seamless release confidence at scale by
empowering teams with robust insights and improved security.
```

## Gate Result

`repair`

Reasoning: the draft contains unsupported benefit claims and does not identify
the actual system mechanics.

## Repaired Text

```text
The release-readiness dashboard gives release managers one place to check CI
status, deployment checklist state, and reviewer approvals before approving a
deployment. When approval is granted or denied, the dashboard records the
decision in the audit log.
```

## Validation Notes

- The repaired text preserves the supplied actors, inputs, decision point, and
  audit output.
- Unsupported claims about security, scale, and incident outcomes were removed.
- No citation is shown because the example uses hypothetical local source
  facts. In a real publication, cite supplied documents in the target project's
  required format.
- Optional script check:

```sh
python3 scripts/technical_writing_warning_gate.py <PROJECT_ROOT>/<TARGET_DOCUMENT_PATH>
```

## Adaptation Notes

Replace the scenario, source facts, target document path, and validation command
with the target project's evidence and tooling. Do not treat this example's
dashboard domain as a required project convention.
