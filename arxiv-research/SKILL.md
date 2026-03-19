---
name: arxiv-research
description: Free academic paper research using arXiv API. Search, summarize, and analyze latest AI/ML papers without requiring API keys. Use when you need to research academic literature, find relevant papers, summarize paper content, or track latest research trends on arXiv.
---

# arXiv Research Skill

Free academic paper research using arXiv's open API. No API keys required!

## Capabilities

- Search papers by keywords, authors, or categories
- Download and summarize paper abstracts
- Track latest papers in specific fields
- Generate literature reviews from multiple papers
- Extract key insights and citations

## Usage

### 1. Search Papers

Use the arXiv API to search for papers:

```bash
# Search by keywords
python3 ~/.claude/skills/arxiv-research/scripts/search.py --query "transformer architecture" --max-results 10

# Search by category (cs.AI = Artificial Intelligence)
python3 ~/.claude/skills/arxiv-research/scripts/search.py --category cs.AI --date-from 2025-01-01 --max-results 20

# Search with multiple filters
python3 ~/.claude/skills/arxiv-research/scripts/search.py --query "multi-agent" --category cs.MA --sort-by submittedDate --max-results 15
```

### 2. Get Paper Details

```bash
# Get detailed info about specific papers
python3 ~/.claude/skills/arxiv-research/scripts/search.py --id 2601.01743,2601.02749
```

### 3. Generate Literature Review

```bash
# Auto-generate literature review from search results
python3 ~/.claude/skills/arxiv-research/scripts/search.py --query "AI Agent" --category cs.AI --max-results 20 --output review.md
```

## arXiv Categories for AI/ML Research

- **cs.AI** - Artificial Intelligence
- **cs.LG** - Machine Learning
- **cs.CL** - Computation and Language (NLP)
- **cs.CV** - Computer Vision
- **cs.MA** - Multiagent Systems
- **cs.IR** - Information Retrieval
- **cs.DB** - Databases
- **cs.SE** - Software Engineering
- **stat.ML** - Statistics - Machine Learning

## Search Tips

1. **Use specific keywords**: "transformer attention mechanism" > "deep learning"
2. **Combine with categories**: Always specify a category for better results
3. **Sort by date**: Use `--sort-by submittedDate` for latest papers
4. **Date filtering**: Use `--date-from YYYY-MM-DD` for recent papers

## Alternative: Direct Web Search

For broader research beyond arXiv, use Kimi's built-in web search:
- Simply ask: "Search for latest papers on [topic]"
- Or: "Research the current state of [field]"

## Examples

```bash
# Find latest agent papers
python3 ~/.claude/skills/arxiv-research/scripts/search.py --query "AI Agent" --category cs.AI --date-from 2025-01-01 --max-results 10

# Find RAG-related papers
python3 ~/.claude/skills/arxiv-research/scripts/search.py --query "retrieval augmented generation" --category cs.CL --max-results 15

# Find papers by specific topic
python3 ~/.claude/skills/arxiv-research/scripts/search.py --query "chain of thought reasoning" --category cs.LG --sort-by relevance
```

## Notes

- arXiv API is rate-limited to reasonable usage (no key required)
- Returns abstracts and metadata (not full PDFs)
- For full papers, visit the provided arXiv links
- Respect arXiv's terms of service
