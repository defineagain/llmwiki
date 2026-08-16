---
title: "Pre-compiled RAG"
tldr: "An alternative to retrieval-augmented generation where structural information is baked into pages at write time, instead of being recovered from chunk embeddings at query time."
date_created: 2026-08-16
date_modified: 2026-08-16
type: concept
tags: [rag, architecture, knowledge-base]
sources: ["[[karpathy-2025-llm-wiki-tweet]]", "[[shannhk-2026-llm-wikid-claude-schema]]"]
explored: false
confidence: medium
---

# Pre-compiled RAG

Pre-compiled RAG is the architecture proposed by the
[[llm-wiki-pattern]]: instead of chunking documents, embedding them,
and retrieving by similarity (the standard RAG approach), the agent
maintains a curated knowledge base where each **page** is a
self-contained, structured summary. The structure is computed at
write time by the compiler; the reader does not need to recover
it from embeddings at query time.

The advantages claimed in the schema:

- **No chunking loss.** Boundaries between chunks are arbitrary and
  can split a single idea across two tokens. Pages are written at
  the granularity of an idea.
- **Wikilinks survive.** Structural cross-references (Obsidian-style
  wikilinks) are preserved through the write step. RAG discards them.
- **Frontmatter survives.** Each page carries metadata (`type`,
  `confidence`, `sources`) that retrieval cannot afford to track.
- **The reader is cheaper.** The reader does not need an embedding
  model, a vector store, or a similarity search. It just loads files.

## How It Connects

Standard RAG is a *retrieval* primitive. Pre-compiled RAG is a
*maintenance* primitive. The schema is explicit that the two are
not mutually exclusive — at the 300–500 page scale, the schema
recommends adding `qmd` (hybrid BM25 + vector + LLM re-rank) on
top of the wiki. The wiki is the scaffold; the retrieval is an
acceleration layer.

## Counter-arguments

- The "pre-compiled" framing is optimistic. The compiler is itself
  an LLM and produces errors. The guarantee is "structured output,"
  not "correct output."
- Pre-compiled RAG shifts cost from query time to write time. For
  a knowledge base that grows by 1 page per day, write-time cost
  is fine. For a knowledge base that should mirror the open web in
  real time, write-time cost is wrong.
- The pattern conflates *structure* with *truth*. A perfectly
  structured wiki can still be wrong about everything.

## Data gaps

- Maintenance cost at scale (1k, 10k pages) is not characterized.
- Mixed strategies (wiki for structured knowledge, RAG over the
  raw inbox) are not enumerated in the schema.
