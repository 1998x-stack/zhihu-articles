# 双线时间轴｜论文事件 / 数据与基础设施

> 只标用于定位的高价值历史节点。各地区研究路线不总构成直接传承；确切首发、版本和竞赛口径须参照`research.md`逐项核对。

| 时间 | 思想、算法或论文 | 评价、资源、应用及注意事项 | 对应章 |
| --- | --- | --- | --- |
| 古代—19世纪 | 逻辑、概率、微积分等形式工具不断发展 | **思想前史，不是深度学习出现** | 01 |
| 1943 | McCulloch–Pitts形式神经元 | 与可学习的多层网络有重要区别 | 03 |
| 1949 | Hebb的神经可塑性思想 | 书目原文待查 | 04 |
| 1958 | Rosenblatt感知机论文、IBM704演示 | 论文与硬件演示应分开；校方回顾不是独立测评 | 05 |
| 1960 | Widrow–Hoff自适应切换电路/LMS路线 | 感知机之外的另一类误差驱动训练机制 | 05—06 |
| 1969 | Minsky、Papert出版Perceptrons | 对特定架构与计算几何任务的数学限制；不可误推所有多层模型无效 | 06 |
| 1973 | 英国Lighthill报告 | 英国AI研究政策与期待问题；经费因果仍有争议 | 06 |
| 1970/1976 | 芬兰Linnainmaa硕士论文与BIT论文 | 数值舍入误差/逆向灵敏度研究；不是现代神经网络训练 | 07 |
| 1971 | Intel 4004微处理器商业发布 | 日本Busicom项目背景；不能推出当年具备现代深网训练条件 | 07 |
| 1974 | Werbos的哈佛博士论文 | 非线性预测与反向敏感度路线；不臆造直接师承 | 07 |
| 1978 | Ivakhnenko GMDH统计自组织模型论文 | 结构选择路线与梯度训练各异 | 07 |
| 1979/1980 | Fukushima新认知机IJCAI会议/期刊 | 日本视觉研究：S/C层次、无教师自组织；非现代CNN端到端反传 | 08 |
| 1982 | Hopfield PNAS联想记忆 | 稳定状态与内容寻址；异步能量条件 | 08 |
| 1985 | Ackley、Hinton、Sejnowski玻尔兹曼机学习论文 | 随机状态与能量学习，不等于监督反向传播 | 08 |
| 1985 | LeCun Cognitiva阈值网络学习研究 | 已有隐藏层调整探索，不与1986 Nature方案混同 | 09 |
| 1986-10-09 | Rumelhart–Hinton–Williams的Nature反向传播论文 | 可微隐藏层信用分配与表示学习，重要推广节点而非唯一发明起点 | 09 |
| 1989 | LeCun等Backpropagation Applied to Handwritten Zip Code Recognition | 结合任务结构先验与反向传播；非1998才第一次相关研究 | 10 |
| 1992 | Boser/Guyon/Vapnik最优间隔分类器 | 与神经网络视觉研究并行，有研究人员交叉 | 12 |
| 1994 | Bengio/Simard/Frasconi长期依赖训练困难分析 | 记忆稳定性与可训练性存在张力 | 11 |
| 1995 | Cortes/Vapnik支持向量网络论文 | 研究不可完美分隔数据与非线性映射 | 12 |
| 1997 | Hochreiter/Schmidhuber原始LSTM论文 | CEC/输入输出门，**尚无2000年遗忘门** | 11 |
| 1998 | LeCun/Bottou/Bengio/Haffner IEEE文档识别论文 | LeNet-5、GTN商业票据系统；部署处理量口径未消歧 | 10、12 |
| 1998 | Burges SVM教程、Platt SMO技术报告 | 模型的数学目标与训练工程条件同样重要 | 12 |
| 2000 | Gers/Schmidhuber/Cummins LSTM遗忘门 | 持续序列的自动重置问题，区别于1997原版 | 11 |
| 2000 | Bengio/Ducharme/Vincent三作者NIPS神经概率语言模型会议论文 | 早于2003四作者期刊版本 | 13 |
| 2002 | Hinton对比散度概率模型训练论文 | 为后续RBM逐层训练提供相关工具 | 14 |
| 2003 | Bengio/Ducharme/Vincent/Jauvin JMLR神经概率语言模型 | 共同学习连续词表示与条件概率；非2013 word2vec | 13 |
| 2006 | Hinton/Osindero/Teh深度信念网络逐层训练 | 混合有向/无向生成架构，原论文生成微调是对比式wake-sleep | 14 |
| 2006 | Hinton/Salakhutdinov Science深自编码器 | 好的预训练初始化后使用梯度微调；与DBN生成微调有别 | 14 |
| 2006 | Bengio/Lamblin/Popovici/Larochelle NIPS逐层训练 | 蒙特利尔研究方向，贡献归属不独占 | 14 |
| 2009 | Deng/Wei Dong/Socher/Li-Jia Li/Kai Li/Li Fei-Fei的ImageNet论文 | 当时320万图、5247 synsets；是数据库，不等于年度竞赛子集 | 16 |
| 2010 | ILSVRC开始使用更大规模视觉共同评测 | 训练/验证/隐藏测试，千类竞赛；早有PASCAL VOC先驱 | 16 |
| 2011 | Seide/Gang Li/Dong Yu Interspeech语音研究 | 北京与雷德蒙德署名；RT03S Fisher单遍WER27.4%→18.5%，仅限指定基准 | 15 |
| 2011 | Seide/Gang Li/Xie Chen/Dong Yu ASRU特征工程 | 声学变换及适配重要，不能只归因于网络层数 | 15 |
| 2012 | Dahl/Dong Yu/Li Deng/Acero大词汇CD-DNN-HMM | DNN声学状态后验结合HMM时序解码 | 15 |
| 2012 | Hinton/Li Deng/Dong Yu等四组团队综述 | Toronto、微软、Google、IBM多团队研究与应用进展 | 15 |
| 2012 | Krizhevsky/Sutskever/Hinton的NIPS论文与ILSVRC结果 | 七CNN集成Top-5测试15.3%、第二名26.2%；ReLU、GPU、增强、dropout等协同 | 00、17 |
| 2014—2015 | 序列注意力和GAN路线 | 不同问题与方法分叉 | 20—21 |
| 2014 | VGG/GoogLeNet在ILSVRC前后探索更深结构 | VGG2014预印本、2015 ICLR；Inception研究2015 CVPR正式刊出 | 18 |
| 2015 | Ioffe/Szegedy批归一化与Srivastava等Highway Networks | 训练与信息流不同路线，不应归于ResNet独家首发 | 18 |
| 2015-12-10 | He/Zhang/Ren/Sun ResNet arXiv首版，ILSVRC2015获奖 | 152层网络，竞赛3.57%为Top-5测试集成结果 | 18 |
| 2016 | ResNet CVPR正式论文与后续ECCV Identity Mappings | 训练退化的实验验证、身份捷径与后续预激活调整分开 | 18 |
| 2016 | AlphaGo论文发表 | 搜索、强化学习与神经网络协同 | 25 |
| 2017 | Transformer论文发表 | 注意力机制并非始于2017 | 22 |
| 2018 | BERT预训练论文 | GPT同代路线需补原论文核对 | 23 |
| 2020 | 语言模型规模定律研究 | 实验范围以论文条件为限 | 24 |
| 2020—2021 | AlphaFold2 CASP14与Nature论文 | 科学预测的边界不可夸大 | 26 |
| 2021—2022 | CLIP与潜扩散相关论文 | 跨模态表示、生成是不同任务 | 27 |
| 2022-11-30 | ChatGPT公开研究预览 | 产品发布事实与学术评价区分 | 28 |
| 2024-10-08 | 诺贝尔物理学奖授予Hopfield与Hinton | 回顾性评价而非单一发明者判定 | 08、30 |
| 2025-01-20 | DeepSeek-R1发布 | 厂商声明，模型评估需独立复核 | 29—30 |
| 2026-11-09 | 本专题初版策划截点 | 不对未核实的2026新事件下结论 | 30—31 |
