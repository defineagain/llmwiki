---
title: "LLM Wiki Pattern"
tldr: "Curated, pre-compiled, AI-maintained knowledge base as the agent's persistent memory. Originated by Karpathy (Feb 2025), implemented as Obsidian vaults by shannhk/llm-wikid and others."
date_created: 2026-08-16
date_modified: 2026-08-16
type: concept
tags: [product-pattern, agent-architecture, knowledge-management]
sources: ["[[karpathy-2025-llm-wiki-tweet]]", "[[shannhk-2026-llm-wikid-readme]]", "[[shannhk-2026-llm-wikid-claude-schema]]"]
explored: true
confidence: high
---

# LLM Wiki Pattern

The LLM Wiki is a knowledge-base architecture where an AI agent maintains
a curated set of structured, cross-referenced pages — and reads them
back as its primary memory — instead of relying on chunked retrieval
over raw sources. The agent is the maintainer; the user is the curator
who validates. Each query compounds the system by filing its answer as
a new page.

The pattern is the opposite of [[rag]]: it pre-compiles structural
information into pages rather than embedding raw chunks and hoping
similarity search recovers structure. The compiler is the only thing
that touches raw material; the reader consumes finished pages.

## Key Ideas

- **Compiler / reader split.** The agent that writes pages is different
  from the agent that reads them — different prompts, different scope.
- **Pre-compiled structure.** Wikilinks, frontmatter, and prose headings
  carry the structure that RAG discards.
- **Append-only.** Pages are written once and extended. The schema
  explicitly forbids rewriting.
- **Human validation.** A flagged table (`explored`) marks which pages
  a human has reviewed. The agent never sets the flag.
- **Compound queries.** Every question is filed as a new page. The
  wiki grows sharper with use.

## How It Connects

Karpathy's thread is the origin. The shannhk/llm-wikid repo is the
canonical implementation. Related patterns: vector-store second brains
(Notion AI, Mem), agent-loop memory (MemGPT, Letta), and personal
RAG setups (Obsidian + QMD). The pattern differs from each of those
by being pre-compiled rather than retrieved.

## Counter-arguments

- The maintenance cost is non-trivial. A wiki that stops being tended
  goes stale; a RAG pipeline that hasn't been re-indexed can still
  semi-work.
- The pattern assumes the agent has its own write access to the
  knowledge base. Many deployment contexts (multi-user, shared source-
  of-truth) make this hard.
- The compound design only works if the writer is consistent. A
  messy writer produces a messy wiki; structure is not free.

## Data gaps

- No published benchmark comparing LLM Wiki recall vs. RAG at the
  same scale with the same source corpus.
- The pattern's failure modes on conflicting sources are described
  in the schema but not empirically validated.
