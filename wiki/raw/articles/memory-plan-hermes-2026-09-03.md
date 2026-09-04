---
source_url: local://opt/data (internal working document)
ingested: 2026-09-04
sha256: b041cb07a4b094125540ce8b6497637662838fae776b6a02601fd9805cf9690b
---

# Comprehensive Memory Plan — Hermes four-system topology

2026-09-03 · Author: Joan Harris · v2 — council-reviewed (4/4 seats), revised & finalized
**Implementation status (2026-09-04):** Phases 0–3 executed. Nightly backup live (first run green, restore drill PASSED 325/54/215/70 exact match, cron `memory-nightly-backup` @ 04:00). Weekly consolidation live (`memory-weekly-consolidate` @ Sun 05:00, hot banks only). Service watchdog live (`service-watchdog` @ 6h, recovery drill PASSED on embed server). Bank hygiene audit done: hindsight_banks.py registry is stale (only 5 of 54 banks listed — needs regeneration, not deletion), one slug collision (agent-joan + char-joan — deliberate dual role, documented not merged), char-Dārta_Ozola vs agent-darta-ozola diacritic drift. Phase 6 Honcho: SKIPPED per Daniel. Off-container backup: option (a) weekly pull — Daniel's action, pending.

**Episodic loop verification (2026-09-04):** retain→extract→store→recall verified LIVE — plan decisions retained into agent-joan, M3 extracted (682 tok), recall returns them verbatim. Diagnosis: the loop was idle since Sept 1, not broken — the only automatic write path is hindsight_bridge (fires on character-world scene ops); Hermes sessions do not auto-retain. Consequence: Phase 2.5 retain-outcome hooks are the missing loop-closer and are now the top open item. Interim: with MEMORY.md host-locked, agent-joan bank is carrying the durable decision record.
**Episodic loop CLOSED (2026-09-04):** decision = nightly batch retain (Daniel-approved, not end-of-session hooks). Built `/opt/data/scripts/nightly_retain.py` — one dated ops digest (backup status/sizes, watchdog starts/fails, consolidation results, SHRINK alerts) retained into agent-maintenance daily at 04:30 via cron `memory-nightly-retain`. First digest retained + recall-verified. The 3 crons themselves need no separate hooks — their logs ARE the digest inputs.
Scope: Hindsight (episodes), ActiveGraph (state), my-wikid (knowledge), OpenViking (index), base layer (MEMORY.md/USER.md/session search). Optional: Honcho.

## 1. Current state — verified on this machine today

| Layer | Status | Evidence |
|---|---|---|
| Hindsight (episodes) | **Running, healthy** | `GET :8888/health` → healthy, db connected; MiniMax-M3 extraction; 54 banks (agent-* + char-*) |
| Hindsight durability | **Gap** | No pg_dump cron for its Postgres (:5432). No restore drill ever run. No off-container copy. |
| Consolidation | **Gap** | `/consolidate` endpoint exists; nothing schedules it. Reflect unused. |
| ActiveGraph (state) | Live | world.db, schema v2, bridge mirrors ops into Hindsight banks |
| my-wikid (knowledge) | Live, idle-ish | index/log current as of 2026-09-01; qmd 0.9.0 indexed; git push pending (creds not in sandbox) |
| OpenViking (index) | Live | :1933, key-authed |
| Base layer | **Degraded** | MEMORY.md writes failing all day ("file exists but could not be read" — lock/encoding). Session search healthy. |
| Honcho | **Not installed** | Never installed; candidate #4 in the 2026-08-30 provider audit, unadopted. |

## 2. Best-practice foundations (researched 2026-09-03)

- **CoALA four-tier separation** (working/episodic/semantic/procedural as functional roles) — our topology already respects it. Keep separation sacred; route by memory kind. [arXiv 2309.02427]
- **Consolidation is not per-turn** — RecMem (ACL 2026): recurrence-triggered consolidation cuts token cost up to 87% with equal-or-better accuracy vs eager extraction. Consolidate on cadence or threshold, never per message. [aclanthology 2026.findings-acl.1619]
- **Idempotent consolidation + provenance** — re-running must not duplicate; every derived fact links to source episodes; originals are never destroyed by synthesis. [Geodocs agent-memory spec]
- **Composite retrieval scoring** — relevance × recency × frequency × pinned, with tier-specific half-lives. Simplified per council for solo scale: recency-ranked + pinned-first. [Geodocs; callsphere 2026]
- **Episodic = append-only + time-indexed; semantic = dedupe + supersession on conflict** — contradictions surface for review, never silently overwritten. [callsphere 2026; zylos survey]
- **Evaluation is a deliverable** — LongMemEval-style: temporal correctness, distractor resistance, update handling, abstention. Hindsight is SOTA on LongMemEval (83.6%/20B, independently reproduced) — the eval burden is regression protection, not capability discovery. [LongMemEval; Hindsight paper]
- **Write-time redaction** — secrets/PII never enter any store. [Geodocs]
- **Hybrid vector+graph is the consensus backend** — Hindsight already is one; do not add a second episodic store. [zylos survey]
- **Council additions (2026-09-03):** (a) backups must have an off-container destination and failure alerting, or they are theater; (b) read-side arbitration — designate a system-of-record per fact class; (c) LLM consolidation output is provisional until a human validates it (the wiki's `explored` gate is the right mechanism); (d) active decay — banks nobody reads get archived on a schedule, not eventually.

## 3. The plan

### Phase 0 — Baseline & unblock (today)
1. **Fix the MEMORY.md lock.** Diagnose (`lsof`, stat, encoding, permissions); note the council's root-cause warning: ~20 agents + cron jobs share write paths with no arbitration — if the lock recurs, implement per-agent namespaces or a single-writer queue for base-layer writes. Acceptance: a `memory add` round-trip succeeds.
2. **Service autostart.** start_hindsight.sh / start_viking.sh / embed_server.py survive container restarts (init hook or @reboot cron). Acceptance: restart drill brings all three up green.
3. **Pin the docs.** This plan referenced from OPERATIONS.md; memory-systems skill stays the routing law.

### Phase 1 — Durability (this week)
1. **Nightly backups, one script, all stores:** pg_dump Hindsight (:5432) + Utopia (:1517), sqlite copy of character_world/world.db, tar of my-wikid + `git -C /root/vaults/my-wikid` commit (push stays Daniel's). Retention 14 daily + 4 weekly. 04:00 UTC. Idempotent, logged.
2. **Off-container destination (council-mandated).** Backups land in `/opt/data/backups/` AND a second location outside the container. Decision point for Daniel, cheapest first: (a) weekly manual pull to his laptop, (b) git-remote the wiki + restic/rclone of dumps to any object storage or home NAS, (c) accept single-host risk in writing. The plan does not close this phase until (a)/(b)/(c) is chosen.
3. **Failure alerting on the backup job itself** — cron notify on non-zero exit; a backup that silently fails for 3 weeks is worse than none. Integrity probes in-script: row counts per bank vs previous night; alert on >5% shrink.
4. **Restore drill:** restore Hindsight dump to scratch DB, `/health` it, drop scratch. Once before Phase 1 closes; monthly thereafter (Phase 5).

### Phase 2 — Retention & write law
1. **Routing table stays law** (memory-systems skill): state→ActiveGraph, episodes→Hindsight, knowledge→my-wikid, index→OpenViking, procedural→skills (versioned, human-approved).
2. **Read-side arbitration — the supreme court (council addition).** When systems disagree on a fact: **current state → ActiveGraph wins**; **what happened → Hindsight wins**; **what is true → my-wikid wins** (only pages with `explored: true` are canon); **OpenViking never authoritative** — pointers only. Any retrieved memory that contradicts the system-of-record for its class is surfaced, not used silently.
3. **What never gets retained:** raw state numbers (bridge narrates), secrets/keys, transient tool output. Redaction check at retain time.
4. **Light quarantine (counselor's point, solo-scaled):** cron-job retains are tagged `source=cron, importance=low` by default; they influence retrieval weakly until referenced by a real session or promoted by review. No 48h holding pen — the tag does the work.
5. **Agent coverage:** every cron job gets an explicit retain-outcome step (outcome + decision, not transcripts). Council runs retain a decision record.
6. **Bank hygiene + active decay:** audit 54 banks for collisions/stales; monthly, banks with zero reads in 60 days get flagged → archived via export. Registry must match hindsight_banks.py.

### Phase 3 — Consolidation cadence (RecMem-informed)
1. **Nightly (no LLM):** bank metrics → backup log.
2. **Weekly (LLM):** `POST /consolidate` on the 5–8 hottest banks only (agent-joan, agent-jobsearcher, active char- banks, agent-mizuno). Cold banks are never consolidated.
3. **Monthly (LLM):** `reflect` on agent-joan + agent-jobsearcher → digest retained back as *provisional*.
4. **Quarterly (LLM → wiki):** episodes → knowledge digest pushed to my-wikid **with `explored: false`** — Daniel's validation gate is the human-in-the-loop; LLM synthesis never becomes canon by default (counselor's gate, matches the vault's existing schema).
5. **Provenance (strategist's drift guard):** consolidated/digested entries carry source-episode IDs and dates; originals in Hindsight are never modified by synthesis; wiki digest pages link back to their banks. Original text + diff survives every promotion.
6. **Conflict resolution step:** consolidation that meets contradicting records marks both, records the resolution basis (recency/system-of-record), and lists the conflict in the run's log — never merges silently.
7. **Idempotency check:** second run on a quiescent bank must be a no-op.

### Phase 4 — Retrieval discipline (simplified per council)
1. **Scoring:** recency-ranked retrieval with pinned items surfaced first. Drop frequency weighting and fixed weight vectors — solo scale doesn't need them. Revisit only if retrieval quality measurably degrades.
2. **Tiered reads:** OpenViking abstract→overview→full; Hindsight fact-mode first, narrative-mode for scene work.
3. **Context budget:** ≤20% of context per turn for memory; summarize-out the oldest beyond that.
4. **Abstention (kept, one line):** no memory scores above threshold → say "no relevant memory." Never fabricate from vibes.

### Phase 5 — Evaluation (simplified per council)
- **Monthly spot-check (30 min):** 10 random retrievals verified + restore drill + wiki lint (llm-wiki skill: links, orphans, stale, log rotation).
- **Quarterly full eval:** round-trip (retain→recall→delete), temporal probes ("what did we believe as of Y"), contradiction probes (correction supersedes, not duplicates), decay audit, cost review of consolidation tokens.
- Report: one digest, pass/fail per check.

### Phase 6 — Optional adoptions (decide, don't drift)
1. **Honcho — SKIP, unanimous council.** Dialectic user modeling earns its cost at conversational multi-agent scale; Daniel runs task-delegating personas on one operator, and ActiveGraph + Hindsight already carry the relational context. Two revisit triggers (agreed by both seats): personas start interacting with Daniel conversationally at volume, or cross-surface persona-consistency walls appear. Re-check after Phase 5's first quarterly eval.
2. **qmd at scale:** fine at ~20 pages; re-evaluate at 300+.
3. **obsidian-headless sync** if phone/laptop Obsidian access to my-wikid is wanted.

## 4. Effort & ownership
- Phases 0–3: me, this week, ~2–3 hrs. No new dependencies (off-container destination may add rclone/restic — pending Daniel's pick).
- Phase 5: me, ~30 min setup, then cron.
- Daniel: (a) choose backup destination option a/b/c, (b) my-wikid git push creds (or approve key setup), (c) flip `explored: true` on validated wiki pages — this is now load-bearing (Phase 3.4), (d) Honcho go/no-go — my recommendation stands: skip.

## 5. Risks
- Token cost of consolidation: capped by weekly-hot-only + metrics-first.
- Provider region locks: any provider change passes the egress probe first (OpenCode deepseek-v4 lesson, 2026-09-03).
- Single-container SPOF: mitigated by Phase 1.2 the moment Daniel picks a destination; until then it is the top open risk.
- Memory poisoning via extracted episodes: low threat at solo scale; mitigations are the write-time redaction check + `source=cron` low-influence tags + human validation gate on all LLM synthesis.
- Semantic drift in consolidation: mitigated by Phase 3.5 provenance + immutable originals.
