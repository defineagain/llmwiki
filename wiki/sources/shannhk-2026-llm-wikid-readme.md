---
title: "shannhk/llm-wikid — README"
tldr: "The repo's own README: a Karpathy-style LLM Wiki implemented as an Obsidian vault; the agent reads CLAUDE.md and gets the whole schema, six operations, and a validation gate."
date_created: 2026-08-16
date_modified: 2026-08-16
type: source
tags: [shannhk, llm-wikid, obsidian, vault, schema]
source_type: article
source_file: "[[raw/articles/shannhk-2026-llm-wikid-readme.md]]"
original_url: "https://github.com/shannhk/llm-wikid"
explored: false
confidence: high
---

# shannhk/llm-wikid — README

## Summary

The README from the public repository on the day it was cloned
(Aug 16 2026). The repo is described as a Karpathy-style LLM Wiki
implemented as an Obsidian vault. The README is short — it is a pointer
to `CLAUDE.md`, which the maintainer calls out as "the schema that
controls the entire system." Everything substantive lives in that file.

## Key Takeaways

- **Clone-and-go.** `git clone` → open as Obsidian vault → start an agent
  that reads `CLAUDE.md`. The agent does the rest.
- **Agent-agnostic.** The README explicitly names Claude Code, OpenClaw,
  Hermes, and Codex as compatible agents. The schema is the contract;
  the agent is replaceable.
- **Compound design.** Raw sources go in; structured pages come out;
  every query files an answer back. The wiki builds up over time.
- **One source of truth.** `CLAUDE.md` is the only schema file. The
  README defers to it.

## Concepts & Entities Mentioned

- [[llm-wiki-pattern]]
- [[karpathy]]
- [[shannhk]]
- [[validation-gate]]
- [[obsidian]]

## Counter-arguments

- The README is largely a pointer to `CLAUDE.md`. Treating it as a source
  separate from the schema is a deliberate choice for the wiki (the schema
  is treated as a *describing* doc, not a primary source), but a reader
  should not overweight the README over the actual operational file.
- The repo is a template, not a finished tool. The README's "works with
  any agent" framing assumes the agent actually reads and follows the
  schema — Hermes does, but not every caller does.

## Data gaps

- This is an in-repo snapshot, not a published article. The repo could
  change structure between reads; the wiki's snapshot is dated.
