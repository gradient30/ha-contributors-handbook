#!/usr/bin/env python3
"""Repair heading breaks, terminology, table rows, and official anchors on zh pages."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import translate_docs as td

ZH = Path(__file__).resolve().parents[1] / "src/content/zh"
MD = Path("/tmp/ha-official-md")

TERMS = [
    (re.compile(r"家庭助手"), "Home Assistant"),
    (re.compile(r"家庭助理"), "Home Assistant"),
    (re.compile(r"开源家庭基金会"), "Open Home Foundation"),
    (re.compile(r"开放家居基金会"), "Open Home Foundation"),
    (re.compile(r"测试测试版"), "测试 beta"),
    (re.compile(r"拉动请求"), "pull request"),
    (re.compile(r"拉取请求"), "pull request"),
    (re.compile(r"建筑学"), "架构"),
    (re.compile(r"伴随应用"), "伴侣应用"),
    (re.compile(r"配套应用"), "伴侣应用"),
    (re.compile(r"人工智能策略"), "AI 政策"),
    (re.compile(r"人工智能政策"), "AI 政策"),
    (re.compile(r"人工智能工具"), "AI 工具"),
    (re.compile(r"操作系统和 Supervisor"), "OS 与 Supervisor"),
    (re.compile(r"编写文档"), "撰写文档"),
]

# Title/sidebar overrides for well-known pages
TITLE_OVERRIDES = {
    "start": ("开始贡献", "概览"),
    "start/ai-policy": ("AI 政策", "AI 政策"),
    "start/ai-tools": ("用 AI 工具做贡献", "AI 工具"),
    "start/where-we-talk": ("我们在哪里交流", "我们在哪里交流"),
    "start/report-a-bug": ("报告错误", "报告错误"),
    "start/pull-requests": ("Pull request 与审查", "Pull request 与审查"),
    "architecture": ("架构", "概览"),
}


def apply_terms(text: str) -> str:
    for pat, rep in TERMS:
        text = pat.sub(rep, text)
    # 您 → 你, but not inside code fences / inline code
    parts = re.split(r"(```[\s\S]*?```|`[^`]+`)", text)
    for i, part in enumerate(parts):
        if part.startswith("```") or part.startswith("`"):
            continue
        part = part.replace("您的", "你的")
        part = part.replace("您", "你")
        parts[i] = part
    return "".join(parts)


def repair_tables(text: str) -> str:
    parts = re.split(r"(```[\s\S]*?```)", text)
    out = []
    for part in parts:
        if part.startswith("```"):
            out.append(part)
            continue
        part = re.sub(r"\| \| ", "|\n| ", part)
        part = re.sub(r"\|\| ", "|\n| ", part)
        out.append(part)
    return "".join(out)


def process(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    fm, body = td.parse_frontmatter(raw)
    rel = path.relative_to(ZH).as_posix()
    if rel.endswith(".md"):
        slug = rel[:-3]
    else:
        slug = rel
    official = MD / (slug.replace("/", "__") + ".md")
    body2 = td.repair_markdown(body)
    body2 = repair_tables(body2)
    body2 = apply_terms(body2)
    if official.exists():
        title, desc, source, eng_body = td.parse_official_md(official.read_text(encoding="utf-8"))
        body2 = re.sub(r"(#{1,6} .+?)\s*(\{#[^}]+\}\s*)+$", r"\1", body2, flags=re.M)
        body2 = td.attach_heading_anchors("# " + title + "\n\n" + eng_body, body2)
        body2 = td.rewrite_links_in_text(body2)
        if slug in TITLE_OVERRIDES:
            t, sl = TITLE_OVERRIDES[slug]
            fm["title"] = t
            if fm.get("sidebarLabel"):
                fm["sidebarLabel"] = sl
            # replace first H1 text, keep id
            body2 = re.sub(r"^# .+?(\s*\{#[^}]+\})", r"# " + t + r"\1", body2, count=1, flags=re.M)
        # term-fix titles
        if fm.get("title"):
            fm["title"] = apply_terms(str(fm["title"]))
        if fm.get("description"):
            fm["description"] = apply_terms(str(fm["description"]))
        if fm.get("sidebarLabel"):
            fm["sidebarLabel"] = apply_terms(str(fm["sidebarLabel"]))
        if fm.get("sidebarGroup"):
            fm["sidebarGroup"] = apply_terms(str(fm["sidebarGroup"]))
    new_raw = "---\n" + __import__("yaml").safe_dump(fm, allow_unicode=True, sort_keys=False).strip() + "\n---\n\n" + body2.rstrip() + "\n"
    if new_raw != raw:
        path.write_text(new_raw, encoding="utf-8")
        return True
    return False


def main() -> None:
    n = c = 0
    for path in sorted(ZH.rglob("*.md")):
        # skip handbook-only pages
        if path.name in {"home.md", "updates.md", "sitemap.md", "architecture-site.md", "blog.md"} and path.parent == ZH:
            continue
        n += 1
        if process(path):
            c += 1
    print(f"processed {n}, changed {c}")


if __name__ == "__main__":
    main()
