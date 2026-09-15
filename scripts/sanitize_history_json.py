# -*- coding: utf-8 -*-
"""Keep only complete encyclopedia chapters and rewrite JSON cleanly."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANGS = ("en", "ur", "hi", "bn", "id")
FILES = ("seerah.json", "sahaba.json", "ghazawat.json")
FIELDS = ("title", "heading", "details")


def loc_complete(value):
    if not isinstance(value, dict):
        return False
    texts = []
    for key in LANGS:
        raw = value.get(key)
        if not isinstance(raw, str) or not raw.strip():
            return False
        texts.append(raw.strip())
    # Cut-off mid-generation: one language far shorter than English.
    en = texts[0]
    if len(en) >= 80:
        for other in texts[1:]:
            if len(other) < 20:
                return False
    return True


def item_complete(item):
    if not isinstance(item, dict):
        return False
    return all(loc_complete(item.get(field)) for field in FIELDS)


def chapter_complete(chapter):
    if not isinstance(chapter, dict):
        return False
    if chapter.get("chapter_id") is None and chapter.get("id") is None:
        return False
    if not all(loc_complete(chapter.get(field)) for field in FIELDS):
        return False
    items = chapter.get("items")
    if items is None:
        chapter["items"] = []
        return True
    if not isinstance(items, list):
        return False
    chapter["items"] = [item for item in items if item_complete(item)]
    return True


def sanitize(name):
    path = ROOT / "assets" / "json" / name
    raw = path.read_text(encoding="utf-8")
    data = json.loads(raw)
    if not isinstance(data, list):
        raise ValueError(f"{name} root must be a list")
    kept = []
    dropped = 0
    for chapter in data:
        if chapter_complete(chapter):
            kept.append(chapter)
        else:
            dropped += 1
    path.write_text(
        json.dumps(kept, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    json.loads(path.read_text(encoding="utf-8"))
    print(f"{name}: kept {len(kept)} chapters, dropped {dropped}")


if __name__ == "__main__":
    for file_name in FILES:
        sanitize(file_name)
