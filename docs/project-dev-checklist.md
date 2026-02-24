# Project Development Checklist

## 简介

`project-dev-checklist` 是一个轻量级的开发检查清单 skill，帮助开发者记录和管理开发环境、测试状态、版本信息，不干涉具体开发流程。

## 核心功能

### 1. 环境验证
- **Python 版本**: 检查当前 Python 版本是否符合项目要求
- **虚拟环境**: 确认 venv/conda 已激活
- **依赖安装**: 验证所有依赖正确安装
- **包导入测试**: 确保可以正常导入项目包

### 2. 测试管理
- **测试执行**: 记录测试运行状态和结果
- **覆盖率追踪**: 跟踪代码覆盖率变化
- **测试环境**: 记录测试配置和环境要求
- **测试缺口**: 标记未覆盖的测试场景

### 3. 版本管理
- **包版本**: 当前版本号和发布计划
- **API 兼容性**: 记录 API 变更和兼容性
- **依赖约束**: 依赖版本管理和安全审计

### 4. 提交前检查
- **代码质量**: 格式化、linting、类型检查
- **调试代码**: 检查并移除 print/pdb 等调试代码
- **安全检查**: 扫描 API 密钥、密码等敏感信息

## 记录的检查点

### 开发前检查
```markdown
- [ ] Python 版本正确
- [ ] 虚拟环境已激活
- [ ] 依赖已安装
- [ ] 包可以正常导入
- [ ] 已阅读 AGENTS.md
```

### 开发中检查
```markdown
- [ ] 频繁运行测试
- [ ] 遵循现有代码模式
- [ ] 依赖已正确添加
```

### 提交前检查
```markdown
- [ ] 所有测试通过
- [ ] 无调试代码残留
- [ ] 无敏感信息泄露
- [ ] 代码格式化完成
- [ ] AGENTS.md 已更新
```

## 开发状态记录

运行 `record-dev-status.py` 会自动在 AGENTS.md 中添加：

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

## 使用方法

### 自然语言触发
- `"env check"` - 环境检查
- `"test check"` - 测试检查
- `"version check"` - 版本检查
- `"commit ready"` - 提交前检查
- `"record dev status"` - 自动记录到 AGENTS.md

### 手动记录
```bash
cd /your/project
python ~/.config/agents/skills/project-dev-checklist/scripts/record-dev-status.py
```

## 测试状态追踪

建议定期更新测试状态表格：

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

## 与 project-doc-management 配合

这两个 skill 是互补的：

| Skill | 职责 |
|-------|------|
| `project-doc-management` | 管理文档放在哪里 (WHERE) |
| `project-dev-checklist` | 检查开发中的什么 (WHAT) |

### 完整工作流

```
1. Start
   └─ project-doc-management: 读取 AGENTS.md
   └─ project-dev-checklist: 检查环境

2. Develop
   └─ 编写代码
   └─ project-dev-checklist: 提醒运行测试

3. Pre-commit
   └─ project-dev-checklist: 质量检查
   └─ 运行测试

4. End
   └─ project-dev-checklist: 记录状态
   └─ project-doc-management: 更新 AGENTS.md
```

## 设计理念

- **轻量级**: 只提供检查清单，不强制流程
- **可跳过**: 不适用的检查可以跳过
- **可适应**: 根据项目需要调整检查项
- **记录优先**: 重点是记录状态，而非强制执行

## 常见问题

**Q: 这个 skill 会强制我如何写代码吗？**
A: 不会。它只提醒你检查什么，具体如何开发完全由你决定。

**Q: 我可以跳过某些检查吗？**
A: 可以。这是检查清单，不是强制流程。

**Q: 如何知道测试覆盖率是否足够？**
A: skill 不会告诉你"足够"的标准，只帮你记录当前覆盖率。
