#!/usr/bin/env python3
"""
Record development status to AGENTS.md
Usage: python record-dev-status.py
"""

import os
import sys
import subprocess
from datetime import datetime

def get_python_version():
    try:
        result = subprocess.run(['python', '--version'], capture_output=True, text=True)
        return result.stdout.strip() or result.stderr.strip()
    except:
        return "Unknown"

def get_package_version():
    """Try to get version from common locations"""
    # Try pyproject.toml
    if os.path.exists('pyproject.toml'):
        try:
            import tomllib
            with open('pyproject.toml', 'rb') as f:
                data = tomllib.load(f)
                return data.get('project', {}).get('version', 'Unknown')
        except:
            pass
    
    # Try __init__.py
    for root, dirs, files in os.walk('src'):
        if '__init__.py' in files:
            try:
                with open(os.path.join(root, '__init__.py')) as f:
                    for line in f:
                        if line.startswith('__version__'):
                            return line.split('=')[1].strip().strip('"\'')
            except:
                pass
    
    return "Unknown"

def check_tests():
    """Check if tests exist and can run"""
    if not os.path.exists('tests'):
        return "No tests/ directory found"
    
    try:
        result = subprocess.run(
            ['python', '-m', 'pytest', 'tests/', '--collect-only', '-q'],
            capture_output=True, text=True, timeout=30
        )
        lines = result.stdout.strip().split('\n')
        for line in lines:
            if 'test session starts' in line or 'collected' in line:
                return line
        return "Tests found"
    except Exception as e:
        return f"Couldn't collect: {e}"

def main():
    print("Recording development status...\n")
    
    # Gather info
    date_str = datetime.now().strftime("%Y-%m-%d")
    python_ver = get_python_version()
    pkg_ver = get_package_version()
    test_status = check_tests()
    
    # Print gathered info
    print(f"Date: {date_str}")
    print(f"Python: {python_ver}")
    print(f"Package version: {pkg_ver}")
    print(f"Tests: {test_status}")
    print()
    
    # Check if AGENTS.md exists
    if not os.path.exists("AGENTS.md"):
        print("⚠️  AGENTS.md not found. Please run this from project root.")
        print("   Or use 'project-doc-management' skill to initialize first.")
        sys.exit(1)
    
    # Read existing AGENTS.md
    with open("AGENTS.md", 'r') as f:
        content = f.read()
    
    # Check if Development Status section exists
    if "## Development Status" in content:
        print("⚠️  Development Status section already exists in AGENTS.md")
        response = input("   Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("   Cancelled.")
            sys.exit(0)
        # Remove old section
        import re
        content = re.sub(r'## Development Status.*?(?=##|$)', '', content, flags=re.DOTALL)
    
    # Add new section
    new_section = f"""## Development Status

**Last Updated**: {date_str}

### Environment
- Python: {python_ver}
- Package version: {pkg_ver}
- Test status: {test_status}

### Quick Commands
```bash
# Run tests
pytest tests/ -v

# Check code
ruff check src/ && mypy src/

# Format code
ruff format src/
```

---

"""
    
    # Insert before the first ##
    if "## " in content:
        first_section = content.find("## ")
        new_content = content[:first_section] + new_section + content[first_section:]
    else:
        new_content = content + "\n" + new_section
    
    # Write back
    with open("AGENTS.md", 'w') as f:
        f.write(new_content)
    
    print("✅ Development status recorded in AGENTS.md")
    print("\n📋 Next steps:")
    print("   1. Review the recorded information")
    print("   2. Fill in missing details (test coverage, known gaps)")
    print("   3. Update as development progresses")

if __name__ == "__main__":
    main()
