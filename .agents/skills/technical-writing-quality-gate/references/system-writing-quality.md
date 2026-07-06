# System Writing Quality Reference

Use this reference when drafting, revising, or evaluating substantial technical
or system descriptions.

## Concrete System Content

A strong technical description usually answers:

- What is the system?
- What job does it perform?
- Who uses it, operates it, maintains it, or depends on it?
- What inputs, outputs, interfaces, data flows, or dependencies matter?
- What workflow, control loop, decision process, or lifecycle state does it
  support?
- What constraints, risks, failure modes, limits, or open questions should the
  reader understand?
- Which outcomes are supported by source evidence rather than asserted as
  promotional claims?

## Human Engineering Prose

Prefer:

- specific nouns over abstract labels;
- active verbs over inflated phrasing;
- short causal sequences over slogan-like claims;
- concrete tradeoffs over one-sided praise;
- named uncertainty where evidence is incomplete;
- source-backed mechanisms before benefits.

Avoid making every system sound frictionless, autonomous, intelligent,
powerful, scalable, reliable, secure, or transformative unless those qualities
are shown by evidence.

## Warning Patterns

These are warning signs, not banned words:

- `seamless`, `robust`, `cutting-edge`, `transformative`, `revolutionary`;
- `unlock`, `empower`, `harness`, `leverage`, `at scale`;
- `game-changing`, `next-generation`, `holistic`, `dynamic`;
- claims of improved efficiency, trust, safety, security, performance, or
  insight without a mechanism;
- lists of benefits that do not name system behavior;
- polished introductions that delay the concrete subject.

## Evaluation Checklist

Return `pass` when the text is concrete, accurate relative to supplied sources,
audience-fit, and free of unsupported claims.

Return `repair` when the problem is fixable from available context, such as
vague wording, inflated tone, weak sequence, unsupported benefit language, or
missing concrete system nouns.

Return `block` when missing information prevents responsible writing or review,
such as absent source facts, unclear audience, missing authority, unsupported
claims, or unavailable comparison data.

## Dataset Iteration Rule

When using a human reference dataset:

1. Generate from the topic and source brief only.
2. Compare against the human reference only after generation.
3. Identify repeated source coverage, tone, vocabulary, sentence-shape, and
   unsupported-claim gaps.
4. Revise local guidance only when the gap is general enough to improve future
   outputs.
5. Treat metrics as review aids, not as proof of correctness or authorship.
