---
title: "shannhk/llm-wikid — CLAUDE.md schema"
tldr: "The actual operational schema: frontmatter contract, six operations (INGEST, QUERY, EXPLORE, LINT, COMPILE, save), source-resolution toolkit, validation gate, and scale plan."
date_created: 2026-08-16
date_modified: 2026-08-16
type: source
tags: [shannhk, llm-wikid, schema, claude-md, contract]
source_type: article
source_file: "[[raw/articles/shannhk-2026-llm-wikid-claude-schema.md]]"
original_url: "https://raw.githubusercontent.com/shannhk/llm-wikid/main/CLAUDE.md"
explored: true
confidence: high
---

# shannhk/llm-wikid — CLAUDE.md schema

## Summary

The full text of `CLAUDE.md` at the vault root, captured the same day
the repo was cloned. This is the *actual* operational specification —
the file the agent reads to know what to do. Compiled to wiki for
diffability and reference.

## Key Takeaways

- **Frontmatter contract.** Every page has `title`, `tldr`, `date_created`,
  `date_modified`, `type`, `tags`, `sources`, `explored`, `confidence`.
- **Six operations.** INGEST, QUERY, EXPLORE, LINT, COMPILE, plus the
  slash-command-style `save` that files a conversation as a page.
- **Page-creation threshold.** 2+ sources → full page; 1 source → stub.
  Never leave a `[[wikilink]]` pointing to nothing.
- **Source resolution.** Tools per URL type: `yt-dlp` for YouTube,
  scrapling or X API for web/tweets, read directly for PDFs.
- **Validation gate.** `explored: false` on every AI page. The human flips
  it after review. The agent never sets it true.
- **Bias check.** Every concept/synthesis/source page must include
  `## Counter-arguments` and `## Data gaps`. Inline contradictions use
  `> [!contradiction]` callouts.
- **Scale plan.** 0–300 pages = file-based, index.md TLDR scan. 300–500
  = add `qmd` for hybrid search. 500+ = consider a structured DB.

## Concepts & Entities Mentioned

- [[llm-wiki-pattern]]
- [[pre-compiled-rag]]
- [[validation-gate]]
- [[source-resolution]]
- [[bias-check]]
- [[shannhk]]
- [[qmd]] (shorthand: qmd)

## Counter-arguments

- The schema is long and detailed. An agent that misreads or cherry-picks
  sections will produce a broken wiki. The README's claim that "the agent
  reads `CLAUDE.md` and knows everything" only works if the agent actually
  reads it.
- The scale plan (file-based → qmd → structured DB) is unproven at the
  upper bound. The schema does not ship with benchmarks.
- Media extraction (images, video transcripts) is treated as a first-class
  responsibility but the resolution tooling (`scrapling`, X API) is fragile
  on gated sources.

## Data gaps

- The schema does not specify how to handle conflicting facts between two
  sources beyond the `> [!contradiction]` callout. Resolution policy is
  implicit ("prefer recency").
- The hot cache (`wiki/hot.md`) is described as auto-managed by a Stop
  hook calling `claude -p` in the background — that hook is set up for
  Claude Code users, not for every agent named in the README.
