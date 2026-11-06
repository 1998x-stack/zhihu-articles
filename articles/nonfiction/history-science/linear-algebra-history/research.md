# 史料研究：基础参考与待核清单

> 当前只是可信来源的初步索引；**各章的关键断言尚未逐项核验**，evidence_verified=false。来源能够为某些主题提供依据，并不表示已证明所有具体人物或年代细节。

## 初步参考

- **H1** MacTutor / Matrices and determinants：https://mathshistory.st-andrews.ac.uk/HistTopics/Matrices_and_determinants/
- **H2** MacTutor / Abstract linear spaces：https://mathshistory.st-andrews.ac.uk/HistTopics/Abstract_linear_spaces/
- **H3** G. H. Moore (1995) / The axiomatization of linear algebra: 1875–1940：https://www.sciencedirect.com/science/article/pii/S0315086085710257
- **H4** MAA / Math Origins: Eigenvectors and Eigenvalues：https://old.maa.org/press/periodicals/convergence/math-origins-eigenvectors-and-eigenvalues
- **H5** G. W. Stewart (1993) / On the Early History of the Singular Value Decomposition：https://epubs.siam.org/doi/10.1137/1035134
- **H6** Golub & Uhlig (2009) / The QR algorithm: 50 years later：https://doi.org/10.1093/imanum/drp012
- **H7** Farebrother (2022) / Notes on the prehistory of principal components analysis：https://www.sciencedirect.com/science/article/pii/S0047259X21000920
- **H8** Larson / On the Histories of Linear Algebra: The Case of Linear Systems：https://sigmaa.maa.org/rume/crume2010/Archive/Larson.pdf
- **H9** Trefethen / Numerical Analysis historical essay：https://webs.um.es/eliseo/um/uploads/Main/TrefethenNAessay.pdf

## 事实分类

- A 已核事实：有可靠来源支持的人物、著作、年代、定理表述。
- B 学术解释：研究路线为何发生、受到哪些思想影响；须引用研究。
- C 尚有争议：独立发现、优先权、命名、成书和出版日期。
- D 现代重构：现代矩阵、向量、行列式符号对历史算法的解释，不得冒充原始语言。

## 重点风险

1. 古代消元与现代高斯消元法不是同一整套理论；高斯不应被称为首位消元发明人。
2. 行列式的历史早于成熟的矩阵代数；关孝和与莱布尼茨的思想应分清用途与传播。
3. 格拉斯曼、皮亚诺、韦尔、诺特、巴拿赫的不同工作互不等同，也不全是直接师承。
4. 特征值、谱、若尔当标准形、SVD和QR的结果有多位贡献者，不能写为单次发明。
5. 历史上的概念发现、后来命名、现代证明、有效数值算法往往不在同一年代。
6. 量子、PCA、网页排名、机器学习是现代应用，不是古人研究动机。

## 开始正式写作前

逐章补充一手作品或专业数学史来源；记录准确卷页／章节、数学论证及不同解释；将重大断言单列入 claim-ledger.md，明确证据强度；未查证不得声明研究阶段完成。


## 已核验专题｜第一部第一章《九章算术》卷八（2026-11-06）

**本次核验的精确范围仅为第01章核心主张**。全书其余章节仍属于尚未验证的策划目录。

| claim_id | 主张 | 来源 | 支持边界 | 状态 |
|---|---|---|---|---|
| C01-01 | 卷八首题的三组禾、总斗数与三个分数答案 | S1 | 古籍直接文本 | CONFIRMED |
| C01-02 | 卷八方程术按右、中、左排列数量，并采用倍乘和直除／消去 | S1,S2 | 古籍程序及注释 | CONFIRMED |
| C01-03 | 本书作者不详，成书阶段有学术争论，刘徽于263年完成注释 | S3,S4,S5 | 专业数学史研究 | CONFIRMED_WITH_DATE_BOUNDARY |
| C01-04 | 卷八含正负术；刘徽注解讨论正负筹算 | S1,S2 | 古籍与注解 | CONFIRMED |
| C01-05 | 古代数字列与现代增广矩阵可作数学对应，不能作史实同一 | S3,S4 | 现代数学史解释 | CONFIRMED_WITH_DISTINCTION |
| C01-06 | 现代消元推演得x=37/4,y=17/4,z=11/4，三组条件全部回代成立 | DIRECT_CALCULATION | 数学演示，非历史原文 | VERIFIED_BY_SUBSTITUTION |
| C01-07 | 原书注释体现算法为何成立的分析，不应认定古代数学只有无理由的口诀 | S2,S4 | 古籍注释与专业数学史研究 | CONFIRMED |
| C01-08 | 行列式、矩阵、秩、相容性为后续数学概念，非原书已有现代公理体系 | S3,S4 | 现代重构边界 | CONFIRMED_AS_EDITORIAL_BOUNDARY |

### 章节一手与二手来源

- S1 《九章算术》卷八“方程”第一题及方程术：https://zh.wikisource.org/wiki/九章算術
- S2 《九章算术》卷八带刘徽注文的传世文本：https://www.shidianguji.com/zh/book/NGJ892411999012434109202/chapter/1lujrqp073wvz
- S3 MacTutor, Nine Chapters on the Mathematical Art：https://mathshistory.st-andrews.ac.uk/HistTopics/Nine_chapters/
- S4 Karine Chemla, Using Documents from Ancient China to Teach Mathematical Proof (2012)：https://link.springer.com/chapter/10.1007/978-94-007-2129-6_18
- S5 Donald B. Wagner, The development of the classical Chinese algebra of polynomials (2026)：https://journals.sagepub.com/doi/full/10.1177/20966083261418725

### 数学独立验算记录

原题以现代字母表示为 3x+2y+z=39，2x+3y+z=34，x+2y+3z=26。以 3·E2−2·E1 得 5y+z=24；以 3·E3−E1 得 4y+8z=39；以 5·(4y+8z=39) −4·(5y+z=24) 得 36z=99。回代得到 x=37/4，y=17/4，z=11/4，逐项代入得39、34、26。此处为现代代数推演，不宣称与古代算筹操作细节逐字相同。

### 研究约束

- 文献版本及刘徽注、唐代注释的层次要明确，不将编辑排版转述为确切历史现场。
- 书籍成书年代并无唯一公认精确年份，“汉代前后”和“刘徽263年注释”应分别陈述。
- 第01章其他待补项为底本异文比较、各版本插图及算筹实物复原问题；不影响本章慎重限定的主张。
