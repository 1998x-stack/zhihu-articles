# OpenCode / Pi / Codex 兼容性说明

| 引擎 | 默认项目级发现路径 | 本仓库路径 |
|---|---|---|
| OpenCode | `.opencode/skills/<name>/SKILL.md`（也扫描 `.agents/skills`） | `.opencode/skills` |
| Pi | `.pi/skills/<name>/SKILL.md`（也扫描 `.agents/skills`） | `.pi/skills` |
| Codex | `.agents/skills/<name>/SKILL.md` | `.agents/skills` |

保留 `.codex/skills` 是为了延续用户要求的历史副本，**不要将该目录误写成 Codex 的标准自动发现路径**。四份文件全部字节一致，`.opencode/skills` 作为维护源。

## 已知兼容性取舍：同名发现
因为同时保留独立的 OpenCode / Pi 技能目录和共享 `.agents/skills` 目录，OpenCode 与 Pi **可能同时发现两个同名的定义**。OpenCode 根据来源优先级选择项目 `.opencode/skills`；Pi 会对重名发出警告并保留先发现项。此处保留冗余副本是为了满足三个工具目录均可直接查看、复制、独立使用的需求；同步校验保证无实际内容差异，但不消除 Pi 的重名提示。

若团队更看重「零重名警告」，可在以后仅保留 `.agents/skills` 为有 SKILL.md 的实际发现目录，把其余副本移至不会被扫描的归档位置；这需要改变当前用户指定的路径约束。

## 使用注意
- Skills 只被发现和按需加载，不会自动替代写作流程调度；切换阶段需遵循 `workflow.json` 及 `workflow-state.json`。
- `prompt.txt` 是配套资源，各工具不保证自动载入，Skill 指令明确要求先读取它。
- 按同目录相对路径读取资源，避免把 `.opencode` 写死为唯一读取根目录。
- 审稿分数只供编辑参考，不能跳过引用与一致性审查。
- 本仓库目前通过 GitHub 上的静态结构及模拟状态闸门测试；没有实机证明三个不同客户端的技能选择或文学质量。

文档参考：
- https://opencode.ai/docs/skills
- https://learn.chatgpt.com/docs/build-skills
- https://pi.ubitools.com/skills/
