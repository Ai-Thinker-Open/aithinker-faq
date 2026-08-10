[![English](https://img.shields.io/badge/English-文档-green)](ARCHITECTURE.md)

# 架构说明

## 构建流程

```text
source/index.rst + source/docs/**/*.rst
                 |
                 +-- zh_CN Sphinx 构建 ---------------------> 中文 HTML
                 |
                 +-- gettext 提取 --> locale/en/**/*.po
                                         |
                                         +-- sphinx-intl --> .mo
                                                              |
                                  en Sphinx 构建 <--------+
                                         |
                                         +--------------------> 英文 HTML
```

`source/conf.py` 根据 `READTHEDOCS_LANGUAGE` 选择语言，本地默认为 `zh_CN`。`gettext_compact = False` 使翻译目录路径与文档路径镜像对应，`gettext_uuid = True` 用于在源文行号变化时尽量保留译文。

## 内容层级

根文档 `source/index.rst` 连接六个分类：使用说明、开发环境、应用方案、软件使用、硬件相关和出厂固件。各分类通过直接或 glob `toctree` 条目覆盖 46 个源文档。

## 部署边界

`.readthedocs.yaml` 使用 Ubuntu 22.04 和 Python 3.8，安装 `docs/requirements.txt` 后先编译英文目录。配置中额外输出格式列表为空，因此不请求 PDF、EPUB 或 HTML ZIP。本地校验也遵循这个仅 HTML 的边界。

## 生成物与维护对象

- 维护人员编辑 `.rst` 和 `.po`。
- `sphinx-intl build -l en` 生成并跟踪 `.mo`。
- Sphinx 生成不跟踪的 `build/` 输出。
- `docs/validation-logs/` 保存证据校验结果，不是站点构建输出。
