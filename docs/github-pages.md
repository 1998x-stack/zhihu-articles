# GitHub Pages · 电子书书架

本仓库的公开门户是一座 **按题材分类的电子书书房**，每部书或系列文章使用一张封面卡片。网站与写作 Skills、研究资料、草稿审稿流程相互隔离。

## 结构

```text
site/
  index.html                       # 书架主页与详情弹窗
  assets/
    css/main.css                   # 响应式视觉、实体书封/书架效果、深浅主题
    js/app.js                      # 分类/搜索/详情/主题交互
    data/books.json                # 在架书目（手工维护）
    covers/                        # 未来每部作品的 PNG 封面
    favicon.svg
scripts/build_pages.py            # 仅构建允许公开的内容
.github/workflows/pages.yml       # 自动构建并部署至 GitHub Pages
_site/                            # 本地产物（不应提交）
```

**分类唯一来源：** 根目录 `catalog.json` 的 `genres`。构建脚本自动生成网站使用的 `assets/data/genres.json`，保留全部 10 个分类；不要再维护另一份重复分类表。

**书目来源：** `site/assets/data/books.json`。书籍可以位于本仓库，也可以指向其他 GitHub 仓库，例如《空位》。

## 启用 GitHub Pages

1. 合并包含本网站的 PR 到 `main`。
2. 进入仓库 **Settings → Pages → Build and deployment**，将 **Source** 选为 **GitHub Actions**。
3. 在 **Actions → Publish e-book bookshelf** 确认首次部署执行；必要时用 **Run workflow** 手动触发。
4. 部署成功后，项目站点通常位于 **https://1998x-stack.github.io/zhihu-articles/**。实际 URL 以 Pages 设置和工作流的 deployment URL 为准。

若仓库或组织限制 Actions / Pages 写权限，需在 GitHub 设置中开放相应部署权限。此 PR 只提交部署工作流，**不会自行修改仓库 Pages 设置**。

## 本地预览

```bash
python scripts/build_pages.py --out _site
python -m http.server 8000 --directory _site
# 浏览 http://localhost:8000
```

`file://` 直接打开 `index.html` 可能被浏览器阻止加载 JSON；请通过本地 HTTP 服务预览。

验证：

```bash
python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/validate_repo.py
```

## 增加一本书 / 一组系列文章

编辑 `site/assets/data/books.json`，按现有对象添加书目。推荐字段：

| 字段 | 含义 |
| --- | --- |
| `id` | 稳定且唯一的英文 slug |
| `title`、`subtitle` | 中文书名、可选英文副题 |
| `genre` | 对应 `catalog.json` 的 `skill`，例如 `genre-history-science` |
| `type` | 如“科学发现史 · 长篇”“悬疑故事 · 系列” |
| `author`、`description`、`tags` | 作者、简介、搜索关键词 |
| `status`、`note` | 实际写作状态与补充说明；不要把草稿标成已出版 |
| `url` | 作者仓库/书目入口的 HTTPS URL |
| `readUrl` | **可选**，仅已有公开审定版时填写该阅读入口 |
| `cover` | `null`，或确实存在的 `assets/covers/<slug>.png` |
| `palette`、`coverInk` | PNG 未制作时的封面渐变色与字体颜色（六位 HEX） |
| `coverShort`、`coverEyebrow`、`coverFooter` | 无 PNG 时的书封排版文字 |

### PNG 封面

将封面保存为 `site/assets/covers/<book-id>.png`，建议 **1400 × 2000 px**（约 7:10 纵向比例）、sRGB，尽量压缩体积。然后把对应书目的 `cover` 从 `null` 改成 `"assets/covers/<book-id>.png"`。构建脚本会检查图片路径、是否存在，并将其复制到公开产物中。如果没有 PNG，前台自动使用排版式电子书封面，不显示破图。

## 发布安全

- 构建脚本采用**白名单复制**：只发布主页、样式、交互脚本、书目 JSON、生成的分类 JSON、站点图标和 PNG 封面。
- 不发布 `articles/` 下的原始草稿、审核记录、来源台账，也不发布 `.agents/` 等写作工具目录。
- 已在馆藏出现 ≠ 已通过编辑审稿。作品的具体状态以各作品仓库为准。
- 若未来需要站内长篇阅读器，应只从通过 `workflow_gate.py --target publish` 和人工终审的作品生成阅读内容，不要遍历 `draft/` 自动上架。

## 调整外观

所有主题、立体封面、书架层板、移动端断点均在 `site/assets/css/main.css`；交互集中在 `site/assets/js/app.js`。站点不依赖前端框架或 npm，适合长期用 GitHub Pages 托管。
