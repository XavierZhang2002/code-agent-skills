#!/usr/bin/env python3
"""
Zotero Local Library Search Tool
Direct access to Zotero SQLite database - no API keys needed!
"""

import argparse
import sqlite3
import json
import sys
import os
import shutil
import tempfile
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple


def find_zotero_database() -> Optional[str]:
    """Find Zotero SQLite database path based on OS."""
    home = Path.home()
    
    # macOS
    if sys.platform == "darwin":
        zotero_dir = home / "Library/Application Support/Zotero"
        if zotero_dir.exists():
            # Find profile directories
            for profile_dir in zotero_dir.glob("Profiles/*"):
                db_path = profile_dir / "zotero.sqlite"
                if db_path.exists():
                    return str(db_path)
    
    # Linux
    elif sys.platform.startswith("linux"):
        zotero_dir = home / ".zotero/zotero"
        if zotero_dir.exists():
            for profile_dir in zotero_dir.glob("*"):
                db_path = profile_dir / "zotero.sqlite"
                if db_path.exists():
                    return str(db_path)
    
    # Windows
    elif sys.platform == "win32":
        appdata = os.environ.get("APPDATA")
        if appdata:
            zotero_dir = Path(appdata) / "Zotero/Zotero"
            if zotero_dir.exists():
                for profile_dir in zotero_dir.glob("Profiles/*"):
                    db_path = profile_dir / "zotero.sqlite"
                    if db_path.exists():
                        return str(db_path)
    
    return None


class ZoteroLibrary:
    """Interface to Zotero SQLite database."""
    
    def __init__(self, db_path: Optional[str] = None, copy_db: bool = False):
        self.original_db = db_path or find_zotero_database()
        if not self.original_db:
            raise FileNotFoundError(
                "Could not find Zotero database. "
                "Make sure Zotero is installed and has been run at least once."
            )
        
        self.copy_db = copy_db
        self.temp_db = None
        
        if copy_db:
            # Create temporary copy to avoid locking issues
            self.temp_db = tempfile.mktemp(suffix=".sqlite")
            shutil.copy2(self.original_db, self.temp_db)
            self.conn = sqlite3.connect(self.temp_db)
        else:
            self.conn = sqlite3.connect(self.original_db)
        
        self.conn.row_factory = sqlite3.Row
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    
    def close(self):
        """Close database connection and cleanup."""
        if self.conn:
            self.conn.close()
        if self.temp_db and os.path.exists(self.temp_db):
            os.remove(self.temp_db)
    
    def search_items(
        self,
        query: Optional[str] = None,
        author: Optional[str] = None,
        tag: Optional[str] = None,
        collection: Optional[str] = None,
        item_type: Optional[str] = None,
        since: Optional[str] = None,
        fulltext: bool = False,
        limit: int = 20
    ) -> List[Dict]:
        """Search items with various filters."""
        
        # Build query
        conditions = ["i.itemTypeID != 14"]  # Exclude attachments
        params = []
        
        if query:
            if fulltext:
                conditions.append("""
                    (idv.value LIKE ? OR 
                     EXISTS (SELECT 1 FROM itemNotes n 
                            WHERE n.parentItemID = i.itemID 
                            AND n.note LIKE ?))
                """)
                params.extend([f"%{query}%", f"%{query}%"])
            else:
                conditions.append("idv.value LIKE ?")
                params.append(f"%{query}%")
        
        if author:
            conditions.append("""
                EXISTS (SELECT 1 FROM creators c
                        JOIN itemCreators ic ON c.creatorID = ic.creatorID
                        WHERE ic.itemID = i.itemID
                        AND (c.firstName LIKE ? OR c.lastName LIKE ?))
            """)
            params.extend([f"%{author}%", f"%{author}%"])
        
        if tag:
            conditions.append("""
                EXISTS (SELECT 1 FROM tags t
                        JOIN itemTags it ON t.tagID = it.tagID
                        WHERE it.itemID = i.itemID
                        AND t.name LIKE ?)
            """)
            params.append(f"%{tag}%")
        
        if collection:
            conditions.append("""
                EXISTS (SELECT 1 FROM collections c
                        JOIN collectionItems ci ON c.collectionID = ci.collectionID
                        WHERE ci.itemID = i.itemID
                        AND c.collectionName LIKE ?)
            """)
            params.append(f"%{collection}%")
        
        if since:
            conditions.append("i.dateAdded >= ?")
            params.append(since)
        
        if item_type:
            conditions.append("""
                EXISTS (SELECT 1 FROM itemTypes itt
                        WHERE i.itemTypeID = itt.itemTypeID
                        AND itt.typeName = ?)
            """)
            params.append(item_type)
        
        where_clause = " AND ".join(conditions)
        
        sql = f"""
            SELECT DISTINCT
                i.itemID,
                idv.value as title,
                i.dateAdded,
                i.dateModified,
                it.typeName as itemType
            FROM items i
            JOIN itemData id ON i.itemID = id.itemID
            JOIN itemDataValues idv ON id.valueID = idv.valueID
            JOIN fields f ON id.fieldID = f.fieldID
            JOIN itemTypes it ON i.itemTypeID = it.itemTypeID
            WHERE f.fieldName = 'title'
            AND {where_clause}
            ORDER BY i.dateAdded DESC
            LIMIT ?
        """
        params.append(limit)
        
        cursor = self.conn.execute(sql, params)
        items = []
        
        for row in cursor.fetchall():
            item = dict(row)
            item['authors'] = self.get_item_authors(row['itemID'])
            item['tags'] = self.get_item_tags(row['itemID'])
            item['collections'] = self.get_item_collections(row['itemID'])
            item['url'] = self.get_item_url(row['itemID'])
            item['abstract'] = self.get_item_abstract(row['itemID'])
            items.append(item)
        
        return items
    
    def get_item_authors(self, item_id: int) -> List[str]:
        """Get authors for an item."""
        cursor = self.conn.execute("""
            SELECT c.firstName, c.lastName
            FROM creators c
            JOIN itemCreators ic ON c.creatorID = ic.creatorID
            WHERE ic.itemID = ?
            ORDER BY ic.orderIndex
        """, (item_id,))
        
        authors = []
        for row in cursor.fetchall():
            if row['firstName']:
                authors.append(f"{row['firstName']} {row['lastName']}")
            else:
                authors.append(row['lastName'])
        return authors
    
    def get_item_tags(self, item_id: int) -> List[str]:
        """Get tags for an item."""
        cursor = self.conn.execute("""
            SELECT t.name
            FROM tags t
            JOIN itemTags it ON t.tagID = it.tagID
            WHERE it.itemID = ?
        """, (item_id,))
        
        return [row['name'] for row in cursor.fetchall()]
    
    def get_item_collections(self, item_id: int) -> List[str]:
        """Get collections an item belongs to."""
        cursor = self.conn.execute("""
            SELECT c.collectionName
            FROM collections c
            JOIN collectionItems ci ON c.collectionID = ci.collectionID
            WHERE ci.itemID = ?
        """, (item_id,))
        
        return [row['collectionName'] for row in cursor.fetchall()]
    
    def get_item_url(self, item_id: int) -> Optional[str]:
        """Get URL for an item."""
        cursor = self.conn.execute("""
            SELECT idv.value
            FROM itemData id
            JOIN itemDataValues idv ON id.valueID = idv.valueID
            JOIN fields f ON id.fieldID = f.fieldID
            WHERE id.itemID = ?
            AND f.fieldName = 'url'
        """, (item_id,))
        
        row = cursor.fetchone()
        return row['value'] if row else None
    
    def get_item_abstract(self, item_id: int) -> Optional[str]:
        """Get abstract for an item."""
        cursor = self.conn.execute("""
            SELECT idv.value
            FROM itemData id
            JOIN itemDataValues idv ON id.valueID = idv.valueID
            JOIN fields f ON id.fieldID = f.fieldID
            WHERE id.itemID = ?
            AND f.fieldName = 'abstractNote'
        """, (item_id,))
        
        row = cursor.fetchone()
        return row['value'] if row else None
    
    def get_collections(self) -> List[Dict]:
        """Get all collections."""
        cursor = self.conn.execute("""
            SELECT collectionID, collectionName, parentCollectionID
            FROM collections
            ORDER BY collectionName
        """)
        
        return [dict(row) for row in cursor.fetchall()]
    
    def get_tags(self) -> List[str]:
        """Get all tags."""
        cursor = self.conn.execute("""
            SELECT name FROM tags ORDER BY name
        """)
        
        return [row['name'] for row in cursor.fetchall()]
    
    def get_item_notes(self, item_id: int) -> List[Dict]:
        """Get notes/annotations for an item."""
        cursor = self.conn.execute("""
            SELECT note, dateAdded
            FROM itemNotes
            WHERE parentItemID = ?
            ORDER BY dateAdded DESC
        """, (item_id,))
        
        return [dict(row) for row in cursor.fetchall()]
    
    def get_statistics(self) -> Dict:
        """Get library statistics."""
        stats = {}
        
        # Total items
        cursor = self.conn.execute("""
            SELECT COUNT(*) FROM items WHERE itemTypeID != 14
        """)
        stats['total_items'] = cursor.fetchone()[0]
        
        # Items by type
        cursor = self.conn.execute("""
            SELECT it.typeName, COUNT(*) as count
            FROM items i
            JOIN itemTypes it ON i.itemTypeID = it.itemTypeID
            WHERE i.itemTypeID != 14
            GROUP BY it.typeName
            ORDER BY count DESC
        """)
        stats['by_type'] = {row['typeName']: row['count'] for row in cursor.fetchall()}
        
        # Total collections
        cursor = self.conn.execute("SELECT COUNT(*) FROM collections")
        stats['total_collections'] = cursor.fetchone()[0]
        
        # Total tags
        cursor = self.conn.execute("SELECT COUNT(*) FROM tags")
        stats['total_tags'] = cursor.fetchone()[0]
        
        return stats


def format_item(item: Dict, index: int) -> str:
    """Format an item for display."""
    lines = []
    lines.append(f"\n{'='*80}")
    lines.append(f"[{index}] {item.get('title', 'N/A')}")
    lines.append(f"{'='*80}")
    
    if item.get('authors'):
        lines.append(f"Authors: {', '.join(item['authors'][:5])}")
        if len(item['authors']) > 5:
            lines.append(f"        ... and {len(item['authors']) - 5} more")
    
    if item.get('itemType'):
        lines.append(f"Type: {item['itemType']}")
    
    if item.get('dateAdded'):
        lines.append(f"Added: {item['dateAdded']}")
    
    if item.get('collections'):
        lines.append(f"Collections: {', '.join(item['collections'][:3])}")
    
    if item.get('tags'):
        tag_str = ', '.join(item['tags'][:10])
        if len(item['tags']) > 10:
            tag_str += f" ... ({len(item['tags']) - 10} more)"
        lines.append(f"Tags: {tag_str}")
    
    if item.get('url'):
        lines.append(f"URL: {item['url']}")
    
    if item.get('abstract'):
        abstract = item['abstract'][:500] + "..." if len(item['abstract']) > 500 else item['abstract']
        lines.append(f"\nAbstract:\n{abstract}")
    
    return "\n".join(lines)


def generate_literature_review(items: List[Dict], query: str) -> str:
    """Generate a literature review from items."""
    lines = []
    lines.append(f"# Literature Review: {query}")
    lines.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"Source: Zotero Personal Library")
    lines.append(f"Papers analyzed: {len(items)}\n")
    
    lines.append("## Overview\n")
    lines.append(f"This review covers papers from your Zotero library related to **{query}**.\n")
    
    # Group by year
    by_year = {}
    for item in items:
        year = item.get('dateAdded', 'Unknown')[:4] if item.get('dateAdded') else 'Unknown'
        by_year.setdefault(year, []).append(item)
    
    if by_year:
        lines.append("### Papers by Year\n")
        for year in sorted(by_year.keys(), reverse=True):
            lines.append(f"- {year}: {len(by_year[year])} papers")
        lines.append("")
    
    lines.append("## Key Papers\n")
    
    for i, item in enumerate(items[:20], 1):
        lines.append(f"### {i}. {item.get('title', 'N/A')}")
        
        if item.get('authors'):
            lines.append(f"- **Authors:** {', '.join(item['authors'][:3])}")
            if len(item['authors']) > 3:
                lines.append(f"- ... and {len(item['authors']) - 3} more")
        
        if item.get('dateAdded'):
            lines.append(f"- **Date:** {item['dateAdded'][:10]}")
        
        if item.get('url'):
            lines.append(f"- **URL:** {item['url']}")
        
        if item.get('tags'):
            lines.append(f"- **Tags:** {', '.join(item['tags'][:5])}")
        
        if item.get('abstract'):
            abstract = item['abstract'][:300] + "..." if len(item['abstract']) > 300 else item['abstract']
            lines.append(f"- **Abstract:** {abstract}")
        
        lines.append("")
    
    lines.append("\n---\n")
    lines.append("*Generated by Zotero Research Skill*")
    
    return "\n".join(lines)


def export_bibtex(items: List[Dict]) -> str:
    """Export items to BibTeX format."""
    entries = []
    
    for item in items:
        key = f"{item.get('authors', ['Unknown'])[0].split()[-1] if item.get('authors') else 'Unknown'}{item.get('dateAdded', '2024')[:4]}"
        entry = f"@article{{{key},\n"
        entry += f"  title = {{{item.get('title', '')}}},\n"
        
        if item.get('authors'):
            authors = ' and '.join(item['authors'])
            entry += f"  author = {{{authors}}},\n"
        
        if item.get('dateAdded'):
            entry += f"  year = {{{item['dateAdded'][:4]}}},\n"
        
        if item.get('url'):
            entry += f"  url = {{{item['url']}}},\n"
        
        entry += "}\n"
        entries.append(entry)
    
    return "\n".join(entries)


def main():
    parser = argparse.ArgumentParser(
        description="Search your Zotero library (offline, no API keys needed!)"
    )
    
    # Search options
    parser.add_argument("--query", "-q", help="Search query")
    parser.add_argument("--author", "-a", help="Search by author")
    parser.add_argument("--tag", "-t", help="Search by tag")
    parser.add_argument("--collection", "-c", help="Search in collection")
    parser.add_argument("--item-type", help="Item type (journalArticle, book, etc.)")
    parser.add_argument("--since", help="Only items added since date (YYYY-MM-DD)")
    
    # Display options
    parser.add_argument("--limit", "-n", type=int, default=20, help="Maximum results")
    parser.add_argument("--fulltext", action="store_true", help="Include notes in search")
    parser.add_argument("--format", choices=["text", "json", "markdown"], default="text")
    
    # Actions
    parser.add_argument("--collections", action="store_true", help="List all collections")
    parser.add_argument("--tags", action="store_true", help="List all tags")
    parser.add_argument("--stats", action="store_true", help="Show library statistics")
    parser.add_argument("--item-key", help="Get specific item by ID")
    parser.add_argument("--annotations", action="store_true", help="Show item annotations")
    
    # Output
    parser.add_argument("--output", "-o", help="Output file")
    parser.add_argument("--export", choices=["bibtex"], help="Export format")
    parser.add_argument("--copy-db", action="store_true", help="Copy DB to avoid locking")
    parser.add_argument("--db-path", help="Path to Zotero SQLite database (optional)")
    
    args = parser.parse_args()
    
    try:
        with ZoteroLibrary(db_path=args.db_path, copy_db=args.copy_db) as zotero:
            
            # List collections
            if args.collections:
                collections = zotero.get_collections()
                print(f"\n{'='*60}")
                print("Collections in your Zotero library:")
                print(f"{'='*60}")
                for coll in collections:
                    print(f"  - {coll['collectionName']}")
                print(f"\nTotal: {len(collections)} collections")
                return
            
            # List tags
            if args.tags:
                tags = zotero.get_tags()
                print(f"\n{'='*60}")
                print("Tags in your Zotero library:")
                print(f"{'='*60}")
                for tag in tags:
                    print(f"  - {tag}")
                print(f"\nTotal: {len(tags)} tags")
                return
            
            # Show statistics
            if args.stats:
                stats = zotero.get_statistics()
                print(f"\n{'='*60}")
                print("Zotero Library Statistics:")
                print(f"{'='*60}")
                print(f"Total Items: {stats['total_items']}")
                print(f"Collections: {stats['total_collections']}")
                print(f"Tags: {stats['total_tags']}")
                print("\nItems by Type:")
                for item_type, count in list(stats['by_type'].items())[:10]:
                    print(f"  - {item_type}: {count}")
                return
            
            # Search
            if args.query or args.author or args.tag or args.collection:
                items = zotero.search_items(
                    query=args.query,
                    author=args.author,
                    tag=args.tag,
                    collection=args.collection,
                    item_type=args.item_type,
                    since=args.since,
                    fulltext=args.fulltext,
                    limit=args.limit
                )
                
                if not items:
                    print("No items found matching your criteria.")
                    return
                
                # Export
                if args.export == "bibtex":
                    output = export_bibtex(items)
                    if args.output:
                        with open(args.output, 'w') as f:
                            f.write(output)
                        print(f"Exported {len(items)} items to {args.output}")
                    else:
                        print(output)
                    return
                
                # Generate literature review
                if args.output and args.output.endswith('.md'):
                    review = generate_literature_review(items, args.query or "Research")
                    with open(args.output, 'w') as f:
                        f.write(review)
                    print(f"Literature review saved to: {args.output}")
                    print(f"Analyzed {len(items)} papers")
                    return
                
                # Display results
                if args.format == "json":
                    output = json.dumps(items, indent=2, ensure_ascii=False)
                    if args.output:
                        with open(args.output, 'w') as f:
                            f.write(output)
                        print(f"Saved {len(items)} items to {args.output}")
                    else:
                        print(output)
                
                elif args.format == "markdown":
                    lines = [f"# Search Results: {args.query or 'All Items'}\n"]
                    for i, item in enumerate(items, 1):
                        lines.append(f"## [{i}] {item.get('title', 'N/A')}")
                        if item.get('authors'):
                            lines.append(f"**Authors:** {', '.join(item['authors'][:3])}")
                        if item.get('url'):
                            lines.append(f"**URL:** {item['url']}")
                        lines.append("")
                    output = "\n".join(lines)
                    
                    if args.output:
                        with open(args.output, 'w') as f:
                            f.write(output)
                        print(f"Saved to {args.output}")
                    else:
                        print(output)
                
                else:  # text format
                    print(f"\nFound {len(items)} items:\n")
                    for i, item in enumerate(items, 1):
                        print(format_item(item, i))
                    
                    print(f"\n{'='*80}")
                    print(f"Showing {len(items)} results")
                    print(f"{'='*80}")
            
            else:
                parser.print_help()
    
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        print("\nTroubleshooting:", file=sys.stderr)
        print("1. Make sure Zotero is installed", file=sys.stderr)
        print("2. Run Zotero at least once to create the database", file=sys.stderr)
        print("3. If Zotero is running, try using --copy-db flag", file=sys.stderr)
        sys.exit(1)
    
    except sqlite3.OperationalError as e:
        if "locked" in str(e).lower():
            print(f"Error: Zotero database is locked.", file=sys.stderr)
            print("Please close Zotero desktop app and try again.", file=sys.stderr)
            print("Or use --copy-db flag to create a temporary copy.", file=sys.stderr)
        else:
            print(f"Database error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
