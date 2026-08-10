[![中文](https://img.shields.io/badge/中文-文档-blue)](VALIDATION.zh.md)

# Validation

## Reproduce the checks

```powershell
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install -r docs/requirements.txt
python tools/validate_repository.py
```

The validator checks:

1. Every `.rst` document has a corresponding English `.po` and `.mo` path, with no orphan catalogs.
2. Every active gettext message has a translation and no active message is marked fuzzy.
3. English catalogs compile successfully.
4. Fresh Simplified Chinese and English HTML builds succeed with Sphinx warnings treated as errors.

The last committed result is stored in `docs/validation-logs/Sphinx-validation.log`; machine-readable evidence is in `docs/technical-evidence.json`.

## Scope and limitations

This is a documentation repository, so there is no firmware compilation, device flashing, hardware-in-the-loop test, or runtime unit-test suite. The hosted configuration requests HTML only; optional PDF, EPUB, and HTML ZIP builders are outside the declared release surface. External sites are not availability-tested, so a passing run proves reST/catalog/build integrity but not the continued availability or correctness of third-party links.
