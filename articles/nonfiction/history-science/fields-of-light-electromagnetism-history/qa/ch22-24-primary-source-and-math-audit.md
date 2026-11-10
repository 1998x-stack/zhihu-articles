# 第22—24章｜1887原始观测、1905论文归属与电磁场变换专项审计

> **审阅范围**：合并后的 PR [#61](https://github.com/1998x-stack/zhihu-articles/pull/61) 所提交的 \`proposals/22.md\`、\`23.md\`、\`24.md\` 与对应 \`*.claims.json\`。参考后续 PR #63 仅用于确认跨章衔接，不在本报告内审其量子论章节。
>
> **审查形式**：基于可访问的一手论文/经过原刊校对的转写、二手史学研究、现代大学讲义及独立代数推导的**专项复核**；不是外部第三方同行评审，也不是仓库正式 \`continuity-audit\` + \`developmental-editor\` 双审。
>
> **版本**：\`workflow-state.json.current_revision=0\`；正式 \`outline_approved=false\`、\`evidence_verified=false\`、\`review_status=PENDING\`。本文的编辑结论 **CHANGES_REQUIRED（专项建议）**，不自动更改上述状态、\`draft/\`、\`book.json\` 或任何正式审稿报告。
>
> **结论摘要**：第22章的干涉仪平方项推导与原刊0.4条纹数量级正确；第23章时钟同步和洛伦兹变换表达符合现代教材；第24章 \(\mathbf E,\mathbf B\) 变换方向、正负号、两个不变量及例子经独立验算正确。**仍需修订历史精度和公式可复算性**，特别是1887年记录的平均层级、1905年论文确实提及“探测地球相对光媒介运动失败”的事实、爱因斯坦1905年已经推出电磁分量变换、以及四维方程没有明确给出统一的 \`F\` 张量约定。

## 一、1887年原始实验记录的证据等级

### 可以落实为确证的事实

1. 原始发表记录：Michelson & Morley, *American Journal of Science*, third series, **34** (203), **333–345** (1887)，[期刊书目和DOI](https://ajsonline.org/article/62505-on-the-relative-motion-of-the-earth-and-the-luminiferous-ether)，[按原刊扫描核过的完整转写](https://onepagepapers.com/michelson-morley/read/)。
2. 1881年首轮方案曾**忽略垂直光臂的运动校正**；1887年作者明确承认，洛伦兹已指出这一点，使预期效应减半，且初次实验接近误差范围；新仪器采用石台—水银浮托及多次反射延长光程。应在第22章研究动机中恢复这条具体因果，而非仅称“改进了装置”。
3. 1887年发表的观察表：仪器刻有16个方位标记，约6分钟旋转一周；对每个方位取**六次旋转的读数平均**；白天观察日期为7月8、9、11日，傍晚为7月8、9、12日。原刊显示 **noon** 与 **P.M.** 两组表、以及图6的观察曲线。第22章不宜称之为每一次逐点未经处理的“原始读数”。[原论文转写：观察程序和两组表](https://onepagepapers.com/michelson-morley/read/)。
4. 原论文使用 \(D\approx11\,\mathrm m\)、约 \(2\times10^7\) 个黄光波长，给出旋转条纹预测约 **0.4 fringe**。观察位移判断为不大于约 **0.01 fringe** 的量级；作者表述为肯定不到预期的 **1/20**、很可能不到 **1/40**。这些是**作者在所选模型与观察条件下的判断**，不是今天直接给出的严格统计置信区间。
5. 1982年 M. A. Handschy 在 *American Journal of Physics* 50(11), 987 起的 [重新分析](https://muj.optol.cz/~richterek/data/media/ref_str/handschy1982.pdf) 说明：发表的数值是经过平均的数据，未见更早逐圈未简化读数留存；作者原文对长期漂移的消除方法没有完全解释。Handschy 重新处理后仍支持原实验的“未检出预期以太风效应”结论，但**不能因此把1887年未提供的逐圈原始记录说成现在仍可逐项重建**。

### 数学复算（M22-01：通过）

在特定静止以太、刚性双臂、单程有效长度 \(L\)、\(v\ll c\)、忽略高于二阶项的简化模型下：

\[
t_\parallel=\frac L{c-v}+\frac L{c+v}\simeq\frac{2L}{c}\left(1+\frac{v^2}{c^2}\right),
\]
\[
t_\perp=\frac{2L}{\sqrt{c^2-v^2}}\simeq\frac{2L}{c}\left(1+\frac{v^2}{2c^2}\right).
\]

旋转90°使两臂角色交换，预计总条纹位移量级：
\[
\Delta N\simeq\frac{2L}{\lambda}\frac{v^2}{c^2}.
\]

以 \(L=11\,\mathrm m\)、\(\lambda=550\,\mathrm{nm}\)、\(v/c=10^{-4}\) 代入，\(\Delta N=0.40\) 条纹，吻合原论文报告的数量级。这只是**模型预测**，并不直接证明绝对静止以太存在。

### 章22需办

| ID | 严重度 | 对应主张/位置 | 问题和修订动作 |
|---|---|---|---|
| H22-01 | **HIGH** | E22-02/E22-06/E22-07，第五节 | 明确“发表数据是按每方向六次旋转平均后的表和图6”，并区分观测结果、作者对漂移的处理与后来重分析；不得称未留存的逐圈读数已被复核。 |
| H22-02 | **MEDIUM** | E22-01/E22-05，第四、五节 | 增补1881年垂直臂校正被遗漏、1887年理论预期调整的史实。 |
| H22-03 | **MEDIUM** | E22-06/E22-08，第五、六节 | “0.4、0.01、1/20、1/40”分别标注为理论预计、观测相关位移量级与作者界限判断；不要包装成现代统计置信限。 |
| H22-04 | **MEDIUM** | E22-08，第六至八节 | 补一句地球轨道速度估计忽略了当时未确定的太阳系运动分量及时间取样问题；原刊提及后续按季重复的设想。 |

## 二、1905年论文和历史贡献的精确归属

### 原刊落实的事实

- Einstein, [*Zur Elektrodynamik bewegter Körper*](https://onlinelibrary.wiley.com/doi/10.1002/andp.19053221004)，*Annalen der Physik* **17**, **891–921** (1905)，1905年6月30日收稿，9月26日发表；[德国原文校对转写](https://onepagepapers.com/einstein-electrodynamics/read/)、[牛津物理系保存的英文译本](https://users.physics.ox.ac.uk/~rtaylor/teaching/specrel.pdf)。
- 原论文引言的第一个例子确实是**磁铁和导体相对运动的电磁解释不对称**。但下一段也**明确提到了探测地球相对“光媒介”运动的失败尝试**；这不是完全没有谈运动光学实验。原论文**没有在此直接点名Michelson–Morley实验或将其指认为唯一原因**。
- 原论文第1节讨论异地钟同步；第3节给出惯性系间坐标变换；第6节（Maxwell–Hertz方程的变换）**已经直接推导电场与磁场分量随相对运动混合的关系**。不能把“电磁分量可以相互混合”写成闵可夫斯基1908年才第一次得出的结论。闵可夫斯基后续的关键贡献包括将其整理进显式的四维时空几何和协变张量表述。
- 洛伦兹（包括1895的局部时间与1904的理论修订）、庞加莱（相对性原理与局部时间/同步解释等）都在1905年前有独立研究；**存在相关先行成果**与**爱因斯坦个人是否实际阅读、采用了哪些成果**是不同的史学断言。须把“发表先后”与“思想影响”分开。参见 [Darrigol 2000章节摘要](https://academic.oup.com/book/52864/chapter-abstract/421895998)及[庞加莱专题研究摘要](https://academic.oup.com/book/43798/chapter-abstract/370736067)。

### 数学复算（M23-01：通过）

在 \(S'\) 相对 \(S\) 沿 \(+x\) 方向匀速 \(v\)，同源同时、惯性系条件下，标准现代写法
\[
x'=\gamma(x-vt),\quad t'=\gamma(t-vx/c^2),\quad\gamma=(1-v^2/c^2)^{-1/2}
\]
成立。因此对 \(\Delta t=0\) 且 \(\Delta x\ne0\) 的空间分离事件，\(\Delta t'=-\gamma v\Delta x/c^2\)；\(\Delta t=\gamma\Delta\tau\) 与 \(L=L_0/\gamma\) 也须明确各自测量系与同刻条件。第23章已作了这些限定，未见致命公式错误。

### 章23需办

| ID | 严重度 | 对应主张/位置 | 问题和修订动作 |
|---|---|---|---|
| H23-01 | **HIGH** | E23-01/E23-11，第一、八节；与章22互引 | 建议精确改为：“1905论文以磁铁—导体不对称开头，随后提及探测地球相对光媒介运动的失败尝试，但未在引言中以迈克耳孙—莫雷为具名或唯一原因。”原文现有“并非从干涉仪曲线起笔”不算错，**但未补这一层容易误读**。 |
| H23-02 | **HIGH** | E23-03/E23-13，第三、九节 | 洛伦兹、庞加莱各自的具体文章、理论含义及出版先后需作为“已发表”事实核实；不得由作品存在直接推出爱因斯坦的个人阅读史或把三人理论解释视为等价。 |
| H23-03 | **MEDIUM** | E23-12，第二、九节 | 建议第24章开篇交接时点明：1905年已出现电磁分量变换，1907—1908年新发展主要是显式四维几何/张量的组织方式。 |

## 三、第24章电磁场公式的独立验算

### 约定先行（M24-01：通过，M24-02：需补说明）

取 \(x^\mu=(ct,x,y,z)\)，度规 \(\eta=\mathrm{diag}(+1,-1,-1,-1)\)，\(S'\) 相对 \(S\) 沿 \(+x\) 速度 \(v\) 运动，坐标变换 \(x'=\gamma(x-vt)\)。采用现代真空SI制：

\[
\mathbf E'_\parallel=\mathbf E_\parallel,\qquad
\mathbf E'_\perp=\gamma(\mathbf E_\perp+\mathbf v\times\mathbf B),
\]
\[
\mathbf B'_\parallel=\mathbf B_\parallel,\qquad
\mathbf B'_\perp=\gamma\left(\mathbf B_\perp-\frac{\mathbf v\times\mathbf E}{c^2}\right).
\]

上述**正负号经独立张量变换复核正确**，亦与 MIT 8.033 2024年 Lecture 11 [PDF第7—8页、公式(11.33)—(11.38)](https://web.mit.edu/sahughes/www/8.033/lec11.pdf) 一致。注意不同参考系相对速度符号取反时，叉乘项也必须相应改变。

对 \(\mathbf E=(0,E_y,0),\mathbf B=0,\mathbf v=(v,0,0)\)：
\[
E'_y=\gamma E_y,\quad B'_z=-\gamma vE_y/c^2.
\]
所以第24章第5节的**示例方向和负号均正确**。

### 不变量检验（M24-03：通过）

用上述同一变换，代数展开得到：
\[
(\mathbf E')^2-c^2(\mathbf B')^2=\mathbf E^2-c^2\mathbf B^2,\quad
\mathbf E'\cdot\mathbf B'=\mathbf E\cdot\mathbf B.
\]

做一组可复算的数值测试：\(E_y=10\,\mathrm{V/m},\ B=0,\ v=0.8c\)，则 \(\gamma=5/3\)，\(E'_y\approx16.666667\,\mathrm{V/m}\)，\(B'_z\approx-4.44752127\times10^{-8}\,\mathrm T\)。由此 \(E'^2-c^2B'^2=100\,(\mathrm{V/m})^2\)，且 \(\mathbf E'\cdot\mathbf B'=0\)，与原系相同。独立符号化计算对一般 \((E_x,E_y,E_z,B_x,B_y,B_z)\) 的差值均化简为零。

### 协变方程的必要补注（M24-04：**HIGH 修订项**）

正文第八节给出 \(\partial_\mu F^{\mu\nu}=\mu_0J^\nu\)，却没有展示具体 \(F^{\mu\nu}\) 约定。该公式**可以正确**，但对不同度规、协变/逆变索引和张量整体号数，会有不同的右端符号；只写“依符号约定”不足以让读者复算。

建议紧邻方程给出一套**自洽定义**（以下为建议插文，非1908年原作排印）：

\[
J^\mu=(c\rho,\mathbf J),\quad
F^{\mu\nu}=
\begin{pmatrix}
0&-E_x/c&-E_y/c&-E_z/c\\
E_x/c&0&-B_z&B_y\\
E_y/c&B_z&0&-B_x\\
E_z/c&-B_y&B_x&0
\end{pmatrix}.
\]

规定 \(\partial_\mu=(c^{-1}\partial_t,\partial_x,\partial_y,\partial_z)\)。此时 \(\nu=0\) 分量正好是 \(\nabla\cdot\mathbf E=\rho/\epsilon_0\)；\(\nu=i\) 给出 \(\nabla\times\mathbf B-\mu_0\epsilon_0\partial_t\mathbf E=\mu_0\mathbf J\)，因而与第16章真空SI麦克斯韦方程严格一致。无源磁场及法拉第定律还须另外用反对称恒等式表达，**单独这一个四维方程不代表所有四条麦克斯韦方程已经写完**。

### 年代与归属（H24-01：**HIGH 修订项**）

可明确核对的顺序是：
- **1905年**：爱因斯坦原论文第6节已经写出电磁场分量的惯性系变换（旧符号/单位制）。
- **1907年11月5日**：闵可夫斯基在哥廷根作“相对性原理”讲演（其完整文本后来才发表）。
- **1907年12月21日**：向哥廷根学会提交/报告 *Die Grundgleichungen ...*；**1908年**以该年卷刊出（见[哥廷根原刊扫描](https://gdz.sub.uni-goettingen.de/download/pdf/PPN252457811_1908/PPN252457811_1908.pdf)及[原文转写](https://de.wikisource.org/wiki/Die_Grundgleichungen_f%C3%BCr_die_elektromagnetischen_Vorg%C3%A4nge_in_bewegten_K%C3%B6rpern)）。
- **1908年9月21日**：在科隆作《空间与时间》讲演，**1909年**刊出。可参见 [Pérez、Ferreirós、de Paz (2026)](https://link.springer.com/article/10.1140/epjh/s13129-026-00124-2)。

因此可说“四维表述更透明”，但不宜叙述成“先有闵可夫斯基，后人才发现运动观察者会把电场和磁场混合”。

### 章24需办

| ID | 严重度 | 对应主张/位置 | 问题和修订动作 |
|---|---|---|---|
| H24-01 | **HIGH** | E24-01/E24-02/E24-12，第一、二、八节 | 在正文点名爱因斯坦1905原论文§6的电磁分量变换，区分“已有分量变换”与“1907—1908显式四维组织”的贡献。 |
| M24-04 | **HIGH** | E24-12，第八节 | 四维公式旁明确 \(x^\mu,\eta,J^\mu,F^{\mu\nu},\partial_\mu\)；至少验证 \(\nu=0\) 和空间分量，不能单独给无约定的方程。 |
| H24-02 | **MEDIUM** | E24-02/E24-03，第二节 | 区分1907讲演、1908刊出和1908演讲、1909刊出，避免把讲演年份当全文发表年份。 |
| M24-05 | **LOW** | E24-09/E24-10，第七节 | 两个场不变量可加一句“真空经典场、洛伦兹变换下的局域场值”；波的 \(E=cB\) 限定在**理想真空平面波**。原文基本已有正确限定。 |

## 四、提交给修订者的最小执行清单

1. **先修文字归属**：章22补原始数据平均层级及1881修正；章23补1905论文确实提及失败的“光媒介”运动探测；章24标明1905已有电磁分量变换。
2. **再修公式可复算性**：章24增加完整张量/度规/相对速度方向约定及两条麦克斯韦分量回代；章22图表注明预期0.4、相关位移约0.01与1/20、1/40的不同含义。
3. **补强来源矩阵**：关联E22-02/05/06/07/08、E23-01/03/11/12/13、E24-01/02/03/06/07/09/12，增列1887原表、1982重分析、爱因斯坦1905 §6、闵可夫斯基1908原刊和MIT讲义(11.33—11.38)的精确位置。
4. **保留闸门**：由\`revision-manager\`形成有版本记录的修订后，才讨论下一轮正式 \`continuity-audit\` 与 \`developmental-editor\`；不能因为本专项数学PASS而把任何章晋级\`final\`。

## 五、已完成/未完成的真实性边界

- **完成**：1887年期刊书目、经过原刊校对的观察表与图6文字、16方向/六旋转程序、论文作者数值断言核对；与1982学术重分析交叉比较；爱因斯坦1905引言、§1/§3/§6的原语言转写与英文译文对照；闵可夫斯基1907/1908/1909关键时间核对；第22—24章主要公式的独立代数及数值验算。
- **尚未完成**：1887年所有逐圈实验手记（1982研究指出无法作为留存原始记录重建）；原刊高清各页的逐字版面鉴真；洛伦兹与庞加莱全部先行原文逐篇比勘；外部物理学史专家与理论物理学家双人签核。
- **编辑判定**：**专项复核：CHANGES_REQUIRED**；数学分量变换/不变量**通过**，历史归属和张量约定**待改**。这不是项目正式终审结论。

## 主要外部资料入口

- [Michelson–Morley 1887 期刊目录与DOI](https://ajsonline.org/article/62505-on-the-relative-motion-of-the-earth-and-the-luminiferous-ether) · [原论文逐页转写与表](https://onepagepapers.com/michelson-morley/read/)。
- [M. A. Handschy (1982), *Re-examination of the 1887 Michelson–Morley experiment*](https://muj.optol.cz/~richterek/data/media/ref_str/handschy1982.pdf)。
- [Einstein 1905 原论文书目](https://onlinelibrary.wiley.com/doi/10.1002/andp.19053221004) · [原德文完整转写](https://onepagepapers.com/einstein-electrodynamics/read/) · [英文译本](https://users.physics.ox.ac.uk/~rtaylor/teaching/specrel.pdf)。
- [Minkowski 1908 哥廷根原刊](https://de.wikisource.org/wiki/Die_Grundgleichungen_f%C3%BCr_die_elektromagnetischen_Vorg%C3%A4nge_in_bewegten_K%C3%B6rpern) · [2026年史学研究](https://link.springer.com/article/10.1140/epjh/s13129-026-00124-2)。
- [MIT 8.033 2024 Lecture 11，场张量与变换式](https://web.mit.edu/sahughes/www/8.033/lec11.pdf)。
