# TOPLINK Run 2 Phase B — final QA

## Verdict

`PASS · CODEX_RUN2_PHASEB_LOCAL_VERIFIED · NOT_COMPLETE`

## Node evidence

- N0: manifest/profile/source/DMP/brand locks match; 5/5 sources and 14/14 Run 1 outputs matched at entry.
- N1: one scoped Codex writer lease; no overlap.
- N2: eight-axis independent audit + mandatory reference scan persisted.
- N3: blind audit frozen before withheld read at SHA-256 `f56264b3a95d799b41313eee63a25a63bf90eb94627dbabaf4374005b0f82720`.
- N4: Claude locks match; 7/7 envelope-listed artifacts match; Claude blind digest `8625ceed…` matches; 14/14 canonical outputs matched at handoff read.
- N5: 10 merged ledger items: 8 AGREES, 1 Codex NEW, 1 Phase-A metadata CONTRADICTS resolved in recipient ledger.
- N6: targeted repairs complete; 7 outputs changed, 7 byte-unchanged; no DMP reauthor; no new fact/claim/pillar/stable ID.
- N7: safety/gate and reference audits PASS; claims/assets/decisions unresolved = 0/0/0; all human/legal/privacy/consent gates retained.
- N8: repaired candidates promoted in place; no `_v2`.
- N9: paired manifest PASS; profile/source/DMP/brand pair-match, 14 paths/hashes exact, 10/10 merged IDs unique.
- N10: signed `SheetTargetApproval` absent; subgraph skipped; `BLOCKED_TARGET_INPUT · SYNC_PENDING_TARGET`; `external_writes=0`.

## Mechanical checks

| Check | Result |
|---|---|
| Run 2 manifest JSON parse | PASS |
| Generated output path/hash read-back | 14/14 PASS |
| Changed vs Run 1 | 7 changed / 7 byte-unchanged |
| Duplicate output/merged IDs | 0 / 0 |
| Claim/asset/decision orphan | 0 / 0 / 0 |
| Calendar / `NEEDS_HUMAN_REVIEW` rows | 28 / 14 |
| UTF-8 / final newline failures | 0 / 0 |
| Secret/private-key patterns | 0 |
| Cross-brand matches in 14 outputs | 0 |
| Scoped `git diff --check` | PASS |
| Actionable TODO/TBD/CHANGEME | 0 (one allowed negation-only “không tạo plan/todo cạnh tranh” control) |
| Human `APPROVED` or `PUBLISHED` granted | 0 |
| Page/Sheet/publish/profile external mutation | 0 |

## Final manifest

- Path: `docs Toplink/staging/run2/run2-manifest.json`
- SHA-256: `a4e6de7582e7d1c51136029e16ffaf266906d97f721cf3510a7768b40c86e939`
- `paired_manifest_status=PASS`
- `sheet_plan.sync_state=SYNC_PENDING_TARGET`
- `final_status=NOT_COMPLETE`

Open human gates remain listed in the manifest, including final disclaimer wording and founder D24–D28 sliding-window choice. This QA does not grant publish approval or milestone completion.
