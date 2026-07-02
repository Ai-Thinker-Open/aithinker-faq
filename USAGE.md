# AiThinker-FAQ 仓库使用说明

> 本文档面向**不熟悉 Sphinx / Read the Docs** 的研发同事，用于讲解本仓库的结构、日常维护方式与中英文发布流程。  
> 建议配合本地预览实际操作一遍。

---

## 目录

1. [这个仓库是做什么的](#1-这个仓库是做什么的)
2. [先搞懂 5 个核心概念](#2-先搞懂-5-个核心概念)
3. [目录结构说明](#3-目录结构说明)
4. [站点导航与文档分类](#4-站点导航与文档分类)
5. [FAQ 文档怎么写（最重要）](#5-faq-文档怎么写最重要)
6. [新增或修改一条 FAQ 的完整流程](#6-新增或修改一条-faq-的完整流程)
7. [英文翻译怎么维护](#7-英文翻译怎么维护)
8. [本地环境搭建与预览](#8-本地环境搭建与预览)
9. [Read the Docs 线上发布](#9-read-the-docs-线上发布)
10. [常见问题排查](#10-常见问题排查)
11. [术语表](#11-术语表)

---

## 1. 这个仓库是做什么的

本仓库是 **安信可（Ai-Thinker）官方 FAQ 文档站** 的源码，最终发布为在线网站：

- 用户可以在网站上 **搜索** 常见问题与解答
- 内容按 **模组类型 / 开发环境 / 出厂固件** 等分类组织
- 支持 **中文 + 英文** 两个语言版本

### 用一句话理解技术栈

| 组件 | 作用 | 类比 |
|------|------|------|
| **`.rst` 文件** | 文档正文（中文源稿） | Word 文档 |
| **Sphinx** | 把 `.rst` 转成 HTML 网站 | 排版 + 发布工具 |
| **`.po` / `.mo` 文件** | 英文翻译词典 | 中英对照表 |
| **Read the Docs (RTD)** | 云端自动构建并托管网站 | 自动部署平台 |

**你只需要会编辑 `.rst` 和 `.po`，其余构建、部署大多可自动化。**

---

## 2. 先搞懂 5 个核心概念

### 2.1 源语言 vs 翻译语言

- **源语言（中文）**：所有正文写在 `source/docs/**/*.rst` 里，**只维护这一份中文源稿**
- **英文**：不单独维护一套英文 `.rst`，而是维护 `source/locale/en/LC_MESSAGES/**/*.po` 里的 `msgstr`

```
中文源稿 (.rst)  ──gettext 提取──▶  .po 里的 msgid（中文）
                                        │
                                   研发填写 msgstr（英文）
                                        │
                                   编译为 .mo
                                        │
英文站点构建 ◀──────────────────────────┘
```

### 2.2 `.rst` 是什么

ReStructuredText（reST）是 Sphinx 使用的标记语言，类似 Markdown，但语法略有不同。

常见写法：

```rst
章节标题
========

小节标题
--------

``行内代码``

**加粗**

`链接文字 <https://example.com>`__

.. code:: bash

   AT+GMR
```

### 2.3 `.po` 和 `.mo` 是什么

| 文件 | 谁编辑 | 作用 |
|------|--------|------|
| `.po` | **人工编辑** | 翻译源文件，含 `msgid`（中文）和 `msgstr`（英文） |
| `.mo` | **机器生成** | `.po` 编译后的二进制，**Sphinx 构建英文站时实际读取的文件** |

> **重要：** 只改 `.po` 不改 `.mo`，英文站可能仍显示旧内容或中文。  
> 改完 `.po` 后必须执行 `sphinx-intl build -l en`（或运行 `./build_i18n.ps1`）。

### 2.4 一份 `conf.py` 服务两个语言

`source/conf.py` 通过环境变量 `READTHEDOCS_LANGUAGE` 决定构建哪种语言：

| 环境 | `language` | 读什么内容 |
|------|------------|------------|
| 未设置（本地默认） | `zh_CN` | 直接读 `.rst` 中文 |
| RTD 中文项目 | `zh_CN` | 直接读 `.rst` 中文 |
| RTD 英文项目 | `en` | 读 `.rst` + `locale/en/**/*.mo` 译文 |

### 2.5 线上是「一个仓库 + 两个 RTD 项目」

- **中文 RTD 项目**：Language = `Simplified Chinese (zh_CN)`
- **英文 RTD 项目**：Language = `English (en)`，导入**同一个 Git 仓库**
- 在主项目里把英文项目 **关联为 Translation**，RTD 会自动提供语言切换

---

## 3. 目录结构说明

```
aithinker-faq/
│
├─ source/                          ← 【文档源目录，日常主要改这里】
│  ├─ conf.py                         Sphinx 配置（语言、主题、i18n）
│  ├─ index.rst                       网站首页（六大入口导航）
│  │
│  ├─ docs/                           【中文 FAQ 正文，按分类分子目录】
│  │  ├─ instruction/                 使用说明
│  │  ├─ development-environment/     开发环境
│  │  ├─ application-solution/        应用方案
│  │  ├─ software-framework/          软件使用（体量最大）
│  │  ├─ hardware-related/            硬件相关
│  │  └─ taobao/                      出厂固件
│  │
│  ├─ _static/                        图片、Logo、CSS 等静态资源
│  ├─ _templates/                     HTML 模板（一般不用动）
│  │
│  └─ locale/                         【英文翻译文件】
│     └─ en/LC_MESSAGES/              与 docs/ 目录一一对应的 .po / .mo
│        ├─ index.po                  首页翻译
│        └─ docs/.../*.po             各分类页翻译
│
├─ docs/requirements.txt              Python 构建依赖（RTD 也用这份）
├─ .readthedocs.yaml                  RTD 云端构建配置
├─ build_i18n.ps1                     Windows 一键：更新翻译 + 本地双语预览
├─ Makefile / make.bat                Sphinx 构建入口（可选）
├─ README.md                          仓库简介（快速入口）
└─ USAGE.md                           本文档（详细使用说明）
```

### 3.1 `.rst` 与 `.po` 的对应关系

每个 `source/docs/xxx/yyy.rst` 对应一个翻译文件：

```
source/docs/software-framework/WiFi/BL/wifi.rst
    ↕ 一一对应
source/locale/en/LC_MESSAGES/docs/software-framework/WiFi/BL/wifi.po
source/locale/en/LC_MESSAGES/docs/software-framework/WiFi/BL/wifi.mo
```

当前仓库共有 **45 个** `.rst` 文档 + **1 个** 首页 `index.rst`，对应 **46 个** `.po` 文件。

### 3.2 不要提交到 Git 的内容

已在 `.gitignore` 中忽略：

| 路径/模式 | 说明 |
|-----------|------|
| `build/` | 本地构建输出 |
| `_build_en/` | 本地英文预览输出 |
| `*.po~` | msgmerge 自动生成的备份，可删 |
| `_pot_out/` | 临时 gettext 模板目录 |

---

## 4. 站点导航与文档分类

### 4.1 首页六大模块

首页 `source/index.rst` 提供六个入口：

| 入口 | 目录 | 说明 |
|------|------|------|
| 使用说明 | `docs/instruction/` | 如何搜索 FAQ |
| 开发环境 | `docs/development-environment/` | 开发板/模组环境搭建 |
| 应用方案 | `docs/application-solution/` | 应用场景相关 |
| 软件使用 | `docs/software-framework/` | 各系列模组软件 FAQ（最多） |
| 硬件相关 | `docs/hardware-related/` | 硬件类问题 |
| 出厂固件 | `docs/taobao/` | 出厂固件相关 |

### 4.2 软件使用下的主要子分类

`docs/software-framework/index.rst` 通过 `toctree` 自动索引子目录，例如：

- `WiFi/` — 含博流(BL)、RTL87XX、平头哥(TG)、Ai-M61 等
- `bt/` — 蓝牙
- `2.4G/`、`GPRS/`、`GPS/`、`UWB/`、`LoRa-LoRaWan/`、`VC/`、`Rd/`、`Ai-pi/`、`TOOL/`

### 4.3 我该把新问题加到哪个文件？

按 **产品系列 / 问题类型** 选择对应 `.rst`：

| 问题类型 | 建议文件 |
|----------|----------|
| WB2 / 博流 WiFi | `docs/software-framework/WiFi/BL/wifi.rst` 或同目录其它专题 |
| RTL87XX | `docs/software-framework/WiFi/RTL87XX/index.rst` |
| 平头哥 TG | `docs/software-framework/TG/index.rst` 或 `development-environment/TG/tg_12f.rst` |
| 蓝牙 AT | `docs/software-framework/bt/bt.rst` |
| GPRS/4G | `docs/software-framework/GPRS/index.rst` |
| 出厂固件 BW16 | `docs/taobao/BW16/index.rst` |

**不确定时**：先在本地构建预览，或询问文档维护负责人。

---

## 5. FAQ 文档怎么写（最重要）

### 5.1 标准「一问一答」格式

本仓库 FAQ 普遍采用如下结构（**标题下划线长度需 ≥ 标题文字长度**）：

```rst
问题标题写在这里
----------------

答案写在这里。可以有多行。

下一条问题标题
--------------

下一条答案。
```

**真实示例**（摘自 `WiFi/BL/wifi.rst`）：

```rst
WB2系列模组支持MQTT开发吗
--------------

支持

请问WB2系列模组支持接入中文名称的WIFI么？
-------------------

支持UTF-8格式的中文
```

### 5.2 常用 reST 语法速查

| 效果 | 写法 |
|------|------|
| 行内代码 / 型号 | ``Ai-WB2-12F`` |
| 加粗 | `**加粗文字**` |
| 外链 | `` `链接文字 <https://url>`__ `` |
| 代码块 | `.. code:: bash` 下一行起缩进 |
| 图片 | `.. figure:: _static/xxx.png` |
| 分隔线 | 单独一行 `--------------` |

### 5.3 带章节自动编号的页面

部分页面（如 `WiFi/BL/wifi.rst`）顶部有 HTML 计数器，用于自动生成「1.1、1.2」式编号：

```rst
.. raw:: html

   <style>
   body {counter-reset: h2}
     h2 {counter-reset: h3}
     h2:before {counter-increment: h2; content: counter(h2) ". "}
     h3:before {counter-increment: h3; content: counter(h2) "." counter(h3) ". "}
     h2.nocount:before, h3.nocount:before, { content: ""; counter-increment: none }
   </style>
```

**新增页面如无特殊需求，可不添加此段**；保持与同目录其它文件风格一致即可。

### 5.4 写作注意事项

1. **标题就是搜索关键词**：用户会搜「MQTT」「esptouch」，标题里应包含这些词
2. **答案宜短**：FAQ 不是教程，直接给结论；需要详细步骤时再写长答案
3. **型号、URL、AT 指令**：保持原文，英文翻译时也通常原样保留
4. **不要随意改已有问题的标题**：改标题会导致 `.po` 里 `msgid` 变化，原有英文翻译会失效，需重新翻译
5. **图片放 `_static/`**：引用路径写 `_static/图片名.png`

---

## 6. 新增或修改一条 FAQ 的完整流程

以下以「在 `WiFi/BL/wifi.rst` 新增一条 WB2 相关问题」为例。

### 步骤 1：编辑中文源稿

打开 `source/docs/software-framework/WiFi/BL/wifi.rst`，在文件末尾追加：

```rst
WB2系列模组是否支持 XXX 功能
-----------------------------

支持 / 不支持 / 具体说明...
```

### 步骤 2：本地预览中文效果

```powershell
cd D:\GitHub\aithinker-faq
sphinx-build -b html source build\html
# 浏览器打开 build\html\docs\software-framework\WiFi\BL\wifi.html
```

或使用一键脚本（见第 8 节）。

### 步骤 3：更新英文翻译模板

中文源稿变更后，需要刷新 `.po` 文件（会把新增中文写入 `msgid`，并保留已有 `msgstr`）：

```powershell
./build_i18n.ps1 -UpdateOnly
```

底层等价命令：

```powershell
sphinx-build -b gettext source build\gettext
sphinx-intl update -p build\gettext -l en -d source\locale
```

此时 `source/locale/en/LC_MESSAGES/docs/software-framework/WiFi/BL/wifi.po` 会出现新的空 `msgstr` 条目。

### 步骤 4：填写英文翻译

用文本编辑器打开对应 `.po`，找到新增条目：

```po
#: ../source/docs/software-framework/WiFi/BL/wifi.rst:99
msgid "WB2系列模组是否支持 XXX 功能"
msgstr ""          ← 在这里填写英文

#: ../source/docs/software-framework/WiFi/BL/wifi.rst:101
msgid "支持 / 不支持 / 具体说明..."
msgstr ""          ← 在这里填写英文
```

填写示例：

```po
msgid "WB2系列模组是否支持 XXX 功能"
msgstr "Does the WB2 series module support XXX?"

msgid "支持 / 不支持 / 具体说明..."
msgstr "Supported / Not supported / Details..."
```

**翻译规范：**

- 保留 `` ` `` 包裹的 reST 标记、URL、型号
- `msgstr` 不要留空（构建英文站时需要）
- 同一段中文若在多处出现，`.po` 可能合并为一条，填一次即可

### 步骤 5：编译 `.mo` 文件

```powershell
cd source
sphinx-intl build -l en
```

### 步骤 6：预览英文效果

```powershell
cd D:\GitHub\aithinker-faq
sphinx-build -b html -D language=en source build\html\en
# 浏览器打开 build\html\en\docs\software-framework\WiFi\BL\wifi.html
```

### 步骤 7：提交 Git

```powershell
git add source/docs/software-framework/WiFi/BL/wifi.rst
git add source/locale/en/LC_MESSAGES/docs/software-framework/WiFi/BL/wifi.po
git add source/locale/en/LC_MESSAGES/docs/software-framework/WiFi/BL/wifi.mo
git commit -m "docs(WiFi/BL): 新增 XXX 相关 FAQ 及英文翻译"
git push
```

推送后 RTD 会自动重新构建中英文两个项目。

### 流程图（总览）

```
编辑 .rst（中文）
      │
      ▼
本地预览中文 build\html
      │
      ▼
./build_i18n.ps1 -UpdateOnly   → 刷新 .po
      │
      ▼
编辑 .po 填写 msgstr（英文）
      │
      ▼
sphinx-intl build -l en        → 生成 .mo
      │
      ▼
本地预览英文 build\html\en
      │
      ▼
git commit & push              → RTD 自动部署
```

---

## 7. 英文翻译怎么维护

### 7.1 `.po` 文件结构说明

```po
#: ../source/docs/xxx.rst:行号 唯一ID
msgid "中文原文（从 .rst 自动提取）"
msgstr "English translation（人工填写）"
```

- **`msgid`**：不要手动改，由 Sphinx 从 `.rst` 提取
- **`msgstr`**：填英文；留空则英文站显示中文

### 7.2 何时需要更新 `.po`

| 操作 | 是否需要 update |
|------|-----------------|
| 新增 FAQ 条目 | ✅ 需要 |
| 修改中文措辞（标题/答案变了） | ✅ 需要（旧 msgid 变 obsolete，新 msgid 出现） |
| 只改英文翻译 | ❌ 直接改 msgstr 即可 |
| 删除 FAQ 条目 | ✅ update 后 obsolete 条目可清理 |

### 7.3 `*.po~` 是什么

执行 `msgmerge` 或 `sphinx-intl update` 时可能生成 `.po~` 备份文件，**可安全删除**，不要提交到 Git。

### 7.4 新增整页文档时

若新建了 `source/docs/新目录/新文件.rst`：

1. 确保已被某个 `index.rst` 的 `toctree` 引用（否则不会出现在导航）
2. 执行 `./build_i18n.ps1 -UpdateOnly` 自动生成对应 `.po`
3. 翻译并 `sphinx-intl build -l en`

---

## 8. 本地环境搭建与预览

### 8.1 环境要求

- **Python 3.8+**（与 RTD 线上一致，推荐 3.8）
- **Windows**（本仓库提供 PowerShell 脚本；Mac/Linux 可用等价命令）

### 8.2 一次性安装依赖

```powershell
cd D:\GitHub\aithinker-faq
pip install -r docs/requirements.txt
```

主要依赖：

| 包 | 用途 |
|----|------|
| Sphinx | 文档构建 |
| sphinx-rtd-theme | 网站主题（与 RTD 线上一致） |
| myst-parser | Markdown 支持（本仓库主要用 .rst） |
| sphinx-intl | 翻译文件管理 |

### 8.3 一键脚本（推荐）

```powershell
# 更新 .po + 编译 .mo + 构建中英文预览
./build_i18n.ps1

# 仅更新翻译文件
./build_i18n.ps1 -UpdateOnly

# 仅构建预览（不更新 .po）
./build_i18n.ps1 -BuildOnly
```

构建完成后用浏览器打开：

| 语言 | 路径 |
|------|------|
| 中文 | `build\html\index.html` |
| 英文 | `build\html\en\index.html` |

### 8.4 手动命令（等价）

```powershell
# 中文
sphinx-build -b html source build\html

# 英文（需先有 .mo）
cd source && sphinx-intl build -l en && cd ..
sphinx-build -b html -D language=en source build\html\en
```

---

## 9. Read the Docs 线上发布

### 9.1 架构说明

```
GitHub 仓库 (aithinker-faq)
        │
        ├─▶ RTD 项目 A（中文，Language = zh_CN）
        │       构建 URL: /zh-cn/latest/
        │
        └─▶ RTD 项目 B（英文，Language = en）
                构建 URL: /en/latest/
                读取 locale/en/*.mo 显示英文
```

两个项目导入**同一个仓库**，通过 **Translations 关联** 后，页面右下角会出现语言切换。

### 9.2 首次配置 checklist

**中文主项目：**

1. RTD 导入 GitHub 仓库
2. `Admin → Settings → Language` → **Simplified Chinese (zh_CN)**
3. 确认使用 `.readthedocs.yaml` 配置

**英文项目：**

1. `Dashboard → Add project` → 导入**同一仓库**（建议命名 `aithinker-faq-en`）
2. `Admin → Settings → Language` → **English (en)**
3. 回到**中文主项目** → `Admin → Translations → Add translation` → 选择英文项目

### 9.3 `.readthedocs.yaml` 关键配置说明

```yaml
formats: []                    # 不构建 PDF/EPUB（FAQ 不适合 PDF，且中文 LaTeX 易报错）

build:
  jobs:
    pre_build:
      - cd source && sphinx-intl build -l en   # 构建前把 .po 编译为 .mo
```

> RTD **不会**自动编译 `.po` → `.mo`，因此必须在 `pre_build` 里执行 `sphinx-intl build`，否则英文站可能仍显示中文。

### 9.4 日常发布

**正常流程：改完代码 → `git push` → RTD 自动构建**，无需手动点构建（Webhook 已配置时）。

可在 RTD 项目页查看 Build 日志排查失败原因。

### 9.5 关于 PDF

当前 **不构建 PDF**（`formats: []`）。原因：

- FAQ 体量大，PDF 构建慢且易失败
- 默认 LaTeX 无法处理中文 Unicode
- 英文站虽可翻译，但维护成本高、收益低

---

## 10. 常见问题排查

### Q1：英文站仍显示中文

| 可能原因 | 解决方法 |
|----------|----------|
| 只改了 `.po` 没编译 `.mo` | 执行 `cd source && sphinx-intl build -l en` |
| `msgstr` 为空 | 打开对应 `.po` 填写英文 |
| RTD 英文项目 Language 未设为 `en` | 检查 RTD Admin → Settings |
| 未 push `.mo` 文件 | 把 `.mo` 一并 commit 推送（RTD pre_build 也会编译，但本地需同步） |

### Q2：RTD 构建报 LaTeX / Unicode 错误

说明开启了 PDF 构建。确认 `.readthedocs.yaml` 中：

```yaml
formats: []    # 正确：不构建 PDF
# 错误示例：formats: all  或  formats: [pdf]
```

`formats` 合法值只有 `htmlzip`、`pdf`、`epub`，**不能写 `html`**（HTML 默认就会构建）。

### Q3：RTD 报 Config validation error (formats)

同上，检查 `formats` 配置，不要写 `html`。

### Q4：本地构建报 ERROR: Undefined substitution

多出现在首页 `index.rst` 的图片导航。规则：

- 图片 substitution 名（如 `|instructions|_`）**不要用中文**，用英文内部名
- 只翻译下方文字链接（`` `使用说明`_ ``），不要翻译 substitution 名本身

### Q5：修改中文后 `.po` 里出现大量 `#~`  obsolete 条目

正常现象。`sphinx-intl update` 会标记旧译文为 obsolete，新 `msgid` 需重新填 `msgstr`。obsolete 条目不影响构建，可保留或手动删除。

### Q6：新增了 `.rst` 但导航里看不到

检查是否被父级 `index.rst` 的 `toctree` 引用：

```rst
.. toctree::
   :maxdepth: 1
   :glob:

   WiFi/*        ← 确保 glob 能匹配到你的新文件
```

### Q7：构建有很多 WARNING 但成功了

FAQ 仓库历史较长，部分页面存在标题下划线长度、链接 target 等警告，**通常不影响 HTML 发布**。若出现 **ERROR**（红色），则需要修复后再发布。

---

## 11. 术语表

| 术语 | 解释 |
|------|------|
| **Sphinx** | Python 文档生成工具，把 `.rst` 转成 HTML |
| **reST / RST** | reStructuredText，Sphinx 使用的标记语言 |
| **Read the Docs (RTD)** | 免费文档托管平台，连接 Git 自动构建 |
| **gettext / i18n** | 国际化机制，实现多语言 |
| **`.pot`** | 翻译模板（从 `.rst` 提取的中间文件，一般不提交 Git） |
| **`.po`** | 翻译编辑文件（人工维护） |
| **`.mo`** | 编译后的翻译文件（构建时读取） |
| **msgid** | `.po` 中的源语言字符串（中文） |
| **msgstr** | `.po` 中的译文（英文） |
| **toctree** | Sphinx 目录树指令，控制左侧导航 |
| **sphinx-intl** | Sphinx 国际化辅助工具 |
| **READTHEDOCS_LANGUAGE** | RTD 注入的环境变量，值为 `en` 或 `zh_CN` 等 |
