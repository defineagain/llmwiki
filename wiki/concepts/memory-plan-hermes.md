---
title: "Hermes four-system memory topology"
tldr: "The operator's memory architecture: state→ActiveGraph, episodes→Hindsight, knowledge→my-wikid, index→OpenViking; read-side arbitration makes my-wikid (explored:true only) the system-of-record for truth."
date_created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [memory, architecture, agent]
sources: [raw/articles/memory-plan-hermes-2026-09-03.md]
explored: true
confidence: high
---

# Hermes four-system memory topology

Four stores, one rule each (see [[llm-wiki-pattern]] for the knowledge layer's design): **state → ActiveGraph** (who/where/what-intensity now), **episodes → Hindsight** (what happened and what it meant; SOTA LongMemEval recall, MiniMax-M3 extraction), **knowledge → [[obsidian]]-vault my-wikid** (compiled, validated canon — this vault), **index → OpenViking** (tiered pointers, never authoritative). Procedural memory lives in versioned skills. The base layer (MEMORY.md/session search) sits underneath all four.

Read-side arbitration (the "supreme court"): when stores disagree, current state wins from ActiveGraph, what-happened wins from Hindsight, what-is-true wins from my-wikid **only for pages with explored: true** — the [[validation-gate]] is load-bearing architecture, not ceremony.

Operational loop (live since 2026-09-04): nightly backup+restore-drill → nightly episodic digest retained into Hindsight → weekly consolidation on hot banks only (RecMem-informed token guard) → quarterly episodes→knowledge digest for human validation.

## Counter-arguments

- Four systems is real operational overhead for one operator; the council judged the separation worth it (conflating tiers is the root cause of "my agent forgot"), but a skeptic would start with two.
- Composite retrieval scoring was simplified to recency+pinned for solo scale — the 4-weight formula may need to come back if retrieval quality degrades measurably.

## Data gaps

- Off-container backup destination still pending (option a: weekly manual pull).
- MEMORY.md base-layer lock is host-side and unresolved from the container.
