# 20 — Runtime compatibility reconciliation

Status: `LOCAL_READBACK_PASS · TL-M1_TO_TL-M5_COMPATIBLE`

No runtime mutation was performed by Codex.

| Gate | Exact read-back | Verdict |
|---|---|---|
| DMP version | installed plugin path and both Phase A markers = `3.15.1` | `PASS` |
| Active brand | `brands/_active-brand.json.active_slug=toplink-y-vien`; markers agree | `PASS` |
| Profile digest | `a45e4ae49f60308654df49381caea8bd3cd24cb415fcb071c05cb064c8cbe349` | `PASS` |
| Source digest | `3ba91761612ca482471dc1c071bd7e9d82e5708a3bb13ceb630fed476541fe76`; 5/5 members | `PASS` |
| Thảo Tây isolation | no reused external target, credential, deliverable, baseline or milestone | `PASS` |
| Runtime/Page/Sheet/publish mutation | none | `PASS_ZERO` |

## Real DMP evidence coverage

| Trace ID | Milestone | Capability / mechanism | Raw evidence | Status |
|---|---|---|---|---|
| `TL-M1-DMP-SWITCH-001` | TL-M1 | deterministic guarded brand switch | `staging/toplink-reconciled/TL-M1-evidence/tl-m1-dmp-trace.md` | `VERIFIED_REAL_INVOKE` |
| `TL-M1-DMP-IMPORT-001` | TL-M1 | deterministic guideline import | same trace; active-brand read-back and output digests | `VERIFIED_REAL_INVOKE` |
| `TL-M2-DMP-BRAND-002` | TL-M2 | non-mutating `brand-setup` proposal | raw output + invocation sidecar | `VERIFIED_REAL_INVOKE` |
| `TL-M3-DMP-AUD-002` | TL-M3 | `audience-intelligence` | raw output + invocation sidecar | `VERIFIED_REAL_INVOKE` |
| `TL-M3-DMP-CAMP-002` | TL-M3 | `campaign-plan` positioning/narrative | raw output + invocation sidecar | `VERIFIED_REAL_INVOKE` |
| `TL-M3-DMP-SOC-002` | TL-M3 | `social-strategy` pillars | raw output + invocation sidecar | `VERIFIED_REAL_INVOKE`; `REGENERATE` |
| `TL-M3-DMP-SOC-003` | TL-M3 | `social-strategy` Page strategy | raw output + invocation sidecar | `VERIFIED_REAL_INVOKE` |
| `TL-M4-DMP-CAMP-002` | TL-M4 | `campaign-plan` architecture/KPI | raw output + invocation sidecar | `VERIFIED_REAL_INVOKE` |
| `TL-M5-DMP-CAL-002` | TL-M5 | `content-calendar` | raw output + invocation sidecar | `VERIFIED_REAL_INVOKE` |
| `TL-M5-DMP-ENG-002` | TL-M5 | `content-engine` | raw output + invocation sidecar | `VERIFIED_REAL_INVOKE` |
| `TL-M5-DMP-VID-002` | TL-M5 | `video-script` | raw output + invocation sidecar | `VERIFIED_REAL_INVOKE` |

The TL-M1 trace records exact timestamps, mechanisms, active-brand read-back and outputs under the frozen
Run 1 lock; the run-level lock supplies the common DMP `3.15.1` context. The nine M2–M5 authoring
sidecars each independently record version, brand, inputs, raw output hash, selected outputs, status and
`external_writes=0`. Evaluator scripts remain separate `check` evidence and are not counted as authoring.

No active trace is labeled scaffold, planned, manual-only or read-back-only. Run 2 must use the same lock.
