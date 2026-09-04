---
title: Human Procedure — Operating the Wiki as the Human Half
created: 2026-09-04
updated: 2026-09-04
type: concept
tags: [meta, validation-gate, workflow]
sources: [sources/shannhk-2026-llm-wikid-claude-schema.md]
confidence: high
---

# Human Procedure — your half of the division of labor

The [[llm-wiki-pattern]] splits labor: the agent ingests, cross-references, files, and maintains; **the human curates sources and validates truth**. This page is the exact checklist for the human half. Related: [[validation-gate]], [[bias-check]], [[llm-wikid]].

## 1. Validate pages — the only gate that makes knowledge canon

Every AI-written page carries `explored: false`. It becomes canon only when YOU flip it to `explored: true`. That flag is load-bearing: the memory plan's read-side arbitration rule says only `explored: true` wiki pages win contradictions (system-of-record for "what is true").

Per page (2-4 min each):
1. Read it. Ask: are the claims right? Is anything missing or overstated?
2. Check it has `## Counter-arguments` and `## Data gaps` ([[bias-check]] contract) — if the agent wrote neither, reject the page back for rework.
3. If good: change `explored: false` to `explored: true` in the frontmatter. Either edit it yourself (Obsidian/any editor) or tell the agent "validated: <page names>" and it flips the flags for you.

Current queue (20 pages, all from the Aug 16 seeding): 3 sources, 9 concepts, 2 entities, index/dashboard/log/hot/synthesis/onboarding plumbing. Suggested order: the 3 sources/ first (shortest), then concepts/llm-wiki-pattern + concepts/validation-gate (the load-bearing ones), then the rest mechanically.

## 2. Feed sources — the wiki compounds only if you feed it

Nothing has been ingested since Aug 16. The wiki is a compiled knowledge base: it is only as good as what you push into it. When you find something worth keeping (article, paper, transcript, your own notes): hand the URL/file/paste to the agent with "ingest this" — the agent does source-resolution, entity extraction, cross-linking, index/log updates. You never write wiki pages by hand unless you want to.

Good current candidates: the Utopia audit (/opt/data/utopia-audit-2026-09-03.md), the memory plan (/opt/data/memory-plan-2026-09-03.md), the article-1 research base — say the word and they become pages.

## 3. Publishing — nothing to do (changed 2026-09-04)

The old "push blocked, no credentials" note in the log is stale: a deploy key is installed and verified (git push origin main -> "Everything up-to-date", authenticated as defineagain/llmwiki). The nightly backup auto-commits and pushes. You only need to look at the repo if you want to.

## 4. Optional: read it in Obsidian

The vault is an Obsidian vault out of the box (wikilinks, graph view, frontmatter). To browse on phone/laptop, say "set up obsidian-headless" — that is plan Phase 6.3, ~15 min, needs your Obsidian Sync account.

## The contract, in one line

You: validate pages, feed sources. Agent: everything else. `explored: true` is your signature that a page is canon.
