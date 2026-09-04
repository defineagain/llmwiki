# qmd notes (updated 2026-09-04 - supersedes the setup section in qmd-notes.md)

## Current install (working)
- qmd 2.8.3 (npm install -g @tobilu/qmd@latest), bun 1.1.34 x64 at /root/.bun/bin/bun
- Index: 30 docs / 55 chunks embedded, hybrid search verified working
- Collection: llm-wiki -> /root/vaults/my-wikid/wiki ("**/*.md"), config /root/.config/qmd/index.yml

## CRITICAL gotchas learned 2026-09-04
1. The npm wrapper segfaults (rc=139) on ALL subcommands except --help. Always invoke via bun directly:
   cd /usr/local/lib/node_modules/@tobilu/qmd && bun dist/cli/qmd.js <cmd>
2. bun was ARM64 on an x64 box (silently broken sometime after Aug 16 setup). Fixed with bun-linux-x64.zip v1.1.34 from GitHub releases.
3. `qmd index` no longer exists in 2.8.3 - use `qmd update`. Old index.sqlite (0.9.0 format) kept as index.sqlite.old09.
4. CPU-only queries are slow with reranking (1.7B expansion model): 20-50s/query. Use --no-rerank for interactive speed; full rerank acceptable for batch.
5. Old qmd-notes.md wrongly credits `Tobilu/qmd` - repo does not resolve on GitHub (npm package @tobilu/qmd is real; upstream repo URL unverified). Corrected on wiki concepts/qmd.md with a contradiction callout.

## Day-to-day (2.8.3 syntax)
```bash
cd /usr/local/lib/node_modules/@tobilu/qmd
bun dist/cli/qmd.js update                    # re-index after vault changes
bun dist/cli/qmd.js embed                     # embed new chunks (~3.5 min for 55 chunks CPU)
bun dist/cli/qmd.js query "..." --no-rerank   # fast hybrid search
bun dist/cli/qmd.js query "..."               # full quality (slow on CPU)
```
