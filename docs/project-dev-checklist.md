# Project Development Checklist

## Overview

`project-dev-checklist` is a lightweight development checklist skill that helps developers record and manage development environment, test status, and version information without interfering with specific development workflows.

## Core Features

### 1. Environment Verification
- **Python Version**: Check if current Python version meets project requirements
- **Virtual Environment**: Confirm venv/conda is activated
- **Dependencies**: Verify all dependencies are correctly installed
- **Package Import Test**: Ensure project package can be imported normally

### 2. Test Management
- **Test Execution**: Record test run status and results
- **Coverage Tracking**: Track code coverage changes
- **Test Environment**: Record test configuration and environment requirements
- **Test Gaps**: Mark uncovered test scenarios

### 3. Version Management
- **Package Version**: Current version and release plans
- **API Compatibility**: Record API changes and compatibility
- **Dependency Constraints**: Dependency version management and security audit

### 4. Pre-Commit Checks
- **Code Quality**: Formatting, linting, type checking
- **Debug Code**: Check and remove print/pdb debug code
- **Security Scan**: Scan for API keys, passwords, and other sensitive info

## Recorded Checkpoints

### Pre-Development Check
```markdown
- [ ] Python version correct
- [ ] Virtual environment activated
- [ ] Dependencies installed
- [ ] Package imports correctly
- [ ] Read AGENTS.md
```

### During Development Check
```markdown
- [ ] Running tests frequently
- [ ] Following existing code patterns
- [ ] Dependencies properly added
```

### Pre-Commit Check
```markdown
- [ ] All tests passing
- [ ] No debug code残留
- [ ] No sensitive info leaked
- [ ] Code formatting completed
- [ ] AGENTS.md updated
```

## Development Status Recording

Running `record-dev-status.py` automatically adds to AGENTS.md:

```markdown
## Development Status

**Last Updated**: 2026-02-24

### Environment
- Python: 3.10.12
- Package version: 0.1.0
- Test status: 45 tests collected

### Quick Commands
```bash
pytest tests/ -v
ruff check src/ && mypy src/
ruff format src/
```
```

## Usage

### Natural Language Triggers
- `"env check"` - Environment check
- `"test check"` - Test check
- `"version check"` - Version check
- `"commit ready"` - Pre-commit check
- `"record dev status"` - Automatically record to AGENTS.md

### Manual Recording
```bash
cd /your/project
python ~/.config/agents/skills/project-dev-checklist/scripts/record-dev-status.py
```

## Test Status Tracking

Recommended to regularly update test status table:

```markdown
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

## Integration with project-doc-management

These two skills are complementary:

| Skill | Responsibility |
|-------|---------------|
| `project-doc-management` | Manage WHERE documents go |
| `project-dev-checklist` | Check WHAT during development |

### Complete Workflow

```
1. Start
   ├─ project-doc-management → Read AGENTS.md, understand project status
   └─ project-dev-checklist  → Check development environment

2. Development
   ├─ Write code
   └─ project-dev-checklist  → Remind to run tests

3. Pre-commit
   ├─ project-dev-checklist  → Quality check
   └─ Run test suite

4. End
   ├─ project-dev-checklist  → Record status
   └─ project-doc-management → Update AGENTS.md progress
```

## Design Philosophy

- **Lightweight**: Only provides checklist, no forced process
- **Skippable**: Checks that don't apply can be skipped
- **Adaptable**: Adjust checklist items based on project needs
- **Record First**: Focus on recording status, not enforcement

## FAQ

**Q: Will this skill force me how to write code?**
A: No. It only reminds you what to check, specific development is completely up to you.

**Q: Can I skip certain checks?**
A: Yes. This is a checklist, not a forced process.

**Q: How do I know if test coverage is sufficient?**
A: The skill won't tell you "sufficient" standards, only helps record current coverage.
