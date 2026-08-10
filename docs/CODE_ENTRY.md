[![中文](https://img.shields.io/badge/中文-文档-blue)](CODE_ENTRY.zh.md)

# Code entry points

This repository is a Sphinx documentation application. It has no firmware or runtime service entry point.

| Entry | Role | Typical caller |
|---|---|---|
| `source/index.rst` | Root document and top-level navigation | Sphinx |
| `source/conf.py` | Language, gettext, source, theme, and output configuration | `sphinx-build` |
| `build_i18n.ps1` | Updates translations and/or builds both local HTML sites | Windows maintainer |
| `.readthedocs.yaml` | Selects the hosted OS/Python environment, dependencies, and catalog pre-build step | Read the Docs |
| `Makefile`, `make.bat` | Standard Sphinx make-mode wrappers | Local maintainer |
| `tools/validate_repository.py` | Strict catalog and bilingual HTML validation | Maintainer or CI |

Content begins at `source/index.rst`, whose hidden `toctree` reaches the six category indexes under `source/docs/`. English rendering uses the same source paths plus compiled catalogs under `source/locale/en/LC_MESSAGES/`.
