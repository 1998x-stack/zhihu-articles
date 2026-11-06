# 修订执行日志｜revision-manager

revision_count: 1
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
