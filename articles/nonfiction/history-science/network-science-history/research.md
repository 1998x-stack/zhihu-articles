# 历史资料与学术证据台账

状态：已定位代表论文和学术机构页面，但**未对全部章级断言完成原文核证**。来源列表是下一阶段查证入口，不等于逐章审稿通过。

| ID | 文献 | 年份 | 入口 |
|---|---|---|---|
| S01 | Newman, Structure and Function of Complex Networks | 2003 | [查阅](https://doi.org/10.1137/S003614450342480) |
| S02 | University of Michigan, Origins of Social Network Analysis | 2026 | [查阅](https://psc.isr.umich.edu/news/the-research-center-for-group-dynamics-the-origins-of-network-analysis/) |
| S03 | Freeman, Centrality in Social Networks | 1978—1979 | [查阅](https://doi.org/10.1016/0378-8733(78)90021-7) |
| S04 | Cohen/Havlin, The Erdős–Rényi Models | 2010 | [查阅](https://doi.org/10.1017/CBO9780511780356.002) |
| S05 | Granovetter, The Strength of Weak Ties | 1973 | [查阅](https://doi.org/10.1086/225469) |
| S06 | Watts/Strogatz, Small-world Networks | 1998 | [查阅](https://doi.org/10.1038/30918) |
| S07 | Barabási/Albert, Emergence of Scaling | 1999 | [查阅](https://doi.org/10.1126/science.286.5439.509) |
| S08 | Clauset/Shalizi/Newman, Power-Law Distributions | 2009 | [查阅](https://doi.org/10.1137/070710111) |
| S09 | Kleinberg, Navigation in a Small World | 2000 | [查阅](https://doi.org/10.1038/35022643) |
| S10 | Albert/Jeong/Barabási, Error and Attack Tolerance | 2000 | [查阅](https://doi.org/10.1038/35019019) |
| S11 | Girvan/Newman, Community Structure | 2002 | [查阅](https://doi.org/10.1073/pnas.122653799) |
| S12 | Newman/Girvan, Evaluating Community Structure | 2004 | [查阅](https://doi.org/10.1103/PhysRevE.69.026113) |
| S13 | Blondel et al., Fast Unfolding of Communities | 2008 | [查阅](https://doi.org/10.1088/1742-5468/2008/10/P10008) |
| S14 | Milo et al., Network Motifs | 2002 | [查阅](https://doi.org/10.1126/science.298.5594.824) |
| S15 | Pastor-Satorras/Vespignani, Epidemic Spreading | 2001 | [查阅](https://doi.org/10.1103/PhysRevLett.86.3200) |
| S16 | Watts, A Simple Model of Global Cascades | 2002 | [查阅](https://doi.org/10.1073/pnas.082090499) |
| S17 | Holme/Saramäki, Temporal Networks | 2012 | [查阅](https://doi.org/10.1016/j.physrep.2012.03.001) |
| S18 | Kivelä et al., Multilayer Networks | 2014 | [查阅](https://doi.org/10.1093/comnet/cnu016) |
| S19 | Hamilton/Ying/Leskovec, GraphSAGE | 2017 | [查阅](https://papers.neurips.cc/paper_files/paper/2017/hash/5dd9db5e033da9c6fb5ba83c7a7ebea9-Abstract.html) |

## 重点风险

1. 欧拉七桥轶事、基尔霍夫与凯莱优先权：需原始史料。
2. Gilbert G(n,p)和Erdős–Rényi G(n,m)要区分；巨型分量阈值必须写明渐近条件。
3. 米尔格拉姆/特拉弗斯研究存在抽样、链完成率的解释问题；不能把六度当自然常数。
4. 小世界短路≠局部导航成功；幂律需和其他长尾分布比较，不以对数图直线判断。
5. 2000年鲁棒性论文2001年存在勘误：https://doi.org/10.1038/35054111 。
6. 传播零阈值的结论依赖特定网络、动力学及极限，不能无条件概括。
7. 社群、模体、GNN的预测不能直接当作真实功能或因果解释；高阶、图嵌入、早期GNN与链接预测须补原始文献。

## 必需证据字段

记录断言、来源、发表口径、原文位置、支持强度、反例、是否仅为现代教学类比。虚构引语和私下心理一律禁止。


## 第01章增量史料核查（2026-11-06）

> 针对“七座桥的困局”开展章节级原始资料核对。以下仅支持本章指定断言；**全书的 `evidence_verified` 仍为 false**，且未触发非虚构全书写作/终稿批准。

| ID | 来源和定位 | 支持的具体内容 | 性质与核查结果 |
|---|---|---|---|
| S20 | [Euler Archive E53](https://scholarlycommons.pacific.edu/euler-works/53/) 作品记录 | 原文题目、档案编号 E53、撰写1735、出版1741、来源卷8页128-140 | 学术原始文献档案元数据；已对照页面核验 |
| S21 | [Euler 原论文拉丁文本转录](https://www.cantab.net/users/michael.behrend/repubs/maze_maths/pages/euler.html) §§1-17 | §§1-3：位置几何、桥问题、拒绝暴力枚举；§§4-9：八个字母槽位、A三次与B/C/D各两次；§§16-17：两端度数相加为二倍桥数 | 原文的公开转录，逐节核对；该网页存在少数转录或排印勘记，应回到影印本终审 |
| S22 | [MAA: Leonard Euler's Solution](https://old.maa.org/press/periodicals/convergence/leonard-eulers-solution-to-the-konigsberg-bridge-problem) | 历史背景、现代解释、欧拉原文结构 | 学术学会科普二手解释；仅用作交叉核验 |
| S23 | [Cambridge: Early Writings on Graph Theory](https://www.cambridge.org/core/books/abs/resources-for-teaching-discrete-mathematics/early-writings-on-graph-theory-euler-circuits-and-the-konigsberg-bridge-problem/859A9DB1C6FDA9C581788160BB734446) | 莱布尼茨位置几何与欧拉图论起点的历史语境 | 学术教育史来源；避免夸大成图论全史完成 |

### 该章可交付正文的结论范围

- 原始史实：七桥与四片陆地；欧拉以 A,B,C,D 标记，七桥 a-g；论文讨论枚举方法及其不足；原论文自身的九对八矛盾已于 §§4-9 核实。
- 现代数学：原始连接关系作为无向多重图，度数5/3/3/3；有限无向图欧拉行走需非零度点连通且奇数度顶点为0或2；新添 B-C 边后的示范路线 A-B-A-C-A-D-B-C-D 可手工逐边核查。属于现代逻辑推导和教学类比，**不是原文原句**。
- 历史语境：1735年撰写、1741年实际发表；存在1736年期卷口径。不要写成“1736年正式出版”。
- 排除：居民周末散步竞赛、欧拉在柯尼斯堡现场解谜、真实人物心理对白，均未获得独立可靠史料，正文不主张为事实。
- 后续质量门禁：原文影印页逐句复核、统一数学符号、编辑进行独立的结构和连续性核验；尚未封版。
