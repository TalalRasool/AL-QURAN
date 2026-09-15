#!/usr/bin/env python3
"""Generate lib/features/hadith/data/hadith_chapter_names.dart from TSV data."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TSV = ROOT / "scripts" / "hadith_chapter_i18n.tsv"
OUT = ROOT / "lib" / "features" / "hadith" / "data" / "hadith_chapter_names.dart"


def dart_escape(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace("'", "\\'")
        .replace("$", "\\$")
        .replace("\n", " ")
    )


def main() -> None:
    rows: dict[str, dict[str, str]] = {}
    for raw in TSV.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 5:
            raise SystemExit(f"Bad TSV row ({len(parts)} cols): {line[:80]!r}")
        en, ur, hi, bn, ident = [p.strip() for p in parts]
        rows[en] = {"ur": ur, "hi": hi, "bn": bn, "id": ident}

    names = list(rows)
    db_path = ROOT / "assets" / "databases" / "hadith.db"
    if db_path.exists():
        import sqlite3

        db_names = {
            row[0]
            for row in sqlite3.connect(db_path).execute(
                "SELECT DISTINCT name FROM chapters"
            )
        }
        missing = sorted(db_names - set(rows))
        extra = sorted(set(rows) - db_names)
        if missing:
            raise SystemExit(f"Missing {len(missing)} names, first: {missing[:8]}")
        if extra:
            print("Extra TSV keys (ok):", extra[:8])
        names = sorted(db_names)

    lines = [
        "// Generated from scripts/hadith_chapter_i18n.tsv. Do not edit by hand.",
        "const hadithChapterNames = <String, Map<String, String>>{",
    ]
    for en in names:
        tr = rows[en]
        lines.append(f"  '{dart_escape(en)}': {{")
        lines.append(f"    'ur': '{dart_escape(tr['ur'])}',")
        lines.append(f"    'hi': '{dart_escape(tr['hi'])}',")
        lines.append(f"    'bn': '{dart_escape(tr['bn'])}',")
        lines.append(f"    'id': '{dart_escape(tr['id'])}',")
        lines.append("  },")
    lines.append("};")
    lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT} ({len(names)} chapters)")


if __name__ == "__main__":
    main()
