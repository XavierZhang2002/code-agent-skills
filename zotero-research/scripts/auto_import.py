#!/usr/bin/env python3
"""
Zotero 自动导入工具
将 arXiv 搜索结果自动导入 Zotero

使用方法:
    python3 auto_import.py --arxiv-id 2401.12345
    python3 auto_import.py --query "multi-agent RL" --max-results 5
"""

import argparse
import urllib.request
import urllib.parse
import json
import os
import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Optional


def get_zotero_profile_dir() -> Optional[str]:
    """获取 Zotero 配置目录"""
    home = Path.home()
    
    if sys.platform == "darwin":  # macOS
        zotero_dir = home / "Library/Application Support/Zotero"
        if zotero_dir.exists():
            # 读取 profiles.ini 找到默认配置
            profiles_ini = zotero_dir / "profiles.ini"
            if profiles_ini.exists():
                with open(profiles_ini) as f:
                    for line in f:
                        if line.startswith("Path="):
                            return str(zotero_dir / line.strip().replace("Path=", ""))
    
    return None


def create_zotero_import_file(papers: List[Dict], output_path: str):
    """
    创建 Zotero 可导入的 RDF/CSL JSON 文件
    
    Zotero 支持导入格式:
    - RDF (zotero.rdf)
    - CSL JSON
    - BibTeX
    - RIS
    """
    
    # 使用 CSL JSON 格式 (Zotero 原生支持)
    csl_items = []
    
    for paper in papers:
        # 解析作者
        authors = []
        for author in paper.get('authors', []):
            parts = author.split()
            if len(parts) > 1:
                authors.append({
                    "family": parts[-1],
                    "given": " ".join(parts[:-1])
                })
            else:
                authors.append({"family": author, "given": ""})
        
        # 构建 CSL 条目
        item = {
            "id": paper.get('id', ''),
            "type": "article-journal",
            "title": paper.get('title', ''),
            "author": authors,
            "abstract": paper.get('abstract', ''),
            "URL": paper.get('url', ''),
            "issued": {
                "date-parts": [[int(paper.get('published', '2024')[:4])]]
            } if paper.get('published') else {}
        }
        
        csl_items.append(item)
    
    # 保存为 CSL JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(csl_items, f, indent=2, ensure_ascii=False)
    
    return output_path


def fetch_arxiv_papers(query: Optional[str] = None, arxiv_id: Optional[str] = None, 
                       max_results: int = 10) -> List[Dict]:
    """从 arXiv 获取论文元数据"""
    
    if arxiv_id:
        # 获取特定论文
        url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    elif query:
        # 搜索论文
        encoded_query = urllib.parse.quote(query)
        url = f"http://export.arxiv.org/api/query?search_query=all:{encoded_query}&max_results={max_results}"
    else:
        return []
    
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        
        with urllib.request.urlopen(req, timeout=30) as response:
            xml_data = response.read().decode('utf-8')
            return parse_arxiv_xml(xml_data)
            
    except Exception as e:
        print(f"Error fetching from arXiv: {e}", file=sys.stderr)
        return []


def parse_arxiv_xml(xml_data: str) -> List[Dict]:
    """解析 arXiv API XML 响应"""
    import xml.etree.ElementTree as ET
    
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_data)
    
    papers = []
    for entry in root.findall("atom:entry", ns):
        paper = {}
        
        # ID
        id_elem = entry.find("atom:id", ns)
        if id_elem is not None:
            paper["id"] = id_elem.text.split("/")[-1]
            paper["url"] = f"https://arxiv.org/abs/{paper['id']}"
            paper["pdf_url"] = f"https://arxiv.org/pdf/{paper['id']}.pdf"
        
        # Title
        title_elem = entry.find("atom:title", ns)
        if title_elem is not None:
            paper["title"] = title_elem.text.strip().replace("\n", " ") if title_elem.text else ""
        
        # Summary
        summary_elem = entry.find("atom:summary", ns)
        if summary_elem is not None:
            paper["abstract"] = summary_elem.text.strip() if summary_elem.text else ""
        
        # Authors
        authors = []
        for author in entry.findall("atom:author", ns):
            name_elem = author.find("atom:name", ns)
            if name_elem is not None:
                authors.append(name_elem.text)
        paper["authors"] = authors
        
        # Date
        published_elem = entry.find("atom:published", ns)
        if published_elem is not None:
            paper["published"] = published_elem.text[:10]
        
        papers.append(paper)
    
    return papers


def open_in_zotero(import_file: str):
    """
    在 Zotero 中打开导入文件
    
    注意: Zotero 需要安装并运行
    """
    # macOS
    if sys.platform == "darwin":
        zotero_app = "/Applications/Zotero.app"
        if os.path.exists(zotero_app):
            subprocess.run(["open", "-a", "Zotero", import_file])
            return True
    
    # Linux
    elif sys.platform.startswith("linux"):
        subprocess.run(["xdg-open", import_file])
        return True
    
    # Windows
    elif sys.platform == "win32":
        os.startfile(import_file)
        return True
    
    return False


def generate_bibtex(papers: List[Dict]) -> str:
    """生成 BibTeX 格式"""
    entries = []
    
    for paper in papers:
        # 生成 cite key
        first_author = paper.get('authors', ['Unknown'])[0].split()[-1] if paper.get('authors') else 'Unknown'
        year = paper.get('published', '2024')[:4]
        cite_key = f"{first_author}{year}"
        
        entry = f"@article{{{cite_key},\n"
        entry += f"  title = {{{paper.get('title', '')}}},\n"
        
        if paper.get('authors'):
            authors = ' and '.join(paper['authors'])
            entry += f"  author = {{{authors}}},\n"
        
        entry += f"  year = {{{year}}},\n"
        entry += f"  url = {{{paper.get('url', '')}}},\n"
        entry += f"  abstract = {{{paper.get('abstract', '')}}},\n"
        entry += "}\n"
        
        entries.append(entry)
    
    return "\n".join(entries)


def main():
    parser = argparse.ArgumentParser(description="自动导入 arXiv 论文到 Zotero")
    
    # 输入选项
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--arxiv-id", help="arXiv ID (如: 2401.12345)")
    group.add_argument("--query", "-q", help="搜索关键词")
    group.add_argument("--file", "-f", help="包含 arXiv ID 列表的文件")
    
    # 其他选项
    parser.add_argument("--max-results", "-n", type=int, default=5, 
                       help="最大结果数 (默认: 5)")
    parser.add_argument("--output", "-o", help="输出文件路径")
    parser.add_argument("--format", choices=["csl", "bibtex"], default="csl",
                       help="输出格式 (默认: csl)")
    parser.add_argument("--open", action="store_true", 
                       help="自动在 Zotero 中打开")
    parser.add_argument("--download-pdf", action="store_true",
                       help="同时下载 PDF 文件 (需要配置)")
    
    args = parser.parse_args()
    
    print("🔍 获取论文元数据...")
    
    # 获取论文
    if args.arxiv_id:
        papers = fetch_arxiv_papers(arxiv_id=args.arxiv_id)
    elif args.query:
        papers = fetch_arxiv_papers(query=args.query, max_results=args.max_results)
    elif args.file:
        # 从文件读取 arXiv ID 列表
        with open(args.file) as f:
            ids = [line.strip() for line in f if line.strip()]
        papers = []
        for arxiv_id in ids:
            paper = fetch_arxiv_papers(arxiv_id=arxiv_id)
            papers.extend(paper)
    else:
        print("错误: 请指定 --arxiv-id, --query 或 --file", file=sys.stderr)
        sys.exit(1)
    
    if not papers:
        print("未找到论文")
        sys.exit(0)
    
    print(f"✅ 找到 {len(papers)} 篇论文")
    
    # 显示论文列表
    for i, paper in enumerate(papers, 1):
        print(f"  {i}. {paper.get('title', 'N/A')[:60]}...")
    
    # 确定输出文件
    if args.output:
        output_path = args.output
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"zotero_import_{timestamp}.{args.format}"
    
    # 生成导入文件
    print(f"\n📝 生成导入文件: {output_path}")
    
    if args.format == "csl":
        create_zotero_import_file(papers, output_path)
    elif args.format == "bibtex":
        bibtex = generate_bibtex(papers)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(bibtex)
    
    print(f"✅ 文件已保存: {os.path.abspath(output_path)}")
    
    # 提供导入说明
    print("\n📖 导入到 Zotero 的方法:")
    print("  方法 1: 直接双击文件 (如果 Zotero 是默认程序)")
    print("  方法 2: Zotero → 文件 → 导入 → 选择此文件")
    print("  方法 3: 拖拽文件到 Zotero 窗口")
    
    # 自动打开
    if args.open:
        print("\n🚀 正在尝试在 Zotero 中打开...")
        if open_in_zotero(output_path):
            print("✅ 已在 Zotero 中打开")
        else:
            print("⚠️ 无法自动打开，请手动导入")
    
    print(f"\n💡 提示: 可以使用以下命令导入")
    print(f"  python3 {sys.argv[0]} --open {output_path}")


if __name__ == "__main__":
    from datetime import datetime
    main()
