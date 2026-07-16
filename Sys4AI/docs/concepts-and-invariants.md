# Concepts and invariants

Sys4AI separates a framework product, a runtime applying that framework, a host
supplying mechanisms, and target systems retaining their own authority.

Core invariants:

- requirements use stable identifiers;
- authority and validation are distinct;
- approval and implementation are distinct;
- evidence and capability claims are distinct;
- generated artifacts cannot promote themselves;
- execution requires current authorization and an explicit permission envelope;
- material self-change requires a separate approving actor;
- target systems retain independent authority and runtime state;
- source-first memory navigates to authority but does not replace it;
- retirement withdraws authority and preserves required evidence.

These dimensions remain independent: authority, lifecycle, approval,
implementation, validation, capability, and evidence freshness. A canonical
artifact can be unapproved; an implementation can be unvalidated; a passing
test can use stale evidence; and an operational system can still lack authority
for a new action.
