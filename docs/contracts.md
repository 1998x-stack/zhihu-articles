# 作品文件契约与阶段交接（Schema 2.0）

## 核心原则
每个文件有明确主写入者，后继阶段优先**读取、引用、追加独立文件**，而不是无记录覆盖已有产物。必要的结构性改动通过 `revision-manager` 记录请求并回交相应文件所有者。每次修订使旧审稿结论过期。

## 两条独立通道
虚构：
```text
topic-development(brief) → story-architect(outline) → character-world(story-bible)
→ plot-and-clues(plot-ledger) → chapter-writer(draft + chapter-state)
→ continuity-audit → developmental-editor → [revision-manager → 两道复审]*
→ line-edit(edited) → final-approval(final) → publication-package(metadata)
```
非虚构：
```text
topic-development(brief) → fact-research(research) → nonfiction-architect(outline + claim-ledger)
→ nonfiction-writer(draft + claims) → continuity-audit → developmental-editor
→ [fact-research补核 + revision-manager → 两道复审]* → line-edit(edited)
→ final-approval(final) → publication-package(metadata)
```
研究阶段不是虚构的自由补全环节。若历史事实无法核证，缩小论断或暂缓写作。

## 文件所有权与交接表
| 文件 | 主写入 Skill | 主要读者 | 校验要点 |
|---|---|---|---|
| `brief.md` | topic-development | 选定分支全流程 | 唯一题材、读者承诺、编辑性假设 |
| `research.md` | fact-research | 非虚构架构和写作 | 来源、时间、证据范围与争议 |
| `outline.md` | story-architect（虚构）/nonfiction-architect（非虚构） | 所有下游 | 分支互斥；没有二次选题 |
| `story-bible.md` | character-world | 虚构作家及审稿 | 角色、规则、不变量、知情时间 |
| `plot-ledger.md` | plot-and-clues | 虚构作家及审稿 | 线索前置、误导公平、伏笔回收 |
| `claim-ledger.md` | nonfiction-architect | 非虚构作家及审稿 | 每个章节主张与 research 来源对应 |
| `draft/NN.md` | chapter-writer（虚构）/nonfiction-writer（非虚构） | 审稿 | 同一作品只能使用一条分支 |
| `chapter-state.json` | chapter-writer | 虚构续写和核对 | 章号、人物状态、信息和伏笔 |
| `draft/NN.claims.json` | nonfiction-writer | 审稿/事实编辑 | 本章主张标注与证据来源 |
| `qa/continuity-report.md` | continuity-audit | 审稿/修订 | revision_count、冲突位置 |
| `qa/developmental-review.md` | developmental-editor | 修订/终审 | PASS/CHANGES_REQUIRED、阻断项 |
| `revised.md`、`qa/revision-log.md` | revision-manager | 两道复审 | 变更前后及依赖影响 |
| `edited.md` | line-edit | final-approval | 不改变来源、因果或设定 |
| `qa/final-approval.md`、`final.md` | final-approval | publication-package | 同版本审核通过后封版 |
| `metadata.yaml` | publication-package | 归档工具 | 与已封版正文一致 |
| `workflow-state.json` | 主编调度者（阶段事件更新） | gate/所有阶段 | 是机器闸门的明确状态来源 |

## 统一工作状态
`workflow-state.json` 使用 `scripts/workflow_gate.py` 检查，字段：
- `lane`: `fiction` 或 `nonfiction`，一旦开始写作不得悄然更改。
- `current_revision`: 非负整数，每次结构或事实修订必须递增。
- `outline_approved`: bool，结构或证据架构通过后才能 draft。
- `evidence_verified`: bool，非虚构必须为 true 才能 draft/最终封版。
- `review_status`: `PENDING`/`CHANGES_REQUIRED`/`PASS`。
- `reviewed_revision`: 上一次完成两道审稿的修订版本号；必须与 `current_revision` 相同。
- `unresolved_blockers`: 尚未解决的阻断/高优先级错误列表。
- `edited_revision`: 语言编辑所基于的修订版本号。
- `final_approved`: bool，仅终审通过后为 true。

修订事件需要使 `review_status=PENDING`、`reviewed_revision=null`、`edited_revision=null`、`final_approved=false`，并使既有终审/发布结论失效。

## 阶段闸门
- `draft`：结构已批准，分支必备档案存在；非虚构已核实事实。
- `edit`：当前版本的两份审稿报告存在、`review_status=PASS`、版本匹配、无未解决阻断项。
- `final`：edit 闸门和 `edited.md` 满足，语言编辑版本相同。
- `publish`：final 闸门以及终审记录、`final.md`、终审批准状态同时满足。

## 用户已有作品
现存 `articles/` 作品及其状态保持不变。新模板提供 `workflow-state.json`；旧作品只有在准备正式写作/进入审稿闸门时才应迁移状态，不因添加验证器而自动宣布已验收。
