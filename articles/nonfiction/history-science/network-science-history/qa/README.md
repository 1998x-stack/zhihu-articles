# 网络科学史｜全书审校工作台

**首轮正式审校已启动（2026-11-10），结论：需修订（CHANGES_REQUIRED），未取得正式独立双审批准。**

全书34篇：**25篇实际研究性工作初稿，9篇只有策划占位**。现有267条章级主张、25篇原稿纳入首轮文档一致性/结构评估；原始文献逐页核证尚未完成。下列文件用于可审计地交接真实问题，不是全书PASS或发布许可。

- [首轮连续性、年代、事实—主张追溯审计](continuity-report.md)（revision_count: 0；status: CHANGES_REQUIRED；列出BLOCKER/HIGH/MEDIUM及选定原刊交叉核查）
- [首轮结构审稿与退修工作包](developmental-review.md)（revision_count: 0；status: CHANGES_REQUIRED；针对全书叙事兑现、重复、9篇缺稿）
- [34篇逐章审校覆盖矩阵](chapter-review-matrix.md)（25篇已成稿及9篇占位、267条主张、锚点覆盖）
- [机器可读审校启动快照](review-state.json)（单列工作阶段，绝不篡改正式稿件审批）

## 重大阻断项

1. **缺稿**：序章00、第26—32章、尾声33尚未形成可送审正文。全书不具备封版条件。
2. **上游正式质量闸门**：`workflow-state.json` 仍为 `outline_approved=false`、`evidence_verified=false`、`review_status=PENDING`、`final_approved=false`；严格不得“先过闸再补证”。
3. **主张定位**：01—19章218条已登记主张尚无正文显式ID锚点；24章有一条 `NS-24-09` 未标正文；01章存在旧版claims字段格式差异。
4. **高风险数学史边界**：原始论文与后世标准公式、动态模型的参数假设与教学演算必须逐项复核。

## 审稿顺序与版本纪律

先补缺稿及前置证据 → 统一主张锚点与字段 → 依本轮问题单修订 → 通过 `scripts/workflow_state.py ... new-revision` 在实际修改时使旧审稿意见失效 → 对新版本重新进行连续性/事实审计和发展性结构审稿 → **只有双审真正PASS**，才可以执行line-edit和正式final-approval。

当前两份审校文档由同一轮助手执行的两个审查维度形成，尚未实现两个相互独立审稿人的正式签审。**本目录的CHANGES_REQUIRED为首轮退修判断，工作流权威状态仍保留PENDING**；所有用户都应以 `workflow-state.json` 判断正式发布权限。

未经真实源核与人工审核确认，不得修改 `outline_approved`、`evidence_verified`、`final_approved` 为true，也不允许为了站点外观把chapter状态改成final。
