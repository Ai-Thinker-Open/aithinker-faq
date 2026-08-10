[![中文](https://img.shields.io/badge/中文-文档-blue)](ARCHITECTURE.zh.md)

# Architecture

## Build flow

```text
source/index.rst + source/docs/**/*.rst
                 |
                 +-- zh_CN Sphinx build ------------------------> Chinese HTML
                 |
                 +-- gettext extraction --> locale/en/**/*.po
                                              |
                                              +-- sphinx-intl --> .mo
                                                                   |
                                      en Sphinx build <-------------+
                                              |
                                              +------------------> English HTML
```

`source/conf.py` selects the language from `READTHEDOCS_LANGUAGE`; local execution defaults to `zh_CN`. `gettext_compact = False` makes catalog paths mirror document paths, and `gettext_uuid = True` helps preserve translations when source line numbers move.

## Content hierarchy

The root `source/index.rst` links six category indexes: instructions, development environment, application solutions, software frameworks, hardware, and factory firmware. Category indexes use direct and globbed `toctree` entries to reach 46 source documents.

## Deployment boundary

`.readthedocs.yaml` uses Ubuntu 22.04 and Python 3.8, installs `docs/requirements.txt`, and compiles English catalogs before Sphinx runs. The declared output formats list is empty, so no optional PDF, EPUB, or HTML ZIP artifact is requested. Local validation follows the same HTML-only boundary.

## Generated and maintained artifacts

- Maintainers edit `.rst` and `.po` files.
- `sphinx-intl build -l en` generates tracked `.mo` files.
- Sphinx generates untracked `build/` output.
- `docs/validation-logs/` contains the committed result of the evidence run, not generated site output.
