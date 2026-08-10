[![English](https://img.shields.io/badge/English-文档-green)](CODE_ENTRY.md)

# 代码入口

本仓库是 Sphinx 文档应用，不包含固件或常驻服务运行入口。

| 入口 | 作用 | 主要调用方 |
|---|---|---|
| `source/index.rst` | 根文档与顶层导航 | Sphinx |
| `source/conf.py` | 语言、gettext、源文件、主题和输出配置 | `sphinx-build` |
| `build_i18n.ps1` | 更新翻译并/或构建本地中英文 HTML | Windows 维护人员 |
| `.readthedocs.yaml` | 指定线上环境、依赖和翻译编译步骤 | Read the Docs |
| `Makefile`, `make.bat` | Sphinx make 模式包装入口 | 本地维护人员 |
| `tools/validate_repository.py` | 严格校验翻译目录与中英文 HTML | 维护人员或 CI |

内容从 `source/index.rst` 开始，其隐藏 `toctree` 连接到 `source/docs/` 下六个分类首页。英文站使用同一套源路径，叠加 `source/locale/en/LC_MESSAGES/` 下编译后的翻译目录。
