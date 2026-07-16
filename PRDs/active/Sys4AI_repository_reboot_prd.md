---
artifact_id: SFA-PRD-REPOSITORY-REBOOT-001
artifact_type: prd
subject: development-system
subject_layer: development
authority: controlled
status: active
approval: approved
implementation: complete
validation: pass
owner: system_director
supersedes: null
source_trace:
  - repository-review-sha256:cc4684b8db7c90be65fbb3fcab65adfbd3efe38f732652c528805720f1532139
  - pre-reboot-2026-07-15
---

# Sys4AI Repository Reboot PRD

## 1. Objective

Extract the semantic value of the pre-reboot repository into a comprehensible,
self-contained monorepo while removing active-tree development history,
authority inversions, duplicated skill sources, generated-document authority
pressure, and product dependencies on the development workspace.

## 2. Scope

This change controls repository structure, bootstrap-runtime location, product
packaging, CLI boundaries, state and evidence retention, planning hygiene,
validation boundaries, and self-hosting configuration. It does not authorize
production deployment or autonomous release promotion.

## 3. Functional requirements

- **RB-001:** Keep one monorepo during the reboot and make `Sys4AI/`
  independently extractable.
- **RB-002:** Separate project control, bootstrap development, product,
  integration/target, and evidence planes.
- **RB-003:** Enforce the dependency direction development -> product ->
  generated target with no product dependency back into the repository root.
- **RB-004:** Provide `README.md`, `SYSTEM_MAP.md`, `PROJECT_STATUS.md`,
  `CHANGELOG.md`, an architecture index, and a decision index as human front
  doors.
- **RB-005:** Maintain exactly one canonical product baseline and one active
  change PRD; retain accepted Phase 1 and Phase 2 sources only as baselines or
  reference.
- **RB-006:** Maintain exactly one plan under
  `implementation_plans/active/`; remove compatibility pointers, duplicate
  IDs, completed plans, receipts, audits, and acceptance reports from the
  active planning tree.
- **RB-007:** Convert durable environment, self-hosting, boundary, bootstrap,
  and packaging decisions into ADRs.
- **RB-008:** Relocate canonical development skills and catalogs to
  `development/bootstrap-agent/`.
- **RB-009:** Generate minimal `.agents/` and `.codex/` host bindings from
  the canonical development skill catalog and validate every binding target.
- **RB-010:** Relocate development schemas and tools under `development/`;
  retire the name-migration validator and other completed migration machinery.
- **RB-011:** Make product skills independent assets under
  `Sys4AI/assets/skills/` with no path back to development skills.
- **RB-012:** Normalize the product distribution, package, and CLI to
  `sys4ai`; provide the repository-specific `sfadev` development CLI.
- **RB-013:** Split product domain, application, runtime, governance, memory,
  generation, assurance, CLI, port, and adapter concerns.
- **RB-014:** Move development program state, SFADEV transactions, decisions,
  handoffs, preflights, receipts, and historical registries out of the product
  and rely on the frozen baseline for archival history.
- **RB-015:** Retain generic product contracts, examples, policies, templates,
  role/skill/artifact catalogs, target generation, memory, trace, assurance,
  and host-adapter interfaces.
- **RB-016:** Move the self-hosting development profile under
  `development/bootstrap-agent/profiles/`; ship only a generic product schema
  and example.
- **RB-017:** Keep generic assurance templates in the product, release evidence
  under `development/evidence/releases/`, and omit transaction-numbered
  measurements from the active tree.
- **RB-018:** Replace the large registry set with
  `development/catalog/artifacts.yaml`,
  `development/catalog/skills.yaml`,
  `development/catalog/decisions.yaml`, and
  `development/trace/requirements.csv`; create smaller product type catalogs.
- **RB-019:** Remove committed generated documentation from the active product;
  generated readers may be local, CI, or release artifacts and remain
  noncanonical.
- **RB-020:** Move the repository-steward package to
  `integration/fixtures/target-systems/` and validate it as a derivative
  fixture, not a product asset or production claim.
- **RB-021:** Provide separate development, product, and integration workflows
  and root Make targets.
- **RB-022:** Preserve the current role, skill, and lifecycle guides as
  product-local explanatory sources without parent-path dependencies.
- **RB-023:** Ignore mutable `.sys4ai/` runtime state, caches, builds, local
  evidence, and generated readers.
- **RB-024:** Record the pre-reboot commit and tag and preserve historical
  sources through Git history and the dedicated legacy repository rather than
  copying them into the active tree.

## 4. Non-functional requirements

- **RNFR-001:** A new contributor shall be able to identify the development
  system, product, bootstrap runtime, active PRDs, active plan, current state,
  product validation, and target fixtures within five minutes.
- **RNFR-002:** Repository validators shall fail closed on missing authority,
  broken bindings, duplicate active plans, product parent dependencies,
  unregistered controlled artifacts, and product hygiene violations.
- **RNFR-003:** The migration shall preserve LICENSE and NOTICE unchanged.
- **RNFR-004:** The migration shall preserve uncommitted role/skill/lifecycle
  guide intent and shall not overwrite unrelated user work.
- **RNFR-005:** Source files shall use stable capability names; lifecycle phases
  and transaction numbers belong in evidence, not permanent APIs.
- **RNFR-006:** Structural passing results shall retain explicit non-production
  and non-semantic limitations.

## 5. Acceptance criteria

The reboot candidate is acceptable only when:

1. `make validate-development`, `make validate-product`,
   `make validate-integration`, and `make validate` pass.
2. From inside `Sys4AI/`, lint, tests, contract validation, asset validation,
   and build pass without a parent repository.
3. Product source contains no `SFADEV`, `temp_handoff`, `AJ-P1-`,
   `TX-35`, `../PRDs`, `../scripts`, or `.agents/skills` occurrence,
   except an explicitly labeled negative-test fixture.
4. Exactly one active implementation plan and one active change PRD exist.
5. Development state is small, current, and outside the product.
6. Generated docs are absent from tracked product source.
7. Host bindings are generator-produced and resolve to canonical development
   skills.
8. The target fixture validates through the product interface.
9. Self-hosting profiles, candidate isolation, independent verification, human
   promotion, and rollback are explicit.
10. Final diff, whitespace, and repository-hygiene checks show no unrelated
    loss or accidental authority duplication.

## 6. Rollback

The trusted rollback point is tag `pre-reboot-2026-07-15` at commit
`5a6aaf7652661e094cdfa40be55a380e9bc0cd8c`. Rollback shall use Git history or
a separate worktree; activated legacy records shall not be rewritten.
