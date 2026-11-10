# 第六批16—18章｜独立连续性事实审计与结构审稿交接任务书

revision_count: 0
status: PENDING
scope: 16-18 working drafts
independent_review_completed: false

## 三章阅读期待的独立审查线索

- **第16章**：模型排行的数字为何值得共同相信？从2012公开竞争回溯2009 ImageNet WordNet/AMT与2010 ILSVRC，最终交付Top-1/Top-5四图示例。核验“2009数据库规模”与“2012竞赛子集”不混，人工标注角色没有虚构。
- **第17章**：以2012竞赛15.3与26.2的结果切入，但必须注明均为Top-5测试错误，前者为7 CNN集成；NeurIPS网页摘要与PDF发生数字歧义，以PDF/表2为主。技术推进要体现CNN/GPU/ReLU/数据增强/dropout/监督预训练/训练调参共同作用，不编造唯一发明者。
- **第18章**：先展示plain20和plain56的CIFAR-10训练误差反常（不是单纯测试过拟合），再给出残差身份捷径及toy梯度。保留2015 Highway网络研究、2014 VGG/Inception和2015 BN，区分2015预印本/比赛与2016CVPR正式发表。

## 独立事实审稿必须裁决

1. ImageNet2009作者六人、WordNet层级、AMT标注抽查；ILSVRC2012分类集1,281,167训练等年度表的精确引用。
2. 2012官方NeurIPS网站摘要与原始PDF不同，15.3%、26.2%以及七CNN系统必须引用同一个官方PDF版本。
3. 2015 ResNet集成Top-5测试3.57%与2016 CVPR摘要一致吗？哪一项实验证明训练退化，什么模型结构是对照？
4. 2015 Highway Networks与ResNet原论文的shortcut区别、2016 ECCV preactivation改进是否发生倒因果叙述？
5. 教学式F(x)+x以及普通/残差导数对比是否正确限定为示意；是否暗示对任何权重、网络都保证不退化？
6. 下一章语言序列/机器翻译的承接是否自然，不能将ResNet视觉胜利写成整个NLP领域突然成功的唯一原因。

**交接文件，不是实际的独立双审报告**。不得由此声称qa/continuity-report.md或qa/developmental-review.md PASS，不能生成edited/final阶段成果。
