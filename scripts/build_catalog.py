#!/usr/bin/env python3
"""Build catalog-data.json and refresh official-map translatedAtSha from zh files."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "src/content/zh"
SRC = Path("/workspace/ha-contributors-official/src/content/docs")
MANIFEST = Path("/tmp/ha-official-md/_manifest.json")
CATALOG = ROOT / "src/lib/docs/catalog-data.json"
MAP = ROOT / "src/lib/docs/official-map.json"

AREAS = json.loads((ROOT / "src/lib/docs/catalog-data.json").read_text())["areas"] if (ROOT / "src/lib/docs/catalog-data.json").exists() else []

# fallback hardcoded if stub missing areas
if not AREAS:
    AREAS = json.loads(Path("/workspace/ha-contributors-handbook/src/lib/docs/catalog-data.json").read_text())["areas"]


def parse_fm(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    data = yaml.safe_load(text[3:end]) or {}
    body = text[end + 4 :].lstrip("\n")
    return data if isinstance(data, dict) else {}, body


def slug_of(rel: str) -> str:
    slug = rel.rsplit(".", 1)[0]
    if slug == "index":
        return "index"
    if slug.endswith("/index"):
        slug = slug[: -len("/index")]
    return slug


def zh_file(slug: str) -> Path:
    return ZH / f"{slug}.md"


def load_pages():
    pages = []
    for src in sorted(SRC.rglob("*")):
        if src.suffix not in {".md", ".mdx"}:
            continue
        rel = src.relative_to(SRC).as_posix()
        slug = slug_of(rel)
        src_fm, _ = parse_fm(src.read_text(encoding="utf-8"))
        zpath = zh_file(slug)
        if zpath.exists():
            zh_fm, _ = parse_fm(zpath.read_text(encoding="utf-8"))
        else:
            zh_fm = {}
        title = zh_fm.get("title") or src_fm.get("title") or slug
        desc = zh_fm.get("description") or src_fm.get("description") or ""
        sidebar_label = zh_fm.get("sidebarLabel") or title
        area = slug.split("/")[0]
        pages.append({
            "slug": slug,
            "title": title,
            "sidebarLabel": sidebar_label,
            "description": desc,
            "href": f"/{slug}",
            "officialUrl": f"https://contributors.home-assistant.io/{slug}/",
            "area": area,
            "order": src_fm.get("order"),
            "sidebarGroup": zh_fm.get("sidebarGroup") or src_fm.get("sidebarGroup"),
            "sidebarGroups": zh_fm.get("sidebarGroups") or src_fm.get("sidebarGroups") or [],
            "sidebarCollapse": bool(src_fm.get("sidebarCollapse") or zh_fm.get("sidebarCollapse")),
            "isIndex": src.name.startswith("index."),
            "translated": zpath.exists() and zpath.stat().st_size > 200,
        })
    return pages


class Folder:
    def __init__(self, name: str):
        self.name = name
        self.index = None
        self.pages = []
        self.folders = {}


def build_folder_tree(area: str, pages: list) -> Folder:
    root = Folder(area)
    for p in pages:
        if p["area"] != area:
            continue
        segs = p["slug"].split("/")[1:]
        folder_segs = segs if p["isIndex"] else segs[:-1]
        folder = root
        for s in folder_segs:
            folder = folder.folders.setdefault(s, Folder(s))
        if p["isIndex"]:
            folder.index = p
        else:
            folder.pages.append(p)
    return root


def title_from_name(name: str) -> str:
    return name.replace("-", " ").capitalize()


def folder_label(folder: Folder) -> str:
    if folder.index:
        return folder.index["sidebarLabel"] or folder.index["title"]
    return title_from_name(folder.name)


def sort_key(order, label):
    inf = 10**9
    o = inf if order is None else order
    return (o, str(label))


def page_link(p, label=None):
    return {
        "kind": "link",
        "slug": p["slug"],
        "title": label or p["sidebarLabel"] or p["title"],
        "href": p["href"],
    }


def folder_items(folder: Folder):
    items = []
    groups = {}
    for page in folder.pages:
        g = page.get("sidebarGroup")
        if g:
            groups.setdefault(g, []).append(page)
        else:
            items.append((page.get("order"), page["sidebarLabel"], page_link(page)))
    group_order = (folder.index or {}).get("sidebarGroups") or []
    for name, pages in groups.items():
        children = sorted(pages, key=lambda x: sort_key(x.get("order"), x["sidebarLabel"]))
        pos = group_order.index(name) if name in group_order else 10**9
        items.append((pos, name, {
            "kind": "folder",
            "title": name,
            "children": [page_link(c) for c in children],
        }))
    for name, sub in folder.folders.items():
        node = folder_node(sub)
        order = sub.index.get("order") if sub.index else None
        items.append((order, node["title"], node))
    items.sort(key=lambda x: sort_key(x[0], x[1]))
    return [it[2] for it in items]


def folder_node(folder: Folder):
    children = folder_items(folder)
    if folder.index:
        children = [page_link(folder.index, "概览")] + children
    if folder.index and folder.index.get("sidebarCollapse"):
        return {
            "kind": "folder",
            "title": folder_label(folder),
            "children": children,
            "collapsed": True,
            "href": folder.index["href"],
            "slug": folder.index["slug"],
        }
    return {"kind": "folder", "title": folder_label(folder), "children": children}


def area_nav(area: str, pages: list):
    root = build_folder_tree(area, pages)
    items = folder_items(root)
    if root.index:
        items = [page_link(root.index, "概览")] + items
    return items


def catalog_page(p):
    return {
        "slug": p["slug"],
        "title": p["title"],
        "description": p["description"],
        "href": p["href"],
        "officialUrl": p["officialUrl"],
        "area": p["area"],
    }


def main():
    pages = load_pages()
    areas = []
    if CATALOG.exists():
        areas = json.loads(CATALOG.read_text()).get("areas") or []
    nav = {}
    for a in areas:
        nav[a["id"]] = area_nav(a["id"], pages)
    data = {"areas": areas, "pages": [catalog_page(p) for p in pages], "navByArea": nav}
    CATALOG.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print("catalog pages", len(pages), "translated", sum(1 for p in pages if p["translated"]))

    if MAP.exists() and MANIFEST.exists():
        snap = json.loads(MAP.read_text())
        by_slug = {p["slug"]: p for p in pages}
        for d in snap.get("docs", []):
            if d.get("kind") != "official":
                continue
            p = by_slug.get(d["slug"])
            if p and p["translated"] and d.get("lastSeenSha"):
                d["translatedAtSha"] = d["lastSeenSha"]
        MAP.write_text(json.dumps(snap, ensure_ascii=False, indent=2) + "\n")
        print("official-map refreshed")


if __name__ == "__main__":
    main()
