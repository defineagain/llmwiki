---
title: "How to operate an LLM Wiki — synthesis across the seed sources"
tldr: "Three seed sources (Karpathy's Feb 2025 thread, the shannhk/llm-wikid README, and the shannhk/llm-wikid CLAUDE.md schema) converge on the same operational doctrine: the agent is a compiler, the reader is a reader, the human is the validator."
date_created: 2026-08-16
date_modified: 2026-08-16
type: synthesis
tags: [llm-wiki, doctrine, operating-model]
sources:
  - "[[karpathy-2025-llm-wiki-tweet]]"
  - "[[shannhk-2026-llm-wikid-readme]]"
  - "[[shannhk-2026-llm-wikid-claude-schema]]"
explored: false
confidence: medium
---

# How to operate an LLM Wiki — synthesis across the seed sources

The three seed sources are not three independent witnesses. They are
three layers of the same doctrine: the originating tweet ([Karpathy],
Feb 2025) names the pattern, the shannhk/llm-wikid README points at
the schema, and the shannhk/llm-wikid CLAUDE.md schema defines the
operational contract. Read together, they prescribe a single division
of labor: the agent is the compiler, the agent is also the reader,
and the user is the validator.

## Threads Across Sources

**1. Pre-compiled structure is the point.** Karpathy's thread names
[[pre-compiled-rag]] as the alternative to chunked retrieval. The
shannhk schema codifies it as frontmatter, wikilinks, and prose
sectioning — three concrete artifacts that RAG discards. The README
is short on this point because the schema is explicit.

**2. The compiler is the only thing that touches raw material.**
The schema's source-resolution step (yt-dlp, scrapling, X API, direct
read) is the *compiler's* job. The reader never sees raw chunks. The
[[llm-wiki-pattern]] imports the discipline of newspaper editing: the
writer deals with the source, the reader deals with the front page.

**3. The validation gate is the trust boundary.** Every source
articulates the [[validation-gate]] explicitly — Karpathy's
"validated" flag, the schema's `explored: false`, the README's
implicit "the agent does the rest, but review is yours." The gate
is what distinguishes the wiki from a confident pile of AI output.

**4. Append-only is the discipline.** All three sources agree:
pages are written, never rewritten. The schema forbids
overwriting. The lint pass exists to catch drift. The pattern
preserves context that a rewrite would destroy.

**5. The hot cache is the bridge between sessions.** The schema
specifies `wiki/hot.md` as a short-term memory layer. Karpathy
does not name it, but the compiled structure implies something
like it. The README points at the schema, where the cache is
defined. The cache is the only mechanism that survives between
agent invocations.

## Open Questions

- **How is the schema updated?** The schema is the source of truth
  for the agent, but the schema itself is shipped with the repo.
  When the schema changes, do existing wikis migrate? The seed
  sources do not address this.
- **Which agent owns the hot cache?** The shannhk schema describes
  a Claude Code Stop hook that calls `claude -p` in the background
  to regenerate the cache. Hermes does not implement this hook.
  A wiki run on Hermes needs an equivalent ritual.
- **What happens when the schema and the user's customizations
  disagree?** The skill for this vault directs the agent to follow
  the user's `CLAUDE.md` over the skill's defaults. The repo does
  not anticipate this case.

## Counter-arguments

- The three sources are not independent. The schema is downstream
  of the tweet; the README is downstream of the schema. A "synthesis"
  across artifacts that are causally sequenced is closer to a
  paraphrase than a corroboration.
- The pattern is asserted, not benchmarked. The schema confidently
  recommends file-based for 0–300 pages, qmd for 300–500, structured
  DB for 500+, but does not cite the measurements behind the
  thresholds.

## Data gaps

- The pattern's failure modes on conflicting sources are described
  in the schema but not empirically validated.
- The schema's scale plan (file → qmd → DB) is unproven at the
  upper bound.
- The validation gate's actual flip rate in conversational use is
  not published.
