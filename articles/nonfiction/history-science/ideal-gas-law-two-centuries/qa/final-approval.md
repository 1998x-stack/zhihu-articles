# 终审前置核查记录｜final-approval

revision_count: 1
approved: false
status: HOLD_FORMAL_GATE_NOT_EXECUTED
date: 2026-11-06
manuscript: edited.md

## 一、终审前置条件已核查

| 条件 | 结果 | 可核文件 |
|---|---|---|
| nonfiction事实前置证据标志 | **已满足**，evidence_verified=true | workflow-state.json，research.md |
| 正式章纲 | **已满足**，outline_approved=true | outline.md |
| 当前修订版本 | **1** | workflow-state.json，revised.md |
| 连续性复审 | **PASS，revision_count=1** | qa/continuity-report.md |
| 发展性结构复审 | **PASS，revision_count=1** | qa/developmental-review.md |
| 当前审稿状态 | **PASS，reviewed_revision=1** | workflow-state.json |
| 未解决高优先级问题 | **0**，unresolved_blockers=[] | workflow-state.json |
| 精修稿版本 | **edited_revision=1**，edited.md已存在且非空 | edited.md、workflow-state.json |
| 精修稿完整性 | **17个章节标题、306个不同的来源主张标记、136处数学公式块**；主张均可在全书账本索引 | edited.md、claim-ledger.md、draft/NN.claims.json |
| 变更记录 | **完整**，首轮两份报告归档，S87增量事实核查与rev1修订日志可查 | qa/revision-log.md，qa/history/，research.md |

## 二、终审禁止越过的门槛

按照仓库`final-approval` Skill，**必须实际运行**

```bash
python scripts/workflow_gate.py articles/nonfiction/history-science/ideal-gas-law-two-centuries --target final
```

当前环境的本地容器无法从GitHub克隆真实工作树（网络域名解析失败），仅能通过已连接的GitHub接口读取并修改文件。已经对状态与文件进行的**远程等价字段检查不等于执行了仓库本身的workflow_gate.py**，不得标记其输出为PASS。正式门禁的运行日志或其他可核凭据目前未取得。

另外，rev0/rev1两个审稿阶段属于按不同仓库Skill执行的**两份独立职责报告**，并非已经由两个外部人类专家分别签字；如有出版级同行外审要求，应另行安排。

## 三、本轮终审决定

- **approved: false**，理由：**未取得正式工作树上的`workflow_gate.py --target final`通过凭据**。本报告不为文字质量或史实提供额外的终审批准。
- **不生成`final.md`**，不更新`final_approved=true`，不生成出版封版文件。
- 保持`edited.md`为可送终审的整书精修合订稿，保留306条证据索引。
- 下一步在可运行仓库脚本的环境取得实际`PASS: final gate`，并按`final-approval`规则逐项核对格式、科学事实与同版本审稿记录；只有通过才可重新评估本报告、封版`final.md`。当前仍不对外发布。
