# 质量闸门（尚未实施审核）

**当前：**第一至三批01—12研究性初稿已写，第13—45及序尾仍占位。第一批未经独立双审，没有终稿，不生成虚假的 `qa/continuity-report.md`、`qa/developmental-review.md`、`edited.md`、`final.md`。

## 执行顺序

1. 事实研究：章级证据、日期、名称、统计口径、争议和替代解释。
2. 叙事架构：审定 `outline.md`、`claim-ledger.md`，批准进入非虚构正文。
3. 正文：`nonfiction-writer` 撰写并对应 `draft/NN.claims.json`。
4. **独立双审**：`continuity-audit` 查跨章时间和术语；`developmental-editor` 查结构、推理、节奏和证据支撑。
5. 若不通过，`revision-manager` 修订并重新双审；然后 `line-edit` 与 `final-approval`。

### 需重点防范

- 把“税商”写成历史上某一税种的原生名称。
- “税轻=人民富”“国库钱多=国家安全”“商税高=宋朝必富”的跳跃。
- 用财政单因解释秦亡、隋亡、宋亡、明亡。
- 将不同朝代价格、人口、两银与税负直接比较。
- 将作者观点、制度条文、执行实况与现代解释混在一起。
- 1912年以后章节没有独立公开来源仍写成已核实事实。

## 状态说明

`workflow-state.json` 中 `outline_approved=true`、`evidence_verified=true`（**仅01—12章的限定证据范围**）、`review_status=PENDING`、`final_approved=false`；计划文件存在不代表写作闸门已经通过。

## 第二批（05—08）非独立预检

- [时间线、因果与术语预检](batch-02-continuity-precheck.md)（不是正式continuity-audit报告）
- [结构、解释深度与证据预检](batch-02-developmental-precheck.md)（不是正式developmental-editor报告）
- [工序及未获批准事项](batch-02-gate-note.md)

正式独立双审尚未执行，质量状态维持PENDING，不写正式`final.md`。

## 第三批（09—12）独立双审前资料

- [第三批连续性预检](batch-03-continuity-precheck.md)：检出会议记载、东汉度田、曹魏屯田、北魏均田的时间与概念边界。
- [第三批结构预检](batch-03-developmental-precheck.md)：四章各自故事承诺与下一章因果交接。
- [第三批流程说明](batch-03-gate-note.md)：有限研究来源、预检不等于正式审稿或机器闸门PASS。

**保留`review_status=PENDING`和`final_approved=false`。** 不生成无人正式确认的`continuity-report.md`、`developmental-review.md`或`final.md`。
