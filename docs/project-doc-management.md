# Project Document Management

## Overview

`project-doc-management` is a Claude Code skill for managing project documentation structure. It ensures standardized document locations, supports multi-session continuous development, and prevents loss of original requirements.

## Core Features

### 1. Enforced Document Location
- **Root Directory Cleanup**: Only standard files (`AGENTS.md`, `README.md`) allowed in root
- **Standardized Directory Structure**: All project documents must go to `docs/`, `notes/`, `progress/`
- **Prevent Document Scattering**: Prohibits creating `todo.md`, `plan.md` in root directory

### 2. Multi-Session Continuous Development Support
- **AGENTS.md Checkpoint**: Read at session start, update at session end
- **Session Continuity**: New agent can understand project status within 5 minutes
- **Progress Tracking**: Records current progress, active tasks, blockers

### 3. Original Requirements Protection
- **requirements.md**: Frozen original requirements, changes require documented reasons
- **Requirements Alignment Check**: Verify before development if deviating from original requirements
- **Deviation Log**: Records requirement changes and justifications

### 4. Document Lifecycle Management
| Stage | Icon | Meaning | Location |
|------|------|---------|----------|
| 🟢 Active | Currently in use | `docs/` |
| 🧊 Reference | Stable reference | `docs/` or `docs/archive/reference/` |
| 📦 Archive | Historical record | `docs/archive/` |
| 🗑️ Temp | Temporary | `notes/` |

### 5. Naming Convention
- **Standard Files**: `README.md`, `AGENTS.md` (keep uppercase)
- **Project Documents**: Use `snake_case` (e.g., `requirements.md`, `implementation_summary.md`)

## Directory Structure

```
project-root/
├── AGENTS.md              # Project dashboard (required)
├── docs/
│   ├── requirements.md    # Original requirements
│   ├── architecture.md    # Architecture design
│   ├── archive/           # Archived documents
│   │   ├── implementation_summary.md
│   │   └── project_completion_report.md
│   ├── guides/            # User guides (reserved)
│   ├── references/        # API docs (reserved)
│   └── decisions/         # Architecture decisions (reserved)
├── notes/                 # Temporary notes
│   └── YYYY-MM-DD-*.md
└── (other project files)
```

## AGENTS.md Template Structure

```markdown
# Project Name

## 🚀 New Agent Quick Start
- Project Status: 🔵 Active / 🟡 Maintenance / 🟢 Completed
- Read First: requirements.md, (other key documents)

## 📚 Documentation Map
| Document | When to Read | Lifecycle |
|----------|--------------|-----------|
| requirements.md | Before changes | 🧊 Reference |

## 🔥 Current Focus
Current active task

## 📋 Document Review
- Active Documents
- Archive Candidates
- Naming Audit
- Long-term Documents

## Recent Sessions
Last 5 session records
```

## Usage

### Initialize Project
```bash
cd /path/to/project
python ~/.config/agents/skills/project-doc-management/scripts/init-project.py "Project Name"
```

### Natural Language Triggers
- `"init project"` - Initialize document structure
- `"checkpoint"` - Check project status
- `"save progress"` - Save current progress
- `"project status"` - View current status

## Best Practices

1. **Session Start**: Read AGENTS.md to understand status
2. **During Development**: Place documents in correct locations
3. **Session End**: Update AGENTS.md
4. **Regular Review**: Archive old documents, clean temporary notes

## Integration with project-dev-checklist

- **project-doc-management**: Manages WHERE documents go
- **project-dev-checklist**: Checks WHAT to verify during development

Typical workflow:
1. `project-doc-management` reads AGENTS.md
2. `project-dev-checklist` checks development environment
3. Develop code
4. `project-dev-checklist` runs tests
5. `project-doc-management` updates documents and progress
