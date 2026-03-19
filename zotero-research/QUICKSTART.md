# Zotero Research Skill - 快速入门指南

## ✅ 安装完成

你的 Zotero Research Skill 已成功安装！

**位置**: `~/.claude/skills/zotero-research/`

---

## 🚀 第一步：添加文献到 Zotero

由于你的 Zotero 数据库目前为空，首先需要添加一些文献：

### 方法 1：浏览器插件（推荐）
1. 安装 Zotero Connector 浏览器插件
2. 访问学术网站（Google Scholar, arXiv, PubMed 等）
3. 点击插件图标一键保存文献

### 方法 2：手动导入
1. 打开 Zotero 桌面应用
2. 文件 → 导入
3. 选择 BibTeX/CSV 文件或 PDF 文件

### 方法 3：从 arXiv 批量导入
```bash
# 使用之前安装的 arxiv-research skill 下载文献元数据
# 然后导入 Zotero
```

---

## 📖 常用命令

### 查看库统计
```bash
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --stats
```

### 列出所有集合
```bash
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --collections
```

### 列出所有标签
```bash
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --tags
```

### 搜索文献
```bash
# 关键词搜索
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --query "machine learning"

# 作者搜索
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --author "Bengio"

# 标签搜索
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --tag "deep-learning"

# 综合搜索
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --query "transformer" --tag "attention" --limit 10
```

### 生成文献综述
```bash
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --query "reinforcement learning" --limit 20 --output rl_review.md
```

### 导出为 BibTeX
```bash
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --query "robotics" --export bibtex --output robotics.bib
```

---

## 💡 在 Claude 中使用

### 直接询问
```
"搜索我的 Zotero 中关于 multi-agent 的论文"

"列出我最近添加的 AI 相关文献"

"生成一份关于 transformer 的文献综述"

"查找 Bengio 的所有论文"
```

### 结合其他技能
```
"从我的 Zotero 搜索 RAG 相关论文，然后用 ai-llamaindex 建索引"

"找到我的论文中关于 Chain-of-Thought 的，总结最新进展"
```

---

## 📁 推荐的工作流

### 1. 日常文献收集
```
浏览器看到好论文 → Zotero Connector 保存 → 自动同步到本地库
```

### 2. 定期文献整理
```bash
# 每周运行一次
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --since $(date -v-7d +%Y-%m-%d) --output weekly_papers.md
```

### 3. 项目文献管理
```bash
# 为特定项目创建集合，然后搜索
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --collection "PhD Thesis" --query "attention mechanism"
```

### 4. 写作时引用
```bash
# 导出特定主题的 BibTeX
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --tag "to-cite" --export bibtex --output references.bib
```

---

## 🔧 故障排除

### "Could not find Zotero database"
- 确保已运行 Zotero 桌面应用至少一次
- 检查 `~/Library/Application Support/Zotero/` 是否存在

### "Database is locked"
- 关闭 Zotero 桌面应用后再运行搜索
- 或使用 `--copy-db` 参数：
```bash
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --query "AI" --copy-db
```

### 搜索结果为空
- 确认 Zotero 中有文献
- 尝试更简单的关键词
- 使用 `--tags` 查看可用的标签

---

## 🎯 高级技巧

### 1. 结合 grep 过滤
```bash
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --query "transformer" --format json | grep -i "attention"
```

### 2. 定时自动备份
```bash
# 添加到 crontab，每周备份文献列表
0 9 * * 1 python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --format json --output ~/backup/zotero_backup_$(date +\%Y\%m\%d).json
```

### 3. 与其他工具集成
```bash
# 导出到 Notion/Obsidian
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py \
  --query "PhD" --format markdown --output ~/Obsidian/papers.md
```

---

## 📚 下一步

1. **添加文献**: 使用 Zotero Connector 添加 5-10 篇文献
2. **测试搜索**: 运行 `--stats` 和 `--query` 命令
3. **创建集合**: 在 Zotero 中创建项目集合
4. **添加标签**: 为文献添加标签以便检索

---

需要帮助？使用以下命令获取帮助：
```bash
python3 ~/.claude/skills/zotero-research/scripts/zotero_search.py --help
```
