# 看不见的秩序：PV=nRT的两百年接力

*The Invisible Order: Two Centuries Behind the Ideal Gas Law*

> 1834年，一位工程师把一条气体规律写成了 `pv=R(267+t)`。为什么这里是267，而不是今天的273.15？从一根玻璃管到无数分子的运动，这个差异恰好藏着一场跨越两百年的科学接力。

**作品性质**：历史与科学发现｜非虚构知识叙事。当前状态：**revision 2 独立双审PASS，已完成line-edit，等待final-approval（尚未封版、未发布）**。

- **读者**：具有初中到高中物理基础的普通读者；关键概念会逐层解释。
- **结构**：五部十五章、序章与尾声，总体目标约4万字，逐章可按证据与叙事节奏调整。
- **叙事主线**：观测压强与体积 → 理解温度 → 认识分子数量 → 合并为状态方程 → 解释与修正模型。
- **文风**：借鉴知乎盐选优秀知识叙事的悬念与节奏，不照搬特定作品；历史事实必须有可核查来源。

## 阅读目录

> **当前建议阅读版本**：[精修合订稿 edited.md](edited.md)（revision 2，待终审）；[审校合订稿 revised.md](revised.md)；以下17份逐章文件是保存的初稿版本。

- [序章｜267：那个不该被忽略的数字（已写初稿）](draft/00.md)
- **第一部｜空气的反抗**
  - [01｜空气有重量吗——真空问题改变了世界（已写初稿）](draft/01.md)
  - [02｜1662年，J形玻璃管里的秘密（已写初稿）](draft/02.md)
  - [03｜一条定律，为什么有两个名字（已写初稿）](draft/03.md)
- **第二部｜温度的秘密**
  - [04｜看不见的热，怎么量出空气的膨胀（已写初稿）](draft/04.md)
  - [05｜查理没有发表，盖-吕萨克发表了（已写初稿）](draft/05.md)
  - [06｜一条通向零下273度的直线（已写初稿）](draft/06.md)
- **第三部｜看不见的数量**
  - [07｜体积为什么会按整数比例结合（已写初稿）](draft/07.md)
  - [08｜1811年，阿伏伽德罗数出了看不见的东西（已写初稿）](draft/08.md)
  - [09｜1860年的会议：被重新带回来的假说（已写初稿）](draft/09.md)
- **第四部｜蒸汽机上的方程**
  - [10｜蒸汽机到底能做多少功——卡诺的追问（已写初稿）](draft/10.md)
  - [11｜1834年，克拉佩龙写下267（已写初稿）](draft/11.md)
  - [12｜一个常数，怎样成为所有气体的常数（已写初稿）](draft/12.md)
- **第五部｜完美公式的裂缝**
  - [13｜数不尽的分子，竟能导出一条简单方程（已写初稿）](draft/13.md)
  - [14｜1873年，范德瓦耳斯为理想气体补上现实（已写初稿）](draft/14.md)
  - [15｜从R到kB：五个字母的现代意义（已写初稿）](draft/15.md)
- [尾声｜从267回望：一条不完美方程的价值（已写初稿）](draft/16.md)

## 写作与研究资料

- [选题 Brief：读者承诺与三案取舍](brief.md)
- [全篇结构及章节认知推进](outline.md)
- [研究来源与证据边界](research.md)
- [主张—来源账本](claim-ledger.md)
- [修订合订稿（revision 2）](revised.md)
- [语言精修合订稿（edited.md）](edited.md)
- [连续性审计与复审报告](qa/continuity-report.md)
- [发展性结构审稿与复审报告](qa/developmental-review.md)
- [逐项修订日志](qa/revision-log.md)
- [终审前置核查：revision 2正式门禁待执行，未批准封版](qa/final-approval.md)
- [首轮未通过报告归档](qa/history/continuity-r0.md)
- [版本与审稿门禁状态](workflow-state.json)
- [序章逐条主张追踪](draft/00.claims.json)

## 本篇工作流

`topic-development → fact-research → nonfiction-architect → nonfiction-writer → continuity-audit → developmental-editor → line-edit → final-approval → publication-package`。

**当前工作流**：rev0审稿要求修订；rev1形成合订稿并经并行编辑初步双PASS，后因新增史料S87引用失效而触发独立来源复核与revision2增量修订。rev2两项报告分别PASS，已在保留主分支精修成果的基础上继续完成13处跨章衔接调整，`edited.md`保留17篇与306条主张。正式`workflow_gate.py --target final`尚未在真实工作树上执行；`final_approved=false`，`final.md`尚未生成，不能视为已发表。

> 历史表达边界：不虚构人物直接对白、私密动机、日记或“当时的一幕”；不把现代记号、摩尔定义与绝对温标倒灌给17—19世纪科学家。
