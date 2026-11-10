# AGENTS.md｜OpenCode、Pi、Codex 共同写作协议

本仓库采用主编统筹 + **严格阶段交付** 的写作体系，避免一次性生成导致剧情因果或史料边界失控。

## 入口
- 主控：`chief-narrative-editor`（对应根目录 `catalog.json`）。
- 类型规则：从10种 `genre-*` Skills 中选择主类型，最多辅助一到两种副类型，但不可覆盖主类型的证据约束。
- 写作分支：**fiction / nonfiction 必须先确定**。不能用虚构小说的分章写作器处理历史科学或调查文章。
- Codex 自动加载的标准 Skill 路径是 `.agents/skills/`；OpenCode 使用 `.opencode/skills/`；Pi 使用 `.pi/skills/`。另保留 `.codex/skills/` 兼容性副本。四套内容相同。
- 同名 Skill 在 Pi 和 OpenCode 的兼容路径可能被重复发现；名称和内容完全一致，按各平台优先级选择。详见 `docs/compatibility.md`。

## 必要协议
1. 先读 `docs/contracts.md`、`workflow.json` 和核心 Skill；再加载目标类型和当下阶段。
2. `topic-development` 只做**一次三方案比较**并形成 brief；后续步骤不得反复重新选题。
3. **非虚构**：`topic-development → fact-research → nonfiction-architect → nonfiction-writer`，史实先于架构。**虚构**：`topic-development → story-architect → character-world → plot-and-clues → chapter-writer`。
4. 每一阶段只拥有自己的产物写入权，遵循 `docs/contracts.md`。不要越权覆盖旧大纲、审稿报告或终稿。
5. 连续性审计和独立结构审稿必须是不同报告：`qa/continuity-report.md` 与 `qa/developmental-review.md`。
6. 审稿未通过：`revision-manager` 修改 → 旧审稿失效 → `continuity-audit` 与 `developmental-editor` 针对新版本再次审核，直到通过或明确无法修复。
7. 仅在最新审稿通过后运行 `line-edit`，输出 `edited.md`；由 `final-approval` 独占生成 `final.md`；发布包装只编辑 `metadata.yaml`。
8. 执行写作或验收前按阶段使用 `python scripts/workflow_gate.py <article_dir> --target draft|edit|final|publish`；记录 `workflow-state.json`。自动校验只是机器闸门，不代替人工/模型实际审稿。
9. 版本流转通过 `scripts/workflow_state.py` 显式执行：新修订使旧审稿失效，审稿通过、提纲批准及最终封版必须基于实际审核后明确确认，不可跳过。
10. 章节写作必须更新 `chapter-state.json`；非虚构必须在章节中保留 claim 到来源的可追溯对应。
11. 不能编造证据、原始引文、采访或真实人物私下心理；未授权不得对外发布或假称已获平台收录。


## GitHub Pages 系列收录与章节导航
- **两种不同的“发布”**：GitHub Pages 允许明确标记的未审工作初稿和占位目录供阅读，**不等于**知乎平台发布、事实核验通过或 `final-approval`。正式出版仍须遵守 `workflow_gate.py --target publish`，不得因网页可读而自行修改 `final_approved`。
- **新书登记的原子交付**：目录 `articles/<fiction|nonfiction>/<genre>/<slug>/` 下必须有 `README.md` 和 `book.json`（建议同时维护 `metadata.yaml`）。`book.json` 的 `schema_version=1`，`id` 与 slug 一致，章节须逐条声明 `id/title/part/file/status`，不得批量曝光 research、claims、QA 或提示词。
- **三章一批联动**：章节 Agent 交付 Markdown、证据记录及章节编号/标题/分部/源路径/状态；主编或仓库维护者核对并同步 `book.json`。`outline` 是占位，`draft` 是工作初稿，`final` 只给确已批准的章节。新增章节不自动晋升审稿状态。
- **网站自动发现**：`scripts/build_pages.py` 扫描 `catalog.json` 的归档路径，将新作品自动加入书架。已有 `site/assets/data/books.json` 是可选的陈列定制，不再是唯一入口；缺封面使用文字封面。
- **必须验证**：`python scripts/build_pages.py --check-catalog`、`python scripts/sync_skills.py --check`、`python -m unittest discover -s scripts -p 'test_*.py'`。新系列缺 `book.json` 时必须构建失败，不能静默跳过。合并后检查 GitHub Actions 的 Pages build、deploy 和站内书籍/章节路由。详见 `docs/pages-publishing.md`。

## 章节进度同步（每一批均必须执行）
- 一章进入真实工作初稿时，由主编/仓库维护者根据实际正文、章级来源记录**明确更新**该系列 \`book.json\` 的 \`chapters[].status\`（\`outline\` → \`draft\`）；并同步原有 \`chapter-state.json\` 的详细章级字段。不可仅凭文件大小批量晋升，\`proposals/\` 候审稿仍须单独统计。
- 完成正文与书籍清单同步后执行 \`python scripts/check_series_progress.py --write\`：只更新所有系列 README 的机器进度区块及 \`chapter-state.json.progress_summary\` 派生快照，不会篡改 \`book.json\`、\`workflow-state.json\`、审稿结果或正文。
- 提交前执行 \`python scripts/check_series_progress.py --check\` 与 \`python scripts/build_pages.py --check-catalog\`；\`validate.yml\` 与 \`pages.yml\` 均会阻断陈旧的书目状态、README 进度和章级派生快照。详细见 \`docs/pages-publishing.md\`。
- 旧有 chapter-state 可能仅追踪某一批次的连续性记录；允许其覆盖范围不完整，但**已记录的**章节与主工作流版本、审稿状态必须一致。未创建该文件的系列会生成仅用于同步的衍生摘要，绝不能假称续写检查或审稿已实际发生。
- \`site/assets/data/books.json\` 只保留人工编辑的封面与长期有效简介，不维护 \`status\`、\`note\` 等易过期进度；公开书架在构建时按 \`book.json\` 自动计算，避免双重事实源。

## 原始 Prompt 保存
核心通用 Prompt 的原始完整版为 `chief-narrative-editor/prompt.txt`；过去的精简版存为 `prompt-condensed-v1.txt`。十套题材 Prompt 的原文在各自 `prompt-original.txt`，阶段旧版 A/B/C 亦在对应目录保留。分阶段执行时优先遵循阶段输入输出权限，而不是照搬原始 Prompt 的“立即输出全文”。

## 修改 Skills
`python scripts/sync_skills.py --write` 同步四套目录；`python scripts/validate_repo.py` 核验同步与协议；`python -m unittest discover -s scripts -p 'test_*.py'` 验证流程闸门。不得把结构检查成功冒称为实际创作质量或平台自动发现已实机测试成功。
