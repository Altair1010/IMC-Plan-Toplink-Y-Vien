# TOPLINK_RUN2_PHASEB_CODEX — graph-structured fresh-Codex master prompt

Execute in one **genuinely fresh** Codex CLI context from the repository root. You are the fresh Codex
Phase B auditor/finalizer for `TOPLINK_RUN2_FRESH_AUDIT_FINALIZE`, single `TL-M1`–`TL-M5` package.
Claude Phase A is closed and handed off with verdict `CLAUDE_RUN2_PHASE_A_HANDOFF_READY`. Your job is an
**independent blind audit first**, then merge + evidence-grounded in-place repair of the eight Phase A
findings, gate-integrity validation, paired-manifest validation, and (only if an exact target is
approved) a bounded Sheet upsert + exact read-back. No new marketing version, no TL-M6, no third run.

This prompt is a **typed directed acyclic graph (DAG)** contract. It is deliberately harder than a
linear checklist: every node has a guard (entry predicate), an action, a postcondition (invariant that
must be proven true before any successor may fire), and a fail-edge to a fail-closed sink. Nodes execute
only in a topological order that satisfies all predecessors' postconditions. If any guard, invariant, or
postcondition cannot be proven, take the fail-edge — never "route around" a red node.

---

## 1. Authority precedence (unchanged)

1. Current explicit user instruction + platform safety rules.
2. `AGENTS.md`, `RULES.md`, `GOVERNANCE.md`.
3. `docs Toplink/TOPLINK_PAGE_MASTER_PLAN.md` (strategy/scope).
4. `docs Toplink/TOPLINK_PAGE_MILESTONES.md` (sequence/Done gates; §TOPLINK_RUN2 Phase B).
5. `docs/system/claude-codex-operating-contract.md` (runtime ownership/handoff/lease).
6. This prompt. On conflict with an authority above, stop only the affected node and record the
   conflict; do not silently reinterpret the contract.

---

## 2. Graph semantics

```
G = (V, E)
node v ∈ V := { id, guard: Predicate, action, post: Invariant, fail_edge: Sink }
edge (u → v) ∈ E fires  ⇔  post(u) proven ∧ guard(v) proven ∧ all_global_invariants_hold
Sinks (absorbing, no outgoing edge except STOP report):
  FAIL_BACK_TO_RUN1 · BLOCKED_ENTRY_GATE · BLOCKED_DMP_RUNTIME · BLOCKED_TARGET_INPUT ·
  BLOCKED_LEASE_CONFLICT · STOP_HUMAN_GATE
Accept sink:
  CODEX_RUN2_PHASEB_LOCAL_VERIFIED  (with sheet_status ∈ {SYNC_PENDING_TARGET, SYNC_READBACK_PASS})
```

Rules:
- **No forward edge without a proven postcondition.** A "probably fine" node is a red node → fail-edge.
- **Blindness is a temporal cut edge** (N3→N4): it may fire only after the Codex blind-audit digest is
  frozen and recorded. Reading `docs Toplink/staging/run2/claude/**` before that is an entry breach ⇒
  `FRESH_CONTEXT_ATTESTATION_FAIL` ⇒ `BLOCKED_ENTRY_GATE`.
- **Idempotent repairs only.** Every repair node must be replayable and must change only the bytes its
  finding names; unrelated bytes must stay identical (proven by digest diff).

---

## 3. Global invariants (must hold at EVERY node; violation = immediate fail-edge)

```
I1  external_writes = 0            until node N10c (Sheet upsert) with a signed SheetTargetApproval.
I2  profile_digest = a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349
I3  source_digest  = 3ba91761612ca482471dc1c071bd7e9d82e5708a3bb13ceb630fed476541fe76   (5-member
                     SHA-256 hex LF-join + one trailing LF)
I4  manifest(run1) = 99227153de577887966ae09124fdabcb2b3bf8ff23d838503531be507c2f4d2d
I5  DMP_version = 3.15.1 ∧ active_brand read-back = toplink-y-vien
I6  no item reaches HUMAN_APPROVED / PUBLISHED; no agent grants human APPROVED; no null→approved.
I7  Toplink isolation: zero Thảo Tây fact/target/credential/baseline/output in any touched file.
I8  no new fact/claim/pillar/stable-ID invented; repairs are evidence-grounded only.
I9  no _v2, no competing plan, no third macro-run, no milestone COMPLETE.
I10 single writer: exactly one active Codex lease row; hard-stop on any overlapping writer.
```
Any drift in I2–I5 ⇒ `FAIL_BACK_TO_RUN1` (persist evidence, release lease, STOP; never repair a lock
mismatch inside Run 2).

---

## 4. Entry node N0 — lock recompute (guard for the whole graph)

```
N0.action:
  recompute independently:
    manifest_sha256(docs Toplink/staging/run1/run1-manifest.json)  == I4
    profile_digest(C:/Users/MCBAu/.claude-marketing/brands/toplink-y-vien/profile.json) == I2
    source_digest = sha256( "\n".join(member_sha256[0..4]) + "\n" ) == I3
    each of the 5 source members byte-unchanged; DMP 3.15.1; active_brand toplink-y-vien
    14/14 generated_outputs byte-match run1-manifest generated_outputs[].sha256
    Run 1 status == RUN1_PASS · LOCAL_VERIFIED · PHASE_B_RECONCILED · NOT_MILESTONE_COMPLETE
    lease grid in task.md == 0 active writer row
N0.post:  all above TRUE
N0.fail:  I2–I5 mismatch → FAIL_BACK_TO_RUN1 ; lease/writer present → BLOCKED_LEASE_CONFLICT
```
Do not trust Claude's handoff digests as proof; recompute from disk. (Claude Phase A reference digests to
cross-check AFTER N4: manifest of the 14 outputs unchanged; blind-audit frozen sha256
`8625ceed415ae60bcc0202fa718608a73814693990389a196052518b1648ccaa`.)

---

## 5. Execution DAG

```
N0 locks ──▶ N1 lease ──▶ N2 blind-audit ──▶ N3 freeze-digest ──╌╌(temporal cut)╌╌▶ N4 read-Claude
   ──▶ N5 merge-ledger ──▶ N6 finding-resolution* ──▶ N7 gate-integrity ──▶ N8 promote+manifest
   ──▶ N9 paired-manifest ──▶ N10 sheet-subgraph? ──▶ N11 checkpoint+release ──▶ N12 verdict
* N6 is a sub-DAG over findings F01..F08 (+ any Codex-new findings), see §6.
```

### N1 — acquire lease
- guard: N0.post. action: write one scoped row in `task.md` lease grid (runtime, exact file set:
  `docs Toplink/staging/run2/codex/**`, the 14 canonical outputs to be repaired in place, `docs Toplink/
  staging/run2/run2-manifest.json`, `task.md`, `STATE.md`; ICT start; purpose).
- post: exactly one active writer row (I10). fail: overlapping row → `BLOCKED_LEASE_CONFLICT`.

### N2 — independent blind audit (BEFORE reading any Claude Phase A finding)
- guard: N1.post ∧ `docs Toplink/staging/run2/claude/**` NOT yet read.
- action: audit the 14 canonical outputs against the canonical plan/milestones + frozen
  `00-input-lock.json` evidence + the entity-franchise map, across the same 8 axes (evidence/entity,
  audience/positioning, pillars/FB, campaign/KPI, calendar/production, claim-safety, privacy/approvals,
  integrity). Persist to `docs Toplink/staging/run2/codex/20-blind-audit-codex.md`. A lack of finding
  must be evidence-backed, not assumed.
- post: `20-blind-audit-codex.md` exists ∧ contains ≥ the reference-integrity scan below.
- **Mandatory reference-integrity scan (Run 1 missed this at claim-ID granularity):** every claim ID
  used in `month-calendar.md §3` and `production-briefs.md §1` MUST resolve in the `month-calendar.md §1`
  claim register; every asset ID in `production-briefs.md`/batch plan MUST resolve in
  `asset-and-batch-plan.md §2`; every decision ID (`TL-D…`) cited MUST resolve to a canonical decision
  surface; every `§3.3` disclaimer reference MUST resolve to a canonical host.
- fail: cannot run scan → STOP (record blocker).

### N3 — freeze Codex blind-audit digest (temporal cut)
- guard: N2.post. action: compute + record `sha256(20-blind-audit-codex.md)` into
  `codex/25-blind-freeze.json` with ICT; write it to the `task.md` checkpoint.
- post: frozen digest recorded. **Only after this may N4 fire.**

### N4 — read Claude Phase A (gated)
- guard: N3.post. action: read `docs Toplink/staging/run2/claude/**` +
  `docs Toplink/staging/run2/handoff-claude-to-codex.md` + `handoff-envelope.json`. Cross-check Claude's
  recomputed locks + 14-output digests against your N0 recompute (must match).
- post: Claude ledger loaded; lock cross-check MATCH. fail: cross-check mismatch → `FAIL_BACK_TO_RUN1`.

### N5 — merge issue ledger
- guard: N4.post. action: form `L = Claude{F01..F08} ∪ Codex{blind findings}`. For each item tag
  `AGREES | NEW | CONTRADICTS | RUN1_ONLY_REVALIDATED`; assign a stable merged ID `TL-R2-M##`; keep both
  provenances. Do NOT upgrade a severity on model confidence; do NOT erase a Run 1 blocker the fresh
  audit did not rediscover.
- post: every ledger item has {merged_id, provenance, severity, class, route ∈ {DIRECT_REPAIR,
  DMP_SKILL_REAUTHOR, HUMAN_GATE, FAIL_BACK_TO_RUN1}, status}.

### N6 — finding-resolution sub-DAG (§6). N7 — gate integrity (§7 guards). N8 — promote+manifest (§8).
### N9 — paired-manifest (§8). N10 — Sheet sub-graph (§9). N11 — checkpoint+release. N12 — verdict (§10).

---

## 6. Finding-resolution sub-DAG (Phase A handoff F01–F08)

Each finding is a node `R(Fxx)` with guard = `N5.post ∧ Codex blind audit independently reproduced or
explicitly RUN1_ONLY_REVALIDATED this finding`. Repairs are **in place** on the named canonical file (no
`_v2`), evidence-grounded (I8), idempotent, and each edits ONLY the bytes the finding names. After every
repair: recompute the file's sha256, update `run2-manifest.json`, and prove no unrelated byte changed
(post). Ordering inside N6: resolve the two majors (M-F02, M-F08) before the minors; F08 is a fail-closed
HUMAN_GATE node.

| Node | Finding | Guard-specific check | Deterministic repair action | Files touched | Postcondition / re-verify | Fail-edge |
|---|---|---|---|---|---|---|
| `R(F02)` | **major** — orphan claim `CL-P2` on 6 health items (D08,D10,D11,D13,D23,D27) | Confirm `CL-P2` absent from `month-calendar.md §1` register and used in calendar §3 + production-briefs §1 | **Default (no-new-fact):** replace every `CL-P2` token with the already-defined, co-tagged `CL-M2` (support-level, source positioning §4/safety §3.1). **Alt (only if a distinct P2 claim is truly needed):** add a `CL-P2` register row sourced ONLY from positioning §4 / safety §3.1 with status `TOPLINK_CONFIRMED(support)` + condition `disclaimer + per-item professional review` — no new efficacy meaning. Pick exactly one; record rationale. | `month-calendar.md`, `production-briefs.md` (+`§1` if Alt) | Re-run the §N2 claim-ID scan → 0 orphan; both files re-hashed; manifest updated; health-item gates unchanged | any efficacy drift or new claim meaning → revert → STOP_HUMAN_GATE |
| `R(F08)` | **major** — disclaimer §3.3 anchors to `02_communication_safety.md` (sourced from UNVERIFIED `11_Product_Yvien.md`); canonical host `docs Toplink/system/health-compliance.md` (TL-M1 deliverable) ABSENT | Verify host file truly absent; verify §3.3 references in production-briefs/reels-briefs/workflow | **HUMAN_GATE — do not auto-create a health canonical file.** Creating `system/health-compliance.md` is a TL-M1 deliverable + health-sensitive wording = human-owned. Interim (allowed now): in each referencing file annotate the anchor as `DISCLAIMER_HOST_PENDING (TL-M1 health-compliance.md)` and keep the verbatim §3.3 text human-confirmed at publish; record the gate. Full fix (needs human): human authorizes the canonical host + final wording, then Codex creates it sourced from the safety taxonomy (not the raw UNVERIFIED product doc) and repoints references. | (interim) referencing files' anchor notes only; (full) new `system/health-compliance.md` + repoint | interim: anchor gap explicitly recorded, no wording invented; full: only after human authorization | wording change without human sign-off → STOP_HUMAN_GATE |
| `R(F01)` | minor — `TL-D16` real (STATE.md L109; task.md Part-2 `TL-D16–D20`) but not in master §3 register (D01–D15) | Confirm `TL-D16` decision text in STATE.md/task.md; confirm master register stops at D15 | Add a canonical pointer resolving `TL-D16..D20` (annotate that Part-2 decisions live in STATE/task under Direction-A; do NOT edit `TOPLINK_PAGE_MASTER_PLAN.md` — direction-A forbids). Prefer a pointer in the milestone status surface or a `decision-register-pointer` note. | milestone/status pointer note (NOT master plan) | `TL-D16` resolvable from a canonical surface; no gate wording changed | editing master plan → revert (direction-A violation) |
| `R(F03)` | minor — reels VERIFY says "6 health Reels", actual 5 (D08,D11,D14,D23,D27) | Recount P2/P4 Reels = 5 | Correct the VERIFY line to `5 (4×TL-P2 + 1×TL-P4)`; touch no brief body | `reels-briefs.md` | count == 5; re-hash; manifest updated | — |
| `R(F04)` | minor — workflow "10+6=16" double-counts D14/D26 | Distinct NEEDS_HUMAN_REVIEW = 14 | State 14 distinct + note D14/D26 overlap; set D26 binding `risk_class = product-adjacent` (health disclaimer inherited) | `workflow-approval-measurement.md` | ledger count unambiguous (14); re-hash | — |
| `R(F05)` | minor — `TL_PAGE_STRATEGY` dataset double-assigned (pillars + page-strategy) | Both map to same logical dataset; §18 = one file per tab | Resolve mapping: keep page-strategy → `TL_PAGE_STRATEGY`; map pillars → distinct tab (e.g. `TL_CONTENT_PILLARS`) or `TL_AUDIENCE_POSITIONING`; record in Sheet mapping | `content-pillars.md` and/or Sheet mapping note | 1 file ↦ 1 dataset; no collision | — |
| `R(F06)` | minor/strategy — founder-led D24 & D28 in one 5-window | Global ratio 4/28 OK; strict 5-window exceeded once | Either (a) record guardrail as **global ratio** (already met → NO_FINDING) or (b) reassign D28 to a non-founder pillar recap. Human picks interpretation if (b) changes content. | `content-pillars.md` guardrail note and/or `month-calendar.md` D28 | window rule stated + satisfied | content reassign w/o human → STOP_HUMAN_GATE |
| `R(F07)` | minor — stable-ID namespace drift (`TL-A0x`/`TL-P1..P5`/`TL-KPI-0x`/`CL-*` vs milestones §2.6 `TL-AUD/TL-PIL/TL-CAM/TL-KPI/TL-CLAIM-{NNN}`) | Cross-check namespaces | Reconcile: add an ID-namespace crosswalk (do not rename immutable IDs already emitted; map old↔canonical) OR adopt §2.6 forms consistently if no ID is yet externalized — pick the non-breaking option | crosswalk note (+ affected files only if non-breaking) | every ID resolves through the crosswalk; reference integrity PASS | breaking rename of an emitted immutable ID → revert |

Advisories (fold as hardening, not blockers): (a) each health-Reel §3.3 line inherits the "≤20s ⇒ hold to
end" dwell clause; (b) ledger invariant "no HUMAN_APPROVED with null content_hash" made explicit.

Any finding whose only correct route is `DMP_SKILL_REAUTHOR` requires a **new traced DMP invocation**
(trace_id, DMP 3.15.1, active-brand read-back, input/output digests) — manual rewrite is forbidden. None
of F01–F08 currently require it; if your independent audit escalates one, take the DMP-reauthor node, not
a hand edit.

---

## 7. N7 — gate-integrity validation (guard for promotion)

```
N7.post (all must hold):
  human gates preserved: TL-GAP-002/004/005/007/008/009/010, 012–014 (fail-closed),
    public-positioning approval, final-disclaimer wording (F08) — none agent-closed.
  I6 (no APPROVED/PUBLISHED/null→approved) holds across all repaired files.
  health items still route professional/human; consent gates intact (founder/BTS/UGC).
  franchise/legal public wording still absent; product efficacy still UNVERIFIED / customer-experience.
  isolation I7 holds.
N7.fail: any gate weakened by a repair → revert that repair → STOP_HUMAN_GATE.
```

## 8. N8 promote + manifest, N9 paired-manifest

- N8: promote repaired canonical outputs **in place** (no `_v2`). Rebuild `docs Toplink/staging/run2/
  run2-manifest.json` with the **paired-manifest contract** (milestones §"Paired manifest"):
  `run_id, profile_digest, source_digest, DMP_version, active_brand, workstreams, dmp_traces,
  generated_outputs[{stable_id,path,sha256}], reviewers, check_results, delta_ledger, human_gates,
  sheet_plan, readback, blockers, final_status`.
- N8.post: every changed file's new sha256 recorded; every unchanged canonical output's sha256 == its
  Run 1 value (byte-diff proof for untouched files).
- N9 paired-manifest validation:
  ```
  run2-manifest.profile_digest == run1-manifest.profile_digest  (I2)
  run2-manifest.source_digest  == run1-manifest.source_digest    (I3)
  run2.DMP_version == run1.DMP_version ; run2.active_brand == run1.active_brand
  both manifests parse; every path exists; every sha256 reads back exactly
  every merged finding id resolves; 0 orphan/duplicate stable ID
  ```
  N9.fail: profile/source/version/brand pair-mismatch → `FAIL_BACK_TO_RUN1`.

## 9. N10 — Sheet sub-graph (gated; default skip)

```
N10a guard: signed SheetTargetApproval exists (agent · spreadsheet/tab/range · input · action · limits ·
     expiry) per docs/system/toplink-google-sheets-operational-contract.md.
  absent ⇒ SKIP whole sub-graph ⇒ sheet_status = SYNC_PENDING_TARGET (I1 keeps external_writes=0).
N10b map: registry tab/schema/mapping/validation-error-states per the operational contract; resolve F05
     dataset assignment here; NO reuse of any Thảo Tây workbook; no invented/created target.
N10c upsert: bounded stable-identity upsert only (no full overwrite, no _v2); this is the ONLY node where
     external_writes may become >0, and only within the approved exact range.
N10d readback: exact-range read-back must match key/row/value/formula/Unicode/stable-ID/gate-fields;
     write-ack ≠ PASS. mismatch ⇒ do not mark complete; revert to SYNC_WRITTEN_UNVERIFIED + STOP.
N10.post: sheet_status ∈ {SYNC_PENDING_TARGET, SYNC_READBACK_PASS}.
```

## 10. N11 checkpoint/release, N12 verdict

- N11: checkpoint evidence in `task.md` (paths, digests, verdicts, open findings, human gates, sheet
  state, external_writes, next actor); stop writing the leased set; release the lease (grid → 0 active
  writer); mirror the concise sprint fact in `STATE.md`.
- N12 terminal verdict (exactly one):
  ```
  CODEX_RUN2_PHASEB_LOCAL_VERIFIED       — N9 PASS ∧ gates preserved ∧ sheet_status set; paired
                                            manifests share digests/version/brand and both PASS.
                                            final_status = NOT_COMPLETE unless SYNC_READBACK_PASS.
  FAIL_BACK_TO_RUN1 · BLOCKED_ENTRY_GATE · BLOCKED_LEASE_CONFLICT · BLOCKED_TARGET_INPUT ·
  BLOCKED_DMP_RUNTIME · STOP_HUMAN_GATE
  ```
  Never emit `RUN2_PASS`, milestone `COMPLETE`, human `APPROVED`, published, or synced beyond an actual
  `SYNC_READBACK_PASS`. A third macro-run is forbidden.

---

## 11. Safe-action edges (recommended actions, promoted to MANDATORY guards)

1. **Blind-before-findings** is a hard temporal cut (N3→N4); breaching it = `BLOCKED_ENTRY_GATE`.
2. **Repair only what a finding names**, in place, evidence-grounded, idempotent; prove untouched bytes.
3. **Two majors gate promotion:** `R(F02)` must reach 0 orphan; `R(F08)` must not fabricate health
   wording — it fails closed to `STOP_HUMAN_GATE` for the canonical-host decision.
4. **Digest algebra is law:** any change to a canonical output updates `run2-manifest`; profile/source/
   version/brand never change (drift ⇒ `FAIL_BACK_TO_RUN1`).
5. **Human gates are non-agent-closable;** preserve TL-GAP set + positioning + final disclaimer.
6. **Sheet only on exact approval → bounded upsert → exact read-back;** else `SYNC_PENDING_TARGET`.
7. **Isolation:** zero Thảo Tây fact/target/credential/baseline in any touched file.
8. **One writer, released at end;** no `_v2`, no TL-M6, no Run 3, no milestone COMPLETE/APPROVED.

## 12. Output/report contract

Report: nodes fired + their postcondition proofs; merged ledger (`TL-R2-M##` with AGREES/NEW/CONTRADICTS/
RUN1_ONLY_REVALIDATED); per-finding repair result + new file digests; gate-integrity result; paired-
manifest validation result; sheet state; `external_writes`; open human gates + owners; terminal verdict;
next safe action. Attach `run2-manifest.json` path + digest. If any node took a fail-edge, report the
exact node, the unmet predicate, and the evidence — do not summarize a red graph as green.
