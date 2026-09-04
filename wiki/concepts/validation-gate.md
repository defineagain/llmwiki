---
title: "Validation Gate"
tldr: "The 'explored: true' flag on every AI-created page. The agent never sets it to true; only the human does. The discipline that prevents the wiki from becoming a pile of confident AI output."
date_created: 2026-08-16
date_modified: 2026-08-16
type: concept
tags: [human-in-the-loop, governance, schema-discipline]
sources: ["[[karpathy-2025-llm-wiki-tweet]]", "[[shannhk-2026-llm-wikid-claude-schema]]"]
explored: true
confidence: high
---

# Validation Gate

The validation gate is the [[llm-wiki-pattern]]'s human-in-the-loop
boundary, encoded as a single frontmatter field: `explored`. Every
page that the agent creates or appends to gets `explored: false`.
After reviewing a page, the user manually flips the flag to `true`.

The gate is the *only* mechanism that distinguishes "AI wrote this"
from "human signed off on this." Without it, the wiki is a pile of
confident AI output. With it, the user can browse the vault and
visually skip everything unset.

## Key Ideas

- **The agent never sets `explored: true`.** Even when the agent is
  confident the page is correct, the flag stays false. The schema
  is explicit.
- **The flag is per-page.** It is not a vault-wide "I'm feeling good"
  dial. Each page is reviewed on its own merits.
- **Confidence is separate.** The `confidence` field is the agent's
  self-assessment. `explored` is the human's. A page can be
  `confidence: high` and `explored: false` — the agent thinks it
  got it right, the human hasn't agreed.
- **The lint catches violations.** The schema's linter flags any
  page with `explored: true` that was created by the agent (vs. by
  the human creating the page in the first place).

## How It Connects

The gate is the user-facing surface of the schema. Everything else
(INGEST, QUERY, EXPLORE, LINT) is machinery. The gate is the trust
mechanism. The lint pass is the only thing that audits the gate.

## Counter-arguments

- In practice, the user may never flip the flag. If review is
  expensive, the gate becomes decorative.
- The gate is binary. There is no "partially validated" state.
- The gate assumes the user is the right reviewer. For a shared
  knowledge base, the right reviewer might be a team or a process,
  not an individual.

## Data gaps

- Actual flip rates in conversational use are not published.
- The schema does not specify the cost of the review workflow —
  how long it takes, what reviewers look for, what passes.
