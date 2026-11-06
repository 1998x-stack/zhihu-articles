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


## 第02章专题史料核验：未知数符号化（2026-11-06）

> 本条目仅核验第02章的历史主张；这不是宣布全书其他章节完成研究。资料涵盖三类不同的记号：字母简记、算筹位置系统、一般已知量和未知量的参数化；不能将其硬说成单线演进。

| claim_id | 待落实主张 | 来源编号 | 性质及可确认范围 | 本次状态 |
|---|---|---|---|---|
| C02-01 | 丢番图《算术》的未知数和幂的缩写式记法；其年代存在讨论 | N02-S1 | 史学事实及年代边界：MacTutor / Diophantus | 史学事实及年代边界 |
| C02-02 | 9世纪花拉子米以语言表述方程、分类并采用配方法，例x²+10x=39 | N02-S2,N02-S3 | 古代文本对应现代方程的解释：MacTutor传记与MAA历史数学教育研究 | 古代文本对应现代方程的解释 |
| C02-03 | 李冶《测圆海镜》1248及天元术：位置式多项式处理，天元一为未知量 | N02-S4,N02-S5 | 符号/筹式结构对应，不能直接等同字母x：学术期刊与MacTutor数学史资料 | 符号/筹式结构对应，不能直接等同字母x |
| C02-04 | 朱世杰《四元玉鉴》1303引入至多四未知量处理，天、地、人、物元 | N02-S4,N02-S5 | 四元术多变量多项式，不同于现代向量空间：学术期刊与数学史研究 | 四元术多变量多项式，不同于现代向量空间 |
| C02-05 | 罗伯特·雷科德1557年《智慧磨刀石》使用等号，传播并非立即 | N02-S6 | 首次印刷/传播的具体界限：MacTutor数学符号文献 | 首次印刷/传播的具体界限 |
| C02-06 | 韦达1591年《分析术引论》以元音表达待求量，以辅音表达已知量 | N02-S7,N02-S8 | 相当于参数运算，但受量纲齐次制约：MacTutor与SEP，含原著转引 | 相当于参数运算，但受量纲齐次制约 |
| C02-07 | 笛卡尔1637年《几何学》使用字母表后部字母代表未知量、前部字母代表已知量，扩展几何分析 | N02-S7,N02-S9 | verified_with_caveat：MacTutor与SEP，考证约定不是唯一/普遍定律 | verified_with_caveat |
| C02-08 | 2x2含参数线性方程组的消元通式及ad-bc条件 | MATH-DERIVATION | modern_reconstruction_verified：独立现代代数证明与反例 | modern_reconstruction_verified |
| C02-09 | 古中希阿及欧洲传统的贡献并行/交错，不能写成必然单线师承 | N02-S1,N02-S2,N02-S4,N02-S8,N02-S9 | editorial_interpretation：跨史料谨慎解释 | editorial_interpretation |

### 来源索引与支持范围

- **N02-S1** MacTutor: Diophantus of Alexandria（学术数学史概览）：https://mathshistory.st-andrews.ac.uk/Biographies/Diophantus/
- **N02-S2** MacTutor: Al-Khwarizmi（学术数学史概览）：https://mathshistory.st-andrews.ac.uk/Biographies/Al-Khwarizmi/
- **N02-S3** Mathematical Association of America: Algebra Tiles Explorations of al-Khwārizmī’s Equation Types（数学史与原文例题教学研究）：https://old.maa.org/press/periodicals/convergence/algebra-tiles-explorations-of-al-khw-rizm-s-equation-types-al-khw-rizm-s-compendium-on-calculating
- **N02-S4** Donald B. Wagner (2026): The development of the classical Chinese algebra of polynomials（学术期刊研究论文）：https://journals.sagepub.com/doi/10.1177/20966083261418725
- **N02-S5** MacTutor: The Jade Mirror of the four unknowns（数学史研究摘录）：https://mathshistory.st-andrews.ac.uk/Extras/Jade_mirror/
- **N02-S6** MacTutor: Earliest Uses of Symbols of Relation（数学符号史）：https://mathshistory.st-andrews.ac.uk/Miller/mathsym/relation/
- **N02-S7** MacTutor: Earliest Uses of Symbols for Variables（数学符号史）：https://mathshistory.st-andrews.ac.uk/Miller/mathsym/variables/
- **N02-S8** MacTutor: François Viète（学术数学史概览）：https://mathshistory.st-andrews.ac.uk/Biographies/Viete/
- **N02-S9** Stanford Encyclopedia of Philosophy: Descartes’ Mathematics (2025 revised)（同行评阅学术百科）：https://plato.stanford.edu/entries/descartes-mathematics/

### 不能误写的史实边界

1. 丢番图使用未知量与幂的简记，但对生活年代的传统估计存在文本学争论；其体系不具备后世任意已知参数的统一代数符号。
2. 花拉子米的《代数学》并非现代字母方程排版；“平方与十倍根为三十九”可数学翻译为 x²+10x=39。历史语境采用正量，现代负根−13不得冒充他的算术结果。
3. 宋元天元术及四元术有自身的发展路线。李冶的1248年《测圆海镜》、朱世杰1303年《四元玉鉴》均经专题研究确认；现代系数列展示须注明是说明图而非古书字面排版。
4. 雷科德1557年使用长形等号，其传播并非马上普遍；韦达1591年以大写元音与辅音区分不同性质的量，笛卡尔1637年的常用字母习惯是后来的重要规范化，不能说他们“发明了所有代数记号”。
5. 韦达重视几何量纲齐次，不能将现代代数的任意符号操作无条件投射到其1591年著作。
6. 对两元一次方程含参数的通解，当 ad-bc 不等于0才能除以它；当等于0，不能断言一定无解，还可能无穷多解。

### 数学独立验算

设 ax+by=p，cx+dy=q，则 dE1-bE2 可得 (ad-bc)x=dp-bq；aE2-cE1 可得 (ad-bc)y=aq-cp。因此当 ad-bc≠0，x=(dp-bq)/(ad-bc)，y=(aq-cp)/(ad-bc)。这只是当代数学为说明“未知量与参数一并符号化”的教学推导，**不是**韦达或笛卡尔原文中的通式。对 x²+10x=39，(x+5)²=64，x=3 或 x=−13；历史正几何量只取3。
