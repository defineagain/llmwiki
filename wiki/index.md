---
title: "Wiki Index"
tldr: "Master catalog of all wiki pages with TLDRs for fast scanning"
date_created: 2026-08-16
date_modified: 2026-08-16
explored: false
confidence: medium
---

# Wiki Index

_Scan TLDRs to find relevant pages. Load full pages only when needed._

## Sources

- [[karpathy-2025-llm-wiki-tweet]] — Originating tweet coining the LLM Wiki pattern (Feb 2025).
- [[shannhk-2026-llm-wikid-readme]] — Repo README: clone-and-go, agent-agnostic, deferred to CLAUDE.md.
- [[shannhk-2026-llm-wikid-claude-schema]] — The actual operational schema: frontmatter, six operations, validation gate.

## Concepts

- [[llm-wiki-pattern]] — Curated, pre-compiled, AI-maintained knowledge base as the agent's memory. Originated by Karpathy, implemented by shannhk.
- [[llm-wikid]] — The shannhk/llm-wikid repo: the canonical implementation as an Obsidian vault.
- [[pre-compiled-rag]] — A RAG alternative where structure is baked into pages at write time, not recovered at query time.
- [[rag]] — Retrieval-augmented generation. The default LLM pattern the LLM Wiki positions itself against.
- [[validation-gate]] — The `explored: false` flag on every AI page. The agent never sets it true; only the human does.
- [[bias-check]] — Every wiki page must include `## Counter-arguments` and `## Data gaps`; inline `> [!contradiction]` callouts.
- [[source-resolution]] — The pre-compile step: fetch full content from a raw URL using the right tool before classifying.
- [[obsidian]] — Markdown-based personal knowledge base. The vault format for shannhk/llm-wikid.
- [[qmd]] — Tobilu/qmd hybrid BM25 + vector + LLM re-rank search. Schema recommends at 300–500 pages.

## Entities

- [[karpathy]] — AI researcher; originated the LLM Wiki pattern.
- [[shannhk]] — Maintainer of the shannhk/llm-wikid repo.

## Syntheses

- [[llm-wikid-seed-synthesis]] — How the three seed sources (Karpathy, README, CLAUDE.md) prescribe a single operating doctrine.

## SOPs

- [[AGENT-ONBOARDING]] — Paste-ready setup for paperclip/holycode: clone, install qmd, index, expose MCP, wire schema into every agent.

## Outputs

_No outputs yet. Run `/wiki-query` to ask a question._

## Projects

_No projects yet._
