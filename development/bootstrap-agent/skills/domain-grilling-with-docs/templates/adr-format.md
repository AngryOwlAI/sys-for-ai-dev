# ADR Format Template

Use this template when a target project needs a lightweight architecture
decision record. Adapt the directory, numbering, and status conventions to the
target project.

## Default Location

```text
<PROJECT_ROOT>/<ADR_DIRECTORY>/
```

Use sequential numbering when the target project does not define another
scheme:

```text
0001-<short-slug>.md
0002-<short-slug>.md
```

Create the ADR directory lazily. Do not create an ADR until there is a settled
decision worth preserving.

## Minimal Template

```md
# <Short Decision Title>

<One to three sentences explaining the context, the decision, and why this
choice was made.>
```

## Optional Sections

Use optional sections only when they add real value.

```md
---
status: proposed | accepted | deprecated | superseded by ADR-NNNN
---

## Considered Options

- <Option A>
- <Option B>

## Consequences

- <Non-obvious downstream effect>
```

## When To Create An ADR

Create or offer an ADR only when all three conditions are true:

- The decision is hard to reverse.
- The decision would be surprising without context.
- The decision came from a real tradeoff between plausible alternatives.

Skip the ADR when the decision is obvious, easy to reverse, purely local, or
not yet settled.

## Good ADR Subjects

- Architecture shape, service boundaries, or ownership boundaries.
- Integration patterns between modules, services, or contexts.
- Technology choices with meaningful lock-in.
- Deliberate deviations from the obvious path.
- Constraints not visible in code.
- Rejected alternatives when future readers are likely to revisit them.
