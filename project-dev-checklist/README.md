# Project Development Checklist

Development environment and testing checklist for Python projects.

## Purpose

Track:
- **Environment**: Python version, venv, dependencies
- **Testing**: Test execution, coverage, gaps
- **Version**: Package version, API compatibility
- **Quality**: Code checks, secrets scanning

**Not a process - just reminders of what to verify.**

## Usage

### Natural Language Triggers

```
"env check"         → Show environment verification
"test check"        → Show testing checklist  
"version check"     → Show version management
"commit ready"      → Show pre-commit checks
"record dev status" → Run script to update AGENTS.md
```

### Manual Recording

```bash
# Record current dev status to AGENTS.md
cd /your/project
python ~/.config/agents/skills/project-dev-checklist/scripts/record-dev-status.py
```

## What It Tracks

### 1. Environment Configuration
- Python version (required vs current)
- Virtual environment status
- Dependencies installed
- Package imports correctly

### 2. Testing Status
- Test execution results
- Coverage metrics
- Test environment setup
- Known gaps

### 3. Version Management
- Package version
- API compatibility
- Dependency constraints
- Security audit status

### 4. Pre-Commit Checks
- Code quality (format, lint, type check)
- Debug code removal
- Secrets scanning

## Recording Template

Use `record-dev-status.py` to create/update this section in AGENTS.md:

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
```
```

## Integration with project-doc-management

These two skills work together:

| Skill | Responsibility |
|-------|---------------|
| `project-doc-management` | WHERE documents go |
| `project-dev-checklist` | WHAT to check in development |

**Workflow**:
1. `project-doc-management` → Read AGENTS.md, understand project
2. `project-dev-checklist` → Verify environment, run tests
3. Develop
4. `project-dev-checklist` → Pre-commit checks
5. `project-doc-management` → Update AGENTS.md

## Checklist Items

### Environment
- [ ] Python version correct
- [ ] Virtual environment activated
- [ ] Dependencies installed
- [ ] Package imports without error

### Testing
- [ ] Tests exist in tests/
- [ ] All tests pass
- [ ] Coverage acceptable
- [ ] No broken tests

### Version
- [ ] Version bumped appropriately
- [ ] API compatibility maintained
- [ ] Dependencies constrained
- [ ] CHANGELOG updated

### Quality
- [ ] No debug code (print, pdb)
- [ ] No secrets committed
- [ ] Formatter/linter happy (if configured)

## Philosophy

**Check, don't enforce.**

- Skip items that don't apply
- Adapt to your project's needs
- Focus on catching oversights
- Keep the bar low, progress steady
