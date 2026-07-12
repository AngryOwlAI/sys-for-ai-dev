# TX-34 Cross-Version Python CI Evidence

## Conclusion

`TX-34-CROSS-VERSION-PYTHON-CI` passes. The first retained dependency-ready external evidence obligation is closed for the current candidate baseline: GitHub Actions run [`29197460029`](https://github.com/AngryOwlAI/Sys4AI-dev/actions/runs/29197460029) executed the full repository-root validation from clean checkouts on Python 3.10, 3.11, 3.12, 3.13, and 3.14, and all five jobs passed.

This evidence supports cross-version compatibility of the current repository validation stack across the stable minors implied by `requires-python = ">=3.10"` on 2026-07-12. It does not prove package publication, stakeholder consensus, domain acceptance, production readiness, target-runtime operation, permission expansion, operational authority, or `G-10` acceptance.

## Authority And System Layer

- Accountable authorization: human-issued task instruction dated 2026-07-12.
- Gate decision: `DDR-SFADEV-STRATEGIC-BASELINE-G11-011`.
- Execution transaction: `TX-34-CROSS-VERSION-PYTHON-CI`.
- Candidate commit: `fe9b99fb89ebbc4550eae25cc2813fe4e4d65370`.
- Subject layer: `framework_product`; the workflow and CI validator are controlled development-system verification surfaces.
- External executor: GitHub-hosted `ubuntu-latest` runners with read-only repository contents permission.
- Frozen TX-23 ledger, TX-25 interpretation, canonical PRDs, and 227-row trace: unchanged.

## Selection Reasoning

TX-33 exhausted all locally executable verification obligations. Cross-version CI was selected before stakeholder, domain, production, or operational evidence because it was immediately executable with current authority and infrastructure. It required no unavailable target runtime, representative, specialist, production owner, monitoring interval, incident exercise, maintenance owner, secret, deployment permission, or operational grant.

## Workflow Contract

The controlled workflow:

- triggers on pushes to `main`, pull requests, and manual dispatch;
- grants only `contents: read`;
- uses `actions/checkout@v6` and `actions/setup-python@v6`;
- sets a 30-minute timeout per job and disables fail-fast so every minor yields evidence;
- creates a clean `Sys4AI/.venv`, installs only declared dependencies, and runs `make validate PY=python` from the repository root;
- contains no secrets, deployment, write permission, target runtime, or external mutation step.

The static validator and five-test suite fail closed on an omitted supported minor, write permission, and partial validation command.

## External Execution Evidence

| Python | Job ID | Result | Completed |
|---|---:|---|---|
| 3.10 | `86662895300` | Pass | 2026-07-12T15:05:18Z |
| 3.11 | `86662895290` | Pass | 2026-07-12T15:05:09Z |
| 3.12 | `86662895291` | Pass | 2026-07-12T15:05:03Z |
| 3.13 | `86662895307` | Pass | 2026-07-12T15:05:06Z |
| 3.14 | `86662895333` | Pass | 2026-07-12T15:05:20Z |

Run metadata:

- Workflow: `Cross-version Python`.
- Event: `push`.
- Run ID: `29197460029`.
- Candidate SHA: `fe9b99fb89ebbc4550eae25cc2813fe4e4d65370`.
- Started: 2026-07-12T15:04:08Z.
- Completed: 2026-07-12T15:05:21Z.
- Conclusion: `success`.
- Matrix: 5/5 jobs passed; each `Validate repository` step passed.

## Local Verification

- Cross-version workflow contract: 5/5 passed.
- Focused positive-negative tests: 5/5 passed.
- Candidate product suite: 334/334 passed before external publication.
- Final closeout product suite: 335/335 passed after receipt, handoff, and program-state reconciliation.
- Product aggregate validation: passed.
- Root aggregate validation before candidate publication and after closeout: passed.
- Generated derivatives: current and noncanonical.
- Patch integrity: passed.
- Memory status: `PASS_WITH_WARNINGS`; 1,248 objects, 563 known pending-hash warnings, zero authority inversions.
- Trace remains `pass=94`, `planned=133`; TX-34 adds external evidence without changing trace states or the 410 retained future-work dispositions.

## Residual Boundary

The following remain unexecuted or ungranted:

1. Quantitative vision success measures and accepted observation results.
2. Independent external, confidential, and rotated evaluation.
3. Broad stakeholder and affected-party review.
4. Target-domain evaluation and specialist acceptance.
5. Production target runtime, monitoring, incident and recovery exercise, maintenance ownership, and operational authorization.
6. Permission expansion and target-runtime authority.
7. Accountable `G-10` reacceptance.

## Rollback And Supersession

The candidate workflow was published before external evidence could exist. The successful run activates that evidence. Any later workflow repair or support-range change must use an additive transaction and preserve run `29197460029` as historical evidence. The workflow can be removed by an explicit superseding change, but the activated decision, report, receipt, and run reference must not be rewritten.

## References

GitHub. (2026). *Running variations of jobs in a workflow*. https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations

GitHub. (2026). *setup-python*. https://github.com/actions/setup-python

Python Software Foundation. (2026). *What’s new in Python 3.14*. https://docs.python.org/3.14/whatsnew/3.14.html

Sys4AI-dev. (2026). *Sys4AI-dev strategic baseline migration full implementation plan* [Implementation plan].
