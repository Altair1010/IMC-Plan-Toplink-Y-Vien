# GM-0 Requirement-to-Evidence Matrix

- Revision under test: `program/ktd-great-migration` from `f9ea6b61941dd46872acc39d180b8d847ceb1ec7`
- Input revisions: migration package v1.0; legacy workbook metadata read at run start

| REQ_ID | Requirement | Acceptance condition | Required evidence | Observed evidence | Verdict | Notes |
|---|---|---|---|---|---|---|
| GM0-01 | Package files present | All mandatory files and templates are readable | E1 | `docs Toplink/KTD-GREAT-MIGRATION-PACKAGE-v1.0/` inventory | PASS | 16 checksummed files plus checksum manifest present. |
| GM0-02 | Package integrity known | Every checksum matches | E2 | `migration/baseline/baseline-manifest.json` | PASS | 16 of 16 match. |
| GM0-03 | Repository identity proven | Local path and origin match the package | E1 | `migration/baseline/baseline-manifest.json` | PASS | Exact GitHub origin match. |
| GM0-04 | Source revision proven | Local and remote main match packaged source revision | E2 | `migration/baseline/baseline-manifest.json` | PASS_WITH_NOTE | Package calls a commit SHA a tree SHA; both objects are preserved explicitly. |
| GM0-05 | Working tree recorded | Existing changes are listed and preserved | E1 | `migration/baseline/baseline-manifest.json` | PASS | Three pre-existing untracked package/spec paths preserved. |
| GM0-06 | Workbook identity and topology proven | ID, title, locale, timezone, and tab topology match | E3 | live Sheets metadata; baseline manifest | PASS | 22 sheets: 21 legacy human-layer sheets plus `Trang tính1`. |
| GM0-07 | Isolated target exists | Target ID differs and copied topology reads back | E3 | staging workbook metadata; baseline manifest | PASS | Distinct ID with 22 copied sheets. |
| GM0-08 | Legacy lineage remains reachable | Stable repository and workbook pointers exist | E1 | `migration/baseline/legacy-reference.md` | PASS | No rename or deletion. |
| GM0-09 | Durable state initialized | Resume file contains route, phase, evidence, and gates | E2 | parsed `migration/state/KTD_GREAT_MIGRATION_STATE.json` | PASS | JSON parse check passed. |
| GM0-10 | AMH evidence initialized | Run record exists at required path | E2 | parsed `F:/tmp/evidence AMH v0.3/runs/2026-09/KTD-GM-20260914-201546-f9ea6b6/run.json` | PASS | Persistence confirmed. |

- HARD_FAILS: none
- OPEN_UNKNOWNS: current KTD fact coverage outside the live owner instruction and package
- CONVERGENCE: PROGRESSING
- NEXT_SIGNAL: current-source inventory and fact provenance extraction
- PROMOTION_ALLOWED: YES
