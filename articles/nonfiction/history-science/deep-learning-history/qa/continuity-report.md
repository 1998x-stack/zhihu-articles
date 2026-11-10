# 《让机器学会学习》全书连续性与证据一致性审计｜首轮

revision_count: 0
review_round: 1
status: CHANGES_REQUIRED
scope: draft/00.md—draft/31.md; appendix appendices/A.md; book/outline/research/claims/timeline
independent_review_completed: false
reviewed_revision: null
checked_at: 2026-11-10
audit_type: whole-book initial consistency & source crosswalk

> **审校性质与限制**：本次是对既有稿件的首次全书一致性筛查和重点史料抽核。32篇均已进入结构、引用和章级主张统计，重要段落与个别原始资料已对读；但尚未把166份DL资料全部独立逐页核证，也未逐句审核全部22.7万字符。审查者与此前协助起草者来自同一对话助手执行环境，因此不冒称**外部独立审稿人已经完成核准**。此报告有真实缺陷且判定CHANGES_REQUIRED，绝非PASS。

## 1. 审计基线与有效进度

- 原定正式目录00—31，共32篇：00序章、30章正文、31尾声；书外另有非编号附录A。所有正式篇目book.json状态为draft，不是final。
- 32篇约227,024个字符（含Markdown），逐章claims共249项；研究索引含连续DL01—DL166共166个编号来源，另有R系列。索引编号齐全不能代表链接内容逐项已核。
- workflow-state.json.current_revision=0；进入本次审计前review_status=PENDING，final_approved=false。
- 第一轮跨章结构/来源映射记录见[whole-book-review-matrix.md](whole-book-review-matrix.md)。

## 2. 发现与修复要求（按优先级排序）

### FA-001｜BLOCKER｜第14章一项来源映射被Markdown竖线破坏

- **证据位置**：claim-ledger.md中的C14-07行；draft/14.claims.json中C14-07.source_ids字段。
- 当前ledger原文写P(h=1|v=0/1)，竖线未转义，使Markdown表格多拆出一列；对应JSON里，source_ids竟然成为字符串“v=0/1)=0.5/0.75”，而应是作者的AUTHOR_DERIVATION以及其计算结论。这是实际读取确认的数据错误，不只是引文排版。
- **修复**：nonfiction-architect修复ledger表格列分隔；nonfiction-writer重新生成该claim记录，核实w=ln3时σ(0)=0.5、σ(ln3)=0.75并指定AUTHOR_DERIVATION。补上源ID合法格式检查，经revision-manager记录版本并复审。
- **放行条件**：ledger列数一致，source_ids只含已登记文献标识或合法作者推导ID，计算与正文匹配。

### FA-002｜HIGH / 审稿放行阻断｜正文与逐章claims范围不对称

- **正文有来源标记、但没有列入该章claims.source_ids的编号**：
  - 00：DL78；02：R01；04：DL22、DL24；10：DL40；
  - 12：DL51；17：DL77；20：DL91；21：DL96；
  - 31：DL80、DL129、DL142、DL148、DL159。
  - 共计14项，分布在9篇。它们可能是背景引用，不自动表示来源或事实有误，正式事实审稿要判断是否支撑需要列入的核心主张。
- **反向差异**：08的claims包含DL42而正文未见[DL42]编号；10含DL63、DL41；17含DL52；27含DL135；31含DL163、DL164、DL143。逐项核对主张是否有正确引证。
- 06章C06-02/03采用AUTHOR_PROOF标识，其他作者算例多数采用AUTHOR_DERIVATION；需在契约中规范这两者的合法性与证据类型。
- **修复**：按实际独立论断补来源映射，非核心背景资料可标明context_only；建立正文段落→claim_id→原始来源定位。不能简单把所有参考文献机械变成核心claims。

### FA-003｜HIGH｜第01—03章claims审稿字段尚用旧版本

- draft/01.claims.json、draft/02.claims.json、draft/03.claims.json采用overall_review_status，却没有后续批次所用review_status和independent_reviewed。
- 这是元数据格式不一致，不代表前三章已经通过审稿。它们全部仍是工作初稿。
- **修复**：确定向后兼容的claims JSON schema，补明review_status=PENDING、independent_reviewed=false并运行32篇一致性检查。

### FA-004｜HIGH｜提纲、账本旧进度与真实目录矛盾

- outline.md旧批次说明仍保留“其余第16—31章与序章仍待核”、“22—31和序章仍规划”，而开头已声明32篇初稿齐备。
- claim-ledger.md开头旧总述依然写“第31章及序章仍待核”；其CORE行虽明确标为初始策划，仍应明确旧数据被后续批次更新覆盖。
- book.json的01、02、04、06章source_hints仍为TO_VERIFY，但相应research/claims已有来源。
- **修复**：对历史批次声明加明确的“当时记录/后续覆盖”标注，统一当前进度；只把已经查明的来源ID写入书目提示，不冒称独立全文核证。

### FA-005｜MEDIUM｜专题叙事的时间折返需要额外导读

- 10章1998票据→11章1997 LSTM；21章生成模型跨至2022→22章回2017 Transformer；24章2022 Chinchilla→25章回顾2015—2018 AlphaGo。
- 22、25章正文已有“专题回溯”说明，这一做法有效；建议在目录/每部导读声明书籍按机制而非年份严格单调排序。
- 序章00→01古代→16/17正式回收2012→31再看2012，符合初始读者承诺，但细节重复过多，交结构审稿处理。

### FA-006｜MEDIUM｜高风险实验及史学优先权尚需独立原文复核

优先独立逐页查证：04章Hebb1949原书第62页与后世格言；05章1958演示设备/活动记录；07章Linnainmaa1970及Werbos1974学位原本；09章反传优先权；10章1998商业票据处理量口径；11章1997 LSTM vs 2000遗忘门；15章2011 RT03S Fisher; 17章AlexNet官方PDF; 19章2014翻译BLEU; 24章2022 Chinchilla对照；26章CASP14结构域指标；28章InstructGPT人评条件；29章模型许可证；30章2026论文与预印本等级。

**研究索引存在不代表这些原始资料已全部通过独立审计。**

## 3. 首轮针对高风险数字的外部原始记录抽核

| 核查项 | 有限外部证据 | 本轮可确认的范围 |
| --- | --- | --- |
| 2012 ILSVRC | [官方成绩表](https://image-net.org/challenges/LSVRC/2012/results.html) / [官方赛事时间表](https://image-net.org/challenges/LSVRC/2012/) | SuperVision0.15315（额外数据）/0.16422（仅比赛数据）、ISI0.26172；官方2012-10-13公布完整成绩，00/17主要数值可支持 |
| AlphaFold2 CASP14 | [评估摘要](https://pubmed.ncbi.nlm.nih.gov/34599769/) / [AlphaFold2论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC8371605/) | domain GDT_TS中位92.4和Cα RMSD95中位0.96Å不是相同量度，26章区分方向正确 |
| Qwen2.5许可 | [团队2024-09公告](https://qwenlm.github.io/blog/qwen2.5/) | 3B、72B是Apache2.0例外，29章限定结论成立；逐模型历史许可证仍需核 |
| Meta Llama2 | [官方Community License](https://ai.meta.com/llama/license/) | 700m月活附加授权条件存在，需注明版本 |
| DeepSeek-R1 | [项目README](https://github.com/deepseek-ai/DeepSeek-R1) | 主体MIT与部分Llama蒸馏基座许可证不同 |
| HLE 2026 | [Nature2026-01-28](https://www.nature.com/articles/s41586-025-09962-4) | 2500专家题与正式发表日期正确，不代表全部现实能力 |
| 推理共享预算 | [arXiv2608.07968](https://arxiv.org/abs/2608.07968) | 2026年8月预印本研究，不能推广为全部模型和任务的定理 |

## 4. 审核分工与下一步

1. 先修复BLOCKER/HIGH的来源链、字段与陈旧状态；所有正文核心结论仍需后续独立原文逐项核对。
2. 结构评审见[developmental-review.md](developmental-review.md)，分开评判盐选开篇、节奏、人物贡献、因果和认知兑现。
3. 由revision-manager落实修改、递增current_revision，使本轮审稿结果失效；修订后重新做事实/连续性与结构双重审稿。
4. 只有全部最新版双审真实PASS，才能进入line-edit、final-approval及正式发布。

**本轮结论：CHANGES_REQUIRED。** 它是可执行的修订入口，不是出版许可。
