# 序章00｜独立证据审阅记录（研究阶段附录）

> 分支：nonfiction / `genre-history-science`；主文：`../proposals/00.md`。本文件为研究性补充，不是全书34章的事实认证。

## 主张矩阵

| ID | 待发表主张 | 类型 | 当前核查范围 | 来源 | 文章位置 |
|---|---|---|---|---|---|
| E00-01 | 太阳—地球平均距离与光行时间约8分20秒 | 可证实事实 | 已核对公开机构页面 | [NASA太阳系资料](https://science.nasa.gov/mission/voyager/voyager-1/voyager-1-what-is-a-light-day/) | 正文 §一 |
| E00-02 | 电磁波无需普通物质介质即可在真空传播；声波需物质 | 现代科学解释 | 已核对机构页面 | [NASA/NOAA](https://www.nasa.gov/directorates/somd/space-communications-navigation-program/spectrum-overview/) | 正文 §一/§八 |
| E00-03 | 1600年吉尔伯特《论磁》与地球磁性观点、电磁现象分类 | 史实，原著馆藏记录 | 已核馆藏元数据与简介；原著逐页待核 | [史密森馆藏与美国历史博物馆](https://library.si.edu/digital-library/book/guilielmigilber00gilb) | 正文 §二/§九 |
| E00-04 | 1820年奥斯特报告电流偏转磁针；课堂传说存在争议 | 事实与争议 | 公开专栏已核；原始1820短文待核 | [APS史学专栏](https://www.aps.org/apsnews/2008/07/1820-oersted-electromagnetism) | 正文 §三 |
| E00-05 | 1831年8月29日法拉第铁环线圈装置与瞬时感应 | 实物与研究 | 已核馆藏和研究摘要；原始笔记逐页待核 | [皇家研究院实物/2006年学术研究](https://www.rigb.org/explore-science/explore/collection/michael-faradays-ring-coil-apparatus) | 正文 §四 |
| E00-06 | 法拉第后续磁铁穿线圈感应；亨利独立研究分歧 | 历史叙述 | 公开机构说明已核；序章不展开优先权 | [皇家研究院/计算机历史博物馆](https://www.rigb.org/explore-science/explore/collection/michael-faradays-generator) | 正文 §四 |
| E00-07 | 现代真空波速c=1/√(μ0ε0)与电磁波方程 | 后见物理解释 | 现代教材网页已核；禁止回写为历史符号 | [OpenStax/LibreTexts](https://phys.libretexts.org/Bookshelves/University_Physics/University_Physics_%28OpenStax%29/University_Physics_II_-_Thermodynamics_Electricity_and_Magnetism_%28OpenStax%29/16%3A_Electromagnetic_Waves/16.03%3A_Plane_Electromagnetic_Waves) | 正文 §六/§八 |
| E00-08 | 麦克斯韦动态场论文1864宣读/1865发表 | 档案直接支持 | 原始档案的发表日期已核 | [皇家学会档案与原始期刊](https://makingscience.royalsociety.org/items/pt_72_7/paper-a-dynamical-theory-of-the-electromagnetic-field-by-j-james-clerk-maxwell) | 正文 §六 |
| E00-09 | 现代四条方程经历后世赫维赛德等人的整理 | 二手历史研究 | 已核专题网页，具体数学贡献待进一步核史 | [IEEE Spectrum史学专题](https://spectrum.ieee.org/the-long-road-to-maxwells-equations) | 正文 §六 |
| E00-10 | 赫兹1887—1888电磁波实验证据，波速测定有历史局限 | 学术二手和再实验评论 | 已核论文摘要；避免断言原实验精确测量光速 | [IEEE学术论文与后续研究](https://ieeexplore.ieee.org/document/8072640/) | 正文 §七 |

## 需注意的证据分层

- §一和§八的电磁波传播是现代科学知识，不是1600年的历史认识；说“近乎真空”而非“日地空间绝对无任何物质”。
- §二、§三从局部发现谈主线；序章不捏造一段由现代视角回填的历史人物内心活动。
- §四1831铁环实验的第二线圈响应短暂，不能写成持续发电。后来的磁铁穿线圈是不同实验装置；不要混为第一天发生。
- §六麦克斯韦的1864宣读、1865发表分清楚；现代SI四方程不是他的原始四条格式；他当时使用的以太背景需要保留。
- §七赫兹实验支持电磁波，不能宣称当时全部速度数值已精确证实；参考2017 IEEE研究对历史速度测量的细化。
- §八电磁波在无源区传播不代表真空任意凭空产生辐射；由源或初值产生的波解在无源区延续。
## 尚待完成（用于正式稿转化）

1. 原始奥斯特1820年报告的译本核对。
2. 法拉第1831年实验日记、1832年刊行版及各图号页码双重核对。
3. 麦克斯韦1865原论文的符号、机械介质假设逐段核对；此轮仅利用皇家学会档案记录和发布页面。
4. 赫兹1887—1888原文、历史上各实验的先后与测量不确定度核对。
5. 按仓库 `workflow_gate.py --target draft` 的实际规则，系列 `outline_approved=false`、`evidence_verified=false`；本稿保存在 `proposals/`，不覆盖 `draft/00.md` 占位，不创建假的审稿PASS或终稿。
