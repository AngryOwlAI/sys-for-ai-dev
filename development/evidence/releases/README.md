# Release Evidence

Each accepted release receives one immutable directory:

    <version>/
      release-manifest.yaml
      requirement-coverage.csv
      validation-summary.md
      security-summary.md
      test-results.json
      unresolved-risks.md

Transaction-by-transaction logs remain CI or local artifacts unless a release
owner explicitly selects them for the bundle.
