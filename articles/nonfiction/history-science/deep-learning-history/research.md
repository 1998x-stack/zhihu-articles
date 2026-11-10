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


## 第六批16—18章限定证据复核（2026-11-10，非独立审稿）

> 本节只为第16—18章的**史实与机制性工作初稿**提供有界证据。核查了三篇原论文的公开PDF首页/关键表格以及2012竞赛官方说明；正式同行史学审阅、重复实验、全部图表核对仍未完成。本节不能将全书evidence_verified外推为全部资料已核。

| ID | 原始来源、时间与可核链接 | 检查点 / 精确支持范围 | 边界 |
| --- | --- | --- | --- |
| DL77 | Deng, Dong, Socher, Li-Jia Li, Kai Li, Li Fei-Fei, “ImageNet: A Large-Scale Hierarchical Image Database”, CVPR **2009**, [论文PDF](https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf) | PDF p.1摘要与§2：当时12个子树、**5,247个synsets、约320万图像**；基于WordNet词义集；§3.2通过Amazon Mechanical Turk进行人工候选图核实。 | **2009快照**，不能拿来描述2012竞赛训练集的1000类/120万图像；原论文50百万是长远目标，不是2009已完成数。 |
| DL78 | ImageNet团队， [ILSVRC 2012官方挑战页面](https://image-net.org/challenges/LSVRC/2012/)，2012 | Data节：挑战分类为1000类，训练集约**120万**图像，验证集50,000，官方验证+测试共150,000；测试标签当时不公开。 | 比赛任务子集与整个ImageNet数据库不等价；不同年份任务、评估口径不得直接排序。 |
| DL79 | Russakovsky et al., “ImageNet Large Scale Visual Recognition Challenge”, IJCV **2015**, 115:211–252，[arXiv稿](https://arxiv.org/abs/1409.0575)、[期刊记录](https://link.springer.com/article/10.1007/s11263-015-0816-y) | 自2010年起的ILSVRC体系性回顾；数据采集/评测协议、分类与检测任务分别说明，含数据集与评测的局限。 | **2015回顾文章**不属于2009建库或2012论文当时的原始发表；后见之明应明确标注。 |
| DL80 | Krizhevsky, Sutskever & Hinton, “ImageNet Classification with Deep Convolutional Neural Networks”, NeurIPS/NIPS **2012**, [官方PDF](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) | PDF p.1、§3–§6、Table 1/2：5卷积+3全连接学习层；两块GTX580 3GB，训练约5–6天；**ILSVRC-2010 test top-1 37.5%、top-5 17.0%；ILSVRC-2012单CNN验证top-5 18.2%、7模型集成测试top-5 15.3%，竞赛第二名26.2%**。 | 2012年**15.3%是混合预训练模型的集成比赛结果**，不是单个AlexNet的表现；NIPS网页摘要与该PDF在2010示例数字存在不一致，本批采用PDF并记录版本风险。2010与2012的数字不可混称。 |
| DL81 | He, Zhang, Ren & Sun, “Deep Residual Learning for Image Recognition”, [2015-12预印本](https://arxiv.org/abs/1512.03385)、CVPR **2016** [官方开放PDF](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf) | PDF p.770–775，Fig.1、Fig.2、Fig.4、Table 2：CIFAR-10较深**plain 56层比20层训练误差更大**；ImageNet plain 18层top-1验证错误率27.94%、plain34层28.54%，ResNet-18为27.88%、ResNet-34为25.03%；论文Table 5所述ILSVRC2015集成测试top-5错误率**3.57%**。 | 高训练误差是**优化退化**证据，不等于单纯过拟合或所有情形下都由梯度消失造成；3.57%是集成测试，非任意单模型。2015先公开预印本，2016发表于CVPR。 |

### 本批结构性核验结论

1. **ImageNet ≠ ILSVRC ≠ ILSVRC-2012训练切片**：2009建库论文的320万与2012挑战训练120万不矛盾，统计对象和版本不同。[DL77,DL78,DL79]
2. **AlexNet结果保留双口径**：2010数据上的单网络37.5/17.0，2012挑战18.2%单模型验证 vs 15.3%七模型集成测试，禁止将后者与2010结果拼成“同一次试验”。[DL80]
3. **赛事比较应按指标**：top-5错误率是正确类不出现在前五个候选中的比例。2012年15.3%与26.2%差**10.9个百分点**，相对误差下降10.9/26.2≈**41.6%**；不等于准确率提高41.6个百分点。算术为作者可复算示例。[DL80,AUTHOR_DERIVATION]
4. **残差不是凭空增加信息**：当映射H(x)适合保留已有表征时，学习F(x)=H(x)-x并叠加x，提供优化的方便路径；x+F(x)为形状一致/适当投影条件下的块表示，不能写成所有网络“梯度永远不消失”。[DL81]
5. **ResNet实验口径**：Fig.1与Fig.4的plain深层训练误差更高是退化；Table2显示plain34（28.54）高于plain18（27.94），而ResNet34（25.03）低于ResNet18（27.88）。这组为**ImageNet验证top-1**，与2015年ILSVRC top-5集成3.57%不同。[DL81]

### 非虚构审查边界 / 待审问题

- 第16—18章允许使用以上已核到原始论文与比赛官方页面的**有限史实与教学计算**写作工作初稿；争议、历史“第一”、平台归因须保守。
- ImageNet的类别构造、网页搜索和人工标注都包含采样和社会语义边界；本批不做未经独立数据研究支持的偏见量化、人工标注质量的绝对化断言。
- 将NeurIPS官方网站HTML摘要与PDF版本差异登记为开放的版本复核事项；优先使用链接的正式论文PDF表与具体实验口径。
- 独立的连续性/事实审计、结构审稿、修订精修与最终发布继续标记PENDING。本记录不等同同行审稿，也不证明实验复现。
