[![中文](https://img.shields.io/badge/中文-README-blue)](README.zh.md)

# AiThinker-FAQ

Ai-Thinker's bilingual FAQ documentation site. It uses [Sphinx](https://www.sphinx-doc.org/) and the [Read the Docs theme](https://sphinx-rtd-theme.readthedocs.io/), and is configured for deployment on [Read the Docs](https://readthedocs.org/).

Simplified Chinese is the source language in `source/docs/**/*.rst`. English content is maintained in gettext catalogs under `source/locale/en/LC_MESSAGES/` and compiled to `.mo` files before the English site is built.

## Quick start

```powershell
# Install the pinned documentation dependencies.
python -m pip install -r docs/requirements.txt

# Update translations and build both languages.
./build_i18n.ps1

# Open these files in a browser:
# Chinese: build\html\index.html
# English: build\html\en\index.html
```

For the complete authoring and translation workflow, see [USAGE.md](USAGE.md). Technical maintainers can start with:

- [Code entry points](docs/CODE_ENTRY.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Validation evidence](docs/VALIDATION.md)

## Repository layout

```text
aithinker-faq/
├─ source/
│  ├─ conf.py                    Sphinx and language configuration
│  ├─ index.rst                  Documentation root
│  ├─ docs/                      Chinese FAQ sources
│  ├─ _static/                   Images and static assets
│  └─ locale/en/LC_MESSAGES/     English .po and compiled .mo catalogs
├─ docs/requirements.txt             Pinned build dependencies
├─ .readthedocs.yaml                 Hosted build configuration
├─ build_i18n.ps1                    Windows translation/build entry point
└─ tools/validate_repository.py      Strict local validation entry point
```

## Maintenance workflow

1. Edit the relevant Chinese `.rst` file under `source/docs/`.
2. Run `./build_i18n.ps1 -UpdateOnly`, translate every new `msgstr`, and compile the catalogs.
3. Run `python tools/validate_repository.py` and review its result before submitting changes.
4. Commit the `.rst`, `.po`, and generated `.mo` changes together.

The hosted configuration builds HTML only. PDF and EPUB are intentionally not enabled.

## Contact

1. Samples: <https://anxinke.taobao.com>
2. Product documents: <https://docs.ai-thinker.com>
3. Business cooperation: +86 755-29162996
4. Address: Rooms 403–405 and 408–410, Building C, Huafeng Smart Innovation Port, Gushu, Xixiang, Bao'an District, Shenzhen, China
