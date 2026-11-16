#!/usr/bin/env python3
"""Force-sync title/description/H1 from official English via Argos + glossary keep-list."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import translate_docs as t

ADDITIVE = {"home", "updates", "sitemap", "architecture-site", "blog"}

# Keep these titles in English (product / acronym pages).
KEEP_EN = {
    "apps/supervisor-api",
    "architecture/platform/cloud",
    "glossary/assist",
    "glossary/ci",
    "glossary/core",
    "glossary/hacs",
    "glossary/home-assistant-link",
    "glossary/home-assistant-os",
    "glossary/lokalise",
    "glossary/nabu-casa",
    "glossary/open-home-foundation",
    "glossary/supervisor-api",
    "glossary/supervisor",
    "os/operating-system/odroid",
    "os/operating-system",
    "os/supervisor",
}

TITLE_MAP = {
    "companion": "伴侣应用",
    "companion/apple": "Apple",
    "companion/android": "Android",
    "companion/first-contribution": "你的第一个伴侣应用贡献",
    "companion/mobile-app-api": "移动应用 API",
    "companion/mobile-app-api/encryption": "加密",
    "companion/mobile-app-api/notifications": "通知",
    "companion/mobile-app-api/sending-data": "发送数据",
    "companion/mobile-app-api/sensors": "传感器",
    "companion/mobile-app-api/setup": "连接与注册",
    "companion/mobile-app-api/webview": "WebView",
    "companion/android/submitting": "提交 Android pull request",
    "companion/android/testing": "测试 Android 应用",
    "companion/android/ui-architecture": "Android UI 架构",
    "companion/apple/architecture": "Apple 架构",
    "companion/apple/ci": "Apple 持续集成",
    "companion/apple/code-style": "Apple 代码风格",
    "companion/apple/get-started": "开始使用 Apple",
    "companion/apple/releases": "Apple 发布",
    "companion/apple/submitting": "提交 Apple pull request",
    "companion/apple/targets": "Apple 目标",
    "companion/apple/testing": "测试 Apple 应用",
    "core/development": "开发工作流",
    "core/development/catching-up": "保持分支最新",
    "core/development/checklist": "开发清单",
    "core/development/checks": "Linter、hassfest 与 CI",
    "core/development/deprecating": "弃用",
    "core/development/environment": "搭建开发环境",
    "core/development/input-validation": "校验输入",
    "core/development/labs": "Labs 预览功能",
    "core/development/review-process": "打开 pull request 之后",
    "core/development/reviewing": "审查 pull request",
    "core/development/style": "代码风格",
    "core/development/submitting": "提交 pull request",
    "core/development/testing": "运行测试",
    "core/development/tests": "编写测试",
    "core/development/tips": "提示与技巧",
    "core/development/typing": "类型提示",
    "core/development/versioning": "版本",
    "core/entities": "实体",
    "core/entities/icons": "图标",
}


def has_cjk(s: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", s or ""))


def looks_bad(s: str) -> bool:
    if not s:
        return True
    # Arabic / weird scripts from MT corruption
    if re.search(r"[\u0600-\u06FF\u0590-\u05FF]", s):
        return True
    if "该死" in s or "酩酊" in s or "锺" in s or "Andro表达" in s:
        return True
    return False


def main() -> int:
    fixed = 0
    for path in sorted(t.ZH_ROOT.rglob("*.md")):
        slug = str(path.relative_to(t.ZH_ROOT)).removesuffix(".md")
        if slug in ADDITIVE:
            continue
        official = t.MD_DIR / (slug.replace("/", "__") + ".md")
        if not official.exists():
            continue
        en_title, en_desc, _, _ = t.parse_official_md(official.read_text(encoding="utf-8"))
        raw = path.read_text(encoding="utf-8")
        fm, body = t.parse_frontmatter(raw)
        title = str(fm.get("title") or "")
        m = re.search(r"^#\s+(.+?)\s*$", body, re.M)
        h1_raw = m.group(1) if m else ""
        h1 = re.sub(r"\s*\{#[^}]+\}\s*$", "", h1_raw).strip()
        am = re.search(r"\{#[^}]+\}", h1_raw)
        anchor = f" {am.group(0)}" if am else (f" {{#{t.github_slug(en_title)}}}" if en_title else "")

        need = False
        if slug in KEEP_EN:
            new_title = en_title or title
        elif slug in TITLE_MAP:
            new_title = TITLE_MAP[slug]
        elif looks_bad(title) or not has_cjk(title) or not has_cjk(h1) or looks_bad(h1):
            # Prefer catalog Chinese title if any
            cat = t.CATALOG_TITLES.get(slug) or ""
            if has_cjk(cat) and not looks_bad(cat):
                new_title = cat
            else:
                new_title = t.translate_sentence(en_title or title or h1)
                new_title = t.post_fix(new_title)
                if looks_bad(new_title) or not has_cjk(new_title):
                    # last resort: keep English product-ish title
                    new_title = en_title or title or h1
            need = True
        else:
            new_title = title

        if title != new_title or h1 != new_title:
            need = True

        if not need and has_cjk(h1) and h1 == title and not looks_bad(title):
            continue

        fm["title"] = new_title
        if en_desc and (not fm.get("description") or looks_bad(str(fm.get("description"))) or not has_cjk(str(fm.get("description")))):
            fm["description"] = t.post_fix(t.translate_sentence(en_desc))
        # sync sidebarLabel if English/bad
        sl = str(fm.get("sidebarLabel") or "")
        if sl and (looks_bad(sl) or (not has_cjk(sl) and slug not in KEEP_EN and re.search(r"[A-Za-z]{3,}", sl))):
            fm["sidebarLabel"] = new_title if has_cjk(new_title) else t.post_fix(t.translate_sentence(sl))

        if m:
            body = re.sub(r"^#\s+.+?\s*$", f"# {new_title}{anchor}", body, count=1, flags=re.M)
        else:
            body = f"# {new_title}{anchor}\n\n" + body
        t.write_zh(path, fm, body)
        fixed += 1
        print(f"fixed {slug} -> {new_title}", flush=True)
    print(f"done fixed={fixed}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
