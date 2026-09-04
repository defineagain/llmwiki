---
source_url: local://opt/data (internal working document)
ingested: 2026-09-04
sha256: 37adfe5187ca5462dd470f1d0e2d07fd8093b3f4a0b2538afac2589047c55dc3
---

# Google Just Renamed NotebookLM. Where Your Private Corpus Should Live Is Now a Real Decision.

*Published September 3, 2026 · Limits and prices verified as of this date; volatile claims are date-stamped because Google moves monthly.*

**Verdict up front:** you cannot self-host Google's NotebookLM — renamed **Gemini Notebook** on July 16, 2026 [1][4][5] — but for text-heavy work on private material, you can replace most of what it does with infrastructure you own. For researchers, writers, and consultants who query their own corpus weekly and hold unpublished or client material, the rational setup in late 2026 is a hybrid: cloud for public sources and the studio outputs only Google provides, your own hardware for everything that must stay yours.

**TL;DR:** NotebookLM is now Gemini Notebook (July 16, 2026), with per-notebook code execution and metered limits (Sept 2, 2026). You can't self-host it. For private corpora, run a self-hosted equivalent — an open-source notebook tool or a provenance-tracking knowledge substrate — and keep the cloud for public work and audio/video outputs.

## What changed, exactly

On July 16, 2026, Google renamed NotebookLM to **Gemini Notebook** [1][4]. The product is unchanged at its core — upload sources, ask questions, get answers with inline citations — but the update bundled three structural shifts:

- **A per-notebook code computer.** Each notebook gets a secure container that writes and executes Python against your sources. Shipped first to AI Ultra and Workspace business tiers, expanding to Pro [1][5][8].
- **Metered usage.** Effective September 2, 2026, nearly every action sits on a counter: 50 sources/notebook and 50 chats/day free, scaling to 600 sources and 5,000 chats/day at the top tier [2].
- **Ecosystem folding.** Notebooks sync with the Gemini app and are announced for Search's AI Mode [1][4][5].

Google reports 30 million users and 600,000 organizations [1][5]. This is the center of the consumer research stack — which is why the self-hosting question got sharper, not weaker.

**Key terms, since the rest of this article depends on them:**

- **Sovereignty-first tools** — open-source notebook alternatives you host yourself and point at any model provider (Open Notebook, SurfSense).
- **Knowledge substrate** — a database layer that stores facts with provenance and validity windows, queryable by scripts and agents, not just chat (Utopia, Graphiti).
- **Bitemporal** — every fact carries two timestamps: when it was true in the world, and when the system learned it. Corrections supersede instead of overwrite.

## The honest case for the cloud version

Grounded chat with passage-level citations remains the best zero-setup document Q&A available, now running on Gemini 3.5 [5][7]. The code execution is a genuine new capability class, not a demo [1][5]. Audio Overviews, Video Overviews (including a cinematic tier), flashcards, mind maps, and slide decks make it a complete studio [2][7]. The free tier is real, and the $4.99 Plus tier removes most everyday walls [2][7]. And the strongest cloud argument isn't privacy policy — it's velocity: cinematic video overviews and per-notebook code execution are capabilities no self-hosted stack matches at any price today [2][5]. For public research, it is the rational default.

## Three walls — and one of them is moving

**Wall one: the corpus boundary.** Everything you upload lives and is processed on Google's infrastructure. For public material this costs nothing. For unpublished manuscripts, client work, licensed corpora, or anything under NDA, neither the computation nor the copy is yours. Google's own pages state your data "is not used to train Gemini Notebook unless you provide feedback," and Workspace-tier uploads are never human-reviewed or used for training even with feedback [16]. Take that at face value. The boundary issue survives it: the corpus still sits on someone else's infrastructure, under someone else's terms and uptime. That is a decision about your material, not an accusation about Google's.

**Wall two: the meter.** Chats, overviews, deep-research runs, even flashcards now sit on counters [2]. Fifty chats a day is plenty for a student and tight for a working researcher on deadline. Meters are a moving target — Google restructured the tiers twice in recent months [2][7] — so every specific limit in this article is stamped "as of early September 2026."

**Wall three: no agent surface — for now.** There is no consumer API; programmatic access exists only in the enterprise product [7]. Your corpus is an island reachable only through the app, so your own scripts and AI agents can't read it first-class. Google ships fast and the enterprise API already exposes notebook management [7], so treat this wall as the one most likely to move. The other two are structural.

## What "self-hosting it" actually looks like

| | Sovereignty-first tools | Knowledge substrate | Gemini Notebook (cloud) |
|---|---|---|---|
| Example | Open Notebook, SurfSense | Utopia, Graphiti | Gemini Notebook |
| Software cost | $0 (open source) | $0 (open source) | Free tier / $4.99–$200/mo [2] |
| Model quality | Whatever endpoint you attach | Whatever endpoint you attach | Gemini 3.5 [5][7] |
| Studio outputs (audio/video/flashcards) | Partial (podcasts via your TTS) | None | Best-in-class [2][7] |
| Agent/API access | Full REST API [3] | MCP + API [12][14] | Enterprise only [7] |
| Provenance & history | Basic citations | Per-fact provenance, validity windows [12][13][14] | Passage citations only |
| Setup | Afternoon | Afternoon | Zero |
| Ongoing work | You are the operator | You are the operator | None |
| Corpus boundary | Your hardware | Your hardware | Google cloud |

**Sovereignty-first tools** are the closest in feel: Open Notebook (MIT, 38,000+ GitHub stars) runs multi-provider models including fully local via Ollama, multi-speaker podcast generation, and a full REST API [3][9][11]; SurfSense (16,000+ stars) adds connectors to Slack, Notion, GitHub, and search engines [10]. You give up Gemini-grade synthesis for model choice and data ownership, and podcast quality depends on whichever TTS you configure.

**Knowledge substrates** are the different category. Bitemporal systems like Utopia (single Rust binary + PostgreSQL, Apache-2.0), Graphiti (Apache-2.0, 30,000+ stars), and RAGBrain store *facts with validity windows and per-fact provenance* rather than chunks with embeddings [12][13][14]. Three query classes no notebook tool expresses:

- *"What did this document say before it was edited?"* — corrections supersede; history stays queryable.
- *"What did the system believe as of March?"* — answers are validity-filtered, not guessed.
- *"Which source passage is this claim from?"* — every fact carries provenance to its evidence.

In our own deployment (below), the cited-chat half of this is verified daily: answers open the exact source passage. The time-travel query classes are the storage model's documented capability [13][14]; our corpus has not yet needed them in anger, which is itself information — the value arrives when corrections start.

## The hybrid, and when each side actually wins

**The hybrid wins** when the private corpus is substantial and the public work uses the studio: keep Gemini Notebook for published papers and media outputs; put the manuscript, client files, and licensed data on your own hardware. The sync friction is real — two systems, two backup regimes — and it is smaller than either single-system compromise *at that workload*.

**Pure cloud wins** when: sources are mostly public, volume fits the free or $4.99 tier, and you have no appetite for maintenance. That is most students and most casual researchers, and for them the managed product is simply better.

**Pure self-hosted wins** when: the corpus must never touch cloud infrastructure at all (air-gapped work, strict client terms), or your agents need programmatic access daily. Skip the hybrid; the cloud leg buys you nothing you're allowed to use.

"Serious users," then, means specifically: people who query their own corpus weekly and hold material they can't put on someone else's servers. If that isn't you, the cloud product is the right answer and this article's hardware talk is optional reading.

## What a month of running it actually costs — ours, disclosed

Disclosure: the deployment below is our own live instance — one practitioner data point, not a benchmark. Utopia v0.1.0-rc4, self-hosted, holding a working writer's corpus (a novel's worldbuilding bible plus research files, ~200 documents, ~2 MB of text). The project went public in August 2026 and has cut four release candidates in the 48 hours before this writing (rc4, shipped today, adds undoable document deletion) [14][15] — rapid rc cadence reads as active maintenance, not stability, and pre-1.0 means pin your version and test your backups.

- **Setup:** one afternoon — server install, a local embedding model (bge-small), corpus upload. All ~200 documents ingested within an hour, mostly unattended.
- **Resources:** ~0.6 GB RAM (server) + ~1.7 GB (local embedding model). Comfortable on a $5–10/month VPS or spare hardware.
- **Ongoing cost:** software $0 (Apache-2.0). Maintenance budget: 1–3 hours/month for a single-node setup by our estimate — two weeks in, it has actually been minutes per week (backups, one version pin). Embeddings run locally at $0; a hosted chat model bills per token, the same way any RAG stack does. If your hourly rate is high and your volume low, do that math honestly before switching — it may favor the managed tier.
- **Quality, in our testing:** cited Q&A across a fiction-and-notes corpus returns accurate inline citations that open the exact passage; open-ended synthesis quality trails Gemini, as expected with a smaller endpoint. The substrate's value is grounding and provenance, not out-writing Gemini.
- **Security:** you own the attack surface — one exposed port turns your private corpus public. Ours is loopback-only with no inbound exposure. If you can't say the same, don't put your sensitive corpus on it.

## The decision, compressed

If your sources are public and the studio serves you: stay. If your corpus holds work that must remain yours: the tools to own it are mature enough in September 2026 that the default — everything in the cloud — is now a choice rather than a given. The rename didn't change that; it only made the alternative stack easier to see.

---

## FAQ

**Is NotebookLM still free after the Gemini Notebook rename?**
Yes. As of September 2026 the free tier includes 100 notebooks, 50 sources per notebook, 50 chats per day, and 3 audio plus 3 video overviews per day [2]. Paid tiers (Plus $4.99, Pro $19.99, Ultra from $99.99/month) raise the meters rather than unlock new core features [2][7].

**Can you self-host NotebookLM itself?**
No. There is no self-hostable version and no consumer API; programmatic access exists only in the enterprise Gemini Notebook offering [7]. You can self-host equivalents: sovereignty-first tools (Open Notebook, SurfSense) or knowledge substrates (Utopia, Graphiti) [3][10][12][14].

**What is the best self-hosted NotebookLM alternative in 2026?**
Depends on the job. Open Notebook (38k+ stars, MIT) is the closest drop-in feel with podcast generation and 18+ model providers [3][9]. SurfSense wins on external connectors like Slack and Notion [10]. For provenance-tracked, time-aware knowledge your own agents can query, a bitemporal substrate like Utopia or Graphiti does what notebook tools cannot [12][13][14].

**How long does it take to set up a self-hosted alternative?**
A basic deployment is an afternoon: install the server, configure an embedding model, upload your corpus. Our ~200-document corpus finished ingesting within an hour, mostly unattended. Budget extra time for OCR-heavy PDFs and for testing your backup routine.

**Does NotebookLM use your documents to train Google's models?**
Google's documentation states your data is not used to train Gemini Notebook unless you submit feedback, and Workspace-tier uploads are never human-reviewed or used for training even with feedback [16]. Training policy is not the same as infrastructure ownership, though — the corpus still resides on Google's cloud, which is the boundary self-hosting addresses.

**What do you lose by self-hosting?**
The studio — Audio Overviews, Video Overviews, flashcards, and per-notebook code execution are cloud capabilities self-hosted tools haven't matched [2][5]. Synthesis quality also depends on your chosen model endpoint; Gemini remains ahead of most self-hosted stacks for open-ended analysis.

**Is self-hosting secure?**
It transfers security to you. Done right — loopback or VPN-only access, no exposed ports, encrypted backups, pinned versions — it is defensible. Done casually, one exposed container publishes your private corpus.

**Is my data locked in if I self-host?**
Less than with most SaaS: open-source substrates store plain files and open databases (PostgreSQL, SQLite), and notebook tools support standard exports. Check the export path before committing — a substrate you cannot leave is just a slower cloud.

**How do self-hosted tools handle deletion requests?**
By design, better than the cloud for verifiability: substrates like Utopia store deletions as retractions on a bitemporal ledger — rc4 made document deletion an undoable, auditable event rather than a hole in the database [15] — so you can prove what was removed and when. That matters for GDPR-style erasure obligations on private corpora.

**What happens if Google changes the limits again?**
It will — Google restructured the tiers twice in recent months [2][7]. That volatility is itself an argument for owning the substrate for high-volume work.

---

## Sources

Primary (Google):
[1] Google blog, "NotebookLM is now Gemini Notebook," July 16, 2026 — blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/
[2] Google Support, "Upgrade Gemini Notebook" — limits effective Sept 2, 2026 — support.google.com/gemininotebook/answer/16213268
[16] Google Support, "Learn about Gemini Notebook" — data-handling section — support.google.com/gemininotebook/answer/16164461

Independent coverage of the rename:
[4] 9to5Google, "Google renames NotebookLM to Gemini Notebook," July 16, 2026
[5] TechCrunch, July 16, 2026; The Next Web rebrand + code-execution expansion coverage
[6] Google Workspace Updates, "NotebookLM is now Gemini Notebook," July 2026

Product analysis:
[7] Glasp, "NotebookLM Is Now Gemini Notebook: 2026 Guide" (tier table, enterprise-API analysis)

Sovereignty-first tools:
[3] Open Notebook — github.com/lfnovo/open-notebook (MIT; star count via GitHub API, Sept 3, 2026)
[9] KDnuggets, "Open Notebook: A True Open Source Private NotebookLM Alternative"; XDA Developers hands-on
[10] SurfSense — github.com/MODSetter/SurfSense (16,000+ stars via GitHub API, Sept 3, 2026; feature set per project README)
[11] Pinggy, "Self-Host Open Notebook: Run Your Own Private NotebookLM"

Knowledge substrates:
[12] Graphiti (Zep) — github.com/getzep/graphiti (Apache-2.0; star count via GitHub API, Sept 3, 2026)
[13] RAGBrain — github.com (bitemporal RAG, as-of retrieval and system-time replay)
[14] Utopia — github.com/deeplethe/utopia (Apache-2.0; 3,532 stars via GitHub API, Sept 3, 2026)
[15] Utopia release notes v0.1.0-rc1–rc4, Sept 2–3, 2026

Deployment numbers are from the authors' own live instance (September 2026) — one practitioner data point, not a benchmark.
