# 资料库｜深度学习发展史（初版研究索引）

> **核证范围声明（2026-11-09）**：本文件已对下列若干原始论文/机构页面的书目信息、发表时间与公开摘要或公告进行起始检索，尚**未逐章研读全文和独立交叉核验所有历史主张**。因此此处是**策划级前置书目**，不是可以设置`evidence_verified=true`的证据核验报告。个别早期争议、2023—2026年比较结论必须进一步查证。

## 一、已定位的高价值来源入口

| source_id | 年代 | 作者/机构 | 文献与链接 | 当前只可支持的范围 |
| --- | --- | --- | --- | --- |
| R01 | 1943 | McCulloch & Pitts | [A Logical Calculus of the Ideas Immanent in Nervous Activity](https://doi.org/10.1007/BF02478259) | 形式神经元、阈值逻辑；不可声称已训练 |
| R02 | 1958 | Rosenblatt | [The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain](https://pubmed.ncbi.nlm.nih.gov/13602029/) | 感知机论文与发表时间 |
| R03 | 1980 | Fukushima | [Neocognitron](https://pubmed.ncbi.nlm.nih.gov/7370364/) | 视觉层级、位置变化与无监督组织 |
| R04 | 1986 | Rumelhart, Hinton & Williams | [Learning Representations by Back-propagating Errors](https://doi.org/10.1038/323533a0) | 隐藏单元的权重调整；非反向模式求导的唯一发明起点 |
| R05 | 1998 | LeCun et al. | [Gradient-based Learning Applied to Document Recognition](https://proceedingsoftheieee.ieee.org/gradient-based-learning-applied-to-document-recognition/) | CNN在文档识别任务的训练及应用 |
| R06 | 1997 | Hochreiter & Schmidhuber | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 循环梯度难题与LSTM |
| R07 | 2003 | Bengio et al. | [A Neural Probabilistic Language Model](https://jmlr.org/papers/v3/bengio03a.html) | 分布式词表示与概率建模 |
| R08 | 2006 | Hinton, Osindero & Teh | [A Fast Learning Algorithm for Deep Belief Nets](https://doi.org/10.1162/neco.2006.18.7.1527) | 逐层无监督预训练及深层信念网络 |
| R09 | 2009 | Deng et al. | [ImageNet: A Large-Scale Hierarchical Image Database](https://doi.org/10.1109/CVPR.2009.5206848) | 数据库的提出和标注组织；不是ILS VRC 2012获胜论文 |
| R10 | 2012 | Krizhevsky, Sutskever & Hinton | [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) | CNN、GPU与分类结果；原版/转录的数字须再次核对 |
| R11 | 2015/2016 | He, Zhang, Ren & Sun | [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) | 残差网络原始预印本及后续发表 |
| R12 | 2014/2015 | Bahdanau, Cho & Bengio | [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) | 翻译中的软对齐注意力 |
| R13 | 2014 | Goodfellow et al. | [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661) | 对抗式生成模型原论文 |
| R14 | 2017 | Vaswani et al. | [Attention Is All You Need](https://research.google/pubs/attention-is-all-you-need/) | Transformer的提出与并行化 |
| R15 | 2016 | Silver et al. | [Mastering the Game of Go with Deep Neural Networks and Tree Search](https://www.nature.com/articles/nature16961) | 策略/价值网络+树搜索 |
| R16 | 2021 | Jumper et al. | [Highly Accurate Protein Structure Prediction with AlphaFold](https://www.nature.com/articles/s41586-021-03819-2) | CASP14与AlphaFold2方法的边界 |
| R17 | 2022 | Rombach et al. | [High-Resolution Image Synthesis with Latent Diffusion Models](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html) | 潜空间扩散、条件生成与效率 |
| R18 | 2022 | OpenAI | [Introducing ChatGPT（产品公告，非独立科学评价）](https://openai.com/index/chatgpt/) | 2022-11-30公开预览与RLHF说明；评价须另找独立材料 |
| R19 | 2024 | Nobel Prize | [2024 Physics Prize Press Release](https://www.nobelprize.org/prizes/physics/2024/press-release/) | Hopfield/Hinton获奖事实；不替代历史贡献分析 |
| R20 | 2025 | DeepSeek | [DeepSeek-R1 Release（厂商公告，非独立效果核验）](https://deepseek.com/en/news/deepseek-r1/) | 2025-01-20发布声明、开放权重与后训练叙述 |
| R21 | 2020 | Kaplan et al. | [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) | 固定条件下的经验规模律 |
| R22 | 2018 | Devlin et al. | [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805) | BERT的双向预训练及下游迁移 |
| R23 | 2021 | Radford et al. | [Learning Transferable Visual Models from Natural Language Supervision](https://arxiv.org/abs/2103.00020) | CLIP图文对比式预训练 |
| R24 | 2019 | Cornell Chronicle | [Professor’s Perceptron Paved the Way for AI—60 Years Too Soon（校方史料文章）](https://news.cornell.edu/stories/2019/09/professors-perceptron-paved-way-ai-60-years-too-soon) | 感知机背景和当时公众传播；历史解释需交叉验证 |

**来源分级**：R01—R17、R21—R23以研究论文为主；R18/R20为**发布者自述**，不得据以声称独立比较结论；R19为奖项官方声明；R24为校方历史报道而非原论文。所有论文原文结论仍须与后续复现、批判文献对照。R09注意ImageNet数据库与ILSVRC评测的年份和样本口径不同；R10原论文页面与流传版本在分类误差数据口径可能出现差异，正文不得未经核对引用具体百分比。

## 二、叙述中拟使用、但目前不可直接宣称已核证的节点

| 待核主题 | 首选材料与校验路径 | 风险 |
| --- | --- | --- |
| 古代思想—近代计算的远源比较 | 数学思想史、原典与现代史学专著交叉对照 | 相似思想不是直接血统 |
| 神经科学前史和Hebb 1949 | *The Organization of Behavior* 原著与学术史 | 可塑性假说与现代学习算法不同 |
| Widrow–Hoff、Minsky/Papert与1969争议 | 原论文、*Perceptrons*、AI史多来源 | 禁止‘一本书引发AI寒冬’单因论 |
| 1970年代自动微分、Werbos与Linnainmaa | 原始著作与自动微分史 | ‘反向传播的发明者’优先权复杂 |
| Hopfield 1982、Boltzmann机器1985 | 原论文及研究史 | 模型思想、方法、实践区分 |
| SVM、核方法的比较 | Vapnik等著作与真实任务评测 | 数据集/评测方案不可后见选择 |
| 2010前后语音识别产业化、中文语音 | 系统论文、公司档案、公开基准 | 不可编造采用年份、准确率 |
| word2vec、seq2seq、GPT-3与训练规模 | 官方论文、完整实验设置 | 模型参数与性能须核不同版本 |
| AlphaGo Zero、GAN—扩散分支 | 原论文及史学分析 | 别把不同算法合并 |
| 中国/国际学界及开源生态 | 研究论文作者署名、机构信息、模型卡与协议 | 国籍不等于归属；开放权重≠数据开放 |
| 2024—2026推理模型、效率、评测 | 正式技术报告+第三方评测，注明截稿日 | 时效性强；不将供应商广告当事实 |

## 三、重点反例与史学敏感点

1. 1943年形式神经元是计算/逻辑模型的重要节点；不能说该模型可像今天的深度网络一样从海量数据端到端训练。
2. Rosenblatt的感知机有具体结构和不同变体；‘单层感知机不解XOR’不能推论‘任何多层网络不解XOR’。
3. 链式法则、反向模式自动微分、神经网络反向传播是有关联但并非同一发明事件；1986年是重要传播与应用节点。
4. 卷积网络与新认知机存在形态和研究方法上的复杂关系；必须在细节上区别训练方式。
5. 2012年AlexNet效果不能孤立于ImageNet标注、GPU、ReLU、数据增强、dropout及实验社区。
6. Transformer不等于最早注意力机制；2017年论文在序列建模与并行化上有自己的创新。
7. AlphaFold的结构预测准确不等同于掌握蛋白质折叠动力学、所有蛋白质复合体或医学问题。
8. ‘会生成流畅文本’不等于事实准确；基准成绩不直接推出现实可靠性。
9. 对2025年厂商发布和2026年进展须拆分“发布时间—技术报告—独立评估—实际落地”。

## 四、章节级核证流程（未执行完成）

- 对每章提出3—6个可检验的历史主张，为每个主张赋`claim_id`，附原文页码/图表和发表版本。
- 对关键年份、人物、机构与性能数字使用至少一份原始资料；解释性/争议主张补至少一份可靠二手史学或独立研究。
- 对公式与例题执行独立推导/复算，写明现代回译与历史原表达的差别。
- 每章正文完成后生成`draft/NN.claims.json`且其中每条断言追溯本索引的source_id；待核未解则不可标记成稿。
- 完成上游证据核查与真正的编辑审查后，才能显式批准`evidence_verified`；本次未授权做此事。

## 五、第一批第01—03章：已完成的前置来源核对（2026-11-09）

> **阶段批准范围仅01—03章。** 已通过公开学术书目、原始论文摘要/历史综述交叉核对下列**中心史实**并明确其支持范围。并非声称所有细节均完成正式全文查证；未来章节仍为待核证。正文如需增加细节，必须新增claim和来源支持；拟写现代教学例题需独立验算，不构成历史史料。

| ID | 文献（入口） | 类型 | 可直接支持的范围 |
| --- | --- | --- | --- |
| DL01 | [Aristotle’s Logic](https://plato.stanford.edu/entries/aristotle-logic/) | SEP；学术综述 | 亚里士多德三段论、前提/结论结构及其范围限制 |
| DL02 | [Mohist Canons](https://plato.stanford.edu/entries/mohist-canons/) | SEP；学术综述 | 墨经年代大范围、名实分类和论辩；不支持现代形式逻辑等同 |
| DL03 | [Logic in Classical Indian Philosophy](https://plato.stanford.edu/entries/logic-india/) | SEP；学术综述 | 古典印度正理/佛教逻辑的推理与证据传统 |
| DL04 | [Leibniz: Logic](https://iep.utm.edu/leib-log/) | IEP；学术综述 | 莱布尼茨逻辑演算与通用符号愿景；不是现代编程 |
| DL05 | [George Boole](https://plato.stanford.edu/entries/boole/) | SEP；学术综述 | 1847、1854布尔著作与代数逻辑 |
| DL06 | [Frege’s Logic](https://plato.stanford.edu/entries/frege-logic/) | SEP；学术综述 | 1879概念文字与量化逻辑；历史贡献归属需带争议 |
| DL07 | [Interpretations of Probability](https://plato.stanford.edu/entries/probability-interpret/) | SEP；学术综述 | 帕斯卡-费马、概率数学化与1933柯尔莫哥洛夫公理化 |
| DL08 | [Bayes & Price, An Essay...](https://doi.org/10.1098/rstl.1763.0053) | 1763皇家学会《哲学汇刊》原始书目 | 贝叶斯/普赖斯论文、期刊第53卷；1763/1764书目口径注意 |
| DL09 | [Isaac Newton](https://plato.stanford.edu/entries/newton/) | SEP；历史综述 | 牛顿微积分与十七世纪数学背景；与莱布尼茨独立发展 |
| DL10 | [Nobel Prize in Physiology or Medicine 1906](https://www.nobelprize.org/prizes/medicine/1906/summary/) | 诺奖官方历史记录 | 1906高尔基、卡哈尔共同获奖 |
| DL11 | [A Century of Neuroscience Discovery: Golgi and Cajal](https://pmc.ncbi.nlm.nih.gov/articles/PMC2235197/) | 同行评审历史科学综述 | 1873黑色反应、网状/神经元学说分歧、卡哈尔工作 |
| DL12 | [Bennett 1999, The Early History of the Synapse](https://doi.org/10.1016/S0361-9230(99)00094-5) | 神经科学史综述 | 谢灵顿1897采用synapse用语；不推出所有生理机制 |
| DL13 | [Sherrington's Integrative Action: Centennial Appraisal](https://pubmed.ncbi.nlm.nih.gov/17223135/) | 历史神经科学综述 | 1906年反射整合和突触的理论组织作用 |
| DL14 | [Nobel 1932: Network Management](https://www.nobelprize.org/prizes/medicine/1932/speedread/) | 诺奖官方科学史科普 | 阿德里安单纤维测量和全或无脉冲 |
| DL15 | [Adrian & Bronk 1928, Discharge of Impulses...](https://pubmed.ncbi.nlm.nih.gov/16993976/) | 1928原始研究书目 | 单纤维记录的论文年代和作者；细节不得仅由摘要推断 |
| DL16 | [Brunel & van Rossum 2007, Lapicque's 1907 Paper](https://pubmed.ncbi.nlm.nih.gov/17968583/) | 同行评审历史研究 | 拉皮克1907与积分-发放现代回译的关系 |
| DL17 | [Turing 1936, On Computable Numbers](https://www.verostko.com/turing/1936-paper.html) | 1936原始论文授权HTML转载 | 可计算性与理论机器；不是1943网络可学习的证据 |

### 证据审查小结与限制

- **01章（数学远源）**：DL01—DL09涵盖逻辑史、多文明论证传统、近代形式逻辑、概率与微积分。验证的是**思想与著作史事实**，并不能证明这些传统之间存在直接传承，更不能证明古代“发明深度学习”。现代教学的逻辑真值表、测试条件概率、单参数梯度下降由作者复算，明确非历史实验。
- **02章（神经生理）**：DL10—DL16覆盖诺奖官方记录与同行评审神经科学史：Golgi和Cajal的贡献与分歧、突触观念、神经脉冲测量、Lapicque的历史回译。确证的是**可追溯的研究方向和关键节点**，不把生物神经元描述为仅有二值信号。
- **03章（1943理论）**：R01 [McCulloch & Pitts](https://doi.org/10.1007/BF02478259)，1943年《数学生物物理学通报》5:115—133，摘要支持全或无神经活动、循环回路需更复杂逻辑、特定逻辑表达式可由网络实现；DL17帮助限制可计算性措辞。神经元阈值演示是现代简化的形式例子，而非论文原始装置实验。
- **仍需编辑注意**：贝叶斯原文出版口径、谢灵顿术语采用年份、Lapicque现代公式与原始论文区分；文章不能据文献摘要宣称已经重建作者全部数学证明。技术上对简单例题已做算术/逻辑核对，复杂证明暂不进入正文。

### 第一批 source / claim 对照与放行范围

| claim_id | 内容 | 来源 | 校验结论 |
| --- | --- | --- | --- |
| C01-01 | 亚里士多德有系统三段论，传统与今日形式逻辑非同一体系 | DL01 | 核验中心事实，历史解释有范围限制 |
| C01-02 | 墨家与印度逻辑传统讨论分类、论证和推理，各有不同方法 | DL02,DL03 | 核验；不推出文明直传 |
| C01-03 | 莱布尼茨通用演算理想、布尔1847/1854逻辑代数、弗雷格1879概念文字 | DL04,DL05,DL06 | 核验核心书目与差别 |
| C01-04 | 近代概率数学化、贝叶斯-普赖斯论文和微积分前史 | DL07,DL08,DL09 | 关键书目核验；精确出版口径谨慎 |
| C01-05 | 梯度教学例L=(2w-6)^2，在w=2、η=0.1时由4降至0.16 | 作者独立算术推导 | VERIFIED_DERIVATION；不是史实 |
| C02-01 | 1906 Golgi+Cajal诺奖及理论分歧 | DL10,DL11 | 双源核证 |
| C02-02 | Golgi银染方法1873及Cajal神经元学说贡献 | DL11 | 可靠综述核证，具体实验页码后补 |
| C02-03 | Sherrington/突触名称与反射整合的历史 | DL12,DL13 | 双综述核证 |
| C02-04 | Adrian/ Bronk脉冲测量、全或无与发放频率 | DL14,DL15 | 原始论文书目+官方科学史交叉核证 |
| C02-05 | Lapicque 1907与现代积分-发放模型关联 | DL16 | 史学综述核证；不归属现代公式逐字内容 |
| C03-01 | McCulloch、Pitts论文1943，题名与5卷115—133页 | R01 | 原出版页面核证 |
| C03-02 | 全或无、阈值、抑制、固定连接作为形式理想化假设 | R01 | 论文摘要与原文可查说明；模型规则按原文解释范围 |
| C03-03 | 非循环回路的命题逻辑表达与反馈回路之记忆 | R01 | 论文摘要直接支持；可计算性不泛化成两元件万能 |
| C03-04 | 1943模型不含现代有监督权重学习/梯度优化 | R01 | 对该文形式假设的有限范围解释，不排除后续人工网络新算法 |

## 六、第二批04—06章：前置史实研究与证据边界（2026-11-09）

**范围说明**：本批仅对04—06章的中心年份、论文书目、理论支持范围和现代例题开展前置核证，不能外推为全书史料已审。1958 Rosenblatt与1960 Widrow–Hoff原论文PDF已查看首页原版；1949 Hebb原书大体量扫描截图未成功，关于原书第62页使用原文可见摘录与同行评审研究交叉核对，不能声称已完整校勘该书。1969专著以MIT出版社说明和后续学术史解释为证据，不对未逐页读到的证明作细节复述。

| source_id | 可靠性类别 | 来源 | 可支持的具体范围 |
| --- | --- | --- | --- |
| DL18 | 原始著作书目与可见摘录 | [D. O. Hebb, The Organization of Behavior (1949)](https://www.angiologie-muenster.de/wp-content/uploads/2023/02/Hebb_1949_The_Organization_of_Behavior.pdf) | 第62页反复参与触发的假说、细胞集合及阶段序列（后两者见相应章节；需后续页码复核） |
| DL19 | 同行评审历史综述 | [Richard E. Brown, Donald O. Hebb and the Organization of Behavior: 17 years in the writing (2020)](https://doi.org/10.1186/s13041-020-00567-8) | 1949出版、此前十余年研究，Hebb synapse、cell assembly和phase sequence相互关系 |
| DL20 | 同行评审学术史 | [The Hebb Synapse Before Hebb (2021)](https://doi.org/10.3389/fnbeh.2021.732195) | 第62页原假设、赫布以前的联结与记忆思想，反对单人一夜发明的叙述 |
| DL21 | 当事学者后世访谈及学术分析 | [Carla Shatz访谈 (2020)](https://blogs.imperial.ac.uk/neuron-topic/2020/04/02/interview-with-professor-carla-shatz-when-i-received-the-phd-in-neurobiology-from-harvard-medical-school-in-1976-i-was-the-first-woman-to-do-so/)；[历史分析](https://pmc.ncbi.nlm.nih.gov/articles/PMC4006178/) | “fire together, wire together”并非1949 Hebb逐字原话；Shatz自述其传播经历 |
| DL22 | 1958原始论文元数据 | [Frank Rosenblatt, The Perceptron, Psychological Review 65(6):386–408](https://pubmed.ncbi.nlm.nih.gov/13602029/) | 论文的作者、期刊、年月、题目和页码 |
| DL23 | 1958原始论文首页扫描 | [Rosenblatt 1958 PDF](https://henriquetmaia.github.io/pdf/papers/rosenblatt1958.pdf) | 感知、记忆、存储如何影响识别的核心问题；与后世单阈值模型不完全等同 |
| DL24 | 康奈尔大学历史档案 | [Professor's perceptron paved the way for AI (2019)](https://psychology.cornell.edu/news/professors-perceptron-paved-way-ai-60-years-too-soon) | 1958年7月IBM 704上的感知机演示及当时报刊热情；校方历史叙事不能作独立效果评测 |
| DL25 | 博物馆藏品记录（页面可用性待核） | [Smithsonian, Mark I Perceptron](https://www.si.edu/object/electronic-neural-network-mark-i-perceptron%3Anmah_334414) | S感知/A联络/R响应等单元与实物传统；不能仅据检索结果断言特定完工月份 |
| DL26 | 1960原始论文首页扫描 | [Widrow & Hoff, Adaptive Switching Circuits](https://isl.stanford.edu/~widrow/papers/c1960adaptiveswitching.pdf) | ADALINE/自适应切换研究的误差驱动、训练示例与线性可分函数限制 |
| DL27 | 研究团队教学材料 | [Stanford PDP Handbook: The Delta Rule](https://web.stanford.edu/group/pdplab/pdphandbookV3/handbookch5.html) | 感知机纠错与Widrow–Hoff/LMS既相关又不同 |
| DL28 | 1969原始专著书目、出版方介绍 | [Minsky & Papert, Perceptrons (MIT Press)](https://mitpress.mit.edu/9780262130431/perceptrons/) | 1969著作、所讨论的特定架构、几何与函数类别的限制；不支持“所有神经网络都无效” |
| DL29 | 科学社会学同行评审研究 | [Olazaran, A Sociological Study of the Official History of the Perceptrons Controversy (1996)](https://doi.org/10.1177/030631296026003005) | 学术权力、资源分配和符号主义的竞争解释；不构成唯一因果证明 |
| DL30 | 英国议会上院研究回顾 | [AI in the UK: Historical background (2018)](https://publications.parliament.uk/pa/ld201719/ldselect/ldai/100/10005.htm) | 1973 Lighthill报告、英国AI领域政策背景及资金因果争议 |
| DL31 | 研究者在再版序中的史学反思 | [Léon Bottou, Foreword to Perceptrons (2017)](https://leon.bottou.org/papers/bottou-foreword-2017) | “一本书是否杀死研究”并不足以概括数学争议 |
| DL32 | 研究者论文目录 | [Stanford Widrow publication list](https://www-isl.stanford.edu/~widrow/publications.html) | 1960年Widrow–Hoff论文出版年、会议与页码 |

### 事实核证结论

**04章**：1949年Hebb关注的是神经活动反复参与产生长期连接效率变化的假设，同时提出细胞集合与阶段序列。其观点既有前驱研究，也不是现代误差反传。流行格言不是Hebb原话；现代 Δw=ηxy 只能作为教学简化。

**05章**：1958原文首先是感知与记忆的理论模型；IBM 704的演示和后来的Mark I硬件不应混成同一场景。简化感知机可以通过带标签的误判纠错学会线性分界，收敛与泛化不是无条件保证。1960 Widrow–Hoff具有另一种基于误差与均方意义的训练规则。

**06章**：XOR不可被单层线性阈值分类器实现，但有隐藏层的固定网络可以表达XOR，训练多层网络却是另外的问题。1969书对特定感知机架构给出了数学限制，学术与公共争议有复杂传播过程。1960年仍有自适应神经计算研究，1973年的Lighthill报告涉及AI研究资金与政策的另一路线，因此1969不是整个AI冬天的充分、唯一原因。

### 可自行复算的现代例题，不冒充历史实验

- Hebb简化教学式：若η=0.1，x=y=1，w=0.2→0.3；若x=0则此步无增长。该式不代表1949原书的完整生理模型。
- 感知机更新式：若目标y与评分符号不相容，w←w+ηyx、b←b+ηy。正/负样本训练两步可得到w=(2,0)、b=0；这仅是线性阈值教学模型。
- XOR证明：线性评分满足s(0,0)+s(1,1)=s(1,0)+s(0,1)。XOR要求左侧两项都负、右侧两项都非负，矛盾。
- 两隐藏单元的构造：h1=step(x1+x2−0.5)，h2=step(x1+x2−1.5)，输出step(h1−2h2−0.5)正好是XOR。这说明表示可能，不说明如何由数据学出这种连接。

### 待独立审稿重点

1. 赫布1949年原书全文扫描仍需就细胞集合相关原页进一步核查。
2. Rosenblatt原始多单元感知机与现代单神经元教学简化绝不等同；Mark I硬件具体年月暂不作肯定断言。
3. 1969年原书的复杂拓扑和连通性证明不在本轮复现范围内。
4. “AI冬天”的年代与具体经费因果，按独立史学研究核对；如来源不能支持绝对断言，必须改为解释性的有限表述。
