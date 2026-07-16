---
artifact_id: SFA-DEV-POLICY-BOOTSTRAP-AUTHORITY-001
artifact_type: policy
subject: development-system
subject_layer: development
authority: controlled
status: active
owner: system_director
supersedes: implementation_plans/self_hosting_boundary_decision_record.md
source_trace:
  - ADR-0001
  - ADR-0002
  - ADR-0003
---

# Bootstrap Authority Policy

The bootstrap agent may inspect registered project authority and implement the
active plan within the user's authorization. It may not approve product
purpose, expand its permissions, waive validation, promote a release, alter
external systems without explicit authority, or treat its output as approval.

Source precedence is:

1. Higher-priority platform and safety constraints.
2. Explicit user/project authorization.
3. Active PRDs and accepted ADRs.
4. Active implementation plan.
5. Current controlled state and exact evidence.
6. Generated bindings, readers, caches, and memory navigation.

Generated and retrieved material must resolve back to a controlled source before
it affects routing, requirements, permissions, or claims.
