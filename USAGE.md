[![中文](https://img.shields.io/badge/中文-README-blue)](USAGE.zh.md)

# AiThinker-FAQ repository guide

This guide is for maintainers who are new to Sphinx, gettext, or Read the Docs. It describes the repository as it is implemented today and gives a repeatable bilingual publishing workflow.

## 1. What this repository publishes

The repository contains the source of Ai-Thinker's searchable FAQ website. Questions are grouped by product family and topic, including development environments, software frameworks, hardware, application solutions, and factory firmware.

| Component | Purpose |
|---|---|
| `.rst` | Simplified Chinese source content |
| Sphinx | Converts the source tree to HTML |
| `.po` | Editable English gettext translations |
| `.mo` | Compiled catalogs consumed by Sphinx |
| Read the Docs | Hosted build and publication service |

## 2. Language model

There is one Chinese source tree, not a second English `.rst` tree:

```text
Chinese .rst
    └─ Sphinx gettext extraction
         └─ .po msgid (Chinese) + msgstr (English)
              └─ sphinx-intl build
                   └─ .mo
                        └─ English HTML build
```

`source/conf.py` reads `READTHEDOCS_LANGUAGE`. Values beginning with `en` select English; values beginning with `zh` select Simplified Chinese; local builds default to `zh_CN`.

## 3. Important directories and entry points

- `source/index.rst` is the root document and navigation entry.
- `source/docs/` contains the six top-level Chinese documentation categories.
- `source/locale/en/LC_MESSAGES/` mirrors the source document paths with `.po` and `.mo` files.
- `source/conf.py` configures Sphinx, gettext, the theme, and language selection.
- `docs/requirements.txt` pins the build toolchain.
- `.readthedocs.yaml` installs those dependencies and compiles English catalogs before a hosted build.
- `build_i18n.ps1` is the Windows maintenance entry point.
- `tools/validate_repository.py` performs strict bilingual validation.

See [CODE_ENTRY.md](docs/CODE_ENTRY.md) and [ARCHITECTURE.md](docs/ARCHITECTURE.md) for a maintainer-oriented map.

## 4. Writing an FAQ entry

Choose the `.rst` file that matches the product family and topic. Questions are normally section titles followed by their answers:

```rst
Does-this-placeholder-represent-the-question
--------------------------------------------

The answer belongs here.
```

In real content, use the Chinese question and make the underline at least as long as the rendered title. Keep a blank line around lists, literal blocks, directives, tables, and section boundaries. Use explicit links so underscores in URLs cannot be mistaken for reST reference targets:

```rst
`参考资料 <https://example.com/path_with_underscore>`__
```

Use double backticks for identifiers such as ``GLB_Set_System_CLK()``. Put images in the appropriate source directory or in `source/_static/`, and verify their relative paths with a strict build.

## 5. Updating a question and its translation

1. Edit the Chinese source `.rst` file.
2. Extract messages and update English catalogs:

   ```powershell
   ./build_i18n.ps1 -UpdateOnly
   ```

3. Open the corresponding `.po` file under `source/locale/en/LC_MESSAGES/`.
4. Translate every new `msgid` into its `msgstr`. Preserve reST markup, URLs, model names, commands, and code identifiers.
5. Compile `.po` files to `.mo` files:

   ```powershell
   Push-Location source
   sphinx-intl build -l en
   Pop-Location
   ```

6. Run strict repository validation:

   ```powershell
   python tools/validate_repository.py
   ```

7. Review and commit the related `.rst`, `.po`, and `.mo` files together.

Do not edit `msgid` manually. It is generated from the Chinese source. A `fuzzy` flag means gettext is uncertain about a reused translation; review it, correct the `msgstr`, and remove the flag before publishing.

## 6. Local builds

Install dependencies once in a virtual environment if possible:

```powershell
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -r docs/requirements.txt
```

Run the convenience script:

```powershell
./build_i18n.ps1             # update catalogs and build both languages
./build_i18n.ps1 -UpdateOnly # update and compile translations only
./build_i18n.ps1 -BuildOnly  # compile catalogs and build both languages only
```

The output paths are `build/html/index.html` for Chinese and `build/html/en/index.html` for English.

For an evidence-quality check, use `python tools/validate_repository.py`. It verifies source/catalog path parity, rejects active fuzzy or untranslated messages, compiles English catalogs, and builds both languages with warnings treated as errors.

## 7. Read the Docs deployment

The repository is intended to be imported into two linked Read the Docs projects:

| Project | Language setting | Content |
|---|---|---|
| Primary project | Simplified Chinese (`zh_CN`) | Chinese source |
| Translation project | English (`en`) | English gettext catalogs |

Link the English project from the primary project's Translations settings to expose the language switcher. `.readthedocs.yaml` runs `sphinx-intl build -l en` during `pre_build`, because `.po` files are not consumed directly. It requests HTML only; PDF, EPUB, and HTML ZIP are not part of the configured validation surface.

## 8. Troubleshooting

### English pages still contain Chinese

- Check that the active `.po` entry has a non-empty `msgstr`.
- Remove `fuzzy` only after reviewing the translation.
- Recompile `.mo` files.
- Confirm the English RTD project language is set to `en`.

### Sphinx reports an unknown target

Bare URLs containing underscores can be parsed as reference names. Convert them to explicit links, or use inline literals for code identifiers containing underscores.

### Sphinx reports a short title underline

Extend the underline character sequence. Chinese characters can require more display width than their code-point count suggests.

### A new page is absent from navigation

Ensure a parent `toctree` includes it, directly or through a matching `:glob:` pattern, then run strict validation.

### Dependency installation selects incompatible `sphinxcontrib` releases

Use the pinned `docs/requirements.txt`. Sphinx 4.5 requires the compatible extension releases listed there; unpinned current 2.x extensions require newer Sphinx versions.

## 9. Submission checklist

- Chinese source and English translation describe the same answer.
- No active translation is empty or fuzzy.
- `.mo` files were regenerated from the committed `.po` files.
- `python tools/validate_repository.py` exits with code 0.
- Generated `build/`, virtual environments, editor state, and gettext backup files are not committed.

The latest recorded validation scope and limitations are documented in [VALIDATION.md](docs/VALIDATION.md).
