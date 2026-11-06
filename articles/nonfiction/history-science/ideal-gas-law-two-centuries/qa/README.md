# 独立审稿资料夹｜revision 2
本项目依照仓库合同采用**连续性核验与发展性审稿两个独立环节**；两份报告必须分别通过、版本号一致且无未解决阻断项，才能进行语言精修。

## 当前有效报告
- [连续性/史实一致性审计](continuity-report.md)：revision_count:2、PASS，检查跨章年代、人物贡献、术语、公式符号与来源追踪。
- [发展性结构审稿](developmental-review.md)：revision_count:2、PASS，独立检查17篇主线、读者承诺、重复叙述、证据边界与问题兑现。
- [revision-manager修订日志](revision-log.md)：rev0→rev1→rev2所有重大修复及与来源的依赖关系。
- [历史审稿记录](history/)：保存rev0和rev1报告，已失效，不可作为rev2的许可。

## 交接状态
- 当前精修稿：[../edited.md](../edited.md)，依据revision2 双PASS进入`line-edit`。
- 流程单一事实来源：[../workflow-state.json](../workflow-state.json)，其中`review_status=PASS`、`reviewed_revision=2`、`edited_revision=2`、`final_approved=false`。
- **下一阶段为`final-approval`的独立终稿审验**，当前未创建正式`final.md`或终稿批准报告，不应将此作品写为published。

独立双审结论是对当前有来源范围的文本编辑审查，不代表所有历史原始文献已逐页查证。