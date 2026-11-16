#!/usr/bin/env python3
"""Repair garbled Chinese front matter, headings, and known runaway body dumps."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from zh_labels import is_bad, pick_label

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "src/content/zh"
SRC = Path("/workspace/ha-contributors-official/src/content/docs")

GLOBAL_SUBS = [
    (re.compile(r"建立起的均已将收到就这些的(?:\s*但这提供任何的+和的+的*)?"), "路线图"),
    (re.compile(r"仍在进行的(?:草的)+草?"), "警报器"),
    (re.compile(r"不用 页所提供的就有业已协商 为什么 就是的支持(?:支援)+"), "媒体与图片"),
    (re.compile(r"蓓丝卡及更多"), "自定义卡片及其他"),
    (re.compile(r"踌咕鹫衲ỡ turkey荚咀玄"), "模式"),
    (re.compile(r"更多信息ppe"), "更多信息"),
    (re.compile(r"建设一体化"), "构建集成"),
    (re.compile(r"整合质量尺度"), "集成质量等级"),
    (re.compile(r"核心和一体化"), "核心与集成"),
    (re.compile(r"写入文件"), "撰写文档"),
    (re.compile(r"哈西欧-阿东斯/巴希奥"), "hassio-addons/bashio"),
    (re.compile(r"衲子\s*"), ""),
    (re.compile(r"\[4\.a\(a\)的合格后[^\]]+\]\((/core/internals/auth/?)\)"), r"[认证](\1)"),
    (re.compile(r"^##\s*4\.a\(a\)的合格后.*$", re.M), "## 认证"),
    (re.compile(r"4\.a\(a\)的合格后[^\n]*"), "认证"),
    (re.compile(r"掌握的掌握的[^。\n]*有关的[^\n]*"), "只能阻塞的代码（例如没有异步支持的库）应通过 `hass.async_add_executor_job` 放到 executor 线程里运行。"),
    (re.compile(r"的的有关的的有关[^\n]*"), ""),
    (re.compile(r"咕噜咕+[^|\n]*"), "只读字典，存放额外信息。请保持可 JSON 序列化。"),
    (re.compile(r"ẹ/恪[^|\n]*"), "雾"),
    (re.compile(r"用的用用的用用的[^\n]*"), ""),
    (re.compile(r"的为的为的为[^\n]*"), ""),
    (re.compile(r"\.{5,}的\.{3,}[^\n]*"), ""),
    (re.compile(r"宵衲凸艳桦"), ""),
    (re.compile(r"\)\"\"\"\"\"\"的的的[^\n]*"), "熟悉家庭网络和开发、并且会写代码的人。"),
]


PAGE_BODIES = {
    "roadmap": '''---
title: 路线图
description: 想法如何在 Open Home Foundation 变成计划中的工作，当前在推进什么，以及你可以从哪里参与、影响接下来要做的事。
---

# 路线图 {#roadmap}

Home Assistant 上的多数工作并不需要先做规划：集成的缺陷修复或改进可以直接提交 pull request。更大的工作则不同。当一件事跨多个仓库、需要设计，或会改变人们每天使用 Home Assistant 的方式时，会放在 [Open Home Foundation](/glossary/open-home-foundation/) 的路线图上规划。

路线图不是一份带日期的功能清单。它描述项目接下来想解决的问题，并公开邀请大家在这些方向上贡献。其中的每项工作都发生在公开的 GitHub 仓库里，因此你可以全程跟进，也可以随时加入。

## 从这里开始 {#start-here}

- [你的第一次路线图贡献](/roadmap/first-contribution/)：提交功能请求，或为已有请求补充你的使用场景。
- [从构想到发布](/roadmap/how-it-works/)：完整路径——从基金会的目标，到功能请求、机会项（opportunity）、史诗（epic）、任务，再到随版本发布。文中会用一个真实例子从头到尾串起来。

## 正在进行的工作 {#what-is-being-worked-on}

- [路线图仓库](https://github.com/OpenHomeFoundation/roadmap) 存放机会项：基金会已决定着手解决的问题。
- [项目看板](https://ohf.to/roadmap) 可以一览这些机会项。
- [Epics](https://github.com/home-assistant/epics) 把一个机会项拆成若干阶段，任务落在实际开发的仓库里。
- 路线图进展会发布在 Home Assistant 博客的 [roadmap 分类](https://www.home-assistant.io/blog/categories/roadmap/)。

## 路线图与架构 {#the-roadmap-and-the-architecture}

路线图决定*做什么*。Home Assistant *怎么做*则由架构会议把关，它与路线图并列：无论来自路线图还是贡献者自己的想法，架构上的变更都需要该会议批准。[架构决策如何作出](/architecture/decisions/) 说明了这一侧。

## 该和谁交流 {#who-to-talk-to}

- **想法**请发到 [功能请求](https://github.com/home-assistant/feature-requests/discussions)，大家都可以投票和讨论。
- **针对某个机会项的评论**请写在 [路线图仓库](https://github.com/OpenHomeFoundation/roadmap) 对应的 issue 下。
- **关于某件事该如何实现的问题**请到 [架构讨论](https://github.com/home-assistant/architecture/discussions)，或 [Discord](https://www.home-assistant.io/join-chat) 的 **#developers** 频道。
''',
}


def parse_fm(text: str) -> tuple[dict, str, str]:
    if not text.startswith("---"):
        return {}, text, ""
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text, ""
    raw = text[3:end]
    try:
        data = yaml.safe_load(raw) or {}
    except yaml.YAMLError:
        data = {}
        for line in raw.splitlines():
            m = re.match(r"^([A-Za-z0-9_]+)\s*:\s*(.*)$", line)
            if not m:
                continue
            val = m.group(2).strip()
            if len(val) >= 2 and val[0] in "\"'" and val[-1] == val[0]:
                val = val[1:-1]
            data[m.group(1)] = val
    body = text[end + 4 :]
    return (data if isinstance(data, dict) else {}), body, raw


def official_src(slug: str) -> Path | None:
    for ext in (".md", ".mdx"):
        p = SRC / f"{slug}{ext}"
        if p.exists():
            return p
        p = SRC / f"{slug}/index{ext}"
        if p.exists():
            return p
    return None


def quote_yaml(value: str) -> str:
    if value is None:
        return '""'
    text = str(value)
    if any(c in text for c in ":#{}[]&*?|>!%@`'\"") or text != text.strip() or text.lower() in {"true", "false", "null"}:
        return json_style(text)
    return text


def json_style(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def replace_fm_scalar(raw: str, key: str, new: str) -> str:
    pattern = re.compile(
        rf"^{re.escape(key)}\s*:(?:[ \t]*[^\n]*\n(?:[ \t]+[^\n]*\n)*)",
        re.M,
    )
    replacement = f"{key}: {quote_yaml(new)}\n"
    if pattern.search(raw):
        return pattern.sub(replacement, raw, count=1)
    return raw.rstrip() + f"\n{key}: {quote_yaml(new)}\n"


def fix_first_heading(body: str, title: str) -> str:
    m = re.match(r"(\s*#\s+)([^\n{]+?)(\s*\{#[^}]+\})?", body)
    if not m:
        return body
    current = m.group(2).strip()
    if is_bad(current) or current in {"联合国", "芭蕉", "警卫", "写入文件", "建设一体化", "整合质量尺度", "更多信息ppe"}:
        mid = f"{m.group(1)}{title}"
        if m.group(3):
            mid += f" {m.group(3)}"
        return mid + body[m.end() :]
    return body


def apply_global(text: str) -> str:
    for pat, repl in GLOBAL_SUBS:
        text = pat.sub(repl, text)
    # leftover runaway runs
    text = re.sub(r"(的){6,}", "的", text)
    text = re.sub(r"(支援){3,}", "", text)
    text = re.sub(r"(等等){3,}", "", text)
    text = re.sub(r"、{3,}", "", text)
    return text


GLOSSARY_ROADMAP = '''# 路线图 {#roadmap}

路线图不是一份带日期的功能清单。它是一组 [机会项（opportunity）](/glossary/opportunity/)，每一项都是值得解决的问题，由基金会的产品团队管理。社区的功能请求会汇入其中，每个机会项都关联基金会的一项目标。参见 [从构想到发布](/roadmap/how-it-works/)。
'''

EVENT_LOOP_BODY = '''# 事件循环 {#event-loop}

- 代码：`async_`、`hass.async_add_executor_job`
- 另见：asyncio、executor

以 `async_` 开头的函数在事件循环中运行，并且绝不能阻塞。只能阻塞的代码（例如没有异步支持的库）应通过 `hass.async_add_executor_job` 放到 executor 线程里运行。

## 相关术语 {#related-terms}

- [Home Assistant Core](/glossary/core)：位于 Home Assistant 核心的 Python 应用程序及其所有集成，代码在 `home-assistant/core` 仓库中。
- [hass 对象](/glossary/hass)：集成获得的 `HomeAssistant` 实例，用于访问状态机、事件总线、动作和配置。
'''


def rewrite_keep_fm(original: str, new_body: str, title: str, description: str | None = None, sidebar_group: str | None = None) -> str:
    fm, _, raw = parse_fm(original)
    if not raw:
        raw = f"\ntitle: {quote_yaml(title)}\n"
    raw = replace_fm_scalar(raw, "title", title)
    if description:
        raw = replace_fm_scalar(raw, "description", description)
    if sidebar_group:
        raw = replace_fm_scalar(raw, "sidebarGroup", sidebar_group)
    body = new_body if new_body.lstrip().startswith("#") or new_body.lstrip().startswith("-") else new_body
    return f"---{raw}\n---\n\n{body.lstrip()}\n"


def special_pages(slug: str, text: str) -> str | None:
    if slug == "roadmap":
        return PAGE_BODIES["roadmap"]
    if slug == "glossary/roadmap":
        return rewrite_keep_fm(
            text,
            GLOSSARY_ROADMAP,
            "路线图",
            "Open Home Foundation 接下来希望在 Home Assistant 及其他项目中解决的问题，以机会项的形式记录在 OpenHomeFoundation/roadmap 仓库中。",
            "贡献",
        )
    if slug == "glossary/event-loop":
        return rewrite_keep_fm(
            text,
            EVENT_LOOP_BODY,
            "事件循环",
            "运行 Home Assistant Core 的 asyncio 循环。若代码在没有 await 的情况下等待网络，就会卡住其他所有任务。",
            "核心与集成",
        )
    if slug == "design/users":
        text = apply_global(text)
        text = text.replace("## 排出者 {#outgrowers}", "## 超越者 {#outgrowers}")
        text = text.replace("## 叮当工 {#tinkerers}", "## 折腾者 {#tinkerers}")
        text = text.replace("## 质询者 {#questioners}", "## 求问者 {#questioners}")
        if "熟悉家庭网络和开发" not in text:
            text = re.sub(
                r"(## 折腾者 \{#tinkerers\}\n\n)[^\n#]*",
                r"\1熟悉家庭网络和开发、并且会写代码的人。\n",
                text,
            )
        return text
    return None


def patch_front_matter(text: str, src_fm: dict) -> str:
    fm, body, raw = parse_fm(text)
    if not raw:
        return text
    changed = False
    new_title = pick_label(fm.get("title"), src_fm.get("title"))
    if new_title and new_title != str(fm.get("title") or "").strip():
        raw = replace_fm_scalar(raw, "title", new_title)
        changed = True
    else:
        new_title = str(fm.get("title") or new_title or "")
    en_label = src_fm.get("sidebarLabel")
    if en_label or is_bad(fm.get("sidebarLabel")):
        new_label = pick_label(fm.get("sidebarLabel"), en_label or src_fm.get("title"))
        if new_label and new_label != str(fm.get("sidebarLabel") or "").strip():
            if "sidebarLabel" in fm or is_bad(fm.get("sidebarLabel")):
                if "sidebarLabel" in fm:
                    raw = replace_fm_scalar(raw, "sidebarLabel", new_label)
                    changed = True
    if is_bad(fm.get("description")):
        desc = src_fm.get("description") or ""
        if desc:
            raw = replace_fm_scalar(raw, "description", desc)
            changed = True
    if src_fm.get("sidebarGroup"):
        new_g = pick_label(None, src_fm.get("sidebarGroup"))
        if new_g and (is_bad(fm.get("sidebarGroup")) or fm.get("sidebarGroup") != new_g):
            # only rewrite when existing is bad or we have an official group
            if is_bad(fm.get("sidebarGroup")) or fm.get("sidebarGroup") in {
                "捐款", "船", "董事会", "采摘者", "你说的", "黄金", "铂", "铜", "联合国", "核心和一体化",
            }:
                raw = replace_fm_scalar(raw, "sidebarGroup", new_g)
                changed = True
            elif fm.get("sidebarGroup") != new_g and src_fm.get("sidebarGroup"):
                raw = replace_fm_scalar(raw, "sidebarGroup", new_g)
                changed = True
    body2 = fix_first_heading(body, new_title)
    if changed or body2 != body:
        return f"---{raw}\n---{body2}"
    return text


def process(path: Path, slug: str) -> bool:
    original = path.read_text(encoding="utf-8")
    src = official_src(slug)
    src_fm, _, _ = parse_fm(src.read_text(encoding="utf-8")) if src else ({}, "", "")
    special = special_pages(slug, original)
    if special is not None:
        new = special if special.endswith("\n") else special + "\n"
    else:
        new = apply_global(original)
        new = patch_front_matter(new, src_fm or {})
        # Fix a few known bad first headings even after global
        fm, body, _ = parse_fm(new)
        title = pick_label(fm.get("title"), (src_fm or {}).get("title"))
        body2 = fix_first_heading(body, title)
        if body2 != body:
            end = new.find("\n---", 3)
            raw = new[3:end]
            new = f"---{raw}\n---{body2}"
    if new != original:
        path.write_text(new if new.endswith("\n") else new + "\n", encoding="utf-8")
        return True
    return False


def main():
    changed = []
    for path in sorted(ZH.rglob("*.md")):
        slug = path.relative_to(ZH).as_posix()[:-3]
        if process(path, slug):
            changed.append(slug)
    print(f"repaired {len(changed)} files")
    for s in changed:
        print(" ", s)


if __name__ == "__main__":
    main()
