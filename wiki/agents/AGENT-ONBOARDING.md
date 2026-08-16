---
title: "Paperclip / Holycode Agent Setup Guide"
tldr: "Paste-ready onboarding for the holycode container: clone the vault, install qmd, index the wiki, expose qmd via MCP, wire the schema into every agent's system prompt, and sync to GitHub."
date_created: 2026-08-16
date_modified: 2026-08-16
type: sop
tags: [agent-onboarding, holycode, paperclip, qmd, mcp]
sources: ["[[shannhk-2026-llm-wikid-claude-schema]]"]
explored: false
confidence: medium
---

# Paperclip / Holycode Agent Setup Guide

How to wire the `~/vaults/my-wikid` vault + qmd search into every agent
running in the `coderluii/holycode:latest` container (ID `4426fd822233`),
so any agent can read and write the wiki, and search it during normal
operation.

## What paperclip needs to do

1. Clone the vault into holycode at `/root/vaults/my-wikid`.
2. Install `bun` + `qmd` in holycode.
3. Index the vault with qmd.
4. Expose qmd tools to every agent (Claude Code, Hermes, Codex, etc).
5. Tell every agent that the wiki is its persistent memory.

## 1. Clone the vault

```bash
# Inside the holycode container
mkdir -p /root/vaults
cd /root/vaults
git clone https://github.com/defineagain/llmwiki.git my-wikid
cd my-wikid

# Configure commit identity (so any agent can commit cleanly)
git config user.email "agent@defineagain.local"
git config user.name "agent"
```

The vault already has 16 wiki pages, 3 sources, 2 entities, 1 synthesis,
all on `main`. Git log: `fb9d68d` setup, `f1a4c8c` seed.

## 2. Install bun + qmd

```bash
# bun (qmd runtime)
curl -fsSL https://bun.sh/install | bash
export PATH="$HOME/.bun/bin:$PATH"
echo 'export PATH="$HOME/.bun/bin:$PATH"' >> ~/.bashrc

# qmd (Tobilu/qmd) — the search engine
npm install -g @tobilu/qmd

# Verify
qmd --version   # expect 0.9.0
```

## 3. Index the vault

```bash
cd /root/vaults/my-wikid

# Create the qmd collection (BM25 + vector + LLM rerank ready)
qmd collection add wiki --name llm-wiki --mask "**/*.md"

# Pre-compute embeddings (one-time, ~5-7 min on CPU)
qmd embed
```

After this, `qmd status` should show:

```
Documents
  Total:    20 files indexed
  Vectors:  23 embedded
```

## 4. Expose qmd tools to every agent

### Option A — Start the qmd MCP server (recommended)

qmd exposes a Model Context Protocol server. Run it as a daemon and point
every agent at it:

```bash
# HTTP daemon (works for any MCP client)
qmd mcp --http --port 8181 --daemon

# Smoke test
curl http://localhost:8181/health
```

Then point each agent's MCP config at it. For Claude Code, add to
`~/.claude/mcp_servers.json`:

```json
{
  "mcpServers": {
    "qmd": {
      "url": "http://localhost:8181/mcp"
    }
  }
}
```

For Hermes, add to `~/.hermes/config.yaml`:

```yaml
mcp:
  servers:
    - name: qmd
      url: http://localhost:8181/mcp
```

After this, every agent has six new tools:

- `qmd_search` — BM25 keyword search
- `qmd_vsearch` — vector similarity (needs embed)
- `qmd_query` — hybrid BM25 + vector + LLM rerank
- `qmd_get` — fetch a single doc by URI
- `qmd_multi_get` — fetch multiple docs by glob
- `qmd_ls` — list the wiki

### Option B — Direct CLI invocation

If MCP isn't easy in the agent, add qmd to the agent's shell PATH
(`export PATH="$HOME/.bun/bin:$PATH"` in `.bashrc`) and document the
commands in the agent's system prompt. Every agent can run:

```bash
qmd search "validation gate"
qmd query "what is the validation gate"
```

## 5. Tell every agent that the wiki is its memory

This is the most important step. Add this to the system prompt of every
agent (or agent role) that runs in holycode:

```
You have a persistent knowledge base at /root/vaults/my-wikid.

It is your memory. Before answering any question that asks for prior
context, decisions, or facts, search it first:

  qmd search "<query>"            # instant BM25
  qmd query "<question>"          # hybrid with LLM rerank

The schema that controls how to maintain it lives in
/root/vaults/my-wikid/CLAUDE.md. Read it on every session start.

Skills available: hermes-agent-skill-authoring, plan, simplify-code,
test-driven-development, systematic-debugging, plan, llm-wikid-vault,
llm-wiki, obsidian. The "llm-wikid-vault" skill is the one that drives
the six operations (INGEST, QUERY, EXPLORE, LINT, COMPILE, save).

When you finish a task that produced new knowledge, append it to the
wiki (don't rewrite). When you file a query, save the answer as
`wiki/outputs/<slug>.md` with `type: output`. The wiki compounds.
```

For Hermes specifically, this works as a profile-level system prompt
patch. For Claude Code, drop it into `~/.claude/CLAUDE.md` or the
project-level `CLAUDE.md`. For Codex, into the prompt config.

## 6. Maintenance cron

qmd must be re-indexed after any wiki/ or raw/ change. Recommended:

```bash
# /etc/cron.d/qmd-reindex (root, every 5 min)
*/5 * * * * root cd /root/vaults/my-wikid && qmd update && qmd embed 2>&1 | logger -t qmd-reindex
```

Or wire it into a git post-commit hook:

```bash
# /root/vaults/my-wikid/.git/hooks/post-commit
#!/bin/bash
cd /root/vaults/my-wikid
qmd update >> /var/log/qmd-update.log 2>&1
```

## 7. Daily ritual — read hot cache

The schema's `wiki/hot.md` is the short-term memory. Every agent
should read it at session start. Best done via a SessionStart hook:

```bash
# /root/vaults/my-wikid/.context-snapshot.sh
echo "## Hot cache"
cat /root/vaults/my-wikid/wiki/hot.md
echo "## Recent sources"
ls -lt /root/vaults/my-wikid/wiki/sources/ | head -5
```

Pipe this into every agent's first message. Or trigger it from
paperclip's agent-spinup flow.

## 8. Git sync

The vault is meant to be pushed to GitHub. holycode needs push access:

```bash
# Option 1 — SSH key (most secure)
ssh-keygen -t ed25519 -C "holycode@defineagain"
cat ~/.ssh/id_ed25519.pub
# paste into https://github.com/settings/keys
git remote set-url origin git@github.com:defineagain/llmwiki.git

# Option 2 — Personal access token (less secure, simpler)
git remote set-url origin https://<TOKEN>@github.com/defineagain/llmwiki.git
```

After that, every agent can:

```bash
git -C /root/vaults/my-wikid add -A
git -C /root/vaults/my-wikid commit -m "<operation>: <summary>"
git -C /root/vaults/my-wikid push
```

The schema's `scripts/update-hot-cache.sh` (in the shannhk repo) is a
working example of doing this from a hook.

## 9. Health checks

```bash
# Is qmd running?
curl -fsS http://localhost:8181/health

# Is the index fresh?
qmd status | grep "Updated"

# Is the wiki lint-clean?
python3 /root/vaults/my-wikid/scripts/lint.py /root/vaults/my-wikid
```

## 10. Putting it together — one-shot

For a fresh holycode container, this is the complete onboarding:

```bash
# Inside the container
set -e

# 1. Vault
mkdir -p /root/vaults && cd /root/vaults
git clone https://github.com/defineagain/llmwiki.git my-wikid
cd my-wikid
git config user.email "agent@defineagain.local"
git config user.name "agent"

# 2. Bun + qmd
curl -fsSL https://bun.sh/install | bash
export PATH="$HOME/.bun/bin:$PATH"
echo 'export PATH="$HOME/.bun/bin:$PATH"' >> ~/.bashrc
npm install -g @tobilu/qmd

# 3. Index
qmd collection add wiki --name llm-wiki --mask "**/*.md"
qmd embed

# 4. MCP daemon
qmd mcp --http --port 8181 --daemon

# 5. Wait for MCP
for i in {1..30}; do
  curl -fsS http://localhost:8181/health && break
  sleep 1
done

# 6. Git sync
ssh-keygen -t ed25519 -C "holycode@defineagain" -N '' -f ~/.ssh/id_ed25519
echo "Add this key to https://github.com/settings/keys:"
cat ~/.ssh/id_ed25519.pub
git remote set-url origin git@github.com:defineagain/llmwiki.git
git push -u origin main

# 7. Lint
python3 scripts/lint.py .

# 8. Status
qmd status
echo "Onboarding complete."
```

Then any agent in holycode can:
- Search the wiki (`qmd search` / `qmd query`)
- Read the schema (`/root/vaults/my-wikid/CLAUDE.md`)
- Maintain the wiki (six operations from the schema)
- Get the hot cache (`wiki/hot.md`)
- Push changes upstream

## What "memory" means in this setup

Each agent is a **reader**. The vault is the **memory**. The agent
that wrote the wiki searched sources, structured pages, and biased
against echo. The agent that reads it now loads TLDRs from `wiki/index.md`
first, expands pages as needed, and **appends** new info — never
overwrites. The human (you) flips `explored: false` to `true` after
review. The validation gate is the trust boundary.

This is the LLM Wiki pattern. It is *not* RAG. The agent reads
pre-compiled pages, not chunks. The system compounds because every
query files back as a new page.

---

## Reference: the seeds already in the vault

- [[karpathy-2025-llm-wiki-tweet]] — origin of the pattern
- [[shannhk-2026-llm-wikid-readme]] — repo README
- [[shannhk-2026-llm-wikid-claude-schema]] — the schema
- [[llm-wiki-pattern]] — synthesis of the three
- [[pre-compiled-rag]], [[validation-gate]] — core concepts
- 6 other concepts, 2 entities, 1 synthesis

Reading the wiki first is what makes the agents' answers grounded
in the system's own operating doctrine.

## Counter-arguments

- **The schema is opinionated.** [[pre-compiled-rag]] is one architecture
  among many. A paperclip that reads only this wiki will produce
  answers that match the wiki's biases. The [[validation-gate]] is
  the only thing that surfaces this — and only when the human
  actually flips it.
- **MCP is a coupling point.** The qmd MCP server is a thin layer over
  SQLite + a 1.7B model. If paperclip spawns many agents in parallel,
  all hitting the same `qmd mcp` daemon, the daemon becomes a
  bottleneck. Plan for per-agent namespaces or per-agent collections.
- **Hot cache drift.** `wiki/hot.md` is regenerated by a hook that
  needs to be set up per agent. If some agents don't write it, the
  hot cache will diverge from the actual operation history.
- **The schema does not specify how paperclip handles multi-agent
  merges.** If two agents both write to the same page, who wins?
  Out of scope for this guide; a real production setup needs
  optimistic concurrency or a CRDT.

## Data gaps

- The holycode container's `coderluii/holycode:latest` image is not
  documented here. The setup assumes a Linux x86_64 base with
  `curl`, `git`, `npm`, and bash. If the image is Alpine, `npm` may
  need `apk add` first.
- No benchmark for "does this actually compound?" The seed proves
  the plumbing works; it does not prove the loop improves answers.
- The MCP server's authentication is not configured. Anyone on the
  docker bridge can read `qmd` results. For a public-facing setup,
  wrap the daemon behind paperclip's auth gateway.
