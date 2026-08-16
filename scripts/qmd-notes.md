# qmd setup for the llm-wiki vault

This vault is indexed by `qmd` (Tobilu/qmd) for hybrid search:
keyword (BM25) + vector similarity + LLM re-ranking.

## Install

```bash
# bun is required by qmd
curl -fsSL https://bun.sh/install | bash
export PATH="$HOME/.bun/bin:$PATH"

# qmd itself
npm install -g @tobilu/qmd
```

## Initial index

```bash
cd /root/vaults/my-wikid
qmd collection add wiki --name llm-wiki --mask "**/*.md"
qmd embed                         # ~5-7 min on CPU; downloads embeddinggemma 300M
```

## Day-to-day

```bash
# After editing wiki/ or raw/:
qmd update                        # re-index
qmd embed                         # re-embed (only needed for new/changed docs)

# Search:
qmd search "validation gate"      # BM25 keyword search, instant
qmd vsearch "validation gate"     # vector similarity (needs embed)
qmd query "what is the validation gate"   # BM25 + vector + LLM rerank (slow)
```

## What lives where

| Path | Purpose |
|------|---------|
| `/root/.cache/qmd/index.sqlite` | The qmd index (FTS5 + vectors) |
| `/root/.cache/qmd/models/` | Downloaded GGUF models |
| `~/.qmd` or in-repo config | (qmd has no project-level config — runs from cwd) |

## Models

- `hf_ggml-org_embeddinggemma-300M-Q8_0.gguf` (333 MB) — embeddings
- `hf_tobil_qmd-query-expansion-1.7B-q4_k_m.gguf` (1.28 GB) — query
  expansion + re-ranking

Both downloaded automatically on first use. Both run on CPU; for a
larger vault, GPU acceleration is recommended.

## Schema integration

The shannhk/llm-wikid schema's `CLAUDE.md` says:

> 300-500 pages: Add qmd — local markdown search with hybrid
> BM25/vector + LLM re-ranking. CLI and MCP server.

This vault currently has 16 wiki pages, so qmd is overkill — but
it's preinstalled so the wiki grows into it without ceremony.

## MCP server

```bash
qmd mcp --http --port 8181         # stdio MCP server (for Claude Code)
qmd mcp --http --daemon            # HTTP daemon (for any MCP client)
```

The MCP server exposes `search`, `vsearch`, `query`, `get`, `multi_get`,
and `ls` as tools.
