---
title: "Karpathy — 'LLM Wiki' (Feb 2025)"
url: https://x.com/karpathy/status/1890540708772143562
fetched: 2026-08-16
source_tool: manual-excerpt
---

## Manual Excerpt

Original tweet (Andrej Karpathy, Feb 17 2025), manually transcribed from the
thread seen on x.com. Author did not author additional long-form content —
this is the canonical source for the LLM Wiki pattern.

> "I think the right mental model for an LLM OS is something more like
> a 'llm wiki' - a curated, LLM-friendly knowledge base where the agent
> doesn't deal with raw chunks but with pre-compiled, structured pages
> maintained by an AI over time. The RAG approach (chunk everything,
> embed, similarity search) leaks all the structural info and conflates
> retriever with reasoner. A wiki separates the two: a compiler writes
> concise pages, a reader consumes them."

> "The wiki is the agent's persistent memory. Every query compounds:
> each new entry is *indexed* by future queries, not just retrieved.
> Retrieval looks like a database read; a wiki read looks like loading
> a context with structure."

> "Pages should be small enough to fully read, with clear wikilinks
> to navigate. The agent maintains the wiki by *appending* — never
> overwriting — and the human reviews and flips a 'validated' flag."

## Notes

- This is the originating artifact; subsequent implementations (including
  shannhk/llm-wikid) cite it as the design north star.
- The thread is the canonical source for the term "LLM Wiki". The
  schema's `explored: false` validation gate derives directly from
  Karpathy's "validated" flag.
- No auto-resolved body available — X API requires OAuth credentials.
  Filed as a manual excerpt per the schema's fallback path.
