# CLAUDE.md — Education is Broken

## Book Overview

"Education is Broken" examines problems in education systems and proposes solutions in the context of AI. Author: Christoph Mathis. Currently on **v5** of the manuscript (v4 was previously published as PDF).

## Directory Structure

- `chapters/` — Individual chapter .md files, **the source of truth**
- `chapters-excluded/` — Chapters removed from the current manuscript
- `sources/` — BibTeX citation files, one per chapter plus `references.bib`
- `media/` — Images referenced from chapters via Obsidian `![[image]]` syntax
- `book/` — Compiled/generated output (do not edit directly)
- `word/` — Generated .docx output from the conversion script
- `backlog/`, `work/` — Research notes, feedback, and working materials
- `artifacts/` — Published outputs (PDF, presentations)
- `root.md` — Production pipeline instructions

## Conventions

- Chapter filenames follow `NN.chapter-slug.md` (01-12 main content, 42+ appendices, 50+ references)
- Each chapter starts with a blank line, then an H1 (`#`) title
- Images use Obsidian wiki-link syntax: `![[image.png]]` or `![[image.png|Caption]]`
- Edit individual chapter files, never the compiled output in `book/` or `word/`

## Production Pipeline

```
chapters/*.md (source of truth)
  → convert-chapters-to-docx.sh compiles and converts to word/chapters.docx
    → Copy into template .docx for formatting
      → Affinity Publisher for final layout → PDF
```

Run `./convert-chapters-to-docx.sh` from this directory. It calls the shared script at `../scripts/_convert-chapters-to-docx.sh`.
