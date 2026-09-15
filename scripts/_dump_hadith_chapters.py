#!/usr/bin/env python3
"""Dump unique hadith chapter names from the SQLite database."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "assets" / "databases" / "hadith.db"
OUT = ROOT / "scripts" / "_hadith_chapters.json"

con = sqlite3.connect(DB)
books = list(con.execute("SELECT id, name FROM books ORDER BY id"))
chapters = list(
    con.execute(
        "SELECT book_id, number, name FROM chapters ORDER BY book_id, number"
    )
)
unique = sorted({row[2] for row in chapters})
print("books", books)
print("chapter_count", len(chapters))
print("unique", len(unique))
print("max_len", max(len(n) for n in unique), max(unique, key=len))
print("empty", sum(1 for n in unique if not n.strip()))
print("intro", [c for c in chapters if c[2].lower() in ("introduction", "") or c[1] == 0])

OUT.write_text(
    json.dumps(
        {
            "books": [{"id": i, "name": n} for i, n in books],
            "chapters": [
                {"book_id": b, "number": n, "name": name} for b, n, name in chapters
            ],
            "unique": unique,
        },
        ensure_ascii=False,
        indent=2,
    ),
    encoding="utf-8",
)
print("wrote", OUT)
