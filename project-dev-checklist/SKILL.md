---
name: project-dev-checklist
description: |
  Development environment and testing checklist for Python projects.
  Use when setting up dev environment, before committing, or verifying testing coverage.
  Tracks: Python version, dependency management, test execution, test environment setup.
  Triggers: "dev checklist", "env check", "test check", "version check", "setup dev", 
            "run tests", "testing setup", "commit ready", "pre-commit check".
---

# Project Development Checklist

## Environment Verification

### Python Version
```markdown
Required Python: [from pyproject.toml or README]
Current Python: [run python --version]
Status: ✅ Match / ❌ Mismatch
```

### Virtual Environment
```markdown
- [ ] venv/conda activated? (which python shows venv path)
- [ ] .venv/ or env/ in .gitignore?
- [ ] pip list shows expected packages?
```

### Dependencies
```markdown
Install command: pip install -e ".[dev]" or pip install -r requirements-dev.txt
- [ ] Package imports without error? (python -c "import pkg_name")
- [ ] CLI entry points work? (if applicable)
- [ ] Development tools installed? (pytest, black, etc.)
```

---

## Testing Checklist

### Test Execution
```markdown
Test runner: pytest / unittest
Run command: pytest tests/ -v

Before committing:
- [ ] All existing tests pass?
- [ ] New tests added for new features?
- [ ] Test coverage acceptable? (if tracked)
```

### Test Environment
```markdown
Test configuration: [pytest.ini, pyproject.toml, or conftest.py]
- [ ] Test database configured? (if needed)
- [ ] Mock external services? (APIs, files)
- [ ] Test fixtures up to date?
```

### Test Records (Update in AGENTS.md)
```markdown
## Testing Status (Last run: YYYY-MM-DD)

| Test Suite | Status | Coverage | Notes |
|------------|--------|----------|-------|
| Unit tests | ✅ Pass | 85% | Core modules |
| Integration | ⚠️ Skip | N/A | Requires API key |
| E2E tests | ❌ Fail | - | Known issue #123 |

Known test gaps:
- [ ] Error handling paths
- [ ] Edge cases for large inputs
- [ ] Concurrent access scenarios
```

---

## Version Management

### Package Version
```markdown
Current version: [from __version__ or pyproject.toml]
Version format: semver (MAJOR.MINOR.PATCH)

Before release:
- [ ] Version bumped appropriately?
- [ ] CHANGELOG.md updated?
- [ ] Git tag created? (git tag v1.2.3)
```

### API Version (if applicable)
```markdown
API version: v1 / v2
Breaking changes: None / Documented
- [ ] Deprecation warnings added?
- [ ] Migration guide provided?
- [ ] Backward compatibility maintained?
```

### Dependency Versions
```markdown
Key dependencies:
- package_a: >=1.0,<2.0 (constrained)
- package_b: ^2.1.0 (caret)

Checks:
- [ ] No unpinned dependencies?
- [ ] Security vulnerabilities checked? (pip-audit)
- [ ] Compatible with downstream projects?
```

---

## Pre-Commit Checklist

### Code Quality
```markdown
If project has linting configured:
- [ ] Formatter run? (black/ruff format)
- [ ] Linter clean? (ruff/flake8)
- [ ] Type checker pass? (mypy/pyright)

Quick check: ruff check src/ && mypy src/
```

### Debug Code Removal
```markdown
Search for:
- [ ] print() statements (not in CLI code)
- [ ] import pdb; pdb.set_trace()
- [ ] TODO/FIXME comments (should be issues)
- [ ] Hardcoded paths or credentials
```

### Secrets Check
```markdown
Scan for accidental commits:
- [ ] API keys (sk-*, AKIA*, etc.)
- [ ] Passwords or tokens
- [ ] Private keys
- [ ] Internal URLs/IPs

Tools: git-secrets, detect-secrets
```

---

## Development Environment Records

Record in AGENTS.md:

```markdown
## Development Environment

**Setup verified**: 2026-02-24
**Python**: 3.10+ (tested on 3.10.12)
**Package manager**: pip + venv
**Install**: `pip install -e ".[dev]"`

### Required Tools
| Tool | Purpose | Install |
|------|---------|---------|
| pytest | Testing | pip install pytest pytest-asyncio |
| ruff | Lint/format | pip install ruff |
| mypy | Type check | pip install mypy |

### Test Execution
```bash
# Run all tests
pytest tests/ -v

# Run specific test
pytest tests/test_core.py -v -k test_name

# With coverage
pytest tests/ --cov=src/pkg_name
```

### Known Issues
- Integration tests require OPENAI_API_KEY
- Some tests are slow (marked with @pytest.mark.slow)
```

---

## Downstream Compatibility

If modifying shared libraries:

```markdown
Downstream projects:
- [ ] Tested with openmanus_long_agent?
- [ ] API changes communicated?
- [ ] Migration guide provided (if breaking)?
```

---

## Quick Commands

```bash
# Full environment check
"env check" → Show environment verification

# Testing
"test check" → Show testing checklist
"run tests" → Remind how to run tests

# Before commit
"commit ready" → Show pre-commit checks

# Version
"version check" → Show version management
```

---

## Integration with Document Management

This skill complements `project-doc-management`:

1. **Start session**: 
   - `project-doc-management` → Read AGENTS.md
   - `project-dev-checklist` → Verify environment

2. **During development**:
   - `project-dev-checklist` → Remind to run tests

3. **Before commit**:
   - `project-dev-checklist` → Quality checks
   - Update AGENTS.md Testing Status

4. **End session**:
   - `project-doc-management` → Update AGENTS.md

---

## Recording Template

When user asks to "record dev status", create this in AGENTS.md:

```markdown
## Development Status (Updated: YYYY-MM-DD)

### Environment
- Python: 3.10.12
- venv: .venv/
- Install: pip install -e ".[dev]"

### Testing
- Unit tests: ✅ 45/45 pass
- Integration: ⚠️ 2 skipped (need API key)
- Coverage: 82%

### Version
- Current: 0.1.0
- Next planned: 0.2.0

### Blockers
- None / [describe]
```
