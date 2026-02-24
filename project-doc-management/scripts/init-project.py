#!/usr/bin/env python3
"""
Initialize project documentation structure.
Usage: python init-project.py "Project Name"
"""

import os
import sys
from datetime import datetime

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates")

def read_template(name):
    path = os.path.join(TEMPLATES_DIR, name)
    with open(path, 'r') as f:
        return f.read()

def write_file(path, content):
    dir_path = os.path.dirname(path)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"  ✓ {path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python init-project.py \"Project Name\"")
        sys.exit(1)
    
    project_name = sys.argv[1]
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    print(f"\nInitializing project documentation for: {project_name}\n")
    
    # Check existing
    if os.path.exists("AGENTS.md"):
        print("⚠️  AGENTS.md already exists.")
        response = input("   Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("   Cancelled.")
            sys.exit(0)
        print()
    
    # Create AGENTS.md
    agents_content = read_template("agents-md-template.md")
    agents_content = agents_content.replace("{PROJECT_NAME}", project_name)
    agents_content = agents_content.replace("{DATE}", date_str)
    write_file("AGENTS.md", agents_content)
    
    # Create docs/requirements.md
    req_content = read_template("requirements-md-template.md")
    write_file("docs/requirements.md", req_content)
    
    # Create docs/ architecture.md
    arch_content = read_template("architecture-md-template.md")
    write_file("docs/architecture.md", arch_content)
    
    # Create docs/archive/ for lifecycle management
    write_file("docs/archive/.gitkeep", """# Archive Directory
# Purpose: Store historical documents and old versions
# Documents here are kept for reference but not part of active development
""")
    
    write_file("docs/archive/reference/.gitkeep", """# Reference Archive
# Purpose: Store stable reference documents that are no longer actively updated
# Examples: old architecture versions, completed API specs
""")
    
    # Create empty but documented directories
    # guides/ - reserved for user guides
    write_file("docs/guides/.gitkeep", """# Reserved for user guides and tutorials
# Status: Currently empty
# Planned: Add getting_started.md, advanced_usage.md when needed
# Naming: Use snake_case: getting_started.md (not getting-started.md)
""")
    
    # references/ - reserved for API references
    write_file("docs/references/.gitkeep", """# Reserved for API reference documentation
# Status: Currently empty  
# Planned: Add api_reference.md, configuration_guide.md when needed
# Naming: Use snake_case: api_reference.md (not api-reference.md)
""")
    
    # decisions/ - reserved for architecture decision records
    write_file("docs/decisions/.gitkeep", """# Reserved for Architecture Decision Records (ADRs)
# Status: Currently empty
# Usage: Add adr_XXX_description.md for major architectural decisions
# Naming: adr_001_database_choice.md, adr_002_caching_strategy.md
#         (snake_case for project documents)
""")
    
    # Create notes/ directory with an example note
    write_file(f"notes/{date_str}-getting-started.md", f"""# Getting Started

**Project**: {project_name}  
**Date**: {date_str}

## Initial Thoughts
[Document your initial thoughts, decisions, and plans here]

## Key Decisions
- Decision 1: [Why you chose X over Y]
- Decision 2: [Rationale]

## Open Questions
- [Question 1]
- [Question 2]

---
*This is an example note. Create new notes with format: YYYY-MM-DD-brief-description.md*
""")
    
    print(f"\n✅ Project '{project_name}' initialized successfully.\n")
    print("📁 Structure created:")
    print("   AGENTS.md              - Project dashboard with Quick Start section")
    print("   docs/requirements.md   - Original requirements (long-term)")
    print("   docs/architecture.md   - System design (long-term)")
    print("   docs/archive/          - For completed/archived documents")
    print("   docs/guides/.gitkeep   - Reserved for user guides (documented)")
    print("   docs/references/.gitkeep - Reserved for API docs (documented)")
    print("   docs/decisions/.gitkeep  - Reserved for ADRs (documented)")
    print("   notes/                 - Thinking process (temporary)")
    print("\n📋 Naming Convention:")
    print("   Standard files: README.md, AGENTS.md (uppercase)")
    print("   Project docs: requirements.md, api_reference.md (snake_case)")
    print("   ❌ Avoid: Requirements.md, api-reference.md, apiReference.md")
    print("\n📝 Next steps:")
    print("   1. Edit docs/requirements.md with your project goals")
    print("   2. Edit AGENTS.md status sections")
    print("   3. Start developing")
    print("\n💡 Remember:")
    print("   - Say 'checkpoint' to check project status")
    print("   - Say 'save progress' to update AGENTS.md")
    print("   - Create notes/YYYY-MM-DD-brief_description.md for thinking")
    print("   - Review documents monthly: archive old, delete temp notes")

if __name__ == "__main__":
    main()
