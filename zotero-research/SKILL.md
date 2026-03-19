---
name: zotero-research
description: Access and search your local Zotero research library directly. Search papers by title, author, tag, or content. Extract annotations and notes. Generate literature reviews from your collection. No API keys required - works offline with your local Zotero database.
---

# Zotero Research Skill

Access your personal Zotero research library directly through the local SQLite database. Works completely offline - no API keys needed!

## Features

- 🔍 **Full-text search** across titles, abstracts, and notes
- 🏷️ **Tag-based browsing** and filtering
- ✍️ **Author search** and citation analysis
- 📝 **Annotation extraction** from PDF highlights
- 📚 **Collection navigation** and management
- 📊 **Literature review generation** from search results

## Requirements

- Zotero desktop app installed
- Python 3 with sqlite3 support (built-in)
- No additional dependencies!

## Setup

The skill automatically detects your Zotero data directory:
- **macOS**: `~/Library/Application Support/Zotero/Profiles/*/zotero.sqlite`
- **Linux**: `~/.zotero/zotero/*/zotero.sqlite`
- **Windows**: `%APPDATA%/Zotero/Zotero/Profiles/*/zotero.sqlite`

## Usage

### 1. Search Your Library

```bash
# Search by keywords
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --query "multi-agent"

# Search by author
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --author "Russell"

# Search by tag
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --tag "AI"

# Combined search
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --query "reinforcement learning" --tag "deep-learning"
```

### 2. Browse Collections

```bash
# List all collections
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --collections

# Search within a specific collection
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --collection "AI Papers" --query "transformer"
```

### 3. Get Paper Details

```bash
# Get detailed info about a paper
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --item-key "ABC123"

# Show annotations/notes
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --item-key "ABC123" --annotations
```

### 4. Generate Literature Review

```bash
# Generate markdown review from search results
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --query "AI Agent" --limit 20 --output review.md
```

### 5. Advanced Search

```bash
# Recent papers only
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --query "large language model" --since 2025-01-01

# Full-text search including notes
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --query "attention mechanism" --fulltext

# Export to BibTeX
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --query "robotics" --export bibtex --output robotics.bib
```

### 6. Auto-import from arXiv (New!)

Automatically import arXiv papers into Zotero:

```bash
# Import specific paper by arXiv ID
python3 ~/.claude/skills/zotero-research/scripts/auto_import.py \
  --arxiv-id 2401.12345 --open

# Search and import multiple papers
python3 ~/.claude/skills/zotero-research/scripts/auto_import.py \
  --query "multi-agent reinforcement learning" \
  --max-results 5 --open

# Import from file containing arXiv IDs
python3 ~/.claude/skills/zotero-research/scripts/auto_import.py \
  --file arxiv_ids.txt --format bibtex

# Export as CSL JSON (Zotero native format)
python3 ~/.claude/skills/zotero-research/scripts/auto_import.py \
  --arxiv-id 2401.12345 --format csl --output paper.json
```

**Supported formats:**
- `csl` - CSL JSON (Zotero native, recommended)
- `bibtex` - BibTeX format

**Import methods:**
1. Use `--open` flag to auto-open in Zotero (macOS/Linux/Windows)
2. Drag the generated file into Zotero window
3. Use Zotero menu: File → Import

## Search Examples for AI Research

```bash
# Find papers about multi-agent systems
"Search my Zotero for multi-agent papers from 2024"

# Find papers by specific author
"Find all papers by Yoshua Bengio in my library"

# Get recent additions
"Show me the 10 most recent papers I added about transformers"

# Generate topic summary
"Create a summary of all papers in my 'RL' collection"

# Find unread papers
"List papers in my 'To Read' collection about LLMs"
```

## Output Formats

The script supports multiple output formats:
- `--format text` (default): Human-readable format
- `--format json`: Machine-readable JSON
- `--format markdown`: Markdown with links
- `--format csv`: Spreadsheet format

## Tips

1. **Use Zotero tags effectively**: Tag papers by topic, status (read/unread), importance
2. **Organize with collections**: Create collections for different projects
3. **Add notes**: Your notes are searchable too!
4. **Sync regularly**: The skill reads from local database; sync Zotero to get latest

## Troubleshooting

**"Cannot find Zotero database"**
- Make sure Zotero is installed and has been run at least once
- Check that `zotero.sqlite` exists in your profile directory

**"Database is locked"**
- Close Zotero desktop app before running searches
- Or use `--copy-db` flag to create a temporary copy

**"No results found"**
- Try broader search terms
- Check that papers are actually imported into Zotero
- Verify tags and collections names match exactly

## Alternative: Direct SQL Access

For power users, you can directly query the Zotero SQLite database:

```bash
# Connect to database
sqlite3 ~/Library/Application\ Support/Zotero/Profiles/*/zotero.sqlite

# Example queries
.tables                          # List all tables
SELECT * FROM items LIMIT 5;     # Show first 5 items
SELECT * FROM collections;       # List collections
```

## Integration with Other Skills

Combine with other skills for powerful workflows:

```bash
# 1. Find papers in Zotero
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --query "transformer" --output transformers.json --format json

# 2. Use ai-llamaindex to build index
# 3. Use ai-chroma for vector search
# 4. Generate paper summaries with Claude
```

## Automated Import Workflows

### Method 1: Zotero Connector (Recommended for daily use)

**Installation:**
1. Install [Zotero Connector](https://www.zotero.org/download/connectors) for your browser
2. Install Zotero desktop app
3. Sign in to sync (optional)

**Usage:**
- On any academic website (Google Scholar, arXiv, etc.)
- Click the Zotero icon in browser toolbar
- Paper is automatically saved with PDF and metadata

### Method 2: Automated Import Script

**For bulk import from arXiv:**

```bash
# Create a workflow script
cat > import_workflow.sh << 'EOF'
#!/bin/bash
# Import workflow: arXiv → Zotero

TOPIC="$1"
MAX_RESULTS="${2:-10}"

echo "🔍 Searching arXiv for: $TOPIC"
echo "📥 Will import $MAX_RESULTS papers"

# Import and auto-open in Zotero
python3 ~/.claude/skills/zotero-research/scripts/auto_import.py \
  --query "$TOPIC" \
  --max-results "$MAX_RESULTS" \
  --format csl \
  --open

echo "✅ Import complete!"
EOF

chmod +x import_workflow.sh

# Use it
./import_workflow.sh "multi-agent RL" 5
```

### Method 3: Watch Folder

**Setup:**
1. Zotero → Edit → Preferences → Advanced → Files and Folders
2. Set "Linked Attachment Base Directory"
3. Set "Watch Folder" for automatic PDF import

**Usage:**
- Drop PDFs into watch folder
- Zotero auto-imports with metadata extraction

### Complete Research Workflow

```
1. Discover papers (Google Scholar, arXiv, Twitter)
   ↓
2. Import to Zotero (Connector or auto_import script)
   ↓
3. Tag and organize (in Zotero)
   ↓
4. Search and analyze (zotero-research skill)
   ↓
5. Generate literature review
   ↓
6. Export citations for writing
```

**One-liner for complete workflow:**
```bash
# Search, import, and generate review
python3 ~/.claude/skills/zotero-research/scripts/auto_import.py \
  --query "agentic AI" --max-results 20 && \
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --query "agentic" --output agentic_review.md --limit 20
```
