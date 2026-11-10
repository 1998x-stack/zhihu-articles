# 网络科学史｜退修变更日志

## 2026-11-10｜revision0 → revision1｜P0填补第26—28章

**修订理由**：依据revision0初轮连续性报告 \`NS-CONT-B01\` 与结构报告 \`NS-DEV-B01/H05\`，完成仍为占位的第26—28章，建立可审阅的第六部完整后半部分。新增三篇研究性初稿、26条来源/教学主张，延续第25章向第29章的问题链。

**变更范围**：
- 新正文：\`draft/26.md\`、\`draft/27.md\`、\`draft/28.md\`。
- 主张文件：\`draft/26.claims.json\`、\`draft/27.claims.json\`、\`draft/28.claims.json\`。
- 原阶段所有者资料的增量交接：\`research.md\` S94—S102、\`claim-ledger.md\`、\`outline.md\`、\`timeline.md\`；采用新增条目/严格定位替换，不推翻之前正文事实。
- 主编/维护者派生登记：\`book.json\`三章由outline→draft、\`README.md\`及\`chapter-state.json\`派生摘要、第五部之后的第六部分卷目录与批次索引。
- 编辑状态：显式把全书 \`current_revision\` 从0更新到1，使revision0报告不能成为revision1的审稿许可；\`review_status=PENDING\`、\`reviewed_revision=null\`、\`edited_revision=null\`、\`final_approved=false\`维持，原 \`outline_approved/evidence_verified\` 仍false。

**报告失效处理**：旧 \`qa/continuity-report.md\` 与 \`qa/developmental-review.md\` 仍留作revision0基线，均为CHANGES_REQUIRED；旧章级矩阵不改写成“已审核29章”。新revision1未获得独立双审。继续依 [P0交接](p0-repair-26-28.md) 改稿与补稿。

**边界**：修订日志记录的“版本变更”不表示已运行终稿门禁，也不表示程序化测试能代替编辑事实审校。未创建 \`edited.md\`、\`final.md\`，未批准任何实际出版渠道。
