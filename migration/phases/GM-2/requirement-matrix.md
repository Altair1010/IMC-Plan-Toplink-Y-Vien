# GM-2 Requirement-to-Evidence Matrix

- Revision under test: `eb5e1aa` plus current GM-2 artifacts
- Input revisions: 22-sheet live metadata; package repository material map; runtime dependency scan

| REQ_ID | Requirement | Acceptance condition | Required evidence | Observed evidence | Verdict | Notes |
|---|---|---|---|---|---|---|
| GM2-01 | Active inventory complete | All 22 workbook tabs and material repo/runtime consumers are listed | E2 | `active-legacy-object-inventory.csv` | PASS | 50 unique semantic objects. |
| GM2-02 | One disposition per object | Inventory and ledger object IDs form an exact one-to-one set | E2 | deterministic CSV coverage query | PASS | 50 of 50 classified; no duplicate IDs. |
| GM2-03 | Removed constraints archived | Legal reviewer approval claim and experiment objects are ARCHIVE_ONLY | E2 | `archive-only.csv`; ledger status scan | PASS | Excluded from active target and runtime. |
| GM2-04 | Transformations sourced | REPLACE REVALIDATE and TRANSFORM rows have a current source | E2 | non-empty source validation | PASS | Unknown-register pointers are used when current validation is still pending. |
| GM2-05 | Unknowns do not promote | Revalidation queue names the blocking unknown | E1 | `revalidation-queue.csv` | PASS | Five rows remain explicitly dependent on current evidence. |
| GM2-06 | Target lineage explainable | Every target surface maps to legacy inputs and current authority | E1 | `target-lineage-map.csv` | PASS | Legacy is input lineage rather than current authority. |
| GM2-07 | Runtime consumers classified | Sync builder registry tests and loaders have dispositions | E1 | KTD-L-044 through KTD-L-050 | PASS | Legacy runtime remains untouched. |

- HARD_FAILS: none
- OPEN_UNKNOWNS: five revalidation rows remain excluded from current factual population
- CONVERGENCE: PROGRESSING
- NEXT_SIGNAL: build source-bounded target strategy surfaces
- PROMOTION_ALLOWED: YES
