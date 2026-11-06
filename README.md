# 知乎盐选风格原创写作工作台

> 用**注意力设计 → 阅读期待管理 → 价值兑现**组织原创中文短篇及知识叙事。

本仓库用于管理写作提示词、OpenCode 项目 Skills、文章分类、创作档案与独立审稿；不是知乎官方规则库，不保证平台收录、收益或发布。

## 快速使用

1. 在仓库根目录打开 OpenCode；项目 Skills 会从 `.opencode/skills/<name>/SKILL.md` 被发现。
2. 让代理加载 `chief-narrative-editor`，确定主题、题材和虚构/非虚构边界。
3. 再加载相应的 `genre-*` Skill，并完整读取该 Skill 的 `prompt.txt`。
4. 按阶段调用选题、故事架构、人物世界观、伏笔设计、资料核验（需要时）、分章写作、一致性审计、结构审稿、文字精修和终稿归档。
5. 将具体作品放进 `articles/<fiction|nonfiction>/<genre>/<article-slug>/`，使用 `articles/_template/` 中的文件作为起点。

示例对话：「请加载 chief-narrative-editor 和 genre-mystery-detective，先调用 story-architect，为一个8000字、以身份谜团为核心的原创故事制作 brief、story-bible、outline；确认逻辑成立之后再分章写作。」

## 分类目录

| 分类 | 归档目录 | Skills |
| --- | --- | --- |
| 现实逆袭 | `articles/fiction/realistic-comeback/` | `genre-realistic-comeback` |
| 职场博弈 | `articles/fiction/workplace-politics/` | `genre-workplace-politics` |
| 家庭伦理 | `articles/fiction/family-ethics/` | `genre-family-ethics` |
| 悬疑推理 | `articles/fiction/mystery-detective/` | `genre-mystery-detective` |
| 古风权谋 | `articles/fiction/historical-intrigue/` | `genre-historical-intrigue` |
| 规则怪谈与脑洞 | `articles/fiction/rules-fantasy/` | `genre-rules-fantasy` |
| 科幻与AI伦理 | `articles/fiction/ai-scifi/` | `genre-ai-scifi` |
| 青春成长 | `articles/fiction/coming-of-age/` | `genre-coming-of-age` |
| 历史与科学发现 | `articles/nonfiction/history-science/` | `genre-history-science` |
| 社会现实与商业调查 | `articles/nonfiction/social-business/` | `genre-social-business` |

## 技能目录

- 核心总控：`.opencode/skills/chief-narrative-editor/`（原通用 Prompt V1.0，强化深度构思、因果反推和跨类型路由）
- 题材专属：10 个 `genre-*` Skill（每个都有完整 `SKILL.md` + 来自 V2.0 的原始 `prompt.txt`）
- 写作阶段：`topic-development`、`story-architect`、`character-world`、`plot-and-clues`、`fact-research`、`chapter-writer`、`continuity-audit`、`developmental-editor`、`line-edit`、`publication-package`（每个都有独立 `prompt.txt`）

原有 V2.0 的三个阶段 Prompt 分别保存在 `story-architect`（Prompt A）、`chapter-writer`（Prompt B）、`developmental-editor`（Prompt C）。

## 创作阶段与产物

| 阶段 | Skill | 主要产物 |
| --- | --- | --- |
| 选题开发与定位 | `topic-development` | `brief.md` |
| 故事策划与结构蓝图 | `story-architect` | `outline.md` |
| 人物世界观与约束系统 | `character-world` | `story-bible.md` |
| 因果链悬念伏笔工程 | `plot-and-clues` | `outline.md` |
| 非虚构资料核验与证据边界 | `fact-research` | `research.md` |
| 分章写作执行 | `chapter-writer` | `draft/NN.md` |
| 跨章连续性与事实一致性审计 | `continuity-audit` | `qa-report.md` |
| 结构审稿与修订 | `developmental-editor` | `qa-report.md` |
| 语言节奏与文学性精修 | `line-edit` | `final.md` |
| 终稿包装与归档 | `publication-package` | `metadata.yaml` |

作品建议的目录结构（实际作品需新建独立 slug 目录）：

```text
articles/fiction/mystery-detective/<article-slug>/
├── metadata.yaml
├── brief.md
├── story-bible.md
├── research.md
├── outline.md
├── draft/
│   ├── 01.md
│   └── 02.md
├── qa-report.md
└── final.md
```

模板位于 `articles/_template/`。非虚构强制维护 `research.md` 和来源矩阵。**文章存放在 articles，指令存放在 .opencode/skills，二者不要混用。**

## 质量标准

- 开头有可兑现的真实问题，中段每一幕有实际推进，结尾兑现情绪或认知承诺。
- 结构问题优先于语言问题；重大逻辑漏洞不得凭文字润色掩盖。
- 历史、科学、现实调查不虚构事实、采访或参考文献；无法核实之处应明确标注。
- 评分参考：开篇15、节奏15、信息差15、人物15、逻辑20、情绪与价值10、语言10（非官方，非虚构另需事实核验）。

## 验证

运行 `python scripts/validate_repo.py` 检查 Skills frontmatter、配套 Prompt、分类和模板的结构完整性。GitHub Actions 会在提交时自动执行同一检查。

更多详见 `AGENTS.md`、`docs/editorial-standards.md`、`catalog.json`。
