# AGENTS.md｜OpenCode / Pi / Codex 项目代理协作规范

本仓库的唯一创作总控为 `chief-narrative-editor`。不要将某种题材的 Prompt 直接当成所有类型通用的风格模板。

**Skill 目录映射**：OpenCode 使用 `.opencode/skills/`，Pi 使用 `.pi/skills/`，Codex 使用 `.codex/skills/`。三套内容是逐字节一致的镜像；`.opencode/skills/` 为维护源，任何 Skill 更新都应同步至另外两个目录并通过 `scripts/validate_repo.py` 验证。下文的 `.opencode/skills/` 路径在 Pi 与 Codex 中可替换为其对应的根目录。

## 开始一篇新文章
1. 先读取 `.opencode/skills/chief-narrative-editor/SKILL.md` 及其 `prompt.txt`，冻结主题与创作约束。
2. 根据 `catalog.json` 选择一个主要类型 Skill，完整读取其 `SKILL.md` 与 `prompt.txt`；混合类型可参考副类型，但以主类型约束为准。
3. 先执行 `topic-development` 与 `story-architect`，再使用 `character-world` 和 `plot-and-clues`，记录经得起因果审计的构思。
4. 现实专业背景、历史科学或非虚构必须先 `fact-research`；证据不足时停止将推断当事实。
5. 使用 `chapter-writer` 逐章写作；维持故事档案和章节状态，不改变已锁定规则。
6. 执行 `continuity-audit`、`developmental-editor` 和 `line-edit`；通过后再 `publication-package`。
7. 成稿归入 `articles/<分类>/<类型>/<slug>/`；及时更新 metadata 和创作状态。

## 编辑纪律
- 虚构故事允许想象，但不得移植受保护作品的标志性人物或大段表达。
- 非虚构严禁编造历史引文、证据、统计、采访和引用；资料边界以 research 为准。
- 不得用过度暴力、血腥、未成年人不适宜的露骨情节吸引流量。
- 重要剧情变更须更新 story-bible、outline 与 qa-report，保证版本一致。
- 不得未经请求直接执行外部发布、提交到第三方平台或宣称完成商业审核。

## 优先级
用户具体任务 > 作品确定的事实与规则 > 核心 Skill > 主类型 Skill > 阶段 Skill > 语言风格偏好；遇到冲突，应透明说明并给出修复建议。
