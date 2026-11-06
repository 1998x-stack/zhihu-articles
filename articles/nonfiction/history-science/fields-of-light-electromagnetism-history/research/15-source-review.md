# 第15章｜一个计算结果为什么指向了光速：来源审阅与增量核查

> 独立候审稿配套材料，不属于已通过全书workflow gate的事实核证证书。正文：[第15章](../proposals/15.md)；逐项主张：[JSON矩阵](../proposals/15.claims.json)。保留research.md、outline.md和claim-ledger.md的阶段所有权。

## 主张—来源矩阵

| 证据ID | 章节位置 | 主要断言及限定 | 对应来源 | 类型 |
|---|---|---|---|---|
| E15-01 | 一、四 | 1861-10-19 Maxwell致Faraday信比较193088与193118英里每秒 | S15-01 | 原始通信数字 |
| E15-02 | 二 | Weber Kohlrausch 1856测的是两种电学量/单位关系，不是直接电磁波速度 | S15-01、S15-07 | 科学史有界解释 |
| E15-03 | 二 | 原始电学单位关系与现代SI具有不同约定及可能的系数差异 | S15-01、S15-03 | 历史计量限制 |
| E15-04 | 三 | 麦克斯韦基于旋转涡旋与介质弹性的模型给出横向扰动速度 | S15-01、S15-03 | 1861通信及1862理论 |
| E15-05 | 四 | 193088和193118作为历史数据不得被当成现代高精度比对 | S15-01 | 测量学限定 |
| E15-06 | 五 | 1862年论文第三部分提出光与电磁扰动相联系的论证 | S15-02、S15-03 | 原始论文/书目 |
| E15-07 | 六 | 1864-10-27接收、12-08宣读、1865正式刊出Dynamical Theory | S15-04、S15-05 | 皇家学会档案 |
| E15-08 | 七 | 现代真空中Faraday与Ampere Maxwell两旋度方程推出场波动方程 | S15-06 | 现代演算 |
| E15-09 | 八 | 现代真空电磁波速c=1/sqrt(μ0 ε0)由电磁量决定 | S15-06 | 现代定律 |
| E15-10 | 九 | 光的电磁解释需超越简单速度巧合并涉及波的偏振和传播 | S15-05、S15-07 | 科学史界限 |
| E15-11 | 九 | 1861—1865的以太概念不等同于现代真空相对论解释 | S15-01、S15-05 | 历史概念界限 |

## 原始及二手来源、支持范围

- **S15-01** [Maxwell to Faraday, 19 October 1861, Epsilon Letter 4081](https://epsilon.ac.uk/view/faraday/letters/Faraday4081)。性质：编辑出版的十九世纪原始通信；支持范围和不足：193088、193118英里每秒数字，理论背景、通信原文和写信日期；不是测量误差证明。
- **S15-02** [Maxwell's Enduring Legacy bibliography](https://www.cambridge.org/core/books/abs/maxwells-enduring-legacy/references/3124D60FA2532B0FC07CB57DC07DFA3F)。性质：学术专著书目；支持范围和不足：1861—62《论物理力线》各部分刊印日期及相关页码。
- **S15-03** [Maxwell On Physical Lines of Force III DOI](https://doi.org/10.1080/14786446208643207)。性质：1862原著原刊书目；支持范围和不足：第三部分Vol23 pp12—24的刊行与静电模型、速度讨论，原数学需逐页勘误。
- **S15-04** [Royal Society PT/72/7 A Dynamical Theory](https://makingscience.royalsociety.org/items/PT_72_7)。性质：一手档案；支持范围和不足：Received Oct 27 Read Dec 8 1864、published 1865。
- **S15-05** [Smithsonian 1865 Maxwell Dynamical Theory](https://library.si.edu/digital-library/book/dynamicaltheoryo00maxw)。性质：一手文献馆藏；支持范围和不足：1865年完整原印本、光学理论专章；未全部逐页复核。
- **S15-06** [OpenStax University Physics §16.2 Plane Electromagnetic Waves](https://openstax.org/books/university-physics-volume-2/pages/16-2-plane-electromagnetic-waves)。性质：现代物理教材；支持范围和不足：在真空推导∇²E=μ0ε0∂²E/∂t²与c的SI表达，非1862原文。
- **S15-07** [IEEE Spectrum Long Road to Maxwell's Equations](https://spectrum.ieee.org/the-long-road-to-maxwells-equations)。性质：科学史专题；支持范围和不足：1861/62、1864/65、1873与后续电磁波检验时间线，非韦伯单位原始测量。

## 正式审稿前必须补核

- 1856 Weber Kohlrausch原始论文精确量纲及韦伯系数√2的换算需核查。
- 1861年书信数值与1862年期刊计算值须辨认是否相同口径。
- 皇家学会1865印本的光学小节逐页核对。
- 区别1862机械传播模型、1865动态理论与现代SI传播式。

## 本轮边界及交接

- 已按公开史料、机构文献与现代物理教材的支持范围进行增量核对；尚未对原著所有页面、归属争议、计量约定完成审校。
- 现存 workflow-state.json 的 outline_approved=false/evidence_verified=false/review_status=PENDING 应保持不变。独立候审稿写在 proposals/，不得绕过非虚构写作与审稿闸门。
- 发现史料冲突时，应返回 fact-research 并记录版本修订后重新审阅，不可直接将待核项改成已证实。
