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

## 三本书如何映射

| 书籍 | 章节 JSON | Markdown 来源 |
|---|---|---|
| 空位 | `The-Empty-Spaces/book.json` | `The-Empty-Spaces/manuscript/` |
| 失去确定性 | `articles/nonfiction/history-science/the-loss-of-certainty-math-crises/book.json` | 同目录 `draft/` |
| 信用、债务与权力 | `articles/nonfiction/social-business/credit-debt-power-global-financial-history/book.json` | 同目录 `draft/` |

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
- 字号与浅色/深色主题（浏览器本地保存）；
- 章节阅读进度线、返回顶部；
- 正文初稿／章节占位状态提示。

同一本书的所有章节、甚至不同书籍的章节都使用 **同一份 `site/reader.html` 与 `site/assets/css/reader.css`**，不需要手动复制模板到每个 Markdown 旁边。

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
