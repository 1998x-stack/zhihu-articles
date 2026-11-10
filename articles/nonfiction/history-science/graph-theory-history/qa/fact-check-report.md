# 《连接的秩序：图论三百年》｜全书史实独立核验报告（首轮）

revision_count: 0
status: CHANGES_REQUIRED
date: 2026-11-10
lane: nonfiction
scope: 序章00、正文01—36、尾声37；共38篇
review_type: independent_fact_verification_round_1
publication_clearance: false

> **审查与创作的权限分开：** 本文件是正文写成后的独立核验工作产物，不是续写时自动附加的“已核证”声明。独立的意思是审阅对象、问题ID和结论与写作文件分离；此轮仍是模型/资料抽核，**没有外部人类史学编辑签字，不冒称全文逐字校勘或学界同行审定**。本报告列出已经复核的事实、尚缺的核验及阻断项。**结论：CHANGES_REQUIRED。**

## 1. 核验范围与证据级别

- **全量机械追溯：** 38/38篇 \`draft/NN.md\` 均存在，38份 \`draft/NN.claims.json\` 均为draft，合计 **423条不同的claim_id**：序章00有13条、01—37有410条；每个编号至少在对应正文出现一次，正文中的GT编号均能在本章claims文件找到。旧章有同一个编号多次引用的正常现象，**引用出现次数≠不同主张数**。
- **来源登记：** \`research.md\` 编号范围S01—S169，按当前档案 **S14未登记/跳号**，并非169条独立资料均完成逐篇全文核对。当前资源提供链接、出版事项及部分出处支持范围；后世解读、出版社摘要、原作全文和作者自制算例在证据强度上并不相同。
- **实质性公开源抽核：** 对关键争议点查询了大学原始档案、出版社出版页与论文/机构出版记录（下表）。有的只核对论文**题名、日期、作者、摘要或原始报告首页**，有的核对规范数学结论；未按页次逐字复审全部38篇的全部引用。
- **数学与历史解读分工：** 对每章的GT标签仅确认“可追踪”，并不因标签存在就把该句提升为“独立核证正确”。数式正确性另见 [数学公式审查](math-review.md)。

### 2. 已完成的重点事实抽核

| 章 | 核查命题 | 核查证据/结果 | 级别 |
|---|---|---|---|
| 00、01、37 | 欧拉七桥文稿1735；期刊标示1736；实际刊印1741；原论文第8卷128—140页 | [University of the Pacific Euler Archive E053](https://scholarlycommons.pacific.edu/euler-works/53/)、[MAA原刊历史说明](https://old.maa.org/press/periodicals/convergence/leonard-eulers-solution-to-the-konigsberg-bridge-problem)：**相符**；“论文首次在1736年实刊”不是可接受改写 | 原始学术档案+后世历史综述 |
| 02 | 1750年欧拉—哥德巴赫书信提出多面体公式；后来证明历程与笛卡尔优先权须分开 | [*Handbook of Graph Theory*历史摘录](https://api.pageplace.de/preview/DT0400.9781439880197_A24454585/preview-9781439880197.pdf)及图论史基础文献：核对到1750、1752、1794、1813等节点；具体原刊逐页仍待 | 历史综述，非全原稿校勘 |
| 06—07 | 1852四色问题弗朗西斯·格思里及德摩根10月23日致Hamilton信；肯普1879与希伍德1890 | [MacTutor四色定理史](https://mathshistory.st-andrews.ac.uk/HistTopics/The_four_colour_theorem/)：起源主线相符；戏剧化场景须维持条件化措辞 | 专业史料综述 |
| 26 | Christofides1976最坏比率度量TSP、原始CMU技术报告No.388 | [1976原始报告公开副本](https://www.ibr.cs.tu-bs.de/courses/ss21/na/uebungen/ADA025602.pdf)：月份、技术报告编号、三角不等式、MST+匹配内容与现代\(\le3/2\)保证的关联相符 | 原报告题录/摘要 |
| 29 | Robertson—Seymour《Graph Minors XX》2004证明Wagner猜想，不是整个系列终止 | [Elsevier原刊](https://www.sciencedirect.com/science/article/pii/S0095895604000784)：题名、卷92、页325—357、摘要中有限图小式良拟序命题相符 | 出版社原刊页面 |
| 31 | Lovász—Szegedy2004研究报告→2006期刊；不是2012才提出Graphon极限 | [Microsoft Research TR-2004-79](https://www.microsoft.com/en-us/research/publication/limits-of-dense-graph-sequences/)、[Elsevier JCTB96 (2006)](https://www.sciencedirect.com/science/article/pii/S0095895606000517)：相符 | 原报告及出版社摘要 |
| 32 | PageRank历史四人原稿、Brin/Page搜索系统论文与现代概率方程应分开 | [1998四人原稿存档](https://storm.cis.fordham.edu/~gweiss/selected-papers/classic-pagerank-paper.pdf)、[Google Research论文](https://research.google/pubs/the-anatomy-of-a-large-scale-hypertextual-web-search-engine/)：版本/作者来源已登记；未核1999所有报告版本 | 原始文献书目、部分内容 |
| 33 | Travers—Milgram1969 296起始、64完成、平均5.2“中间人”仅在完成链计算 | [*Sociometry* 32(4)原文摘要存档](https://snap.stanford.edu/class/cs224w-2010/readings/travers69smallworld.pdf)：数据口径相符，不能表述为全球人人平均最短路 | 原始摘要 |
| 34 | Broido—Clauset2019对普遍无标度断言的批评 | [Nature Communications 10:1017](https://www.nature.com/articles/s41467-019-08746-5)：出版时间2019-03-04、近千现实网络样本相符；不同严格度定义的结论不能互换 | 出版社原刊摘要 |
| 35 | Newman/Girvan2004模块度与每轮重算边介数 | [APS PRE69 026113](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.69.026113)：出版2004-02-26、摘要明确重算edge betweenness，相符 | 原刊摘要 |
| 36 | 2009 \`The Graph Neural Network Model\` 不等于2017 GCN初创 | [PubMed PMID19068426](https://pubmed.ncbi.nlm.nih.gov/19068426/)：2009卷20(1)61—80，2008-12-09 Epub；[Kipf/Welling arXiv](https://arxiv.org/abs/1609.02907) 2016-09-09，时间不同 | 原刊索引+原预印页 |
| 37 | 时间网络2012；多层网络2014的出版与建模范围 | [Holme–Saramäki2012](https://doi.org/10.1016/j.physrep.2012.03.001)、[Kivelä等2014](https://academic.oup.com/comnet/article/2/3/203/2841130)：论文题录与模型边界相符 | 出版社/机构资料 |

> **阶段性结论：** 上表这些“相符”仅针对明确列出的日期、署名、摘要和定理范围；不表示表外419?条主张自动获核证，也不等于完成逐段原作审查。（不同抽核条目可覆盖多条主张，不能从该表计算“已通过主张总数”。）

## 3. 审稿发现与待处理问题

| ID | 严重度 | 位置 | 实际问题及证据 | 修复方式 | 是否阻断终稿 |
|---|---|---|---|---|---|
| F-H01 | **HIGH** | 全书00—37，特别\`research.md\`与423条claims | 当前文件的\`verified=true\`主要记载**分章创作前限定核证**，并非针对全书全部423主张的独立原刊逐页证据核查。多项文献只掌握出版社摘要或后世综述；无法据此证明全书已获事实终审 | 建立\`claim_id → 历史来源版本/页码/段落 → 支持原话范围 → 现代解释/争议 → 复核人/结论\`逐条矩阵；高风险优先，再处理其余主张；将无法核实处降格为解释或删除 | **是** |
| F-H02 | **HIGH** | 第02、05、09、14、20、22等历史优先权/“首次”叙述 | 多处涉及原始发现优先权与较复杂出版史：笛卡尔—欧拉、多位树计数先驱、平面性先驱、1936年“第一部图论教科书”、1975/1978正则性、Ford/Moore/Dijkstra原始算法史。现有正文已加警示，但**尚不能宣布逐份原稿均独立核毕** | 逐章优先取得原刊或权威研究史全文，补准确页码和原文支持范围；保留“常见概括”“后世标准形式”等限定，并列明仍有争议的先驱问题 | **是** |
| F-M01 | MEDIUM | 第06开场；其他以“假如”“想象”引入的历史场景 | 第06章以1852年一位年轻人给英格兰地图着色开头，与格思里史料主线大体相合，但需要确认具体镜头细节不是作者代替历史人物补写；其他章节若有无提示的场景化描述亦需复扫 | 对真实人物场景加“据后世回忆/史料记载”或改为明确现代假设；不虚构当事人引语、心理活动、实验细节 | 否，待修 |
| F-M02 | MEDIUM | \`research.md\`、全书来源目录 | S01—S169范围内**S14未编入研究资料表**；连续ID并非必须，但若对外宣称“169条已核文献”将错误。S166曾有表格空行断裂，本批已在审稿前修复 | 生成真实source-id索引与不存在/未分配清单；将正文源表引用与研究登记自动对比；无来源的ID禁止claim引用 | 否 |
| F-M03 | MEDIUM | 第24、31、34、36等 | 现代数学示例和原刊出版史的边界总体有文字，但部分\`claims.json\`的\`status\`是自定义阶段标签，未提供统一、可机器判定的历史事实/现代证明/争议枚举规范 | 统一claim分类词汇与验证级别，给关键正史命题增加一手/二手/现代演绎的明确判定字段 | 否，待规范 |
| F-L01 | LOW | 第00、01、37及年表 | 欧拉写于1735、期刊卷1736、实刊1741已被三处明显交代；建议在全书书目中用统一脚注格式，防止之后语言编辑删掉限定 | 全书脚注统一为“E053：1735稿；1736卷号；1741实刊” | 否 |

## 4. 本轮审校总结与下一步签核条件

1. 已完成**全38章主张映射与出版史重点抽核**；关键抽核未找到足以立刻推翻正文主线的史实矛盾。
2. **没有**完成423条主张逐一核对原刊页码、版本、论证口径的完整学术事实复审，不能把38/38工作初稿或GitHub Actions机器通过误写为“史实核验PASS”。
3. F-H01、F-H02保留阻断；在相应证据补核及正文改动后，应按仓库\`revision-manager\`流程创建新修订版本，重新进行连续性与独立结构审稿。
4. 本报告是正式审稿的**首轮产出**，不是承诺以后会异步完成。当前结论：**CHANGES_REQUIRED**，不生成\`edited.md\`或\`final.md\`，不授权平台发布。
