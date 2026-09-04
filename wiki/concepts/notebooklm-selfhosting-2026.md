---
title: "NotebookLM → Gemini Notebook and the self-hosting question"
tldr: "Google renamed NotebookLM (2026-07-16), added per-notebook code execution and metered limits (2026-09-02). Self-hosting the substrate for private corpora + cloud for studio outputs = the 2026 hybrid default."
date_created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [comparison, memory, self-hosted, tool]
sources: [raw/articles/notebooklm-selfhosting-article-2026-09-03.md]
explored: true
confidence: high
---

# NotebookLM → Gemini Notebook and the self-hosting question

Verified timeline: renamed Gemini Notebook 2026-07-16 (Google blog + Workspace Updates + 3 outlets); per-notebook secure code execution (Ultra first, Pro rolling); metered limits effective 2026-09-02 (free: 50 sources/notebook, 50 chats/day → top tier: 600/5k). No consumer API; no self-hostable version. Training policy: not used for training unless feedback submitted; Workspace tier never.

The decision framework (article-1 of the series, council-iterated 2 rounds): sovereignty-first tools (Open Notebook 38k★ MIT, SurfSense 16k★) vs knowledge substrates ([[utopia-knowledge-base]], Graphiti 30k★ — bitemporal, provenance-tracked) vs hybrid. Hybrid wins for substantial private corpora + studio use; pure cloud for public sources; pure self-hosted for air-gapped/agent-access needs. This vault's operator runs the hybrid: [[utopia-knowledge-base]] holds the private novel corpus; Gemini Notebook stays for public material.

## Counter-arguments

- "Most serious users need hybrid" is a decision threshold, not a law — below the threshold (public sources, low volume) the managed product is simply better and the article says so.
- The no-API wall is the most likely to move (enterprise API already exists); the corpus-boundary wall is structural.

## Data gaps

- Limits are date-stamped 2026-09; Google restructured tiers twice recently — re-verify before citing.
- Retrieval-quality benchmark vs NotebookLM grounding: none exists; comparison rests on features, not measured recall.
