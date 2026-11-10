# 第九批25—27章：作者侧数学、事实范围与连续性自查

revision_count: 0
status: PENDING
scope: 25-27 working drafts
independent_review_completed: false

> 本文件是作者自检，**不是独立continuity-audit / developmental-editor的PASS报告**，不得变更全书review_status或生成final.md/发布包。

## 可复核的数学演算

| 章节 | 自造教学算例 | 结果 | 正确解释 |
| --- | --- | --- | --- |
| 25 | 先验p=[0.6,0.3,0.1]；后续搜索访问N=[10,30,10] | 访问分布π=[0.2,0.6,0.2] | 搜索可改变最终行动偏好，但访问次数本身纯假设，非真实MCTS输出 |
| 25 | 分支为100、深度为5的固定搜索树示意 | 100^5=10^10 | 非围棋实际合法棋谱数量、非计算完整游戏状态数 |
| 26 | 三对已对齐坐标偏差1/2/3Å | RMSD=√(14/3)≈2.160247Å | 不含最优结构叠合，不能混入CASP14 RMSD₉₅ |
| 27 | 单位向量图v=(1,0)，猫t1=(0.8,0.6)，车t2=(0,1) | cosine=[0.8,0] | 只说明相似度的一个假设数值 |
| 27 | 仅两候选、温度τ=1的softmax(0.8,0) | P猫≈0.689974、P车≈0.310026 | 不是现实校准概率或论文准确率，候选文本变化会重算 |

## 三章不可混用的年份、比赛与论文口径

1. AlphaGo 2015樊麾5:0（2016 Nature公布）；2016年3月李世石4:1（第4局李世石赢）；2017 AlphaGo Zero论文的100:0是对先前发表的旧AlphaGo**程序**；2018 AlphaZero Science论文进一步跨国际象棋/将棋/围棋。
2. 原始2016 AlphaGo策略网络与价值网络，加人类棋谱监督、强化学习和MCTS；2017 Zero去掉高手棋谱监督而仍遵循围棋规则并使用搜索、算力。不可混称“无规则/无搜索”。
3. CASP13 2018旧AlphaFold→Nature2020 Senior等；CASP14 2020新AlphaFold2→Nature2021 Jumper等。GDT_TS=92.4是结构域中位分数而非92.4%蛋白完全正确；Cα RMSD₉₅=0.96Å是特定覆盖与结构对齐的中位距离误差。
4. 2021人类蛋白质组98.5%的蛋白预测覆盖≠58%残基达到confidence≠36%残基very high confidence。2024数据库超过2.14亿预测结构不能倒灌2020的CASP测试阶段。
5. CLIP 2021 ICML十二作者四亿图文对的图像/文本双塔匹配，ALIGN同期十作者约18亿噪声alt-text图文对是独立研究；CLIP自身不等于文生图生成器。
6. 第一代DALL-E2021是文本与图像tokens的Transformer自回归生成，DALL-E2 2022为CLIP latent prior+diffusion decoder，Rombach等LDM2022是压缩视觉潜空间的条件扩散；各自论文、团队与训练目标不得合并。
7. 24章2022模型规模研究→25章专题回到2016 AlphaGo→26章CASP14/AlphaFold2→27章2021图文对齐及2022生成，28章另一条对话系统主线须单独核证。章节顺序不是一条严格发明因果链。

## 正式独立审稿仍需办理

- 对AlphaGo Nature2016的训练阶段、搜索算法、胜率/棋力对照与AlphaGo Zero Nature2017的100:0具体条件，逐页双重审校。
- 对AlphaFold2 Nature2021与独立CASP14评价中“structure domains、RMSD_95、GDT_TS、confidence”精确分母与对齐程序核查；EBI后续数据库FAQ不应当作2020当时已验证功能。
- 对2021 CLIP/ALIGN、第一代DALL-E、2022 DALL-E2与LDM论文的训练数据来源、对比/生成模型结构、零样本协议和评价边界分别核查。
- 盐选叙事要求：检查三篇是否有真实矛盾、可验证来源、示例与机制、限制条件、下一章钩子；不得以拟人心理和虚构现场补充历史。
- 全书已有01—24章待审，新增三章不得令此前任何结论自动PASS。

**状态**：作者数学及结构一致性自查完成；所有独立事实/结构审稿PENDING，final_approved=false。
