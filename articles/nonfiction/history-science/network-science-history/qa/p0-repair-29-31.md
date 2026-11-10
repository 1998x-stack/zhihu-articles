# P0整改交接｜第29—31章新增实质正文（revision2）

revision_count: 2
status: PENDING
editorial_findings: REVISION0_CHANGES_REQUIRED_RETAINED_AS_HISTORICAL_ISSUES
not_a_full_book_pass: true
as_of: 2026-11-10
baseline_revision: 1

## 一、关联的正式审校问题

**NS-CONT-B01 / NS-DEV-B01（9篇缺稿）**：在revision1补齐26—28后，revision2完成29—31三章。全书仍有**00、32、33三篇缺稿**，故全书BLOCKER依然开放，绝不把31/34工作初稿写为34/34终稿。

**NS-DEV-H05（全书核心认知承诺）**：第29章预测新增边、第30章学习节点向量、第31章从邻居生成特征，明确指出各方法的训练/测试与归纳假设，且章末承接第32章“预测不等于因果解释”。必须在32和33形成真实正文后再检查价值兑现，而不能现在宣布解决。

**NS-CONT-H04（历史年份/公式）**：CIKM2003与JASIST2007两种版本要分开；DeepWalk2014、node2vec2016不等同现代GCN；早期Scarselli 2008线上、2009期刊及2016预印本/2017 ICLR Kipf—Welling，GraphSAGE和MPNN同为2017不同贡献；GCN对称归一化与本文均值教学算例明确分开。仍需由独立事实编辑复核相应原文具体节和全部算式。

**NS-CONT-H01—H03（主张精准追踪）**：新增27条 `NS-29/30/31-xx` 都可在正文检索ID，旧01—19章218条及24章NS-24-09的直接锚点仍缺失，旧01章claim JSON字段差异仍待规范化。不能把新的章级账本当成旧问题已被解决。

**流程**：本次只是非虚构作者补稿与主编/维护者进度登记，**不是**continuity-audit与developmental-editor两个真正独立审稿人的PASS。正式 `workflow-state.json.review_status` 仍是PENDING；outline_approved/evidence_verified均false。

## 二、局部原刊与教学数学核查

| 章 | 本轮已核的边界 | 下一轮需复核 |
|---|---|---|
| 29 | 2003 CIKM短篇与2007 JASIST期刊版次序；六边共邻居算例和99%/0召回率反常；预测未来边≠删边恢复 | 原文共著网络构建、各指标基线、负样本抽样和未来时间切分，不能把模型分数当概率 |
| 30 | 2014 KDD DeepWalk与2016 KDD node2vec出处；二阶权重(0.5,1,2)归一化(1/7,2/7,4/7) | node2vec边权和方向处理、DeepWalk原训练层次softmax细节、跨任务向量使用合法性 |
| 31 | 2008/2009、2016/2017、2019等版本线索；三节点均值和六环/两三角反例在指定共享邻居聚合条件下可复算 | GCN规范化精确表达、GraphSAGE归纳任务数据、MPNN/1-WL边界及over-smoothing/over-squashing应用范围 |

局部计算由作者单独检查，不能视为两名独立事实审稿人对所有技术细节的验收。

## 三、修订前后

| 指标 | revision1 | revision2 |
|---|---:|---:|
| 规划篇数 | 34 | 34 |
| 实质工作初稿 | 28 | 31 |
| 占位篇数 | 6 | 3 |
| 章级主张 | 293 | 320 |
| 正文可检索claim ID | 74 | 101 |
| 既有主张缺少行内ID | 219 | 219 |
| 全书独立双审PASS | 否 | 否 |
| 正式终稿批准 | 否 | 否 |

最后3篇待补：序章00，第32章，尾声33。待全部写成后按新版本统一修复旧章证据锚点、来源范围与跨章术语，再开展正式独立事实连续性与结构双审。