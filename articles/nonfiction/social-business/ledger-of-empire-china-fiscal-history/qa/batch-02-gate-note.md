# 第二批工序说明

本批按照仓库的 `topic-development → fact-research → nonfiction-architect → nonfiction-writer` 非虚构路线，沿既定系列Brief而非重复选题；主类型为 `genre-social-business`，辅以历史知识叙事规范。

- 原书《何以帝国》EPUB限用于作者观点对照，不上传原书或复制原文；章06、07、08与 B04—B06 对应。
- 通过浏览器核读秦汉传世史书、博物馆来源、国家社科基金成果报告、学术文章和出版社摘要；使用 DOI 与书目只界定证据支持范围，不装作读完无法取得的全文。
- 05—08研究性正文各有主张 JSON；`batch-02-source-ledger.csv` 维护出处、年份、范围及读取层级。
- 05及08单章节叙事、研究范围已做预检；第06、07章身份税和年代争议做了防断言限制。
- 由于未进行不同审核者的独立双审，不写/覆盖 `qa/continuity-report.md`、`qa/developmental-review.md`，也不生成 `edited.md` 或 `final.md`。
- 项目 `workflow-state.json` 的 `evidence_verified` 与 `outline_approved` 继续只表示**第01—08章研究性写作范围的限定前置条件**，第09—45章及序尾章仍不能开始确定性正文。
- GitHub 连接器流程下未运行仓库 `workflow_gate.py` 本机闸门；以源映射与结构校验脚本做本批机械检验，不冒称实机 gate PASS。
