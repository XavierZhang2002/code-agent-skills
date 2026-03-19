#!/usr/bin/env python3
"""
Free arXiv paper search tool - No API key required!
"""

import argparse
import sys
import urllib.request
import urllib.parse
import json
from datetime import datetime
from typing import List, Optional

ARXIV_API_URL = "http://export.arxiv.org/api/query"


def search_papers(
    query: Optional[str] = None,
    category: Optional[str] = None,
    paper_ids: Optional[List[str]] = None,
    max_results: int = 10,
    sort_by: str = "relevance",
    date_from: Optional[str] = None,
) -> dict:
    """
    Search arXiv papers using the open API.
    
    Args:
        query: Search query string
        category: arXiv category (e.g., cs.AI, cs.LG)
        paper_ids: List of arXiv IDs to fetch directly
        max_results: Maximum number of results (default: 10)
        sort_by: Sort order (relevance, lastUpdatedDate, submittedDate)
        date_from: Filter papers from this date (YYYY-MM-DD)
    """
    
    # Build search query
    search_query = ""
    
    if paper_ids:
        # Fetch specific papers by ID
        id_query = ",".join(paper_ids)
        params = {"id_list": id_query}
    else:
        # Build search query
        parts = []
        if query:
            parts.append(f"all:{query}")
        if category:
            parts.append(f"cat:{category}")
        if date_from:
            parts.append(f"submittedDate:[{date_from} TO NOW]")
        
        search_query = " AND ".join(parts) if parts else "all:*"
        
        # Map sort options
        sort_mapping = {
            "relevance": "relevance",
            "lastUpdatedDate": "lastUpdatedDate",
            "submittedDate": "submittedDate",
        }
        sort_criteria = sort_mapping.get(sort_by, "relevance")
        
        params = {
            "search_query": search_query,
            "start": 0,
            "max_results": max_results,
            "sortBy": sort_criteria,
            "sortOrder": "descending",
        }
    
    # Build URL
    query_string = urllib.parse.urlencode(params)
    url = f"{ARXIV_API_URL}?{query_string}"
    
    try:
        # Make request
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
        )
        
        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read().decode("utf-8")
            return parse_arxiv_response(data)
            
    except Exception as e:
        print(f"Error fetching from arXiv: {e}", file=sys.stderr)
        return {"papers": [], "total": 0}


def parse_arxiv_response(xml_data: str) -> dict:
    """Parse arXiv API XML response."""
    import xml.etree.ElementTree as ET
    
    # Define namespaces
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom"
    }
    
    root = ET.fromstring(xml_data)
    
    papers = []
    
    for entry in root.findall("atom:entry", ns):
        paper = {}
        
        # Get ID and extract arXiv number
        id_elem = entry.find("atom:id", ns)
        if id_elem is not None:
            paper["id"] = id_elem.text.split("/")[-1]
            paper["url"] = f"https://arxiv.org/abs/{paper['id']}"
        
        # Get title
        title_elem = entry.find("atom:title", ns)
        if title_elem is not None:
            paper["title"] = title_elem.text.strip().replace("\n", " ")
        
        # Get summary (abstract)
        summary_elem = entry.find("atom:summary", ns)
        if summary_elem is not None:
            paper["abstract"] = summary_elem.text.strip() if summary_elem.text else ""
        
        # Get authors
        authors = []
        for author in entry.findall("atom:author", ns):
            name_elem = author.find("atom:name", ns)
            if name_elem is not None:
                authors.append(name_elem.text)
        paper["authors"] = authors
        
        # Get published date
        published_elem = entry.find("atom:published", ns)
        if published_elem is not None:
            paper["published"] = published_elem.text[:10]  # YYYY-MM-DD
        
        # Get categories
        categories = []
        for cat in entry.findall("arxiv:primary_category", ns):
            cat_term = cat.get("term")
            if cat_term:
                categories.append(cat_term)
        paper["categories"] = categories
        
        # Get PDF link
        for link in entry.findall("atom:link", ns):
            if link.get("title") == "pdf":
                paper["pdf_url"] = link.get("href")
                break
        
        papers.append(paper)
    
    # Get total results
    total = len(papers)
    
    return {"papers": papers, "total": total}


def format_paper(paper: dict, index: int) -> str:
    """Format a single paper for display."""
    lines = []
    lines.append(f"\n{'='*80}")
    lines.append(f"[{index}] {paper.get('title', 'N/A')}")
    lines.append(f"{'='*80}")
    lines.append(f"Authors: {', '.join(paper.get('authors', [])[:5])}")
    if len(paper.get('authors', [])) > 5:
        lines.append(f"        ... and {len(paper['authors']) - 5} more")
    lines.append(f"Date: {paper.get('published', 'N/A')}")
    lines.append(f"Categories: {', '.join(paper.get('categories', []))}")
    lines.append(f"URL: {paper.get('url', 'N/A')}")
    if 'pdf_url' in paper:
        lines.append(f"PDF: {paper['pdf_url']}")
    lines.append(f"\nAbstract:\n{paper.get('abstract', 'N/A')[:500]}...")
    
    return "\n".join(lines)


def generate_literature_review(papers: List[dict], query: str) -> str:
    """Generate a simple literature review from papers."""
    lines = []
    lines.append(f"# Literature Review: {query}")
    lines.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d')}")
    lines.append(f"Total papers analyzed: {len(papers)}\n")
    
    lines.append("## Overview\n")
    lines.append(f"This review covers recent research on **{query}** based on {len(papers)} papers from arXiv.\n")
    
    # Group by date
    recent_papers = [p for p in papers if p.get('published', '').startswith('2025') or p.get('published', '').startswith('2026')]
    if recent_papers:
        lines.append(f"### Recent Papers (2025-2026): {len(recent_papers)}\n")
    
    lines.append("## Key Papers\n")
    
    for i, paper in enumerate(papers[:10], 1):
        lines.append(f"### {i}. {paper.get('title', 'N/A')}")
        lines.append(f"- **Authors:** {', '.join(paper.get('authors', [])[:3])}")
        if len(paper.get('authors', [])) > 3:
            lines.append(f"- ... and {len(paper['authors']) - 3} more")
        lines.append(f"- **Date:** {paper.get('published', 'N/A')}")
        lines.append(f"- **URL:** {paper.get('url', 'N/A')}")
        lines.append(f"- **Abstract:** {paper.get('abstract', 'N/A')[:300]}...")
        lines.append("")
    
    lines.append("\n## Research Trends\n")
    lines.append("Based on the analyzed papers, key research directions include:\n")
    
    # Simple trend analysis (could be improved with NLP)
    lines.append("- [Analyze abstracts to identify common themes]")
    lines.append("- [Identify emerging techniques and methodologies]")
    lines.append("- [Note gaps and future research opportunities]\n")
    
    lines.append("---\n")
    lines.append("*Generated using arXiv Research Skill*")
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Search arXiv papers (Free - No API key required!)")
    parser.add_argument("--query", "-q", help="Search query")
    parser.add_argument("--category", "-c", help="arXiv category (e.g., cs.AI, cs.LG)")
    parser.add_argument("--id", help="Comma-separated arXiv IDs")
    parser.add_argument("--max-results", "-n", type=int, default=10, help="Max results (default: 10)")
    parser.add_argument("--sort-by", choices=["relevance", "lastUpdatedDate", "submittedDate"], 
                       default="relevance", help="Sort order")
    parser.add_argument("--date-from", help="Date from (YYYY-MM-DD)")
    parser.add_argument("--output", "-o", help="Output file (generates literature review)")
    parser.add_argument("--format", choices=["text", "json", "markdown"], default="text",
                       help="Output format")
    
    args = parser.parse_args()
    
    # Validate inputs
    if not args.query and not args.category and not args.id:
        print("Error: Please provide --query, --category, or --id", file=sys.stderr)
        parser.print_help()
        sys.exit(1)
    
    # Parse IDs if provided
    paper_ids = None
    if args.id:
        paper_ids = [id.strip() for id in args.id.split(",")]
    
    # Search
    print(f"Searching arXiv...", file=sys.stderr)
    result = search_papers(
        query=args.query,
        category=args.category,
        paper_ids=paper_ids,
        max_results=args.max_results,
        sort_by=args.sort_by,
        date_from=args.date_from,
    )
    
    papers = result.get("papers", [])
    
    if not papers:
        print("No papers found.", file=sys.stderr)
        sys.exit(0)
    
    print(f"Found {len(papers)} papers\n", file=sys.stderr)
    
    # Output
    if args.output:
        # Generate literature review
        review = generate_literature_review(papers, args.query or "Research Topic")
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(review)
        print(f"Literature review saved to: {args.output}")
    elif args.format == "json":
        print(json.dumps(papers, indent=2, ensure_ascii=False))
    elif args.format == "markdown":
        for i, paper in enumerate(papers, 1):
            print(f"\n## [{i}] {paper.get('title', 'N/A')}")
            print(f"- **Authors:** {', '.join(paper.get('authors', []))}")
            print(f"- **Date:** {paper.get('published', 'N/A')}")
            print(f"- **URL:** {paper.get('url', 'N/A')}")
            print(f"- **Abstract:** {paper.get('abstract', 'N/A')[:400]}...")
    else:
        # Text format
        for i, paper in enumerate(papers, 1):
            print(format_paper(paper, i))


if __name__ == "__main__":
    main()
