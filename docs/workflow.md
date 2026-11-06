# 分支化写作工作流 V2

中央机器契约：`workflow.json`；具体产物规范：`docs/contracts.md`；类型路由：`catalog.json`。

## 虚构写作
```text
选题（brief）→ 小说架构（outline）→ 人物/规则（story-bible）
→ 悬念账本（plot-ledger）→ 写章节（draft + chapter-state）
→ 连续性审计 → 结构审稿
                      ├─ CHANGES_REQUIRED → revision-manager → 两道复审 ─┐
                      └─ PASS → line-edit → final-approval → publication ──┘
```

## 非虚构写作
```text
选题（brief）→ 前置事实核验（research）→ 证据叙事结构（outline + claim-ledger）
→ 逐章写作（draft + claims）→ 连续性/事实审计 → 结构审稿
                         ├─ CHANGES_REQUIRED → 补核/修订 → 两道复审 ─┐
                         └─ PASS → line-edit → final-approval → publication ─┘
```

史实、新闻与科学知识绝不可为故事化而虚构。当资料不足以解释“为什么”时，用可证实的“知道什么、不知道什么”组织叙事。

## 阶段产物与职责
| Skill | 分支 | 主产物 |
|---|---|---|
| `topic-development` | both | `brief.md` |
| `fact-research` | nonfiction | `research.md` |
| `story-architect` | fiction | `outline.md` |
| `character-world` | fiction | `story-bible.md` |
| `plot-and-clues` | fiction | `plot-ledger.md` |
| `nonfiction-architect` | nonfiction | `outline.md`、`claim-ledger.md` |
| `chapter-writer` | fiction | `draft/NN.md`、`chapter-state.json` |
| `nonfiction-writer` | nonfiction | `draft/NN.md`、`draft/NN.claims.json` |
| `continuity-audit` | both | `qa/continuity-report.md` |
| `developmental-editor` | both | `qa/developmental-review.md` |
| `revision-manager` | both | `revised.md`、`qa/revision-log.md` |
| `line-edit` | both | `edited.md` |
| `final-approval` | both | `qa/final-approval.md`、`final.md` |
| `publication-package` | both | `metadata.yaml` |

## 示例调用
```text
加载 chief-narrative-editor 与 genre-history-science：
先为数学史文章执行 topic-development，形成 brief。
然后通过 fact-research 核实人物、年代与原始来源。
只根据已经核实的证据调用 nonfiction-architect 创建 outline / claim-ledger。
用 nonfiction-writer 写第一章并逐条记录引用，随后执行连续性与结构审查。
```

## 闸门命令
```bash
python scripts/workflow_gate.py articles/fiction/mystery-detective/example --target draft
python scripts/workflow_gate.py articles/fiction/mystery-detective/example --target edit
python scripts/workflow_gate.py articles/fiction/mystery-detective/example --target final
python scripts/workflow_gate.py articles/fiction/mystery-detective/example --target publish
```
命令仅检查状态和文件是否满足条件，**不替代内容审稿、事实核验和不同客户端的实际演练**。
