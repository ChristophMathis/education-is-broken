#!/usr/bin/env bash
# _convert-chapters-to-docx.sh
# Converts all markdown chapters to .docx using pandoc.
# Resolves Obsidian ![[image]] embeds to standard Markdown image syntax.
#
# Usage: ./scripts/_convert-chapters-to-docx.sh <book-directory>
# The book-directory should contain chapters/ with .md files.

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <book-directory>" >&2
  echo "  e.g. $0 education-is-broken" >&2
  exit 1
fi

BOOK_ROOT="$(cd "$1" && pwd)"

SRC_DIR="$BOOK_ROOT/chapters"
OUT_DIR="$BOOK_ROOT/word"

mkdir -p "$OUT_DIR"

# Find the absolute path of an image file within the vault.
# Obsidian resolves ![[name]] by searching the entire vault.
find_image() {
  local name="$1"
  local result
  result="$(find "$BOOK_ROOT" -name "$name" -type f 2>/dev/null | head -1)"
  echo "$result"
}

# Convert Obsidian ![[image.ext]] and ![[image.ext|Caption]] embeds to standard
# Markdown ![alt](path) syntax. Supports common image extensions.
resolve_obsidian_images() {
  local input="$1"
  local tmp
  tmp="$(mktemp)"

  while IFS= read -r line; do
    # Match ![[filename.ext|Caption]] (with pipe-separated caption)
    if [[ "$line" =~ !\[\[([^]|]+\.(png|jpg|jpeg|gif|svg|webp))\|([^]]+)\]\] ]]; then
      local img_name="${BASH_REMATCH[1]}"
      local caption="${BASH_REMATCH[3]}"
      local img_path
      img_path="$(find_image "$img_name")"
      if [ -n "$img_path" ]; then
        line="${line//\!\[\[$img_name\|$caption\]\]/![$caption]($img_path)}"
      else
        echo "  WARNING: image not found: $img_name" >&2
      fi
    # Match ![[filename.ext]] (without caption)
    elif [[ "$line" =~ !\[\[([^]]+\.(png|jpg|jpeg|gif|svg|webp))\]\] ]]; then
      local img_name="${BASH_REMATCH[1]}"
      local img_path
      img_path="$(find_image "$img_name")"
      if [ -n "$img_path" ]; then
        line="${line//\!\[\[$img_name\]\]/![$img_name]($img_path)}"
      else
        echo "  WARNING: image not found: $img_name" >&2
      fi
    fi
    printf '%s\n' "$line"
  done < "$input" > "$tmp"

  echo "$tmp"
}

converted=0
failed=0

OUT_FILE=$OUT_DIR/chapters.md

echo "\n" >$OUT_FILE
for md_file in "$SRC_DIR"/*.md; do
    echo "processing $md_file"
    cat $md_file >>$OUT_FILE
    echo "" >>$OUT_FILE
done


for md_file in "$OUT_FILE"; do
  [ -f "$md_file" ] || continue

  basename="$(basename "$md_file" .md)"
  docx_file="$OUT_DIR/${basename}.docx"

  echo "Converting: $(basename "$md_file")"

  # Pre-process to resolve Obsidian image embeds
  tmp_file="$(resolve_obsidian_images "$md_file")"
  trap "rm -f '$tmp_file'" EXIT

  if pandoc "$tmp_file" -o "$docx_file" --from markdown --to docx \
       --resource-path="$BOOK_ROOT:$BOOK_ROOT/media"; then
    converted=$((converted + 1))
  else
    echo "  ERROR: conversion failed for $(basename "$md_file")" >&2
    failed=$((failed + 1))
  fi

  rm -f "$tmp_file"
done

echo ""
echo "Done. $converted converted, $failed failed."
echo "Output: $OUT_DIR/"
