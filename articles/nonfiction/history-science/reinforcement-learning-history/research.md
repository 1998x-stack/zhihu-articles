# 研究档案｜强化学习发展史（前置索引，未完成逐章核证）

> 负责阶段：fact-research。以下核对到权威出版社、会议、期刊或论文登记页的题名／年代及摘要级结论；**未逐页通读所有原文、没有完成所有章节主张核证**。此稿不构成证据验收通过。

## 工作假设与源流边界

Sutton 与 Barto 的史学性综述（R01）认为现代强化学习的早期形成包含试错学习、最优控制与时序差分三条路径；这是一个有来源的史学概括，**并非每一项技术都沿同一师承关系直线发展**。本书再横向处理策略梯度、博弈与搜索、模型学习、偏好优化等发展支线。

## 来源目录（可追溯编号）

| ID | 权威记录或原始论文 | 当前可确定的支持范围 |
| --- | --- | --- |
| R01 | [Sutton & Barto (2018), Reinforcement Learning: An Introduction, 2nd ed.](https://mitpress.mit.edu/9780262039246/reinforcement-learning/) | 二手综合／学术教材；总体历史与概念体系 |
| R02 | [Samuel (1959), Some Studies in Machine Learning Using the Game of Checkers](https://doi.org/10.1147/rd.33.0210) | 一手论文；跳棋程序与经验改进 |
| R03 | [Bellman, Dynamic Programming（1957初版；出版社现售为后续重版）](https://press.princeton.edu/books/paperback/9780691146683/dynamic-programming) | 奠基著作；初版年份待借馆藏再核 |
| R04 | [Barto, Sutton & Anderson (1983), Neuronlike adaptive elements...](https://ieeexplore.ieee.org/document/6313077/) | 一手论文；ASE/ACE倒立摆 |
| R05 | [Sutton (1988), Learning to Predict by the Methods of Temporal Differences](https://doi.org/10.1007/BF00115009) | 一手论文；TD思想及特定条件下论证 |
| R06 | [Watkins & Dayan (1992), Q-Learning](https://doi.org/10.1023/A:1022676722315) | 一手论文；1989论文前驱与收敛边界 |
| R07 | [Williams (1992), Simple Statistical Gradient-Following Algorithms...](https://doi.org/10.1007/BF00992696) | 一手论文；REINFORCE |
| R08 | [Sutton (1990), Integrated Architectures for Learning, Planning, and Reacting...](https://mlanthology.org/icml/1990/sutton1990icml-integrated/) | 一手论文；Dyna-Q和规划学习融合 |
| R09 | [Tesauro (1995), Temporal Difference Learning and TD-Gammon](https://www.bkgm.com/articles/tesauro/tdl.html) | 作者论文转载；期刊原版需复核 |
| R10 | [Schultz, Dayan & Montague (1997), A Neural Substrate of Prediction and Reward](https://pubmed.ncbi.nlm.nih.gov/9054347/) | 神经科学一手研究；仅能说明类比与实验证据 |
| R11 | [Sutton, Precup & Singh (1999), Between MDPs and Semi-MDPs](https://doi.org/10.1016/S0004-3702(99)00052-1) | 一手论文；options时间抽象 |
| R12 | [Ng & Russell (2000), Algorithms for Inverse Reinforcement Learning](https://ai.stanford.edu/~ang/papers/icml00-irl.pdf) | 一手论文待通读；逆强化学习与不可辨识性 |
| R13 | [Mnih et al. (2015), Human-level Control through Deep Reinforcement Learning](https://doi.org/10.1038/nature14236) | 一手论文；DQN及 Atari |
| R14 | [Silver et al. (2016), Mastering the Game of Go with Deep Neural Networks and Tree Search](https://doi.org/10.1038/nature16961) | 一手论文；AlphaGo |
| R15 | [Silver et al. (2017), Mastering the Game of Go without Human Knowledge](https://doi.org/10.1038/nature24270) | 一手论文；AlphaGo Zero |
| R16 | [Silver et al. (2018), A General Reinforcement Learning Algorithm That Masters Chess, Shogi, and Go through Self-play](https://doi.org/10.1126/science.aar6404) | 一手论文；AlphaZero |
| R17 | [Schulman et al. (2017), Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) | 预印本；PPO |
| R18 | [Haarnoja et al. (2018), Soft Actor-Critic](https://proceedings.mlr.press/v80/haarnoja18b.html) | 一手会议论文；连续控制 |
| R19 | [Schrittwieser et al. (2020), Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model](https://doi.org/10.1038/s41586-020-03051-4) | 一手论文；MuZero |
| R20 | [Kumar et al. (2020), Conservative Q-Learning for Offline Reinforcement Learning](https://papers.nips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) | 一手会议论文；离线分布偏移 |
| R21 | [Christiano et al. (2017), Deep Reinforcement Learning from Human Preferences](https://arxiv.org/abs/1706.03741) | 一手预印本；偏好奖励学习 |
| R22 | [Ouyang et al. (2022), Training Language Models to Follow Instructions with Human Feedback](https://proceedings.neurips.cc/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html) | 一手会议论文；InstructGPT |
| R23 | [Rafailov et al. (2023), Direct Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html) | 一手会议论文；DPO |
| R24 | [Shao et al. (2024), DeepSeekMath](https://arxiv.org/abs/2402.03300) | 一手预印本；GRPO |
| R25 | [DeepSeek-R1 (2025), DeepSeek-R1 Incentivizes Reasoning in LLMs through Reinforcement Learning](https://doi.org/10.1038/s41586-025-09422-z) | 一手期刊论文；强化学习与推理 |
| R26 | [NSF (2025-03-05), 2024 Turing Award announcement](https://www.nsf.gov/news/ai-pioneers-andrew-barto-richard-sutton-win-2025-turing) | 官方公告；2024奖项于2025年公布 |

## 已核对的关键断点

- **1959**：Samuel 跳棋论文 R02 存在，研究如何从经验改进程序；不能倒称其已有今天的 MDP/DQN 全套形式。
- **1983—1992**：R04 的 ASE/ACE，R05 的 1988 TD，R06 的 1992 Q-learning、R07 的 1992 REINFORCE 是不同问题的解决路线，不是一个算法简单替代下一个算法。
- **2013／2015**：DQN 的 2013 预印本与 2015 Nature 文章必须区分；当前直接核证期刊版本 R13，预印本具体版本仍待补核。
- **2016／2017／2018**：AlphaGo R14、AlphaGo Zero R15、AlphaZero R16：是否使用人类棋谱、依赖哪些环境规则、使用何种搜索与自我对弈，三者不能混写。
- **2019／2020**：MuZero R19 的预印本与期刊出版存在时间差，现核证 2020 期刊版本。
- **2017—2025**：R21 处理人类对轨迹偏好的学习；R22 处理 InstructGPT；R23 的 DPO 是不同于传统在线 RL 的直接偏好优化；R24 引入 GRPO；R25 为 2025 期刊论文，不能概括成所有模型的普遍训练方式。
- **奖项时间**：2024 年度图灵奖于 2025-03-05 公布（R26），不能误写为 2024 年 3 月宣布。

## 待补一手材料／高优先级核查

- [ ] 1898 桑代克动物实验、斯金纳操作性条件作用的出版年代与原始叙事，防止“迷箱”奇闻化。
- [ ] 多臂老虎机的 Thompson／Robbins 文献脉络和 bandit 与一般 RL 的分界。
- [x] Bellman《Dynamic Programming》1957初版及Howard《Dynamic Programming and Markov Processes》1960年出版信息已交叉核查；[ ] MDP术语更早流变及全书论证仍需深度复核，不能将现代教材记号倒推给早期作者。
- [x] 第10章已在1988年Sutton原始论文摘要及作者正文中核对Samuel、Holland、adaptive heuristic critic等TD前驱；[ ] 其他早期前驱的完整年代与技术同构程度尚需专题史学核对。
- [x] 第11—12章已核对Watkins剑桥1989学位记录、Watkins/Dayan1992表格Q-learning定理摘要、Rummery/Niranjan1994报告公告以及Sutton1996命名的教材史学记录；[ ] 原始报告全文更新式与严格定理假设还需独立逐页复核。
- [ ] 经验回放技术的早期 Lin 论文与 DQN 的差别。
- [ ] 致命三角典型反例及成立条件；数学推导逐项验算。
- [ ] 多智能体 RL、机器人控制、层次方法的遗漏贡献与性别／地域偏差。
- [ ] 2024—2026 的最新工作若拟加入，只能在补核一手论文后追加；不以趋势宣传当定论。

## 证据等级使用规则

- **A**：原始研究方法、发表年份、结论与限定均与原文交叉核对。
- **B**：出版记录及摘要已核，但未核对正文细节；仅可支撑概述。
- **C**：专业综述支持，适宜历史背景，不单独支持争议归属。
- **D**：编辑假设、类比或待核猜想，不进入正文事实陈述。

截至2026-11-09，第01—12章已分别针对各自可访问的一手原文片段、出版社与大学馆藏记录以及技术定义开展**限定范围前置核验**；第13章以后及未通读完整原著的争议细节仍属 **B/C 或待核**。不能据此宣布全书完成来源核查。只能在所列证据范围内起草，不据此声称全书全面核证。下游章节动笔前，必须将相关事实升级到足够的 A/B 证据，创建实际的 `draft/NN.claims.json`，并由独立审阅检查。

## 第01—03章增量核证记录（2026-11-09）

> 此节只为首批三章的具体论断服务；后续第04—32章没有获得本批核验许可。章节正文引注的 T/S/B 别名在 claims JSON 中映射至 R 编号。

| 新增来源 ID | 题名／来源 | 本次实际核查范围 |
| --- | --- | --- |
| R27 | [Thorndike (1898), Animal Intelligence: An Experimental Study of the Associative Processes in Animals](https://books.google.co.uk/books/about/Animal_Intelligence.html?id=jfJGAAAAYAAJ) | 一手研究，迷箱任务及历史出版；原文本节选可见：https://www.appstate.edu/~steelekm/classes/psy5150/Documents/Thorndike1898.pdf |
| R28 | [Thorndike (1911), Animal Intelligence, Chapter II](https://psychclassics.yorku.ca/Thorndike/Animal/chap2.htm) | 一手重印，Cat 12 Box A 24次逃脱用时及曲线解释 |
| R29 | [Thorndike (1911), Animal Intelligence, Chapter V](https://psychclassics.yorku.ca/Thorndike/Animal/chap5.htm) | 一手重印，效果律和练习律，p.244附近 |
| R30 | [Domjan (online 2025-12-09), Thorndike's law of effect and its inconsistent description over the years](https://doi.org/10.1002/jeab.70073) | 同行评审史学分析，1898迷箱与1911成熟效果律叙述的区别 |
| R31 | [Skinner (1938), The Behavior of Organisms: An Experimental Analysis](https://www.bfskinner.org/product/the-behavior-of-organisms/) | 一手著作的作者基金会原版资料和内容介绍；未逐页精读全书 |
| R32 | [Skinner (1990), From Behaviorism to Teaching Machines to Enjoying Old Age](https://garfield.library.upenn.edu/classics1990/A1990CK52100001.pdf) | 研究者本人第一手回顾，1938著作、实验鼠、累计记录与桑代克关系 |
| R33 | [Ferster & Skinner (1957), Schedules of Reinforcement](https://www.bfskinner.org/product/schedules-of-reinforcement/) | 作者基金会出版记录与研究概述；FR/FI现代示例不是书中实验数据 |
| R34 | [APA Dictionary of Psychology, negative reinforcement (updated 2018)](https://dictionary.apa.org/negative-reinforcement) | 专业术语定义，用于区别负强化与惩罚 |
| R35 | [Thompson (1933), On the Likelihood that One Unknown Probability Exceeds Another in View of the Evidence of Two Samples](https://doi.org/10.1093/biomet/25.3-4.285) | 期刊一手出版记录及题名；付费全文未逐页访问，不据此宣称原文现代采样算法细节 |
| R36 | [Robbins (1952), Some Aspects of the Sequential Design of Experiments](https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society/volume-58/issue-5/Some-aspects-of-the-sequential-design-of-experiments/bams/1183517370.pdf) | 一手原文 §2，两枚硬币、依后果切换、长期损失及稀疏探索构造 |

### 首批史实界限和技术验算

1. **01章：**1898 实验报告与 1911 年效果律明确表述分别定位；1911 Chapter II Cat 12 Box A 24项数据逐数核对，前4次均值85秒，后4次均值6.75秒。**1898 原著全109页尚未逐页通读**；不声称猫突然懂得机械原理。
2. **02章：**1938 著作年份、1990 年研究者一手回顾及1957强化日程出版信息已核；APA术语区分负强化／惩罚；FR/FI的规则解释与计数、时间例子单独验算。**1957全书具体实验效应未逐图复核**，正文不引用未经核对的个体实验数字。
3. **03章：**1933 Thompson期刊题名、年份与论文类型已核，**付费全文未通读**；Robbins 1952 §2 原始PDF的硬币规则和渐近平均损失讨论已核；现代遗憾定义、ε-greedy概率及 Beta 后验积分（5/6）独立验算，明确不倒推给1933作者。
4. **尚未完成：**非虚构独立连续性审计、结构审稿、对全文所有脚注的逐段二次核查，以及第04章以后的全部证据验收。

## 第二批04—06章增量研究与证据边界（2026-11-09）

> 【限域】此节只支持04、05、06章的具体审定论断；未将整个书、全部出版物或后续章节事实核验判定为已完成。正文引用 M/D/P 别名，见对应 `claims.json` 映射。

| 新来源 ID | 文献／馆藏入口 | 具体使用范围与限制 |
| --- | --- | --- |
| R37 | [Samuel, A. L. (1959), Some Studies in Machine Learning Using the Game of Checkers](https://gwern.net/doc/reinforcement-learning/model-free/1959-samuel.pdf) | IBM Journal of Research and Development 3(3):210–229，一手论文全文；核对pp.211—221及方法限制；IBM刊载书目信息 DOI:10.1147/rd.33.0210 |
| R38 | [Bellman (1952), On the Theory of Dynamic Programming](https://doi.org/10.1073/pnas.38.8.716) | PNAS 38(8):716–719；期刊目录与影印；一手论文，早期递推与存在性条件 |
| R39 | [Bellman (1954), The Theory of Dynamic Programming](https://www.ams.org/bull/1954-60-06/S0002-9904-1954-09848-8/S0002-9904-1954-09848-8.pdf) | Bulletin of AMS 60:503–515；1953报告／1954发表，最优性原理、确定／随机递推；主要核对pp.503—506 |
| R40 | [Bellman, Dynamic Programming (Princeton 1957 first edition)](https://store.doverpublications.com/products/9780486317199) | Dover版次说明明确其重印1957年Princeton版；本轮仅核对出版版次，未逐页通读全书 |
| R41 | [Bellman (1957), A Markovian Decision Process](https://iumj.s3-us-west-2.amazonaws.com/abstracts/56038_abs.pdf) | Journal of Mathematics and Mechanics 6(5):679–684；一手论文首页递推已核，其余证明页未获全文核验 |
| R42 | [Howard (1960), Dynamic Programming and Markov Processes](https://www.si.edu/object/dynamic-programming-and-markov-processes%3Asiris_sil_26454) | Smithsonian馆藏记载1960、书名、136页、与MIT论文关系；馆藏书目核验，非全书细读 |
| R43 | [Ronald A. Howard chronological bibliography](https://www.ronhoward.org/pure-ron/bibliography) | 研究者相关文献年表交叉佐证1959论文与1960专著，不是MDP首次概念的独家归属证据 |
| R44 | [Kaelbling, Littman & Cassandra (1998), Planning and Acting in Partially Observable Stochastic Domains](https://www.sciencedirect.com/science/article/pii/S000437029800023X) | Artificial Intelligence 101(1–2):99–134；期刊摘要核证POMDP与隐藏状态问题；不倒叙归为1957论文结果 |
| R45 | [Puterman (1994), Markov Decision Processes: Discrete Stochastic Dynamic Programming](https://doi.org/10.1002/9780470316887) | Wiley学术专著；正式出版记录与相关折扣MDP章节目录，作为现代数学边界参考 |

### 三章历史先后与技术要点

1. **04 塞缪尔1959**：一手论文全文核到页码：pp.211—213 已知规则、棋局搜索、评价函数和既有程序前驱；pp.214—221 记忆式学习与泛化、Alpha/Beta结构、局限性。**论文反对“完全从零”与“已证明最优收敛”**。
2. **05 贝尔曼1952—1957**：1952 PNAS 38(8):716—719可查；1953年数学会报告、1954刊发原文明确最优性原理；1957《Dynamic Programming》是普林斯顿原版，书目已核，**全书未逐页核读**。1957《A Markovian Decision Process》只核到原文首页及期刊信息。
3. **06 MDP谱系**：1957 Bellman论文首页给出状态转移概率加权递推；Howard 1960专著由史密森馆藏与作者年表交叉确认；1998 Kaelbling/Littman/Cassandra资料用于部分可观察问题的**后世理论边界**，并非1957理论已完整解决的结果。
4. **教学演算复核**：04章两次评价函数权重变化(6,3.4)→(2,5)，minimax结果4；05章二元20阶段2^20=1,048,576、仓库收益11与折扣10.1/6.5；06章价值6.76与3.16，均为原创建模和独立验算，**不是历史实验数据**。
5. **审核仍待做**：独立连续性审计、结构审稿和稿件级细节检查；上述证据记录用于当前初稿写作许可，不替代最终独立审稿。

### 第二批年代复核补正（2026-11-09）

| ID | 补充原始机构记录 | 准确范围 |
| --- | --- | --- |
| R46 | [Howard, *Studies in Discrete Dynamic Programming*, MIT Sc.D. Thesis (1958)](https://dspace.mit.edu/entities/publication/0171fa39-3922-4636-a02f-a123fe63477f) | MIT机构馆藏“Date Issued 1958”，与[INFORMS传记](https://www.informs.org/content/view/full/269156)的1958博士年份一致。个人年表R43列作1959，属来源冲突；正文优先采用正式学位馆藏，1960年专著另见R42。 |

## 第三批07—09章增量研究档案（2026-11-09）

> 此处只对07—09的明确论断提供对应来源和技术解释，不是全书完整史实核证。正文的 C/Y/K来源缩写可通过各章 claims JSON 映射为R编号。

| 新来源 | 论文或馆藏入口 | 本批证据范围与明确限制 |
| --- | --- | --- |
| R47 | [Bellman & Kalaba (1961), Reduction of Dimensionality, Dynamic Programming, and Control Processes](https://doi.org/10.1115/1.3658896) | ASME 83(1):82–84，原刊摘要关于高维控制问题；未验证短语最早出现 |
| R48 | [Puterman & Shin (1978), Modified Policy Iteration Algorithms for Discounted Markov Decision Problems](https://doi.org/10.1287/mnsc.24.11.1127) | INFORMS Management Science 24(11):1127–1137，关于修改策略迭代、收敛、计算对比的原始摘要；定理证明待全读 |
| R49 | [Sutton (1990), Integrated Modeling and Control Based on Reinforcement Learning and Dynamic Programming](https://papers.neurips.cc/paper_files/paper/1990/hash/d9fc5b73a8d78fad3d6dffe419384e70-Abstract.html) | NeurIPS官方会议摘要，Dyna-AHC及Dyna-Q；注意同年ICML论文R08另提Dyna-PI |
| R50 | [Michie & Chambers (1968), BOXES: An Experiment in Adaptive Control](https://aitopics.org/download/classics%3A10C04649) | 历史原始研究存档，杆平衡自适应控制先驱；具体实验次数未核，正文不用 |
| R51 | [Barto, Anderson & Sutton (1982), Synthesis of nonlinear control surfaces by a layered associative search network](https://pubmed.ncbi.nlm.nih.gov/7093360/) | PubMed论文书目摘要，Biological Cybernetics 43:175–185，是1983年工作的相关前驱 |
| R52 | [C. W. Anderson, Publications: academic bibliography](https://www.cs.colostate.edu/~anderson/wp/publications/) | 作者学院公开书目，校对1983研究三位作者和1982工作脉络 |

### 历史时间线与研究支线

- **1961年高维难题**：Bellman—Kalaba原始出版摘要明确把高维状态向量视作动态规划在控制问题中的困难。不能未经版本考证就说“curse of dimensionality”一词必定首发于这篇论文。
- **1990年Dyna**：ICML论文R08和NeurIPS论文R49均属Sutton1990研究，但不应当作同一篇：前者摘要列出 Dyna-PI、Dyna-Q，后者摘要列出 Dyna-AHC、Dyna-Q；都说明真实交互和学习模型基础上的规划相结合。
- **1983年倒立摆**：IEEE R04明确为Barto、Sutton、Anderson三名作者，研究未知小车—杆动力学、失败信号与ASE/ACE。Michie与Chambers1968 BOXES及1982相关论文R51是前驱。第08章（1990）到第09章（1983）属于**教学认识顺序的历史回溯**，不能写作严格年代继承。

### 数学独立复核和未尽证据

- 07章：(10^{10})个状态、4动作、每值8字节=320GB（十进制，不计其他内存）；(5^4=625)、(50^4=6,250,000)；两状态同步值迭代 (V_1(A)=2, V_2(A)=4.5)。全部是作者设计的教学模型，不是1961原始实验。
- 08章：确定性A→B→终点，(alpha=1,gamma=0.9)，经历两次真实更新后，使用学习模型重演A→B可使 (Q(A)=0.9)。**只有在模型相应转移正确时才能如此计算**。
- 09章：现代教学式误差 (delta=0+0.9(-0.3)-0.2=-0.47)，更新 (0.2+0.2(-0.47)=0.106)；绝非1983 ACE准确原始参数更新。
- R47、R48、R49及R04的关键论断主要核至权威出版社／会议的原始出版页面和摘要，原文所有证明与试验图表仍待独立全文二审，不可冒称终审或科研复现。

## 第四批10—12章研究与归属限度（2026-11-09）

> 在本批中，`evidence_verified`只能指第10—12章所列可支持事实的**写作前核查**，不代表每份原始论文全部章节已完成目视复核。别名TD-/Q/S见逐章claims映射到R号。

| 来源ID | 一手/学术资料入口 | 所支持的具体层级与限制 |
| --- | --- | --- |
| R53 | [Sutton (1988), Learning to Predict by the Methods of Temporal Differences](https://mlanthology.org/mlj/1988/sutton1988mlj-learning/) | Machine Learning 3:9–44，原刊题名、作者、摘要；TD作为预测方法的系统化、先驱（Samuel/Holland/自适应评价）、限定情形收敛 |
| R54 | [Sutton (1988), original paper scan, random-walk §3.2](https://www.derongliu.org/adp/adp-cdrom/refs/sutton19880009.pdf) | 原论文文本摘录核对天气周一/周二例子和A—G七状态对称随机游走；截图服务未成功，不引用未经目视确认的图表坐标或性能数字 |
| R55 | [Watkins (1989), Learning from Delayed Rewards, Cambridge PhD thesis](https://www.repository.cam.ac.uk/items/f1ce2aa9-2e01-4a08-92b7-1eec76b652ed) | 剑桥大学机构一手馆藏，1989-05-10学位论文提交记录、作者与摘要：从延迟奖励学有效行为、动态规划与增量学习 |
| R56 | [Christopher Watkins, Reinforcement Learning: Some History (author recollection)](https://www.cs.rhul.ac.uk/home/chrisw/RL_some_history.html) | 作者本人历史回顾，1989年向Barto与Sutton分享草稿；属多年后回忆，不可虚构逐字会谈 |
| R57 | [Watkins & Dayan (1992), Q-Learning, Machine Learning 8:279–292](https://doi.org/10.1007/BF00992698) | 原刊出版摘要与部分全文文本，离散表格、重复采样和学习率等条件下最优动作价值的概率一收敛；与1989论文分开 |
| R58 | [G. A. Rummery (1994-10-04), TR166 author announcement and abstract](https://groups.google.com/g/comp.ai.neural-nets/c/GtWN2rmxvME) | 原作者1994公告：Rummery与Niranjan、Cambridge Engineering TR166、Modified Connectionist Q-Learning、在线更新/神经逼近；原文并非直接命名SARSA |
| R59 | [Rummery & Niranjan (1994), Cambridge TR166 external academic bibliography](https://www.cs.utexas.edu/~shivaram/readings/b2hd-RummeryNiranjan1994.html) | 大学学术书目交叉确认1994技术报告号及原题；报告全部参数与实验图表尚未逐页核对 |
| R60 | [Singh, Jaakkola, Littman & Szepesvari (2000), Convergence Results for Single-Step On-Policy Reinforcement-Learning Algorithms](https://doi.org/10.1023/A:1007678930559) | 原始期刊摘要，on-policy单步控制、递减/持续探索与特定条件收敛，不能外推到一般深度函数逼近 |
| R61 | [Dayan & Sejnowski (1994), TD(lambda) Converges with Probability 1](https://www.gatsby.ucl.ac.uk/~dayan/papers/ds94.pdf) | 作者论文摘要与发布记录，对TD(lambda)部分形式加强概率一收敛结果，强调与1988期望收敛区别 |

### 必须保留的时间线和科学条件

- **1988 TD**：Sutton论文《Learning to Predict by the Methods of Temporal Differences》首先是**预测学习**的理论系统化；天气周一50%/周二75%是原文用来阐释TD的假设示例；七状态A—G随机游走来自原文§3.2。它明确承认1959 Samuel跳棋、Holland bucket brigade和更早adaptive heuristic critic的相关思想。TD(λ)、TD(0)的现代符号与原论文符号须区分，收敛结论不得无限推广。
- **1989／1992 Q-learning**：剑桥大学馆藏Watkins博士论文提交日为1989-05-10，Watkins与Dayan1992期刊论文则专门详证表格有限Markov环境下，在充分采样和适当学习率等前提下的最优动作价值概率一收敛。**这不是任意离策略神经网络的全局保证**。
- **1994／1996 SARSA**：Rummery与Niranjan1994剑桥工程系TR166摘要使用**Modified Connectionist Q-Learning**命名；Sutton与Barto2018教材历史注释将Sarsa名的引入归于Sutton1996；不能把1994技术报告标题改成“SARSA”。2000年Singh等提供特定探索条件下的在策略理论结果。
- **现代同样数字不同目标**：设(Q(s,a)=2,r=-1,gamma=.9,alpha=.5,Q(s',左)=6,Q(s',右)=1)，下一实际动作选右。Q-learning目标4.4、一次更新3.2；SARSA目标-0.1、一次更新0.95。两者均正确且都是**作者自设教学例题**，不是学术论文原始实验。TD另例(p=.5)周二(p=.75)以(alpha=.2)更新至.55；状态估值.4→.4575，(delta=.23)。
- **本批未完成**：1988论文与1992论文PDF截图服务失败，虽可获取原始文本段落、期刊摘要，但不能宣称所有图表已目视二核；1994剑桥TR166全文未完整阅读；尚无独立连续性审稿、发展审稿或终稿批准。
