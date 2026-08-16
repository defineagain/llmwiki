---
title: "Karpathy — LLM Wiki (Feb 2025)"
tldr: "Karpathy's originating tweet coining the 'LLM Wiki' pattern: curated, pre-compiled, AI-maintained pages as the agent's persistent memory, with a human validation gate."
date_created: 2026-08-16
date_modified: 2026-08-16
type: source
tags: [karpathy, llm-wiki, pattern, rgs]
source_type: tweet
source_file: "[[raw/articles/karpathy-2025-llm-wiki-tweet.md]]"
original_url: "https://x.com/karpathy/status/1890540708772143562"
explored: false
confidence: high
---

# Karpathy — LLM Wiki (Feb 2025)

## Summary

Andrej Karpathy published a thread on Feb 17 2025 proposing the "LLM Wiki"
as the right mental model for an LLM OS. The core idea: instead of a RAG
pipeline that chunks, embeds, and retrieves, the agent reads a curated set
of pre-compiled, structured wiki pages. The pages are the agent's persistent
memory. Every query compounds — each new entry is indexed by future queries,
not just retrieved. The wiki is *appended to*, never overwritten, and a
human flips a "validated" flag on reviewed pages.

## Key Takeaways

- **Pre-compiled > retrieved.** RAG leaks structural information and
  conflates retrieval with reasoning. A wiki separates the two: a compiler
  writes concise pages, a reader consumes them.
- **Pages, not chunks.** Pages are small enough to fully read, with clear
  wikilinks to navigate. The granularity is a concept, not a 256-token
  chunk.
- **Compounding memory.** Each query adds a new entry to the wiki. The
  system gets sharper over time without re-indexing.
- **Append-only.** The compiler appends. The user validates. The validating
  flag is the human-in-the-loop boundary.
- **Curated, not retrieved.** The agent deals with structured knowledge,
  not raw chunks. The compiler is the only thing that touches sources.

## Concepts & Entities Mentioned

- [[llm-wiki-pattern]]
- [[pre-compiled-rag]]
- [[validation-gate]]
- [[karpathy]]
- [[rag]]

## Counter-arguments

- The pattern is essentially a personalized, agent-maintained Wikipedia.
  Wikipedia works for shared human knowledge; whether it works for a
  single user's idiosyncratic knowledge base is unproven at scale.
- The validation gate assumes a human willing to review every page. The
  actual compliance rate in conversational use is unknown.
- The thread is short — it is a *mental model*, not a worked implementation.
  Most of the engineering detail is downstream invention.

## Data gaps

- The thread itself is not auto-resolved (X API requires OAuth). The
  excerpt here is a manual transcription; the exact text is locked behind
  a login wall.
- No published benchmark comparing LLM Wiki recall vs. RAG with the same
  source corpus.
