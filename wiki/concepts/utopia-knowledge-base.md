---
title: "Utopia"
tldr: "deeplethe/utopia — self-hosted bitemporal knowledge base (Rust+Postgres). Live here since 2026-09-03 with the Leela Protocol corpus; complements NotebookLM for private corpora."
date_created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [tool, knowledge-base, memory, self-hosted]
sources: [raw/articles/utopia-deeplethe-audit-2026-09-03.md, raw/articles/notebooklm-selfhosting-article-2026-09-03.md]
explored: true
confidence: high
---

# Utopia

Self-hosted "world model": bitemporal knowledge graph, one Rust binary + PostgreSQL, Apache-2.0. Deployed live in this container 2026-09-03. Key verified properties: cited document Q&A (answers open the exact source passage), bitemporal facts (corrections supersede, history queryable as-of any date), read-only MCP exposure for agents, hybrid Tantivy full-text + pgvector search. See [[pre-compiled-rag]] for why this beats per-query retrieval, and [[llm-wiki-pattern]] for the complementary compile-once pattern.

## Verified deployment numbers (this container, 2026-09-03)

- Leela Protocol corpus: 196/196 docs ready, 2,285 chunks all embedded
- ~0.6 GB RAM server + ~1.7 GB local embedding model (bge-small-en-v1.5 served OpenAI-shaped locally)
- Maturity: repo went public 2026-08-07; v0.1.0 withdrawn and re-cut as rc1-rc4 in 48h (rc4 = undoable deletions). Pre-1.0: pin versions, test backups.

## Counter-arguments

- No audio/video studio outputs — NotebookLM-class features it will never have; the hybrid pattern (article: cloud for studio, self-hosted for private corpus) exists precisely because of this.
- Young project, no third-party usage reports; extraction quality depends on the model endpoint configured.
- No encryption at rest (vendor-documented 1.0 item) — loopback-only in this deployment.

## Data gaps

- Long-term durability at scale unverified (no public 100k-doc benchmark yet).
- Bitemporal query classes not yet exercised in anger on the Leela corpus.
