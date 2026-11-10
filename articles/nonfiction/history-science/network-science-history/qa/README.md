# 网络科学史｜全书审校工作台

**全书revision3已完成34篇研究性初稿覆盖；revision0首轮报告CHANGES_REQUIRED为历史退修快照。当前正式工作流仍为PENDING，没有独立全书双审或封版许可。**

历史快照：revision0为25初稿/9占位/267主张，revision1为28/6/293，revision2为31/3/320。**revision3补齐序章、第32章及尾声：34篇研究性工作初稿、0篇占位、347条主张**。旧双报告和矩阵只针对revision0，不能被视为revision3已独立审核。

- [首轮连续性、年代、事实—主张追溯审计](continuity-report.md)（revision_count: 0；status: CHANGES_REQUIRED；列出BLOCKER/HIGH/MEDIUM及选定原刊交叉核查）
- [首轮结构审稿与退修工作包](developmental-review.md)（revision_count: 0；status: CHANGES_REQUIRED；针对全书叙事兑现、重复、9篇缺稿）
- [34篇逐章审校覆盖矩阵](chapter-review-matrix.md)（25篇已成稿及9篇占位、267条主张、锚点覆盖）
- [机器可读审校与修订状态](review-state.json)（已登记revision1，保留原报告revision0历史信息）
- [revision1补稿26—28的历史记录](p0-repair-26-28.md)
- [revision2补稿29—31历史交接](p0-repair-29-31.md)
- [revision3全书P0补稿与余项登记](p0-repair-00-32-33.md)
- [34篇可审文本及阻断项准入清单（revision3）](full-manuscript-intake-r3.md) · [修订日志](revision-log.md)

## 重大阻断项

1. **缺稿子项已关闭**：34篇均有实质研究性初稿；但整书正式验收仍需事实、结构及来源复审，不能因缺稿为零认定出版阻断消失。
2. **上游正式质量闸门**：`workflow-state.json` 仍为 `outline_approved=false`、`evidence_verified=false`、`review_status=PENDING`、`final_approved=false`；严格不得“先过闸再补证”。
3. **主张定位**：01—19章218条已登记主张尚无正文显式ID锚点；24章有一条 `NS-24-09` 未标正文；01章存在旧版claims字段格式差异。
4. **高风险数学史边界**：原始论文与后世标准公式、动态模型的参数假设与教学演算必须逐项复核。

## 审稿顺序与版本纪律

先补缺稿及前置证据 → 统一主张锚点与字段 → 依本轮问题单修订 → 通过 `scripts/workflow_state.py ... new-revision` 在实际修改时使旧审稿意见失效 → 对新版本重新进行连续性/事实审计和发展性结构审稿 → **只有双审真正PASS**，才可以执行line-edit和正式final-approval。

当前两份审校文档由同一轮助手执行的两个审查维度形成，尚未实现两个相互独立审稿人的正式签审。**本目录的CHANGES_REQUIRED为首轮退修判断，工作流权威状态仍保留PENDING**；所有用户都应以 `workflow-state.json` 判断正式发布权限。

未经真实源核与人工审核确认，不得修改 `outline_approved`、`evidence_verified`、`final_approved` 为true，也不允许为了站点外观把chapter状态改成final。

**重要的版本说明**：旧 `qa/continuity-report.md`、`qa/developmental-review.md` 和 `qa/chapter-review-matrix.md` 均针对 revision0；revision1在补齐剩余P0稿件、修复P1追溯和完成实际来源复核后必须生成**新版本的双审报告**，旧 `CHANGES_REQUIRED` 不会自行变成PASS。
**revision2版本纪律**：本轮补齐29—31章是正文交付，不是审稿PASS。旧qa报告仍可作整改依据，却不能当成对本版本独立双审的结论。
**revision3状态分界**：P0缺正文子任务完成，下一轮P1高优先级为01—19章218条行内ID追踪、第24章NS-24-09、第01章旧claims schema、跨章数学与原刊证明核查；同时检查第00、32、33章的历史事实和认识边界。`workflow-state.json`仍为唯一正式审批来源。
