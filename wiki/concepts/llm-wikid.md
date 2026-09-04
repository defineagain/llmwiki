---
title: "llm-wikid"
tldr: "The shannhk/llm-wikid repo: a Karpathy-style LLM Wiki implemented as an Obsidian vault. The schema (`CLAUDE.md`) is the contract; the agent is replaceable."
date_created: 2026-08-16
date_modified: 2026-08-16
type: concept
tags: [repo, obsidian, vault, llm-wiki]
sources: ["[[shannhk-2026-llm-wikid-readme]]", "[[shannhk-2026-llm-wikid-claude-schema]]"]
explored: true
confidence: high
---

# llm-wikid

The shannhk/llm-wikid repository: the canonical implementation of the
[[llm-wiki-pattern]] as an Obsidian vault. The repo is a *template* —
clone it, open as a vault, run an agent that reads `CLAUDE.md`. The
schema in that file is the contract; the agent (Claude Code, Hermes,
Codex, OpenClaw) is interchangeable.

## Key Ideas

- **Schema is the contract.** `CLAUDE.md` defines frontmatter, six
  operations, source-resolution toolkit, validation gate, and scale
  plan. Everything else is template.
- **Agent-agnostic.** The repo points at multiple agents by name. The
  schema is the only thing that has to be consistent.
- **Obsidian-backed.** Pages are markdown files in `wiki/`. The repo
  ships `.obsidian/` config and an Obsidian Bases dashboard.
- **Git-versioned.** Every change is a commit. The vault is the
  source of truth.

## How It Connects

- [[llm-wiki-pattern]] — the pattern this repo implements.
- [[shannhk]] — the maintainer.
- [[shannhk-2026-llm-wikid-readme]] — the README as a source.
- [[shannhk-2026-llm-wikid-claude-schema]] — the schema as a source.

## Counter-arguments

- The repo is a template, not a finished product. Its adoption
  depends on whether the agent actually follows the schema correctly.
- The schema is opinionated: pre-compiled, append-only, validated
  by humans. Implementations that disagree on any of these have
  to fork.

## Data gaps

- The repo's actual maintenance pace (last push April 2026) suggests
  it may be in maintenance mode, not active development.
