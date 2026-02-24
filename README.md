# 科研论文调研 Skills 快速参考

## 已安装的 Skills

### 1. arxiv-research
**功能**: 搜索、获取和总结 arXiv 论文

**使用示例**:
```bash
# 搜索最新论文
kimi "搜索 arXiv 上最近关于 transformer 的论文"

# 特定类别
kimi "查找 cs.LG 类别昨天发表的新论文"

# 生成每日简报
kimi "帮我生成一份 arXiv AI 论文的每日摘要"
```

**触发词**: "search arxiv", "find papers", "summarize arxiv", "latest research"

---

### 2. paper-analyzer
**功能**: 深度分析论文的方法、贡献和局限

**使用示例**:
```bash
# 分析本地 PDF
kimi "深度分析这篇论文" ./paper.pdf

# 批判性分析
kimi "这篇论文的方法有什么缺陷？" ./paper.pdf

# 比较分析
kimi "比较这两篇论文的方法差异" paper1.pdf paper2.pdf
```

**触发词**: "analyze this paper", "deep dive", "critique", "methodology analysis"

---

### 3. literature-review
**功能**: 生成综合文献综述

**使用示例**:
```bash
# 基于多篇论文生成综述
kimi "基于这些论文写一份文献综述" ./papers/*.pdf

# 特定主题
kimi "写一份关于多模态学习的文献综述"

# 状态综述
kimi "调研一下当前大模型推理能力的最新进展"
```

**触发词**: "write literature review", "synthesize papers", "state of the art", "survey"

---

### 4. research-gap-finder
**功能**: 发现研究空白和生成新想法

**使用示例**:
```bash
# 找研究空白
kimi "基于这些论文找出研究空白" ./papers/*.pdf

# 生成研究想法
kimi "生成5个关于LLM推理的创新研究想法"

# 评估想法
kimi "评估以下研究想法的可行性: [你的描述]"
```

**触发词**: "find research gaps", "generate research ideas", "what's missing", "novel ideas"

---

## 组合使用示例

### 完整科研流程

```bash
# 1. 收集论文
kimi "搜索 arXiv 上关于'chain of thought'的最新20篇论文" > papers_list.md

# 2. 分析重点论文
kimi "深度分析这篇论文的方法论" ./key-paper.pdf > analysis.md

# 3. 生成综述
kimi "基于这些分析写一份文献综述" ./analysis.md > review.md

# 4. 发现机会
kimi "基于这份综述找出研究空白和机会" ./review.md > gaps.md

# 5. 生成想法
kimi "基于发现的研究空白生成3个具体的研究提案" ./gaps.md > proposals.md
```

---

## 手动指定 Skill

如果你想明确使用某个 Skill:

```bash
kimi "/skill:arxiv-research 查找论文"
kimi "/skill:paper-analyzer 分析这篇"
kimi "/skill:literature-review 写综述"
kimi "/skill:research-gap-finder 找空白"
```

---

## Skills 位置

这些 Skills 安装在:
```
~/.config/agents/skills/
├── arxiv-research/SKILL.md
├── paper-analyzer/SKILL.md
├── literature-review/SKILL.md
└── research-gap-finder/SKILL.md
```

你可以编辑这些文件来自定义行为。

---

## 故障排除

### Skills 没有触发？
1. 确保使用相关的关键词触发
2. 尝试手动指定: `/skill:skill-name`
3. 检查 Skills 是否正确安装: `ls ~/.config/agents/skills/`

### 想要修改 Skill？
直接编辑对应的 SKILL.md 文件:
```bash
vim ~/.config/agents/skills/arxiv-research/SKILL.md
```

### 添加新的 Skill？
创建新目录和 SKILL.md:
```bash
mkdir ~/.config/agents/skills/my-skill
cat > ~/.config/agents/skills/my-skill/SKILL.md << 'EOF'
---
name: my-skill
description: My custom skill description
---

# My Skill

Your instructions here...
EOF
```

---

## 提示技巧

1. **具体说明需求**: "搜索关于 X 的论文" 比 "找论文" 效果更好
2. **提供上下文**: "基于 Y 方法" 帮助 Kimi 理解背景
3. **指定输出格式**: "用表格形式" 或 "生成 Markdown 报告"
4. **设置约束**: "只看最近一年" 或 "只看顶会论文"

---

## 进阶用法

### 创建项目级 Skills
```bash
mkdir -p ./my-project/.kimi/skills/
cp ~/.config/agents/skills/arxiv-research/SKILL.md ./my-project/.kimi/skills/
# 编辑以适应项目需求
```

### 使用 Flow Skills
创建多步骤自动化流程（需要编写 Mermaid 或 D2 流程图）

### 组合多个 Skills
在一个会话中先后使用多个 Skills 完成复杂任务

---

更多信息和示例:
- Kimi Skills 文档: https://moonshotai.github.io/kimi-cli/zh/customization/skills.html
- Agent Skills 标准: https://agentskills.io/
