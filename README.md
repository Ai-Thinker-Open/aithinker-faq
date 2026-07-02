# AiThinker-FAQ

安信可科技常见问题（FAQ）文档站点，基于 [Sphinx](https://www.sphinx-doc.org/) + [sphinx-rtd-theme](https://sphinx-rtd-theme.readthedocs.io/) 构建，托管于 [Read the Docs](https://readthedocs.org/)。

站点支持 **中英文双语**：以简体中文为源语言（`source/docs/**/*.rst`），英文通过 `.po` 翻译文件（`source/locale/en/`）生成，采用 RTD 官方「单仓库 + 双项目关联」方案。

---

## 快速开始

```powershell
# 1. 安装依赖（一次性）
pip install -r docs/requirements.txt

# 2. 更新翻译 + 本地预览中英文
./build_i18n.ps1

# 3. 浏览器打开
#    中文：build\html\index.html
#    英文：build\html\en\index.html
```

---

## 详细使用说明

**给部门同事的内部培训文档（推荐从这里开始）：**

👉 **[USAGE.md](./USAGE.md)** — 含目录结构、FAQ 写作规范、翻译流程、RTD 部署、常见问题排查等完整说明。

---

## 目录结构（简表）

```
aithinker-faq/
├─ source/
│  ├─ conf.py                 # Sphinx 配置
│  ├─ index.rst               # 首页
│  ├─ docs/                   # 中文 FAQ 正文（.rst）
│  ├─ _static/                # 图片等静态资源
│  └─ locale/en/LC_MESSAGES/  # 英文翻译（.po / .mo）
├─ docs/requirements.txt      # Python 构建依赖
├─ .readthedocs.yaml          # RTD 构建配置
├─ build_i18n.ps1             # Windows 一键脚本
├─ README.md                  # 本文件（快速入口）
└─ USAGE.md                   # 详细使用说明（培训用）
```

---

## 日常维护（三步）

```
1. 编辑 source/docs/.../*.rst（中文）
2. ./build_i18n.ps1 -UpdateOnly → 编辑 .po 填英文 → 脚本会自动编译 .mo
3. git commit & push → RTD 自动部署
```

---

## Read the Docs 部署要点

| 项目 | Language 设置 |
|------|---------------|
| 中文主项目 | Simplified Chinese (zh_CN) |
| 英文项目（同一仓库） | English (en) |

在主项目 `Admin → Translations` 中关联英文项目后，站点右下角会出现语言切换。

> 注意：`.readthedocs.yaml` 中 `formats: []` 表示只构建 HTML，不构建 PDF（FAQ 不适合 PDF）。

---

## 联系我们

1. 样品购买：<https://anxinke.taobao.com>
2. 样品资料：<https://docs.ai-thinker.com>
3. 商务合作：0755-29162996
4. 公司地址：深圳市宝安区西乡固戍华丰智慧创新港 C 栋 410
