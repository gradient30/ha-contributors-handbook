#!/usr/bin/env python3
"""Re-translate English titles/descriptions/sidebar labels in existing zh files."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import translate_docs as t  # noqa: E402

ADDITIVE = {"home", "updates", "sitemap", "architecture-site", "blog"}
ZH = t.ZH_ROOT


def has_cjk(s: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", s or ""))


def main() -> int:
    n_title = n_desc = n_side = 0
    files = sorted(ZH.rglob("*.md"))
    for path in files:
        slug = str(path.relative_to(ZH)).removesuffix(".md")
        if slug in ADDITIVE:
            continue
        raw = path.read_text(encoding="utf-8")
        fm, body = t.parse_frontmatter(raw)
        # official title from official md if possible
        official = t.MD_DIR / (slug.replace("/", "__") + ".md")
        en_title = ""
        en_desc = ""
        if official.exists():
            en_title, en_desc, _, _ = t.parse_official_md(official.read_text(encoding="utf-8"))
        changed = False
        title = str(fm.get("title") or "")
        if title and not has_cjk(title):
            fm["title"] = t.translate_sentence(en_title or title)
            n_title += 1
            changed = True
        elif not title and en_title:
            fm["title"] = t.translate_sentence(en_title)
            n_title += 1
            changed = True
        desc = str(fm.get("description") or "")
        if desc and not has_cjk(desc) and (en_desc or desc):
            fm["description"] = t.translate_sentence(en_desc or desc)
            n_desc += 1
            changed = True
        for key in ("sidebarLabel", "sidebarGroup"):
            val = fm.get(key)
            if isinstance(val, str) and val and not has_cjk(val) and re.search(r"[A-Za-z]{3,}", val):
                fm[key] = t.translate_sentence(val)
                n_side += 1
                changed = True
        if isinstance(fm.get("sidebarGroups"), list):
            newg = []
            gch = False
            for x in fm["sidebarGroups"]:
                sx = str(x)
                if sx and not has_cjk(sx) and re.search(r"[A-Za-z]{3,}", sx):
                    newg.append(t.translate_sentence(sx))
                    n_side += 1
                    gch = True
                else:
                    newg.append(x)
            if gch:
                fm["sidebarGroups"] = newg
                changed = True
        # Fix H1 if English
        m = re.match(r"^#\s+(.+?)\s*$", body, re.M)
        if m:
            h1 = re.sub(r"\s*\{#[^}]+\}\s*$", "", m.group(1)).strip()
            if h1 and not has_cjk(h1):
                new_h = fm.get("title") or t.translate_sentence(h1)
                # preserve anchor
                am = re.search(r"\{#[^}]+\}", m.group(1))
                anchor = f" {am.group(0)}" if am else ""
                body = re.sub(r"^#\s+.+?\s*$", f"# {new_h}{anchor}", body, count=1, flags=re.M)
                changed = True
        if changed:
            t.write_zh(path, fm, body)
            print(f"fixed {slug}", flush=True)
    print(f"done titles={n_title} desc={n_desc} sidebar={n_side}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
