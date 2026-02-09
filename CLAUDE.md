# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **book manuscript project**, not a software project. The book "Education is Broken" examines problems in education systems and proposes solutions in the context of AI. Author: Christoph Mathis.

The project is currently on **v5** of the manuscript, with v4 previously published as PDF.

## Repository Structure

- `education-is-broken-vault/` — Primary Obsidian vault (main working directory)
  - `book/chapters/` — Individual chapter files (markdown), the source of truth
  - `book/Index.md` — Longform plugin config defining chapter order and compilation
  - `book/manuscript-v5.md` — Compiled full manuscript (generated from chapters)
  - `book/sources/` — References and citation materials
  - `backlog/`, `current/`, `work/` — Research, feedback, and working materials
- `af/` — Affinity Publisher layout files (binary `.af` format) for final PDF production
- `archive/` — All previous manuscript versions (v1-v4) for reference
- `prompts/` — Claude prompts used for writing assistance

## Writing & Publication Pipeline

```
Individual chapter .md files (source of truth)
  → Obsidian Longform plugin compiles into manuscript-v5.md
    → Pandoc plugin exports to .docx
      → Affinity Publisher for final layout → PDF
```

**Chapter order** is defined in `education-is-broken-vault/book/Index.md` via YAML frontmatter. Chapters are numbered with prefixes (01-12 for main content, 42+ for appendices, 50+ for references, 61+ for analysis).

## Key Conventions

- All manuscript content is in **Markdown** within the Obsidian vault
- Chapter filenames follow the pattern `NN.chapter-slug.md`
- The compiled `manuscript-v5.md` is a generated artifact — edit individual chapter files, not the compiled manuscript
- Obsidian community plugins in use: `longform`, `obsidian-outliner`, `obsidian-pandoc`

## Claude Code Permissions

The local settings (`.claude/settings.local.json`) restrict bash to read-only commands: `grep`, `ls`, `find`, `git status`, `file`, `du`. This is intentional — the project is a writing project where destructive shell operations are not needed.

## Launch Script

`start-claude.sh` sets `CLAUDE_CODE_TASK_LIST_ID="education-is-broken-tasks"` for task list persistence across sessions.
