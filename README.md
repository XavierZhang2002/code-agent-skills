# Claude Code Skills Collection

Personal collection of Claude Code skills for AI-assisted development.

## Skills

### Custom Created

| Skill | Purpose | Documentation |
|-------|---------|---------------|
| `project-doc-management` | Document management | [📖 Documentation](docs/project-doc-management.md) |
| `project-dev-checklist` | Development checklist | [📖 Documentation](docs/project-dev-checklist.md) |

**项目文档管理** (`project-doc-management`): 
- 强制项目文档位置规范（AGENTS.md, docs/, notes/）
- 支持多轮次持续开发，不丢失上下文
- 保护原始需求不被偏离
- 文档生命周期管理

**开发检查清单** (`project-dev-checklist`):
- 记录开发环境配置（Python版本、依赖）
- 追踪测试状态和覆盖率
- 版本管理和API兼容性检查
- 提交前质量检查

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

[详细文档 →](docs/project-doc-management.md)

### 2. Development Checklist

```bash
# Record development status
python ~/.config/agents/skills/project-dev-checklist/scripts/record-dev-status.py

# Or say to Claude: "env check", "test check", "commit ready"
```

[详细文档 →](docs/project-dev-checklist.md)

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
├── docs/                           # 文档说明
│   ├── project-doc-management.md   # 文档管理 skill 说明
│   └── project-dev-checklist.md    # 开发清单 skill 说明
├── project-doc-management/         # 自定义 - 文档管理
│   ├── SKILL.md
│   ├── README.md
│   ├── scripts/
│   └── templates/
├── project-dev-checklist/          # 自定义 - 开发清单
│   ├── SKILL.md
│   ├── README.md
│   ├── scripts/
│   └── templates/
└── ...                             # 其他 skills
```

## Workflow: Two Skills Working Together

```
1. Start Session
   ├─ project-doc-management → 读取 AGENTS.md，了解项目状态
   └─ project-dev-checklist  → 检查开发环境，验证测试

2. Development
   ├─ 编写代码
   └─ project-dev-checklist  → 提醒运行测试

3. Pre-commit
   ├─ project-dev-checklist  → 代码质量检查
   └─ 运行测试套件

4. End Session
   ├─ project-dev-checklist  → 记录开发状态
   └─ project-doc-management → 更新 AGENTS.md 进度
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
