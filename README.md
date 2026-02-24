# Claude Code Skills Collection

Personal collection of Claude Code skills for AI-assisted development.

## Skills

### Custom Created

| Skill | Purpose | Description |
|-------|---------|-------------|
| `project-doc-management` | Document management | Enforces project documentation structure (AGENTS.md, docs/, notes/) |
| `project-dev-checklist` | Development checklist | Tracks environment, testing, and version management |

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
git clone <your-repo-url> /tmp/claude-skills
cp -r /tmp/claude-skills/* ~/.config/agents/skills/
```

## Usage

### project-doc-management

```bash
# Initialize a new project
cd /path/to/your/project
python ~/.config/agents/skills/project-doc-management/scripts/init-project.py "Project Name"

# Or say to Claude: "init project"
```

### project-dev-checklist

```bash
# Record development status
python ~/.config/agents/skills/project-dev-checklist/scripts/record-dev-status.py

# Or say to Claude: "env check", "test check", "commit ready"
```

## Structure

```
.skills/
├── project-doc-management/     # Custom - Document management
│   ├── SKILL.md
│   ├── README.md
│   ├── scripts/
│   └── templates/
├── project-dev-checklist/      # Custom - Development checklist
│   ├── SKILL.md
│   ├── README.md
│   ├── scripts/
│   └── templates/
└── ...                         # Other skills
```

## License

Custom skills (project-doc-management, project-dev-checklist): MIT License

Third-party skills: See individual skill directories for licenses.

## Author

Created and maintained for personal Claude Code workflows.
