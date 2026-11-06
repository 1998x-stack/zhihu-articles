# GitHub Pages · 电子书书架与章节阅读器

公开入口：**https://1998x-stack.github.io/zhihu-articles/**

本项目采用静态站点生成：书架索引、**每本书独立的 book.json**、所有明确映射的 Markdown 章节，共享 HTML/CSS 阅读模板。用户不需要在 GitHub 上阅读源码；每个章节都有单独的可分享阅读网址。

## 目录和数据架构

```text
zhihu-articles/
├── site/
│   ├── index.html                         # 分类书架
│   ├── reader.html                        # 所有章节共用的 HTML 模板
│   └── assets/
│       ├── css/main.css                   # 书架样式
│       ├── css/reader.css                 # 统一阅读排版
│       ├── js/app.js                      # 分类书架与阅读入口
│       ├── js/reader.js                   # 目录抽屉、字号、明暗主题、阅读进度
│       ├── covers/*.png                   # 每本书的正式封面
│       └── data/books.json                # 仅保存跨书的封面/简介/类型/来源
├── articles/nonfiction/.../<book>/
│   ├── book.json                          # 本书唯一章节目录
│   └── draft/**/*.md                      # 各章原始 Markdown
├── scripts/
│   ├── build_pages.py                     # Markdown → 统一静态 HTML
│   └── requirements-pages.txt
└── .github/workflows/pages.yml            # GitHub Pages 发布

The-Empty-Spaces/                         # 独立 GitHub 仓库
├── book.json                              # 《空位》的章节目录
└── manuscript/**/*.md                     # 书稿
```

所有一级题材分类继续只从本仓库根目录 `catalog.json` 派生，不复制分类定义。

## 每本书 book.json 格式

```json
{
  "schema_version": 1,
  "id": "the-empty-spaces",
  "reading_notice": "本书尚在创作与史料审校中。",
  "chapters": [
    {
      "id": "prologue",
      "title": "序章：一个数字，足以推翻整个理论",
      "part": "序章",
      "file": "manuscript/00-prologue/prologue.md",
      "status": "draft"
    },
    {
      "id": "chapter-01",
      "title": "第1章：33种基本物质——拉瓦锡的化学革命",
      "part": "第一部：混沌的元素世界",
      "file": "manuscript/part-01-chaos/chapter-01.md",
      "status": "draft"
    }
  ]
}
```

`file` 必须是相对于 **该 book.json 所在目录** 的安全相对路径，不能跨目录跳转。目录顺序即阅读顺序，`id` 决定永久链接，建议公开后保持稳定。使用 `part` 在侧栏分组，不需要为每组新增页面。

`status` 目前支持：
- `draft`：已有正文初稿，但待审校。
- `outline`：章节尚未写完，Markdown 仍是章节编辑占位，页面会警示。
- `final`：经实际终审确认的最终正文。**不得仅因创建文件就标成 final**。

例如添加新一章：写入对应的 `draft/05.md`，然后在**同一本书**的 `book.json` 添加记录。构建程序不会擅自把研究资料、其他未列出的 Markdown、草稿版本历史或 QA 文件发布到阅读器。

## 十一本书如何映射

| 书籍 | 章节 JSON | Markdown 来源 |
|---|---|---|
| 空位 | `The-Empty-Spaces/book.json` | `The-Empty-Spaces/manuscript/` |
| 失去确定性 | `articles/nonfiction/history-science/the-loss-of-certainty-math-crises/book.json` | 同目录 `draft/` |
| 信用、债务与权力 | `articles/nonfiction/social-business/credit-debt-power-global-financial-history/book.json` | 同目录 `draft/` |
| 从方程到空间：线性代数史 | `articles/nonfiction/history-science/linear-algebra-history/book.json` | 同目录 `draft/` |
| 偶然的法则：概率论史 | `articles/nonfiction/history-science/the-laws-of-chance-probability/book.json` | 同目录 `draft/` |
| 从切线到无穷：微积分史 | `articles/nonfiction/history-science/the-making-of-calculus/book.json` | 同目录 `draft/` |
| 连接的秩序：图论史 | `articles/nonfiction/history-science/graph-theory-history/book.json` | 同目录 `draft/` |
| 热与时间：热力学史 | `articles/nonfiction/history-science/heat-and-time-thermodynamics-history/book.json` | 同目录 `draft/` |
| 看不见的场：电磁学史 | `articles/nonfiction/history-science/fields-of-light-electromagnetism-history/book.json` | 同目录 `draft/` |
| 看不见的秩序：理想气体定律史 | `articles/nonfiction/history-science/ideal-gas-law-two-centuries/book.json` | 同目录 `draft/` |
| 连接的真相：网络科学史 | `articles/nonfiction/history-science/network-science-history/book.json` | 同目录 `draft/` |

书架主数据 `site/assets/data/books.json` 的每条记录新增一个 `source` 字段：

```json
"source": {
  "repository": "self",
  "manifest": "articles/nonfiction/history-science/the-loss-of-certainty-math-crises/book.json"
}
```

外部的《空位》使用 `"repository": "1998x-stack/The-Empty-Spaces"`、`"manifest": "book.json"`。要新增其他外部 GitHub 仓库，需在构建脚本的允许仓库白名单与 Actions 的 checkout 步骤中登记，避免执行不可信内容。

## 统一阅读页

书籍目录页：

```text
https://1998x-stack.github.io/zhihu-articles/read/the-empty-spaces/
```

直接分享章节链接：

```text
https://1998x-stack.github.io/zhihu-articles/read/the-empty-spaces/chapter-01/
```

阅读器具备：
- 左侧分部与章节目录，手机端可展开抽屉；
- Markdown 标题、引文、列表、表格、代码块与脚注排版；
- 使用 MathJax 渲染行内 `$...$` 和块级 `$$...$$` 数学公式（MathJax 使用 CDN，断网时公式保留源码）；
- 上一章/下一章、返回全书目录、回到分类书架；
- 字号、衬线／无衬线字体与浅色/深色主题（浏览器本地保存）；
- 章节阅读进度线、返回顶部；
- 正文初稿／章节占位状态提示。

同一本书的所有章节、甚至不同书籍的章节都使用 **同一份 `site/reader.html` 与 `site/assets/css/reader.css`**，不需要手动复制模板到每个 Markdown 旁边。

### 动态阅读视觉（Apple 网站启发，不是 Apple 官方站点）

在原有样式上额外加载 `site/assets/css/reader-apple.css`，让整套阅读器具有现代科技官网的清爽排版、超大章节标题、轻盈的渐变光效、半透明吸顶工具栏和卡片式书目。

`site/assets/js/reader.js` 实现：
- 屏幕滚动进度与当前小节名称提示；
- 章节标题背景轻微视差、支持鼠标/触控板的渐变追光；
- 使用 IntersectionObserver 的章节标题、引文、图片渐入（仅首次进入视口）；
- 阅读正文字体在书籍衬线与现代无衬线之间切换；
- 保留字号、夜间模式及原有阅读导航。

所有动画都设置了 `prefers-reduced-motion: reduce` 降级；JS、IntersectionObserver 不可用时默认全部内容可见，不影响纯 HTML 阅读。不引入 Apple 商标、图片、私有字体或代码。

## 安全与版权边界

阅读器遵循**章节白名单**，只有 book.json 中列出的 Markdown 被转换为公开 HTML。不会整仓公开 `research.md`、`qa/`、`editorial/`、`.agents/`、`final.md` 等非阅读资源。Markdown 生成的 HTML 会过滤危险标签和属性；站内相对链接转换为站内章节 URL，未登记的文稿链接只跳回 GitHub 源文件。图片仅复制实际被章节引用的、位于允许书稿仓库内的常见图片格式。

**公开可读不等于已出版或已通过审校。** 根据当前书稿状态，正式正文完成度较低；目录中的占位章节只能显示现有占位内容，不会人工填充未完成章节。为区分状态，目录及每章页均显示标记。

## 部署和自动更新

1. 仓库 Settings → Pages → Source 使用 **GitHub Actions**。
2. 本仓库 `main` 的 `site/`、书稿 `draft/`、`book.json` 或构建脚本变化会自动重新部署。
3. 《空位》在独立仓库，Pages 工作流构建时先 checkout 其最新 `main` 版本。由于独立仓库的提交不会直接触发本仓库 workflow，额外配置了每天一次定时同步；也可进入 Actions → **Publish e-book bookshelf → Run workflow** 立即同步。
4. 部署任务对缺失的独立仓库或章节文件采用**失败优先**原则，避免静默发布不完整目录。

本地构建需要 Python 3.11+：

```bash
python -m pip install -r scripts/requirements-pages.txt
mkdir -p external
git clone https://github.com/1998x-stack/The-Empty-Spaces.git external/the-empty-spaces
python scripts/build_pages.py --out _site --require-all-sources
python -m http.server 8000 --directory _site
```

本地访问 `http://localhost:8000/`，阅读 `/read/<book-id>/<chapter-id>/`。没有下载独立仓库时，可省略 `--require-all-sources` 只预览本仓库内的两本书。

构建检查：

```bash
python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/validate_repo.py
```

### PNG 封面

将封面 PNG 存入 `site/assets/covers/<book-id>.png`，建议约 1400 × 2000 像素，更新 `site/assets/data/books.json` 中的 `cover` 属性即可。阅读器首页目录也复用对应书封。


## 新书与封面工作流（2026-11）

新增八本作品已在 `site/assets/data/books.json` 以真实标题、英文副题、简介、分类和章节索引路径登记。

- 八本暂时均设置 `cover: null`；书架与全书目录自动使用字体排版式封面，不依赖 PNG，也不会出现空白封面。
- 书籍正式封面按 `site/assets/covers/<book-id>.png` 命名；制作完成后再更新对应 `cover` 字段，无须修改模板。
- 微积分已有 `series.json`，图论已有 `chapters.json`，两者为原有研究资料，**新增的 `book.json` 是 Pages 阅读器的统一规范**，不要删除原先的研究记录。
- 电磁学 `README.md` 将序章描述为候审稿，但目前 `draft/00.md` 实际仍是设计占位。因此标准章节索引按实际文件标记为 `outline`，待真正正文更新后再调整。
- 标为 `draft` 的章节不意味着已通过独立审稿或可以声称正式出版。

## 公式渲染与故障排查（2026-11 修复）

Markdown 构建现在启用 `pymdownx.arithmatex` 的 `generic` 模式，在 Python-Markdown 转换 HTML **之前**保护 LaTeX，支持四种写法及 `\\begin{align}` 等环境：

- 行内：`$x^2$` 或 `\\(x^2\\)`
- 块级：`$$E=mc^2$$` 或 `\\[E=mc^2\\]`
- 多行：`\\begin{align}a&=b\\\\c&=d\\end{align}`

输出统一成为 `<span class="arithmatex">\\(...\\)</span>` 或 `<div class="arithmatex">\\[...\\]</div>`，再由 MathJax 3 渲染。HTML 清理保留这些安全的容器标签，不再吞掉 TeX 分隔符。普通货币的美元符号通过 `smart_dollar` 避免误判；代码围栏中的美元符号也不会触发数学公式。

**CDN 故障**：优先 jsDelivr，失败则自动回退到 cdnjs；两个 CDN 均不可达时，站点将保留 LaTeX 文本并显示提示。MathJax 本身需要外网，不会假称完全离线可用。

**构建自检**：单元测试现在检查真实的理想气体、线性代数、数学思想史章节中的原始 `\\[...`、`\\(...`、`\\begin{cases}`、`$...$`，以及内联美元货币与代码段。新增 PNG 文件也要通过构建校验与公开链接探测。

注意：**引擎能显示公式不等于数学内容本身无误**；书稿中的公式推导、中文标点及历史表述仍需要作者按章节校对。
