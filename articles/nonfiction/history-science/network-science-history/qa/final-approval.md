# 《连接的真相：一部网络科学发展史》｜Revision 3 正式终审准入裁定

- 裁定日期：2026-11-10
- 当前稿件版本：revision 3
- 仓库基线：`main@6abbc677b789c0516387f76bae4b0a8ce7ef7e6f`
- 裁定范围：34篇研究性初稿及对应claims、书目进度、工作流和既有QA；抽查原始学术来源和关键数学史口径
- **终审结论：NOT APPROVED — CHANGES_REQUIRED（退修后复审）**
- **正式机器工作流原状态：PENDING；不得把本文件视为已通过独立双审**
- 执行者身份：本次AI编辑性准入审核；不是两名彼此独立的事实/结构审稿人签批
- 终稿输出：**不生成 `final.md`；不修改 `workflow-state.json`、`book.json`、`chapter-state.json`、任何正文或出版元数据**

## 一、审定权限与版本纪律

依据仓库 `AGENTS.md`、`docs/contracts.md`、`docs/workflow.md`、`.agents/skills/final-approval/SKILL.md` 与 `workflow.json`：

1. `final-approval` 的正向准入须以**当前同一修订版**的事实/连续性审核、独立结构审稿均PASS，且 `edited.md` 已按版本完成为前提。
2. 现有 `qa/continuity-report.md` 与 `qa/developmental-review.md` 的 `revision_count=0`；它们是历史问题单，并非revision3独立复审。
3. `workflow-state.json`：`current_revision=3`、`outline_approved=false`、`evidence_verified=false`、`review_status=PENDING`、`reviewed_revision=null`、`edited_revision=null`、`final_approved=false`。这些字段不得为完成审批而强制改写。
4. 当前作品目录未见可供本阶段使用的 `edited.md` 及 `final.md`。对未满足准入条件的内容出具**否决与整改意见**，不能封版。

本文件的 `CHANGES_REQUIRED` 是本次**终审准入裁定**，不冒充 `workflow-state.json` 中已经完成的两个独立审稿结论。此前P0“9篇缺稿”已于revision3关闭；旧报告相关陈述已过时。

## 二、实际检查范围和量化结果

逐份读取并检查 `draft/00.md`—`draft/33.md` 与34份 `NN.claims.json`，使用 **claim ID文本是否可在对应正文中直接检索到** 作为最低追溯性检查，不把检索命中当成引证准确。

- 全部规划：**34篇**，分别为序章00、第01—32章、尾声33。
- 有实质正文及章级主张文件：**34/34**；规划占位：**0**；`book.json` 所有章节仍为 `draft`，没有正式 `final`。
- 主张总数：**347**；正文可直接检索的ID：**128**；缺ID：**219**。
- 第01—19章共**218**条主张缺正文显式ID；第24章 **NS-24-09** 缺正文ID。其他已登记ID在正文中均可找到字符串，但尚未逐条完成事实与来源页码核验。
- 第01章 `claims.json` 仍使用 `id/claim/status`，相较其他章常用 `claim_id/statement/verification_status` 为旧schema。旧数据不能无损默认为独立审校通过。

### 章节追溯矩阵（含当前稿态，不是质量评分）

| 章节 | 正文ID命中/主张 | 章节 | 正文ID命中/主张 | 章节 | 正文ID命中/主张 |
|---|---:|---|---:|---|---:|
| 00 | 9/9 | 01 | 0/9 | 02 | 0/8 |
| 03 | 0/8 | 04 | 0/10 | 05 | 0/11 |
| 06 | 0/11 | 07 | 0/13 | 08 | 0/11 |
| 09 | 0/9 | 10 | 0/12 | 11 | 0/12 |
| 12 | 0/12 | 13 | 0/13 | 14 | 0/12 |
| 15 | 0/13 | 16 | 0/15 | 17 | 0/12 |
| 18 | 0/13 | 19 | 0/14 | 20 | 9/9 |
| 21 | 7/7 | 22 | 8/8 | 23 | 8/8 |
| 24 | 8/9 | 25 | 8/8 | 26 | 9/9 |
| 27 | 9/9 | 28 | 8/8 | 29 | 8/8 |
| 30 | 8/8 | 31 | 11/11 | 32 | 9/9 |
| 33 | 9/9 | **合计** | **128/347** |  |  |

## 三、有限范围的一手文献对照

以下是**本次重新核对的样本**，不是347条史实全部源检：

| 章节 / 问题 | 核查入口 | 样本判定 |
|---|---|---|
| 01、00、33：Euler E53的年份 | [Euler Archive E53](https://scholarlycommons.pacific.edu/euler-works/53/) 与 [Eneström目录](https://eulerarchive.maa.org/resources/enestrom/Enestrom_Index.pdf) | 1735年写作、1736卷年、1741年发表需要区分；目前相关稿件已作限定 |
| 07：Travers–Milgram实验的基数 | [Sociometry 1969原文扫描](https://www.cs.cornell.edu/courses/cs6241/2019sp/readings/Travers-1969-smallworld.pdf)，摘要及RESULTS | 296名起始者、217人实际传递、64条完成，完成链平均5.2位中间人；第07章此处基本相符 |
| 11、00：Watts–Strogatz 1998模型 | [Nature原文页面](https://www.nature.com/articles/30918) | WS模型采用重连，序章加边教学例子不能冒充原文算法；稿件已提示区分，后续仍须复算 |
| 13：Clauset等2009对幂律的检验 | [SIAM Review期刊目录](https://epubs.siam.org/toc/siread/51/4)、[论文原文](https://snap.stanford.edu/class/cs224w-readings/clauset09powerlaw.pdf) | 原研究考察24份数据；“17份未拒绝”不是证实17份皆遵循幂律，正文目前保留了此边界 |

**限制说明**：原始来源版本、每条claim的locator与原文句子、教材性质的构造示例及全部数学计算，仍缺独立全量核证。不能由以上四项抽样得出全书核证通过结论。

## 四、阻断项及明确验收条件

### BLOCKER FA-R3-B01｜版本不匹配，缺同版独立双审

- **证据**：只有revision0的 `qa/continuity-report.md`、`qa/developmental-review.md`；revision3没有两名独立审稿人对本版全文的事实/结构PASS。
- **退回**：`continuity-audit` 与 `developmental-editor` 阶段，必须在证据修复后的**同一版本**出具新的可复核意见；因实际改稿而增加revision时，旧结果失效。
- **关闭阈值**：事实审计和结构审稿各有独立结论、冲突定位、来源支持、明确版本；两份均PASS且无阻断项。

### BLOCKER FA-R3-B02｜大纲与事实授权尚未取得

- **证据**：`outline_approved=false`、`evidence_verified=false`。
- **退回**：`fact-research` / `nonfiction-architect` 和主编质量门禁。
- **关闭阈值**：关键原刊/版本、实验数字、数学条件按claim落点核证，明确完成真实审批；不得只根据文件存在更改布尔值。

### BLOCKER FA-R3-B03｜还没有合法精修稿

- **证据**：`edited_revision=null`，作品目录未见 `edited.md`。
- **退回**：只有上述真实双审完成后，才可启用 `line-edit`。
- **关闭阈值**：精修稿完整、且标记的 `edited_revision=current_revision`；事实/数学不得在此阶段偷改。

### HIGH FA-R3-H01｜219条主张失去正文一跳定位

- **位置**：01—19章共218条，以及24章 `NS-24-09`。
- **处理**：将主张ID绑定至真正承载论断的段落，并逐条查证其 `source_ids`、`locator`、原始结论与现代解释分层；不要在章节结尾集中堆砌219个ID冒充逐段追溯。
- **关闭阈值**：347/347正文有语义准确的锚点，新增检测脚本也通过，且由审核人确认与原句匹配。

### HIGH FA-R3-H02｜claims schema与核验强度不一致

- **位置**：`draft/01.claims.json`。
- **处理**：保守迁移字段，保留旧 `status` 的真实含义；`verified_at_source_level`、`excluded_from_historical_claims` 等不能一概转换为“independent_verified”。
- **关闭阈值**：全34份claims均可稳定被同一提取器解析，状态迁移有记录且不抬高事实核验级别。

### HIGH FA-R3-H03｜跨部模型假设及教学例子待全量复算

- **高风险范围**：05—06随机图大分量/全连通；07/14/25成功链/导航/时间可达；11—13小世界/增长机制/幂律拟合；20—23 SIR、SIS、阈值级联、相位同步；24 HITS/PageRank转移矩阵归一化；26—28多层、高阶、同质性与因果；29—32预测评测、图嵌入、GNN可表达性与干预。
- **处理**：记录“原刊命题 / 现代数学回译 / 作者构造算例 / 现实数据推断”四种证据身份，分别检查参数、单位、适用范围、分母和计算。
- **关闭阈值**：数学复算和主要来源页码具有独立复核记录，不出现用教学例子冒充历史观察或用相关性冒充因果。

### MEDIUM FA-R3-M01｜章节承接和分部边界

- **位置**：第25章的“下一部真正的难题”一节标题，虽然25章已是第六部首章；04与09章中心性论述存在可优化重复；第五部跨年代回溯需让读者明确是问题序而非单线师承。
- **处理**：由修订流程建议把25章节标题改作“本部的下一道难题”，04侧重指标意涵，09侧重标准化/图级集中化；保留必要的年代跳转说明。
- **关闭阈值**：分部导航和正文互相吻合，删除重复而不删除关键适用条件。

## 五、审定结论及下一阶段

**不予封版、退回修订（CHANGES_REQUIRED）**。已承认revision3完成**34/34篇工作初稿**，但不能批准**34/34篇终稿**。同时：

- 不生成 `final.md`，不将任何章节由 `draft` 擅改为 `final`。
- 不将任何现有审核闸门改为PASS或 `true`。
- 不将GitHub Pages可读性等同于知乎平台发表、出版许可或独立审稿。
- 本文件仅登记本轮审定的**拒绝理由及后续放行门槛**，不能作为 `review-passed` 或 `finalize --confirm` 的依据。

**建议顺序**：P1正文锚点与第01章schema修复 → 原始文献/数学逐项复核 → 事实与结构双审（同版）→ 语言精修 → 再次运行final-approval。P1整改导致内容修订时按 `revision-manager` 明确递增版本并让旧审核失效，避免将本轮拒绝记录包装成下轮批准。
