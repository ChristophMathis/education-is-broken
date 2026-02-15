---
name: word-index
description: "Add a back-of-book index to a Word (.docx) document. Use this skill whenever the user asks to create an index, add index entries, generate a book index, or mark terms for indexing in a Word document. Also triggers when users mention XE fields, index entries, or want to make a document searchable by key terms. Works with any .docx file and an optional glossary/term list as input."
---

# Word Index Generator

Adds XE (index entry) field codes throughout a Word document and places an INDEX field at the end. When the document is opened in Word and fields are updated (`Ctrl+A` → `F9`), the index renders with page numbers automatically.

## How it works

The procedure uses the docx skill's unpack→edit XML→repack workflow to inject standard Word field codes into the document XML. Each glossary term gets one XE entry per chapter section (detected via Heading 1 style boundaries), marking the first occurrence of that term in each section.

## Prerequisites

- The **docx skill** must be available (for `unpack.py` and `pack.py`)
- A **term source**: either a markdown glossary table (`| Term | Explanation |`) or a list of terms provided by the user
- The target `.docx` file

## Step-by-step procedure

### 1. Prepare the term list

If the user provides a markdown glossary file with a table like:

```markdown
| Term | Explanation |
|------|-------------|
| Bologna Process | Intergovernmental reform... |
| ECTS | European Credit Transfer... |
```

→ Parse the first column to extract index terms.

If no glossary exists, ask the user for terms or extract them from the document content.

### 2. Unpack the document

Use the docx skill's unpack tool **without run merging** to preserve the original XML structure:

```bash
python <docx-skill>/scripts/office/unpack.py document.docx unpacked/ --merge-runs false
```

The `--merge-runs false` flag is important because run merging can combine field code elements in ways that break them when repacked.

### 3. Run the index insertion script

```bash
python <this-skill>/scripts/add_word_index.py unpacked/word/document.xml glossary.md
```

The script does three things:

1. **Parses the glossary** to build a term list
2. **Inserts XE fields** after the first `<w:r>` containing each term per Heading 1 section
3. **Adds an INDEX field** on a new page at the end of the document

Use `--dry-run` to preview without writing changes.

### 4. Repack and validate

```bash
python <docx-skill>/scripts/office/pack.py unpacked/ output.docx --original document.docx
```

If validation fails with content-type errors for images (common with pandoc-generated documents), add the missing `<Default Extension="png" ContentType="image/png"/>` to `[Content_Types].xml` before repacking.

### 5. Tell the user how to activate the index

The INDEX field shows placeholder text until updated. In Microsoft Word:

- `Ctrl+A` then `F9` to update all fields
- Or right-click the INDEX field → "Update Field"

In LibreOffice Writer:

- `F9` or Tools → Update → Fields

## Critical: XE field format

XE field codes **must not** include `<w:vanish/>` in the run properties. Word and LibreOffice silently ignore XE entries that have vanish set on the `<w:fldChar>` or `<w:instrText>` runs. This is a non-obvious pitfall — many online references suggest adding vanish to hide XE fields, but it actually prevents Word from recognising them as index entries.

Correct format:
```xml
<w:r><w:fldChar w:fldCharType="begin"/></w:r>
<w:r><w:instrText xml:space="preserve"> XE "Term" </w:instrText></w:r>
<w:r><w:fldChar w:fldCharType="end"/></w:r>
```

Wrong format (entries will be invisible to the INDEX field):
```xml
<w:r><w:rPr><w:vanish/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r>
<w:r><w:rPr><w:vanish/></w:rPr><w:instrText ...> XE "Term" </w:instrText></w:r>
<w:r><w:rPr><w:vanish/></w:rPr><w:fldChar w:fldCharType="end"/></w:r>
```

## INDEX field format

The INDEX field at the end of the document uses a two-column layout with alphabetical headings:

```xml
<w:fldChar w:fldCharType="begin"/>
<w:instrText xml:space="preserve"> INDEX \c "2" \h "A" \e "	" </w:instrText>
<w:fldChar w:fldCharType="separate"/>
<w:t>Update this field to generate the index.</w:t>
<w:fldChar w:fldCharType="end"/>
```

Switches: `\c "2"` = two columns, `\h "A"` = alphabetical group headings, `\e "	"` = tab separator between entry and page number.

## Heading style detection

The script auto-detects the Heading 1 style ID from the document. German-locale documents created by pandoc often use `berschrift1` instead of `Heading1`. The script checks common variants across locales and falls back to outline level detection.

## Edge cases

- **Terms inside table cells**: The script matches terms in `<w:t>` elements regardless of whether they're in body paragraphs or table cells
- **Case-insensitive matching**: All term searches are case-insensitive
- **Special characters in terms**: The script XML-escapes `&`, `<`, `>`, and `"` in term names
- **Multiple terms per paragraph**: Each term gets its own XE field after the run where it appears
- **Content-type declarations**: Pandoc-generated .docx files sometimes use per-file Override declarations instead of Default Extension declarations for images. If pack.py validation fails, add the missing Default Extension entry to `[Content_Types].xml`.
