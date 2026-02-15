# Root

## Preparing the Pipeline
1. Prepare a xxx-template.docx file like the example in book. Frontmatter, formattting goes here.
## Production Pipeline

1. Fill chapters into directory chapters. Each should start with a blank line, the a H1 ("#") chapter title. The chapter are used in sequence of the filenams, so mybe you prepend the names with "01.topic"
2. Run the convert-chapters-to-word.sh script in the terminal. It creates a file book/word/chapters.docx. It converts wiki transclusions ( !\[\[image199.png\]\]) into word embeddings
3. Now copy the template into a working document. Open the working dokcument and copy the complete content of chapters.docx into whorking document (replace: "copy content here")
4. If needed, install the word-index skill, then ask claude to create word index entries.
5. Open the working document again and refresh the entries: ctrl-A, F9
6. Happy publishing
