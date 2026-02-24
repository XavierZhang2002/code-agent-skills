#!/bin/bash
# Export skills to a tar.gz archive for backup
# Usage: ./export-skills.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXPORT_DIR="$SCRIPT_DIR/exports"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
EXPORT_FILE="claude-skills-$TIMESTAMP.tar.gz"

echo "📦 Exporting Claude Code skills..."

# Create exports directory
mkdir -p "$EXPORT_DIR"

# Create tar.gz excluding .git directories
cd "$SCRIPT_DIR"
tar -czf "$EXPORT_DIR/$EXPORT_FILE" \
    --exclude='.git' \
    --exclude='exports' \
    --exclude='*.pyc' \
    --exclude='__pycache__' \
    .

echo "✅ Exported to: $EXPORT_DIR/$EXPORT_FILE"
echo ""
echo "📊 Contents:"
tar -tzf "$EXPORT_DIR/$EXPORT_FILE" | head -20
echo "..."
echo ""
echo "💡 To import on another machine:"
echo "   tar -xzf $EXPORT_FILE -C ~/.config/agents/skills/"
