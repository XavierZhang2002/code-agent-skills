# Project Document Management

## 简介

`project-doc-management` 是一个用于管理项目文档结构的 Claude Code skill，确保文档位置规范、支持多轮次持续开发、不丢失原始需求。

## 核心功能

### 1. 强制文档位置管理
- **根目录清理**: 只允许 `AGENTS.md`, `README.md` 等标准文件存在于根目录
- **规范目录结构**: 所有项目文档必须放入 `docs/`, `notes/`, `progress/` 等固定位置
- **防止文档散乱**: 禁止在根目录随意创建 `todo.md`, `plan.md` 等文件

### 2. 支持多轮次持续开发
- **AGENTS.md 检查点**: 每次会话开始时读取，结束时更新
- **会话连续性**: 新Agent能在5分钟内了解项目状态
- **进度追踪**: 记录当前进度、正在进行的任务、阻塞问题

### 3. 原始需求保护
- **requirements.md**: 冻结原始需求，修改需记录原因
- **需求对齐检查**: 开发前检查是否偏离原始需求
- **偏差日志**: 记录需求变更及原因

### 4. 文档生命周期管理
| 阶段 | 图标 | 含义 | 位置 |
|------|------|------|------|
| 🟢 Active | 当前使用中 | `docs/` |
| 🧊 Reference | 稳定参考 | `docs/` 或 `docs/archive/reference/` |
| 📦 Archive | 历史存档 | `docs/archive/` |
| 🗑️ Temp | 临时 | `notes/` |

### 5. 命名规范
- **标准文件**: `README.md`, `AGENTS.md` (保持大写)
- **项目文档**: 使用 `snake_case` (如 `requirements.md`, `implementation_summary.md`)

## 目录结构

```
project-root/
├── AGENTS.md              # 项目仪表盘（必须）
├── docs/
│   ├── requirements.md    # 原始需求
│   ├── architecture.md    # 架构设计
│   ├── archive/           # 归档文档
│   │   ├── implementation_summary.md
│   │   └── project_completion_report.md
│   ├── guides/            # 用户指南（预留）
│   ├── references/        # API文档（预留）
│   └── decisions/         # 架构决策（预留）
├── notes/                 # 临时笔记
│   └── YYYY-MM-DD-*.md
└── (其他项目文件)
```

## AGENTS.md 模板结构

```markdown
# Project Name

## 🚀 New Agent Quick Start
- 项目状态: 🔵 Active / 🟡 Maintenance / 🟢 Completed
- 首先阅读: requirements.md, (其他关键文档)

## 📚 Documentation Map
| Document | When to Read | Lifecycle |
|----------|--------------|-----------|
| requirements.md | 变更前 | 🧊 Reference |

## 🔥 Current Focus
当前正在进行的任务

## 📋 Document Review
- Active Documents
- Archive Candidates
- Naming Audit
- Long-term Documents

## Recent Sessions
最近5次会话记录
```

## 使用方法

### 初始化项目
```bash
cd /path/to/project
python ~/.config/agents/skills/project-doc-management/scripts/init-project.py "Project Name"
```

### 自然语言触发
- `"init project"` - 初始化文档结构
- `"checkpoint"` - 查看项目状态
- `"save progress"` - 保存进度
- `"project status"` - 查看当前状态

## 最佳实践

1. **会话开始**: 读取 AGENTS.md 了解状态
2. **开发中**: 文档放入正确位置
3. **会话结束**: 更新 AGENTS.md
4. **定期审查**: 归档旧文档，清理临时笔记

## 与 project-dev-checklist 配合

- **project-doc-management**: 管理文档位置和内容
- **project-dev-checklist**: 检查开发环境和测试

典型工作流:
1. `project-doc-management` 读取 AGENTS.md
2. `project-dev-checklist` 检查开发环境
3. 开发代码
4. `project-dev-checklist` 运行测试
5. `project-doc-management` 更新文档和进度
