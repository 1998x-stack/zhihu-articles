# 全书首轮审校修订队列｜从发现问题到复审验收

created_at: 2026-11-10
source_revision: 0
review_status: CHANGES_REQUIRED
independent_review_completed: false

> 此表是将[事实连续性报告](continuity-report.md)与[结构编辑报告](developmental-review.md)转成执行任务，不是修改已经完成的证明。编辑阶段仍不获准发布。

## 首批修订优先级

| 顺序 | ID | 等级 | 责任阶段/文件 | 完成定义 |
| --- | --- | --- | --- | --- |
| 1 | FA-001 | BLOCKER | nonfiction-architect → claim-ledger.md；nonfiction-writer → draft/14.claims.json | 修复C14-07数学公式中的管道字符，ledger列数正确；source_ids为AUTHOR_DERIVATION、σ计算正确；增加字段合法性校验 |
| 2 | FA-003 | HIGH | nonfiction-writer/主编schema → draft/01—03.claims.json | 统一review_status/independent_reviewed，保留旧字段审计轨迹，所有32篇JSON schema一致 |
| 3 | FA-004 | HIGH | 主编/目录维护 → outline.md、claim-ledger.md、book.json | 古老阶段“未写/待核”陈述明确标为历史快照或替换，01/02/04/06的TO_VERIFY按真实研究范围更新 |
| 4 | FA-002 | HIGH | fact-research → nonfiction-writer/source map | 审核14个正文编号与claims不对称、反向映射差异、06章AUTHOR_PROOF语义；高风险断言有段落和原始来源定位 |
| 5 | FA-006 | HIGH | fact-research → research.md/claims | 优先逐页核对04/05/07/09/10/11/15/17/19/24/26/28/29/30章原始文献和模型版本；记录证据层级及未决项 |
| 6 | ED-001 | HIGH | developmental-editor建议→revision-manager修稿 | 00/16/17/31重复讲解2012数字压缩，21/27生成模型、24/30算力和28/31可靠性重复减少 |
| 7 | ED-002 | MEDIUM | revision-manager/line-edit准备 | 减少连续问句和“并不意味着”；每部有不同真实史实入口，保留防夸大但移走多余工作流元信息 |
| 8 | ED-004 | MEDIUM | 主编/目录 | 标清10→11、21→22、24→25的专题回溯，避免故事顺序被误读为历史直接因果 |
| 9 | ED-003 | MEDIUM | fact-research/结构编辑 | 增加有原文支持的研究选择与竞争路径，不编造人物心理或现场 |
| 10 | ED-005 | MEDIUM | 主编/发布准备 | 统一读者脚注和工作流警示层；正式版本才调整稿头标记，保留每个关键断言来源 |

## 分批修订以避免全书一次性改坏

**R1：源数据和工作流**：FA-001/003/004，补测试，生成新revision并重新核对来源链（不动历史主张的情况下仍需要状态复审）。

**R2：事实深入复核**：以01—10、11—20、21—31三个阅读阶段逐批核查原文；每章给出claim→source→原文段落与指标分母证据，未核内容谨慎收缩。

**R3：全书结构改写**：先00/16/17/31四篇，再20/22、21/27、24/30、28/31交叉对照；改动前后分别记录章节阅读承诺和删减位置。

**R4：新版本独立双重复审**：针对修订后的revision运行continuity-audit和developmental-editor两套新的审稿报告；只有两者均真实PASS且无blocking issues，才交line-edit和final-approval。

## 绝对不能自动晋级

- 稿件存在32篇不等于已审定32篇。
- 已创建两份报告不等于已经由独立专家核对166份原始文献。
- 本队列描述完成定义不代表任一行已完成；须由revision-manager记录改前/改后、事实依据与复审。
- 任何严重事实修改都应重新评估相关后继章节的因果和引文。
