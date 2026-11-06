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

## 05—07 三章批次进度（2026-11-06）

- **05 马达瓦与喀拉拉学派**：`draft/05.md`、`draft/05.claims.json`，10条主张；ICM2022专业研究§3.4—3.5、Cambridge第1章与后世《Yuktibhāṣā》的传承定位，原创图 `assets/05-kerala-series.svg`。数学复核：交错级数前N项误差 `≤4/(2N+1)`，两种π级数收敛速度比较。独立手稿与后世证明严格区分。
- **06 伽利略**：`draft/06.md`、`draft/06.claims.json`，11条主张；1638《两门新科学》第三日、牛津默顿平均速度研究与苏黎世联邦理工历史说明，图 `assets/06-galileo-speed-triangle.svg`。数学复核：理想 `s=t²`、匀加速时等时间位移 `1:3:5:7`，强调滚球实验条件。
- **07 开普勒**：`draft/07.md`、`draft/07.claims.json`，10条主张；1615年原书馆藏与MAA史学、1616年德文版，原创图 `assets/07-kepler-volume-slices.svg`。数学复核：单位球体积分 `4π/3`，及连续截面半径条件。此章明确回溯至1615年，早于06章提及的1638出版事件。
- **质量边界**：三章均为 `DRAFT_UNREVIEWED`，尚未获得分立的连续性和结构审稿报告；全局 `outline_approved=false`、`evidence_verified=false`、`review_status=PENDING` 原封不动，不冒称已完成编辑、封版或对外发布。

## 08—10 三章批次进度（2026-11-06）

- **08 卡瓦列里**：`draft/08.md`、`draft/08.claims.json`，10条主张，原创图 `assets/08-cavalieri-slices.svg`。核查1627/1635/1647版本节点、古尔丁质疑、托里拆利后续研究；现代演示以矩形剪切和球—柱—双锥截面验证原理。**不可数个零二维面积截线的并**不是普通可数加法。
- **09 笛卡尔**：`draft/09.md`、`draft/09.claims.json`，10条主张，原创图 `assets/09-descartes-normal.svg`。核查《几何学》1637年附论、帕普斯问题、辅助圆与重根法线；原创教学例子 `x²+(y−3/2)²=5/4` 与 `y=x²` 消元给 `(x²−1)²=0`，切点斜率2。现代直角坐标纸非1637原样。
- **10 费马**：`draft/10.md`、`draft/10.claims.json`，11条主张，原创图 `assets/10-fermat-adequality.svg`。费马1891年编订的拉丁文《Methodus》、早期手稿、1638切线争论分开；矩形面积 `x(10−x)`，差商 `10−2a−e` 以及 `25−(x−5)²` 独立验证最大。拟等的意义为史学争论，不把其方法与现代ε–δ定义视作同义。
- **质量边界**：三章均标记 `DRAFT_UNREVIEWED`，章节分项来源与数学复算不代表完整独立审稿。全书 `outline_approved=false`、`evidence_verified=false`、`review_status=PENDING` 保持不变，未生成伪终稿。下批为11—13章。

## 11—13 三章批次（2026-11-06）

- **11 沃利斯、格雷戈里、巴罗**：`draft/11.md`、`draft/11.claims.json`，10条主张。1656沃利斯《无穷算术》、1668格雷戈里《Geometriae pars universalis》、1670巴罗《几何讲义》按发表年代区分，图 `assets/11-wallis-power-sums.svg`。现代平方和 `S_N=(N+1)(2N+1)/(6N²)` 收敛1/3；面积增量通过夹逼得到 `A'(x)=x²`（限x≥0,h>0）。现代记号不倒填17世纪。
- **12 1666年的牛顿**：`draft/12.md`、`draft/12.claims.json`，11条主张。依Newton Project MS Add.3958.3 (1666年10月手稿) 与研究史把1664读书、1665–1666创见、1669和1671后续写作分开；图 `assets/12-newton-binomial.svg`。广义二项式 `(1+z)^{1/2}` 前五项在z=1/4时约1.118011475，与根号真值比较。
- **13 牛顿流数法**：`draft/13.md`、`draft/13.claims.json`，11条主张。区分流量、流数和反流数，图 `assets/13-newton-fluxions.svg`。数学复核 `ẏ=2xẋ`、乘积规则、圆上切线隐式关系、 `A=x³/3⇒Ȧ=x²ẋ`。以1671手稿/1736英文印行等区分研究、转写、出版。
- **严格状态**：全部为 `DRAFT_UNREVIEWED`，未完成独立的 `continuity-audit` 与 `developmental-editor` 正式报告。全书 `outline_approved=false`、`evidence_verified=false`、`review_status=PENDING` 未更改。工作流Gate未通过不能声称已完成终稿。下一批为14—16章。
