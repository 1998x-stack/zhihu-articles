# 第七批19—21章｜独立事实/结构审稿任务书

revision_count: 0
status: PENDING
scope: 19-21 working drafts
independent_review_completed: false

## 审稿时的读者价值检验

第19章：开篇词向量求和不区分“猫追狗”和“狗追猫”，构成可计算矛盾；再从旧SMT讲到Cho七作者短语概率和Sutskever三作者深LSTM序列学习。读者须能解释变长条件概率0.8×0.5=0.4以及BLEU并非准确率。

第20章：固定上下文向量的瓶颈不是“2014所有模型必然无法翻长句”；Bahdanau预印本2014与会议2015分开、Luong2015 global/local做实验交叉证据。读者须能复算softmax的三项权重[0.5,0.25,0.25]与加权上下文0.5，不能把热图当作语义因果解释。

第21章：从“辨认图像不等于生成图像”进入GAN生成/判别的两模型博弈；VAE与diffusion为独立概率建模路线。要按2013/14→2015→2019→2020→2022准确解释建模与算力条件，不能把GAN、VAE、扩散当同一算法的 successive versions。第22章回到2017 Transformer是主动专题回溯，需明确读者不会误解年代。

## 必须由独立审稿者裁定的事实与技术问题

1. EMNLP2014 Cho等的实验用途、作者名单及NIPS2014 Sutskever论文的端到端训练、反转源序列和BLEU配置有无误差。
2. 注意力2014/15原始论文里的双向编码、软对齐和上下文向量公式与正文的现代教学表述是否正确；Luong2015和Transformer2017不能混同。
3. GAN2014八位作者和理论博弈的损失、最优判别器D=0.5的前提是否没有被过度推广。
4. Kingma/Welling VAE与Rezende等随机潜变量、Sohl-Dickstein扩散、Song/Ermon score、Ho等DDPM、Rombach等LDM是否没有被误写为直接师承。
5. 使用历史论文实验结论时是否保留具体语料、类别、指标与能力限制；任何生成图的真实感不能被用于证明图中事实确曾发生。
6. 这三章的注意力设计、期待管理、知识价值兑现、公式密度和知乎盐选式连贯问题链是否达到独立结构审稿要求。
7. 01—18旧章节PENDING状态是否没有被错误标记为通过。

**性质：这是一份独立审稿交接任务书，不是已经完成的continuity-audit或developmental-editor报告。不得据此更改review_status或创建final.md。**
