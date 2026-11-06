# 审稿占位

多数章节仍为策划占位。已成文的章仍须分别进行事实连续性审计和独立结构审稿，生成对应两份报告。现阶段不得标 PASS，不得创建伪造的最终审定稿。

## 00 序章进度

`draft/00.md` 已有有来源的研究初稿、独立计算示例和原创建模图 `assets/00-brachistochrone.svg`。目前**未**触发 `continuity-audit` 与 `developmental-editor` 双报告，故不得标 PASS；后续如有事实或结构修改需按版本机制处理。

## 01 芝诺一章进度

`draft/01.md` 已有来自柏拉图、亚里士多德、SEP 与欧几里得的逐项来源核证、12条可追踪主张，以及两种二分过程的原创 SVG `assets/01-zeno-dichotomy.svg`。已复算几何级数与10m/1m/s追赶示例。独立连续性审计和结构审稿仍未完成；只标记 `draft_unreviewed`，保留整体门禁 `review_status=PENDING`。

## 02—04 三章批次进度（2026-11-06）

- **02 欧多克索斯**：`draft/02.md`、`draft/02.claims.json`，9条主张；《几何原本》V.def.5、X.1、XII.2来源；图 `assets/02-exhaustion-circle.svg`。区分归属传统、古典证明及现代三角函数例子。
- **03 阿基米德**：`draft/03.md`、`draft/03.claims.json`，9条主张；《抛物线求积》命题24、力学发现/几何证明，现代级数和积分复算；图 `assets/03-archimedes-parabola.svg`。
- **04 刘徽**：`draft/04.md`、`draft/04.claims.json`，10条主张；《九章算术注》圆田原文、1986年和较新数学史研究边数考据、祖冲之史料；图 `assets/04-liu-hui-polygons.svg`。
- **质量边界**：三章均属 `DRAFT_UNREVIEWED`，未获得独立 `continuity-audit` / `developmental-editor` 双报告；全局 `outline_approved=false`、`evidence_verified=false`、`review_status=PENDING` 保持原样。本批次不生成伪终稿，不宣称已运行 `workflow_gate.py`。
