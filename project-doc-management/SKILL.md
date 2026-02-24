---
name: project-doc-management
description: |
  Manage project documentation structure and ensure continuity across Claude Code sessions.
  Use for project document management, organizing docs, tracking development progress, saving session state,
  initializing projects, or managing requirements and architecture documents.
  This skill enforces document locations (AGENTS.md, docs/, notes/) and maintains project context for sustainable development.
  Triggers: "document management", "project documents", "manage docs", "organize docs", "project doc management",
            "AGENTS.md", "checkpoint", "save progress", "project status", "init project", "update docs",
            "where did we leave off", "what was I working on", "continue from last time", "check requirements",
            "implement", "develop", "build", "create", "fix", "add feature", "start", "done", "finish", "complete".
---

# Project Document Management

## Critical Rules

### Rule 1: Document Location

```
✅ ALLOWED in root: AGENTS.md, README.md, .gitignore, LICENSE, etc.
❌ FORBIDDEN in root: Any other .md files (todo.md, plan.md, notes.md, etc.)

✅ ALLOWED: docs/*.md, notes/*.md, any subdirectory
```

**Why**: Root directory markdown files create chaos. New agents can't find context. Documents get lost.

### Rule 2: Document Naming Convention

**Standard files** (keep traditional naming):
```
✅ README.md          (project overview)
✅ AGENTS.md          (agent dashboard)
✅ LICENSE            (license file)
✅ CONTRIBUTING.md    (contribution guidelines)
```

**Project-specific documents** (use snake_case):
```
✅ requirements.md
✅ architecture.md
✅ implementation_summary.md
✅ api_reference.md
✅ getting_started.md

❌ AVOID:
  - Requirements.md          (project docs should be lowercase)
  - IMPLEMENTATION_SUMMARY.md (all caps too loud)
  - api-reference.md          (use underscore not hyphen)
  - gettingStarted.md         (use underscore not camelCase)
```

**Why**: 
- Standard files (README, AGENTS) follow tradition
- Project docs use consistent snake_case for readability

### Rule 3: Document Lifecycle Management

Every document has a lifecycle stage. AGENTS.md tracks this.

| Stage | Meaning | Example |
|-------|---------|---------|
| 🟢 **Active** | Currently being used/updated | requirements.md (being refined) |
| 🧊 **Reference** | Stable, read-only reference | architecture.md (completed) |
| 📦 **Archive** | Historical, kept for record | implementation_summary.md |
| 🗑️ **Temp** | Temporary, will be deleted | notes/2024-02-24-scratch.md |

**Rules by stage**:
- **Active**: Keep in docs/, update as needed
- **Reference**: Move to `docs/archive/reference/` if not actively needed
- **Archive**: Move to `docs/archive/` for historical record
- **Temp**: Auto-delete notes/ older than 30 days, or move to archive

---

## Core Mechanism: Three Checkpoints

### Checkpoint 1: Session Start (MANDATORY)

**Actions**:
1. Read `AGENTS.md` if it exists
2. Read `docs/requirements.md` (to understand original intent)

**Purpose**: 
- Understand current project status
- Know what was being worked on
- **Be aware of original requirements before making changes**

**If AGENTS.md doesn't exist**: 
- Ask user: "No project documentation found. Initialize? (y/n)"
- If yes → Run init script
- If no → Continue, but warn about continuity risks

### Checkpoint 2: During Development (Location Check)

**When creating any markdown document**:

```
Location Decision Tree:
├─ Is it project overview/dashboard? → AGENTS.md (root)
├─ Is it requirements/architecture/API? → docs/
├─ Is it progress tracking? → progress/ or AGENTS.md
├─ Is it temporary notes/thoughts? → notes/YYYY-MM-DD-topic.md
└─ Is it anything else? → Create appropriate subdirectory

NEVER: Create loose .md files in root (except AGENTS.md)
```

### Checkpoint 3: Session End (MANDATORY)

**Action**: Update `AGENTS.md` before ending.

**Why**: If you don't update, the next agent won't know what you did.

**What to update**:
- Current status/progress
- What was completed in this session
- What to do next
- Any blockers

**How**: 
- If AGENTS.md exists → Update it
- If you can't update (emergency exit) → Create `notes/YYYY-MM-DD-session-end.md`

---

## Directory Structure

```
project-root/
├── AGENTS.md              ← [REQUIRED] Project dashboard with Quick Start section
├── docs/                  ← [REQUIRED] Static documentation
│   ├── requirements.md    ← Original requirements
│   ├── architecture.md    ← System design
│   └── (other docs)
├── notes/                 ← [REQUIRED] Temporary notes and thinking process
│   └── YYYY-MM-DD-*.md    ← Date-prefixed for easy cleanup
└── (other project files)
```

### Document Types

| Type | Location | Purpose |
|------|----------|---------|
| Dashboard | `AGENTS.md` | Project status, quick start for new agents |
| Requirements | `docs/requirements.md` | Original intent (reference, not action) |
| Architecture | `docs/architecture.md` | System design (reference, not action) |
| Notes | `notes/YYYY-MM-DD-*.md` | Thinking process, discoveries, decisions |

---

## Original Requirements Awareness

**Rule**: Agent must be AWARE of original requirements before implementing.

**Purpose**: Prevent "unconscious deviation" where agent implements something different from original intent without realizing it.

**Requirements Check (AGENTS.md)**:
```markdown
## Requirements Check (Before Development)
**Original Requirements**: See docs/requirements.md

**Current Alignment**:
- [ ] Implementation matches original requirements
- [ ] Implementation deviates from original requirements

**Deviation Log**: Record if intentionally deviating
```

**When to update**:
1. **Before starting work**: Check requirements.md, mark alignment status
2. **If deviating**: Document in Deviation Log (original intent → current approach → reason)
3. **End of session**: Ensure AGENTS.md reflects any requirement-related decisions

---

## New Agent Experience: Preventing Information Overload

### The Problem

When AGENTS.md has too many document links, new agents don't know:
- Which documents to read first
- What's relevant to current work
- What's historical/archived

### The Solution: Structured AGENTS.md

AGENTS.md template includes these sections:

```markdown
## 🚀 New Agent Quick Start
**Status**: [Active development / Maintenance / Completed]
**Read this first**: [Which docs are relevant NOW]

## 📚 Documentation Map
| Document | When to Read | Status |
|----------|--------------|--------|
| requirements.md | Changing requirements | 🧊 Reference |
| architecture.md | Changing architecture | 🧊 Reference |
| notes/ | Understanding decisions | 📂 Active |

## 🔥 Current Focus
[Exactly ONE thing being worked on right now]

## 📋 Next Steps (Prioritized)
1. [P1] [Active task]
2. [P2] [Planned task]
3. [P3] [Future idea]
```

### Agent Behavior

**When reading AGENTS.md for the first time**:
1. Check "New Agent Quick Start" section
2. Note the project status (Active/Maintenance/Completed)
3. Read only the documents marked as "Read this first"
4. Don't read historical docs unless explicitly needed

---

## Empty Directory Guidelines

### The Problem
Empty directories (guides/, references/) can confuse new agents:
- "Should there be content here?"
- "Did something get deleted?"
- "Is this a placeholder?"

### Solution: Keep but Document

**Keep empty directories** for future use, but add explanatory content:

**Option 1: .gitkeep with header comment (Recommended)**
```
# docs/guides/.gitkeep
# Reserved for user guides and tutorials
# Status: Currently empty, planned for v0.2.0
# Expected content: getting-started.md, advanced-usage.md
```

**Option 2: README.md placeholder**
```markdown
# docs/guides/README.md
# Guides Directory

**Status**: Reserved, currently empty
**Planned content**: User guides and tutorials
**Timeline**: v0.2.0

This directory is intentionally kept for future documentation.
```

### Agent Behavior

**When encountering empty directories**:
1. Check for .gitkeep or README.md with explanatory comments
2. If explanation exists → Understand it's reserved
3. If no explanation → Create one (don't delete the directory)

**When creating new directories** (even if empty):
1. Create the directory
2. Add `.gitkeep` with header comment explaining purpose
3. Update AGENTS.md "Documentation Map" with the new directory

---

## Notes Directory: Capturing Thinking Process

### Purpose
`notes/` is for **thinking process**, not just scratch paper.

**Good uses**:
- "2026-02-24-why-we_chose_postgres.md" - Decision rationale
- "2026-02-25-api_design_iterations.md" - Design exploration
- "2026-02-26-session_end.md" - Quick checkpoint when rushed

**Bad uses**:
- Temporary todos (use AGENTS.md instead)
- Code snippets (use actual code files)
- Empty files

### Naming Convention
```
notes/YYYY-MM-DD-brief_description.md  ← Note: snake_case description
```

**Benefits**:
- Chronological order
- Easy to clean up old notes
- Clear when decision was made

---

## Document Lifecycle Management

### The Problem
Over time, docs/ accumulates:
- Temporary files that are no longer needed
- Draft documents that were superseded
- Implementation summaries for completed versions
- Documents with inconsistent naming

This creates confusion for new agents.

### Solution: Explicit Lifecycle Stages

**Stage 1: Active Documents** (in `docs/`)
- Currently being used or updated
- Examples: requirements.md (being refined), architecture.md (current design)

**Stage 2: Reference Documents** (in `docs/` or `docs/archive/reference/`)
- Stable, completed, read-only
- Kept for reference but rarely change
- Examples: completed architecture.md, stable api_reference.md

**Stage 3: Archive Documents** (in `docs/archive/`)
- Historical record
- Implementation summaries, completion reports, old versions
- Kept for history but not part of active development
- Examples: v1_implementation_summary.md, project_completion_report.md

**Stage 4: Temp Documents** (in `notes/`)
- Thinking process, scratch notes
- Auto-expire: Can be deleted after 30 days
- Or manually archived if valuable

### Document Review Process

**When to review**: End of each milestone, or monthly

**Review Checklist** (in AGENTS.md):
```markdown
## Document Review (Last: YYYY-MM-DD)

### Active Documents
| Document | Lifecycle | Action Needed |
|----------|-----------|---------------|
| requirements.md | 🟢 Active | None |
| architecture.md | 🧊 Reference | Consider archive if v2 starts |

### Archive Candidates
| Document | Reason | Decision |
|----------|--------|----------|
| implementation_summary.md | v1 completed | Move to docs/archive/ |
| draft_api.md | Superseded by api_reference.md | Delete |

### Naming Audit
| Document | Current Name | Correct Name | Action |
|----------|--------------|--------------|--------|
| IMPLEMENTATION_SUMMARY.md | PascalCase | implementation_summary.md | Rename |
```

### Naming Convention Enforcement

**When creating a document**:
1. Check name is snake_case: `lowercase_with_underscores.md`
2. No spaces, no uppercase, no hyphens (except in dates for notes)
3. If incorrect → Rename before creating

**When reviewing documents**:
1. Check all docs/ files follow naming convention
2. Rename non-compliant files
3. Update AGENTS.md Documentation Map

### Long-term Storage Policy

**Documents that MUST be kept** (with reason):
```markdown
## Long-term Documents
| Document | Reason for Keeping | Content Summary |
|----------|-------------------|-----------------|
| requirements.md | Original project intent | Core features and constraints |
| architecture.md | System design decisions | Component structure and data flow |
| adr_001_database.md | Why we chose PostgreSQL | Decision rationale and alternatives considered |
```

**Documents that CAN be deleted/archived**:
- Implementation summaries after next version starts
- Draft documents superseded by final versions
- Temp notes older than 30 days (unless archived)
- Meeting notes after action items completed

---

## Workflows

### 1. Project Initialization

```bash
python ~/.config/agents/skills/project-doc-management/scripts/init-project.py "Project Name"
```

Creates:
- `AGENTS.md` (with Quick Start template)
- `docs/requirements.md`
- `docs/architecture.md`
- `notes/` directory

### 2. Every Session Start

**MUST**:
```
1. Read AGENTS.md
2. Read docs/requirements.md
3. Check "New Agent Quick Start" for reading guidance
4. Note project status (Active/Maintenance/Completed)
5. Identify "Current Focus" task
```

**Report to user**:
- Project status
- Current focus
- Which documents you read (don't list all, just relevant ones)

### 3. During Development

**Creating documents**:
- Requirements/design → `docs/`
- Progress/status → Update `AGENTS.md`
- Thinking/decisions → `notes/YYYY-MM-DD-topic.md`
- **NEVER** root directory .md files

**Updating AGENTS.md**:
- Keep "Current Focus" to ONE task
- Update "Documentation Map" if doc status changes
- Mark completed items in "Next Steps"

### 4. Every Session End

**MUST update AGENTS.md**:
- Progress status
- Recent session entry
- Next steps (if changed)
- Any deviation from requirements (with reason)

**MUST create note if rushed**:
```bash
# If no time to update AGENTS.md properly
echo "Session end: Completed X, next is Y" > notes/YYYY-MM-DD-session-end.md
```

---

## Enforcement Mechanisms

### Mechanism 1: Mandatory Checkpoints

**MUST** for:
- Reading AGENTS.md at session start
- Updating AGENTS.md at session end
- No root .md files (except AGENTS.md)

### Mechanism 2: Location Validation

Before creating any .md file:
```
If path is root and not AGENTS.md/README.md:
    ERROR: "Documents must go in docs/, progress/, or notes/"
```

### Mechanism 3: Requirements Awareness

**Before implementing**:
```
1. Read docs/requirements.md
2. In AGENTS.md, check "Requirements Check":
   - If matches → Mark aligned
   - If deviates → Document in Deviation Log
```

---

## Anti-Patterns (Breaks Sustainability)

| Anti-Pattern | Why It Breaks | Correct Approach |
|--------------|---------------|------------------|
| Creating `todo.md` in root | Next agent won't find it | Put in `notes/` or update `AGENTS.md` |
| Ending session without updating AGENTS.md | Next agent doesn't know status | Always update before ending |
| Not checking requirements.md | Unconscious deviation from original intent | Read requirements, mark alignment |
| Too many docs in Quick Links | Information overload for new agents | Curate to 2-3 most relevant docs |
| Empty directories without documentation | Confusion about purpose | Add .gitkeep with explanatory comment |
| Notes/ full of todos | Todos should be in AGENTS.md | Use notes for thinking, AGENTS.md for tasks |
| No date prefix on notes | Can't identify old vs new | Always use YYYY-MM-DD- prefix |

---

## User Commands

```
"init project"              → Initialize structure
"checkpoint" / "status"     → Read AGENTS.md, report status
"update docs" / "save"      → Update AGENTS.md with progress
"project docs"              → Show documentation structure
"organize docs"             → Clean up empty directories, structure review
```

---

## Success Criteria

This skill succeeds when:

1. ✅ **No scattered documents**: All .md files in predictable locations
2. ✅ **New agent onboarding < 5 minutes**: Quick Start section guides reading
3. ✅ **Requirements awareness**: Agent checks requirements before implementing
4. ✅ **Progress tracked**: AGENTS.md always reflects current state
5. ✅ **No information overload**: Only relevant docs highlighted
6. ✅ **Empty directories documented**: Reserved directories have .gitkeep with explanation
