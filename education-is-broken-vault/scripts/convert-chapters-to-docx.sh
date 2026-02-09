#!/usr/bin/env bash
# convert-chapters-to-docx.sh
# Converts all markdown chapters to .docx using pandoc.
#
# Usage: ./scripts/convert-chapters-to-docx.sh
# Run from the repository root (education-is-broken-vault/).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

SRC_DIR="$REPO_ROOT/book/chapters"
OUT_DIR="$REPO_ROOT/book/word"

mkdir -p "$OUT_DIR"

converted=0
failed=0

for md_file in "$SRC_DIR"/*.md; do
  [ -f "$md_file" ] || continue

  basename="$(basename "$md_file" .md)"
  docx_file="$OUT_DIR/${basename}.docx"

  echo "Converting: $(basename "$md_file")"
  if pandoc "$md_file" -o "$docx_file" --from markdown --to docx; then
    converted=$((converted + 1))
  else
    echo "  ERROR: conversion failed for $(basename "$md_file")" >&2
    failed=$((failed + 1))
  fi
done

echo ""
echo "Done. $converted converted, $failed failed."
echo "Output: $OUT_DIR/"
