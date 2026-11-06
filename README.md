# 知乎盐选风格原创中文文章工作台

采用 **注意力设计 → 阅读期待管理 → 价值兑现** 的故事与知识叙事结构，覆盖十种题材、虚构/非虚构独立写作流程和审稿修订闭环。本仓库与知乎官方无关联。

## 快速入口
- [完整写作协议](docs/contracts.md) · [分支工作流](docs/workflow.md) · [跨代理兼容说明](docs/compatibility.md)
- [核心主编 Skill](.opencode/skills/chief-narrative-editor/SKILL.md)：深度构思、类型路由、审稿门槛。
- [完整原始主编 Prompt](.opencode/skills/chief-narrative-editor/prompt.txt)：保留 V1.0 全文；历史精简版另存 `prompt-condensed-v1.txt`。
- 十种题材各有 `SKILL.md`、工作流 `prompt.txt` 和完整原版 `prompt-original.txt`。
- 旧工作流 A/B/C 同样保留各自 `prompt-original.txt`。

## 多代理目录
| 工具 | 目录 | 说明 |
|---|---|---|
| OpenCode | `.opencode/skills/` | 维护源和默认项目目录 |
| Pi | `.pi/skills/` | Pi 项目发现目录 |
| Codex | `.agents/skills/` | Codex 标准项目发现目录 |
| 兼容存档 | `.codex/skills/` | 保留此前指定的副本，但不是 Codex 标准自动发现目录 |

四个目录内容逐字节一致。OpenCode 与 Pi 也可能发现 `.agents/skills`，同名定义有确定的优先/警告行为，见 [兼容说明](docs/compatibility.md)。

## 十种题材归档
- **现实逆袭**：`articles/fiction/realistic-comeback/` · `genre-realistic-comeback`
- **职场博弈**：`articles/fiction/workplace-politics/` · `genre-workplace-politics`
- **家庭伦理**：`articles/fiction/family-ethics/` · `genre-family-ethics`
- **悬疑推理**：`articles/fiction/mystery-detective/` · `genre-mystery-detective`
- **古风权谋**：`articles/fiction/historical-intrigue/` · `genre-historical-intrigue`
- **规则怪谈与脑洞**：`articles/fiction/rules-fantasy/` · `genre-rules-fantasy`
- **科幻与AI伦理**：`articles/fiction/ai-scifi/` · `genre-ai-scifi`
- **青春成长**：`articles/fiction/coming-of-age/` · `genre-coming-of-age`
- **历史与科学发现**：`articles/nonfiction/history-science/` · `genre-history-science`
- **社会现实与商业调查**：`articles/nonfiction/social-business/` · `genre-social-business`

## 两条写作流水线
**虚构：** `topic-development → story-architect → character-world → plot-and-clues → chapter-writer → continuity-audit → developmental-editor → [revision-manager + 复审]* → line-edit → final-approval → publication-package`

**非虚构：** `topic-development → fact-research → nonfiction-architect → nonfiction-writer → continuity-audit → developmental-editor → [fact-research 补核 + revision-manager + 复审]* → line-edit → final-approval → publication-package`

每篇文章保留 `brief.md`、`outline.md`、章稿、证据/伏笔文件、`workflow-state.json`、独立审稿报告与最终审定稿。旧作品保留现状，无自动状态升级。

## 仓库目录（节选）
```text
zhihu-articles/
├── .opencode/skills/           # 主维护源
├── .pi/skills/                 # Pi 副本
├── .agents/skills/             # Codex 可发现副本
├── .codex/skills/              # 兼容存档
├── articles/
│   ├── fiction/
│   ├── nonfiction/
│   └── _template/
├── docs/contracts.md
├── docs/workflow.md
├── docs/compatibility.md
├── catalog.json
├── workflow.json
└── scripts/
```

## 维护与验证
```bash
python scripts/sync_skills.py --check
python scripts/sync_skills.py --write
python scripts/validate_repo.py
python scripts/workflow_state.py <article_dir> new-revision --reason "修复审稿阻断项"
python -m unittest discover -s scripts -p 'test_*.py'
```
GitHub Actions 执行结构、镜像、流程契约与状态机模拟测试。它们不验证实际中文文学品质或平台收录，成稿仍需编辑审查与来源核对。

## 使用方式
在仓库根目录运行适用的代理，要求先加载 `chief-narrative-editor`，再选定主类型 Skill 与当前阶段 Skill。先创作和审核可供复核的方案，再根据分支生成正文。保留用户提供的现有书稿和草稿；未完成的章稿不能直接设为 final。
