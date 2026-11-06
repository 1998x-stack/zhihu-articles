# 质量闸门（尚未实施审核）

**当前：**仅规划与占位。没有实际正文，不生成虚假的 `qa/continuity-report.md`、`qa/developmental-review.md`、`edited.md`、`final.md`。

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

`workflow-state.json` 中 `outline_approved=false`、`evidence_verified=false`、`review_status=PENDING`、`final_approved=false`；计划文件存在不代表写作闸门已经通过。
