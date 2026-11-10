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

## 七、第三批07—09章：独立事实研究与有限证据许可（2026-11-09）

> 此批**只核对第07—09章拟写的中心史实、可复算的数学原理及史学争议**；不是全文逐句核证，更不是对序章和第10—31章的研究许可。优先原始论文出版社、大学馆藏、专业史学论文；后来的诺奖材料只能用于回顾，不能冒充1980年代的当时证据。有关PDF，1985 LeCun会议文本的页面截图无法取得，正文仅用其公开摘要可查范围，不据未看到的页面推断细节。

| ID | 来源属性 | 文献 | 可支持范围与警戒线 |
| --- | --- | --- | --- |
| DL33 | 1970硕士论文大学图书馆原始馆藏 | [Seppo Linnainmaa, Algoritmin kumulatiivinen pyöristysvirhe... (University of Helsinki, 1970)](https://www.finna.fi/Record/helka.9933382303506253) | 证明1970年已有该芬兰硕士论文；书目本身不证明1986作者直接使用了它 |
| DL34 | 1976原始同行评审论文 | [Linnainmaa, Taylor expansion of the accumulated rounding error, BIT 16:146–160 (1976)](https://doi.org/10.1007/BF01931367) | 确定1976发表与误差反向累积分析主题；注意研究目标是数值误差 |
| DL35 | 自动微分领域学术史 | [Andreas Griewank, On automatic differentiation and algorithmic linearization (2014)](https://www.scielo.br/j/pope/a/kZ8M4LPYFryXQkdwHz7QXVx/?lang=en) | 讲述reverse AD与Linnainmaa前史，避免单一首次发明者争论 |
| DL36 | 计算/神经网络史学综述 | [Neural networks for perceptual processing: from simulation tools to theories, open access peer-reviewed review](https://pmc.ncbi.nlm.nih.gov/articles/PMC2323553/) | 指出1974 Werbos、1982 Parker与1986普及不同层级；二手史学概括需限定 |
| DL37 | Werbos原学位论文再版书目评论 | [The Roots of Backpropagation: From Ordered Derivatives to Neural Networks (1996 review of 1974 Werbos thesis)](https://doi.org/10.1088/0954-898X/7/1/008) | 确认1974 Harvard博士论文及后来再版；不据此宣称无争议的全部发明优先权 |
| DL38 | 史密森学会实物与年代记录 | [Intel 4004 Microprocessor, National Museum of American History, 1971](https://www.americanhistory.si.edu/collections/object/nmah_713495) | 1971微处理器商业化节点；不等于70年代具备现代深度网络训练算力 |
| DL39 | 1978统计模型原始论文 | [Ivakhnenko, The group method of data handling in long-range forecasting, Technological Forecasting and Social Change (1978)](https://www.sciencedirect.com/science/article/pii/0040162578900574) | 自组织多项式/模型选择统计路线；不等同1986反向传播或现代深度神经网络 |
| DL40 | 1979原始会议论文 | [Kunihiko Fukushima, Self-Organization of a Neural Network which Gives Position-Invariant Response, IJCAI 1979](https://ijcai.org/proceedings/1979/66) | 可核证1979已有neo-cognitron会议报告，不能把1980写作绝对首发 |
| DL41 | 1980原始研究刊物 | [Fukushima, Neocognitron, Biological Cybernetics 36:193–202 (1980)](https://pubmed.ncbi.nlm.nih.gov/7370364/) | 自组织无教师、S/C交替、位置平移稳定性为论文模型的目标与结果 |
| DL42 | 1982原始视觉研究 | [Fukushima & Miyake, Neocognitron: A new algorithm for pattern recognition tolerant of deformations and shifts (1982)](https://www.sciencedirect.com/science/article/pii/0031320382900243) | 1982后续方法描述与变形稳健性；不保证任意真实图像任务泛化 |
| DL43 | 1982原始论文公开存档 | [Hopfield, Neural networks and physical systems with emergent collective computational abilities, PNAS 79:2554–2558 (1982)](https://pmc.ncbi.nlm.nih.gov/articles/PMC346238/) | 联想记忆、内容寻址和集体能量机制；模型不等同监督分类器 |
| DL44 | 1985原始论文出版社信息 | [Ackley, Hinton & Sejnowski, A learning algorithm for Boltzmann machines, Cognitive Science 9:147–169 (1985)](https://doi.org/10.1016/S0364-0213(85)80012-4) | 1985论文作者、机制框架，统计物理和随机性；与反传为不同训练路线 |
| DL45 | 诺奖官方公告：后见之明 | [Royal Swedish Academy of Sciences, Nobel Prize in Physics 2024 press release (2024-10-08)](https://www.nobelprize.org/prizes/physics/2024/press-release/) | 回顾Hopfield、Hinton的贡献；不是1980年代共同体当时评价 |
| DL46 | 研究者晚近讲座性回顾 | [Hinton, Nobel Lecture: Boltzmann machines, Rev Mod Phys 97 030502 (2025)](https://doi.org/10.1103/RevModPhys.97.030502) | 指出玻尔兹曼机与反传为1980年代两种不同的梯度学习技术，回顾观点标注作者 |
| DL47 | 原始论文期刊页面 | [Rumelhart, Hinton & Williams, Learning representations by back-propagating errors, Nature 323:533–536, 1986-10-09](https://www.nature.com/articles/323533a0) | 确证论文年份、作者、核心目的：优化输出差异并使隐藏单元形成特征 |
| DL48 | 1985研究者一手会议文本摘要 | [Yann LeCun, A Learning Scheme for Assymetric Threshold Network, Cognitiva 85 (Paris, 1985)](https://yann.lecun.com/exdb/publis/pdf/lecun-85.pdf) | 1985已有隐藏层训练、非线性区分的研究探索；论文PDF视觉截图失败，只按公开可读摘要核对，不称等同标准1986反传 |
| DL49 | 认知科学回顾性研究 | [Parallel Distributed Processing at 25: Further Explorations in the Microstructure of Cognition, Cognitive Science (2014)](https://onlinelibrary.wiley.com/doi/10.1111/cogs.12148) | 1986 PDP研究共同体的多领域背景；后世评价不同于原始实验 |
| DL50 | 2025 PNAS学术人物史 | [Profile of John Hopfield and Geoffrey Hinton: 2024 Nobel laureates in Physics, PNAS (2025)](https://doi.org/10.1073/pnas.2423094122) | 关于1986研究形成过程为后世学术回顾；强调当时多个研究路线并行 |

### 源流与因果核查

- **07章：数字微分—训练求梯度—可实现的算力三个条件并行**。芬兰Linnainmaa1970学位论文与1976论文研究的是数值误差灵敏度及反向累积，不是当场训练多层神经网络；Werbos1974论文及1980年代Parker等研究说明应用与传播有各自历史。不能写成一条已经证实的师生传承链；逆向累积算导数与梯度下降优化是相邻而不同的步骤。1978 Ivakhnenko 的GMDH在统计模型选择上提供平行思路，但不等同今天基于反传训练的深度网络。1971 Intel 4004历史有博物馆可证，却不能证明早期微处理器使深网训练现实可行。
- **08章：日本视觉层级—物理学联想记忆—随机生成学习**。1979福岛邦彦IJCAI已有neocognitron会议稿，1980 *Biological Cybernetics*的S/C层次与无教师自组织有原摘要；Hopfield1982强调内容寻址、模式恢复；Ackley/Hinton/Sejnowski 1985玻尔兹曼机强调随机状态和学习连接。模型结构、数据输入和训练目的三者都不同。不以2024诺奖“回头看”的认可代替1980年代成果的实际证据。
- **09章：多层隐藏单位的信用分配问题**。1986 *Nature*论文（1986-10-09）明确以输出和期望差距为训练目标，强调隐藏单元学到任务特征；早期Werbos、Linnainmaa、LeCun等工作应在贡献维度上各自定位，不宣称1986首次发明一般链式求导/逆向微分/所有神经学习。需区分可微链式法则、逆向自动微分、反向传播计算梯度、优化器更新权重、成功泛化五层。

### 现代教学例题，非历史实验记录

1. **07章共享中间量**：u=a×b+c，L=u²。a=2,b=3,c=1时u=7,L=49，逆向得∂L/∂u=14、∂L/∂a=42、∂L/∂b=28、∂L/∂c=14。适合说明一次逆向遍历复用中间量，不证明任何1970年代论文做过同样训练。
2. **08章联想记忆**：三元±1模式p=(+1,+1,-1)，用现代教学式w_ij=p_i p_j (i≠j)，若输入q=(+1,+1,+1)，同步与异步更新必须区分；取**异步只更新第3单元**：h_3=w_31 q_1+w_32 q_2=-2 → q_3从+1到-1，其余保持。该构造展示受约束的内容寻址，不代表系统无条件恢复任意噪声。
3. **09章两层标量网络**：x=1,w=1,v=1,t=1，h=σ(wx)≈0.731059，y=σ(vh)≈0.675038，L=½(y-t)²≈0.052800。反传∂L/∂v≈−0.052113，∂L/∂w≈−0.014015；学习率0.1同时更新后L≈0.052510。教学计算须独立复算，只有在此例的条件下才展示损失下降。

### 未解决的完整史学审读项

- 1970芬兰学位论文与1974 Werbos学位论文的逐页技术原文尚未全部调阅；不虚构引用/文献传播关系。
- 1985 LeCun会议论文PDF截图尝试遇服务器错误，公开文字摘要可定位，但不能引述图号或未观察到的页码。
- Hopfield模型的稳定性需要对称权重、无自连接、合适更新约定等前提；不要把任意异步/同步操作都说成能量单调下降。
- 1986 *Nature*原文摘要可核，本文不自行声称复现实验结果或优先权争议已有定论。


## 八、第四批10—12章｜卷积识别、LSTM时序学习、SVM统计竞争：前置资料核验（2026-11-09）

> **限定研究许可**：本次仅对第10—12章的论文作者、年代、核心模型机制、可复核教学计算和结论边界作前置核证。下列“来源元数据/摘要已核”不代表原论文全部页码及实验表格独立复现。尤其1998论文对商业支票处理量在摘要与导言有不同口径：本稿只说明论文报告已有商业部署，不复述精确日/月数量。1958感知机、1980福岛等前史沿用前批来源，不制造单人首创传奇。

| ID | 来源类别 | 原始出处及入口 | 可信支持范围／不可越界之处 |
| --- | --- | --- | --- |
| DL51 | 原始研究/出版社论文元数据 | LeCun, Boser, Denker, Henderson, Howard, Hubbard & Jackel (1989), [Backpropagation Applied to Handwritten Zip Code Recognition](https://doi.org/10.1162/neco.1989.1.4.541), Neural Computation 1(4), 541–551 | 研究以任务结构约束提升泛化，用单个训练网络从标准化字形图像直接分类美国邮政编码手写数字；非1998才首次研究 |
| DL52 | 原始研究/IEEE出版方官方摘要 | LeCun, Bottou, Bengio & Haffner (1998), [Gradient-Based Learning Applied to Document Recognition](https://proceedingsoftheieee.ieee.org/gradient-based-learning-applied-to-document-recognition/), Proceedings of the IEEE 86(11), 2278–2324; DOI 10.1109/5.726791 | CNN局部连接、共享权重、下采样、LeNet-5；文档管线含定位、切分、识别与语言模型；GTN全局训练；论文报告商业支票识别部署、特定标准数据集上的方法比较 |
| DL53 | 论文作者书目索引 | [Léon Bottou个人论文目录：LeCun等1998](https://leon.bottou.org/papers/lecun-98h) | 核作者、期刊、卷号、页码、年份；不提供新实验数据 |
| DL54 | 先驱原始论文（已有跨章来源） | Fukushima (1980), [Neocognitron](https://pubmed.ncbi.nlm.nih.gov/7370364/)（即前批DL41） | S/C层次与位置变化耐受；不把1980无监督新认知机等同1998可反传训练的CNN |
| DL55 | 原始论文/MIT Press与PubMed | Hochreiter & Schmidhuber (1997), [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735), Neural Computation 9(8):1735–1780, 1997-11-15 | 针对长距离时间依赖的衰减误差反流；constant error carousel与输入/输出门；原论文部分人工任务间隔超过1000时间步；非无条件“永久记忆” |
| DL56 | 原始论文/IEEE与PubMed | Bengio, Simard & Frasconi (1994), [Learning Long-Term Dependencies with Gradient Descent Is Difficult](https://doi.org/10.1109/72.279181), IEEE Transactions on Neural Networks 5(2):157–166 | 长依赖、梯度优化与稳定保存信息之间的困难；并不证明任意RNN无法存储长时信息 |
| DL57 | 原始论文/MIT Press与PubMed | Gers, Schmidhuber & Cummins (2000), [Learning to Forget: Continual Prediction with LSTM](https://doi.org/10.1162/089976600300015015), Neural Computation 12(10):2451–2471 | 为持续输入流中的自动重置引入**遗忘门（forget gate）**；不得把后来的完整三门公式直接归属于1997原始版本 |
| DL58 | 原始论文/ACM会议书目 | Boser, Guyon & Vapnik (1992), [A Training Algorithm for Optimal Margin Classifiers](https://mlanthology.org/colt/1992/boser1992colt-training/), COLT pp.144–152 | 最大间隔、由关键训练样本支撑的边界、OCR比较；不是1995才首次提出所有相关思想 |
| DL59 | 原始论文/Springer出版方 | Cortes & Vapnik (1995), [Support-Vector Networks](https://doi.org/10.1007/BF00994018), Machine Learning 20:273–297 | 把先前可分情形扩展到不可完美分隔的训练数据；非线性映射后线性边界；特定基准验证泛化表现，非对任何数据保证 |
| DL60 | 同时代学术综述/原刊论文 | Burges (1998), [A Tutorial on Support Vector Machines for Pattern Recognition](https://doi.org/10.1023/A:1009715923555), Data Mining and Knowledge Discovery 2:121–167 | 软间隔、核函数、最大间隔、何时优化有全局解；作者也提醒通用泛化并非无条件保证 |
| DL61 | 工程优化原始技术报告 | John Platt (1998), [Sequential Minimal Optimization: A Fast Algorithm for Training SVMs](https://www.microsoft.com/en-us/research/publication/sequential-minimal-optimization-a-fast-algorithm-for-training-support-vector-machines/), Microsoft Research MSR-TR-98-14 | SVM训练涉及二次规划，有效率与内存瓶颈；SMO将QP拆成可解析处理的小块，证明“凸目标≠零工程成本” |
| DL62 | 数据来源/机构数据库说明 | [MNIST handwritten-digit data, Microsoft Learn](https://learn.microsoft.com/en-us/azure/open-datasets/dataset-mnist) | 标准的训练集60,000与测试集10,000；数据经尺寸归一和居中，不能当任意自然图像数据 |
| DL63 | 后世对原论文分类与机制的复核 | [LeCun等1998论文的HTML学术转录／文本核对入口](https://tamnd.github.io/papers-reader/p/lecun-1998-lenet/en/) | 可检索作者对卷积网络的局部连接、权重共享、下采样的叙述，以及实验比较的具体上下文；应优先以IEEE原刊为证据，不把转录视作独立实验 |

### 本批必须守住的三层历史分界

**第10章：1989的邮政编码研究≠1998的LeNet-5与银行支票系统。** 1989 *Neural Computation*说明通过架构内的任务约束帮助泛化；1998 *Proceedings of the IEEE*是团队对文档识别和端到端/多模块训练的集中总结。LeNet-5的卷积、局部感受野、共享权重及下采样一起服务于二维图案变化，但“局部共享”首先带来平移**等变**，只有后续聚合/下采样与相应处理才得到一定**不变性/容忍度**，而非对任意变形完全不变。论文关于“数百万支票/日或月”存在摘要与正文口径差异，不在正文给无条件精确数。

**第11章：1994理论困境、1997 LSTM、2000遗忘门是三个历史节点。** 1997论文提出常量误差旋转单元与乘性门控以改善长间隔任务；2000年才出现针对连续流自动清理状态的遗忘门。今天常用简化递推 c_t=f_t c_(t-1)+i_t g_t 属于含遗忘门版本的**现代教学重构**，不可写成“1997原论文已有完整三门标准式”；在f_t趋近1时梯度路径可较稳，长期依赖却仍受门控学习、容量与数据制约。

**第12章：SVM并非被简单感知机打败后才横空出现的替代品。** 1992最大间隔研究与1995对不可分情形的扩展早于1998 LeNet-5综述。神经网络在若干OCR任务有竞争力且存在商用部署；SVM在另外一些基准与样本条件下具有工程吸引力。1998 IEEE论文称CNN优于其**论文比较的那组方法/条件**，不能外推“所有时期所有数据都赢SVM”；同理不能说SVM普遍胜过CNN。最大间隔是明确的几何与优化选择，并非数学上保证未知数据永不误判。

### 本批教学推导与非史实声明

1. 卷积局部权重复用：设五位序列x=[0,0,1,1,0]、核k=[-1,1]，采用ML常见互相关式局部打分，四处输出[0,1,0,-1]；平移成x'=[0,0,0,1,1]后得到[0,0,1,0]，位置改变但max局部响应仍为1。**仅为一维说明原理**，不能等同真实手写字体模型或1989论文实验。
2. 衰减：若普通循环计算链局部导数乘积系数为0.8，跨20步影响为0.8^20≈0.0115292；现代带遗忘门示意在f=0.9保持20步为0.9^20≈0.121577，而f=1无该特定衰减。**这是受限乘法链例题**，不等于所有LSTM梯度或记忆衰减指数。
3. SVM最大间隔：一维训练样本(x=-2,y=-1),(x=+2,y=+1)，选w=0.5,b=0满足y(wx+b)=1，决策边界x=0，距最近点2。两个样本就是简化例子的支持向量；此结论依赖点和硬间隔设定。
4. 核思想与XOR：对0/1输入先构造φ=(x1,x2,x1*x2)，线性评分s=x1+x2−2x1x2−0.5便满足XOR。它是**显式非线性映射教学例**，不冒充1995原论文使用这四个点或证明某个核超参数适合所有数据。

### 独立审稿未决问题

- 核验1998原文中“每日/每月票据处理量”的上下文差别；当前不以精确数字做认知抓手。
- 查明LeNet变体及1998论文表格中实验集、预处理、训练设置，正式书稿如要报模型误差须连同测评条件与原始表格，不从摘要推导性能优势。
- 核查1997原文与2000版本在输入、输出、遗忘门以及后续peephole连接上的差异；本稿不归属未覆盖的后续变种。
- SVM核优化与神经网络优化的“全局/局部”表述必须以条件、目标及模型非凸性为前提；训练数据质量和泛化风险不可由一种算法名称推出。


## 九、第五批13—15章｜从可共享的词表示到深层初始化、声学模型（2026-11-09）

> **仅针对本批的前置核验**：第13—15章写作之前核对原始发表年份、作者团队、算法机制、可复算例题及哪些结论属于特定实验。2003 JMLR原始论文、2006深度信念网络论文与2011 Interspeech论文已打开并查看PDF首页；本节不假称整篇所有数据表格均已独立审计。来自回顾性论文的历史评价，应与其描述的当年实验分开。以前各批的PENDING审稿状态不因本次追加事实研究而改变。

| source_id | 原始日期与证据属性 | 可核入口 | 直接支持范围与警戒线 |
| --- | --- | --- | --- |
| DL64 | 2000会议版本，一手书目 | Bengio, Ducharme & Vincent, [A Neural Probabilistic Language Model](https://proceedings.neurips.cc/paper_files/paper/2000/hash/728f206c2a01bf572b5940d7d9a8fa4c-Abstract.html), NIPS 2000 | 该研究2000年已有三人署名的会议论文；**2003不是同名思想的首次出现**；会议归年与论文集出版年份不能任意混同 |
| DL65 | 2003-02期刊正式版本；PDF首页已核 | Bengio, Ducharme, Vincent & Jauvin, [A Neural Probabilistic Language Model](https://jmlr.org/papers/v3/bengio03a.html), JMLR 3:1137–1155 | 四人作者、词分布式连续向量与条件概率共同训练；两组文本语料优于论文选定的n-gram比较条件，不能泛化所有语言任务 |
| DL66 | 2003另一原始研究 | Bengio & Senécal, [Quick Training of Probabilistic Neural Nets by Importance Sampling](https://proceedings.mlr.press/r4/bengio03a.html), AISTATS 2003 | 词表softmax训练计算量（每条样本需考虑所有候选词），重要性采样加速探索；不将后来的negative sampling倒灌为2003标准方案 |
| DL67 | 2013原始预印本 | Mikolov, Chen, Corrado & Dean, [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781), 2013-01 | word2vec相关结构是后来的工作；不得把2003 Bengio模型称作“2013 word2vec”或2017 Transformer |
| DL68 | 2006-07同行评审原始论文；作者公开PDF首页已核 | Hinton, Osindero & Teh, [A Fast Learning Algorithm for Deep Belief Nets](https://pubmed.ncbi.nlm.nih.gov/16764513/), Neural Computation 18(7):1527–1554；[作者版PDF](https://www.stats.ox.ac.uk/~teh/research/unsup/nc2006.pdf) | DBN逐层贪心无监督训练，上两层无向关联记忆、下层定向生成连接；原论文生成模型进一步用对比式wake-sleep微调，**不可称所有阶段均为监督反向传播** |
| DL69 | 2002一手论文 | Hinton, [Training Products of Experts by Minimizing Contrastive Divergence](https://pubmed.ncbi.nlm.nih.gov/12180402/), Neural Computation 14(8):1771–1800 | 对比散度作为概率模型训练方法；CD是近似学习工具，不等于对任何RBM都精确求出全似然梯度 |
| DL70 | 2006-07-28 Science原始论文 | Hinton & Salakhutdinov, [Reducing the Dimensionality of Data with Neural Networks](https://pubmed.ncbi.nlm.nih.gov/16873662/), Science 313:504–507 | 用较好预训练初始化深层自编码器，再以梯度下降做重构微调；**与Hinton等2006 DBN原论文的生成式微调要分清** |
| DL71 | 2006 NeurIPS会议研究（论文集也常标2007） | Bengio, Lamblin, Popovici & Larochelle, [Greedy Layer-Wise Training of Deep Networks](https://papers.nips.cc/paper/2006/hash/5da713a690c067105aeb2fae32403405-Abstract.html) | 蒙特利尔团队在2006会议节点探索分层无监督训练、与监督微调的其他安排；不把成果归功于单一多伦多团队 |
| DL72 | 2009后续学术研究 | Larochelle, Bengio, Louradour & Lamblin, [Exploring Strategies for Training Deep Neural Networks](https://jmlr.org/papers/v10/larochelle09a.html), JMLR 10:1–40 | 比较预训练优化、正则化作用与变体；这是后世机制研究，不能冒充2006研究者已知道所有结论 |
| DL73 | 2011-08语音领域原始会议论文；PDF首页已核 | Seide, Gang Li & Dong Yu, [Conversational Speech Transcription Using Context-Dependent Deep Neural Networks](https://www.isca-archive.org/interspeech_2011/seide11_interspeech.html), Interspeech 2011 pp.437–440 | 机构署名：北京Microsoft Research Asia和雷德蒙德Microsoft Research；RT03S Fisher测试单遍无说话人适配场景，GMM-HMM词错误率27.4%→CD-DNN-HMM 18.5%，绝对降8.9百分点，相对降约32.5%；**只限论文同条件** |
| DL74 | 2012-01原始IEEE期刊论文 | Dahl, Dong Yu, Li Deng & Acero, [Context-Dependent Pre-Trained Deep Neural Networks for Large-Vocabulary Speech Recognition](https://www.microsoft.com/en-us/research/publication/context-dependent-pre-trained-deep-neural-networks-for-large-vocabulary-speech-recognition/), IEEE Trans. Audio Speech Lang. Process. 20(1):30–42 | CD-DNN-HMM以DNN输出绑定三音素状态的后验概率，借已有HMM解码大词汇语音；特定商务搜索语音基准胜于给定GMM-HMM参照 |
| DL75 | 2012-11四组团队综合评述（当事作者） | Hinton, Li Deng, Dong Yu et al., [Deep Neural Networks for Acoustic Modeling in Speech Recognition: The Shared Views of Four Research Groups](https://www.microsoft.com/en-us/research/publication/deep-neural-networks-for-acoustic-modeling-in-speech-recognition/), IEEE Signal Processing Magazine 29(6):82–97 | 四组来自多伦多、微软研究院、Google、IBM；2009—2012不同工作线整合成果，**HMM通常仍负责时序解码**，DNN多为声学模型，不等于当时端到端语音大模型 |
| DL76 | 2011另一原始会议论文 | Seide, Gang Li, Xie Chen & Dong Yu, [Feature Engineering in Context-Dependent Deep Neural Networks for Conversational Speech Transcription](https://www.microsoft.com/en-us/research/publication/feature-engineering-in-context-dependent-deep-neural-networks-for-conversational-speech-transcription/), ASRU 2011 | 中国北京机构研究参与者及声学特征工程与适配任务；不得按作者拼写直接推断个人国籍或把团队贡献合并为单一天才故事 |

### 13章史实决议：不是“2003才发明词向量”

- 同名三人会议论文在**2000年**；四人JMLR版发表于**2003年2月**，第4位作者Christian Jauvin不可漏写。原论文的问题是语言序列条件概率的高维稀疏：词序列数目随词表大小和上下文长度组合增长，n-gram平滑有重要历史成绩，但难以只靠精确组合覆盖所有未见文本。
- 同时学习词的连续分布式表示及预测下一词的概率，把不同文本语境之间的统计线索通过共享参数联系起来。**“未出现过的词序列”≠“词表里根本没这个新词”**；OOV、长距依赖和softmax计算成本仍是问题。论文对两组语料的表现不能直接推出开放式长文本理解。
- **教学例题**：人工设3个候选下一词得分[2,1,0]，softmax概率约[0.665241,0.244728,0.090031]，三值和为1；只演示“连续得分如何变成候选概率”，不是2003真实实验或保证语义类比。若词表1万且连续四个词，理论不同组合数可达10^16，不等于实际模型必须完整存这么大参数表。

### 14章史实决议：区分2006 DBN、深层自编码器与后来的监督微调

- 2002 Hinton的CD论文提供训练概率模型的近似工具，2006 Hinton/Osindero/Teh采用逐层无监督训练构建**混合有向/无向的生成式DBN**，其原始文献采用对比式wake-sleep作生成微调；另一篇2006 *Science*论文将较好初始化与**深层自编码器反向传播微调**结合。这不是2006“发明反传”，也不是“原始DBN等于任意多层分类器”。
- 2006 NeurIPS Bengio等团队及2009研究继续比较逐层预训练与深度优化，并非单个团队一项论文独占所有方法；预训练缓解了当时某些深网络的初始化与优化困境，但没有证明所有深度、任务、硬件都因此可训练。
- **教学例题**：玩具RBM仅一可见单元v与一隐藏单元h，取隐偏置0、权重w=ln3，现代标准条件概率P(h=1|v)=σ(wv)；v=0时0.5、v=1时0.75。只是演示“隐藏特征如何根据观察随机激活”，不是2006论文的MNIST训练数据或实际CD采样链。

### 15章史实决议：声学模型突破，而非一次性替换全部语音系统

- 2000年代末—2012年的相关成果是研究团队与工业系统协同迭代。经典GMM-HMM系统中HMM处理声学状态时间变化，GMM评估短帧与状态的吻合；CD-DNN-HMM以深网络估计绑定三音素声学状态的后验概率，并经适当转换/解码与HMM等组件结合。
- 2011 Seide、Gang Li、Dong Yu的Interspeech论文第一作者与第二作者的机构地点为**北京**，第三作者的机构地点为**美国雷德蒙德**，可证明跨地点合作，**不能由地点推断每个人国籍**。2012四组综述表明并非只有一家公司推动；2012 Dahl等原始期刊论文强调上下文相关声学建模与预训练。不要把所有2012工业成果写成2006 DBN“必然导致”的单一链条。
- **具体基准**：2011 Interspeech论文在RT03S Fisher子集、单遍、说话人无关条件下将词错误率27.4%降至18.5%，相差8.9百分点；以27.4%为基数相对下降≈32.5%。**不允许省略测试条件并声称所有语音识别任务一律下降33%**。
- **教学例题**：四个空格分隔英文词 reference “we need more data”，hypothesis “we need new data”，编辑距离替换1个，WER=(S+D+I)/N=1/4=25%。是自造教学，不是2011实验原句。若中文按字计数应称字错误率CER，不可和WER混用。

### 独立审稿尚未完成

1. 2000 NIPS会议原始完整PDF与2003 JMLR模型结构及正式出版年代需要按页码再次核对；本轮首屏/元数据核验足以支持概述而非全文逐行引用。
2. DBN2006的有向/无向分层和生成微调与2006 Science的自编码器梯度微调必须分别审。对比散度的精确目标及计算代价仍需算法专审。
3. 2011语音论文的模型规模（训练小时数/状态数/层数）可以按其论文范围引用，但不同基准或统计口径不可直接横比；如使用27.4与18.5必须注明单遍、说话人无关、RT03S Fisher数据条件。
4. 不得虚构中国学者国籍、现场对话或实验日志；应以原论文中北京/雷德蒙德机构署名和原始作者列为准。
5. 本轮所有章节仍为工作初稿研究范围；独立连续性审计和结构审稿没有PASS，最终版本未批准。

## 十、第六批16—18章：ImageNet—AlexNet—ResNet限定史料核查（2026-11-10）

> **本批仅核定16—18章中心史实、模型架构、可复算示例、指标口径与史学因果约束**。原始PDF已查看ImageNet 2009、AlexNet 2012（官方NIPS PDF首页及结果表）、ResNet 2016（CVPR首页及残差机制）。尚非三章全文每句的独立审稿，不授权16—18以外的任何章节，也不变更此前01—15的PENDING状态。

| ID | 证据属性 | 原始文献 | 可支撑范围与必须警惕的细节 |
| --- | --- | --- | --- |
| DL77 | CVPR 2009 原始论文（ImageNet官网PDF已逐页目视核首页） | [Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, Li Fei-Fei; ImageNet: A Large-Scale Hierarchical Image Database](https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf) | 论文发布时12个子树、5247 synsets、320万图片；WordNet层级、众包标注；这不是2012竞赛的1000类子集 |
| DL78 | CVPR 2009正式会议书目 | [ImageNet: A Large-Scale Hierarchical Image Database, IEEE CVPR 2009, pp.248–255](https://doi.org/10.1109/CVPR.2009.5206848) | 确认2009会议论文与作者、发布日期；不可把项目目标的数千万图片说成2009已实有 |
| DL79 | IJCV 2015竞赛研究史（arXiv 2014先行版） | [Russakovsky et al., ImageNet Large Scale Visual Recognition Challenge](https://arxiv.org/abs/1409.0575) | ILSVRC自2010起年赛；2010起1000类图像分类与检测等任务；训练/验证/测试、隐藏测试答案、公开标准；2015期刊总结回溯，不能冒称2010当年回顾 |
| DL80 | MIT存档及NIPS原始PDF，首页、结果表已目视核对 | [Krizhevsky, Sutskever & Hinton, ImageNet Classification with Deep Convolutional Neural Networks (2012)](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) | 2012 ILSVRC top-5 test 15.3%为七个CNN组合（五个相关模型+两个在更大ImageNet版本监督预训练的模型），第二名26.2%；2010数据单CNN test top1 37.5%、top5 17.0%不可与2012指标混同 |
| DL81 | NeurIPS 2012官网摘要网页，与同站正式PDF数值有差异 | [NIPS 2012 paper landing page: ImageNet Classification with Deep Convolutional Neural Networks](https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) | 网页摘要称1.3m与500k神经元/39.7%、18.9%；官方PDF首页则称1.2m、650k/37.5%、17.0%。本文统一以论文PDF+表格为口径并显式标记该矛盾 |
| DL82 | ICLR 2015正式论文／2014预印本 | [Simonyan & Zisserman, Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556) | VGG 16–19个含权重层，2014 ILSVRC比赛对应、2015 ICLR正式发表；证明深度价值但不保证无限堆叠 |
| DL83 | CVPR 2015正式论文，团队来自多机构 | [Szegedy et al., Going Deeper with Convolutions (Inception/GoogLeNet)](https://openaccess.thecvf.com/content_cvpr_2015/html/Szegedy_Going_Deeper_With_2015_CVPR_paper.html) | ILSVRC2014期间提出22层GoogLeNet、多尺度Inception模块，追求算力利用；不应由ResNet讲述中省去其他路线 |
| DL84 | ICML 2015原始论文 | [Ioffe & Szegedy, Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://proceedings.mlr.press/v37/ioffe15.html) | 批归一化缓解当时优化困难；2015作者机制说法不应绝对当作后世唯一解释 |
| DL85 | NIPS 2015原始论文 | [Srivastava, Greff & Schmidhuber, Training Very Deep Networks (Highway networks)](https://papers.nips.cc/paper_files/paper/2015/hash/215a71a12769b056c3c32e7299f1c5ed-Abstract.html) | 同年存在带可学习门控的捷径/信息高速公路网络；ResNet身份直连与Highway门控不同；不称跳连接2015首次诞生 |
| DL86 | ResNet原始预印本2015-12-10 | [He, Zhang, Ren & Sun, Deep Residual Learning for Image Recognition, arXiv:1512.03385](https://arxiv.org/abs/1512.03385) | 2015预印本与ILSVRC2015获奖事实，不能把2016正式发表日误当竞赛时间 |
| DL87 | CVPR 2016原始正式论文，PDF首页和机制章节已目视核对 | [He, Zhang, Ren & Sun, Deep Residual Learning for Image Recognition, CVPR2016 pp.770–778](https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html) | plain 20/56层在CIFAR-10训练退化（较深训练误差更高）；残差块y=F(x)+x，有维度改变时投影；152层网络、ILSVRC2015集成top5 test3.57%；不把退化等同过拟合 |
| DL88 | ECCV 2016后续机制研究 | [He, Zhang, Ren & Sun, Identity Mappings in Deep Residual Networks](https://mlanthology.org/eccv/2016/he2016eccv-identity/) | 探讨身份捷径和激活位置、pre-activation改进；属于2016后续，不可倒灌2015竞赛版本架构 |
| DL89 | 作者论文内实验示例来源 | [ImageNet 2012 NeurIPS原文：Section 4/5/6 （GPU/ReLU/dropout/数据增强/训练时间）](https://courses.csail.mit.edu/6.803/pdf/2012%20hinton.pdf) | 原文报告两块NVIDIA GTX580 3GB GPU训练5–6日及多种技术协作；不宣称GPU或ReLU由该团队第一次发明 |

### 技术与年代三重分界

1. **ImageNet数据库 ≠ ILSVRC竞赛 ≠ 某次竞赛的训练集。** CVPR2009论文报告项目当时320万图、5247个WordNet同义词集合（synsets），竞赛自2010起，是从更大数据库组织出的分任务评测。不能将“ImageNet有320万图”当作“2012模型训练了320万图”，也不能把ImageNet等同猫狗二分类或1000类别的全部含义。2009论文报告子集标注抽查准确率，不是无限定的每张图100%真实标签。
2. **2012成绩的三种口径**：NIPS官方PDF给ILSVRC-2010单模型top1=37.5%、top5=17.0%；ILSVRC-2012竞赛top5测试=15.3% **七CNN集成**（含在Fall2011 ImageNet版本做大类别**监督训练**的模型），第二名26.2%，下降10.9个百分点、相对下降约41.6%。NeurIPS官网网页摘要和同站正式PDF存在指标版本差异（详见DL81），本批依据直接核验的PDF表2，**不把15.3%称单个网络性能**。
3. **2015竞赛 ≠ 2016正式发表**：He等ResNet 2015-12-10 arXiv预印本、ILSVRC2015获奖，CVPR2016正式论文。152层指模型层数；3.57%是 **网络集成**的ILSVRC2015 classification top-5测试错误率。CIFAR-10 plain 56比plain 20层的训练误差更高属于**优化退化**，不是简单过拟合或单凭梯度消失解释。跳连接历史另有Highway2015等相关研究，不能宣称He团队首次想到跨层信息路径。

### 三个教学示例及边界

- **16章Top-k**：人造四张图正确类别排名[1,3,6,4]，top-1错误3/4=75%，top-5错误1/4=25%；只描述给定排序的排行榜指标，不是官方2012比赛统计、也不证明模型理解语义。多数ILSVRC分类基准可采用top-5，须注明不同任务如检测的指标不同。
- **17章ReLU+dropout**：ReLU(-2)=0, ReLU(3)=3；假设inverted dropout保留率p=1/2，原激活为4，训练一次变为0或8，期望值仍为4。该公式为现代实现教学化版本，dropout是训练过程的随机正则化，不等于预测时每个单元必随机开关。2012 paper 15.3 vs 26.2，相对差10.9/26.2≈41.6%。
- **18章残差块**：设F(x)=-0.1x且x=2，普通映射F(x)=-0.2，导数-0.1；残差映射y=x+F(x)=1.8，导数1-0.1=0.9；五个完全相同的小模型线性块，普通导数(-0.1)^5=-0.00001、残差导数0.9^5=0.59049。只说明身份路径如何影响数学梯度，并不证明真实ResNet无梯度消失或实际网络有这组固定参数。若F'(x)≈-1则身份项亦可能被抵消。

### 独立审稿必查

- 2009 ImageNet志向数千万图、当时320万、后续ImageNet Fall 2011规模、ILSVRC2012训练约120万与1000类别的差异；与WordNet分类层级和AMT劳务关系不得虚构。
- 2012 NIPS网页摘要与正式PDF不同，所有具体数字须标注本批选择的版本；15.3%七CNN集成与单CNN验证18.2%和2010单CNN test17.0%均不能混为一谈。
- 2015 ILSVRC竞赛与2016 CVPR论文时间坐标，3.57%为集成；ResNet 2016 ECCV的pre-activation改善非2015原始结果。
- 残差连接作用不能写成对梯度消失绝对免疫；其论文直接的训练退化证据比媒体口号重要。Highway网络/批归一化/VGG/Inception均为当时重要相邻研究路线。

## 十一、第七批19—21章：seq2seq、注意力、GAN—扩散生成有限核证（2026-11-10）

> **章节顺序以本仓库原有策划为准**：19是词向量到变长编码器—解码器；20是2014预印本/2015发表的神经机器翻译注意力；**21是GAN至潜空间扩散的图像生成发展**；Transformer是第22章，不提前擅改标题。现阶段仅核主张所需原论文元数据、公开摘要、机制与现代数学教学例题；不是逐页全文独立科学史审稿。

| ID | 证据性质 | 论文与年份 | 支持范围/警戒 |
| --- | --- | --- | --- |
| DL90 | 原始会议论文/ACL Anthology | [Cho, van Merriënboer, Gulcehre, Bahdanau, Bougares, Schwenk & Bengio (EMNLP 2014), Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation](https://aclanthology.org/D14-1179/) | 2014-10七作者：变长源短语→固定长度编码→变长目标短语，条件概率用作传统phrase-based SMT重排/特征，不能冒称该篇整体替换全部SMT系统 |
| DL91 | 原始会议论文/NeurIPS | [Sutskever, Vinyals & Le (NIPS 2014), Sequence to Sequence Learning with Neural Networks](https://proceedings.neurips.cc/paper_files/paper/2014/hash/5a18e133cbf9f257297f410bb7eca942-Abstract.html) | 2014 WMT14英法任务LSTM BLEU 34.8，与论文所述phrase-based SMT 33.3同条件；对1000候选重排后得36.5是另一个任务配置；论文观察反转源词顺序利于优化，不能写成意义翻译的必备规则 |
| DL92 | 原始预印本/日期 | [Sutskever, Vinyals & Le, Sequence to Sequence Learning, arXiv:1409.3215](https://arxiv.org/abs/1409.3215) | 2014-09-10预印本日期，别把2014论文写成2015发明 |
| DL93 | 原始预印本/期刊会议年份对照 | [Bahdanau, Cho & Bengio, Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) | 2014-09-01初稿，后来ICLR2015；提出固定长向量可能是瓶颈、解码时依据输出状态为源位置生成软对齐注意力，不能说2014已经有Transformer |
| DL94 | 正式会议书目/出版信息 | [Bahdanau, Cho & Bengio, Neural Machine Translation by Jointly Learning to Align and Translate, ICLR2015](https://apice.unibo.it/bin/view/Publication/AttentionmechanismIclr2015?language=en) | 2015会议发表与2014预印本区别；该研究为神经机器翻译重要attention路线，但不是注意力作为一般心理或计算概念首创 |
| DL95 | ACL正式论文 | [Luong, Pham & Manning (EMNLP 2015), Effective Approaches to Attention-based Neural Machine Translation](https://aclanthology.org/D15-1166/) | 在2014/15软对齐之后研究global/local attention；论文提供特定WMT英德提升，不能将不同任务BLEU直接比较 |
| DL96 | 已核2017原始论文门户/下一批边界 | [Vaswani et al., Attention Is All You Need, NeurIPS2017](https://research.google/pubs/attention-is-all-you-need/) | 2017 Transformer以注意力为主的非循环架构，是**第22章**，本批第20章只作年代对照与下一部悬念，不提前写成已完成第21章 |
| DL97 | 原始GAN论文/NeurIPS | [Goodfellow, Pouget-Abadie, Mirza, Xu, Warde-Farley, Ozair, Courville & Bengio, Generative Adversarial Nets (2014)](https://proceedings.neurips.cc/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html) | 原始八作者、生成器G与判别器D的对抗式极小极大训练；理想分布匹配时D(x)=0.5是非参数理论极限，不是实际训练保证 |
| DL98 | 原始预印本（VAE与生成另一条线） | [Kingma & Welling, Auto-Encoding Variational Bayes, first arXiv submission 2013-12-20, ICLR2014](https://arxiv.org/abs/1312.6114) | 随机潜变量、变分下界及重参数化；不能把VAE说成GAN的一个判别器，或2014之后GAN的直接后代 |
| DL99 | ICML2014另一组生成建模先驱 | [Rezende, Mohamed & Wierstra, Stochastic Backpropagation and Approximate Inference in Deep Generative Models](https://proceedings.mlr.press/v32/rezende14.html) | 随机潜变量与近似后验的独立研究路线；不能把所有随机生成都归为GAN |
| DL100 | ICML2015原始扩散模型论文 | [Sohl-Dickstein, Weiss, Maheswaranathan & Ganguli, Deep Unsupervised Learning using Nonequilibrium Thermodynamics](https://proceedings.mlr.press/v37/sohl-dickstein15.html) | 前向渐进破坏数据结构及学习逆向恢复；最早现代扩散重要路线并非2020才突然出现 |
| DL101 | NeurIPS2019得分模型相邻路线 | [Song & Ermon, Generative Modeling by Estimating Gradients of the Data Distribution](https://proceedings.neurips.cc/paper/2019/hash/3001ef257407d5a371a96dcd947c7d93-Abstract.html) | 以多噪声尺度估计数据分布score、模拟Langevin生成，历史上与扩散在后续工作有交汇，但不能误当GAN鉴别器 |
| DL102 | NeurIPS2020原始DDPM论文 | [Ho, Jain & Abbeel, Denoising Diffusion Probabilistic Models](https://proceedings.neurips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html) | 按噪声过程训练去噪概率模型，高质量图像采样；论文无条件CIFAR10 FID3.17须有基准条件，不必在正文作跨年代排行榜 |
| DL103 | CVPR2022原始LDM论文 | [Rombach, Blattmann, Lorenz, Esser & Ommer, High-Resolution Image Synthesis With Latent Diffusion Models](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html) | 先借自编码器压缩到潜空间再作扩散/去噪，降低高分辨率像素域成本，支持cross-attention文本等条件；潜空间有损压缩/速度仍非零成本 |
| DL104 | 研究团队正式页面及术语口径 | [CompVis / Rombach et al., High-Resolution Image Synthesis with Latent Diffusion Models](https://ommer-lab.com/research/latent-diffusion-models/) | 论文团队对应的LDM/Stable Diffusion相关命名；不可拿品牌推出整条扩散研究只有一个公司或某个单人首创 |
| DL105 | 2013词向量原始先驱（前章跨引） | [Mikolov, Chen, Corrado & Dean, Efficient Estimation of Word Representations in Vector Space (2013)](https://arxiv.org/abs/1301.3781) | 2013连续词向量与第13章2000/2003神经概率语言模型先驱有关但不是同一方法；向seq2seq延展需另外学习语序 |
| DL106 | 人工指标不等于意思完整性的限制 | [Papineni, Roukos, Ward & Zhu (ACL 2002), BLEU: a Method for Automatic Evaluation of Machine Translation](https://aclanthology.org/P02-1040/) | BLEU基于对参考译文的n-gram匹配与长度惩罚，是语料级指标；34.8与33.3为分数点差，不是准确率百分比 |

### 第19章边界与现代教学推导

**词向量≠整个句子翻译**。2013的word2vec为分布式词向量研究中的后来节点；2014 Cho等EMNLP七作者编码器—解码器把变长序列压成固定维度向量，实验中作为原有SMT短语对概率特征；2014 NIPS Sutskever/Vinyals/Le三作者深LSTM给出端到端序列映射与WMT14英法34.8 BLEU，所述短语统计系统33.3，重排1000候选后的36.5是**另一个设置**。2014文章对长句的正面实验和第20章作者提出的潜在瓶颈并不构成无条件矛盾：不同模型、上下文、数据与优化条件。

教学例子：五个源token [A,B,C,D,EOS]，两个输出token [X,EOS]，以P(X|c)=0.8与P(EOS|X,c)=0.5人为指定，联合条件概率0.8×0.5=0.4；这演示变长条件生成的链式分解，**不是论文真实的WMT译文或结果**。词向量距离是否相近不能证明“真实理解”。BLEU是语料级近似匹配评估，不等于句子正确率。

### 第20章边界与现代数学例子

Bahdanau/Cho/Bengio论文**2014-09-01预印本→ICLR2015**；提出解码每个目标token时根据当前解码状态与源端隐状态产生“软对齐”权重，而不是整句都使用相同单一信息瓶颈。2015 Luong/Pham/Manning比较global与local不同注意力设计；**2017 Transformer本身尚未写到**，更不是attention在2014首次进入一切AI领域。注意力热度不能说明热力图是完备因果解释。

教学例子：解码某词时对源3个位置打分[ln2,ln1,ln1]，softmax概率[0.5,0.25,0.25]；源3个标量特征[2,0,-2]，加权上下文0.5×2+0.25×0+0.25×(-2)=0.5。下一输出步权重可改变。源词位置的“注意”是可微权重，不自动证明语义正确对齐。

### 第21章边界与现代数学例子

2014 Goodfellow等八作者GAN**对抗分布学习**，理想匹配时D(x)=1/2不意味着现实模型训练永不崩塌。VAE 2013年末预印本、2014 ICLR和Rezende等ICML是独立潜变量近似推断路线，不能写作GAN的后代。扩散从2015 Sohl-Dickstein等非平衡热力学出发，2019 Song/Ermon score路线，2020 Ho/Jain/Abbeel DDPM，2022 Rombach等潜空间扩散/文本条件，属于若干研究路线交汇，不是“2014 GAN逐代替换成diffusion”。

玩具GAN：若D(real)=0.8、D(G(z))=0.2，log value约ln0.8+ln(1-0.2)=2ln0.8≈-0.44629；若理想D均0.5，则2ln0.5≈-1.38629，仅说明固定两项的损失值，**不是训练收敛证据**。玩具扩散：x0=2，加一轮noise ε=-1，系数sqrt(alpha)=sqrt(0.75)、sqrt(1-alpha)=0.5，则x1≈1.23205；训练去噪可以估计原信号/噪声，但不能保证每一步真实图像唯一恢复。

### 独立审稿风险

- 2014两个seq2seq方向一个是phrase rescoring、一个是NIPS的end-to-end实验，术语相同但成果不能合并；34.8/33.3/36.5 BLEU均有任务和系统条件。
- 2014-09先公开Bahdanau注意力，2015 ICLR正式发表；没有2017 Transformer自注意力的完整计算架构。2015 Luong attention路线说明非独家单一发明。
- GAN2014与VAE2014、diffusion2015、score2019、DDPM2020、LDM2022方法目标、采样与评估差异不能化为“同一个生成模型”；本文并非跨所有生成质量基准定胜负。
- 用户要求非虚构知乎盐选风格，不准虚构研究者实验室对话、心理、图像截图或未提供的具体算法运行结果。所有演算标注现代作者例题。第01—18章独立审核继续PENDING。

## 十二、第八批22—24章：Transformer、双路线预训练、规模定律与GPT-3（2026-11-10）

> **限定范围前置核查**：已经核对2017 Transformer原始NeurIPS正式PDF首页/模型机制段，另用NeurIPS/ACL会议档案、机构原始论文与公告核对2018—2022关键论文时间、作者与摘要。依仓库阶段契约，此处不是独立审稿PASS，不表示所有论文的全部图表已复现。第22—24章之外的写作许可不扩大。

| ID | 证据类型 | 原始文献 | 可支持论断与禁止混淆 |
| --- | --- | --- | --- |
| DL107 | 2017 NeurIPS原始正式会议PDF，首屏已截图 | [Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser & Polosukhin, Attention Is All You Need](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf) | 八作者、6层编码/解码、QKV、scale/sqrt(d_k)、8-head、正余弦位置编码、残差/层归一化；PDF摘要28.4英德BLEU、41.0英法BLEU（不同摘要有版本差异）。 |
| DL108 | 2017 NeurIPS论文门户，版本差异证据 | [Attention is All you Need, NeurIPS 2017 abstract landing page](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html) | 网页摘要写27.5英德、41.1英法，**与同站PDF 28.4/41.0不一致**；正文只采用PDF版数字并主动说明。 |
| DL109 | 2017-06-12预印本，另一版本 | [Vaswani et al., arXiv:1706.03762 Attention Is All You Need](https://arxiv.org/abs/1706.03762) | 部分arXiv摘要写41.8英法，进一步证明存在版本数字问题；不混用。 |
| DL110 | 2018 NAACL原始会议 | [Peters, Neumann, Iyyer, Gardner, Clark, Lee & Zettlemoyer, Deep Contextualized Word Representations (ELMo)](https://aclanthology.org/N18-1202/) | 2018双向LSTM语言模型导出上下文词表示，多义词语境变化；**不是基于Transformer的BERT**。 |
| DL111 | 2018 ACL正式会议 | [Howard & Ruder, Universal Language Model Fine-tuning for Text Classification (ULMFiT)](https://aclanthology.org/P18-1031/) | 预训练/微调迁移路线2018已有LSTM系；原论文在6文本分类任务显示收益，不是Google或OpenAI独占思想。 |
| DL112 | 2018-06-11机构研究公告 | [OpenAI, Improving language understanding with unsupervised learning](https://openai.com/index/language-unsupervised/) | GPT早期方案将Transformer与生成式语言模型预训练、各任务有监督微调组合；公告的具体基准有时不如其他方法，不宣称全面第一。 |
| DL113 | 2018原始技术报告 | [Radford, Narasimhan, Salimans & Sutskever, Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | GPT(2018)四作者，因果左到右Transformer语言模型预训练后按具体任务微调；不等于GPT-3 few-shot无权重更新。 |
| DL114 | 2018-10-11首版预印本 | [Devlin, Chang, Lee & Toutanova, BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | BERT双向Transformer encoder, MLM, 原始版NSP，**2018公开不是2019才首发**；15%token选择预测，选中的80%MASK、10%随机、10%不变。 |
| DL115 | 2019-06 NAACL正式会议 | [Devlin, Chang, Lee & Toutanova, BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://aclanthology.org/N19-1423/) | 四位作者、2019正式会议4171–4186；原实验在11类NLP任务有竞争结果，不能外推所有下游任务。 |
| DL116 | 2019-02-14官方研究公告 | [OpenAI, Better Language Models and Their Implications (GPT-2)](https://openai.com/index/better-language-models/) | GPT-2是2019后续生成式LM，阶段性release政策也随着时间变化，不能称2019永久未公开。 |
| DL117 | 2020-01-23原始论文与官方摘要 | [Kaplan et al., Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) | 在论文测量范围内测试交叉熵loss随模型N、数据D、计算量C近似幂律；当时提出较大模型/较少token的compute efficiency安排，**实验归纳而非所有任务数学定律**。 |
| DL118 | 2020 NeurIPS正式论文 | [Brown, Mann, Ryder et al., Language Models are Few-Shot Learners](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) | GPT-3为175B参数的自回归LM；zero/one/few-shot示例仅在推理输入上下文中，无梯度更新/微调；原文明确承认多任务能力缺陷与训练语料污染等方法风险。 |
| DL119 | 2022-03预印本、2022 NeurIPS正式论文 | [Hoffmann, Borgeaud, Mensch et al., Training Compute-Optimal Large Language Models / An Empirical Analysis of Compute-Optimal Large Language Model Training](https://proceedings.neurips.cc/paper_files/paper/2022/hash/c1e2faff6f588870935f114ebe04a3e5-Abstract.html) | 四百余模型实验，计算预算固定下N和D适宜共同增长；Chinchilla70B与Gopher280B相近训练算力、前者约四倍训练数据并在论文多项基准上领先；实验拟合条件限制明显。 |
| DL120 | 2022-04-12官方研究解读 | [Google DeepMind, An empirical analysis of compute-optimal large language model training](https://deepmind.google/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training/) | 对compute-optimal与部署推理成本解释；不是超越所有模型的永恒保证。 |
| DL121 | 2021原始研究前史 | [Rae et al., Scaling Language Models: Methods, Analysis & Insights from Training Gopher](https://arxiv.org/abs/2112.11446) | Gopher 280B原始论文，2022 Chinchilla的相近算力对照参照；勿将此数据条件与GPT-3混用。 |
| DL122 | 2020-05-28 GPT-3预印本记录 | [Brown et al., Language Models are Few-Shot Learners, arXiv:2005.14165](https://arxiv.org/abs/2005.14165) | 2020年5月公开、后NeurIPS2020；GPT-3正式论断是few-shot上下文学习而非当时已完成通用可靠推理。 |

### 第22章：正式PDF与网页摘要数字有冲突

- **准确论文身份**：八作者Ashish Vaswani、Noam Shazeer、Niki Parmar、Jakob Uszkoreit、Llion Jones、Aidan N. Gomez、Lukasz Kaiser、Illia Polosukhin，NIPS2017；2017年6月已有预印本。PDF首页贡献脚注列多位作者分工，故不得将其称作某一人独创注意力。2014/2015 Bahdanau/Cho/Bengio已经采用跨源注意力，2017改变的是以自注意力为核心的完整序列结构。
- **2017正式会议PDF为本批数字依据**：WMT14英德28.4 BLEU、英法41.0 BLEU；官网网页摘要则列27.5与41.1，arXiv摘要有英法41.8。只使用原PDF的英德28.4作单一例子，另一组仅记录文献异文。各BLEU数字均是翻译评估，不是“28.4%句子正确”。
- **机制**：编码器6层，每层多头自注意力＋前馈；解码器6层，每层因果遮罩自注意力＋编码器/解码器注意力＋前馈。源/目标都有位置编码、残差连接及layer norm。Scaled dot-product attention = softmax(QKᵀ/√d_k)V，原实验h=8，d_model=512，d_k=64。位置编码原实验用不同频率sin/cos，学习式位置表示亦有比较；**没有循环不等于完全没有序列位置**。
- **并行限定**：训练阶段已知目标序列，可用因果遮罩并行计算多个位置；**自回归推断仍须一个token接一个token地产生**。完全全局attention简单实现包含n²成对分数与长上下文内存成本，不能宣传序列变长总更快。自注意力也非2017首次出现于全部研究。
- **算例**：q=(√2,0)、k₁=(ln3,0)、k₂=(0,1)、d_k=2，点积分数除√2得到[ln3,0]，权重[0.75,0.25]。值v₁=2、v₂=-2，加权结果=1.0。此为作者手工安排的单头标量V，不是2017真实模型权重。

### 第23章：2018两条迁移路线，不制造“谁先发明预训练”的伪冲突

- ELMo（Peters等NAACL2018）利用双向LSTM语言模型提供**上下文相关词表示**；ULMFiT（Howard/Ruder ACL2018）展示LSTM LM预训练后微调分类任务。GPT（Radford/Narasimhan/Salimans/Sutskever）2018-06官方公告结合**Transformer解码式左到右语言建模与任务微调**，而非GPT-3式推理只看示例且不修改权重。
- BERT四作者2018-10-11首版预印本、2019-06 NAACL正式论文。BERT使用双向Transformer**编码器**，masked LM以及原始版的NSP；选择15% WordPiece位置预测，所选中80%替换[MASK]、10%随机词片、10%原样不变。并非把原始文本的15%全部变成[MASK]，更不是所有训练步骤都在单词层而不是词片层。
- **现代教学**：若虚构训练批有1000个token位置，按期望比例选择150个作为MLM预测位；对应120个[MASK]、15随机替换、15不变（实际随机样本不需刚好精确）。GPT输入“我 今天 去”要预测下一token，BERT输入“我 [MASK] 去 学校”能借右侧位置；两任务不互相包含。2020 GPT-3的few-shot无梯度更新与2018 GPT微调**不是同一事实**。
- GPT-2 2019是独立后续节点；不能用今天模型产品能力倒写为2018原版已经能够处理任意多轮对话、工具或长推理。

### 第24章：参数、训练token、算力在同一约束下的权衡

- Kaplan等（2020-01）测量特定语言模型训练的**交叉熵损失**与N（参数量）、D（训练token）、C（训练计算）近似幂律关系。经验曲线不等于“倍增参数必倍增智能”“无限提升保证”。当时偏向更大模型、较少训练步的高效方案，在测量目标和约束下有成立条件。
- Brown等GPT-3（2020-05/NeurIPS2020）自回归1750亿参数（175B），zero/one/few-shot**在推理阶段不更新模型权重**；只将示例置于文本上下文。原文同时报告多个困难任务/数据污染、偏差与文本可靠性问题。
- Hoffmann等（2022 NeurIPS）在**训练计算预算固定**下，经验发现模型参数和训练token应更均衡增长。Chinchilla 70B参数、约1.4万亿tokens，对照Gopher 280B参数、较少训练tokens，在论文报告的测试任务上表现更好，二者大致相同的训练算力。70B不是“全世界所有任务最优”，也不意味着更新模型以后参数越多在任何约束下都无用。
- **算例**：20亿参数×400亿token与40亿参数×200亿token，参数量与训练token乘积都为800亿²；若采用训练FLOPs≈6ND的粗略估计，则两者成本同阶，**性能谁更高需实验**。70B与1.4T对应约20训练token/参数，是Chinchilla这个实验配置比值，不能宣布业界永恒经验常数。玩具幂律E(N)=A N^-0.1表示N翻倍时误差余量乘2^-0.1≈0.933（改善约6.7%，并非两倍）；指数-0.1由作者任意设定，不是Kaplan论文实际拟合指数。
- **制度与商业代价**：更大的模型训练通常需要昂贵的算力与数据质量治理；固定算力下更适当的模型/数据平衡还能降低推断成本，但是否适用取决于目标、训练分布、数据清洗、模型结构及实际环境。2020原论文的预训练损失与few-shot任务得分是不同指标，不能据一项推出事实可靠性和伦理治理已解决。

### 独立审稿未决事项

1. NeurIPS2017网页/正式PDF/arXiv三者数字冲突；全书22章只使用正式PDF已核值，若新增实验表必须注明原PDF版本与任务。对Transformer原始作者脚注、8头和position details逐页复审。
2. ULMFiT、ELMo、GPT2018和BERT2018/2019原始训练目标、模型架构及预训练-微调阶段归属独立核查，BERT遮罩采样按所选预测token而非总token百分比记述。
3. Kaplan2020、Brown GPT-3 2020、Hoffmann2022在不同模型、样本、预算及指标上的结果不能化作“参数唯一决定智能”的口号。
4. 第25章AlphaGo研究是**时间回溯**（2016—2017），并非2022规模定律直接产物；须在第24章尾与下一部开篇明确。
5. 此前第01—21章均仍为工作初稿并待独立双重审稿。本批独立审稿、终稿批准仍PENDING。

## 十三、第九批25—27章：AlphaGo/AlphaFold2/视觉语言多模态限域研究（2026-11-10）

> 本批只核查第25—27章中心论文书目、赛事实验协议、模型机制和作者侧例题；与先前第01—24章审稿状态互不替代。以下是可以进入非虚构工作初稿的**限定研究材料**，不是独立完整事实审计或终稿许可。外部原始论文、官方发布记录与研究机构方法说明已交叉查证，实际性能结论必须写明模型/版本/任务/年份。

| source_id | 来源层级 | 原始文献或机构记录 | 适用结论及危险误读 |
| --- | --- | --- | --- |
| DL123 | Nature原始论文2016-01-27 | [Silver, Huang, Maddison et al., Mastering the game of Go with deep neural networks and tree search](https://www.nature.com/articles/nature16961) | AlphaGo策略网络/价值网络/Monte Carlo tree search；人类棋谱监督加自我对弈强化学习；2015与樊麾正式五盘5:0；作者多团队，论文与2016李世石赛事不同 |
| DL124 | Google/DeepMind逐局官方赛事档案2016-03 | [Demis Hassabis, AlphaGo's ultimate challenge: five-game match against Lee Sedol](https://blog.google/innovation-and-ai/products/alphagos-ultimate-challenge/) | 2016-03-09至15首尔李世石5局，AlphaGo赢4输1；第四局李世石获胜，第五局AlphaGo获胜。不得把樊麾5:0或Zero100:0记为李世石分数 |
| DL125 | Nature原始论文2017-10-19 | [Silver, Schrittwieser, Simonyan et al., Mastering the game of Go without human knowledge](https://www.nature.com/articles/nature24270) | AlphaGo Zero从规则与自我对弈学习、单网络产策略与胜负估计，MCTS辅助产生更强策略；100:0对手是先前published champion-defeating AlphaGo版本，不是李世石或人类100局 |
| DL126 | Science原始论文2018-12-07 | [Silver, Hubert, Schrittwieser et al., A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play](https://doi.org/10.1126/science.aar6404) | AlphaZero同一算法规则下学习国际象棋、将棋、围棋；2017-12有预印本，2018 Science正式发表；不代表无需规则、无需算力或能解决现实任意决策 |
| DL127 | Nature原始论文2020-01-15/2018竞赛前因 | [Senior, Evans, Jumper, Kirkpatrick et al., Improved protein structure prediction using potentials from deep learning](https://www.nature.com/articles/s41586-019-1923-7) | 2018 CASP13 AlphaFold较早模型利用深度学习预测结构相关势函数；2020正式论文。它与2020 CASP14所用AlphaFold2不一样，勿混结构或比赛 |
| DL128 | Nature原始论文2021-07-15/CASP14 2020 | [Jumper, Evans, Pritzel et al., Highly accurate protein structure prediction with AlphaFold](https://www.nature.com/articles/s41586-021-03819-2) | AlphaFold2 2020 CASP14盲测，论文2021 Nature；CASP domains median Cα RMSD_95=0.96Å，次优2.8Å；原文明确2020系统不同CASP13 2018前版 |
| DL129 | CASP14评估/2021评审论文 | [Kryshtafovych et al., Applying and improving AlphaFold at CASP14](https://pubmed.ncbi.nlm.nih.gov/34599769/) | median domain GDT_TS=92.4，来自CASP14 evaluator context；GDT_TS百分制结构吻合分数，非92.4%所有蛋白完全正确 |
| DL130 | EMBL-EBI专家课程（方法结构） | [AlphaFold2: A high-level overview](https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/a-high-level-overview/) | MSA、pair representation、Evoformer、structure module与recycling；从序列预测结构非实验测得动态；未知是否每条序列均有丰富MSA |
| DL131 | Nature原始论文2021-07-22/数据扩展 | [Tunyasuvunakool et al., Highly accurate protein structure prediction for the human proteome](https://www.nature.com/articles/s41586-021-03828-1) | 2021约98.5%人类蛋白质有预测结构，但仅58%残基被论文判为confidence prediction、其中36%所有残基very high；覆盖不等于全面高置信 |
| DL132 | EBI AlphaFold DB官方限制与指标说明 | [AlphaFold Protein Structure Database FAQ](https://alphafold.ebi.ac.uk/faq) | pLDDT为局部预测可信度；结构低置信区域、固有无序、配体、复合物、动态构象、突变影响等限制；不同数据库版本更新，勿用它代表CASP14当年可用功能 |
| DL133 | Nucleic Acids Research数据版本回顾2024 | [AlphaFold Protein Structure Database in 2024: over 214 million protein sequences](https://academic.oup.com/nar/article/52/D1/D368/7337620) | 2021首次发布、2022扩库，2024回顾超过214m。与2020盲测模型性能不是同一事；数据库数字可能随版本变化 |
| DL134 | ICML 2021正式原始论文 | [Radford, Kim, Hallacy, Ramesh et al., Learning Transferable Visual Models From Natural Language Supervision (CLIP)](https://proceedings.mlr.press/v139/radford21a.html) | 12位作者；约4亿image-text pairs；双编码器对比训练匹配图与文本，zero-shot图像分类基准；CLIP自身学习匹配/表示，不是文本绘图生成器 |
| DL135 | 原始研究预印本2021-02-26 | [Radford et al., CLIP arXiv:2103.00020](https://arxiv.org/abs/2103.00020) | 与2021 ICML正式论文对应；具体zero-shot条件比较ImageNet原ResNet50，不能宣称所有视觉基准无监督全面优胜 |
| DL136 | ICML 2021正式论文/Google研究团队 | [Jia, Yang, Xia, Chen et al., Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision (ALIGN)](https://proceedings.mlr.press/v139/jia21b.html) | 10作者，约18亿噪声图文alt-text对，双塔对比式学习；与CLIP平行研究，不是CLIP内部组成部分；噪声与数据质量是明确问题 |
| DL137 | ICML 2021原始论文（DALL-E第一代） | [Ramesh, Pavlov, Goh, Gray, Voss, Radford, Chen & Sutskever, Zero-Shot Text-to-Image Generation](https://proceedings.mlr.press/v139/ramesh21a.html) | 2021 DALL-E第一代用Transformer自回归建模文本与图像tokens联合序列，是生成模型，不要与CLIP对比编码器混为同一架构 |
| DL138 | 原始2022研究公告与论文 | [Ramesh, Dhariwal, Nichol, Chu & Chen, Hierarchical Text-Conditional Image Generation with CLIP Latents](https://openai.com/index/hierarchical-text-conditional-image-generation-with-clip-latents/) | 2022第二代文本条件图像生成把文本映射CLIP图像表示，再用扩散解码器生成；先验/解码器机制不同CLIP匹配本身 |
| DL139 | CVPR 2022原始正式论文 | [Rombach, Blattmann, Lorenz, Esser & Ommer, High-Resolution Image Synthesis with Latent Diffusion Models](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html) | 先自编码压缩到潜空间再扩散、cross-attention接受文本等条件；不同于2022 DALL-E2结构与开发团队；本书第21章已经介绍扩散，27章重点是图文条件与表征如何对接 |


### 第25章：2016 AlphaGo、2017 Zero与2018 AlphaZero三者不可合成一个程序

**来源界限**：DL123 2016 Nature披露策略网络+价值网络+MCTS，人类高手棋谱监督学习+自我对弈强化学习；2015年樊麾5比0写在论文中；DL124官方比赛记录2016年3月9—15日对李世石4比1，第四局李世石胜。DL125 2017 Nature AlphaGo Zero只用棋规加自我对弈学习（且需大量计算），100比0是针对**先前发表于2016的AlphaGo**，不是百场挑战人类。DL126的AlphaZero在2017预印本、2018 Science正式刊出，跨围棋、国际象棋与将棋的研究仍以已知规则为条件。**不写“AlphaGo仅靠监督学习”“AlphaGo Zero不需要搜树”“AlphaGo Zero完全没有规则”或“围棋全空间被穷举”。**

**玩具计算（作者演示）**：若某一虚构棋局只剩3个合法行动，策略先验p=[0.6,0.3,0.1]，搜索统计访问N=[10,30,10]，按访问量归一化后π=[0.2,0.6,0.2]。只解释网络先验与搜索后选择可以不同；真实AlphaGo搜树规则远复杂，不是论文训练局面，搜索访问量统计不是原始策略网络输出。若价值网络输出胜率估计0.7，不是“保证70%将赢”，只是模型对指定局面的概率估计，需要校准。请区分prediction、decision和outcome。

### 第26章：蛋白质结构预测不是所有生命机制的解释

**年份/指标分开**：CASP13发生2018，较早AlphaFold结构相关势能研究发表于2020 Nature（DL127）；CASP14发生2020，独立的AlphaFold2模型Nature论文发表于2021（DL128）。该论文中对CASP domains的median Cα RMSD_95约0.96Å vs次优2.8Å，**不是“每个氨基酸误差0.96Å”**；独立CASP14评估median domain GDT_TS=92.4（DL129），**不是92.4%预测蛋白完全正确**。2021人类proteome98.5%覆盖但58%残基有confidence、36%高confidence（DL131）须同时说清，数据库版本后来更新不代表2020盲测前就已经有亿级记录。

**核心工作流程**：序列→MSA/模板与成对信息→Evoformer处理MSA/配对表示→结构模块输出三维坐标→recycling精修；pLDDT为局部可信度指标，不等于实验测量的确证。蛋白质是动态分子，多构象、无序、配体、复合物和突变致病性等问题不能一概由单链静态结构推出（DL130/DL132）。

**教学例题（自造）**：比较三组预测/实验坐标距离误差[1,2,3]Å，按均方根定义RMSD=√((1²+2²+3²)/3)=√(14/3)≈2.160Å。只是已对齐同等对象的极简数学算例，不是CASP计算实现（需要最优结构对齐/95% residue覆盖/多域指标）。0.96Å与2.8Å不能直接用这组toy替代。

### 第27章：共享语义空间≠生成图像本身

CLIP 2021（DL134/DL135）双编码器对4亿图文配对计算匹配，对比学习拉近正确配对并相对拉远不匹配，实现自然语言定义类别的zero-shot分类/检索，但模型自身不是文生图生成器。ALIGN 2021（DL136）使用约18亿噪声alt-text图文对，说明数据规模/标注噪声权衡，**不是CLIP内部训练数据**。2021首代DALL-E（DL137）将文本/图像tokens视作联合序列自回归生成；2022 DALL-E2（DL138）先验预测CLIP image embedding并用扩散解码器绘图；2022 LDM（DL139）在压缩视觉潜空间做扩散及cross attention文本条件，这几条路径**不能视作同一模型改名**。

**玩具对比（自造）**：图像向量v=(1,0)，文本“猫”t₁=(0.8,0.6)、“车”t₂=(0,1)，均为单位向量，余弦相似0.8与0。softmax按温度τ=1，P(cat)=e^0.8/(e^0.8+e^0)≈0.690；图中“猫”获得较高配对分数**不等于图像生成，也不等于对照片内容完备理解**，概率取决候选类别和温度。

**跨章逻辑**：24章2022 scaling→25章专题回到2016 AlphaGo→26章2020 CASP14/2021 Nature AlphaFold→27章2021图文表示/2022条件生成。25–27章展示不同科学任务与不同证据标准；28章对话系统与人类反馈/部署需另查证，不能推断由CLIP唯一直接引发。

## 十四、第十批28—30章：ChatGPT/RLHF、国际开放生态、2024—2026推理与评测（截至2026-11-10）

> **研究版本固定于2026-11-10。** 本批只把原始论文、官方产品档案、许可证和2026年同行评审/预印本研究用于中心史实及机制核查。2026年后续模型榜单不断变化，不使用实时排行榜数值；机构自报成绩保留对照条件，2026年预印本不假装同行评议通过。`DL140—DL161`仅支持第28—30章限定写作；独立双审仍PENDING。

| Source | 等级/节点 | 研究与链接 | 准确支持范围与反证 |
| --- | --- | --- | --- |
| DL140 | NIPS 2017原论文 | [Christiano, Leike, Brown, Martic, Legg & Amodei, Deep Reinforcement Learning from Human Preferences](https://papers.nips.cc/paper_files/paper/2017/hash/d5e2c0adad503c91f91df240d0cd4e49-Abstract.html) | 游戏和模拟控制任务的人类片段偏好学习早于2022 InstructGPT；不是直接训练2017 ChatGPT |
| DL141 | NeurIPS2022原始论文 | [Ouyang, Wu, Jiang等20作者, Training language models to follow instructions with human feedback](https://proceedings.neurips.cc/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract.html) | SFT示范→人类排序→奖励模型→PPO RLHF；1.3B InstructGPT在论文的特定提示集人类偏好评测中优于175B GPT3，不代表一切知识任务更强 |
| DL142 | 官方产品历史公告2022-11-30 | [OpenAI, Introducing ChatGPT](https://openai.com/index/chatgpt/) | ChatGPT 2022-11-30研究预览，产品对话形式与RLHF相关；发布不是RLHF或所有Transformer的发明日；原公告承认貌似合理但错误回答和对提示敏感 |
| DL143 | ACL 2022原始论文 | [Lin, Hilton & Evans, TruthfulQA: Measuring How Models Mimic Human Falsehoods](https://aclanthology.org/2022.acl-long.229/) | 817问题38类别；2022所测试旧系统中某些大模型更易重复错误信念；不能外推成2026任一模型具体成绩 |
| DL144 | 2023 GPT4原始技术报告 | [OpenAI et al., GPT-4 Technical Report](https://arxiv.org/abs/2303.08774) | 2023-03 GPT4技术报告强调仍有幻觉和推理错误，内部评测改进不等于零误差、ChatGPT 2022与GPT4 2023不能倒写 |
| DL145 | NeurIPS2023偏好优化原论文 | [Rafailov, Sharma, Mitchell, Manning, Ermon & Finn, Direct Preference Optimization](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html) | DPO用偏好配对直接优化目标，不需要单独奖励模型+PPO同一训练流程；不是宣称所有对齐只有DPO |
| DL146 | Meta Llama2社区许可证2023-07-18 | [Meta, Llama 2 Community License Agreement](https://ai.meta.com/llama/license/) | 可获取权重、代码但自定义社区许可且大规模商业使用有月活700m门槛；不能把open-weight自动叫OSI open-source |
| DL147 | 2024研究预印本/原始研究 | [Groeneveld et al., OLMo: Accelerating the Science of Language Models](https://arxiv.org/abs/2402.00838) | Ai2 OLMo 2024年连训练数据/代码/检查点一起开放，用于研究可复现；与只释放权重不同 |
| DL148 | OSI 2024-10-28定义v1.0 | [Open Source Initiative, Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition) | 开源AI应有使用/研究/修改/分享自由及训练数据足够信息、完整代码、参数，开放权重≠充分开源 |
| DL149 | 官方Qwen团队2024-09-19 | [Qwen Team, Qwen2.5: A Party of Foundation Models](https://qwenlm.github.io/blog/qwen2.5/) | Qwen2.5多个模型体量，Apache2.0非覆盖所有版本，原官方称3B、72B非Apache2.0；许可证须逐型号确认 |
| DL150 | 2025-05-14技术报告 | [Yang, Li, Yang等, Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) | Qwen3含稠密和MoE架构、thinking/non-thinking模式及预算控制，团队称系列模型Apache2.0；不能宣称是首个有思考的模型 |
| DL151 | 2024-12-27技术报告 | [DeepSeek-AI, DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) | MoE 671B总参数、每token 37B激活；训练耗2.788m H800 GPU小时为论文报告并非所有研发成本或推理价格；MLA/DeepSeekMoE协同 |
| DL152 | 2025-01/2025-09正式Nature | [DeepSeek-AI, DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://www.nature.com/articles/s41586-025-09422-z) | 2025-01先公开原型，2025-09正式Nature；R1-Zero无SFT预置但有基础预训练+RL、完整R1有cold start/SFT/RL，不能混为‘全部不需监督’ |
| DL153 | 原始模型仓库许可与蒸馏派生条件 | [DeepSeek-AI, DeepSeek-R1 README licensing](https://github.com/deepseek-ai/DeepSeek-R1) | 主体R1代码与权重MIT，蒸馏模型继承部分Qwen Apache与Llama自定义许可；不得一概宣布所有衍生MIT |
| DL154 | 2022 NeurIPS原始论文 | [Dao, Fu, Ermon, Rudra & Ré, FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://proceedings.neurips.cc/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html) | IO-aware tiling减少GPU HBM读写且计算精确attention；不是将原有全局数学注意力自动改为O(n)所有运算 |
| DL155 | SOSP2023原始论文 | [Kwon, Li, Zhuang, Sheng, Zheng, Yu, Gonzalez, Zhang & Stoica, Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | vLLM/PagedAttention KV cache分页管理、提高特定实验吞吐；不把论文2-4倍对照值泛化为所有硬件部署 |
| DL156 | 2024-09-12官方研究公告 | [OpenAI, Learning to reason with LLMs (o1)](https://openai.com/index/learning-to-reason-with-llms/) | 2024-09公开o1-preview测试时较长推理与RL，报告性能随训练/测试算力增加而改善（特定实验），不是‘多写字就必对’ |
| DL157 | 2025-01原始预印本 | [DeepSeek-AI, DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) | R1-Zero与R1不一样；GRPO与可验证结果奖励，生成推理文本的长度/正确性不能简单等同 |
| DL158 | Nature 2026-01-28正式基准论文 | [CAIS, Scale AI & HLE Contributors, A benchmark of expert-level academic questions to assess AI capabilities](https://www.nature.com/articles/s41586-025-09962-4) | HLE约2500多领域专家编写封闭式可评分问题，分数只证明该评测目标结果，不能证明跨全部现实研究可靠 |
| DL159 | 2026-08独立研究预印本 | [Fan, Cheng, Li, Liang, Zhou & Feizi, Thinking Hard, Not Smart: Reasoning Models Fail to Ration Test-Time Compute Across Questions](https://arxiv.org/abs/2608.07968) | 2026-08预印本提出多题共预算测评，发现多模型偏按题序分配思考token而非难度和价值；尚非正式独立复制的定论 |
| DL160 | 2024-02论文开放前史 | [AI2, OLMo Release / accessible model flow](https://allenai.org/blog/hello-olmo-a-truly-open-llm-43f7e7359222) | 官方2024-02-01发布OLMo 7B并披露预训练数据与代码；不同于公开推理端点 |
| DL161 | 2025论文与2019—2026跨年限制 | [Brown et al., Language Models are Few-Shot Learners (2020)](https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) | 语言预测和few-shot上下文表现非人类式知识确保；第24章已核，可跨章引用 |

### 第28章前置事实链与教学例子

2017 Christiano等关于模拟任务的人类偏好强化学习，不得写成“ChatGPT在2017年就发布”。2022-03 Ouyang等InstructGPT论文：人工示范→SFT→比较偏好→训练奖励模型→PPO优化输出策略；1.3B模型在**限定的标注者偏好提示分布**上被选高于175B原GPT3（不同版本/条件），不能作为事实准确性、跨所有任务碾压结论。2022-11-30 ChatGPT作为交互研究预览发布，界面/多轮输入与模型训练目标相互配合；2023-03 GPT4是新阶段且仍有幻觉，不能将后续模型能力倒灌2022产品。2023 DPO作为不同偏好优化路径，禁止宣称PPO永远独占后训练。TruthfulQA 817/38是2022原论文测试，不能用来宣称2026任一模型具体正确率。

**玩具例子**：两条虚构回答在3名标注者排序中A胜2、B胜1，简单偏好频率A=2/3；但不等于“回答A在世界上正确概率66.7%”。假设奖励模型分数rA=1.2，rB=0.2，softmax temperature=1 得P(A)=e^1.2/(e^1.2+e^.2)=1/(1+e^-1)≈0.7311，仅是作者概率归一化，不是原始PPO奖励定义或人类事实判定。比较SFT/偏好偏离知识正确与奖励模型的局限。

### 第29章前置事实链与许可边界

章节历史是**国际协作与多种开放制度**，不按个人国籍将成果划为国家竞争比分。2017原Transformer八作者、2015/2016 ResNet作者按所属论文机构与学术交流描述，不能从姓名断定国籍。2023 Meta Llama2自定义Community License有700m MAU附加授权门槛，即使权重可获得也不满足所有OSI1.0自由。2024 Ai2 OLMo公开训练数据+代码+权重与日志，体现可研究完整模型流程；2024 OSI定义v1.0对数据来源信息、训练/推理代码和参数的要求不只下载权重。2024-09 Qwen2.5版本许可有例外（3B和72B），不能将该系列均标Apache2.0；2025-05 Qwen3技术报告称系列Apache2.0，按每个模型具体版本核验。2024-12 DeepSeek-V3 MoE 671B total, 37B activated / token，只是激活参数数、不是单次显卡显存恰好37B；论文报告2.788m H800 GPU小时不等于总研发美元预算。2025-01 DeepSeek-R1主模型权重MIT，蒸馏基于Llama的派生各自许可另看，R1-Zero与正式R1训练流程不同。

**玩具例子**：有8个专家、每次仅激活其中2个专家，设各有10M参数+共有5M，模型总计8*10+5=85M，假设每token激活参数2*10+5=25M，激活比例25/85≈29.41%。仅展示总参数/激活参数区别，非DeepSeek原模型。许可证矩阵：权重/代码/训练数据细节/商用限制可被独立填是/否/未知，缺证不补齐。

### 第30章前置事实链与2026研究边界

2022 FlashAttention依据内存层级减少精确attention IO，2023 vLLM PagedAttention减少KV缓存浪费及改善吞吐；**训练速度、每token生成延迟、端到端成本、单请求质量完全是不同指标**。2024-09 o1官方报道推理过程与测试时计算改善，机理描述仅限官方公开；2025 R1-Zero在基础模型上使用强化学习（非从零预训练）与结果校验、真实R1结合cold-start/SFT等。Qwen3 2025给thinking/non-thinking模式及预算选择；并不表明任意增加推理token无限收益。2026-01 Nature HLE 2500专家题测试不同能力，不能把模型答对题量作为全部真实世界可靠性保证。2026-08 Fan等六作者**预印本**在多题共享token预算下发现多款模型不能有效根据题目价值与难度分配tokens；这是针对固定实验设置的批判，不是全领域已证明的定理。发表截至2026-11-10。

**玩具例子**：两题A值5分、B值1分，共分配10个思考单位；如果A使用6单位可解对，B使用4单位可解对，则6分；若各用5则A未达阈值、B正确，仅1分。人为指定阈值说明共享预算资源分配问题，**不能假装这就是论文模型真实实验**。另算假设一次答题原先1000输出tokens成本100单位，新增500推理tokens成本单价不变则token部分×1.5，不能推为真实API总费用×1.5，因为缓存、模型、请求和硬件条件都会变化。

**写作闸门和交接**：DL140—DL161中的时间/方法/许可/指标限定支持28—30工作初稿；所有前述01—27独立双审仍PENDING。序章00与尾声31无本批写作许可，正式审核与终稿/发布未执行。

## 十五｜第00序章、第31尾声与非编号专题附录A的限定研究（2026-11-10）

> 这轮只补32篇原定结构中尚未完成的序章00、尾声31，并提供第三篇非编号专题附录A。**附录不计入book.json正式章节，也不增加全书数量**。以下仅批准限定史实、数学例题和跨章解释进入工作初稿，不代表独立事实/结构审稿通过。

| ID | 证据身份 | 原始资料 | 限定用途 |
| --- | --- | --- | --- |
| DL162 | 2012 ILSVRC官方当年分类成绩表 | [ILSVRC2012 Task 1: Classification Results](https://image-net.org/challenges/LSVRC/2012/results.html) | SuperVision top5测试0.15315（含Fall2011额外训练数据）；仅使用当年供给训练数据的另一提交0.16422；ISI手工特征组合0.26172。都是5猜错误率，不能当单网络准确率。 |
| DL163 | 2012 NeurIPS论文正式PDF | [Krizhevsky, Sutskever & Hinton, ImageNet Classification with Deep Convolutional Neural Networks](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) | 七个CNN集成的2012竞赛15.3%及第二名26.2%；2010单网络的37.5% top1与17% top5不同任务。NeurIPS网页摘要指标与PDF不同，正文沿用官方竞赛表。 |
| DL164 | Nature2015三作者原始领域综述 | [LeCun, Bengio & Hinton, Deep Learning, Nature 521:436–444](https://www.nature.com/articles/nature14539) | 深层表征、反向传播、CNN/RNN及多领域应用，属于当事学者综述而非所有历史参与者的统一解释。 |
| DL165 | 2024诺贝尔奖官方新闻稿 | [Royal Swedish Academy of Sciences, Physics Nobel Prize 2024, Press Release](https://www.nobelprize.org/prizes/physics/2024/press-release/) | John J. Hopfield与Geoffrey E. Hinton因神经网络机器学习奠基工作获奖；后见之明不能倒写1980年代已具备2012大数据深网。 |
| DL166 | 1943原始论文书目信息 | [McCulloch & Pitts, A logical calculus of the ideas immanent in nervous activity, Bull Math Biophys 5:115–133](https://doi.org/10.1007/BF02478259) | 形式逻辑计算与今天学习参数的深网络不同，历史跨度不是单一师承链。 |

### 序章00：真实的2012异常和四重方法边界

1. 官方ILSVRC2012分类Task1表列：SuperVision 15.315% Top5 test（使用ImageNet Fall2011额外训练数据），SuperVision 16.422%（仅2012供给训练数据），ISI 26.172%（手工特征集成）。2012论文四舍五入15.3%对26.2%，不能把15.3%写成单CNN成绩、不能声称公平控制变量证明纯架构效果，也不代表每张图片理解完整（DL162/DL163/DL80）。
2. 2009 ImageNet数据论文描述320万图片/5247 synsets/12个子树（DL77/DL78），2012 ILSVRC1000分类子集不同（DL79）。不把两数据集版本数量揉成一个实验。
3. CNN早于2012，1943形式神经元（DL166），1986反传重要推广（DL47），1989/1998卷积文档识别路线（第10章及其DL来源）；2012是大数据、GPU实现、ReLU/dropout/数据增强与团队协作形成可核组合（DL80/DL89）。2015综述（DL164）属于后世评论。
4. 作者教学示例：若有10000幅**虚构**图片，四舍五入Top5错误率15.3%对应约1530幅，26.2%对应约2620幅，差1090幅/10.9百分点；假想样本数并非竞赛测试集实际规模，配置非控制实验，不推出单个机制的因果贡献。Top5错误率是正确类未进入5候选的频率，非图片只含5种可能类别。
5. 序章真实问句：为何有此前数十年的可计算形式、反传与CNN，2012才在特定大规模视觉任务里出现令人瞩目的可比改善？第01章从形式工具远源进入，第17章完整兑现训练和测试条件。

### 尾声31：四个未完成但可证其重要的问题

1. **训练与经验**：1943逻辑计算≠1990年代可训练表示，更不等于2020规模增长；1986反传、2006预训练、2012大规模监督训练、2020 Kaplan与2022 Chinchilla分别对训练提出限定回答（DL166/DL47/DL68/DL80/DL117/DL119）。抽离具体条件不能断言“参数翻倍智能翻倍”。
2. **表示与理解**：Transformer2017是序列表示架构（DL107），2018 GPT/BERT任务目标不同（DL113/DL115），CLIP图文匹配不自动生成图像（DL134/DL137），AlphaFold2几何结构盲测不等于所有生物功能（DL128/DL129）。对“理解”的哲学和科学定义应标明争论仍开放。
3. **评价与可靠性**：ILSVRC top5、BLEU、GDT_TS、TruthfulQA、InstructGPT人评、2026 Nature HLE各有不同分母和任务（DL162/DL95/DL129/DL143/DL141/DL158）；模型得分≠全场景事实可靠、法律伦理适用性。
4. **社会价值与治理**：2022 ChatGPT研究预览（DL142）、2024 OSI开源AI定义（DL148）、2024 Hopfield/Hinton物理学奖（DL165）及开放模型的许可（DL146/DL149/DL153）提供讨论依据；究竟该如何治理是作者分析，不能当原始论文已证明的唯一政策方案。
5. 作者教学“矩阵”：假想模型在100分类样本Top5中90题命中，但另一组20项风险场景仍有5次严重错误；两组分母/任务不同，不能用90%推出安全性能。所有数字明确为自造，不冒充真实测试。

### 附录A「深度学习史十个常见误读」来源

①2012年才发明CNN？（第10/17章与DL80）；②15.3%是单网络成绩？（DL162）；③竞赛错误率=世界理解？（DL79）；④反传1986首次发明？（本书第07/09章、DL47）；⑤“AI寒冬”期间全领域停止？（第06—12章）；⑥注意力到2017才有？（DL93、DL107）；⑦GPT/BERT只差参数量？（DL113/DL115）；⑧AlphaGo Zero完全没有人类知识/规则/搜索？（DL125）；⑨CASP14 GDT_TS92.4=92.4%蛋白全部正确？（DL129）；⑩开放权重=完整开源、语言流畅=事实可靠？（DL141/DL143/DL148）。每项为误区、反例、看论文的方法、残留问题；不能编造历史场景或暗示附录替所有章节独立审稿。

**目录约束**：将附录放在appendices/A.md及appendices/A.claims.json，README和批次特别交接链接；不要新增book.json.chapters条目，不要改变32篇总数。所有未审状态保持PENDING。
