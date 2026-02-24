# {PROJECT_NAME}

> **Agent Instructions**: 
> 1. Read this file at session start (say "checkpoint" if unsure)
> 2. Read docs/requirements.md before making changes
> 3. Update this file at session end (say "save progress" to update)

---

## 🚀 New Agent Quick Start

**Project Status**: 🔵 Active Development / 🟡 Maintenance / 🟢 Completed

**Read this first**:
1. [This AGENTS.md](#current-status) - Current status and focus
2. [Requirements](./docs/requirements.md) - What we're building

**Don't need to read yet** (reference only):
- Architecture - Only if changing system design
- Old notes - Only if investigating past decisions

---

## Project Overview
- **Name**: {PROJECT_NAME}
- **Objective**: [What this project does - one sentence]
- **Started**: {DATE}

## Requirements Check (Before Development)
**Original Requirements**: See [docs/requirements.md](./docs/requirements.md)

**Current Alignment**:
- [ ] Implementation matches original requirements
- [ ] Implementation deviates from original requirements (see Deviation Log below)

**Deviation Log** (if any):
| Date | Requirement | Original Intent | Current Approach | Reason for Deviation |
|------|-------------|-----------------|------------------|---------------------|
| - | - | - | - | - |

---

## 🔥 Current Focus
**Working on right now**: [Specific, concrete task]

**Context**: [Why this task, what's the goal]

---

## Current Status (Last Updated: {DATE})
- **Overall Progress**: [e.g., "40%" or "Phase 2 of 4"]
- **Blockers**: [None / describe blockers]

---

## 📚 Documentation Map

### Core Documents
| Document | Lifecycle | When to Read |
|----------|-----------|--------------|
| [requirements.md](./docs/requirements.md) | 🟢 Active | Before making changes |
| [architecture.md](./docs/architecture.md) | 🟢 Active | When changing design |
| [notes/](./notes/) | 🟢 Active | Understanding decisions |

### Reserved Directories (Currently Empty)
These directories are intentionally kept for future use:

| Directory | Purpose | Planned Content |
|-----------|---------|-----------------|
| `docs/guides/` | User guides and tutorials | getting_started.md, advanced_usage.md |
| `docs/references/` | API reference docs | api_reference.md, configuration_guide.md |
| `docs/decisions/` | Architecture Decision Records | adr_XXX_description.md files |

> **Note**: See `.gitkeep` files in each directory for status details.

---

## 📋 Next Steps (Prioritized)
1. **[P1 - Active]** [Current task being worked on]
2. **[P2 - Planned]** [Next task to do after current]
3. **[P3 - Future]** [Future idea, not urgent]

## Recent Sessions (Last 5)
1. [{DATE}] [What was done - be specific]
2. [{DATE}] [What was done]
3. [{DATE}] [What was done]
4. [{DATE}] [What was done]
5. [{DATE}] [What was done]

---

## 📋 Document Review (Last: {DATE})

### Active Documents
| Document | Lifecycle | Status | Notes |
|----------|-----------|--------|-------|
| requirements.md | 🟢 Active | Current | Original project requirements |
| architecture.md | 🟢 Active | Current | System design documentation |

### Archive Candidates (Review Needed)
| Document | Reason for Archive | Decision |
|----------|-------------------|----------|
| - | - | - |

### Naming Audit
| Document | Status |
|----------|--------|
| All docs follow snake_case naming | ✅ / ❌ |

### Long-term Documents (Keep Forever)
| Document | Reason for Keeping |
|----------|-------------------|
| requirements.md | Original project intent |
| architecture.md | System design decisions |

---

## Project Structure
```
{PROJECT_NAME}/
├── AGENTS.md              # Project dashboard
├── README.md              # Project overview
├── docs/                  # Documentation
│   ├── requirements.md    # Original requirements (long-term)
│   ├── architecture.md    # System design (long-term)
│   └── ...                # Other docs
├── notes/                 # Thinking process and decisions
├── src/                   # Source code
├── examples/              # Usage examples
└── tests/                 # Test suite
```

## Downstream Projects (if any)
- **project_name**: Description
  - Location: `/path/to/project/`
  - Status: Current status

---

## Session Continuity Notes
**For next agent**: 
- [Key context next agent should know immediately]
- [Any warnings or gotchas]

---

*This file is updated at the end of every development session to maintain continuity.*

---

## Document Naming Convention

### Standard Files (keep uppercase)
- `README.md` - Project overview
- `AGENTS.md` - This agent dashboard

### Project Documents (use snake_case)
`lowercase_with_underscores.md`

✅ examples: requirements.md, api_reference.md, implementation_summary.md  
❌ avoid: Requirements.md, api-reference.md, gettingStarted.md, IMPLEMENTATION_SUMMARY.md
