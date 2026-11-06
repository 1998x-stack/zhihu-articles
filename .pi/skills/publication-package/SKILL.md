---
name: publication-package
description: 发布包装与归档；仅在fiction 与 nonfiction流程需要仅对已批准终稿设计标题、摘要、标签和状态更新，不再写 final.md。时使用。主要交付metadata.yaml；不负责其他阶段的正文或文件。
---
# 阶段 Skill｜发布包装与归档

## 适用边界
- 工作流分支：**fiction 与 nonfiction**。
- 唯一职责：仅对已批准终稿设计标题、摘要、标签和状态更新，不再写 final.md。
- 必读：本目录 `prompt.txt`；作品主类型 Skill；`docs/contracts.md`、`workflow.json`。
- 输入：final.md、qa/final-approval.md、metadata.yaml。
- 本阶段拥有的文件：`metadata.yaml`；其余阶段文件只读。需要跨文件更改时交由 `revision-manager` 并记录变更理由。
- 非虚构必须有来源；不能以想象补完不存在的历史人物心理、原始引文、采访证据。
- 此阶段不自动触发对外发布。

## 执行步骤
1. 读取当前 `workflow-state.json`，核对分支、版本、上游文件和阶段闸门，不能跳过缺失证据。
2. 加载 `prompt.txt`，只完成本阶段目标；若原始 Prompt 包含与阶段权限冲突的输出指令，以本 Skill 和 contracts 为准。
3. 保留用户已确认的设定和前人文件中的有效事实；如果上游错误妨碍执行，给出问题、引用位置和返回阶段，而不是悄悄重做上游工作。
4. 输出 `metadata.yaml`，注明可以交给下一阶段的确认信息、未决问题和所需校验。
5. 遇到需要修订结构的变更，使当前审稿批准过期；写作质量评分不能豁免关键事实或因果问题。

## 验收
- 文件主写入者唯一、输出范围明确；不得通过“润色”掩盖关键错误。
- 对本轮文稿版本负责；新版本必须重新复审。
- 对非虚构先核对来源和事实强度；对虚构先核对动机、资源、时间线和公平线索。
