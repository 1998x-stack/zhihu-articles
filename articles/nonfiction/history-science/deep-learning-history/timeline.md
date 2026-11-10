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
| 2013-12 | Kingma/Welling VAE预印本（ICLR2014） | 变分潜变量生成，与GAN独立路线 | 21 |
| 2014-06→10 | Cho等七作者RNN Encoder–Decoder论文 | EMNLP2014短语翻译神经概率特征 | 19 |
| 2014-09→NIPS | Sutskever/Vinyals/Le深LSTM seq2seq | WMT英法BLEU34.8与33.3；候选重排36.5另设置 | 19 |
| 2014-09→2015 | Bahdanau/Cho/Bengio注意力预印本与ICLR | 解码时软对齐，不等于2017 Transformer | 20 |
| 2014 | Goodfellow等八作者GAN以及Rezende等潜变量模型 | 对抗与变分生成并行研究 | 21 |
| 2014 | VGG/GoogLeNet在ILSVRC前后探索更深结构 | VGG2014预印本、2015 ICLR；Inception研究2015 CVPR正式刊出 | 18 |
| 2015 | Ioffe/Szegedy批归一化与Srivastava等Highway Networks | 训练与信息流不同路线，不应归于ResNet独家首发 | 18 |
| 2015 | Sohl-Dickstein等扩散生成与Luong/Pham/Manning神经注意力 | 扩散前向加噪与逆向建模；global/local注意力 | 20、21 |
| 2015-12-10 | He/Zhang/Ren/Sun ResNet arXiv首版，ILSVRC2015获奖 | 152层网络，竞赛3.57%为Top-5测试集成结果 | 18 |
| 2016 | ResNet CVPR正式论文与后续ECCV Identity Mappings | 训练退化的实验验证、身份捷径与后续预激活调整分开 | 18 |
| 2015 | AlphaGo与樊麾五盘正式对局 | 原始AlphaGo 5:0，Nature论文于2016发表 | 25 |
| 2016-01→03 | Silver/Huang等Nature AlphaGo论文、对李世石五番棋 | 策略/价值网络+MCTS与人类监督/自对弈；李世石赛事4:1第四局人类获胜 | 25 |
| 2017-10 | AlphaGo Zero Nature论文 | 规则＋自我对弈＋MCTS，对已发表旧程序100:0，不是人类100盘 | 25 |
| 2017-12→2018-12 | AlphaZero预印本与Science正式论文 | 围棋/国际象棋/将棋规则已知，自我对弈与搜索协作 | 25 |
| 2017-06→NIPS | Vaswani等八作者Transformer论文 | NeurIPS正式PDF英德28.4BLEU，网页摘要版本数字有差异；并行训练不等于逐token推断并行 | 22 |
| 2019 | Song/Ermon多噪声尺度score生成 | 与扩散相邻，非GAN判别器 | 21 |
| 2018-01→07 | Howard/Ruder ULMFiT | LSTM语言模型微调迁移路线，早于/同期于Transformer语言模型研究 | 23 |
| 2018-06 | Peters等NAACL ELMo、Radford等GPT早期研究 | 双向LSTM上下文表示及Transformer生成预训练+微调是不同路线 | 23 |
| 2018-10→2019-06 | Devlin/Chang/Lee/Toutanova BERT | 2018预印本、2019 NAACL正式；MLM15%预测token、原版NSP | 23 |
| 2019-02 | GPT-2研究公布 | GPT的后续生成式模型，不是2018首版研究 | 23 |
| 2020-01 | Kaplan等十作者语言模型规模定律 | 参数、训练数据、算力与交叉熵的经验幂律；不等于普适智能定律 | 24 |
| 2020-05→NeurIPS | Brown等GPT-3 1750亿参数论文 | zero/one/few-shot文本上下文推理不更新权重；不同于2018 GPT微调 | 24 |
| 2020 | Ho/Jain/Abbeel DDPM | 去噪扩散概率模型 | 21 |
| 2018→2020-01 | CASP13旧AlphaFold参加评测与Senior等Nature论文 | 旧结构势能路线，非2020 AlphaFold2模型 | 26 |
| 2020→2021 | CASP14 AlphaFold2盲测与Jumper等Nature论文 | domain GDT_TS median92.4、Cα RMSD95 median0.96Å，不能当全蛋白正确率 | 26 |
| 2021-07 | 人类蛋白组AlphaFold预测资源及Nature论文 | 98.5%蛋白覆盖，可信残基仅58%，很高置信约36% | 26 |
| 2021 | Radford等CLIP与Jia等ALIGN分别发表于ICML | 图文双塔对比学习：CLIP约4亿、ALIGN约18亿噪声配对，各自研究 | 27 |
| 2021 | Ramesh等DALL-E初代ICML论文 | 文本与图像token自回归生成；不是CLIP匹配器 | 27 |
| 2022-04 | Ramesh等第二代DALL-E/CLIP图像潜表示 | 文本到CLIP image latent先验，扩散decoder生成图像 | 27 |
| 2022 | Rombach等CVPR潜空间扩散 | 压缩视觉latent扩散与cross-attention文本条件，另一路线 | 21、27 |
| 2022-03→NeurIPS | Hoffmann等计算最优语言模型训练研究 | Chinchilla70B/约1.4万亿tokens对照Gopher280B，同训练算力下数据与模型平衡 | 24 |
| 2022 | Rombach/Blattmann/Lorenz/Esser/Ommer潜空间扩散 | 自编码器潜空间去噪与条件生成，第21章跨年代专题 | 21 |
| 2022-11-30 | ChatGPT公开研究预览 | 产品发布事实与学术评价区分 | 28 |
| 2024-10-08 | 诺贝尔物理学奖授予Hopfield与Hinton | 回顾性评价而非单一发明者判定 | 08、30 |
| 2025-01-20 | DeepSeek-R1发布 | 厂商声明，模型评估需独立复核 | 29—30 |
| 2026-11-09 | 本专题初版策划截点 | 不对未核实的2026新事件下结论 | 30—31 |

## 第十批28—30章：专题回溯与当代证据时间轴（截止2026-11-10）

| 时间 | 原始论文、发布或研究节点 | 不可混淆的范围 | 章节 |
| --- | --- | --- | --- |
| 2017 | Christiano等偏好学习控制任务论文 | 非ChatGPT；并行于Transformer研究 | 28 |
| 2022-03 / NeurIPS | InstructGPT指令微调＋偏好奖励＋PPO | 1.3B对175B限指定人类偏好评测 | 28 |
| 2022-11-30 | ChatGPT对话研究预览官方公告 | 产品发布，不是RLHF/Transformer首次出现 | 28 |
| 2022 / 2023 | TruthfulQA ACL2022、GPT4技术报告2023、DPO NeurIPS2023 | 真相基准、后续模型与偏好算法分开 | 28 |
| 2023-07 | Meta Llama2权重及社区许可 | 附加商用许可条款，不等同OSI开源定义 | 29 |
| 2024-02 / 2024-10 | Ai2 OLMo研究开放，OSI开放AI定义1.0 | 权重、训练代码、数据信息、使用权不同维度 | 29 |
| 2024-09 / 2024-12 | Qwen2.5系列公告和DeepSeekV3技术报告 | Qwen型号许可例外，V3总671B/活跃37B与GPU小时口径 | 29 |
| 2025-01 / 2025-05 | DeepSeek R1公开与Qwen3报告 | R1-Zero/R1不同，思考/非思考模式与许可证版本 | 29—30 |
| 2022 / 2023 | FlashAttention与vLLM PagedAttention论文 | IO核心算子与KV缓存服务并行不同任务 | 30 |
| 2024-09-12 | OpenAI o1推理研究说明 | 厂商报告的测试时计算按任务条件解释 | 30 |
| 2026-01 | Nature HLE专家基准论文 | 专家考题集合，不是现实职业可靠性证明 | 30 |
| 2026-08 | 多题共享计算预算预印本 | 仅作者特定实验，仍非已独立多组核验的定理 | 30 |
