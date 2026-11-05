#!/bin/sh
# Install sources/model-operating-rules.md for one agent harness.
# Run it from a clone, or pipe it from curl with a repo to clone:
#   curl -fsSL <raw url of install.sh> | sh -s -- --repo <repo url> --target codex
# Targets: claude-code, codex, gemini, cursor, copilot.
# Without --target, the script detects Claude Code from its environment.
# It never overwrites a file that has other content.
set -eu

TARGET=""
REPO=""
DEST="."
RULES_NAME="model-operating-rules.md"

usage() {
  sed -n '2,7p' "$0" 2>/dev/null || true
  echo "Usage: install.sh [--target NAME] [--repo URL] [--dir DEST]"
  exit "${1:-0}"
}

while [ $# -gt 0 ]; do
  case "$1" in
    --target) TARGET="$2"; shift 2 ;;
    --repo) REPO="$2"; shift 2 ;;
    --dir) DEST="$2"; shift 2 ;;
    -h|--help) usage ;;
    *) echo "unknown argument: $1" >&2; usage 1 ;;
  esac
done

# Find the rules file: next to this script, in the working folder, or in a clone.
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd || echo "")
RULES=""
for base in "$SCRIPT_DIR" "$PWD"; do
  if [ -n "$base" ] && [ -f "$base/sources/$RULES_NAME" ]; then
    RULES="$base/sources/$RULES_NAME"
    break
  fi
done
if [ -z "$RULES" ]; then
  if [ -z "$REPO" ]; then
    echo "no sources/$RULES_NAME here. Give the repository with --repo URL" >&2
    exit 1
  fi
  TMP=$(mktemp -d)
  trap 'rm -rf "$TMP"' EXIT
  git clone --quiet --depth 1 "$REPO" "$TMP/repo"
  RULES="$TMP/repo/sources/$RULES_NAME"
fi
VERSION=$(sed -n 's/^Version \([0-9.]*\),.*/\1/p' "$RULES" | head -1)

# Detect the harness when no target is given. Claude Code sets CLAUDECODE.
if [ -z "$TARGET" ]; then
  if [ -n "${CLAUDECODE:-}" ]; then
    TARGET="claude-code"
  else
    echo "no --target given, and only Claude Code is detectable." >&2
    echo "name one: claude-code, codex, gemini, cursor, copilot" >&2
    exit 1
  fi
fi

# A copy install writes the full rules text to one file, and never clobbers.
copy_install() {
  out="$1"
  prefix="${2:-}"
  if [ -f "$out" ]; then
    if grep -q "^# Operating Rules" "$out"; then
      echo "already installed: $out"
      return 0
    fi
    echo "$out exists with other content. Append the rules by hand, or move it first" >&2
    exit 1
  fi
  mkdir -p "$(dirname "$out")"
  { [ -n "$prefix" ] && printf '%s\n' "$prefix"; cat "$RULES"; } > "$out"
  echo "installed rules $VERSION (copy): $out"
}

case "$TARGET" in
  claude-code)
    # A pointer install: the rules file plus an import line in CLAUDE.md.
    if [ ! -f "$DEST/$RULES_NAME" ]; then
      cp "$RULES" "$DEST/$RULES_NAME"
    fi
    if [ -f "$DEST/CLAUDE.md" ] && grep -q "$RULES_NAME" "$DEST/CLAUDE.md"; then
      echo "already installed: $DEST/CLAUDE.md imports $RULES_NAME"
      exit 0
    fi
    printf '\n@%s\n' "$RULES_NAME" >> "$DEST/CLAUDE.md"
    echo "installed rules $VERSION (pointer): $DEST/CLAUDE.md imports $RULES_NAME"
    ;;
  codex) copy_install "$DEST/AGENTS.md" ;;
  gemini) copy_install "$DEST/GEMINI.md" ;;
  copilot) copy_install "$DEST/.github/copilot-instructions.md" ;;
  cursor) copy_install "$DEST/.cursor/rules/operating-rules.mdc" "---
alwaysApply: true
---" ;;
  *) echo "unknown target: $TARGET" >&2; usage 1 ;;
esac
