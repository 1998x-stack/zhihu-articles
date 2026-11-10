# Zhihu Articles

**面向中文原创叙事的 Agent Skills 与编辑工作流**  
*An agent-assisted editorial framework for Chinese fiction and narrative nonfiction.*

[![Validate writing framework](https://github.com/1998x-stack/zhihu-articles/actions/workflows/validate.yml/badge.svg)](https://github.com/1998x-stack/zhihu-articles/actions/workflows/validate.yml)
[![Repository](https://img.shields.io/badge/GitHub-1998x--stack%2Fzhihu--articles-24292f?logo=github)](https://github.com/1998x-stack/zhihu-articles)

> 用可追溯的创作决策代替一次性生成：**注意力设计 → 阅读期待管理 → 价值兑现**。

Zhihu Articles 是一套以 **25 个专业 Skill、10 种题材规范、虚构／非虚构双轨流程和可检查的编辑门禁** 为核心的写作工程仓库。它帮助作者和 AI Agent 共同完成选题、研究、结构设计、分章写作、修订、审稿与归档，并为每篇作品保留可复核的过程文件。

项目采用「知乎盐选式知识叙事与故事阅读体验」作为编辑方法参考，**并非知乎或盐言故事的官方项目**，不提供平台发布、流量或商业化结果保证。

**项目导航：** [快速开始](#快速开始) · [体系架构](#体系架构) · [双轨工作流](#双轨工作流) · [题材分类](#题材分类) · [质量控制](#质量控制) · [目录规范](#目录规范) · [现有作品](#现有作品) · [维护与测试](#维护与测试)

---

## 为什么需要这个项目

长篇原创写作不只是生成流畅的正文。缺少阶段约束时，AI 容易重复选题、随意改写人物设定、遗漏伏笔，或把未经核实的历史叙述写成事实。

本项目将这些问题转换为明确的工程约束：

| 设计原则 | 解决的问题 | 对应机制 |
| --- | --- | --- |
| **单一创作总控** | 多个提示词反复决策、互相覆盖 | `chief-narrative-editor` 负责路由与质量闸门 |
| **类型专业化** | 不同题材套用同一套反转和节奏模板 | 10 个 `genre-*` Skill |
| **虚构与非虚构分流** | 小说技巧污染历史、科学和调查事实 | 不同研究、架构及写作执行器 |
| **阶段产物唯一责任人** | 大纲、审稿结论和终稿被其他阶段覆盖 | `workflow.json` 与文件契约 |
| **版本化审稿闭环** | 旧版本审稿结果被误用于新稿 | 修订版本、双重审稿与状态门禁 |
| **跨代理一致性** | 同一项目在不同 Agent 中行为规则漂移 | 四份同步的 Skills 与自动化一致性测试 |

## 快速开始

### 1. 获取仓库

需要 Git 和 Python 3.11 或兼容版本，以执行项目脚本。

```bash
git clone https://github.com/1998x-stack/zhihu-articles.git
cd zhihu-articles
python scripts/validate_repo.py
```

**建议先阅读：** [AGENTS.md](AGENTS.md) · [catalog.json](catalog.json) · [workflow.json](workflow.json) · [docs/contracts.md](docs/contracts.md)。

### 2. 选择写作环境

| Agent | 项目级 Skill 目录 | 用途 |
| --- | --- | --- |
| **OpenCode** | `.opencode/skills/` | 项目中的规范维护源 |
| **Pi** | `.pi/skills/` | Pi 对应的项目副本 |
| **Codex** | `.agents/skills/` | Codex 项目级标准发现路径 |
| **兼容副本** | `.codex/skills/` | 保留的历史目录，**不是** Codex 标准自动发现路径 |

四份内容在仓库中保持字节级一致。OpenCode 和 Pi 也可能发现共享的 `.agents/skills/`，从而提示同名 Skill；这是当前保留多目录副本的已知权衡，详见 [跨代理兼容说明](docs/compatibility.md)。

**注意：** Agent 发现 `SKILL.md` 不等于自动执行整个写作流程。每个 Skill 所需的完整提示词位于同目录 `prompt.txt`，按需加载与交接应遵守 `AGENTS.md`、`workflow.json` 及对应阶段的输入输出约束。

### 3. 创建作品目录

以悬疑推理短篇为例：

```bash
cp -R articles/_template articles/fiction/mystery-detective/my-first-story
```

随后编辑新目录中的 `metadata.yaml` 和 `workflow-state.json`，确认类型、目标字数、作品状态等字段。模板只是初始结构：**占位文件不代表已完成正文或已通过审核**。

非虚构作品应放在 `articles/nonfiction/<genre>/<article-slug>/`，并将 `workflow-state.json` 的 `lane` 设置为 `nonfiction`；写作前必须完成事实与来源核查。

### 4. 向 Agent 下达分阶段任务

推荐从一个明确的任务开始，而不是要求模型在一次回复中交付全文：

```text
请先阅读 AGENTS.md、workflow.json 和 docs/contracts.md，
然后加载 chief-narrative-editor 与 genre-mystery-detective。

任务：策划一篇约 8,000 字的原创悬疑短篇。
先执行 topic-development，生成三个有实质差异的选题方案；
选定方案后进入 story-architect、character-world 与 plot-and-clues。
在完成因果链、角色知识边界和伏笔检查前，不写正文。
所有成果保存在 articles/fiction/mystery-detective/my-first-story/。
```

历史、科学和社会调查项目则应改用 `genre-history-science` 或 `genre-social-business`，并走 **`fact-research → nonfiction-architect → nonfiction-writer`**，不得将真实人物的对白、心理活动或未经核实的事件编造成事实。

## 体系架构

本仓库的 Skill 由三个层级组成：

| 层级 | 数量 | 职责 | 入口 |
| --- | ---: | --- | --- |
| **核心主编** | 1 | 冻结任务、选择分支、协调阶段、裁决质量门禁 | [chief-narrative-editor](.opencode/skills/chief-narrative-editor/SKILL.md) |
| **题材约束** | 10 | 定义各类型的叙事动力、真实性要求和专项审核标准 | [题材分类](#题材分类) |
| **阶段执行器** | 14 | 负责研究、架构、写作、修订、审稿、封版等专门任务 | [工作流契约](workflow.json) |

**Skill 资源约定：**

```text
<skill-name>/
├── SKILL.md              # 触发条件、职责边界与阶段交接
├── prompt.txt            # 当前工作流使用的专业提示词
└── prompt-original.txt   # 有历史原版时保留，不要求所有 Skill 都存在
```

主编的 **V1.0 原始完整版**保存在 [`chief-narrative-editor/prompt.txt`](.opencode/skills/chief-narrative-editor/prompt.txt)；此前精简版本单独存档为 `prompt-condensed-v1.txt`。10 个类型的原始 Prompt，以及早期故事策划／分章写作／结构审稿 Prompt，均保留独立原版，避免迭代时丢失创作规范。

## 双轨工作流

工作流由 [`workflow.json`](workflow.json) 定义，文件读写责任由 [`docs/contracts.md`](docs/contracts.md) 约束。两条分支共用最终审稿机制，但在资料组织和正文写作方法上严格分开。

### 虚构故事 · Fiction

```text
topic-development       选题定位
        ↓
story-architect         故事因果与章节架构
        ↓
character-world         人物、关系和世界规则
        ↓
plot-and-clues          悬念、知识边界与伏笔账本
        ↓
chapter-writer          分章正文 + chapter-state.json
        ↓
continuity-audit        连续性审计
        ↓
developmental-editor    结构审稿
        ↓
   ┌──── 不通过：revision-manager → 两道复审 ────┐
   └──── 通过 ───────────────────────────────────┘
        ↓
line-edit → final-approval → publication-package
```

其中，反转必须能追溯到已建立的事实或线索；主人公的行动应受到人物资源、时间线和世界规则约束。

### 知识叙事 · Narrative Nonfiction

```text
topic-development       确立研究问题
        ↓
fact-research           事先核验史料、数据与争议
        ↓
nonfiction-architect    证据支持的大纲与 claim-ledger.md
        ↓
nonfiction-writer       分章写作 + 主张来源记录
        ↓
continuity-audit        事实与概念一致性检查
        ↓
developmental-editor    独立审稿
        ↓
   ┌──── 不通过：补核 / revision-manager / 两道复审 ─┐
   └──── 通过 ───────────────────────────────────────┘
        ↓
line-edit → final-approval → publication-package
```

非虚构的首要原则是 **证据决定能写什么，叙事决定读者怎样理解它**。不能为了制造冲突而调整史实，也不能将流行轶事、作者推断或后世解释冒充原始记录。

## 题材分类

**虚构作品（Fiction）**

| 类型 | Skill | 主要叙事问题 |
| --- | --- | --- |
| 现实逆袭 | [`genre-realistic-comeback`](.opencode/skills/genre-realistic-comeback/SKILL.md) | 不公如何被可信地改变 |
| 职场博弈 | [`genre-workplace-politics`](.opencode/skills/genre-workplace-politics/SKILL.md) | 资源、授权与利益如何改变局势 |
| 家庭伦理 | [`genre-family-ethics`](.opencode/skills/genre-family-ethics/SKILL.md) | 亲情、责任与公平为何冲突 |
| 悬疑推理 | [`genre-mystery-detective`](.opencode/skills/genre-mystery-detective/SKILL.md) | 线索怎样共同解释真相 |
| 古风权谋 | [`genre-historical-intrigue`](.opencode/skills/genre-historical-intrigue/SKILL.md) | 人物怎样在制度与资源约束下破局 |
| 规则怪谈与脑洞 | [`genre-rules-fantasy`](.opencode/skills/genre-rules-fantasy/SKILL.md) | 隐藏规则是什么、如何被验证 |
| 科幻与 AI 伦理 | [`genre-ai-scifi`](.opencode/skills/genre-ai-scifi/SKILL.md) | 一种技术假设会带来什么社会后果 |
| 青春成长 | [`genre-coming-of-age`](.opencode/skills/genre-coming-of-age/SKILL.md) | 人物如何通过选择改变认知 |

**非虚构作品（Nonfiction）**

| 类型 | Skill | 主要认知问题 |
| --- | --- | --- |
| 历史与科学发现 | [`genre-history-science`](.opencode/skills/genre-history-science/SKILL.md) | 问题、方法与证据如何促成发现 |
| 社会现实与商业调查 | [`genre-social-business`](.opencode/skills/genre-social-business/SKILL.md) | 利益结构与制度机制如何解释现象 |

以上分类是**创作与归档用途**，并非知乎官方分类。作品可以有副类型，但应只有一个主归档目录；非虚构的证据要求不能被副类型的小说规则覆盖。

## 目录规范

```text
zhihu-articles/
├── .opencode/skills/                # Skill 维护源
├── .pi/skills/                      # Pi 镜像
├── .agents/skills/                  # Codex 标准发现目录
├── .codex/skills/                   # 历史兼容副本
├── articles/
│   ├── fiction/                     # 8 种虚构题材
│   ├── nonfiction/                  # 2 种非虚构题材
│   └── _template/                   # 新作品模板
├── docs/
│   ├── contracts.md                 # 文件所有权、交接规则
│   ├── workflow.md                  # 两条工作流与示例
│   └── compatibility.md             # 多代理路径与已知取舍
├── scripts/
│   ├── sync_skills.py               # 四份 Skill 同步
│   ├── validate_repo.py             # 静态结构与契约验证
│   ├── workflow_gate.py             # 生命周期门禁
│   ├── workflow_state.py            # 审核状态与修订转换
│   └── test_*.py                    # 合成样本单元测试
├── AGENTS.md                        # 跨代理操作规范
├── catalog.json                     # 类型与 Skill 注册表
├── workflow.json                    # 阶段依赖与交接契约
└── README.md
```

每篇文章独立维护自己的工作目录。主要文件约定如下：

| 文件 | 作用 |
| --- | --- |
| `brief.md` | 选题、读者、写作目标与假设 |
| `research.md` / `claim-ledger.md` | 非虚构来源、主张及证据边界 |
| `story-bible.md` / `plot-ledger.md` | 虚构人物设定、规则与伏笔 |
| `outline.md` / `draft/` | 章节结构与逐章稿件 |
| `chapter-state.json` | 虚构长稿的续写状态 |
| `qa/` | 连续性审计、结构审稿、修订和终审记录 |
| `edited.md` / `final.md` | 精修稿与已批准终稿 |
| `workflow-state.json` | 修订版本、审批状态和阻断项 |
| `metadata.yaml` | 题材、标题、摘要、标签和项目状态 |

现有文章与早期模板可能采用不同的历史格式。脚本对缺少 `workflow-state.json` 的旧作品采用**显式迁移**原则，不会把原有草稿自动升级为已审核成稿。

## 质量控制

### 四级工作流门禁

门禁由 [`workflow_gate.py`](scripts/workflow_gate.py) 检查：

| 目标 | 主要进入条件 | 检查命令 |
| --- | --- | --- |
| **Draft** | 已批准大纲及对应分支档案；非虚构证据已核验 | `--target draft` |
| **Edit** | 当轮两份审稿报告均通过、版本匹配、无未解决阻断项 | `--target edit` |
| **Final** | 满足 Edit，存在精修稿且编辑版本一致 | `--target final` |
| **Publish** | 满足 Final，且终稿与终审批准记录均存在 | `--target publish` |

示例（将 `ARTICLE` 替换成真实作品目录）：

```bash
ARTICLE=articles/fiction/mystery-detective/my-first-story

# 检查当前阶段能否推进；未满足时返回非零退出码
python scripts/workflow_gate.py "$ARTICLE" --target draft

# 经实际大纲审核后，显式更新状态
python scripts/workflow_state.py "$ARTICLE" outline-approved --confirm

# 审稿出现结构问题时，登记阻断项
python scripts/workflow_state.py "$ARTICLE" add-blocker --reason PLOT-004

# 修复并核对后关闭该问题；之后仍必须重新审稿
python scripts/workflow_state.py "$ARTICLE" resolve-blocker --reason PLOT-004 --confirm

# 开启新修订，废止旧版的审核与精修批准
python scripts/workflow_state.py "$ARTICLE" new-revision --reason "修复动机和时间线冲突"
```

`--confirm` 表示**在真实查验后进行显式确认**，不是自动判断文章质量。非虚构还需调用 `evidence-verified --confirm`；独立审稿通过后才能运行 `review-passed --confirm`，语言精修后才能进入终审封版。

**注意：** `--target publish` 仅检查是否达到项目内的发布准备条件，**不会把文章发布到知乎或任何第三方平台**。自动化门禁不能证明史料真的可靠、文字具备文学价值或作品符合外部平台要求。

### 编辑标准

采用七个维度辅助内部质量评价：开篇吸引力 15、叙事节奏 15、信息差 15、人物塑造 15、逻辑 20、情绪与思想价值 10、语言表达 10。评分是编辑工具而非平台标准；对非虚构来说，关键事实错误可直接阻断交付。


## GitHub Pages 书架注册与可阅读章节
作品在 `articles/` 下建立 `README.md` 和 `book.json` 后，网站构建器会沿 `catalog.json` 的归档路径**自动发现新系列**。已有 `site/assets/data/books.json` 保留人工定制的封面和陈列顺序，但不再需要为每个新书手工追加条目；没有 PNG 封面会显示排版式临时封面。

`book.json` 必须显式列举希望展示的 Markdown 章节及 `outline/draft/final` 状态，不会自动复制整个研究目录。每次三章一批写作需同步状态与章节导航。提交前：
```bash
python scripts/build_pages.py --check-catalog
python scripts/sync_skills.py --check
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/build_pages.py --out _site
```
缺少新系列清单将触发 CI 失败，不会静默漏收录。详细协议见 [GitHub Pages 收录与部署](docs/pages-publishing.md)。**Pages 中阅读工作初稿不代表知乎平台发表或完成独立审稿。**

## 现有作品

这些目录用于实际创作和检验长篇知识叙事方法，**作品状态以各自 `metadata.yaml` 为准**。

| 作品 | 类型 | 当前归档状态 |
| --- | --- | --- |
| [《连接的秩序：图论三百年》](articles/nonfiction/history-science/graph-theory-history/README.md) | 数学思想史 · 图论与网络发展史 · 非虚构系列 | `draft`：7部36章已规划；序章及01—18章有证据范围限定的正文初稿，19—37仍占位，独立审稿未完成 |
| [《从方程到空间：一部线性代数思想发展史》](articles/nonfiction/history-science/linear-algebra-history/README.md) | 数学思想史 · 线性代数发展史 · 非虚构系列 | `outlined`：8部32章及序章、尾声已建立策划占位，正文待写 |
| [《失去确定性：数学史上的三次危机与七次思想革命》](articles/nonfiction/history-science/the-loss-of-certainty-math-crises/README.md) | 数学思想史 · 历史科学非虚构 | `drafting`：第 01 章已有初稿，其他章节主要为结构占位 |
| [《从切线到无穷：微积分的诞生与重建》](articles/nonfiction/history-science/the-making-of-calculus/README.md) | 数学思想史 · 微积分史 · 历史科学非虚构 | `outlined`：七部35章、序章及尾声；00—34共35篇未独立审稿工作初稿，35—36共2篇占位；全书审核门禁尚未通过 |
| [《信用、债务与权力：一部世界金融史》](articles/nonfiction/social-business/credit-debt-power-global-financial-history/README.md) | 世界金融制度史 · 非虚构长篇 | `outlined`：大纲和章节占位，正文尚未完成 |
| [《看不见的秩序：PV=nRT的两百年接力》](articles/nonfiction/history-science/ideal-gas-law-two-centuries/README.md) | 气体定律发现史 · 科学非虚构长文 | `drafting`：序章已有初稿，15章与尾声为占位 |

这些项目不是已正式发布的作品，也不应将章节占位文件视为成稿。

## 维护与测试

### 修改或新增 Skill

1. 在 **`.opencode/skills/<skill>/`** 中修改 `SKILL.md` 与 `prompt.txt`；如涉及原始 Prompt，应保留 `prompt-original.txt`，避免不可逆覆盖。
2. 新增阶段需要同时更新 `catalog.json`、`workflow.json` 及相应文件所有权契约；新增题材要更新 `articles/` 下的分类目录。
3. 将维护源同步到其他 Agent 目录，再检查镜像差异。
4. 为工作流行为变化补充单元测试；提交后检查 GitHub Actions。

```bash
# 将 OpenCode 规范源同步到 Pi / Codex 目录
python scripts/sync_skills.py --write

# 不修改文件，仅检查是否同步
python scripts/sync_skills.py --check

# 检查 Skill 元数据、原始 Prompt、阶段路由、文件契约和模板
python scripts/validate_repo.py

# 执行工作流状态与门禁测试
python -m unittest discover -s scripts -p 'test_*.py' -v

# 检查脚本语法
python -m compileall -q scripts
```

项目配置了 [GitHub Actions 自动验证](.github/workflows/validate.yml)，会在 push / pull request 时执行上述静态检查和单元测试。

### 适用边界

- **它是写作工作流与资源库，而不是无人值守的全自动出版服务。**
- Skills 的实际发现、执行和多阶段交接行为可能因 Agent 客户端而异，需在所用客户端中验证。
- 事实核验需要可靠来源与明确的编辑判断；脚本只验证状态和文件契约。
- 项目不会自动上传到内容平台，也不保证外部审核、阅读量或商业收益。
- 创作内容应保持原创，尊重著作权，并区分虚构叙事、事实、证据与推断。

---

**设计目标：让每个重要段落、人物选择与知识结论都能回答一个问题——它为什么存在，又凭什么成立？**

*This repository is an independent writing framework and is not affiliated with Zhihu.*

