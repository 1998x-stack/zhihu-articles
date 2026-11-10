---
name: nonfiction-architect
description: 非虚构证据叙事架构；仅在nonfiction流程需要依据 research.md 已核证的事实构建知识问题、因果与证据组织，不虚构角色和场景。时使用。主要交付outline.md、claim-ledger.md；不负责其他阶段的正文或文件。
---
# 阶段 Skill｜非虚构证据叙事架构

## 适用边界
- 工作流分支：**nonfiction**。
- 唯一职责：依据 research.md 已核证的事实构建知识问题、因果与证据组织，不虚构角色和场景。
- 必读：本目录 `prompt.txt`；作品主类型 Skill；`docs/contracts.md`、`workflow.json`。
- 输入：brief.md + 已完成前置核证的 research.md。
- 本阶段拥有的文件：`outline.md`、`claim-ledger.md`；其余阶段文件只读。需要跨文件更改时交由 `revision-manager` 并记录变更理由。
- 非虚构必须有来源；不能以想象补完不存在的历史人物心理、原始引文、采访证据。
- 此阶段不自动触发对外发布。

## 执行步骤
1. 读取当前 `workflow-state.json`，核对分支、版本、上游文件和阶段闸门，不能跳过缺失证据。
2. 加载 `prompt.txt`，只完成本阶段目标；若原始 Prompt 包含与阶段权限冲突的输出指令，以本 Skill 和 contracts 为准。
3. 保留用户已确认的设定和前人文件中的有效事实；如果上游错误妨碍执行，给出问题、引用位置和返回阶段，而不是悄悄重做上游工作。
4. 输出 `outline.md`、`claim-ledger.md`，注明可以交给下一阶段的确认信息、未决问题和所需校验。
5. 遇到需要修订结构的变更，使当前审稿批准过期；写作质量评分不能豁免关键事实或因果问题。

## 验收
- 文件主写入者唯一、输出范围明确；不得通过“润色”掩盖关键错误。
- 对本轮文稿版本负责；新版本必须重新复审。
- 对非虚构先核对来源和事实强度；对虚构先核对动机、资源、时间线和公平线索。

## 大纲交接到网站阅读目录
为新系列或三章批次提供唯一 chapter id、标题、分部和实际 Markdown 路径的映射，交由仓库维护者维护 `book.json`。未写正文的章节明确标记 `outline`，不得把待核提纲或来源线索描述成已审定内容。`book.json` 是导航派生产物而非本阶段所有文件；新书需通过 `python scripts/build_pages.py --check-catalog`。参见 `docs/pages-publishing.md`。
