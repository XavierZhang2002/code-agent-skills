# Project Document Management Skill

Ensure project continuity across Claude Code sessions through structured documentation.

## Quick Start

```bash
# Initialize a new project
cd /path/to/your/project
python ~/.config/agents/skills/project-doc-management/scripts/init-project.py "Your Project Name"
```

## Core Concept

**Three Checkpoints** ensure continuity:

1. **Session Start** → Read AGENTS.md (know where we left off)
2. **During Work** → Put documents in correct locations (docs/, notes/)
3. **Session End** → Update AGENTS.md (save progress for next time)

## Directory Structure

```
project-root/
├── AGENTS.md              ← Project dashboard (REQUIRED)
│   ├── 🚀 New Agent Quick Start
│   ├── 🔥 Current Focus
│   ├── 📚 Documentation Map
│   ├── 📋 Next Steps (Prioritized)
│   └── 📋 Document Review    ← Lifecycle management
│
├── docs/                  ← Static documentation
│   ├── requirements.md    ← Original requirements (long-term)
│   ├── architecture.md    ← System design (long-term)
│   ├── archive/           ← Archived documents
│   │   └── reference/     ← Old reference docs
│   └── ...
│
└── notes/                 ← Thinking process
    └── YYYY-MM-DD-*.md    ← Date-prefixed notes (temporary)
```

## Document Naming Convention

### Standard Files (Traditional Naming)
These files keep their traditional uppercase names:

✅ **Keep as-is**:
- `README.md` - Project overview
- `AGENTS.md` - Agent dashboard
- `LICENSE` - License file
- `CONTRIBUTING.md` - Contribution guidelines

### Project-Specific Documents (snake_case)
All project documentation uses `snake_case`:

✅ **Correct**:
- `requirements.md`
- `architecture.md`
- `implementation_summary.md`
- `api_reference.md`
- `getting_started.md`

❌ **Avoid**:
- `Requirements.md` (use lowercase)
- `IMPLEMENTATION_SUMMARY.md` (too loud)
- `api-reference.md` (use underscore `_` not hyphen `-`)
- `implementation summary.md` (no spaces)
- `gettingStarted.md` (use underscore `_` not camelCase)

## Key Features

### 1. New Agent Quick Start
Prevents information overload by telling new agents:
- What to read first (2-3 docs max)
- What's reference material (don't read yet)
- Current project status (Active/Maintenance/Completed)

### 2. Current Focus
Exactly ONE task being worked on right now. Eliminates ambiguity about what to do.

### 3. Documentation Map
Table showing which documents to read when:
| Document | When to Read | Status |
|----------|--------------|--------|
| requirements.md | Before changes | 🧊 Reference |
| architecture.md | When changing design | 🧊 Reference |

### 4. Original Requirements Awareness
Prevents unconscious deviation:
- Check requirements.md before implementing
- Mark alignment in AGENTS.md
- Document deviations with reasons

## User Commands

| Command | Action |
|---------|--------|
| "init project" | Create documentation structure |
| "checkpoint" | Read AGENTS.md, report status |
| "save progress" | Update AGENTS.md with current state |
| "project status" | Show current project status |
| "organize docs" | Review and clean up structure |

## Best Practices

### For Active Development
- Keep "Current Focus" to ONE concrete task
- Update AGENTS.md at every session end
- Create notes/YYYY-MM-DD-*.md for thinking process

### For Maintenance
- Mark status as 🟡 Maintenance in Quick Start
- Keep Next Steps short (1-2 items)
- Archive old notes if they become irrelevant

### For Completed Projects
- Mark status as 🟢 Completed in Quick Start
- Freeze requirements.md and architecture.md
- Remove empty directories (guides/, references/ if unused)

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Creating .md files in root directory | Can't find context | Use docs/ or notes/ |
| Mixed naming for project docs | Inconsistent, hard to search | Use **snake_case** for project docs |
| Too many docs in Quick Start | Information overload | Max 2-3 docs |
| Vague "Current Focus" | Don't know what to do | Be specific about task |
| Empty directories without documentation | Confusion about purpose | Add .gitkeep with comment |
| Not updating AGENTS.md at session end | Lost context | Always update before ending |
| Keeping all documents forever | Clutter, confusion | Archive or delete old docs |
| No lifecycle tracking | Don't know what's current | Use 🟢/🧊/📦/🗑️ in Documentation Map |

## Empty Directory Handling

**Empty directories are kept** but documented:

Directories like `docs/guides/`, `docs/references/`, `docs/decisions/` are reserved for future use.

### Documenting Empty Directories

Add `.gitkeep` with header comment:
```
# docs/guides/.gitkeep
# Reserved for user guides and tutorials
# Status: Currently empty, planned for v0.2.0
# Expected content: getting-started.md, advanced-usage.md
```

Or add `README.md`:
```markdown
# Guides Directory

**Status**: Reserved, currently empty
**Planned content**: User guides and tutorials
**Timeline**: v0.2.0
```

### Why Keep Empty Directories?

1. **Predictable structure** - New agents know where things go
2. **Future-ready** - No need to recreate directories later
3. **Documentation Map** - AGENTS.md lists them as "Reserved"

## Document Lifecycle Management

Documents have lifecycle stages tracked in AGENTS.md:

| Stage | Icon | Meaning | Location |
|-------|------|---------|----------|
| **Active** | 🟢 | Currently being used/updated | `docs/` |
| **Reference** | 🧊 | Stable, read-only | `docs/` or `docs/archive/reference/` |
| **Archive** | 📦 | Historical record | `docs/archive/` |
| **Temp** | 🗑️ | Temporary, auto-expire | `notes/` |

### Document Review Process

**When**: End of each milestone, or monthly

**AGENTS.md includes**:
```markdown
## Document Review (Last: YYYY-MM-DD)

### Active Documents
| Document | Lifecycle | Status |
|----------|-----------|--------|
| requirements.md | 🟢 Active | Current |

### Archive Candidates
| Document | Reason | Decision |
|----------|--------|----------|
| implementation_summary.md | v1 completed | Move to docs/archive/ |

### Naming Audit
| Status |
|--------|
| All docs follow snake_case naming: ✅ |
```

### Long-term Storage Policy

**Keep Forever** (with reason):
- `requirements.md` - Original project intent
- `architecture.md` - System design decisions
- `adr_XXX_*.md` - Why we made key decisions

**Archive After Completion**:
- Implementation summaries
- Project completion reports
- Old version documentation

**Delete After 30 Days**:
- Scratch notes (unless valuable)
- Draft documents superseded by final versions
- Meeting notes after actions completed

## Notes Directory

Use `notes/` for thinking process, not just scratch paper.

**Good examples**:
- `2026-02-24-why_we_chose_postgres.md`  ← Note: snake_case
- `2026-02-25-api_design_decisions.md`
- `2026-02-26-session_end_checkpoint.md`

**Naming**: Use `YYYY-MM-DD-brief_description.md` (snake_case for description)

## Troubleshooting

### "I don't know which documents to read"
→ Check AGENTS.md "🚀 New Agent Quick Start" section

### "There are too many documents"
→ The Documentation Map shows which are relevant now

### "Empty directories are confusing"
→ They are intentionally reserved for future use
→ Check the `.gitkeep` file in each directory for purpose and status
→ See AGENTS.md "Documentation Map" for reserved directories list

### "Document names are inconsistent"
→ Rename all to snake_case: lowercase_with_underscores.md
→ No spaces, no uppercase, no hyphens
→ Update AGENTS.md Documentation Map after renaming

### "There are too many old documents"
→ Review in AGENTS.md "Document Review" section
→ Move completed summaries to docs/archive/
→ Delete temporary notes older than 30 days
→ Keep only: requirements.md, architecture.md, active docs

### "Requirements keep changing"
→ Document deviations in Deviation Log with reasons

## Success Indicators

✅ New agent can onboard in < 5 minutes  
✅ No scattered .md files in root directory  
✅ Clear "Current Focus" task  
✅ Requirements are visible and checked  
✅ Session continuity maintained  
