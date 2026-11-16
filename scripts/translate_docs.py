#!/usr/bin/env python3
"""Ingest official Home Assistant contributor docs and emit Chinese markdown."""
from __future__ import annotations

import hashlib
import json
import random
import re
import sys
import time
import traceback
from pathlib import Path

import yaml

OFFICIAL_ORIGIN = "https://contributors.home-assistant.io"
OFFICIAL_REPO = "https://github.com/home-assistant/contributors.home-assistant.io"
OFFICIAL_SHA = "2438d1027111f842c63059e7c16ae634d5190408"
SRC_DOCS = Path("/workspace/ha-contributors-official/src/content/docs")
MD_DIR = Path("/tmp/ha-official-md")
ZH_ROOT = Path("/workspace/ha-contributors-handbook/src/content/zh")
CACHE_DIR = Path("/tmp/ha-trans-cache")
MANIFEST = MD_DIR / "_manifest.json"
CATALOG_OUT = Path("/workspace/ha-contributors-handbook/src/lib/docs/catalog-data.json")
MAP_OUT = Path("/workspace/ha-contributors-handbook/src/lib/docs/official-map.json")
FAIL_LOG = Path("/tmp/ha-trans-failures.json")

ADDITIVE_SLUGS = ["updates", "sitemap", "architecture-site", "blog"]

# Names and identifiers that must stay in English.
PROTECT_TERMS = [
    "Home Assistant Companion",
    "Home Assistant Cloud",
    "Home Assistant Core",
    "Supervisor API",
    "add-ons",
    "add-on",
    "Add-ons",
    "Add-on",
    "Home Assistant OS",
    "Home Assistant Yellow",
    "Home Assistant Green",
    "Home Assistant Voice",
    "Home Assistant Link",
    "Home Assistant Container",
    "Home Assistant Supervised",
    "Home Assistant Operating System",
    "Open Home Foundation",
    "Home Assistant",
    "Nabu Casa",
    "Zigbee2MQTT",
    "Z-Wave JS",
    "Z-Wave",
    "Zigbee",
    "Thread",
    "Matter",
    "Bluetooth",
    "MQTT",
    "WebSocket",
    "Lokalise",
    "GitHub Copilot",
    "GitHub",
    "Discord",
    "TypeScript",
    "JavaScript",
    "Python",
    "Supervisor",
    "Assist",
    "ESPHome",
    "HACS",
    "Apache License 2.0",
    "CC BY-NC-SA 4.0",
    "Creative Commons",
    "Contributor License Agreement",
    "pull request",
    "Pull Request",
    "pull requests",
    "Pull Requests",
]

# Common post-fixes when MT slips.
POST_FIX = [
    (re.compile(r"家庭助手"), "Home Assistant"),
    (re.compile(r"家庭助理"), "Home Assistant"),
    (re.compile(r"开源家庭基金会"), "Open Home Foundation"),
    (re.compile(r"开放家居基金会"), "Open Home Foundation"),
    (re.compile(r"测试测试版"), "测试 beta"),
    (re.compile(r"拉动请求"), "pull request"),
    (re.compile(r"拉取请求"), "pull request"),
    (re.compile(r"拉式请求"), "pull request"),
    (re.compile(r"Github"), "GitHub"),
    (re.compile(r"GITHUB"), "GitHub"),
    (re.compile(r"建筑学"), "架构"),
    (re.compile(r"伴随应用"), "伴侣应用"),
    (re.compile(r"配套应用"), "伴侣应用"),
    (re.compile(r"人工智能策略"), "AI 政策"),
    (re.compile(r"人工智能政策"), "AI 政策"),
    (re.compile(r"人工智能工具"), "AI 工具"),
    (re.compile(r"操作系统和 Supervisor"), "OS 与 Supervisor"),
    (re.compile(r"伴随构建"), "伴侣应用构建"),
    (re.compile(r"伴随应用"), "伴侣应用"),
    (re.compile(r"开放家庭平台"), "开放家居平台"),
    (re.compile(r"开放主机平台"), "开放家居平台"),
    (re.compile(r"开放家庭基金会"), "Open Home Foundation"),
    (re.compile(r"主管\s*API"), "Supervisor API"),
    (re.compile(r"家庭助理核心"), "Home Assistant Core"),
    (re.compile(r"家庭助手核心"), "Home Assistant Core"),
    (re.compile(r"第一次捐款"), "第一次贡献"),
    (re.compile(r"同伴应用"), "伴侣应用"),
    (re.compile(r"同伴构建"), "伴侣应用构建"),
    (re.compile(r"Android 同伴"), "Android 伴侣应用"),
    (re.compile(r"(?m)^(#+) (建筑|构造|结构)\s*$"), r"\1 架构"),
]

PUNCT_FOR_SLUG = re.compile(r"[\u2000-\u206F\u2E00-\u2E7F\\'\"!#$%&()*+,./:;<=>?@\[\]^`{|}~]")


HEADING_EN = {
    "Architecture": "架构",
    "Overview": "概览",
    "When to use": "何时使用",
    "When not to use": "何时不要使用",
    "Anatomy": "构成",
    "Variants": "变体",
    "Variant": "变体",
    "Appearance": "外观",
    "Behavior": "行为",
    "Accessibility": "无障碍",
    "Size": "尺寸",
    "States": "状态",
    "Next steps": "下一步",
    "Related": "相关",
    "Guides": "指南",
    "Reference": "参考",
    "How it works": "工作原理",
    "First contribution": "第一次贡献",
    "Get started": "开始",
    "Introduction": "简介",
    "Prerequisites": "前提条件",
    "Installation": "安装",
    "Configuration": "配置",
    "Debugging": "调试",
    "Testing": "测试",
    "Troubleshooting": "故障排除",
    "FAQ": "常见问题",
    "See also": "另见",
}

def github_slug(text: str) -> str:

    s = re.sub(r"<[^>]+>", "", text)
    s = s.lower()
    s = PUNCT_FOR_SLUG.sub("", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "section"



_mt_lock = __import__("threading").Lock()

def repair_markdown(text: str) -> str:
    """Restore heading/list breaks that MT often glues to the previous sentence."""
    text = re.sub(r"([^\n#])(#{1,6} )", r"\1\n\n\2", text)
    text = re.sub(r"^#\s*\n+# ", "## ", text, flags=re.M)
    text = re.sub(r"([。！？；])([-*] |\d+\. )", r"\1\n\n\2", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text

def sha12(data: bytes | str) -> str:
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()[:12]


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    raw = text[3:end]
    body = text[end + 4 :]
    if body.startswith("\n"):
        body = body[1:]
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        data = {}
    return data, body


def official_slug_from_rel(rel: str) -> str:
    slug = rel.rsplit(".", 1)[0]
    if slug == "index":
        return "index"
    if slug.endswith("/index"):
        slug = slug[: -len("/index")]
    return slug


def parse_official_md(text: str) -> tuple[str, str, str, str]:
    """Return title, description, source_url, body."""
    lines = text.replace("\r\n", "\n").split("\n")
    title = ""
    desc = ""
    source = ""
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].startswith("# "):
        title = lines[i][2:].strip()
        i += 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].startswith("> "):
        desc_lines = []
        while i < len(lines) and (lines[i].startswith(">") or lines[i] == ">"):
            desc_lines.append(re.sub(r"^>\s?", "", lines[i]))
            i += 1
        desc = " ".join(x.strip() for x in desc_lines).strip()
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].startswith("Source:"):
        source = lines[i].split(":", 1)[1].strip()
        i += 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    body = "\n".join(lines[i:]).strip() + "\n"
    return title, desc, source, body


def rewrite_href(href: str) -> str:
    href = href.strip()
    if not href:
        return href
    # fragment only
    if href.startswith("#"):
        return href
    official = href
    if href.startswith(OFFICIAL_ORIGIN):
        path = href[len(OFFICIAL_ORIGIN) :]
    elif href.startswith("/") and not href.startswith("//"):
        path = href
    else:
        return href
    # keep blog on the official site
    if path.startswith("/blog"):
        return OFFICIAL_ORIGIN + path
    path = re.sub(r"/index\.md(?:$|\?)", "/", path)
    path = re.sub(r"\.md(?:$|\?)", "/", path)
    # split hash
    if "#" in path:
        path, frag = path.split("#", 1)
        frag = "#" + frag
    else:
        frag = ""
    path = path.rstrip("/") or "/"
    return path + frag


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def rewrite_links_in_text(text: str) -> str:
    def repl(m: re.Match) -> str:
        label, href = m.group(1), m.group(2)
        return f"[{label}]({rewrite_href(href)})"

    return LINK_RE.sub(repl, text)


def attach_heading_anchors(english_body: str, chinese_body: str) -> str:
    """Copy github-slugger ids from English headings onto translated headings, in order."""
    eng_ids: list[str] = []
    seen: dict[str, int] = {}
    for line in english_body.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not m:
            continue
        raw = m.group(2)
        raw = re.sub(r"\s*\{#[A-Za-z0-9._-]+\}\s*$", "", raw)
        raw = re.sub(r"`([^`]+)`", r"\1", raw)
        raw = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", raw)
        raw = re.sub(r"[*_]", "", raw)
        base = github_slug(raw)
        n = seen.get(base, 0)
        seen[base] = n + 1
        eng_ids.append(base if n == 0 else f"{base}-{n}")

    out_lines = []
    idx = 0
    for line in chinese_body.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not m:
            out_lines.append(line)
            continue
        hashes, rest = m.group(1), m.group(2).rstrip()
        rest = re.sub(r"\s*(\{#[^}]+\}\s*)+$", "", rest)
        hid = eng_ids[idx] if idx < len(eng_ids) else github_slug(rest)
        idx += 1
        out_lines.append(f"{hashes} {rest} {{#{hid}}}")
    return "\n".join(out_lines)


def protect(text: str) -> tuple[str, list[str]]:
    holders: list[str] = []

    def stash(val: str) -> str:
        holders.append(val)
        return f"{{H{len(holders) - 1}}}"

    # fenced code
    text = re.sub(r"```[\s\S]*?```", lambda m: stash(m.group(0)), text)
    # inline code
    text = re.sub(r"`[^`]+`", lambda m: stash(m.group(0)), text)
    # images (keep whole thing)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", lambda m: stash(m.group(0)), text)
    # link URLs only
    def link_repl(m: re.Match) -> str:
        return f"[{m.group(1)}]({stash(m.group(2))})"

    text = LINK_RE.sub(link_repl, text)
    # bare urls
    text = re.sub(r"https?://[^\s)<>]+", lambda m: stash(m.group(0)), text)
    # html tags
    text = re.sub(r"</?[^>\n]+>", lambda m: stash(m.group(0)), text)
    # keep markdown structure tokens out of the translator
    text = re.sub(r"(?m)^(#{1,6} )", lambda m: stash(m.group(1)), text)
    text = re.sub(r"(?m)^((?:[\t ]*)(?:[-*] |\d+\. ))", lambda m: stash(m.group(1)), text)
    # protected terms, longer first (already sorted by length in list)
    for term in PROTECT_TERMS:
        if term in text:
            text = text.replace(term, stash(term))
    return text, holders


def restore(text: str, holders: list[str]) -> str:
    # run several times in case of nesting or MT spacing
    for _ in range(3):
        def repl(m: re.Match) -> str:
            i = int(m.group(1))
            if 0 <= i < len(holders):
                return holders[i]
            return m.group(0)

        new = re.sub(r"[\{\[\(【]\s*H\s*(\d+)\s*[\}\]\)】]", repl, text, flags=re.I)
        if new == text:
            break
        text = new
    return text


def post_fix(text: str) -> str:
    for pat, rep in POST_FIX:
        text = pat.sub(rep, text)
    return text


# ---------- translator ----------
_translator_name = "bing"
_last_call = 0.0


def _looks_like_token(s: str) -> bool:
    s = s.strip()
    if re.fullmatch(r"[A-Za-z0-9_-]{8,80}", s):
        return True
    # mostly token-like, no CJK
    if not re.search(r"[\u4e00-\u9fff]", s) and re.fullmatch(r"[A-Za-z0-9\s_-]{8,200}", s):
        return True
    return False


def _call_mt(text: str) -> str:
    """Translate one chunk. Prefer local Argos; fall back to online engines."""
    text = text.strip()
    if not text:
        return text
    if not re.search(r"[A-Za-z]{3,}", text):
        return text

    def _acceptable(out: str) -> str | None:
        out = (out or "").strip()
        if not out:
            return None
        if _looks_like_token(out):
            return text
        latin_words = re.findall(r"[A-Za-z]{3,}", text)
        latin_words = [w for w in latin_words if not re.fullmatch(r"H\d+", w)]
        if len(latin_words) >= 2 and not re.search(r"[\u4e00-\u9fff]", out):
            if len(text) < 120 or text.count(" ") < 8:
                return text
            return None
        return out

    try:
        import argostranslate.translate as at

        accepted = _acceptable(at.translate(text, "en", "zh"))
        if accepted is not None:
            return accepted
    except Exception:
        pass

    import fcntl
    import translators as ts

    global _last_call, _translator_name
    last_err = None
    if len(text) > 900:
        raise RuntimeError(f"chunk too long for Bing fallback: {len(text)}")
    lock_path = CACHE_DIR / ".mt.lock"
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with open(lock_path, "a+", encoding="utf-8") as lockf:
        fcntl.flock(lockf.fileno(), fcntl.LOCK_EX)
        try:
            for attempt in range(5):
                now = time.time()
                wait = 0.55 - (now - _last_call)
                if wait > 0:
                    time.sleep(wait)
                try:
                    engines = [("bing", "zh-Hans"), ("sogou", "zh"), ("alibaba", "zh")]
                    out = None
                    err = None
                    for eng, lang in engines:
                        try:
                            out = ts.translate_text(
                                text, translator=eng, from_language="en", to_language=lang
                            )
                            _translator_name = eng
                            break
                        except Exception as e:
                            err = e
                            continue
                    if out is None:
                        raise RuntimeError(err)
                    _last_call = time.time()
                    accepted = _acceptable(str(out) if out is not None else "")
                    if accepted is None:
                        raise RuntimeError(f"no CJK in translation: {str(out)[:60]}")
                    return accepted
                except Exception as e:
                    last_err = e
                    time.sleep(1.0 + attempt * 1.2 + random.random())
                    continue
        finally:
            fcntl.flock(lockf.fileno(), fcntl.LOCK_UN)
    raise RuntimeError(f"MT failed: {last_err}")


def cached_mt(text: str) -> str:
    key = sha12("v3|" + text)
    path = CACHE_DIR / f"{key}.txt"
    if path.exists():
        return path.read_text(encoding="utf-8")
    out = _call_mt(text)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(out, encoding="utf-8")
    tmp.replace(path)
    return out


def chunk_text(text: str, limit: int = 1800) -> list[str]:
    if len(text) <= limit:
        return [text] if text else []
    parts: list[str] = []
    # split by headings first
    blocks = re.split(r"(?=\n#{1,6} )", text)
    buf = ""
    for b in blocks:
        if len(buf) + len(b) <= limit:
            buf += b
            continue
        if buf:
            parts.extend(split_plain(buf, limit))
            buf = ""
        parts.extend(split_plain(b, limit))
    if buf:
        parts.extend(split_plain(buf, limit))
    return [p for p in parts if p]


def split_plain(text: str, limit: int) -> list[str]:
    if len(text) <= limit:
        return [text] if text else []
    paras = re.split(r"(\n{2,})", text)
    out: list[str] = []
    buf = ""
    for p in paras:
        if len(buf) + len(p) <= limit:
            buf += p
        else:
            if buf:
                out.append(buf)
            if len(p) <= limit:
                buf = p
            else:
                # hard split on lines
                lines = p.split("\n")
                buf = ""
                for ln in lines:
                    add = (ln + "\n")
                    if len(buf) + len(add) <= limit:
                        buf += add
                    else:
                        if buf:
                            out.append(buf.rstrip("\n"))
                        if len(add) <= limit:
                            buf = add
                        else:
                            for i in range(0, len(ln), limit):
                                out.append(ln[i : i + limit])
                            buf = ""
            # continue
    if buf:
        out.append(buf)
    return out


def translate_inline(text: str) -> str:
    """Translate a heading, paragraph, or list item while keeping markdown links/code intact."""
    if not text or not text.strip():
        return text
    leading = re.match(r"^\s*", text).group(0)
    trailing = re.search(r"\s*$", text).group(0)
    core = text[len(leading) : len(text) - len(trailing) or None]
    if not core:
        return text

    links: list[tuple[str, str]] = []

    def stash_link(m: re.Match) -> str:
        links.append((m.group(1), m.group(2)))
        return f"{{L{len(links) - 1}}}"

    core = LINK_RE.sub(stash_link, core)
    protected, holders = protect(core)
    # protect() also stashes links; we already extracted them. Remaining {H#} are code/terms.
    if not re.search(r"[A-Za-z]{3,}", protected):
        out = restore(protected, holders)
    else:
        chunks = chunk_text(protected, 1800)
        translated = []
        for ch in chunks:
            if not re.search(r"[A-Za-z]{3,}", ch):
                translated.append(ch)
            else:
                translated.append(cached_mt(ch))
        out = restore("".join(translated), holders)
    out = post_fix(out)

    def restore_link(m: re.Match) -> str:
        i = int(m.group(1))
        if 0 <= i < len(links):
            label, href = links[i]
            return f"[{translate_sentence(label)}]({href})"
        return m.group(0)

    out = re.sub(r"[\{\[\(]\s*L\s*(\d+)\s*[\}\]\)]", restore_link, out)
    return leading + out + trailing


def translate_markdown(text: str) -> str:
    if not text.strip():
        return text

    fences: list[str] = []

    def stash_fence(m: re.Match) -> str:
        fences.append(m.group(0))
        return f"\n\n@@@FENCE{len(fences) - 1}@@@\n\n"

    work = re.sub(r"```[\s\S]*?```", stash_fence, text)
    lines = work.split("\n")
    out_lines: list[str] = []
    i = 0

    def is_special(line: str) -> bool:
        s = line.strip()
        if not s:
            return True
        if re.fullmatch(r"@@@FENCE\d+@@@", s):
            return True
        if re.match(r"#{1,6} ", line):
            return True
        if line.startswith(">") or line == ">":
            return True
        if re.match(r"^(\s*)([-*] |\d+\. )", line):
            return True
        if line.startswith("|"):
            return True
        if re.fullmatch(r"---+", s):
            return True
        return False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            out_lines.append("")
            i += 1
            continue
        fm = re.fullmatch(r"@@@FENCE(\d+)@@@", stripped)
        if fm:
            out_lines.append(fences[int(fm.group(1))])
            i += 1
            continue
        hm = re.match(r"^(#{1,6}) +(.*)$", line)
        if hm:
            raw_title = hm.group(2).strip()
            title = HEADING_EN.get(re.sub(r"\s*\{#[^}]+\}\s*$", "", raw_title), None)
            if title is None:
                title = translate_inline(raw_title)
            title = re.sub(r"^(建筑|构造|结构)$", "架构", title.strip())
            out_lines.append(f"{hm.group(1)} {title}")
            i += 1
            continue
        if line.startswith(">") or line == ">":
            buf: list[str] = []
            while i < len(lines) and (lines[i].startswith(">") or lines[i] == ">"):
                buf.append(re.sub(r"^>\s?", "", lines[i]))
                i += 1
            prefix = buf[0] if buf else ""
            callout = re.match(r"^\[!(NOTE|TIP|WARNING|IMPORTANT|CAUTION)\]\s*$", prefix, re.I)
            if callout:
                trans = translate_inline("\n".join(buf[1:]))
                out_lines.append(f"> {prefix}")
                for ln in trans.split("\n"):
                    out_lines.append(f"> {ln}" if ln else ">")
            else:
                trans = translate_inline("\n".join(buf))
                for ln in trans.split("\n"):
                    out_lines.append(f"> {ln}" if ln else ">")
            continue
        if re.match(r"^(\s*)([-*] |\d+\. )", line):
            while i < len(lines):
                ln = lines[i]
                mark = re.match(r"^(\s*(?:[-*] |\d+\. ))(.*)$", ln)
                if mark:
                    out_lines.append(mark.group(1) + translate_inline(mark.group(2)))
                    i += 1
                    continue
                if not ln.strip() and i + 1 < len(lines) and re.match(r"^(\s+)([-*] |\d+\. )", lines[i + 1]):
                    out_lines.append("")
                    i += 1
                    continue
                # continuation line of a list item
                if ln.startswith("  ") or ln.startswith("\t"):
                    out_lines.append(ln[: len(ln) - len(ln.lstrip())] + translate_inline(ln.lstrip()))
                    i += 1
                    continue
                break
            continue
        if line.startswith("|"):
            while i < len(lines) and lines[i].startswith("|"):
                row = lines[i]
                if re.search(r"^[\s|\\:-]+$", row.replace("\\|", "")):
                    out_lines.append(row)
                else:
                    cells = re.split(r"(?<!\\)\|", row)
                    trans_cells = []
                    for idx, c in enumerate(cells):
                        if idx == 0 or idx == len(cells) - 1:
                            trans_cells.append(c)
                        else:
                            trans_cells.append(" " + translate_inline(c.strip()) + " " if c.strip() else c)
                    out_lines.append("|".join(trans_cells))
                i += 1
            continue
        if re.fullmatch(r"---+", stripped):
            out_lines.append(line)
            i += 1
            continue
        buf = [line]
        i += 1
        while i < len(lines) and not is_special(lines[i]):
            buf.append(lines[i])
            i += 1
        out_lines.append(translate_inline("\n".join(buf)))

    result = "\n".join(out_lines)
    result = post_fix(result)
    return result


def _chunks_lost_newlines(src, dst) -> bool:
    return False


def translate_sentence(text: str) -> str:
    if not text or not text.strip():
        return text
    protected, holders = protect(text)
    if not re.search(r"[A-Za-z]{3,}", protected):
        return restore(protected, holders)
    out = restore(cached_mt(protected), holders)
    return post_fix(out)


DEMO_RE = re.compile(
    r"^(Live demo of .+)$",
    re.M,
)


def annotate_demos(body: str, official_url: str) -> str:
    def repl(m: re.Match) -> str:
        line = m.group(1)
        # after translation this may already be Chinese; handle English source
        return (
            f"{line}\n\n"
            f"> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文]({official_url})。"
        )

    # English form before translation — we'll also handle after
    if "Live demo" in body or "交互式演示" in body or "实时演示" in body:
        if "完整可操作演示请看" not in body and official_url:
            # add a single note after the first demo mention
            body = re.sub(
                r"((?:Live demo[^\n]*|交互式演示[^\n]*|实时演示[^\n]*))",
                r"\1\n\n> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文]("
                + official_url
                + ")。",
                body,
                count=1,
            )
    return body


def write_zh(path: Path, fm: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # dump frontmatter
    dumped = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    text = f"---\n{dumped}\n---\n\n{body.rstrip()}\n"
    path.write_text(text, encoding="utf-8")


def zh_path_for_slug(slug: str) -> Path:
    if slug in ADDITIVE_SLUGS:
        return ZH_ROOT / f"{slug}.md"
    return ZH_ROOT / f"{slug}/index.md" if False else _zh_file(slug)


def _zh_file(slug: str) -> Path:
    # index pages stored as area/index.md or just start/index.md
    return ZH_ROOT / f"{slug}.md"


def load_pages() -> list[dict]:
    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    pages = []
    for item in man["pages"]:
        slug = item["slug"]
        src = Path(item["src"])
        md_file = MD_DIR / (slug.replace("/", "__") + ".md")
        raw_src = src.read_text(encoding="utf-8")
        fm, _src_body = parse_frontmatter(raw_src)
        official_text = md_file.read_text(encoding="utf-8")
        title, desc, source, body = parse_official_md(official_text)
        pages.append(
            {
                "slug": slug,
                "src": str(src),
                "fm": fm,
                "official_text": official_text,
                "title": title or fm.get("title") or slug,
                "description": desc or fm.get("description") or "",
                "source": source or f"{OFFICIAL_ORIGIN}/{slug}/",
                "body": body,
                "size": item.get("size") or len(official_text),
                "sha": item.get("sha256") or hashlib.sha256(official_text.encode()).hexdigest(),
                "is_index": src.name.startswith("index."),
            }
        )
    return pages


def process_page(p: dict) -> dict:
    official_url = p["source"].rstrip("/") + "/"
    # avoid double slash for origin
    if official_url == f"{OFFICIAL_ORIGIN}//":
        official_url = f"{OFFICIAL_ORIGIN}/"

    cat_title = CATALOG_TITLES.get(p["slug"]) or ""
    if re.search(r"[\u4e00-\u9fff]", cat_title):
        title_zh = cat_title
    else:
        title_zh = translate_sentence(p["title"])
    desc_zh = translate_sentence(p["description"])
    body = p["body"]
    body_zh = translate_markdown(body)
    body_zh = repair_markdown(body_zh)
    body_zh = attach_heading_anchors(p["body"], body_zh)
    body_zh = rewrite_links_in_text(body_zh)
    # leftover official absolute links (except those we want to keep official)
    body_zh = body_zh.replace(OFFICIAL_ORIGIN + "/blog/", "___KEEP_BLOG___")
    body_zh = body_zh.replace(OFFICIAL_ORIGIN + "/", "/")
    body_zh = body_zh.replace("___KEEP_BLOG___", OFFICIAL_ORIGIN + "/blog/")
    body_zh = annotate_demos(body_zh, official_url)

    fm = dict(p["fm"] or {})
    fm["title"] = title_zh
    fm["description"] = desc_zh
    if fm.get("sidebarLabel"):
        fm["sidebarLabel"] = translate_sentence(str(fm["sidebarLabel"]))
    if fm.get("sidebarGroup"):
        fm["sidebarGroup"] = translate_sentence(str(fm["sidebarGroup"]))
    if fm.get("sidebarGroups"):
        fm["sidebarGroups"] = [translate_sentence(str(x)) for x in fm["sidebarGroups"]]
    # term.ui only
    term = fm.get("term")
    if isinstance(term, dict) and term.get("ui"):
        term = dict(term)
        term["ui"] = translate_sentence(str(term["ui"]))
        fm["term"] = term

    # compose final markdown: heading + description line optional. We keep H1 from title.
    # Official body usually does not repeat H1 (export put H1 in header we stripped).
    h1 = f"# {title_zh} {{#{github_slug(p['title'])}}}\n\n"
    # if body already starts with the same heading, skip
    final_body = h1 + body_zh
    final_body = re.sub(r"\n{3,}", "\n\n", final_body)

    out_path = _zh_file(p["slug"])
    write_zh(out_path, fm, final_body)
    return {
        "slug": p["slug"],
        "title": title_zh,
        "description": desc_zh,
        "sidebarLabel": fm.get("sidebarLabel") or title_zh,
        "order": fm.get("order"),
        "sidebarGroup": fm.get("sidebarGroup"),
        "sidebarGroups": fm.get("sidebarGroups"),
        "sidebarCollapse": fm.get("sidebarCollapse"),
        "isIndex": p["is_index"],
        "officialUrl": official_url,
        "webPath": "/" + p["slug"] if p["slug"] != "index" else "/",
        "sha": (p["sha"] if len(p["sha"]) == 64 else hashlib.sha256(p["official_text"].encode()).hexdigest())[:12],
        "sha256": p["sha"] if len(p["sha"]) == 64 else hashlib.sha256(p["official_text"].encode()).hexdigest(),
        "size": p["size"],
        "fm": fm,
    }


# Wait, sha12 of hex is wrong. I'll just use first 12 of sha256 hex.
# Fix in caller below.

CATALOG_TITLES: dict[str, str] = {}
if CATALOG_OUT.exists():
    try:
        _cat = json.loads(CATALOG_OUT.read_text(encoding="utf-8"))
        CATALOG_TITLES = {p["slug"]: p["title"] for p in _cat.get("pages", []) if p.get("slug") and p.get("title")}
    except Exception:
        CATALOG_TITLES = {}


def main() -> int:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    ZH_ROOT.mkdir(parents=True, exist_ok=True)
    only = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    pages = load_pages()
    if only:
        pages = [p for p in pages if p["slug"] in only or any(p["slug"].startswith(s) for s in only)]
    # skip pages that already have a substantial Chinese file
    filtered = []
    skipped = 0
    for pg in pages:
        out = _zh_file(pg["slug"])
        if out.exists() and out.stat().st_size > 80:
            skipped += 1
            continue
        filtered.append(pg)
    pages = filtered
    print(f"pages={len(pages)} skipped_existing={skipped}", flush=True)
    results = []
    failures = []
    t0 = time.time()
    workers = 1
    from concurrent.futures import ThreadPoolExecutor, as_completed
    total = len(pages)
    done_n = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(process_page, p): p for p in pages}
        for fut in as_completed(futs):
            src = futs[fut]
            done_n += 1
            try:
                rec = fut.result()
                rec["sha"] = rec["sha256"][:12]
                results.append(rec)
                print(f"OK {done_n}/{total} {src['slug']} {rec['sha']}", flush=True)
            except Exception as e:
                traceback.print_exc()
                failures.append({"slug": src["slug"], "error": str(e)})
                print(f"FAIL {done_n}/{total} {src['slug']} {e}", flush=True)
                FAIL_LOG.write_text(json.dumps(failures, ensure_ascii=False, indent=2), encoding="utf-8")
    elapsed = time.time() - t0
    print(f"done ok={len(results)} fail={len(failures)} in {elapsed:.1f}s", flush=True)
    # meta for later catalog build even if partial
    meta_path = Path("/tmp/ha-trans-results.json")
    meta_path.write_text(json.dumps({"results": results, "failures": failures}, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
