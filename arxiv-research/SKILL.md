---
name: arxiv-research
description: Search, fetch, and summarize arXiv papers. Use when the user wants to find academic papers on a specific topic, get paper summaries, track latest research, or extract key insights from arXiv. Triggers: "search arxiv", "find papers about", "summarize arxiv paper", "latest research on", "arxiv daily digest", "paper summary".
---

# arXiv Research Assistant

A comprehensive skill for searching, retrieving, and analyzing academic papers from arXiv.

## Capabilities

1. **Search Papers**: Query arXiv by keywords, authors, categories
2. **Fetch Metadata**: Get title, abstract, authors, publication date, categories
3. **Download PDFs**: Retrieve full-text PDFs for deep analysis
4. **Generate Summaries**: Create structured summaries of papers
5. **Track Updates**: Monitor specific categories for new papers

## Workflow

### 1. Search Papers

Use arXiv API to search for papers:

```bash
# Search by keyword
curl "http://export.arxiv.org/api/query?search_query=all:<KEYWORD>&start=0&max_results=10&sortBy=submittedDate&sortOrder=descending"

# Search specific category (e.g., cs.AI, cs.LG, cs.CL)
curl "http://export.arxiv.org/api/query?search_query=cat:cs.AI&start=0&max_results=20&sortBy=submittedDate&sortOrder=descending"

# Advanced search with multiple terms
curl "http://export.arxiv.org/api/query?search_query=all:<TERM1>+AND+all:<TERM2>&start=0&max_results=10"
```

Common arXiv categories:
- `cs.AI` - Artificial Intelligence
- `cs.LG` - Machine Learning
- `cs.CL` - Computation and Language (NLP)
- `cs.CV` - Computer Vision
- `cs.IR` - Information Retrieval
- `cs.DB` - Databases
- `cs.SE` - Software Engineering

### 2. Parse Response

The arXiv API returns Atom XML format. Extract:
- `<title>` - Paper title
- `<summary>` - Abstract
- `<author><name>` - Authors
- `<published>` - Publication date
- `<link rel="alternate">` - arXiv page URL
- `<link rel="related" title="pdf">` - PDF URL
- `<category term="">` - Categories

### 3. Generate Summary Structure

For each paper, create:

```markdown
## Paper Title

**Authors**: [Author list]
**Published**: [Date]
**Categories**: [Categories]
**arXiv URL**: [Link]
**PDF URL**: [Link]

### Executive Summary (3-5 sentences)
[Core contribution in plain language]

### Key Contributions
1. [Contribution 1]
2. [Contribution 2]
3. [Contribution 3]

### Methodology
[Brief description of approach/methods]

### Key Findings/Results
[Main results or findings]

### Relevance Assessment
- **Novelty**: [1-5] - How novel is the contribution?
- **Impact Potential**: [1-5] - Potential influence on the field
- **Technical Quality**: [1-5] - Rigor of methodology
- **Clarity**: [1-5] - Quality of writing and presentation

### Limitations & Gaps (from abstract)
[What the authors acknowledge as limitations]

### Connection to User's Interest
[How this relates to the specific research context]
```

## Output Formats

### Daily Digest Format
```markdown
# arXiv Daily Digest - [Date] - [Category/Topic]

## Research Highlights (Top 5)
[Most important papers with full summaries]

## Trending Topics
[Emerging themes from today's papers]

## Quick Scan (Other Papers)
[Brief 1-line summaries of remaining papers]

## Statistics
- Total papers: [N]
- High relevance: [N]
- New methods: [N]
- Experimental papers: [N]
```

### Literature Review Format
```markdown
# Literature Review: [Topic]

## Overview
[Executive summary of the field]

## Categorization of Papers

### Category 1: [Theme]
[Papers grouped by theme with synthesis]

### Category 2: [Theme]
...

## Research Timeline
[Chronological development of ideas]

## Current State of the Art
[Best performing methods/approaches]

## Identified Research Gaps
1. [Gap 1] - [Evidence from papers]
2. [Gap 2] - [Evidence from papers]
3. [Gap 3] - [Evidence from papers]

## Future Directions
[Emerging trends and opportunities]

## Reference List
[Full citations with links]
```

## Best Practices

1. **Always verify PDF accessibility** before promising full-text analysis
2. **Check publication dates** to ensure recency
3. **Cross-reference** multiple papers on same topic
4. **Note methodology quality** - experimental vs theoretical
5. **Highlight reproducibility** - code/data availability
6. **Track citation counts** when available (via Semantic Scholar if needed)

## Tools & Resources

- arXiv API: http://export.arxiv.org/api/query
- arXiv Categories: https://arxiv.org/category_taxonomy
- Rate limit: ~1 request per 3 seconds recommended
