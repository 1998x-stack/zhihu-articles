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

截至2026-11-10，第01—21章已按各自批次对可访问原始研究、出版记录及明示具体主张开展**限定范围写作前核验**；第22章以后及部分未逐页复核的论文实验表格/代码仍待核。未完成全书独立双审、终审及发布。只能在所列证据范围内起草，不据此声称全书全面核证。下游章节动笔前，必须将相关事实升级到足够的 A/B 证据，创建实际的 `draft/NN.claims.json`，并由独立审阅检查。

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

## 第五批13—15章增量研究（2026-11-10）

> 【证据范围】仅支持本批正文的具体历史/数学论断，不代表书籍全文来源验证已完成。F/AC/TG别名由逐章claims JSON映射到对应R号。所有人工数学样本均不作历史实验数据。

| 新来源 | 权威论文或研究入口 | 已支持的论断及审稿限制 |
| --- | --- | --- |
| R62 | [Williams (1992), Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning](https://doi.org/10.1007/BF00992696) | 一手期刊8:229–256及可访问原文影印；随机单元、期望奖励梯度、即时和受限延迟强化；数学保证并非任意序贯任务通用定理 |
| R63 | [Ronald J. Williams author publication bibliography](https://ccs.neu.edu/home/rjw/pubs.html) | 作者本人书目，1992期刊论文与1991/1990相关研究脉络；不是复杂定理的独立证明 |
| R64 | [Barto Sutton Anderson (1983), Neuronlike Adaptive Elements ...](https://doi.org/10.1109/TSMC.1983.6313077) | 原始IEEE论文与可访问影印，对ASE/ACE角色、1983历史先后、BOXES先驱；既有R04但本批精读原文首页与前言 |
| R65 | [Sutton McAllester Singh Mansour (1999), Policy Gradient Methods for RL with Function Approximation](https://proceedings.neurips.cc/paper_files/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html) | 1999 NeurIPS官方摘要，明确可参数化随机策略、动作价值/优势辅助策略梯度与条件性局部最优结论 |
| R66 | [Konda Tsitsiklis (1999), Actor-Critic Algorithms](https://papers.nips.cc/paper/1999/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html) | 另一篇独立1999 NeurIPS论文，双时间尺度、线性TD Critic、近似梯度Actor；不与R65混为一篇 |
| R67 | [Konda Tsitsiklis, On Actor-Critic Algorithms, SIAM journal](https://doi.org/10.1137/S0363012901385691) | 后续一手期刊摘要，双时间尺度Critic线性逼近与受限收敛结果；不扩展为任意深度神经网络 |
| R68 | [Tesauro (1992), Practical Issues in Temporal Difference Learning](https://research.ibm.com/publications/practical-issues-in-temporal-difference-learning) | IBM原始研究目录/摘要，Machine Learning 8:257–277，纯棋盘表示与自我对弈可达较强中等水平 |
| R69 | [Tesauro (1993), TD-Gammon A Self-Teaching Backgammon Program Achieves Master-Level Play](https://research.ibm.com/publications/td-gammon-a-self-teaching-backgammon-program-achieves-master-level-play) | IBM AAAI Fall Symposium 1993-10-22记录，明确纯棋盘版本与加手工特征版本的水平区别 |
| R70 | [Tesauro (1994), TD-Gammon ..., Neural Computation 6(2):215–219](https://doi.org/10.1162/neco.1994.6.2.215) | 1994正式期刊论文与摘要，清楚区别raw board中等水平与手工特征后大师水平；不同于1993会议 |
| R71 | [Tesauro (1995), Temporal Difference Learning and TD-Gammon](https://www.bkgm.com/articles/tesauro/tdl.html) | 原作者1995 Communications of the ACM 38(3):58–68授权转载全文；版本细节、40隐藏单元/20万盘、51盘净负13点、38盘净负7点、四输出与随机骰子解释 |
| R72 | [Tesauro (2002), Programming Backgammon Using Self-Teaching Neural Nets](https://research.ibm.com/publications/programming-backgammon-using-self-teaching-neural-nets) | IBM原始期刊论文摘要，后续总结浅层搜索与doubling策略如何增强自学评价；不倒推到1992版 |
| R73 | [Tesauro (1989), Neurogammon Wins Computer Olympiad](https://doi.org/10.1162/neco.1989.1.3.321) | Neural Computation 1(3):321–323期刊书目及原文摘要，Neurogammon神经网络用专家数据训练，1989计算机奥林匹克双陆棋竞赛 |
| R74 | [Tesauro and Sejnowski (1989), A Parallel Network That Learns to Play Backgammon](https://doi.org/10.1016/0004-3702(89)90017-9) | Artificial Intelligence 39:357–390原始期刊摘要，人类专家评估位置数据训练的神经网络，交叉佐证Neurogammon监督路线 |

### 三章核心史学—技术边界

1. **REINFORCE（1992）**：Williams原始论文研究随机连接主义网络梯度，适用于即时强化和有限延迟任务；现代对数导数的整轨迹策略梯度是一种教学对照，不可当作原文对任意时序任务的统一证明。原创sigmoid训练数值p=0.7，alpha=0.1，抽中左得G=1，则theta增加0.03，p_new≈0.706262；左右+1/-1的两动作期望梯度0.42。
2. **Actor-Critic（1983及1999以后）**：Barto/Sutton/Anderson1983原文有ASE/ACE两类元件；1992 Williams在其原论文中已回顾这一先驱。1999年Konda/Tsitsiklis双时间尺度研究R66与Sutton/McAllester/Singh/Mansour策略梯度研究R65是两篇不同论文。现代教学样本TD误差0.23、Critic价值0.446、Actor权重变化0.0069、概率约0.701447，绝非1983实验。
3. **TD-Gammon（1992/1993/1994/1995）**：1992纯棋盘版本达较强中等水平；1993/1994论文明确手工特征版本达到强大师水平；1995授权转载提供更完整方法、40隐藏单元/20万盘纯输入结果、51盘净负13点和38盘净负7点等数值。相应单位是**点数而非输盘**；有限测试不证明普遍击败世界最强。后续版本涉及2-ply搜索，doubling模块不等同同一训练中的完全自发策略。
4. **Neurogammon及先驱**：1989 Tesauro与Sejnowski原论文有专家评估的监督学习线路，1989Tesauro记录计算机奥林匹克双陆棋比赛；不能写成Tesauro首次就放弃专家数据直接创造TD-Gammon。
5. **未完成事项**：1992 Williams所有推导的逐式二审、1999 Konda证明条件及1995 ACM原刊图表对比未全部独立审阅；章节连续性与发展性审稿均待真实单独执行。阶段仍为`draft_unreviewed`，`review_status=PENDING`。

## 第六批16—18章增量史料与验证边界（2026-11-10）

> 所列可用证据只支持16—18章明示的技术与年代论断；不构成其它章节自动写作许可。O/A/T正文别名详见对应claims JSON。史实原始文献、现代教材、原创教学算例三个层次严格区分。

| 新来源ID | 文献或官方记录 | 限定支持范围及注意事项 |
| --- | --- | --- |
| R75 | [Sutton, Precup & Singh (1999), Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning](https://doi.org/10.1016/S0004-3702(99)00052-1) | Artificial Intelligence 112(1–2):181–211一手全文。§2三元组I,pi,beta，§3 SMDP和折扣k，§4中断，§§5—7内部学习和子目标；作者明确承认时间抽象此前已有宏动作及层次研究 |
| R76 | [Sutton, Precup & Singh (1998), Between MDPs and Semi-MDPs, UMass TR98-74](https://web.cs.umass.edu/publication/docs/1998/UM-CS-1998-074.pdf) | 机构一手技术报告出版形式，1998报告和1999正式期刊不能混同 |
| R77 | [Boyan & Moore (1994 meeting), Generalization in Reinforcement Learning: Safely Approximating the Value Function](https://papers.nips.cc/paper/1018-generalization-in-reinforcement-learning-safely-approximating-the-value-function) | NeurIPS 1994会议，论文集卷7、pp.369–376可能用1995正式出版年；一手摘要与引言确认DP+函数逼近失稳及错误策略，介绍Grow-Support |
| R78 | [Tsitsiklis & Van Roy (1997), An Analysis of Temporal-Difference Learning with Function Approximation](https://doi.org/10.1109/9.580874) | IEEE Transactions on Automatic Control 42(5):674–690一手全文；线性TD在在线目标链抽样及假设1–4下收敛、非目标分布/非线性可能发散，已核PDF首页及正文条件 |
| R79 | [Baird (1995), Residual Algorithms: Reinforcement Learning with Function Approximation](https://mlanthology.org/icml/1995/iii1995icml-residual/) | ICML 1995 pp.30–37一手摘要/出版社记录；表格可收敛方法用线性及其他近似可不稳定，提出残差梯度/残差算法。教材七状态版本细节由R01明确支持 |
| R80 | [Sutton et al. (2009), Fast Gradient-Descent Methods for Temporal-Difference Learning with Linear Function Approximation](https://doi.org/10.1145/1553374.1553501) | ICML2009 pp.993–1000一手摘要；GTD2/TDC及线性离策略梯度TD条件性收敛与效率，非通用深度RL定理 |
| R81 | [Maei et al. (2009), Convergent Temporal-Difference Learning with Arbitrary Smooth Function Approximation](https://proceedings.neurips.cc/paper/2009/hash/3a15c7d0bbe60300a39f76f8a5ba6896-Abstract.html) | NeurIPS2009会议官方摘要：有限MDP、光滑逼近和随机近似条件下局部收敛，不保证一般深度网络全局最优 |

### 第六批有来源的主线

- **16 时间抽象**：Sutton、Precup、Singh1998 UMass TR和1999 *Artificial Intelligence* 论文分清；option=(I,π,β)与SMDP联系、选项中断、内部学习和子目标；不能假称时间抽象始于1999，也不能把options自动等同状态压缩与技能发现。
- **17 价值函数逼近**：Tesauro1992 TD-Gammon已经用神经价值函数；Boyan/Moore1994 NeurIPS论文直接警告函数逼近＋动态规划可能失稳或选错策略；Tsitsiklis/Van Roy1997在线线性TD正定理要求有限的马尔可夫和学习率等条件，并讨论非分布自然抽样及非线性反例。**不是所有神经强化学习都必然失败**。
- **18 致命三角**：2018教材总结函数逼近、自举、离策略训练的潜在失稳；1995 Baird论文给出表格更新搬入线性/非线性近似可能不稳的历史证据。2009 GTD2/TDC等针对特定线性离策略问题有更强的稳定理论；并未给任意DQN无条件保证。
- **原创演算16**：三步技能奖励(-1,-1,8)，结束未来价值5，gamma=.9得8.225；gamma=.5得1.125。
- **原创演算17**：φ(A)=(1,1),φ(B)=(1,.9)，初始w=(2,3)，对A目标6用alpha=.1更新成(2.1,3.1)，B从4.7变4.89。特意使用**外给监督目标**，不声称这一例为TD发散。
- **原创演算18**：人为只抽A→B、V(A)=w,V(B)=2w、gamma=.9、alpha=.1、r=0，半梯度更新w→1.08w；w10≈2.158925,w30≈10.062657。仅为局部自举放大机制图解，不是Baird完整七状态离策略反例或严格普遍发散定理。
- **仍待独立审稿**：全部原论文证明、Baird初始权重和七状态特征向量、1999 Option interruption实验图表、相关现代价值函数训练协议均未全部逐页独立复核。保持`draft_unreviewed`和`review_status=PENDING`。

## 第七批19—21章增量史料与实验口径（2026-11-10）

> 【范围】仅对本批具体历史和数学主张做分层前置核查；正文ER/EV/DQ别名映射见相应逐章claims JSON。1992、2013、2015、2018和2021之间不得人为制造直接先后取代的单线史。

| 新增ID | 论文及权威公开入口 | 可支持论断、文献等级与未证实边界 |
| --- | --- | --- |
| R82 | [Long-Ji Lin (1992), Self-Improving Reactive Agents Based on Reinforcement Learning, Planning and Teaching](https://doi.org/10.1007/BF00992699) | Machine Learning 8:293–321；原始期刊全文第2.3节讨论过去经历反向回放、随策略变化筛选样本，第6.2节加快学习。已核全文首页和章节，不能声称首次发明人类意义的记忆 |
| R83 | [Bellemare, Naddaf, Veness & Bowling (2013), The Arcade Learning Environment](https://doi.org/10.1613/JAIR.3912) | JAIR 47:253–279一手期刊；ALE为多游戏评测平台。2015 IJCAI是原2013论文的扩展摘要，并非首次提出年份 |
| R84 | [Mnih et al. (2013), Playing Atari with Deep Reinforcement Learning](https://arxiv.org/abs/1312.5602) | 2013-12-19 arXiv预印本；七款Atari游戏、6/7超过当时算法、3/7超过所用人类基线。作者名单与2015Nature大团队不同，不混写 |
| R85 | [Henderson et al. (2018), Deep Reinforcement Learning that Matters](https://doi.org/10.1609/aaai.v32i1.11694) | AAAI2018原始论文和官方全文：深度RL随机性、复现障碍、标准实验报告与显著性问题。并非指称全部早期工作无效 |
| R86 | [Machado et al. (2018), Revisiting the Arcade Learning Environment](https://research.google/pubs/revisiting-the-arcade-learning-environment-evaluation-protocols-and-open-problems-for-general-agents/) | JAIR 61:523–562原研究及2018 IJCAI扩展摘要；评测协议差异、训练期间表现、sticky action、游戏模式与不确定性。不可倒写为2015版已有全部方法 |
| R87 | [Agarwal et al. (2021), Deep Reinforcement Learning at the Edge of the Statistical Precipice](https://papers.nips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html) | NeurIPS2021一手论文，少种子统计误差、分层bootstrap、IQM、性能概貌和置信区间，不能把小样本bootstrap当无条件覆盖保证 |
| R88 | [Schaul et al. (2015 preprint / 2016 conference), Prioritized Experience Replay](https://arxiv.org/abs/1511.05952) | 2015预印本及后续ICLR2016论文，优先回放作为均匀随机回放的后续分支；不能倒说1992 Lin便采用该算法 |
| R89 | [Mnih et al. (2015), Nature DQN full paper and Extended Data](https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf) | 原始Nature论文全文和扩展超参数表的可访问学术影印：49游戏、43超过当时对比算法、29超过所用人类基线75%；84×84×4、100万帧回放、batch32、目标每1万次参数更新同步。2015主刊DOI对应R13 |

### 三章事实—技术—教学例子界限

- **19经验回放**：Lin1992原始论文§2.3讨论回放过去的真实状态动作经历、逆序回放以及策略和环境变化造成的风险；§6.2报告其研究设置中的学习加速。2015 Nature DQN采用从过去经验中均匀随机抽样的不同策略（R13/R89），不能把两套实现写成同一方法，也不能说2015首次发明回放。
- **20评测可靠性**：2013 ALE原刊R83提供跨Atari游戏评测平台。2018 Henderson R85讨论随机种子和复现；Machado R86讨论游戏模式、回合结束、时间预算、最佳检查点与sticky action。2021 Agarwal R87在少种子场景倡议分层bootstrap、IQM和性能分布；这些2018/2021方法论是对2015成功的后续审视，不是2015已有完整协议。
- **21 DQN**：Mnih等2013预印本7款游戏，6款超过当时比较算法、3款超过采用人类专家基线；2015 Nature R13/R89为49游戏，43款超过既有RL方法，29款达到所用人类测试者得分的**75%以上（不是29款超过人类）**。2015固定架构/超参数不意味着训练完成的一组权重跨49游戏直接通用。输入84×84×4、回放100万帧、batch32和目标同步间隔10000次参数更新来自2015原文Extended Data Table1。
- **19原创演算**：确定性路径A→B→C→G，奖励0/0/1，γ=.9、α=1。真实一次路径后A=B=0、C=1，倒序重放后B=.9、A=.81；不代表Lin实验运行。
- **20原创统计演算**：A种子0/0/0/0/150 vs B18/19/20/21/22，均值30 vs20、中位数0 vs20，25配对中A>B为5/25。8数值的普通均值22.5与IQM10；人类归一化用随机/人类基线演示50%与200%。全部为作者创设，不可挪成发表论文实测。
- **21原创TD示例**：Q预测2、即时奖励1、下一状态冻结目标网络最高Q=4、γ=.99，目标4.96、误差2.96；单参数插值2.296不等于DQN真正的共享参数批量梯度更新。
- **仍待**：原始DQN完整扩展表的逐项统计复核、2018/2021重复实验程序和随机种子分配的逐代码确认、不同benchmark的统计单位与IQM区间计算参数。章节均未做独立连续性或发展性审稿，不能把前置核验当`review_status=PASS`。
