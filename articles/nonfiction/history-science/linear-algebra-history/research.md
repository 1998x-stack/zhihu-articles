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


## 第12—14章专项史料核证（2026-11-06）

> **审核范围**：仅第12—14章。本记录在正文之前核查历史出处、时间节点、人物贡献及现代数学重构。原典术语与现代公式分开；不替未写各章核证或宣布终稿。课文数学示例以M12/M13/M14标识，属于作者自构且应逐式验算。

### 第12章｜格拉斯曼1844：空间为什么不必三维

**文献与支持范围**

- **H12-S1** MacTutor, *Abstract linear spaces*, https://mathshistory.st-andrews.ac.uk/HistTopics/Abstract_linear_spaces/ 。1844第一版、1862重写、与莫比乌斯研究脉络、格拉斯曼的简单量与复合量、线性独立、后世接收史；Peano 1888年公理化需分开。
- **H12-S2** MacTutor, *Grassmann: 1844 foreword*, https://mathshistory.st-andrews.ac.uk/Extras/Grassmann_1844/ 。1844前言的译文文本，方向位移加法、由平行四边形得到有方向的乘积、改变因子次序会变号。仅意译并明确来源，不捏造原话。
- **H12-S3** *The Chemistry of Space: The Sources of Hermann Grassmann's Scientific Achievements*, *Annals of Science* 71(4) (2014), https://www.tandfonline.com/doi/abs/10.1080/00033790.2013.877339 。1844《扩张论》书目全称及1862版区别、回顾历史背景。
- **H12-S4** Cambridge University Press, *Die Lineale Ausdehnungslehre*, https://www.cambridge.org/core/books/die-lineale-ausdehnungslehre-ein-neuer-zweig-der-mathematik/erster-abschnitt-die-ausdehnungsgrosse/07BBC0E77301FBAF0FAE37CF6A746581 。传世德文内容的出版书目/样张，补证原著存在及结构。
- **M12** 现代外积和线性组合自证：R⁴四个基向量独立、任意非零多维线性组合；(e₁+2e₂)∧(3e₁+e₂+e₃)=-5e₁∧e₂+e₁∧e₃+2e₂∧e₃；反交换；e₁∧e₁=0。不能将wedge符号当作1844年的原著印刷。

**Claim矩阵**

| id | 主张 | 依托 | 限定 |
|---|---|---|---|
| C12-01 | 1844格拉斯曼出版《扩张论》，从空间概念中寻求更抽象的量和运算法则 | H12-S1/S2/S3 | 已核史实，非现代向量空间公理文本 |
| C12-02 | 从有向位移的加法与平行四边形有向乘积出发，前言自述改变次序伴随符号变化 | H12-S2 | 原文意译不伪造对话 |
| C12-03 | 现代高维线性组合和交错外积的教学重构有效 | M12 | 数学自证，非历史原式 |
| C12-04 | 1844书较难阅读与广泛接受，1862重新阐述，1867 Hankel后续引用 | H12-S1 | 不用“完全无人理解”绝对语 |
| C12-05 | 1888 Peano公理化真实线性空间更晚，早期Grassmann不等于现代形式公理 | H12-S1 | 史学分期 |
| C12-06 | 外积与三维叉积概念不同：外积是二向量，可用于高维，不必有欧氏度量 | H12-S1/M12 | 后世理论比较 |

### 第13章｜西尔维斯特：矩阵先有名字，还是先有理论

**文献与支持范围**

- **H13-S1** MacTutor Jeff Miller, *Earliest Known Uses of Some of the Words of Mathematics, M*, https://mathshistory.st-andrews.ac.uk/Miller/mathword/m/ 。1850年James Joseph Sylvester在*Philosophical Magazine* 37(251) 363–370的文章引入matrix，用m行n列的长方排列生成p阶行列式；1855凯莱初步研究。
- **H13-S2** MacTutor, *Matrices and determinants*, https://mathshistory.st-andrews.ac.uk/HistTopics/Matrices_and_determinants/ 。1850命名与1853凯莱逆矩阵先例、1858矩阵代数系统化；英国法律职业交往史（若提及限定为概述）。
- **H13-S3** J. J. Sylvester, *Additions to the Articles ... On Pascal's theorem*, *Philosophical Magazine* 37 (1850), https://doi.org/10.1080/14786445008646629 。期刊原始发表信息及页码，须注意现代在线发布日期不是1850首次出版日期。
- **H13-S4** Nicholas J. Higham, *Sylvester's Influence on Applied Mathematics* (2014), https://eprints.ma.man.ac.uk/2142/ 。专业数值线性代数学者回顾命名及“由长方阵中选择行列得行列式”的定义；不将PDF二手概述当原文绝对权威。
- **M13** 现代3×2矩阵[[1,2],[3,4],[5,6]]的三个2×2子式依次-2,-4,-2；矩阵本身没有方阵行列式；[[1,2],[2,4],[3,6]]全部2阶子式为0, rank=1；以rank语言为后世解释。

**Claim矩阵**

| id | 主张 | 来源 | 限定 |
|---|---|---|---|
| C13-01 | Sylvester 1850在期刊发表中命名matrix | H13-S1/S3 | 与现代在线发布日期分开 |
| C13-02 | 起初概念是长方系数阵列、抽取行列形成各阶行列式；不是全套现代矩阵代数 | H13-S1/S2 | 先有排列运用、后有名称 |
| C13-03 | 数值3×2阵列有三个2×2子式且无自身行列式 | M13 | 数学自证 |
| C13-04 | 全部2阶子式为零并不自动判断增广方程有无解；秩需配合完整系统 | M13 | 后见数学范围 |
| C13-05 | Cayley在1853已有相关逆矩阵记法、1855论文进展，1858系统论述 | H13-S1/S2 | 不写1858此前完全空白 |
| C13-06 | Sylvester/Cayley研究分别体现命名与对象化，不能当作完全不相干单向发明史 | H13-S1/S2/S4 | 历史解释 |
 
### 第14章｜凯莱1858：两次变换为什么可以相乘

**文献与支持范围**

- **H14-S1** Arthur Cayley, *A Memoir on the Theory of Matrices*, *Philosophical Transactions of the Royal Society of London* 148 (1858), 17–37, https://www.jstor.org/stable/108649 。原著出版书目；原文开篇引入线性方程组缩写、同阶矩阵作为单一对象、可加可乘及一般非交换。
- **H14-S2** Cambridge University Press, *The Collected Mathematical Papers*, “A Memoir on the Theory of Matrices”, https://www.cambridge.org/core/books/collected-mathematical-papers/memoir-on-the-theory-of-matrices/6613C9C7BE671897442278152A5C70A4 。凯莱论文重印本首页可见：1857-12-10收到、1858-01-14宣读，1858出版。
- **H14-S3** Royal Society, *Referee's report by George Boole ...*, https://makingscience.royalsociety.org/items/rr_3_55/referees-report-by-george-boole-on-three-papers-a-memoir-on-the-theory-of-matrices-a-memoir-on-the-automorphic-linar-transformation-of-a-bipartite-quadric-function-on-certain-formulae-for-differentiation-by-arthur-cayley 。1858年审稿史料，Boole支持发表矩阵论文；不得虚构两人见面或书信内心。
- **H14-S4** MacTutor, *Matrices and determinants*, https://mathshistory.st-andrews.ac.uk/HistTopics/Matrices_and_determinants/ 。1853与1855发展、1858定义加法、乘法、逆；与Sylvester早期命名联系。
- **H14-S5** Wolfram MathWorld, *Cayley–Hamilton Theorem*, https://mathworld.wolfram.com/Cayley-HamiltonTheorem.html 。1858凯莱仅给二维、三维情形演示或断言一般结果，未提供今日一般证明；第15章专门处理，不能夸大1858全阶证明。
- **M14** 现代变换自证：A=[[1,2],[0,1]],B=[[1,0],[3,1]],AB=[[7,2],[3,1]],BA=[[1,2],[3,7]]。x=(1,1)：A(Bx)=(9,4)、B(Ax)=(3,10)。I为单位元；A⁻¹=[[1,-2],[0,1]]。C=[[1,2],[0,3]]满足C²−4C+3I=0。全部为现代教学例，不冒充凯莱原题。

**Claim矩阵**

| id | 主张 | 来源 | 限定 |
|---|---|---|---|
| C14-01 | 凯莱矩阵论文1857-12-10收稿，1858-01-14宣读，1858年刊出 | H14-S1/S2 | 发表年与收稿年有别 |
| C14-02 | 论文从联立线性方程的速记与变换复合引出矩阵，把同阶矩阵视为能加、能乘的对象 | H14-S1/S2 | 现代符号另标明 |
| C14-03 | 乘法依复合顺序，AB不必等于BA，但满足结合律、单位元 | H14-S1/M14 | 精确验算 |
| C14-04 | 二阶现代示例AB、BA及行列式乘法、逆计算可检验 | M14 | 现代教学算例 |
| C14-05 | 1858论文涉及矩阵满足自身特征方程；一般n阶完整证明不能归于该论文 | H14-S1/H14-S5 | 第15章展开 |
| C14-06 | Cayley以前Sylvester已命名，Cayley也有1853、1855先行工作，不能写成1858从零发明 | H14-S4 | 历史连续性 |
| C14-07 | Royal Society保存Boole对论文的1858年审稿记录且推荐发表 | H14-S3 | 史实但不编造场景 |

**可交付结论**：第12—14章历史骨架有独立外部依据；数学推导可验算；因年代前驱、公理化和一般证明的边界已查清，可交非虚构架构与正文。仍没有正式双审及终稿批准。


## 第15—17章专项史料核证（2026-11-06）

> **阶段：fact-research / 主类型：genre-history-science / 范围：仅第15—17章。** 本节先于本批次细纲及正文编写。史实来源包括原始文献书目、历史研究与专业学会材料；M15—M17仅为另行验证的现代数学推导。**不得把后世现代记号、演示题或史学解释当作历史原著原话。** 本批尚未通过独立连续性审计、独立结构审稿或终稿批准。

### 第15章《凯莱—哈密顿：矩阵满足自己的方程吗》

**来源**

- **H15-S1｜MacTutor, Matrices and determinants**（数学史综合，https://mathshistory.st-andrews.ac.uk/HistTopics/Matrices_and_determinants/）。凯莱1858年在2×2情形证明、在3×3情形验证并声称一般成立；哈密顿1853四元数相关特殊情形；1878弗罗贝尼乌斯给出一般论证。不同数学语境与贡献不可互相抹去。
- **H15-S2｜Wolfram MathWorld, Cayley–Hamilton Theorem**（专业公式/历史核验，https://mathworld.wolfram.com/Cayley-HamiltonTheorem.html）。一般命题 p_A(A)=0；凯莱的证明范围；二维公式。
- **H15-S3｜F. G. Frobenius, Ueber lineare Substitutionen und bilineare Formen, Crelle Journal 84 (1878), 1–63**（一手论文书目，https://doi.org/10.1515/crelle-1878-18788403）。1878原始出版年，网页数字化上架的2019年**不是**当年论文发表年。
- **H15-S4｜Arthur Cayley, A Memoir on the Theory of Matrices (1858)**（一手论文，https://www.jstor.org/stable/108649）。低阶特征方程与一般性断言。
- **H15-S5｜MacTutor, Earliest Known Uses (C)**（术语及前驱，https://mathshistory.st-andrews.ac.uk/Miller/mathword/c/）。哈密顿1853四元数有关结果以及凯莱声明的一般性边界。
- **M15｜现代自证**：A=[[2,1],[0,3]], p_A(t)=t²−5t+6，A²−5A+6I=0、A⁻¹=(5I−A)/6；n阶通用证明可由 adj(tI−A) 的系数递推获得；p_A(I)=2I，故定理不是“代入任何矩阵都为零”。

| claim | 可用事实/定理 | 来源 | 证据强度与边界 |
|---|---|---|---|
| C15-01 | 1858凯莱证明低阶、表述一般；非一般完整证明 | H15-S1/S2/S4 | 学术历史，明确低阶证明/三阶核验差别 |
| C15-02 | 1853哈密顿四元数有关特殊情形，是不同的研究语言 | H15-S1/S5 | 不推称其原文就是现代全部矩阵定理 |
| C15-03 | 1878弗罗贝尼乌斯论文及一般证明 | H15-S1/S3 | 史料与出版物 |
| C15-04 | p_A(A)=0 对任意域上方阵成立，示例可验 | H15-S2/M15 | 现代数学 |
| C15-05 | 通用伴随矩阵证明需要先建立多项式恒等式，不能写det(A−A)=0为证明 | M15 | 现代证明与易错边界 |
| C15-06 | 可逆时可用特征多项式把逆变成低次多项式 | M15 | 现代推论 |
| C15-07 | 该成果把矩阵当代数对象，但不能把所有后续谱研究都归1858 | H15-S1/S2 | 史学解释 |

### 第16章《弗罗贝尼乌斯与秩：变换究竟保留什么》

**来源**

- **H16-S1｜Frobenius, Ueber lineare Substitutionen und bilineare Formen (1878)**（原著期刊书目，https://doi.org/10.1515/crelle-1878-18788403）。一手发表，原始年份1878，1–63页，讨论线性代换和双线性型。
- **H16-S2｜MacTutor, Matrices and determinants**（专业数学史，https://mathshistory.st-andrews.ac.uk/HistTopics/Matrices_and_determinants/）。1878论文涉及矩阵秩、标准形、正交性及一般凯莱—哈密顿定理；弗罗贝尼乌斯当时**并未**沿用matrix一词，1896年才了解到凯莱1858论文；1868魏尔斯特拉斯、1874克罗内克相关先例。
- **H16-S3｜Jean-Luc Dorier, A general outline of the genesis of vector space theory, Historia Mathematica 22(3) (1995), 227–261**（专业史学，https://www.sciencedirect.com/science/article/pii/S0315086085710245）。线性方程研究及几何结构研究并行汇入线性观念；秩的抽象是长期积累，不能写1878从无到有。
- **H16-S4｜MacTutor, Biographical/history discussion**（专业叙述，https://mathshistory.st-andrews.ac.uk/HistTopics/Matrices_and_determinants/）。不能混淆“矩阵秩”的1878系统定义、“nullity”的1884西尔维斯特文本及现代秩—零度定理。
- **M16｜现代自证**：A=[[1,2,0],[2,4,0],[0,0,3]]，三阶行列式0但有二阶子式3≠0，秩2；核空间span{(-2,1,0)}，像空间span{(1,2,0),(0,0,3)}。左/右乘可逆矩阵保持秩；A与B同秩不保证相似：diag(1,0)与diag(2,0)同秩不同特征值。b=(1,2,3)相容且不唯一，b=(1,3,3)不相容。

| claim | 命题 | 来源 | 限定 |
|---|---|---|---|
| C16-01 | 弗罗贝尼乌斯1878重要论文、以线性代换和双线性型为中心 | H16-S1/S2 | 史实，不强行写其当时用现代matrix术语 |
| C16-02 | 秩、分类与不变量此前已有多人先行工作 | H16-S2/S3 | 历史脉络，多人贡献 |
| C16-03 | 现代最大非零子式阶数与像维数、独立行列数一致 | M16 | 数学原理，非1878原文照排 |
| C16-04 | 满秩/亏秩与核空间、解集区别，算例回代 | M16 | 现代数学 |
| C16-05 | P A Q (P,Q可逆)秩不变；同秩不等于相似 | M16 | 现代数学，等价与相似不同 |
| C16-06 | 1884西尔维斯特nullity、1896弗罗贝尼乌斯了解凯莱研究 | H16-S2/S4 | 时间线限制 |
| C16-07 | 秩作为信息保存量与下一部特征方向形成不同问题 | H16-S3/M16 | 现代解释，非唯一历史传承 |

### 第17章《欧拉与拉格朗日：旋转物体的隐藏方向》

**来源**

- **H17-S1｜Leonhard Euler and the mechanics of rigid bodies, European Journal of Physics 38 (2017)**（2016在线发表专业回顾，https://doi.org/10.1088/0143-0807/38/1/015001）。欧拉1738—1775相关刚体力学发展，1752/1765/1776著作，惯性张量分量、主惯性轴、欧拉角与欧拉方程；**不**断言在某一日完整发明现代对称矩阵谱定理。
- **H17-S2｜1911 Encyclopaedia Britannica, Mechanics**（公版历史术语回顾，https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Mechanics）。1755 Segner主轴/永久轴早期研究，不得用“欧拉独自最先发现全部主轴”覆盖。
- **H17-S3｜Pacific Euler Archive, Découverte d'un nouveau principe de mécanique**（原著著录及历史简介，https://scholarlycommons.pacific.edu/euler-works/177/）。著作**1750年撰写、1752年刊出**，涉及刚体与后来称作惯性张量的概念；年代须区分。
- **H17-S4｜Lagrange and the secular equation, Lettera Matematica (2014)**（研究数学史，https://doi.org/10.1007/s40329-014-0051-3）。拉格朗日**1766年**关于小振动的论文；1788《分析力学》；特征方程/久期方程来自耦合微分方程，不直接等于今天矩阵记号。
- **H17-S5｜MacTutor, Lagrange Analytical Mechanics**（数学史，https://mathshistory.st-andrews.ac.uk/Extras/Lagrange_Analytical_Mechanics/）。1788《分析力学》统一广义坐标与分析力学研究，不能把拉格朗日仅当成欧拉主轴定理的简单注脚。
- **H17-S6｜MacTutor, Segner**（人物参考，https://mathshistory.st-andrews.ac.uk/Biographies/Segner/）。塞格纳的刚体研究背景。
- **M17｜现代自证**：对称惯性矩阵I=[[3,1,0],[1,3,0],[0,0,5]]，正交单位特征向量u+=(1,1,0)/√2, u−=(1,−1,0)/√2, u3=(0,0,1)，特征值4,2,5；二次型3x²+2xy+3y²+5z²=4a²+2b²+5c²（a=(x+y)/√2,b=(x−y)/√2,c=z）。对照K=[[3,−1],[−1,3]]的小振动方程q¨+Kq=0：同相(1,1)模态ω²=2，反相(1,−1)模态ω²=4。

| claim | 历史/数学 | 来源 | 保留边界 |
|---|---|---|---|
| C17-01 | 1755塞格纳关于主轴的早期研究 | H17-S2/S6 | 不写欧拉唯一首创 |
| C17-02 | 欧拉1750撰写/1752刊出、1758相关工作/1765专著的刚体力学发展 | H17-S1/S3 | 收稿、研究、印行年份分清；1758具体细节引用时收窄 |
| C17-03 | 拉格朗日1766小振动、1788《分析力学》推进特征方程研究 | H17-S4/S5 | 不冒充现代矩阵谱定理原文 |
| C17-04 | 实对称惯性矩阵主轴为正交特征向量，数值例可检验 | M17 | 现代教学 |
| C17-05 | 角动量L=Iω，非主轴方向可能不平行；动能可分解 | M17 | 现代力学表述 |
| C17-06 | 耦合振动的独立模态与频率平方特征值关系 | H17-S4/M17 | 现代重构/历史动机分开 |
| C17-07 | 正交主轴依赖实对称条件，不可把任意实矩阵都称可正交对角化 | M17 | 适用范围 |
| C17-08 | 第17章从18世纪回溯，因谱理论历史起源早于矩阵代数而非年代错误 | H17-S1/S4 | 编辑顺序声明 |

**可交付到下一阶段的证据结论**：第15—17章的叙事关键日期、论文与贡献归属有可检索的历史或专业材料支撑。数学例题已先行用独立符号计算复核，但文内仍须展示步骤。未得到资料支持的会议现场、人物引语、心理和单一首创说法一律不得写成事实。


## 第18—20章专项史料核证｜2026-11-06

**核证范围**：第五部末三章；依据可检索的原著书目、大学数学史资料、数学史研究论文及数学百科，完成具体历史主张的出处定位。原著著录不等于已逐页校勘原始法文与德文；涉及原典技术细节均以专业史学研究支持的有限措辞表达。M18—M20为独立的**现代教学演算**，不归因于历史人物。

### 第18章：柯西1829与实对称谱

- **H18-S1｜Cauchy, “Sur l'équation à l'aide de laquelle on détermine les inégalités séculaires des mouvements des planètes” (1829)**，原著在《Exercices de mathématiques》1829年卷，Cambridge原著数字化书目：https://www.cambridge.org/core/books/oeuvres-completes/sur-lequation-a-laide-de-laquelle-on-determine-les-inegalites-seculaires-des-mouvements-des-planetes/ACBB0ACB1EA7F0834C5EF84133C67950 。书目已核；不声称逐页核验法文论证。
- **H18-S2｜MAA, “Math Origins: Eigenvectors and Eigenvalues”**，https://old.maa.org/press/periodicals/convergence/math-origins-eigenvectors-and-eigenvalues 。指出1826年柯西关于二次曲面主轴的说明，以及1829年对实对称问题根为实数的直接证明；解释该问题与天体力学“久期方程”的联系。
- **H18-S3｜MacTutor, “Matrices and determinants”**，https://mathshistory.st-andrews.ac.uk/HistTopics/Matrices_and_determinants/ 。1826二次型中的 tableau、可对角化结果、与现代矩阵术语的年代区别。
- **H18-S4｜“Cauchy and the spectral theory of matrices”, Historia Mathematica (1975)**，https://www.sciencedirect.com/science/article/pii/0315086075900324 。摘要明确柯西1829为实对称矩阵特征值实性的早期一般证明，并将其置于18世纪长期前驱中。
- **H18-S5｜“Lagrange and the secular equation” (2014)**，https://doi.org/10.1007/s40329-014-0051-3 。说明柯西与拉格朗日的久期方程不是简单单线师承，且重复根问题具有史学重要性。

| claim | 说明 | 来源 | 边界 |
|---|---|---|---|
| C18-01 | 十八世纪主轴与久期方程是柯西工作之前的背景 | H18-S2/S5；第17章来源 | 不写成柯西独创全部谱思想 |
| C18-02 | 1826研究动机及1829相关论文的时间线 | H18-S1/S2/S3 | 1826说明和1829发表不混淆 |
| C18-03 | 柯西1829对对称问题实根作出关键直接论证 | H18-S2/S4 | 不称其以现代矩阵术语写出今日定理全文 |
| C18-04 | 实对称矩阵特征值实及异特征值正交 | M18 | 现代代数证明 |
| C18-05 | 二次型极值与正交对角化、重根时选基 | M18 | 实对称、有限维 |
| C18-06 | 非对称反例和复特征值反例 | M18 | 不将特殊结论推广到全部实矩阵 |
| C18-07 | 从第17章力学主轴到第19章缺陷矩阵的概念链 | H18-S2/S3、M18 | 编辑组织并非历史人物间直接传承 |

### 第19章：若尔当与标准形

- **H19-S1｜Camille Jordan, Traité des substitutions et des équations algébriques (1870)**，原著书目及“Des substitutions linéaires”目录：https://books.google.com/books/about/Trait%C3%A9_des_substitutions_et_des_%C3%A9quati.html?id=1ZQoc0-V08YC ；BnF馆藏原著影印目录：https://fr.wikisource.org/wiki/Livre:Jordan_-_Trait%C3%A9_des_substitutions_et_des_%C3%A9quations_alg%C3%A9briques,_1870.djvu 。书目及章题核实，未冒称完成原著各页译注。
- **H19-S2｜MacTutor, “Camille Jordan”**，https://mathshistory.st-andrews.ac.uk/Biographies/Jordan/ 。1870著作、线性代换标准形、最初讨论有限域情境而非今日复数域全矩阵陈述。
- **H19-S3｜MacTutor, “Matrices and determinants”**，https://mathshistory.st-andrews.ac.uk/HistTopics/Matrices_and_determinants/ 。强调1870标准形出现于素数阶有限域线性代换背景，先驱包括魏尔斯特拉斯。
- **H19-S4｜Oxford Handbook, “Algebraic generality versus arithmetic generality in the 1874 controversy between C. Jordan and L. Kronecker”**，https://academic.oup.com/edited-volume/41254/chapter-abstract/350819867 。1874围绕若尔当标准形与魏尔斯特拉斯初等因子定理的观点和一般性之争。
- **H19-S5｜1870著作当代书评（1871），Bulletin des sciences mathématiques et astronomiques**，https://www.numdam.org/item/BSMA_1871__2__161_0/ 。作为出版年/流通的额外历史著录，未用来证实全部现代定理。

| claim | 说明 | 来源 | 边界 |
|---|---|---|---|
| C19-01 | 1870《代换与代数方程论》包括线性代换与标准形 | H19-S1/S2 | 不称原书是现代矩阵教材 |
| C19-02 | 魏尔斯特拉斯及克罗内克相关工作和1874争论 | H19-S3/S4 | 不将若尔当描写为无前驱的唯一创始 |
| C19-03 | 1870最初有限域问题与今日复数域Jordan形区分 | H19-S2/S3 | 现代定理为后见整理 |
| C19-04 | 重根导致特征向量不足的3×3示例 | M19 | 现代自建矩阵 |
| C19-05 | 广义特征向量链与幂、矩阵指数 | M19 | 复域/例中实数情形 |
| C19-06 | 特征多项式相同而Jordan结构可异 | M19 | 相似不变量需更丰富 |
| C19-07 | 对称矩阵总可对角化，非对称矩阵可能不可 | M18/M19 | 两类问题不互相矛盾 |

### 第20章：积分方程、Hilbert–Schmidt理论与无限维谱

- **H20-S1｜MacTutor, “Ivar Fredholm”**，https://mathshistory.st-andrews.ac.uk/Biographies/Fredholm/ 。1903文章及其哥廷根传播、希尔伯特接受研究的时间顺序。
- **H20-S2｜MAA, “Math Origins: Eigenvectors and Eigenvalues”**，https://old.maa.org/press/periodicals/convergence/math-origins-eigenvectors-and-eigenvalues 。希尔伯特1904研究积分方程和 eigenvalue 术语的历史。
- **H20-S3｜MacTutor, “Erhard Schmidt”**，https://mathshistory.st-andrews.ac.uk/Biographies/Schmidt/ 。施密特1905博士、1907积分方程两篇研究、1908无穷多个未知量与序列空间的研究；不写Gram–Schmidt正交化为两人共同首次发明。
- **H20-S4｜Encyclopedia of Mathematics, “Integral equation with symmetric kernel”**，https://encyclopediaofmath.org/wiki/Integral_equation_with_symmetric_kernel 。希尔伯特1904、施密特1907的理论分工与实对称核。
- **H20-S5｜Springer原始论文重印汇编书目，Hilbert & Schmidt**，https://link.springer.com/book/10.1007/978-3-322-84410-1 。确认希尔伯特和施密特作品题目，未将1989重印误当研究年份。
- **H20-S6｜MacTutor, “Weyl problems”**，https://mathshistory.st-andrews.ac.uk/Extras/Weyl_problems/ 。希尔伯特最初并非采用当代公理化Hilbert空间定义；后来的谱理论比紧核问题更广。
- **M20｜现代函数分析例题**：区间[0,1]上核K(x,t)=xt的秩一自伴积分算子；单位特征函数sqrt(3)x、非零特征值1/3；核为正交补（无限维）。紧自伴算子谱定理需补充闭包、零特征空间、非零特征值的有限重数/零点聚集限制。乘法算子(Mf)(x)=xf(x)为自伴非紧反例，谱[0,1]而无特征向量。

| claim | 说明 | 来源 | 边界 |
|---|---|---|---|
| C20-01 | Fredholm 1903先驱与Hilbert1904研究关系 | H20-S1/S2 | 有更早19世纪积分方程前驱 |
| C20-02 | Hilbert1904实对称核、特征值特征函数 | H20-S2/S4 | 不能以今日抽象定理全文直接归属原文 |
| C20-03 | Schmidt1907推进、1908序列空间 | H20-S3/S4/S6 | 不单人发明完备抽象Hilbert空间 |
| C20-04 | 积分核xt与L²中的内积特征计算 | M20 | 完全现代构造 |
| C20-05 | 紧自伴谱定理的条件和本征展开 | H20-S4/M20 | 包含零空间；无限谱只可向零聚集 |
| C20-06 | 非紧自伴乘法算子具连续谱、无特征函数 | M20 | 不把一切无限维算子说成可特征展开 |
| C20-07 | 第21章公理化问题由空间结构需要引出 | H20-S3/S6 | 章节顺序为概念教学，不是历史先后 |

**增量研究交付边界**：三章已有经过专业史学资料交叉核对的主要历史框架和可在正文验证的现代推导。具体原典逐页校勘、1907论文定理形式细部仍应留待正式史学复审。任何标为“DRAFT”的章节均未经过独立双审、精修或终稿批准。
