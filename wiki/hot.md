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
- Seeded the vault with three sources (Karpathy 2025 tweet, repo README,
  repo CLAUDE.md), three concepts (LLM Wiki pattern, Pre-compiled RAG,
  Validation Gate), two entities (Karpathy, shannhk), and one synthesis.
- All AI-created pages set `explored: false` per the validation gate.
- Seeded on topic = the LLM Wiki pattern itself, so the wiki is
  self-documenting from session 1.

## Recent decisions

- Use `manual-excerpt` for X/Twitter URLs lacking OAuth credentials.
- Use `curl` for raw GitHub endpoints (works without a search backend).
- Keep the Karpathy entity as a stub (single source) per the schema's
  page-creation threshold.

## Open threads

- Need a Hermes-side equivalent of the upstream Stop hook that
  regenerates `wiki/hot.md` via `claude -p`.
- The schema's `> [!contradiction]` callouts are unused so far —
  will surface once sources start disagreeing.
- No media extraction yet — `raw/assets/images/` is empty.
