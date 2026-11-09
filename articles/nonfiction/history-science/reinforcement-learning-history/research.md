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
- [ ] Bellman 1957 初版、Howard 与 MDP 术语史；不可只用现代教材反推历史。
- [ ] Sutton 的 TD 方法此前 Samuel／Witten／其他前驱及首创归属。
- [ ] Watkins 1989 论文、SARSA/Rummery-Niranjan 源流与收敛条件。
- [ ] 经验回放技术的早期 Lin 论文与 DQN 的差别。
- [ ] 致命三角典型反例及成立条件；数学推导逐项验算。
- [ ] 多智能体 RL、机器人控制、层次方法的遗漏贡献与性别／地域偏差。
- [ ] 2024—2026 的最新工作若拟加入，只能在补核一手论文后追加；不以趋势宣传当定论。

## 证据等级使用规则

- **A**：原始研究方法、发表年份、结论与限定均与原文交叉核对。
- **B**：出版记录及摘要已核，但未核对正文细节；仅可支撑概述。
- **C**：专业综述支持，适宜历史背景，不单独支持争议归属。
- **D**：编辑假设、类比或待核猜想，不进入正文事实陈述。

截至2026-11-09，第01—03章关键出版信息、可访问一手章节和对应技术定义已开展**限定范围前置核验**；其余章节以及三章中未通读完整著作的争议细节仍属 **B/C 或待核**。只能在所列证据范围内起草，不据此声称全书全面核证。下游章节动笔前，必须将相关事实升级到足够的 A/B 证据，创建实际的 `draft/NN.claims.json`，并由独立审阅检查。

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
