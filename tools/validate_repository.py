#!/usr/bin/env python3
"""Validate catalog coverage and strict bilingual Sphinx HTML builds."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from babel.messages import pofile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
LOCALE = SOURCE / "locale" / "en" / "LC_MESSAGES"


def document_keys() -> set[str]:
    return {p.relative_to(SOURCE).with_suffix("").as_posix() for p in SOURCE.rglob("*.rst")}


def catalog_keys(suffix: str) -> set[str]:
    return {p.relative_to(LOCALE).with_suffix("").as_posix() for p in LOCALE.rglob(f"*{suffix}")}


def check_catalogs() -> tuple[int, int, int, int, int, int]:
    docs = document_keys()
    po_keys = catalog_keys(".po")
    mo_keys = catalog_keys(".mo")
    problems: list[str] = []
    for label, keys in (("PO", po_keys), ("MO", mo_keys)):
        missing = sorted(docs - keys)
        orphan = sorted(keys - docs)
        if missing:
            problems.append(f"{label} missing: {', '.join(missing)}")
        if orphan:
            problems.append(f"{label} orphan: {', '.join(orphan)}")

    active = untranslated = fuzzy = 0
    for path in sorted(LOCALE.rglob("*.po")):
        with path.open("r", encoding="utf-8-sig") as stream:
            catalog = pofile.read_po(stream)
        for message in catalog:
            if not message.id:
                continue
            active += 1
            if not message.string:
                untranslated += 1
                problems.append(f"Untranslated: {path.relative_to(ROOT)} :: {message.id!r}")
            if "fuzzy" in message.flags:
                fuzzy += 1
                problems.append(f"Fuzzy: {path.relative_to(ROOT)} :: {message.id!r}")

    if problems:
        raise RuntimeError("\n".join(problems))
    return len(docs), len(po_keys), len(mo_keys), active, untranslated, fuzzy


def run(command: list[str], env: dict[str, str] | None = None) -> None:
    print("$", subprocess.list2cmdline(command), flush=True)
    completed = subprocess.run(command, cwd=ROOT, env=env, text=True)
    if completed.returncode:
        raise RuntimeError(f"Command failed with exit code {completed.returncode}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--keep-build", action="store_true", help="keep the temporary build directory")
    args = parser.parse_args()

    documents, po_count, mo_count, active, untranslated, fuzzy = check_catalogs()
    print(
        f"Catalogs: {documents} documents, {po_count} PO, {mo_count} MO, "
        f"{active} active messages, {untranslated} untranslated, {fuzzy} fuzzy"
    )

    sphinx_build = shutil.which("sphinx-build")
    sphinx_intl = shutil.which("sphinx-intl")
    if not sphinx_build or not sphinx_intl:
        raise RuntimeError("sphinx-build and sphinx-intl must be installed from docs/requirements.txt")

    run([sphinx_intl, "build", "-l", "en", "-d", str(SOURCE / "locale")])
    build_root = Path(tempfile.mkdtemp(prefix="aithinker-faq-validation-"))
    try:
        for language in ("zh_CN", "en"):
            env = os.environ.copy()
            env["READTHEDOCS_LANGUAGE"] = language
            run(
                [
                    sphinx_build,
                    "-q",
                    "-W",
                    "--keep-going",
                    "-E",
                    "-d",
                    str(build_root / f"doctrees-{language}"),
                    "-b",
                    "html",
                    str(SOURCE),
                    str(build_root / f"html-{language}"),
                ],
                env,
            )
            print(f"Strict HTML build passed: {language}")
    finally:
        if args.keep_build:
            print(f"Build output retained: {build_root}")
        else:
            shutil.rmtree(build_root, ignore_errors=True)

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
