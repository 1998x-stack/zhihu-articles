# 修订执行日志｜revision-manager

revision_count: 2
status: IMPLEMENTED_PENDING_REREVIEW
date: 2026-11-06
source_revision: 0
source_artifacts: draft/00.md—draft/16.md
reviewed_artifacts: qa/continuity-report.md; qa/developmental-review.md
new_manuscript: revised.md

## 版本原则

按仓库`revision-manager`执行：**17篇原始初稿不覆盖**，从其正文形成独立合订`revised.md`，由此作为**revision 1**的审稿对象。原始rev0两份审稿报告一律失效；只有新的双报告明确写revision_count:1且PASS，才可进入语言精修。

## 原审稿问题与已执行修改

| ID | 原级别 | 修订前 | 实际修订 | 位置 / 新依据 | 状态 |
|---|---|---|---|---|---|
| C-01/D-04 | HIGH | 05节标题“查理首先让巴黎看见空气的力量”，可能被误读为首次载人自由飞行 | 改为“氢气球让查理进入公众视野”；补1783-11-21蒙哥尔费热气球首次载人自由飞行与12-01查理/罗伯特首次载人氢气球两种优先权 | revised.md第05章；新增研究[S87]与既有[S33]；G05-04同步补证 | FIXED |
| C-02/D-04 | HIGH | 第08章等体积公式`N_A=N_B`与第15章阿伏伽德罗常数`N_A`视觉冲突 | 第08章改为`N_1=N_2`，补术语说明；第15章保留`N_{\mathrm A}`专指阿伏伽德罗常数 | revised.md第08章；[G08-02] | FIXED |
| C-03/D-04 | HIGH | 第13章先讲1876洛施密特，又用“1873研究者将尝试”收尾，时间线误导 | 改为“**把时间从1876年拨回1873年**”，明确另一条并行研究路线上溯；章节先后不再被误认为历史先后 | revised.md第13章至第14章交界 | FIXED |
| C-04/D-03 | MEDIUM | 第09章“假说被遗忘几十年” | 改为“几十年仍未成为共识”；删开头重复水蒸气2:1:2的完整说明；第08章末只留第09章悬念不提前讲尽讲义传播 | revised.md第08—09章 | FIXED |
| C-05/D-01 | MEDIUM/HIGH | 第00/06/11/12/15/16反复完整复述267、273及R | 保留第06章完整温度外推、第11章1834原式；第12章将温标回顾压缩为一句并保留[G12-02][G12-15]，第15章缩减历史重述；尾声去掉重算的三行外推式而保留公式结论与[G16-02]。序章仍只提问题 | revised.md第12、15、16章；各事实主张编号不丢 | FIXED_WITH_PEDAGOGICAL_RECAP_RETAINED |
| D-02 | MEDIUM | 第07—08章水蒸气体积例子连续重述 | 第07章继续承担“实验事实”，第08章承担“分子拆分”解释；第09章删重复叙述。第08章保留用于推导的最少化学计量关系 | revised.md第07—09章 | RESOLVED_EDITORIAL_INTENT |
| D-05 | MEDIUM | 中后段公式密度高 | 保留每个已有的现代符号/假设/单位解释，不添加无证据历史桥段；来源附录为读者提供回溯通道；关键公式仍有前提与文字说明 | revised.md第11—15章 | ACCEPTED_WITH_EXISTING_EXPLANATIONS |
| D-06/C-06 | MEDIUM/LOW | 各篇末尾反复显示“初稿、未审稿”及史料列表，破坏合订阅读 | **保留全部旧稿**的单章史料部分于`draft/NN.md`；合订`revised.md`每章仅保留有追踪编号的正文，末尾增“附录｜证据追踪与史实解释边界”、逐章来源索引；移出独立的初稿状态通告 | revised.md附录；research.md、claim-ledger.md继续可读 | FIXED |
| D-07 | LOW | 早期章节字数大于中后段 | 不机械增加或删除史实；要求下一步line-edit只改善句子密度，不为了字数均衡扩大断言 | QA非阻断备注 | ACCEPTED |

## 依赖资料协同修改（非无记录覆盖）

1. `research.md`追加[S87]史密森学会航空航天馆关于1783-11-21与12-01两次不同载人首飞记录；不借此证明1787查理未刊实验。
2. `claim-ledger.md`第05章G05-04由S33扩充为S33/S87；`draft/05.claims.json`中G05-04的`source_ids`同步加入S87。未改变其他章的历史主张链。
3. `revised.md`由17份初稿正文组成，保留**全部306个独立[Gxx-yy]标记**；其中[G05-20][G05-21][G16-21]原在单章来源说明之中，转至统一附录追踪。
4. 原17份`draft/NN.md`继续作为revision 0版本来源备查；此后正文审核应以revision 1的`revised.md`为唯一基准。

## 复审请求与遗留风险

- **客观待核**：S55/S58等资料只曾部分可见，不能据研究矩阵称“所有原始科学史史料100%逐页独立核查”；旧史料的争议仍要保留原先限定。已核关键历史事实及现代SI定义支持本轮小范围改动。
- **复审必须检查**：C-01—C-04实际修复、306条编号存在、来源附录完整、09→10与13→14倒叙清楚，以及读者在合订稿中不被17份“初稿状态”打断。
- 未开展line-edit，也未执行本地`workflow_gate.py`；本日志**不代表复审通过**。
- Revision 1: 根据continuity-audit与developmental-editor初审意见修正跨章史实、符号、时间线与重复论证（previous approvals invalidated）。

## Revision 2｜独立结构审稿后的小范围修订（2026-11-06）

source_revision: 1
new_revision: 2
reason: DR1-01 (HIGH), DR1-02 (MEDIUM), revised appendix metadata precision
status: IMPLEMENTED_PENDING_REREVIEW

| 问题 | 修改对象及旧问题 | 本轮具体修复 | 事实/结构影响 |
|---|---|---|---|
| DR1-01 HIGH | `research.md`来源S87指向404的史密森馆藏编号 | 用已复核美国国会图书馆展览 `https://www.loc.gov/exhibits/dreamofflight/dream-dream.html` 支持1783-11-21热气球载人自由飞行；保留S33史密森学会支持12-01氢气球载人飞行；`draft/05.claims.json` G05-04验证元数据同步修正 | 两种“首次”区分不变；不借飞行史证明1787气体膨胀实验。证据可追溯性恢复。 |
| DR1-02 MEDIUM | `book.json`将已完成的第05—15章及尾声标为outline，提示“占位” | 17章均标为draft，并明确逐章文件是rev0原初稿、整书审校对象为`revised.md`；终稿未批准 | 修复阅读入口与实际文件状态的矛盾，不将旧稿伪称最终成稿。 |
| DR1-03 LOW | `revised.md`统一证据附录仍用“这些程序未完成”静态文案 | 改为以`workflow-state.json`和同轮QA为准；G16-21明确仅对应原初稿状态而非当前审稿结论 | 避免完成复审后附录状态反过来失实；306个主张编号保持不变。 |

**版本依赖与旧审稿失效**：rev1已归档连续性PASS于`qa/history/continuity-r1.md`，独立结构审稿rev1的CHANGES_REQUIRED归档于`qa/history/developmental-r1.md`。当前rev2不继承rev1的PASS；必须实际完成两道复审并确认同版本后方可精修。

- Revision 2: repair S87 attribution chain and 17-chapter navigation, clarify appendix workflow status (previous approvals invalidated).

## 并行成果整合（2026-11-06）

在本轮rev2修订期间，`main`分支并行完成了rev1的developmental-editor PASS、line-edit和final-approval的HOLD预审。为避免丢失其他编辑已经完成的工作，**rev2的edited.md以main的rev1精修稿为基础**，合并本轮13项跨章自然过渡修订及rev2证据附录更新。保留rev1两种不同时间形成的结构审查意见与rev1终审HOLD报告于`qa/history/`；不把对原版rev1的PASS直接视为新版rev2的审核许可。集成后核对306个主张编号、17个章节标题以及历史/现代公式关键字符串未改变。
