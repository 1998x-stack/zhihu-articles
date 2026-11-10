# 第29章｜《规范对称性：一个数学自由度怎么变成理论原则》独立候审来源审阅

> 正文：[proposals/29.md](../proposals/29.md)；[逐项主张矩阵](../proposals/29.claims.json)。本文件为**候审阶段的部分证据审阅**，并未启动或通过正式双审。

## 一、审查范围与证据强度

以可定位的原论文出版社目录、科研机构记录、诺贝尔讲演、同行评议科学史/现代理论综述为入口，区分直接史实、科学史解释、现代公式及跨章叙事推断。初步匹配**不等于**原刊原语逐页核实或独立物理数学专家批准。

## 二、主张—来源映射

| ID | 正文节 | 事实/解释/公式 | 来源 | 证据类型 |
|---|---|---|---|---|
| E29-01 | 一、二 | 电磁势的规范变换A'=A+∇χ与Φ'=Φ−∂tχ保留同一E和B | S29-01 | 现代理论演算 |
| E29-02 | 二 | B=∇×A与E=−∇Φ−∂tA是现代SI的电磁势表达 | S29-01 | 现代公式 |
| E29-03 | 三 | 洛伦茨规范历史归属应区分Ludvig Lorenz与Hendrik Lorentz | S29-01 | 科学史/命名 |
| E29-04 | 四 | 1918 Weyl原始规范设想涉及长度尺度，不等于后来量子相位 | S29-01、S29-02 | 科学史纠误 |
| E29-05 | 五 | 1926 Fock工作建立电磁势变化与量子波函数相位协变的关系 | S29-01 | 原始贡献归属 |
| E29-06 | 五 | Weyl 1929进一步确立量子相位的规范不变原理 | S29-01 | 科学史 |
| E29-07 | 五、六 | 局域相位变化使普通微分出现多余∇θ项，协变导数可抵消 | S29-01 | 现代理论推导 |
| E29-08 | 六 | ψ'=exp(iqχ/ℏ)ψ与D=∇−iqA/ℏ、Dt=∂t+iqΦ/ℏ自洽 | S29-01 | 现代SI公式 |
| E29-09 | 七 | 局域规范冗余不等于势单点数值本身可直接测量 | S29-01、S29-02 | 概念边界 |
| E29-10 | 七 | Aharonov Bohm量子相位结果为更晚历史，闭合路径相位可与磁通有关 | S29-03 | 现代效应/年代 |
| E29-11 | 八 | Yang Mills论文1954年10月1日发表于Physical Review96 191 | S29-04 | 原刊书目 |
| E29-12 | 八 | 1954 Yang Mills讨论同位旋的局域化及非阿贝尔规范结构，而非完成电弱标准模型 | S29-04、S29-05 | 科学史 |
| E29-13 | 九 | 现代SU(2)非阿贝尔规范场强含交换子项并引致基本规范自耦合 | S29-04 | 现代场论公式 |
| E29-14 | 六、十 | 局域规范不变性并不能单独证明自然界必有对应的力或全部场内容 | S29-02、S29-04 | 理论推断 |
| E29-15 | 十 | 质量生成和重整化问题仍须1960—1970年代后续理论处理 | S29-05 | 跨章历史 |

## 三、来源目录

- **S29-01** [Jackson Okun 2001 Historical roots of gauge invariance](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.73.663)：同行评议历史综述。用途：经典电磁势规范、L. Lorenz与H. Lorentz、Fock 1926/Weyl1929/Yang Mills1954。
- **S29-02** [Stanford Encyclopedia of Philosophy Gauge Theories](https://plato.stanford.edu/entries/gauge-theories/)：学术哲学历史综述。用途：1918 Weyl尺度规范与量子相位理论发展；条目须检查版本。
- **S29-03** [APS News Aharonov Bohm history](https://www.aps.org/apsnews/2009/08/august-1959-aharonov-bohm-effect)：学会历史文章。用途：1959年后量子相位及规范势整体作用；链接和先行史仍待查。
- **S29-04** [Yang Mills Phys Rev 96 191 (1954)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.96.191)：1954原始研究出版社入口。用途：同位旋局域规范、非阿贝尔规范场与非线性。
- **S29-05** [Nobel 1979 Physics press release](https://www.nobelprize.org/prizes/physics/1979/press-release/)：诺贝尔机构史料。用途：杨—米尔斯与电弱理论的历史承接。

## 四、阻断项与待核清单

- [ ] Weyl 1918原文与Einstein针对尺度规范提出的精确反驳应查原函件
- [ ] Fock 1926贡献与Schrödinger/Klein及Weyl 1929先后顺序更细核对
- [ ] 关于Aharonov-Bohm 1959先行研究的多作者署名/实验接受史仍需严谨版本
- [ ] 场强非阿贝尔交换子公式需固定生成元、耦合及符号约定；当前正文已说明自然单位
- [ ] 关于Lorenz规范历史的中文姓名译法应全书统一
- [ ] SEP Gauge Theories条目版次和具体支持段落核对

## 五、科学写作边界与衔接

本章跨时代回溯规范势：十九世纪电磁势、1918 Weyl尺度、1926 Fock相位、1929 Weyl量子规范和1954 Yang–Mills，明确这些贡献并非同一时刻一次完成，且规范自由度本身不是可直接观察的力。

**流转状态：本批稿件位于 `proposals/29.md`，`draft/29.md`、`book.json` 和 `workflow-state.json` 保留既有策划/未审批状态。来源未完全逐页核实，不得标记 `evidence_verified=true` 或 `review_status=PASS`。**
