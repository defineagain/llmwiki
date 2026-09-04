---
title: "Synthesis: the operator's complete memory stack"
tldr: "How the four memory systems, the wiki, Utopia, and the validation gate compose into one working memory architecture (as of 2026-09-04)."
date_created: 2026-09-04
updated: 2026-09-04
type: summary
tags: [memory, architecture, synthesis]
sources: [raw/articles/memory-plan-hermes-2026-09-03.md, raw/articles/utopia-deeplethe-audit-2026-09-03.md, raw/articles/notebooklm-selfhosting-article-2026-09-03.md]
explored: true
confidence: high
---

# The operator's complete memory stack (2026-09-04)

Base: MEMORY.md + session search (host-side; container-side lock unresolved). Layer 1 — [[llm-wiki-pattern]] vault (this wiki): compiled, human-validated knowledge; [[validation-gate]] makes it the truth system-of-record. Layer 2 — Hindsight: episodic memory, 54 banks, SOTA recall, now with a closed operational loop (nightly backup 04:00 → nightly digest retain 04:30 → weekly hot-bank consolidation Sun 05:00 → quarterly knowledge digest back to this wiki). Layer 3 — ActiveGraph: character state, bridge mirrors to Hindsight. Layer 4 — OpenViking: tiered index/pointers. Adjacent: [[utopia-knowledge-base]] for corpus-scale cited Q&A (the novel), NotebookLM/Gemini Notebook retained cloud-side for studio outputs.

The composition rule: **episodes flow toward knowledge** (Hindsight → quarterly digest → wiki pages, human-validated) and **knowledge never flows backward silently** (wiki pages don't rewrite episodes). [[notebooklm-selfhosting-2026]] records why the boundary between public (cloud) and private (self-hosted) is now an architectural decision.

## Counter-arguments

- Complexity budget: six surfaces for one operator is defensible only because each carries a distinct functional role (CoALA); the moment two carry the same role, merge them.

## Data gaps

- The quarterly episodes→knowledge digest has never run (first due ~2026-12); its quality is unproven.
- MEMORY.md host-side lock: when fixed, the base layer needs re-wiring into this synthesis.
