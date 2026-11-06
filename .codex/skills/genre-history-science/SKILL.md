---
name: genre-history-science
description: 历史与科学发现专属写作规范；当用户选定历史与科学发现，或当前工作流需要判断其事实来源、历史证据和解释深度时加载。本 Skill 只约束类型风格，不代替选题、构思、写作或审稿阶段。
---
# 类型 Skill｜历史与科学发现

## 入口与职责
- 主类型归档：`articles/nonfiction/history-science/<article-slug>/`。
- 本 Skill 是**类型约束提供者**，非通用阶段执行器；必须结合 `chief-narrative-editor` 与具体阶段 Skill。
- 先读本目录 `prompt.txt`；原始完整版单独保存在 `prompt-original.txt`。
- 进入规划、写作、复审时分别使用 `plan/write/review` 模式；仅 standalone 可以执行原始 prompt 的直接正文指令。
- 作品身份为 nonfiction。规划前必须先调用 fact-research；随后 nonfiction-architect 与 nonfiction-writer，不能使用 chapter-writer 的小说规则。

## 类型验收
- 对齐读者期望，明确题材独有的主问题，不用机械反转替代进展。
- 因果、公理、角色知情时间与正文完全一致。
- 保留可回读的线索与关键选择的真实代价。
- 重大错误交给 revision-manager 处理；当前类型 Skill 不擅自覆盖其他阶段文件。
- 正式文章仅存 `articles/` 下对应作品目录；题材标准保留在 Skill 目录。
