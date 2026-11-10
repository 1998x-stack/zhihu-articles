# GitHub Pages 书架与章节收录协议

## 根因与新机制
`site/assets/js/app.js` 读取构建生成的 `assets/data/books.json`；旧版构建器仅复制 `site/assets/data/books.json` 的手工书单，新系列即使存在于 `articles/` 也可能不可见。修复后，`scripts/build_pages.py` 会扫描 `catalog.json` 约定的各题材归档：只要含 `README.md` 和有效 `book.json`，新系列便自动加入书架。原有卡片的封面/文案等定制保留；新卡片在缺 PNG 时使用排版式封面。

## 最小作品结构
```text
articles/nonfiction/history-science/my-series/
├── README.md
├── metadata.yaml        # 推荐，提供摘要与标签
├── book.json            # 必须：可公开的章节目录
└── draft/
    ├── 00.md
    └── 01.md
```
`book.json` 示例：
```json
{
  "schema_version": 1,
  "id": "my-series",
  "title": "一部研究性知识叙事",
  "reading_notice": "仅为工作初稿与占位，未经独立双审或终审。",
  "chapters": [
    {"id": "prologue", "title": "序章", "part": "序章", "file": "draft/00.md", "status": "outline"},
    {"id": "chapter-01", "title": "第一章", "part": "第一部", "file": "draft/01.md", "status": "draft"}
  ]
}
```

目录 slug 与 manifest `id` 必须相同。章节 ID 不重复，路径必须在本书目录内且文件真实存在，不允许 `..` 或绝对路径。章节状态只能是 `outline`（明确占位）、`draft`（待审工作初稿）、`final`（确已完成终稿审批）。**绝不能因存在 Markdown、claims 或网页链接自行提升审核状态。**

系列目录、正文及章级来源由对应写作/研究阶段负责；主编/仓库维护者负责根据实际交付同步 `book.json`。新的系列或三章批次，PR 要包括书籍目录、章节状态、源路径映射的核验结果。只有 `book.json` 显式列出的章节会成为站内读者页；研究资料、QA 与 Skill 不应随站点部署泄露。

## 本地检查与 CI
```bash
python scripts/build_pages.py --check-catalog
python scripts/sync_skills.py --check
python -m unittest discover -s scripts -p 'test_*.py' -v
python -m pip install -r scripts/requirements-pages.txt
python scripts/build_pages.py --out _site
```
`--check-catalog` 不需要 Markdown 渲染依赖，能检查新系列漏登记、manifest 标识、章节链接与状态。GitHub Actions 的 `validate.yml` 执行预检和单测，`pages.yml` 拉取外部书稿后构建、部署。合并 PR 后核对两项 job 成功，实际查看首页、`read/<book-id>/` 和至少一章 `read/<book-id>/<chapter-id>/`。站点首页缓存或 Actions 部署未完成均可能延后可见性。

## 常见问题
| 症状 | 处理 |
|---|---|
| 新系列不出现在书架 | 确认目录位于 `catalog.json` 的 archive 下且有 `README.md + book.json`；执行预检 |
| 构建错误缺 book.json | 按真实目录/实际工作稿状态建立 manifest，不应跳过 |
| 有书卡无站内阅读 | 检查 source.manifest、外部书稿 checkout 和 `--require-all-sources` 日志 |
| 章节找不到或状态过期 | 校正 manifest 中章节 id、file、`outline/draft/final` 并重新部署 |
| 网站可读被误当发表 | 明确标出待审状态；网站展示不等于 `workflow_gate.py --target publish` 或知乎发布 |

不要将构建产物 `_site/` 提交进 Git，也不要为通过构建篡改审稿记录或自动把工作初稿标为终稿。
