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


## 第02—04章增量核验（2026-11-06）

> 依据仓库 \`genre-history-science\`、\`fact-research\`、\`nonfiction-writer\` 的证据约束，专门核对三章的书目、概念与贡献归属。详见各章 \`draft/NN.claims.json\`。本节核验**不能代替全书 evidence_verified、outline_approved 或独立审稿**。

| ID | 史料来源 | 明确支持范围及限制 |
|---|---|---|
| S24 | Henry Martyn Mulder, [Electrical Networks and Trees in the 19th Century](https://www.mat.univie.ac.at/~schmitt/OeSGdM/1986_oesgm01.pdf) (1986), §§1–5 | 基尔霍夫1845年电网络基本定律、1847年一般电流求解；生成树和基本回路的历史脉络；凯莱1857年树论。**数学史二手资料**，1847年原始论文影印待核。 |
| S25 | [Encyclopedia of Mathematics: Matrix tree theorem](https://encyclopediaofmath.org/wiki/Matrix_tree_theorem) | 现代拉普拉斯余子式等于生成树数，完全图带标号树数 \(n^{n-2}\)；“经典形式隐含于基尔霍夫工作”不代表1847原文采用现代矩阵符号。 |
| S26 | Jerry Lodder, Mathematical Association of America, [Networks and Spanning Trees](https://old.maa.org/press/periodicals/convergence/networks-and-spanning-trees) | 凯莱1889年《A Theorem on Trees》的计数尝试及普吕弗后续证明，网站偶有访问障碍，正式终审时应复核全文。 |
| S27 | William Spicciotto, [The History of the Enumeration of Trees](https://mathweb.ucsd.edu/~thesis/thesis/spicciotto/spicciotto.pdf), §1.2 | 博尔夏特1860年先得带标号树计数公式，凯莱1889年独立给出。二手数学史来源；原刊优先权仍需核对。 |
| S28 | Knuth, [Trees: History and Bibliography](https://fherrera124.github.io/taocp/OEBPS/Text/ch02b.html) | 早期树研究参考书目及不同研究传统，辅助旁证。 |
| S29 | J. L. Moreno, [Who Shall Survive?](https://books.google.com/books/about/Who_Shall_Survive.html?id=39QhAAAAMAAJ), 1934初版 | 初版作者、年份、社会测量与有向选择图；Helen Jennings有署名附录。不能用1953修订版内容直接冒称1934年首版。 |
| S30 | A. Paul Hare, [Moreno's Sociometric Study at the Hudson School for Girls](https://psychodrama.org.nz/wp-content/uploads/resources/morenos-sociometry-hudson-school-girls.pdf), *Journal of Group Psychotherapy, Psychodrama & Sociometry*, 45(1), **1992** | 哈德逊研究1932—1938年，训练学校制度背景、历史种族分隔、詹宁斯数据分析贡献。研究者所记变化不等于严格识别的因果效果；网站2025上架不是原发表年。 |
| S31 | [History of Information: Early Sociograms](https://www.historyofinformation.com/detail.php?id=3334) | 1934书中社会图的历史实物示例，不在正文中转载受版权约束的图像。 |
| S32 | Alex Bavelas, [A Mathematical Model for Group Structures](https://doi.org/10.17730/humo.7.3.f4033344851gl053), *Human Organization* 7(3), **1948** | 结构中心与群体沟通研究早期论文，2024数字上架时间不得当作1948首次出版日期。 |
| S33 | Harold J. Leavitt, [Some Effects of Certain Communication Patterns upon Group Performance](https://dspace.mit.edu/entities/publication/e08f2f50-972e-4276-99a9-452627ed07a6), MIT PhD thesis, **1949** | 原始学位论文的标题、年代、指导教师 Bavelas。 |
| S34 | Leavitt, [Some Effects of Certain Communication Patterns on Group Performance](https://doi.org/10.1037/h0057189), *Journal of Abnormal and Social Psychology* 46(1), **1951**, 38–50 | 期刊论文的出版信息；不可与1949学位论文混写。 |
| S35 | Linton C. Freeman, [Centrality in Social Networks: Conceptual Clarification](https://doi.org/10.1016/0378-8733(78)90021-7), *Social Networks* 1(3), **1978–1979**, 215–239 | 度、接近、介数三类节点中心性，网络集中化；早期实验研究结果复杂不一。 |
| S36 | Freeman, [A Set of Measures of Centrality Based on Betweenness](https://doi.org/10.2307/3033543), *Sociometry* 40(1), **1977**, 35–41 | 介数中心性标准化研究；不声称介数想法全由这一篇首次创造。 |
| S37 | Leo Katz, [A New Status Index Derived from Sociometric Analysis](https://doi.org/10.1007/BF02289026), *Psychometrika* 18(1), **1953**, 39–43 | “谁选择”与“多少人选择”及间接路径影响衰减；现代逆矩阵式为教学整理。 |
| S38 | University of Michigan, [Origins of Social Network Analysis](https://psc.isr.umich.edu/news/the-research-center-for-group-dynamics-the-origins-of-network-analysis/) | 社会网络分析源流的机构介绍，仅辅助说明，不代替原始研究。 |

### 三章主张边界与可复核算例

- **第02章**：连通图生成树边数 \(n-1\)，回路秩 \(m-n+1\)；三角形拉普拉斯主子式行列式3；\(\tau(K_4)=16\)，\(\tau(K_5)=125\)。1845/1847年基尔霍夫、1857/1889年凯莱、1860年博尔夏特与1918年普吕弗须分开。
- **第03章**：莫雷诺1934年首版、詹宁斯研究贡献与哈德逊制度背景；五人选择箭头是**现代虚构教学数据**，不是任何历史被试的实验记录。社会图显示选择，不自动证明原因或干预效果。
- **第04章**：Bavelas 1948、Leavitt 1949及1951、Katz 1953、Freeman 1977及1978—1979必须按各自论文年份处理。自拟九顶点结构：两个 \(K_4\) 经 A—X—B 相连，\(k_A=k_B=4,k_X=2\)，距离和\(15,15,14\)，介数\(15,15,16\)；是**现代算例**而非真实实验。
- **未审定事项**：需要对照关键史料的初版扫描（尤其1847与1860原刊、1934图及附录），核实公式边界及文本细节，并完成两份独立审稿。全书 \`workflow-state.json\` 保持原样。


## 第05—07章增量研究：随机图、相变与六度实验（2026-11-06）

> 依照\`fact-research\`与\`nonfiction-writer\`的“来源先行”规则，核对原始论文及学术史参考文献。以下验证仅覆盖**这三章**的具体断言，**不等于全书\`evidence_verified\`或\`outline_approved\`通过**。逐条主张详见\`draft/05.claims.json\`至\`draft/07.claims.json\`。

| ID | 原始或学术来源 | 支持范围和证据限制 |
|---|---|---|
| **S39** | E. N. Gilbert, [“Random Graphs,” *Annals of Mathematical Statistics* 30(4), 1141–1144](https://doi.org/10.1214/aoms/1177706098)；[原文扫描](https://www.stat.cmu.edu/~brian/780/bibliography/09%20Other%20Models/Gilbert%20-%201959%20-%20Random%20graphs.pdf) | **1959**，p.1141给出每对节点以相同概率\`p\`独立连边；电话交换局的转接概率作为应用示例。已核对原刊扫描及文本，不应误称固定边数模型。 |
| **S40** | P. Erdős & A. Rényi, [“On Random Graphs I,” *Publicationes Mathematicae Debrecen* 6:290–297](https://www.cse.cuhk.edu.hk/~cslui/CMSC5734/erdos-1959-11.pdf) | **1959**，p.290定义从\`n\`个带标号点与固定\`m\`条边的图中等概率抽样；pp.290–291研究**全图连通**与\`(n/2)log n\`尺度。已对照首页和定理影印。 |
| **S41** | P. Erdős & A. Rényi, [“On the Evolution of Random Graphs,” *Publ. Math. Inst. Hung. Acad. Sci.* 5:17–61](https://www.cse.cuhk.edu.hk/~cslui/CMSC5734/erdos-1960-10.pdf) | **1960（数学史通行引注）**，pp.17–19定义逐边均匀增加与相变阈值，研究不同规模的连通分量。论文明确承认模拟真实交通/通信网络应采用更实际的非均匀假设。部分馆藏将卷期资料标作1959，正式年表需核对。 |
| **S42** | Alan Frieze & Michał Karoński, [*Random Graphs and Networks: A First Course*, Cambridge, Evolution](https://www.cambridge.org/core/books/abs/random-graphs-and-networks-a-first-course/evolution/1DD3E669EBFC7A14C242C38AFD291AB9) | **2023现代数学教材**；亚临界、临界和超临界的分量规模，不能将今日的\`O(log n)\`、\`n^(2/3)\`符号全部冒充1960年原话。 |
| **S43** | Geoffrey Grimmett, [*Probability on Graphs*, Cambridge, Random Graphs](https://www.cambridge.org/core/books/abs/probability-on-graphs/random-graphs/DD4034AA8121B3467216F61DACC96D82) | **2010现代数学教材**；泊松分枝过程与巨型分量比例\`s=1-exp(-cs)\`的联系，系理想化稀疏随机图的渐近结果。 |
| **S44** | Stanley Milgram, [“The Small-World Problem,” *Psychology Today* 1(1):61–67](https://snap.stanford.edu/class/cs224w-readings/milgram67smallworld.pdf) | **1967年5月**；原始公众文章。开头异国咖啡馆偶遇为**说明性故事**，不可当真实访谈。含堪萨斯、内布拉斯加等早期实验叙述；首页原刊影印已核。 |
| **S45** | Jeffrey Travers & Stanley Milgram, [“An Experimental Study of the Small World Problem,” *Sociometry* 32(4):425–443](https://www.cs.cornell.edu/courses/cs6241/2019sp/readings/Travers-1969-smallworld.pdf)；[DOI](https://doi.org/10.2307/2786545) | **1969年12月**；p.425摘要给出**296人起点、64条完成链、完成链平均5.2个中间人**；p.429分组100/96/100；pp.430–431规则及**217人真正启动**；p.439的三名关键末端转交者合计**31/64≈48%**。已核对首页、分组与方法页扫描。 |
| **S46** | Judith Kleinfeld, [“Six Degrees: Urban Myth?”, *Psychology Today*](https://www.psychologytoday.com/us/articles/200203/six-degrees-urban-myth) | **2002评论**；针对公众对抽样、链条退出及“任意两人六度”的过度解释提出质疑。其批评不是1969原始结论，也不是全部实验结果的否定。 |
| **S47** | Columbia University, [Big World: retrospective](https://www.columbia.edu/itc/sociology/watts/w3233/client_edit/big_world.html) | 社会网络研究史的回顾与抽样局限说明；所谓“random”招募是有选择性的志愿群体，而不是严格随机人口代表样本。 |
| **S48** | Béla Bollobás, [*Random Graphs*, Cambridge, Connectivity and Matchings](https://www.cambridge.org/core/books/abs/random-graphs/connectivity-and-matchings/5BFB6F89DAB9880A52E163D2F753CA57) | 现代学术教材；有助于区分**巨型分量阈值**与**全图连通阈值**；纸本/电子上线年份不能误当1959—1960论文年代。 |

### 重要主张与数学检算

- **第05章**：吉尔伯特1959\`G(n,p)\`与厄尔德什—雷尼1959\`G(n,m)\`不同；\`G(n,p)\`条件于恰好\`m\`条边时，对\`0<p<1\`，其条件分布与\`G(n,m)\`相同。四节点六候选边，固定两边共有15个等可能图；\`G(4,1/2)\`抽到空图概率1/64。后者为作者可复核的**现代教学算例**。
- **第06章**：平均度\`c=2m/n\`。固定\`c<1\`的标准稀疏随机图最大分量通常\`O(log n)\`，固定\`c>1\`出现唯一线性规模巨型分量；临界窗口最大分量约\`n^(2/3)\`。现代公式\`s=1-exp(-cs)\`给出\`s(1.2)=0.3136983\`、\`s(2)=0.7968121\`。**全图连通**的阈值在\`c≈log n\`，不是1；“一条边”不是固定一步发生确定性相变的断言。
- **第07章**：**1967**公众文章、**1969**技术报告不可合并为同一套数据。**1969年296起始、217实际启动、64成功**，故分母不同：\`64/296≈21.6%\`与\`64/217≈29.5%\`；**5.2**仅指成功链平均中间人数，非所有两人最短路的普适结论。**31/64**仅为固定目标附近三名高频转交者；未完成的链存在缺失与参与意愿偏差。
- **待核与审稿**：正式发表前继续校对1960卷期、1967原文全部统计口径、1969分组表页和路径结果，另作独立连续性与结构审稿。全书\`workflow-state.json\`不改变未获准状态。


## 第08—10章增量研究：弱关系、中心性澄清与互联网实测（2026-11-06）

> 依照\`fact-research\`与\`genre-history-science\`规范，以期刊论文原版扫描、出版机构书目和数学模型的可复算实例为依据。仅核验本批具体断言；\`workflow-state.json\`中的\`outline_approved=false\`、\`evidence_verified=false\`、\`review_status=PENDING\`继续保持不变。逐条证据追踪见\`draft/08.claims.json\`—\`draft/10.claims.json\`。

| 来源ID | 学术资料与位置 | 事实支持范围／尚存风险 |
|---|---|---|
| **S49** | Mark S. Granovetter, [“The Strength of Weak Ties,” *American Journal of Sociology* 78(6):1360–1380](https://doi.org/10.1086/225469)，**1973年5月**；[斯坦福所藏原刊影印](https://inequality.stanford.edu/sites/default/files/media/_media/pdf/Reference%20Media/Granovetter_1973_Social%20Networks.pdf) | **原始文献扫描核对**：pp.1360–1361微观—宏观研究目标与四维关系强度；pp.1362–1363关系重叠、“两条强边+缺失第三边”的**理想化**三元配置；pp.1364–1365 bridge/local bridge；p.1371求职样本中**N=54**、16.7%经常/55.6%偶尔/27.8%很少，注释说明面访100人及总样本282人；p.1373讨论“弱关系本来更多”的替代解释；pp.1374–1378社区动员是假设性机制而非普遍已证实因果。 |
| **S50** | Mark S. Granovetter, [*Getting a Job: A Study of Contacts and Careers*](https://books.google.com/books/about/Getting_a_Job.html?id=loCRAAAAIAAJ)，Harvard University Press，**1974** | 1973论文引用了早期研究数据，随后出版专书；不能将1974书与1973期刊当作同一发表版本，更不能将1995修订版内容倒灌入1973。 |
| **S51** | Granovetter, [“The Strength of Weak Ties: A Network Theory Revisited,” *Sociological Theory* 1:201–233](https://doi.org/10.2307/202051)，**1983** | 后续讨论进一步强调**不是所有弱关系都承担桥梁功能**；其论断是弱关系成为桥的机会相对更高。用于审查1973论断的边界，不能把1983原话冒称1973原文。 |
| **S52** | Linton C. Freeman, [“Centrality in Social Networks: Conceptual Clarification,” *Social Networks* 1(3):215–239](https://doi.org/10.1016/0378-8733(78)90021-7)，**1978—1979**；[原刊影印](https://www.cin.ufpe.br/~rbcp/taia/Freeman1979-centrality.pdf) | **原始文献扫描核对**：p.215三种中心性概念与节点绝对/相对、全网络集中化；pp.215—216回顾巴维拉斯、利维特及小组实验结果矛盾；pp.227—230图集中化定义和\`(n-1)(n-2)\`度集中化归一化分母；原文表述对星形上界的解释适用于相应简单无向图类。已有S35为同一论文书目入口，S52用于章节原版原文定位。 |
| **S53** | Michalis Faloutsos, Petros Faloutsos, Christos Faloutsos, [“On Power-Law Relationships of the Internet Topology,” *ACM SIGCOMM*](https://doi.org/10.1145/316188.316229)，**1999**；[论文影印](https://snap.stanford.edu/class/cs224w-readings/faloutsos99powerlaw.pdf) | 原文p.251摘要：1997年11月—1998年12月**3个Internet拓扑快照**，网络规模增长约45%，若干拓扑统计量呈幂律近似；作者**明确限制样本规模和泛化范围**。**不**等同网页链接图；高双对数相关度不能充当现代拟合优度的充分检验。 |
| **S54** | Andrei Broder et al., [“Graph Structure in the Web,” *Computer Networks* 33:309–320](https://doi.org/10.1016/S1389-1286(00)00083-9)，**2000**；[原刊PDF](https://www.math.cmu.edu/~ctsourak/T797003/Readings/broder00bowtie.pdf) | **原始论文扫描核对**：p.309 两次AltaVista抓取每次超过2亿页面、约15亿链接；pp.310—311宏观蝴蝶结含SCC（约5600万）、IN、OUT和卷须（各约数千万）。p.310结果：弱连通最大部分超过90%；随机有序页面对存在有向路径约24%，**可达条件下**有向最短路径均值约16，忽略方向且无向可达条件下约6。两次抓取是**1999年5月/10月**，**论文发表2000年**。受抓取覆盖率与有向可达条件影响，不是所有WWW页面的完整普查。 |
| **S55** | M. E. J. Newman, [“The Structure and Function of Complex Networks,” *SIAM Review* 45(2):167–256](https://doi.org/10.1137/S003614450342480)，**2003**；[arXiv原论文](https://arxiv.org/abs/cond-mat/0303516) | 网络类型、路径长度、度分布、三角聚类、零模型和经验测量的系统综述。与本书早期章节S01同文，新增S55强调可核版次及公式定义。**现代统一定义不归为1999年论文原句**。 |

### 第08章：定义、假设、求职证据和竞争解释

- Granovetter的tie strength来自**时间、情感强度、亲密互诉、互惠服务**；论文推导将正向对称关系作为研究简化；求职研究主要以**联系频率**作为操作性代理，两者不可混为完全相同的量。
- 关系越强、朋友重叠越多是作者提出的理论假说。“两条强边但第三边缺失”在推导里被**理想化排除**，不是对所有人类三角关系的定理。
- **局部桥**关注删掉边后，其端点之间最短替代路径长于2步；弱关系更可能充当局部桥，**并不是每条弱关系都是桥**。
- 1973年求职百分比的分母仅**54人**，来自面访100人的子样本，研究总样本282人；不能写成“所有求职者”统计，更不能作为随机干预的因果结论。文中六个字母顶点是**作者自造教学图**。

### 第09章：从节点中心性到网络集中化

- 第04章已经介绍节点度、接近、介数与Katz概念；本章着重Freeman 1978—1979论证**不同中心直觉**以及节点分数 vs 整张图集中化的分层解释。
- 对简单无向图，若\`n>=3\`且\`ki\`为原始度数，度集中化\`sum(kmax-ki)/((n-1)(n-2))\`，星形达到1。五点链的度\`1,2,2,2,1\`得\`2/12=1/6\`；五点环所有度2得0。均为作者可复算的教学图，并非1960年代的原始实验测量值。
- 原论文讨论不同实验任务产生的矛盾结果；不能直接推断“中心化提高效率/降低效率”普遍成立。网络结构指标不是社会权威或因果影响的直接代理。

### 第10章：网络类型、采样、可达口径与数学核对

- **Internet基础设施/AS拓扑**≠**WWW页面超链接有向图**，即使两类网络都表现出高度不均匀的连接，也必须各自建模、各自标注抽样方式。
- Broder论文**1999两次抓取，2000年发表**。弱连通\`>90%\`来自**忽略方向后的页面图**；而\`24%\`有向可达、平均有向路径约16、条件于无向可达的路径约6，是不同统计分母及方向的结果，不能并列当成互相矛盾的“全球平均”。
- 本书自构6顶点示例：两组三角通过一条桥连接，\`m=7\`，度数分别为\`2,2,3,3,2,2\`，平均度\`7/3\`，\`P(2)=4/6\`、\`P(3)=2/6\`；平均局部聚类\`7/9\`与全局传递性\`3/5\`**不是同一个定义**；总15对顶点路径和27，平均\`27/15=1.8\`。是**现代教学演算**，不冒充真实网页数据。
- 由于网络抓取和缺失节点问题，经验数据是对现实的一种样本观察，而非天然完整的图；幂律拟合的统计验证将留给第13章讨论。

### 证据风险与工作流状态

本批章节已完成原始论文关键页核读和数值手算；**尚未**执行全书提纲批准、全书证据核准、独立连续性审查和结构审稿，也未给任何AI审稿分数充当批准结论。\`workflow-state.json\`保持\`PENDING\`。后续应复核格兰诺维特的论断译名、Freeman不同集中化指标的图类边界、1999年Internet拓扑数据的层次与抽样口径。


## 第11—13章增量研究：1998小世界、1999择优连接与2009幂律统计检验（2026-11-06）

> 按\`fact-research\`、\`genre-history-science\`及\`nonfiction-writer\`的工作流契约补充章级史料，优先1998《自然》、1999《科学》及2009《SIAM Review》的原刊扫描与发行记录。**本批核对具体断言，不等于全书证据/提纲审核通过。** 章级逐条说明见\`draft/11.claims.json\`—\`draft/13.claims.json\`。

| ID | 论文及可复核入口 | 年份、原文位置、支持边界 |
|---|---|---|
| **S56** | Duncan J. Watts & Steven H. Strogatz, [“Collective dynamics of ‘small-world’ networks,” *Nature* 393:440–442](https://doi.org/10.1038/30918)；[原刊PDF](https://ndg.asc.upenn.edu/wp-content/uploads/2016/04/Watts-Strogatz-1998.pdf) | **1998年6月4日**；p.440将规则环格子节点与逐边概率\`p\`重连结合，定义\`L(p)\`和\`C(p)\`；p.441图1、图2、表1比较演员、电网、线虫。原刊截图核对：**演员**\`L=3.65/2.99,C=0.79/0.00027\`；**电网**\`18.7/12.4,0.080/0.005\`；**线虫**\`2.65/2.25,0.28/0.05\`；前/后分别为实测/相应随机基准。论文自己注明把不同网络都视为无向、无权、顶点等价是粗略简化；不能扩展为全部现实网络天然遵循同一动力学。 |
| **S57** | Albert-László Barabási & Réka Albert, [“Emergence of Scaling in Random Networks,” *Science* 286:509–512](https://doi.org/10.1126/science.286.5439.509)；[作者团队原刊PDF](https://www.barabasi.com/media/Emergence-Barabasi-1999_gN74Tws.pdf) | **1999年10月15日**；p.510给当时的演员、WWW、电网估算\`gamma≈2.3,2.1,4\`及样本限制；p.511定义每步新增一个节点、\`m\`条边、线性择优概率\`Pi_i=k_i/sum(k_j)\`，变体A只有增长、变体B只有择优，导出长期平均场\`dk_i/dt≈k_i/(2t)\`、幂律\`gamma=3\`。原刊截图核对；**经验幂律**是1999年作者报告，不代表按2009方法全部重新验证。原文也承认模型不能涵盖全部现实机制。 |
| **S58** | Herbert A. Simon, [“On a Class of Skew Distribution Functions,” *Biometrika* 42(3–4):425–440](https://doi.org/10.1093/biomet/42.3-4.425)；[期刊记录](https://academic.oup.com/biomet/article-abstract/42/3-4/425/296312) | **1955年12月1日**；原刊摘要/期刊资料支持词频、城市规模、科学出版等偏斜分布的概率机制研究。属于1999之前的理论先驱；不是1999 BA具体网络模型的作者。 |
| **S59** | Derek de Solla Price, [“A general theory of bibliometric and other cumulative advantage processes,” *JASIS* 27(5):292–306](https://doi.org/10.1002/asi.4630270505)；[影印](https://garfield.library.upenn.edu/price/pricetheory1976.pdf) | **1976年9月**；摘要与原刊首页记录引用关系、出版频率等的累积优势过程，并回溯此前概率模型。此来源明确禁止将“越成功越容易成功”的统计思想首次发明归于1999 BA。 |
| **S60** | Aaron Clauset, Cosma Rohilla Shalizi & M. E. J. Newman, [“Power-Law Distributions in Empirical Data,” *SIAM Review* 51(4):661–703](https://doi.org/10.1137/070710111)；[原刊PDF](https://www.cs.cornell.edu/courses/cs6241/2019sp/readings/Clauset-2009-power-laws.pdf) | **2009年11月6日电子发表**。原刊截图核对：p.663 Box 1流程为估计\`xmin,alpha\`→KS/模拟拟合优度（其约定\`p>0.1\`不拒绝）→与竞争分布做似然比；pp.665–667连续型与离散型MLE区别；pp.671–677下界与拟合优度，pp.678–688竞争模型。**24份数据中，17份未被拟合优度拒绝、7份拒绝**，但竞争模型仍可能同样或更有支持；绝不能把17份称为已证明幂律。 |
| **S61** | M. E. J. Newman, [“Power Laws, Pareto Distributions and Zipf’s Law,” *Contemporary Physics* 46(5):323–351](https://arxiv.org/abs/cond-mat/0412004) | **2005**；幂律密度、尾部分布及多领域模型的解释。作为后世补充参考，不冒充2009综合检验或1999原始研究。 |

### 第11章｜两种结构性质与原始图的操作规则

- 模型首先固定\`n\`顶点、偶数\`k\`近邻环格子，对原有每条边以概率\`p\`**重连**，保留总边数并避免重复边、自环。其\`p=1\`不能直接写成Gilbert逐对独立连边的\`G(n,p)\`。
- \`L(p)\`是全图的典型最短路径，\`C(p)\`是局部邻居闭合程度。少量远程边可能让\`L\`明显下降而\`C\`下降有限，是原论文核心机制。它不等于米尔格拉姆“每个参与者必能找到六步路径”。
- 真实网络表1值已经核对原刊影印；模型比较并非同一实验室生成、同一物理机制。疫病传播等是原论文简化动力学**模型**结果，不能据此宣称所有传播必然更快。

### 第12章｜增长、择优连接与前史

- 1999 BA定义\`m_0\`初始顶点，每步引入一位新节点、连接\`m\`个不同旧顶点，\`Pi_i=k_i/sum_j k_j\`。连续近似给出\`k_i(t)≈m sqrt(t/t_i)\`与长期尾部\`P(k)∝k^-3\`。**正向概率模型**不能由经验幂律外形反推出唯一生成因果机制。
- 原论文对照模型A去掉择优、模型B去掉增长，支持这两个组成部件对**其比较模型族**中稳态幂律出现的重要性；绝非证明“只有BA过程能产生幂律”。
- 四节点种子\`A-B\`→\`C\`连\`A\`→\`D\`选择旧节点，计算\`P(D→A)=2/4\`、\`P(D→B)=P(D→C)=1/4\`，是**本书原创的有限例子**。
- BA基础模型\`m=1\`的现代精确极限度数分布为\`4/[k(k+1)(k+2)]\`，尾部才渐近\`k^-3\`。不把该公式冒称1999原文逐字表述。
- 1955 Simon与1976 Price的先行工作说明累积优势和偏斜分布存在明确早期源流；避免天才独创叙事。

### 第13章｜统计检验及解释强度

- 双对数直线是幂律的**必要图形特征之一**，但有限范围对数正态、截断幂律等也可能近似直线；尤其不能仅用直方图对数回归的线性相关度当证据。
- 连续幂律尾部密度\`p(x)=(alpha-1)/xmin*(x/xmin)^(-alpha)\`，其MLE\`alpha_hat=1+n/sum_i ln(x_i/xmin)\`；度数属于离散整数，需要**离散**幂律的\`zeta(alpha,kmin)\`归一化与对应估计。
- \`xmin\`按候选尾部KS差异选择；因参数及下界都是从同一份数据拟合，拟合优度需要模拟合成样本**复做整个拟合程序**。原论文采用\`p<0.1\`拒绝幂律的经验决策界线，**不是**“真实分布为幂律的后验概率小于10%”。
- 24份数据的原论文分解：**17份未被拒绝，7份拒绝**。但未拒绝并未证明为真；还有对数正态、指数、拉伸指数、截断幂律等竞争模型，需要查看有统计显著性解释的似然比结果。
- \`P(K=k)∝k^-alpha\`与\`P(K≥k)∝k^{-(alpha-1)}\`是不同分布量的尾部渐近记法。若将CCDF斜率当PMF指数，将系统性错估参数。

### 仍需独立检查／工作流约束

本批仅完成具体原刊的定位、关键页核读及可复算的数学推导。尚未完成全书证据核准、提纲正式批准、独立连续性报告、结构审稿及终稿批准。依原仓库非虚构契约，\`workflow-state.json\`维持\`outline_approved=false\`、\`evidence_verified=false\`、\`review_status=PENDING\`。后续正式事实编辑重点复核1998表1图例、1999各实测网络样本口径与2009竞争模型结果。 
