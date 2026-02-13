#!/usr/bin/env python3
"""
Add XE (index entry) fields to a Word document XML and an INDEX field at the end.

Usage:
    python add_word_index.py <unpacked_document_xml> <glossary_md> [--dry-run]

The script:
1. Reads index terms from a glossary markdown file (| Term | Explanation | table)
2. For each term, finds the first occurrence per chapter (Heading 1 section)
3. Inserts an XE field code after the run containing the term
4. Adds an INDEX field on a new page at the end of the document

XE field format (must NOT use <w:vanish/> on field code runs):
    <w:r><w:fldChar w:fldCharType="begin"/></w:r>
    <w:r><w:instrText xml:space="preserve"> XE "Term" </w:instrText></w:r>
    <w:r><w:fldChar w:fldCharType="end"/></w:r>
"""

import re
import sys
import os


def parse_glossary(glossary_path):
    """Parse a markdown glossary table and return list of (display_term, [search_patterns])."""
    terms = []
    with open(glossary_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|") or line.startswith("| Term") or line.startswith("|--"):
                continue
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 3:
                term = parts[1]
                if term:
                    # Build search patterns from the term
                    patterns = [term]
                    # Strip markdown formatting for search
                    clean = re.sub(r'[*_]', '', term)
                    if clean != term:
                        patterns.append(clean)
                    terms.append((term, patterns))
    return terms


def make_xe(term):
    """Generate XML for an XE index entry field.

    CRITICAL: Do NOT add <w:vanish/> to field code runs.
    Word/LibreOffice will not recognise the XE entries if vanish is present
    on the fldChar or instrText runs.
    """
    t = term.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', '&quot;')
    return (
        f'<w:r><w:fldChar w:fldCharType="begin"/></w:r>'
        f'<w:r><w:instrText xml:space="preserve"> XE "{t}" </w:instrText></w:r>'
        f'<w:r><w:fldChar w:fldCharType="end"/></w:r>'
    )


def make_index_field(heading_style="berschrift1"):
    """Generate XML for an INDEX field with a page break and heading.

    Args:
        heading_style: The style ID used for Heading 1 in the document.
                       German-locale docs often use "berschrift1" instead of "Heading1".
    """
    return (
        f'<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
        f'<w:p><w:pPr><w:pStyle w:val="{heading_style}"/></w:pPr>'
        f'<w:r><w:t>Index</w:t></w:r></w:p>'
        f'<w:p><w:r>'
        f'<w:fldChar w:fldCharType="begin"/></w:r>'
        f'<w:r><w:instrText xml:space="preserve"> INDEX \\c "2" \\h "A" \\e "\t" </w:instrText></w:r>'
        f'<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
        f'<w:r><w:t>Update this field to generate the index.</w:t></w:r>'
        f'<w:r><w:fldChar w:fldCharType="end"/></w:r>'
        f'</w:p>'
    )


def detect_heading1_style(content):
    """Auto-detect the Heading 1 style ID from the document XML."""
    # Common style IDs for Heading 1 across locales
    candidates = ["berschrift1", "Heading1", "heading1", "Titre1", "Kop1"]
    for c in candidates:
        if f'w:val="{c}"' in content:
            return c
    # Fallback: look for outlineLevel 0
    m = re.search(r'<w:pStyle w:val="([^"]+)"/>\s*.*?<w:outlineLevel w:val="0"/>', content[:5000])
    if m:
        return m.group(1)
    return "Heading1"


def add_index_entries(xml_path, terms, dry_run=False):
    """Add XE index entries and INDEX field to the document XML."""
    with open(xml_path, "r", encoding="utf-8") as f:
        content = f.read()

    heading1_style = detect_heading1_style(content)
    heading_pattern = re.compile(rf'<w:pStyle w:val="{re.escape(heading1_style)}"/>')

    # Find chapter boundary positions
    chapter_starts = [0] + [m.start() for m in heading_pattern.finditer(content)]

    def get_chapter_idx(pos):
        for i in range(len(chapter_starts) - 1, -1, -1):
            if pos >= chapter_starts[i]:
                return i
        return 0

    # Collect insertion points
    insertions = []
    term_stats = {}

    for display_term, patterns in terms:
        marked_chapters = set()
        for pattern in patterns:
            pat = re.escape(pattern)
            for m in re.finditer(pat, content, re.IGNORECASE):
                pos = m.start()
                chapter = get_chapter_idx(pos)
                if chapter in marked_chapters:
                    continue

                # Verify this match is inside a <w:t> element (text content, not XML markup)
                t_start = content.rfind("<w:t", 0, pos)
                t_end_before = content.rfind("</w:t>", 0, pos)
                if t_start < 0 or (t_end_before >= 0 and t_end_before > t_start):
                    continue

                # Find closing </w:r> to insert after
                r_end = content.find("</w:r>", pos)
                if r_end < 0:
                    continue
                insert_pos = r_end + len("</w:r>")

                insertions.append((insert_pos, make_xe(display_term)))
                marked_chapters.add(chapter)

        term_stats[display_term] = len(marked_chapters)

    # Sort reverse for safe insertion
    insertions.sort(key=lambda x: x[0], reverse=True)

    terms_with_entries = sum(1 for v in term_stats.values() if v > 0)
    print(f"Index terms with matches: {terms_with_entries}/{len(terms)}")
    print(f"Total XE entries to insert: {len(insertions)}")

    if dry_run:
        print("\n[DRY RUN] No changes written.")
        return

    # Insert XE fields
    for pos, xe_xml in insertions:
        content = content[:pos] + xe_xml + content[pos:]

    # Add INDEX field before closing sectPr
    sect_pr_pos = content.rfind("<w:sectPr")
    if sect_pr_pos > 0:
        content = content[:sect_pr_pos] + make_index_field(heading1_style) + content[sect_pr_pos:]
        print("Added INDEX field at end of document")

    with open(xml_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Done. {len(insertions)} XE entries written.")


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <document.xml> <glossary.md> [--dry-run]")
        sys.exit(1)

    xml_path = sys.argv[1]
    glossary_path = sys.argv[2]
    dry_run = "--dry-run" in sys.argv

    terms = parse_glossary(glossary_path)
    print(f"Loaded {len(terms)} terms from glossary")

    add_index_entries(xml_path, terms, dry_run)


if __name__ == "__main__":
    main()
