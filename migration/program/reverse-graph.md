# KTD Great Migration Reverse Dependency Graph

## Terminal state

`KTD_CURRENT_CANONICAL`

```text
KTD_CURRENT_CANONICAL
  <- CUTOVER_RECORD_VALID                         [GM-9]
  <- ACCEPTANCE_MATRIX_PASS                       [GM-8]
  <- RUNTIME_REWIRED_AND_VERIFIED                 [GM-7]
  <- CONTROL_PLANE_COMPLETE_AND_RESOLVABLE        [GM-6]
  <- HUMAN_WORKBOOK_USABLE_AND_CANONICAL          [GM-5]
  <- DRY_RUN_CAMPAIGN_AND_PIPELINE_USABLE         [GM-4]
  <- STRATEGY_LAYER_COHERENT                      [GM-3]
  <- MIGRATION_LEDGER_COMPLETE_FOR_ACTIVE_OBJECTS [GM-2]
  <- CURRENT_KTD_TRUTH_COHERENT                   [GM-1]
  <- BASELINE_REPRODUCIBLE                        [GM-0]
  <- PACKAGE_AND_SOURCE_INTEGRITY_KNOWN           [GM-0]
```

## Earliest prerequisite

The earliest prerequisite is package and source identity. A mismatch would invalidate
every downstream lineage, target, and cutover claim. The cheapest discriminating probes
are checksum verification, Git identity/hash inspection, and read-only Sheet metadata.

## Initial probe result

- All 16 checksummed package files match.
- Local and remote `main` resolve to commit `f9ea6b61941dd46872acc39d180b8d847ceb1ec7`.
- The package label `tree_sha` names that commit; the actual Git tree object is
  `d0067ecd3803b5fb059df06fd2b76a71babd54ca`.
- `STATE.md` matches packaged blob `065467257858f2a9873db59ff4a591a936a6493e`.
- The live workbook ID and 22-tab legacy topology match the package baseline.

The route is therefore not falsified, subject to current-truth and deeper Sheet content inspection.
