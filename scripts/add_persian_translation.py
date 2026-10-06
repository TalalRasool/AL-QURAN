"""Add Persian full-ayah and word-by-word text to the offline Quran database.

Full ayahs: alquran.cloud edition fa.makarem (saved as assets/data/persian.json).
Word-by-word: Quran.com word translations with language=fa, aligned to the
existing ayah_words rows (verse-end markers are skipped).
"""

from __future__ import annotations

import json
import sqlite3
import time
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "assets" / "databases" / "quran_5_languages_wbw_full.db"
JSON_PATH = ROOT / "assets" / "data" / "persian.json"
CACHE_PATH = ROOT / "scripts" / "_fa_wbw_cache.json"
FULL_URL = "https://api.alquran.cloud/v1/quran/fa.makarem"


def fetch_json(url: str) -> dict:
    last_error: Exception | None = None
    for attempt in range(6):
        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "alquran-dev", "Accept": "application/json"},
            )
            with urllib.request.urlopen(request, timeout=120) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as error:
            last_error = error
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"failed to fetch {url}") from last_error


def load_full_translation() -> dict[tuple[int, int], str]:
    if JSON_PATH.exists() and JSON_PATH.stat().st_size > 1000:
        payload = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    else:
        payload = fetch_json(FULL_URL)
        JSON_PATH.write_text(
            json.dumps(payload, ensure_ascii=False),
            encoding="utf-8",
        )
        print("saved", JSON_PATH, flush=True)

    texts: dict[tuple[int, int], str] = {}
    for surah in payload["data"]["surahs"]:
        surah_number = int(surah["number"])
        for ayah in surah["ayahs"]:
            texts[(surah_number, int(ayah["numberInSurah"]))] = (
                f"{ayah.get('text') or ''}".strip()
            )
    return texts


def load_word_cache() -> dict[str, dict[str, list[str]]]:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    return {}


def save_word_cache(cache: dict[str, dict[str, list[str]]]) -> None:
    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")


def download_words(cache: dict[str, dict[str, list[str]]]) -> None:
    for chapter in range(1, 115):
        key = str(chapter)
        if key in cache and cache[key]:
            continue
        page = 1
        words_by_ayah: dict[str, list[str]] = {}
        while True:
            url = (
                "https://api.quran.com/api/v4/verses/by_chapter/"
                f"{chapter}?words=true&language=fa&per_page=50&page={page}"
                "&word_fields=text_uthmani,translation"
            )
            payload = fetch_json(url)
            for verse in payload.get("verses") or []:
                tokens: list[str] = []
                for word in verse.get("words") or []:
                    if word.get("char_type_name") != "word":
                        continue
                    translation = word.get("translation") or {}
                    tokens.append(f"{translation.get('text') or ''}".strip())
                words_by_ayah[str(verse["verse_number"])] = tokens
            next_page = (payload.get("pagination") or {}).get("next_page")
            if not next_page:
                break
            page = int(next_page)
            time.sleep(0.12)
        cache[key] = words_by_ayah
        save_word_cache(cache)
        print(f"chapter {chapter}: {len(words_by_ayah)} ayahs", flush=True)
        time.sleep(0.12)


def ensure_columns(connection: sqlite3.Connection) -> None:
    ayah_columns = {
        row[1] for row in connection.execute("PRAGMA table_info(ayahs)")
    }
    if "persian_full" not in ayah_columns:
        connection.execute(
            "ALTER TABLE ayahs ADD COLUMN persian_full TEXT NOT NULL DEFAULT ''"
        )
    word_columns = {
        row[1] for row in connection.execute("PRAGMA table_info(ayah_words)")
    }
    if "persian" not in word_columns:
        connection.execute(
            "ALTER TABLE ayah_words ADD COLUMN persian TEXT NOT NULL DEFAULT ''"
        )


def write_database(
    full: dict[tuple[int, int], str],
    cache: dict[str, dict[str, list[str]]],
) -> None:
    connection = sqlite3.connect(DB_PATH)
    try:
        ensure_columns(connection)
        missing_ayahs = 0
        for (surah_number, ayah_number), text in full.items():
            cursor = connection.execute(
                """
                UPDATE ayahs
                SET persian_full = ?
                WHERE surah_number = ? AND ayah_number = ?
                """,
                (text, surah_number, ayah_number),
            )
            if cursor.rowcount != 1:
                missing_ayahs += 1

        rows = connection.execute(
            """
            SELECT w.id, a.surah_number, a.ayah_number
            FROM ayah_words w
            JOIN ayahs a ON a.id = w.ayah_id
            ORDER BY a.surah_number, a.ayah_number, w.word_position
            """
        ).fetchall()
        grouped: dict[tuple[int, int], list[int]] = defaultdict(list)
        for word_id, surah_number, ayah_number in rows:
            grouped[(surah_number, ayah_number)].append(word_id)

        mismatched = 0
        updated_words = 0
        for (surah_number, ayah_number), word_ids in grouped.items():
            tokens = cache.get(str(surah_number), {}).get(str(ayah_number), [])
            if len(tokens) != len(word_ids):
                mismatched += 1
            for word_id, token in zip(word_ids, tokens):
                connection.execute(
                    "UPDATE ayah_words SET persian = ? WHERE id = ?",
                    (token, word_id),
                )
                updated_words += 1

        connection.commit()
        empty_full = connection.execute(
            "SELECT COUNT(*) FROM ayahs WHERE TRIM(persian_full) = ''"
        ).fetchone()[0]
        empty_words = connection.execute(
            "SELECT COUNT(*) FROM ayah_words WHERE TRIM(persian) = ''"
        ).fetchone()[0]
        sample = connection.execute(
            """
            SELECT a.persian_full, w.persian
            FROM ayahs a
            JOIN ayah_words w ON w.ayah_id = a.id
            WHERE a.surah_number = 1 AND a.ayah_number = 1
            ORDER BY w.word_position
            """
        ).fetchall()
        print("missing ayah rows", missing_ayahs)
        print("empty full", empty_full)
        print("mismatched ayah word counts", mismatched)
        print("updated words", updated_words)
        print("empty words", empty_words)
        print("sample", sample)
    finally:
        connection.close()


def main() -> None:
    full = load_full_translation()
    print("full ayahs", len(full), flush=True)
    cache = load_word_cache()
    download_words(cache)
    write_database(full, cache)


if __name__ == "__main__":
    main()
