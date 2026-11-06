# Cover PNGs

将每部书 / 每组系列文章的正式封面存为：

```text
site/assets/covers/<book-id>.png
```

- 建议尺寸：1400 × 2000 像素（竖版，7:10）。
- 配色统一不是强制要求；推荐在缩略图尺寸下仍有清晰的大字书名。
- 文件名与 `site/assets/data/books.json` 的 `id` 保持一致。
- 完成 PNG 后，把书目的 `cover` 设为 `"assets/covers/<book-id>.png"`。
- `cover: null` 时显示自动排版的书封，无需现在先制作全部 PNG。
- 只上传有权使用的原创封面或已获授权的素材。
