# Claude Code Skills Collection

Personal collection of Claude Code skills for AI-assisted development.

## Skills

### Custom Created

| Skill | Purpose | Documentation |
|-------|---------|---------------|
| `project-doc-management` | Document management | [📖 Documentation](docs/project-doc-management.md) |
| `project-dev-checklist` | Development checklist | [📖 Documentation](docs/project-dev-checklist.md) |

**Project Document Management** (`project-doc-management`):
- Enforces standardized project document locations (AGENTS.md, docs/, notes/)
- Supports multi-session continuous development without losing context
- Protects original requirements from deviation
- Document lifecycle management

**Development Checklist** (`project-dev-checklist`):
- Records development environment configuration (Python version, dependencies)
- Tracks test status and coverage
- Version management and API compatibility checking
- Pre-commit quality checks

### Third-Party Skills

| Skill | Purpose |
|-------|---------|
| `arxiv-research` | Search and summarize arXiv papers |
| `deep-research` | Enterprise-grade research with multi-source synthesis |
| `literature-review` | Generate comprehensive literature reviews |
| `paper-analyzer` | Deep analysis of academic papers |
| `paper-slide-deck` | Generate professional slide decks from papers |
| `research-gap-finder` | Identify research gaps and generate ideas |
| `research-proposal` | Generate academic research proposals |

## Quick Start

### 1. Document Management

```bash
# Initialize a new project
cd /path/to/your/project
python ~/.config/agents/skills/project-doc-management/scripts/init-project.py "Project Name"

# Or say to Claude: "init project"
```

[Detailed Documentation →](docs/project-doc-management.md)

### 2. Development Checklist

```bash
# Record development status
python ~/.config/agents/skills/project-dev-checklist/scripts/record-dev-status.py

# Or say to Claude: "env check", "test check", "commit ready"
```

[Detailed Documentation →](docs/project-dev-checklist.md)

## Installation

### Individual Skills

Copy specific skill to your Claude Code skills directory:

```bash
# For custom skills
cp -r project-doc-management ~/.config/agents/skills/
cp -r project-dev-checklist ~/.config/agents/skills/

# For third-party skills
cp -r arxiv-research ~/.config/agents/skills/
```

### All Skills

```bash
# Clone this repo
git clone https://github.com/XavierZhang2002/code-agent-skills.git /tmp/claude-skills
cp -r /tmp/claude-skills/* ~/.config/agents/skills/
```

## Directory Structure

```
.skills/
├── docs/                           # Documentation
│   ├── project-doc-management.md   # Document management skill docs
│   └── project-dev-checklist.md    # Development checklist skill docs
├── project-doc-management/         # Custom - Document management
│   ├── SKILL.md
│   ├── README.md
│   ├── scripts/
│   └── templates/
├── project-dev-checklist/          # Custom - Development checklist
│   ├── SKILL.md
│   ├── README.md
│   ├── scripts/
│   └── templates/
└── ...                             # Other skills
```

## Workflow: Two Skills Working Together

```
1. Start Session
   ├─ project-doc-management → Read AGENTS.md, understand project status
   └─ project-dev-checklist  → Check development environment, verify tests

2. Development
   ├─ Write code
   └─ project-dev-checklist  → Remind to run tests

3. Pre-commit
   ├─ project-dev-checklist  → Code quality check
   └─ Run test suite

4. End Session
   ├─ project-dev-checklist  → Record development status
   └─ project-doc-management → Update AGENTS.md progress
```

## Backup & Restore

### Export

```bash
cd ~/.config/agents/skills
./export-skills.sh
# Generates: exports/claude-skills-YYYYMMDD_HHMMSS.tar.gz
```

### Import

```bash
./import-skills.sh exports/claude-skills-YYYYMMDD_HHMMSS.tar.gz
```

## GitHub Repository

**URL**: https://github.com/XavierZhang2002/code-agent-skills

```bash
# Clone with submodules
git clone --recurse-submodules https://github.com/XavierZhang2002/code-agent-skills.git ~/.config/agents/skills
```

## License

- **Custom skills** (`project-doc-management`, `project-dev-checklist`): MIT License
- **Third-party skills**: See individual skill directories for licenses

## Author

Created and maintained for personal Claude Code workflows.
