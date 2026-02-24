#!/bin/bash
# Import skills from a tar.gz archive
# Usage: ./import-skills.sh <path-to-tar.gz>

set -e

if [ $# -eq 0 ]; then
    echo "Usage: $0 <path-to-tar.gz>"
    echo "Example: $0 exports/claude-skills-20260224_123456.tar.gz"
    exit 1
fi

IMPORT_FILE="$1"
TARGET_DIR="${HOME}/.config/agents/skills"

if [ ! -f "$IMPORT_FILE" ]; then
    echo "❌ Error: File not found: $IMPORT_FILE"
    exit 1
fi

echo "📥 Importing skills from: $IMPORT_FILE"
echo "🎯 Target directory: $TARGET_DIR"

# Backup existing skills
if [ -d "$TARGET_DIR" ] && [ "$(ls -A $TARGET_DIR)" ]; then
    BACKUP_DIR="${TARGET_DIR}.backup.$(date +%Y%m%d_%H%M%S)"
    echo "💾 Backing up existing skills to: $BACKUP_DIR"
    cp -r "$TARGET_DIR" "$BACKUP_DIR"
fi

# Create target directory if not exists
mkdir -p "$TARGET_DIR"

# Extract archive
echo "📂 Extracting..."
tar -xzf "$IMPORT_FILE" -C "$TARGET_DIR"

echo "✅ Skills imported successfully!"
echo ""
echo "📋 Installed skills:"
ls -1 "$TARGET_DIR" | grep -v "^\." | head -20
