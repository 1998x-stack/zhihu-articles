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


## 2026-11-10｜revision1 → revision2｜P0补齐第29—31章

**修订依据**：首轮全书审校 `NS-CONT-B01`、`NS-DEV-B01/H05` 的P0缺稿阻断：本次补写原大纲第七部第29、30、31章，使“网络因果→链接预测→表示学习→GNN→预测与解释边界”的问题链可被进一步审查。

**正文与来源**：
- 新增实质正文 `draft/29.md`、`draft/30.md`、`draft/31.md`，分别约4271/4140/4277个汉字，不是原占位。
- `draft/29.claims.json` 8条、`30.claims.json` 8条、`31.claims.json` 11条，共新增**27条**逐项主张与教学演算类型说明。
- `research.md` S103—S113补充原论文、会刊版本和模型适用范围； `claim-ledger.md`、`outline.md`、`timeline.md` 跨章承接同步。
- 维护者派生更新 `book.json`、`README.md`、`chapter-state.json`、`volumes/07/README.md`、`batches`索引，进度变为31/34，3篇策划占位，320条总主张。
- QA工作台 `qa/review-state.json`修订为2；保留revision0历史报告和revision1增量记录，新增[本批P0整改说明](p0-repair-29-31.md)。旧审校结论不能自动对新稿有效。

**审批安全**：`workflow-state.json.current_revision=2`；依然 `outline_approved=false`、`evidence_verified=false`、`review_status=PENDING`、`reviewed_revision=null`、`edited_revision=null`、`final_approved=false`。未编辑 `edited.md` 或 `final.md`，无正式发布许可。

**剩余任务**：序章00、32章、尾声33；旧01—19章218条正文行内主张ID、24章NS-24-09、旧01章claims字段修订；在全书真正完稿并明确修订版本后重新独立开展事实连续性与结构审稿。


## 2026-11-10｜revision2 → revision3｜P0完成序章00、第32章、尾声33

**修订依据**：rev0全书连续性与结构报告NS-CONT-B01/NS-DEV-B01中的九篇缺正文阻断；此前rev1、rev2已补26—31，最后一批补原大纲序章00、32章、尾声33，形成34篇可审工作初稿的文本基线。

**文件与范围**：
- 新正文 draft/00.md、draft/32.md、draft/33.md，分别约4178、4832、4647个汉字，不再是占位提纲/样段。
- 对应00.claims.json、32.claims.json、33.claims.json各9条共27条可检索章内ID，全书主张总量320→347。
- research.md增S114—S117，并沿用S06、S07、S45；claim-ledger.md、outline.md与timeline.md完善终章与序章历史资料和跨章回指。
- 主编/仓库维护者维护book.json、README.md、chapter-state.json、workflow-state.json、批次索引及第七部分卷，全部34篇由31 draft/3 outline变为**34 draft/0 outline**，没有final。
- qa/p0-repair-00-32-33.md、qa/full-manuscript-intake-r3.md为新版本“稿件可审而未审”的交接，不覆盖rev0报告，不虚构两个独立审稿人。
- 已按具体研究范围对1998 WS重连/作者加边、1999 BA生成过程、Euler E53的1735/1736/1741、Pearl因果综述、2018评测预印本与2020 OGB进行来源边界划分；本批两种结构方程模型的观察与干预概率由作者自行演算。

**版本与审批**：workflow-state.json.current_revision=3，reviewed_revision=null，edited_revision=null，review_status=PENDING；outline_approved=false、evidence_verified=false、final_approved=false原样保留。旧rev0/1/2的审稿/交接均不赋予rev3审批。P0仅“缺正文”子项完成；P1需修01—19章218条、24章1条及01旧字段，并逐一核证原刊历史/数学/模型边界。

**下一阶段**：先P1精准来源与数学审计、校正跨章事实和术语，再形成一致版本的新独立连续性/事实与结构双审报告。只有正式PASS并获终稿闸门许可，才能进入line edit、final和出版。
