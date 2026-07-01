# AiThinker-FAQ

安信可科技常见问题（FAQ）文档站点，基于 [Sphinx](https://www.sphinx-doc.org/) + [sphinx_rtd_theme](https://sphinx-rtd-theme.readthedocs.io/) 构建，托管于 [Read the Docs](https://readthedocs.org/)。

站点支持 **中英文双语**：以简体中文为源语言，英文通过 [sphinx-intl](https://sphinx-intl.readthedocs.io/) 翻译工作流生成，并采用 Read the Docs 官方「单仓库 + 双项目关联」方案，由平台自动提供语言切换器。

## 目录结构

```
aithinker-faq/
├─ source/                     # 文档源目录
│  ├─ conf.py                  # Sphinx 配置（语言由 READTHEDOCS_LANGUAGE 决定，回退 zh_CN）
│  ├─ index.rst               # 首页
│  ├─ docs/                    # 各分类文档（.rst）
│  ├─ _static/                 # 图片、样式等静态资源
│  ├─ _templates/              # 模板目录
│  └─ locale/                  # 翻译文件
│     └─ en/LC_MESSAGES/       # 英文 .po 译文
├─ docs/requirements.txt       # 构建依赖（RTD 使用，Python 3.8）
├─ build_i18n.ps1              # Windows 一键：更新翻译 + 双语言本地预览
├─ .readthedocs.yaml           # Read the Docs 构建配置
├─ make.bat / Makefile         # Sphinx 构建入口
└─ README.md
```

## 环境准备（一次性）

```powershell
pip install -r docs/requirements.txt
```

## 本地编译

### 方式一：一键脚本（推荐，Windows PowerShell）

```powershell
# 更新英文 .po + 构建中文(build\html) 与英文(build\html\en)
./build_i18n.ps1

# 仅构建预览，不更新翻译
./build_i18n.ps1 -BuildOnly

# 仅更新翻译文件，不构建
./build_i18n.ps1 -UpdateOnly
```

构建完成后，用浏览器打开：

- 中文：`build\html\index.html`
- 英文：`build\html\en\index.html`

> 本地把英文放在 `build\html\en` 子目录只是为了同时预览两种语言；线上是两个独立的 RTD 项目，不使用该合并布局。

### 方式二：手动命令（等价）

```powershell
# 中文（默认，无环境变量时回退 zh_CN）
sphinx-build -b html source build\html

# 英文（读取 locale\en 的译文）
sphinx-build -b html -D language=en source build\html\en
```

## 翻译工作流

当中文 `.rst` 内容有增改后：

```powershell
# 1. 提取新文案，增量刷新英文 .po（gettext_uuid 会保留已译内容）
./build_i18n.ps1 -UpdateOnly

# 2. 编辑 source\locale\en\LC_MESSAGES\ 下各 .po 文件，填写 msgstr 英文译文

# 3. 提交推送，RTD 会自动重建中英两个语言项目
git add source/ docs/ .readthedocs.yaml
git commit -m "更新文档与英文翻译"
git push
```

底层等价命令（脚本已封装）：

```powershell
sphinx-build -b gettext source build\gettext
sphinx-intl update -p build\gettext -l en -d source\locale
```

## 部署到 Read the Docs

采用官方「单仓库 + 双项目关联」方案：同一个 Git 仓库导入为两个 RTD 项目，分别负责中文与英文，再关联为翻译。

1. **主项目（中文）**：在 RTD `Admin → Settings` 中把 **Language** 设为 `Simplified Chinese (zh_CN)`。
2. **英文项目**：`Dashboard → Add project` 导入**同一个仓库**（项目名建议 `aithinker-faq-en`），其 `Admin → Settings` 的 **Language** 设为 `English (en)`。RTD 会自动注入 `READTHEDOCS_LANGUAGE=en`，配合 `conf.py` 构建英文站点。
3. **关联翻译**：在**主项目** `Admin → Translations → Add translation` 中选择英文项目。
4. **触发构建**：两个项目各构建一次。

部署完成后：

- 中文：`https://<主项目>.readthedocs.io/zh-cn/latest/`
- 英文：`https://<主项目>.readthedocs.io/en/latest/`
- 页面右下角 Read the Docs 悬浮菜单出现 **Languages** 分组，可在当前页面的中英版本间切换；首次访问会按浏览器语言自动匹配。

## 说明

- 语言由 `conf.py` 中 `language = os.environ.get('READTHEDOCS_LANGUAGE', 'zh_CN')` 决定，一份配置服务两个语言项目。
- Markdown 由 [myst-parser](https://myst-parser.readthedocs.io/) 解析（已替代废弃的 recommonmark）。
- 构建依赖锁定于 `docs/requirements.txt`，`.readthedocs.yaml` 中 Python 版本为 3.8。

## 联系我们

1. 样品购买：<https://anxinke.taobao.com>
2. 样品资料：<https://docs.ai-thinker.com>
3. 商务合作：0755-29162996
4. 公司地址：深圳市宝安区西乡固戍华丰智慧创新港 C 栋 410
