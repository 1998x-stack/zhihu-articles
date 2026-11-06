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


## 第03章专题证据记录（2026-11-06）

主题：《高斯之前已有消元：谁把方程排成阶梯》。仅对本章明示的主张做逐项来源核验；全书其他章不得据此继承“已核”状态。

### 依据资料
- **L03-S1** J. J. O'Connor & E. F. Robertson, Matrices and determinants, MacTutor。史学概览，卷八筹式以及后续算法。https://mathshistory.st-andrews.ac.uk/HistTopics/Matrices_and_determinants/
- **L03-S2** Joseph F. Grcar, How ordinary elimination became Gaussian elimination, Historia Mathematica 38 (2011) 163–218。专业史学论文，命名演变/牛顿/高斯。https://doi.org/10.1016/j.hm.2010.06.003
- **L03-S3** Christoph Börgers, Introduction to Numerical Linear Algebra, Chapter 3 (SIAM 2022)。数值线性代数教材的历史边界。https://epubs.siam.org/doi/10.1137/1.9781611976922.ch3
- **L03-S4** 《九章算术》卷八 方程术（传世古籍）。一手传世文本，列式与消元。https://zh.wikisource.org/wiki/九章算術

### 可引用主张
| claim_id | 主张 | 依据 | 范围 | 状态 |
|---|---|---|---|---|
| C03-01 | 卷八方程术使用算筹列排列和相消程序，可用现代矩阵解释，但不是现代矩阵公理 | L03-S1,L03-S4 | 古籍/现代解释 | 已核，须标注转译 |
| C03-02 | 欧洲独立出现消元前驱；牛顿17世纪笔记经后人编印传播，不能说高斯首次发明 | L03-S2,L03-S3 | 专业数学史 | 已核 |
| C03-03 | 高斯在19世纪早期天文观测调整与计算中使用并改进计算记法；现代命名是在后世逐步形成 | L03-S1,L03-S2 | 专业数学史 | 已核，勿将今日名称归于高斯自命 |
| C03-04 | 现代行交换、非零倍乘和倍加操作保留解集，阶梯形与回代揭示主元、秩和相容性 | MATH03 | 现代数学证明 | 独立验算 |
| C03-05 | 零行形如0=非零表示无解；零行0=0并不意味着自动有无穷多解，还需看自由变量 | MATH03 | 逻辑反例 | 独立验算 |
| C03-06 | 精确代数消元与浮点数值稳定性不同，部分主元选取可缓解误差 | L03-S3 | 现代数值算法 | 已核，算法后续章节详讲 |

### 事实边界与本文写法
《九章算术》算筹列阵与现代增广矩阵是可比较的算法结构，而非原文使用了行运算/秩。欧洲教科书消元传统有独立形成的证据，不可构造跨文化单线传承；牛顿约1670年的笔记和后续传播日期不可混淆。现代部分选主元与数值稳定性属于后来发展的算法。


## 第04章专题证据记录（2026-11-06）

主题：《当方程互相矛盾：最小二乘如何救场》。仅对本章明示的主张做逐项来源核验；全书其他章不得据此继承“已核”状态。

### 依据资料
- **L04-S1** A.-M. Legendre, Sur la méthode des moindres quarrés (1805), in A Source Book in Mathematics, translation。原始论文片段的译本及编辑说明。https://en.wikisource.org/wiki/Page:A_Source_Book_in_Mathematics_(Smith).pdf/608
- **L04-S2** Jan R. Magnus, Gauss on least-squares and maximum-likelihood estimation, Archive for History of Exact Sciences 76 (2022)。专业研究，1805与1809及统计解释之异。https://link.springer.com/article/10.1007/s00407-022-00291-w
- **L04-S3** MacTutor, Adrien-Marie Legendre。数学史人物、彗星轨道与争议。https://mathshistory.st-andrews.ac.uk/Biographies/Legendre/
- **L04-S4** Joseph F. Grcar, How ordinary elimination became Gaussian elimination, Historia Mathematica (2011)。消元/正规方程历史背景。https://doi.org/10.1016/j.hm.2010.06.003
- **L04-S5** Mathematical Association of America, Classic Topics on The History of Modern Mathematical Statistics。数学统计史出处口径，Legendre 1805 与 Gauss 1809。https://old.maa.org/node/743958

### 可引用主张
| claim_id | 主张 | 依据 | 范围 | 状态 |
|---|---|---|---|---|
| C04-01 | 真实观测常产生互相不能精确满足的超定方程，需要选择近似而非继续强制精确解 | L04-S3,L04-S4 | 史学背景/一般数学 | 已核 |
| C04-02 | 勒让德1805年先公开发表最小二乘原则，相关著作在有些书目中以1806标示 | L04-S1,L04-S2,L04-S5 | 年代优先权 | 已核，须区分出版/版本 |
| C04-03 | 高斯1809年公开论述原则并称1795年已使用；优先权争议不能当作单一可证明发明时间 | L04-S2,L04-S3 | 争议史 | 已核，采用限定措辞 |
| C04-04 | 勒让德给出最小平方调整规则而高斯在误差概率假设下论证，二者不是同一个数学前提 | L04-S2 | 专业史学论文 | 已核 |
| C04-05 | 最小化平方残差导出正规方程A^T A θ=A^T b，满列秩时唯一；数值演算独立可复验 | MATH04,L04-S4 | 现代推导 | 独立验算 |
| C04-06 | 最小二乘在现代几何中是正交投影，但不必强称早期作者已经建立现代向量空间表述 | MATH04,L04-S2 | 现代重构边界 | 已核 |
| C04-07 | 异常值、误差方差不齐、模型设错等均需要其他处理；最小二乘不是修补事实的魔法 | MATH04 | 现代方法局限 | 例证可复验 |

### 事实边界与本文写法
1805年勒让德公开表述，1809年高斯公开论证而自称1795年以来使用；不是简单的“谁偷了谁的成果”。高斯天体轨道研究与最小二乘的关系应避免把谷神星轨道成功说成其1809年证明的直接证据。正交投影/矩阵正规方程是现代教学转译，误差分布与概率假设需明确。


## 第05章专题证据记录（2026-11-06）

主题：《关孝和与莱布尼茨：两条行列式的早期道路》。仅对本章明示的主张做逐项来源核验；全书其他章不得据此继承“已核”状态。

### 依据资料
- **L05-S1** Naoki Osada, Determinants by Seki Takakazu from the group-theoretic viewpoint, Advanced Studies in Pure Mathematics 79 (2018), 83–99。专业学术论文：1683年手稿传承、n≥5算法瑕疵与后续修正。https://www.lab.twcu.ac.jp/osada/aspm79.pdf
- **L05-S2** MacTutor, Matrices and determinants。数学史概述，关孝和1683、莱布尼茨1693信件。https://mathshistory.st-andrews.ac.uk/HistTopics/Matrices_and_determinants/
- **L05-S3** MacTutor, Takakazu Seki。人物与相关史学参考。https://mathshistory.st-andrews.ac.uk/Biographies/Seki/
- **L05-S4** MAA, Brief History of Determinants (Petrilli & Smolenski)。辅证：独立发展与不同问题背景；可访问性变动。https://old.maa.org/node/915203
- **L05-S5** Mathematical determinant derivations, original worked example in draft/05.md。现代数学证明，不作为古人原始书写。internal://draft/05.md

### 可引用主张
| claim_id | 主张 | 依据 | 范围 | 状态 |
|---|---|---|---|---|
| C05-01 | 关孝和《解伏题之法》1683年再修订，通过学派手稿流传；不是可直接断言1683年公开出版 | L05-S1 | 专业论文纠正旧概述 | 已核 |
| C05-02 | 关孝和在多项式消去与兼容条件中运用行列式式组合；其高阶手法n≥5存在文献指出的错误 | L05-S1 | 专业论文含限定与后续发展 | 已核 |
| C05-03 | 莱布尼茨1693年致德洛必达信，讨论三条方程中两个未知量的相容条件，系数记号是编号而非十、十一这样的整数 | L05-S2 | 专业史学概览 | 已核 |
| C05-04 | 两条路线的用途、书写与传播不同，不能捏造直接相互影响 | L05-S1,L05-S2,L05-S4 | 历史解释 | 已核为审慎边界 |
| C05-05 | 现代det二阶式ad-bc与三阶六项展开、交换两行变号、重复行det为零 | L05-S5 | 现代数学推导 | 独立验算 |
| C05-06 | det=0对三条含两未知量的线性方程组是必要条件，若两列未知量系数不独立则未必充分 | L05-S2,L05-S5 | 历史研究+现代反例 | 独立验算 |
| C05-07 | 早期行列式思想早于成熟矩阵代数；术语与一般性质经历18—19世纪继续发展 | L05-S2 | 数学史概览 | 已核 |

### 事实边界与本文写法
特别以Osada 2018的一手史学研究纠正MacTutor/一些科普中“1683公开出版”的简化：1683《解伏题之法》再修订后经学派手稿传承；其n≥5算法存在错误，后学修正。莱布尼茨的10、11、12是双位标号而非具体十、十一、十二；他的条件对三条方程二未知量而言必须区分必要与充分。


## 第06—08章前置史料核证（2026-11-06；仅对本批三章有效）

### 第06章：克拉默与一般系数通式
- **S06-1** MacTutor, *Matrices and determinants*: https://mathshistory.st-andrews.ac.uk/HistTopics/Matrices_and_determinants/ 。1748年麦克劳林遗著含二、三元解法；1750年克拉默著作给一般的n元规则、系数排列及常数替换，但没有给出我们今天习惯的通式完整证明。
- **S06-2** MacTutor, *Gabriel Cramer*: https://mathshistory.st-andrews.ac.uk/Biographies/Cramer/ 。1750年著作的代数曲线背景。
- **S06-3** Frank J. Swetz, MAA, *Mathematical Treasure: Cramer on His Rule and His Paradox* (2019): https://old.maa.org/node/1899289 。原著和附录页码的史料线索，网站目前可能无法稳定打开。
- **S06-4** Thierry Joffredo, *A genetic analysis of Gabriel Cramer's Introduction...* (2019): https://smf.emath.fr/node/152648 。法国数学会学术文章摘要，论证1750年曲线专著的形成与出版背景。
- **C06-01** 麦克劳林1748年低阶先例，不能说1750年之前无人建立相关公式（S06-1，已核）。
- **C06-02** 克拉默1750年一般n阶规则源于曲线待定系数问题；附录描述排列及符号（S06-1/2/4，已核）。
- **C06-03** 其历史记号不等于今天的det(A_j)/det(A)，完整现代证明由本章教学补写（S06-1，限定）。
- **C06-04** 现代克拉默法则需n阶方阵det(A)≠0，且列替换行列式恒等式可独立证明（MATH06，数学核查）。
- **C06-05** 直接阶乘排列展开n!项，不是大规模数值计算首选；行消元通常三次方量级（MATH06，算法分析）。
- **C06-06** det(A)=0不等于无解，可能无穷多解或矛盾（MATH06，反例）。

### 第07章：拉普拉斯展开与出版年辨析
- **S07-1** MacTutor, *Matrices and determinants*: https://mathshistory.st-andrews.ac.uk/HistTopics/Matrices_and_determinants/ 。贝祖1764、范德蒙德1771、拉普拉斯1772相关工作、拉格朗日1773体积关联；亦指出莱布尼茨有更早扩展想法。
- **S07-2** MacTutor, *Earliest Uses of Symbols for Matrices and Vectors*: https://mathshistory.st-andrews.ac.uk/Miller/mathsym/matrices/ 。拉普拉斯1772年卷及古今符号差异。
- **S07-3** 法语Wikisource，拉普拉斯，*Recherches sur le calcul intégral et sur le système du monde*: https://fr.wikisource.org/wiki/Œuvres_complètes_de_Laplace/Recherches_sur_le_Calcul_intégral_et_sur_le_système_du_monde 。正文书目标明科学院年卷1772、实际印行1776；对出版史只作明确限定。
- **S07-4** 法国国家图书馆（BnF）书目记录: https://catalogue.bnf.fr/ark:/12148/cb30739065z 。支持该论文年卷和单行印本的版本问题。
- **C07-01** 拉普拉斯命名不意味着此前莱布尼茨、贝祖和范德蒙德完全没有展开思想（S07-1）。
- **C07-02** 1772为科学院年卷标识，1776为论文实际印行的重要日期，不能混写（S07-2/3/4）。
- **C07-03** 现代代数余子式C_ij=(-1)^(i+j)det(M_ij)，可沿任一行或列展开（MATH07）。
- **C07-04** 现代四阶教学矩阵行列式为108，按稀疏行展开更短（MATH07）。
- **C07-05** 按行余子式展开是递归组织，稠密情形逐层递归并非最优复杂度（MATH07）。
- **C07-06** 拉格朗日1773体积相关表达与当时行列式理论没有直接统一（S07-1，历史解释限定）。

### 第08章：柯西、比内与雅可比
- **S08-1** MacTutor, *Matrices and determinants*: https://mathshistory.st-andrews.ac.uk/HistTopics/Matrices_and_determinants/ 。柯西1812、比内同期、雅可比1841三篇理论研究。
- **S08-2** MacTutor, *Carl Gustav Jacob Jacobi*: https://mathshistory.st-andrews.ac.uk/Biographies/Jacobi/ 。函数行列式也在早期柯西研究中出现，雅可比1841年专门论述。
- **S08-3** MAA, *Brief History of Determinants*: https://old.maa.org/press/periodicals/convergence/analysis-and-translation-of-raffaele-rubinis-1857-application-of-the-theory-of-determinants-note-0 。柯西1812论证和1815刊印、Gauss1801术语差异及乘法定理。
- **S08-4** MacTutor, *Earliest Uses of Symbols for Matrices and Vectors*: https://mathshistory.st-andrews.ac.uk/Miller/mathsym/matrices/ 。柯西符号历史与凯莱1841竖线记号。
- **C08-01** 柯西1812综合研究、论文1815印行，乘法定理研究亦需记比内同期成果（S08-1/3，已核）。
- **C08-02** Gauss1801曾用determinant一词，但语义与今天行列式不完全相同（S08-1/3）。
- **C08-03** 雅可比1841年专著深化函数行列式，并非这一表达的绝对首创者（S08-1/2）。
- **C08-04** 现代det(AB)=det(A)det(B)二阶示例及一般证明由现代代数给出（MATH08）。
- **C08-05** 二元偏导数Jacobian局部表示有向面积因子；极坐标Jacobian=r（MATH08）。
- **C08-06** Jacobian=0不意味着映射必定局部非单射；(u,v)→(u³,v)反例成立（MATH08）。
- **C08-07** 不能把柯西1812年的工作称为1858年凯莱式完整矩阵代数（S08-1，历史限制）。

**本批前置核验证书**：以上有外部来源的具体历史主张可进入第06—08章写作；MATH06—08为需逐项公开演算的现代解释，不能当成史实。所有章节仍为未终审初稿。其他未写章节并不因本记录自动通过证据闸门。


## 第09—11章专题史料核证｜2026-11-06

**范围**：本部分章节定向核证。第09—11章的历史叙事须以本条目为上限；MATH09—11均是本次独立教学推导，非原典。不得以本批资料为第12章及之后章节颁发通过结论。

### 第10章《莫比乌斯与贝拉维蒂斯：方向也能相加吗》

**来源与用途**
- **G10-S1** MAA Mathematical Treasure: Möbius's Calculus of Centers of Gravity (2016)。https://old.maa.org/press/periodicals/convergence/mathematical-treasure-m-bius-s-calculus-of-centers-of-gravity。支持范围：1827 Möbius《重心演算》。
- **G10-S2** Cambridge Mathematical Gazette: Circles in areals (2016)。https://www.cambridge.org/core/journals/mathematical-gazette/article/abs/circles-in-areals/83BEF0FA3702B3C9CF13D33E3FC54BD7。支持范围：重心坐标、和为1归一化、负权重的平面点。
- **G10-S3** MacTutor: Abstract linear spaces。https://mathshistory.st-andrews.ac.uk/HistTopics/Abstract_linear_spaces/。支持范围：Möbius/ Bellavitis的早期有向量方法及1832年起的研究。
- **G10-S4** MacTutor: Giusto Bellavitis。https://mathshistory.st-andrews.ac.uk/Biographies/Bellavitis/。支持范围：1832起发展，1835与1837论文、同向等长平行的equipollent概念。
- **G10-S5** MAA book review: A History of Vector Analysis by Crowe。https://old.maa.org/node/105858。支持范围：主要史学著作中 Möbius、Bellavitis、Grassmann 为不同线索。

| claim_id | 具体论断 | source_ids | 类型与限制 |
|---|---|---|---|
| C10-01 | 莫比乌斯1827年《重心演算》以带权重的点研究几何；归一化重心坐标是后世表述 | G10-S1,G10-S2 | historical |
| C10-02 | 三角形的权重和为1，非负权在内部、负权允许描述外部；物理质量解释需谨慎 | G10-S2,MATH10 | historical_modern |
| C10-03 | 贝拉维蒂斯在1832年起研究相关有向线段几何，1835/1837有重要等效演算著述 | G10-S3,G10-S4 | historical_publication |
| C10-04 | 等长、平行、同向的有向线段可被视作等效，可经首尾相接相加 | G10-S3,G10-S4,MATH10 | historical_modern |
| C10-05 | 点的仿射组合需权重和1，位移向量与基点平移无关，现代数值反例已复核 | MATH10 | modern_math |
| C10-06 | 不能把这些著作直接宣称为现代向量空间公理或说其中一人单独发明向量 | G10-S3,G10-S5 | historical_caveat |

### 第11章《哈密顿：乘法为什么突然不交换》

**来源与用途**
- **G11-S1** Hamilton to John T. Graves on quaternions (Oct 17, 1843), as quoted by MacTutor。https://mathshistory.st-andrews.ac.uk/Extras/Hamilton_Graves/。支持范围：1843年早期通信与John T. Graves及Warren的思想关系。
- **G11-S2** Hamilton’s later account to son Archibald (1865), transcription。https://www.zipcon.net/~swhite/docs/math/quaternions/Hamiltons_discovery.html。支持范围：1843-10-16河岸桥的回顾记述；不是当日记录。
- **G11-S3** Library of Trinity College Dublin: Hamilton letter (1865)。https://artsandculture.google.com/story/what-is-life-trinity-college-dublin-library/vwWBBcXVXyltKQ?hl=en。支持范围：书信与纪念铭牌原始刻痕不存。
- **G11-S4** National Academies Press: Unknown Quantity, A Real and Imaginary History of Algebra。https://www.nationalacademies.org/read/11540/chapter/13。支持范围：三元乘法难题与四元数的历史数学脉络。
- **G11-S5** Oregon State University, Geometry of the Octonions, Quaternion history。https://sites.science.oregonstate.edu/physics/coursewikis/GO/book/go/qhist.html。支持范围：四元数与后续向量分析及空间旋转的区分。

| claim_id | 具体论断 | source_ids | 类型与限制 |
|---|---|---|---|
| C11-01 | 1843年10月16日哈密顿发现四元数乘法法则，并于次日与Graves通信；桥上事件据1865回顾 | G11-S1,G11-S2,G11-S3 | historical_primary_retrospective |
| C11-02 | 探索三元数时发现不易同时保持复数式乘法良好性质，四个实系数的新代数是关键突破 | G11-S1,G11-S4 | historical_interpretation |
| C11-03 | i²=j²=k²=ijk=-1，ij=k、ji=-k说明非交换；四元数乘法保留结合律 | G11-S1,G11-S4,MATH11 | math_historical |
| C11-04 | q=a+bi+cj+dk是四个实系数的代数元素，不是宣称物理空间四维，也不同于普通三维箭头 | G11-S4,G11-S5 | historical_modern |
| C11-05 | 单位四元数对纯虚四元数用v↦qvq⁻¹表示旋转，q=(1+i)/√2把j变为k | MATH11,G11-S5 | modern_math |
| C11-06 | 桥的旧刻痕不存；现地标志非1843年原始书迹；后世几何与物理应用不全属于1843年一刻 | G11-S2,G11-S3,G11-S5 | historical_caveat |
| C11-07 | 四元数旋转复合一般不交换，举例q_iq_j≠q_jq_i；非交换与非结合不同 | MATH11 | modern_math |

### 第09章《笛卡尔：让几何学开始说代数的语言》

**来源与用途**
- **G09-S1** Stanford Encyclopedia of Philosophy, Descartes' Mathematics (2025修订)。https://plato.stanford.edu/entries/descartes-mathematics/。支持范围：1637《几何学》、帕普斯轨迹问题、曲线与方程及古今差别。
- **G09-S2** SEP, Descartes’ Mathematics, historical notes。https://plato.stanford.edu/archives/win2017/entries/descartes-mathematics/notes.html。支持范围：笛卡尔因图而异的斜交坐标，非现代普适直角坐标系。
- **G09-S3** Cambridge Descartes Lexicon: Geometry (2016)。https://www.cambridge.org/core/books/abs/cambridge-descartes-lexicon/geometry/1A4CC31CA915B00F7CCC91FEABBE9A0B。支持范围：1637《方法谈》末尾附篇，几何与代数研究语境。
- **G09-S4** Library of Congress, Fermat Varia opera mathematica (1679)。https://www.loc.gov/resource/rbc.2017gen28093/?sp=3&st=list。支持范围：费马《平面和立体轨迹引论》1679收入遗著，非当时首次构想。
- **G09-S5** T. L. H., The Geometry of René Descartes, Nature (1926)。https://www.nature.com/articles/118400a0。支持范围：费马独立解析几何先驱；早期评价不能简化为唯一最早。

| claim_id | 具体论断 | source_ids | 类型与限制 |
|---|---|---|---|
| C09-01 | 1637年笛卡尔《几何学》附在《方法谈》后，研究帕普斯轨迹问题和曲线的代数关系 | G09-S1,G09-S3 | historical |
| C09-02 | 笛卡尔当时主要采用由具体问题形成的斜交度量和代数曲线法，非如今固定垂直x/y坐标轴 | G09-S1,G09-S2 | historical_caveat |
| C09-03 | 费马在1630年代发展与笛卡尔并行的解析几何思想，其相关著作收录于1679年遗著 | G09-S4,G09-S5 | historical_caveat |
| C09-04 | 焦点(0,1)、准线y=-1的抛物线推出x²=4y，是独立现代教学重构 | MATH09 | modern_example |
| C09-05 | 图形到方程和方程到轨迹并非一对一自动无约束，平方与坐标系选择引出伪解或分支问题 | MATH09 | modern_math |
| C09-06 | 把本章放于08章之后是因概念路线回溯1637年，不是按史实误置年代 | G09-S1 | editorial_interpretation |

### 三条须避免的失真链

1. **笛卡尔坐标之时代错置**：《几何学》侧重从几何关系到方程，并未以今日所有图形默认的固定正交x、y轴为标准绘图习惯；费马的独立工作及1679年出版须同时呈现。
2. **贝拉维蒂斯年份辨析**：1832年起研究与1835/1837年有代表性出版不矛盾；Möbius 1827带权重的点与Bellavitis等效有向线段是相关却不同的工具，不能硬说某人直接发明现代向量空间。
3. **哈密顿桥上故事证据边界**：1843年事件的细节主要来自他1865年回忆性书信，不能冒充同时期的现场报道；已消失的刻痕与今日纪念铭牌不是同一文物。四元数四个实分量不代表物理空间被发现有四个轴。
