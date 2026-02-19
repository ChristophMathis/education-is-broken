#!/usr/bin/env bash
# convert-chapters-to-docx.sh
# Wrapper that runs the shared conversion script for this book.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

exec "$REPO_ROOT/scripts/_convert-chapters-to-docx.sh" "$SCRIPT_DIR"
