# 网络科学史｜全书审校工作台

**全书revision0首轮报告CHANGES_REQUIRED；当前revision2处于P0补稿阶段，正式工作流PENDING，新版本仍未独立双审。**

历史快照：revision0有25篇初稿/9篇占位/267条主张，revision1有28篇/6篇/293条。**revision2新增29—31章后，现有31篇研究性初稿、3篇占位、320条主张**。旧初轮双报告和矩阵只适用于历史基线，新版本的独立事实和结构审校仍未完成。

- [首轮连续性、年代、事实—主张追溯审计](continuity-report.md)（revision_count: 0；status: CHANGES_REQUIRED；列出BLOCKER/HIGH/MEDIUM及选定原刊交叉核查）
- [首轮结构审稿与退修工作包](developmental-review.md)（revision_count: 0；status: CHANGES_REQUIRED；针对全书叙事兑现、重复、9篇缺稿）
- [34篇逐章审校覆盖矩阵](chapter-review-matrix.md)（25篇已成稿及9篇占位、267条主张、锚点覆盖）
- [机器可读审校与修订状态](review-state.json)（已登记revision1，保留原报告revision0历史信息）
- [revision1补稿26—28的历史记录](p0-repair-26-28.md)
- [revision2补稿29—31新增交接与残余阻断](p0-repair-29-31.md) · [修订日志](revision-log.md)

## 重大阻断项

1. **缺稿**：尚缺序章00、第32章和尾声33三篇正文，不能进入全书终审。
2. **上游正式质量闸门**：`workflow-state.json` 仍为 `outline_approved=false`、`evidence_verified=false`、`review_status=PENDING`、`final_approved=false`；严格不得“先过闸再补证”。
3. **主张定位**：01—19章218条已登记主张尚无正文显式ID锚点；24章有一条 `NS-24-09` 未标正文；01章存在旧版claims字段格式差异。
4. **高风险数学史边界**：原始论文与后世标准公式、动态模型的参数假设与教学演算必须逐项复核。

## 审稿顺序与版本纪律

先补缺稿及前置证据 → 统一主张锚点与字段 → 依本轮问题单修订 → 通过 `scripts/workflow_state.py ... new-revision` 在实际修改时使旧审稿意见失效 → 对新版本重新进行连续性/事实审计和发展性结构审稿 → **只有双审真正PASS**，才可以执行line-edit和正式final-approval。

当前两份审校文档由同一轮助手执行的两个审查维度形成，尚未实现两个相互独立审稿人的正式签审。**本目录的CHANGES_REQUIRED为首轮退修判断，工作流权威状态仍保留PENDING**；所有用户都应以 `workflow-state.json` 判断正式发布权限。

未经真实源核与人工审核确认，不得修改 `outline_approved`、`evidence_verified`、`final_approved` 为true，也不允许为了站点外观把chapter状态改成final。

**重要的版本说明**：旧 `qa/continuity-report.md`、`qa/developmental-review.md` 和 `qa/chapter-review-matrix.md` 均针对 revision0；revision1在补齐剩余P0稿件、修复P1追溯和完成实际来源复核后必须生成**新版本的双审报告**，旧 `CHANGES_REQUIRED` 不会自行变成PASS。
**revision2版本纪律**：本轮补齐29—31章是正文交付，不是审稿PASS。旧qa报告仍可作整改依据，却不能当成对本版本独立双审的结论。