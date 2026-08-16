#!/usr/bin/env python3
"""
Lint the wiki: check that every [[wikilink]] resolves to a real page,
find orphan pages, surface missing frontmatter fields.

Obsidian wikilink resolution: by basename, ignoring the .md extension.
This script mirrors that.
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

VAULT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")

# Build set of available basenames (no extension) across the whole vault
all_files = {}
for p in VAULT.rglob("*.md"):
    all_files.setdefault(p.stem, []).append(p)

# Real wikilinks (skip schema-doc placeholders that don't look like page names)
def is_real_link(target: str) -> bool:
    t = target.strip()
    if not t:
        return False
    if t.lower() in ("wikilink", "wikilinks", "wikilink]]", "wikilinks]]"):
        return False
    # Generic placeholders in docs
    if t in ("filename", "filename.png", "filename.md", "source-page", "source-a", "source-b", "sources", "wiki pages", "wikilink", "wikilinks"):
        return False
    return True

WIKILINK_RE = re.compile(r"\[\[([^\]\|#]+)")

links = []
inbound = defaultdict(list)
for p in sorted(VAULT.rglob("*.md")):
    text = p.read_text(errors="ignore")
    rel = p.relative_to(VAULT)
    for m in WIKILINK_RE.finditer(text):
        target = m.group(1).strip()
        # strip path prefix - Obsidian resolves by basename
        target_stem = target.split("/")[-1].removesuffix(".md")
        if is_real_link(target_stem):
            links.append((rel, target_stem))
            inbound[target_stem].append(rel)

# Check broken links
broken = []
for src, tgt in links:
    if tgt not in all_files:
        broken.append((src, tgt))

# Orphans (wiki/ only, exclude meta)
wiki = VAULT / "wiki"
real_pages = [p for p in wiki.rglob("*.md") if p.name not in ("index.md", "log.md", "hot.md", "dashboard.md")]
orphans = [p for p in real_pages if not inbound.get(p.stem)]

# Frontmatter check
def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end < 0:
        return {}
    fm = text[3:end]
    fields = {}
    for line in fm.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip()
    return fields

REQUIRED = {"title", "tldr", "date_created", "date_modified", "type", "explored", "confidence"}
missing_fm = []
for p in real_pages:
    fm = parse_frontmatter(p.read_text())
    miss = REQUIRED - set(fm.keys())
    if miss:
        missing_fm.append((p.relative_to(VAULT), sorted(miss)))

# Report
print(f"Wiki pages: {len(real_pages)}")
print(f"Total wikilinks (real): {len(links)}")
print(f"Broken links: {len(broken)}")
print(f"Orphan pages (no inbound): {len(orphans)}")
print(f"Pages with missing frontmatter fields: {len(missing_fm)}")
print()
if broken:
    print("BROKEN LINKS:")
    for s, t in broken:
        print(f"  {s} -> [[{t}]]")
    print()
if orphans:
    print("ORPHANS:")
    for o in orphans:
        print(f"  {o}")
    print()
if missing_fm:
    print("MISSING FRONTMATTER:")
    for path, fields in missing_fm:
        print(f"  {path}: missing {fields}")
    print()

print("Inbound link counts:")
for p in sorted(real_pages):
    stem = p.stem
    n = len(inbound.get(stem, []))
    flag = "" if n > 0 else "  (orphan)"
    print(f"  {n:>2}  {p.relative_to(VAULT)}{flag}")

# Exit code
sys.exit(1 if broken or missing_fm else 0)
