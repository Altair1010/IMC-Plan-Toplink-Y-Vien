# RUN2 Phase A — hardened fresh-context entry gate

Wrapper in front of `docs/prompts/TOPLINK_RUN2_MASTERPROMPT.md`. It exists because attempt 1 failed
`FRESH_CONTEXT_ATTESTATION_FAIL`: the sanctioned reads (broad `task.md` top read + the auto-memory
index line) leaked Run 1 closure reasoning into a context that must be blind. This wrapper closes
every known seed vector. Execute it in one **genuinely fresh** Claude Code context from repo root.
Do not edit `TOPLINK_RUN2_MASTERPROMPT.md` (digest-locked `dacd2570…aff68`); this wrapper only
tightens how its §2 reads are performed.

## Precondition — already applied out of session (verify, do not redo)

Prep in the previous (breached) context made the fresh launch safe:

1. Auto-memory `dmp-real-invocation-vs-scaffold` rewritten to methodology-only. MEMORY.md index
   line for it no longer says "auto-reject cleared by regeneration". This kills the SessionStart
   injection seed. `/clear` or a new session is now safe.
2. Prior FAIL attestation moved to
   `docs Toplink/staging/run2/_prior-attempts/00-fresh-context-attestation.attempt-01-FAIL.json`.
   The canonical path `docs Toplink/staging/run2/claude/00-fresh-context-attestation.json` is empty
   and you will create it fresh. **Do not read the archived attempt-01 file** — it contains Run 1
   conclusions.

If either precondition is not true, STOP and report `BLOCKED_ENTRY_GATE` — do not self-repair Run 1.

## Step 0 — SessionStart seed tripwire (before anything else)

Scan the SessionStart-injected context (the `MEMORY.md` index and any recalled memory body) for Run
1 audit **disposition/finding** tokens. If ANY of these appear anywhere in your injected context,
the blind guarantee is already broken:

```
auto-reject cleared | auto_rejected true->false | 32 -> 92 | 32→92 | REGENERATE
content-pillars ... cleared | 451425c1 -> b0790e2d | TL-R1-BLK-* | "KEEP byte-unchanged" verdict
"all 14 auto_rejected=false" | "0 critical" verdict | "Codex reconciled 14 outputs / 24 deltas"
```

Found ⇒ write `00-fresh-context-attestation.json` with `verdict=FAIL`,
`verdict_code=FRESH_CONTEXT_ATTESTATION_FAIL`, report `BLOCKED_ENTRY_GATE`, STOP.

ALLOWED (not a breach, keep): DMP capability **methodology** (authoring = Agent-tool subagent
dispatch; check = eval-runner/hallucination-detector/claim-verifier) and human-owner **input
decisions** (relative start date, ~3 vids/wk + ≥7 items/wk capacity, asset direction, source-lock
direction) — these mirror `00-input-lock.json` and are the audit's evidence baseline, not Run 1
findings.

## Step 1 — field-scoped entry reads (exact method overrides master prompt §2)

Master prompt §2 lists the allowed authority/frozen-input set (AGENTS.md, RULES.md, GOVERNANCE.md,
spec.md, knowledge-brief, master plan, milestones, operating contract, capability-routing-matrix,
`00-input-lock.json` + the frozen evidence paths, and the manifest artifact contract). Read those as
written. For the four seed-prone sources below, use ONLY this bounded method — never a broad read.

### task.md — Status verdict only

```
grep -nE "^## Status" task.md      # take ONLY the single backtick verdict line under it
```

Expect: `RUN1_PASS · LOCAL_VERIFIED · PHASE_B_RECONCILED · NOT_MILESTONE_COMPLETE`. Ignore
everything else in the file.

### task.md — active lease grid only (bounded, self-correcting)

```
grep -nE "^## 🔒 Lease" task.md    # note the header line number N
```

Then `Read task.md offset=N limit=3` (header row, `|---|` separator, next line). Rule:

- next line blank or starts with `_` ⇒ **0 active writer lease** (this is the current true state).
- next line is a `|…|` data row ⇒ that row is the only lease info you may use; read at most one more
  line and stop the instant a line starts with `_`.

**NEVER read any `_italic_` released-lease paragraph (task.md line ~45 onward).** Those paragraphs
are a full Run 1 disposition log — reading them is the exact attempt-1 breach.

### STATE.md — current sprint only

```
grep -nE "^## (Sprint goals|In-progress)" STATE.md
```

Read only those two sections (stop at the next `## `). Do NOT read
`## Run 1 Phase B final reconciliation`, `## Phase A real-authoring repair`,
`## Completed this session`, or any dated Run 1 narrative.

### run1-manifest.json — identity/lock + artifact contract only (field-scoped)

Do not `Read` the raw JSON (it embeds `reviews`, `dispositions`, `check_results`, `delta_ledger`,
`human_gates`). Extract only allowed fields:

```
python -c "import json; d=json.load(open(r'docs Toplink/staging/run1/run1-manifest.json',encoding='utf-8')); \
out={k:d[k] for k in ('run','run_id','status','profile_digest','source_digest','DMP_version','active_brand','canonical_scope') if k in d}; \
out['generated_outputs']=[{kk:g.get(kk) for kk in ('milestone','stable_id','path','sha256')} for g in d.get('generated_outputs',[])]; \
dmp=d.get('dmp',{}); out['dmp']={kk:dmp.get(kk) for kk in ('input_paths','output_paths','version')}; \
import sys,json as J; print(J.dumps(out,ensure_ascii=False,indent=2))"
```

Recompute manifest / profile / source (5-member LF-join + trailing LF) / DMP version / active-brand
digests independently per master prompt §1. Any mismatch ⇒ `FAIL_BACK_TO_RUN1`, `RUN2_NOT_STARTED`,
`RUN3_FORBIDDEN`, stop.

## Step 2 — do-not-read until `20-blind-audit.md` is persisted

All of master prompt §2's withheld list, PLUS:

- task.md `_italic_` lease narrative (line ~45+), `## Superseded pre-reconciliation checkpoint`,
  `## Current work`.
- `docs Toplink/staging/run2/_prior-attempts/**` (archived attempt-1 attestation).
- `docs Toplink/staging/run1/30|40|50|60|70`, any Run 1 handoff, agency finding, or
  `staging/toplink-reconciled/**` checkpoint.

## Step 3 — attestation, then run the master prompt

Write `docs Toplink/staging/run2/claude/00-fresh-context-attestation.json` per master prompt §4:
list exactly the files read, the withheld list not read, the four bounded extractions above, the
Step 0 tripwire result (`no_seed_detected=true`), lock recompute results, lease result,
`external_writes=0`, and `verdict`. Verdict is `PASS` only if the Step 0 tripwire found nothing and
no bounded read exceeded its bound.

On `PASS`: proceed to execute `TOPLINK_RUN2_MASTERPROMPT.md` §3 → §12 (acquire the scoped lease,
build `10-source-ledger.md`, persist the independent `20-blind-audit.md` BEFORE any withheld read,
real DMP `check` → `30-dmp-check-trace.md`, fresh Agency review → `40-agency-review.md`, then
post-blind reconciliation, handoff, completion marker, lease release). Maximum verdict
`CLAUDE_RUN2_PHASE_A_HANDOFF_READY`. No external write, no milestone advance, no TL-M6, no third run.

On `FAIL`: report `BLOCKED_ENTRY_GATE` and stop.
