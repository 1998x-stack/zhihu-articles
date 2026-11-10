---
name: nonfiction-writer
description: 非虚构分章写作；仅在nonfiction流程需要依据证据矩阵撰写历史科学和调查章节，逐条记录主张来源和待核事项。时使用。主要交付draft/NN.md、draft/NN.claims.json；不负责其他阶段的正文或文件。
---
# 阶段 Skill｜非虚构分章写作

## 适用边界
- 工作流分支：**nonfiction**。
- 唯一职责：依据证据矩阵撰写历史科学和调查章节，逐条记录主张来源和待核事项。
- 必读：本目录 `prompt.txt`；作品主类型 Skill；`docs/contracts.md`、`workflow.json`。
- 输入：outline.md、research.md、claim-ledger.md、当前章节。
- 本阶段拥有的文件：`draft/NN.md`、`draft/NN.claims.json`；其余阶段文件只读。需要跨文件更改时交由 `revision-manager` 并记录变更理由。
- 非虚构必须有来源；不能以想象补完不存在的历史人物心理、原始引文、采访证据。
- 此阶段不自动触发对外发布。

## 执行步骤
1. 读取当前 `workflow-state.json`，核对分支、版本、上游文件和阶段闸门，不能跳过缺失证据。
2. 加载 `prompt.txt`，只完成本阶段目标；若原始 Prompt 包含与阶段权限冲突的输出指令，以本 Skill 和 contracts 为准。
3. 保留用户已确认的设定和前人文件中的有效事实；如果上游错误妨碍执行，给出问题、引用位置和返回阶段，而不是悄悄重做上游工作。
4. 输出 `draft/NN.md`、`draft/NN.claims.json`，注明可以交给下一阶段的确认信息、未决问题和所需校验。
5. 遇到需要修订结构的变更，使当前审稿批准过期；写作质量评分不能豁免关键事实或因果问题。

## 验收
- 文件主写入者唯一、输出范围明确；不得通过“润色”掩盖关键错误。
- 对本轮文稿版本负责；新版本必须重新复审。
- 对非虚构先核对来源和事实强度；对虚构先核对动机、资源、时间线和公平线索。

## 三章一批与书架索引交接
本阶段只写本章正文与 claim 证据映射；每批交接实际章号、题名、分部、Markdown 源路径、仍待审的 `draft` 状态，由主编/仓库维护者据此更新站点 `book.json`，不扩大写入权。新增系列须有 `README.md + book.json` 并执行 `python scripts/build_pages.py --check-catalog`；不因网页可读而宣称出版或已通过双审。详见 `docs/pages-publishing.md`。

## 每批章节进度自动核验
写作 Agent 交接真实正文、章级证据和 `book.json` 的对应条目状态，由主编/维护者按事实更新；仅为 `proposals/` 生成的候审稿不可冒充正式 `draft`。每批更新后执行 `python scripts/check_series_progress.py --write` 和 `python scripts/check_series_progress.py --check`，同步 README 与 `chapter-state.json.progress_summary`，并通过 `scripts/build_pages.py --check-catalog`。派生快照绝不授予正式双审、终稿封版或外部发布许可。详见 `docs/pages-publishing.md`。
