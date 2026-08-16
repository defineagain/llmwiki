---
title: "Hot Cache"
tldr: "Rolling summary of recent Claude sessions. Read at SessionStart, rewritten at Stop. Not a replacement for log.md - this is short-term memory."
date_created: 2026-04-21
date_modified: 2026-08-16
type: synthesis
tags: [meta, session-memory]
explored: false
confidence: medium
---

# Hot Cache

## Last session (2026-08-16)

- Cloned shannhk/llm-wikid to `~/vaults/my-wikid`.
- Seeded: 3 sources (Karpathy tweet, repo README, repo CLAUDE.md),
  9 concepts (LLM Wiki pattern, llm-wikid, pre-compiled RAG, RAG,
  validation gate, bias check, source resolution, obsidian, qmd),
  2 entities (Karpathy stub, shannhk), 1 synthesis.
- All AI-created pages set `explored: false` per the validation gate.
- Installed qmd 0.9.0 + bun; embedded 23 chunks; BM25 search verified.
- Set `origin` to user's GitHub repo. **Push blocked**: no GitHub
  creds in this sandbox. User must run the push command below.

## Recent decisions

- Use `manual-excerpt` for X/Twitter URLs lacking OAuth credentials.
- Use `curl` for raw GitHub endpoints (works without a search backend).
- Keep the Karpathy entity as a stub (single source) per the schema's
  page-creation threshold.
- qmd `query` is slow on CPU (~3-5 min cold startup for the 1.7B
  reranker). BM25 search (`qmd search`) is instant. Use BM25 by
  default; only use `query` when reranking matters.

## Open threads

- **Push to GitHub**: user needs to run the push command listed in
  the session reply.
- Need a Hermes-side equivalent of the upstream Stop hook that
  regenerates `wiki/hot.md` via `claude -p`.
- The schema's `> [!contradiction]` callouts are unused so far —
  will surface once sources start disagreeing.
- No media extraction yet — `raw/assets/images/` is empty.
