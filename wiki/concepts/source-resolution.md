---
title: "Source Resolution"
tldr: "The pre-compile step in the INGEST pipeline: fetch full content from a raw URL using the right tool (yt-dlp for YouTube, scrapling for web, X API for tweets, direct read for PDFs)."
date_created: 2026-08-16
date_modified: 2026-08-16
type: concept
tags: [ingest, toolchain, schema]
sources: []
explored: false
confidence: low
---

# Source Resolution

Stub — created to satisfy a `[[wikilink]]` from the seed pages.

Source resolution is the schema's pre-compile step. Before a raw
source can be classified and turned into a wiki page, its full content
must be fetched. The schema maps URL types to tools:

- YouTube → `yt-dlp --write-auto-sub --skip-download`
- X / Twitter → X API (OAuth) or fallback to `curl` + manual excerpt
- Web / Reddit → `scrapling` (or `curl` if scrapling is unavailable)
- PDF → read directly or `summarize` (steipete/tap)

The resolved content is written in place to `raw/`, with `original_url`,
`fetched`, and `source_tool` recorded in frontmatter.

## Counter-arguments

## Data gaps

- No full page here yet — promote to a full page when a second
  source discusses source resolution.
