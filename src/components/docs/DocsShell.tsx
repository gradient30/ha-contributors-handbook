import { useEffect, useMemo, useRef, useState } from "react";
import { Link, useRouterState } from "@tanstack/react-router";
import { ChevronDown, Menu, Search, X } from "lucide-react";
import { cn } from "@/lib/cn";
import {
  ADDITIVE_NAV,
  AREA_GROUPS,
  AREAS,
  NAV_BY_AREA,
  areaIdOf,
  hrefFor,
  neighbors,
  officialUrlFor,
  pageBySlug,
  type DocLink,
  type NavNode,
} from "@/lib/docs/catalog";
import { OFFICIAL_DOCS_SITE } from "@/lib/docs/official-map";
import { getMarkdown, searchDocs } from "@/lib/docs/load";
import { extractToc, Markdown } from "./Markdown";
import { ThemeSwitch } from "./ThemeSwitch";
import { UpdateEntry } from "./UpdateEntry";
import { SitemapBoard } from "./SitemapBoard";
import { UpdateLogBoard } from "./UpdateLogBoard";
import { HomeBoard } from "./HomeBoard";
import { readStoredTheme } from "@/lib/theme";
import { UPDATE_LOGS } from "@/lib/docs/update-logs";

const SITEMAP_TOC = [{ id: "map-docs", text: "手册页", level: 2 }];

const UPDATES_TOC = [
  { id: "cadence", text: "例行更新", level: 2 },
  ...UPDATE_LOGS.map((l) => ({ id: l.id, text: l.title, level: 2 })),
  { id: "latest", text: "最近一次对照明细", level: 2 },
  { id: "history", text: "历史记录", level: 2 },
];

function NavList({
  nodes,
  current,
  onNavigate,
}: {
  nodes: NavNode[];
  current: string;
  onNavigate?: () => void;
}) {
  return (
    <nav className="space-y-1 pb-10">
      {nodes.map((node, i) => (
        <NavItem key={i} node={node} current={current} onNavigate={onNavigate} depth={0} />
      ))}
    </nav>
  );
}

function NavItem({
  node,
  current,
  onNavigate,
  depth = 0,
}: {
  node: NavNode;
  current: string;
  onNavigate?: () => void;
  depth?: number;
}) {
  if (node.kind === "label") {
    return (
      <div className="px-3 pt-3 text-xs font-medium tracking-[0.14em] text-fg-subtle uppercase">{node.title}</div>
    );
  }
  if (node.kind === "link") {
    const active = current === node.slug;
    return (
      <Link
        to={node.href}
        onClick={onNavigate}
        className={cn(
          "block rounded-sm px-3 py-2 leading-5 transition-colors",
          depth === 0 ? "text-sm font-medium" : "text-sm",
          active ? "bg-bg-subtle text-fg" : "text-fg-muted hover:bg-bg-subtle hover:text-fg",
        )}
      >
        {node.title}
      </Link>
    );
  }
  const contains = (n: NavNode): boolean => {
    if (n.kind === "link") return n.slug === current;
    if (n.kind === "folder") return n.slug === current || n.children.some(contains);
    return false;
  };
  const openDefault = contains(node);
  const [open, setOpen] = useState(openDefault);
  useEffect(() => {
    if (openDefault) setOpen(true);
  }, [openDefault]);

  if (node.collapsed && node.href) {
    const active = openDefault;
    return (
      <Link
        to={node.href}
        onClick={onNavigate}
        className={cn(
          "block rounded-sm px-3 py-2 leading-5 transition-colors",
          depth === 0 ? "text-[15px] font-semibold tracking-tight" : "text-sm",
          active ? "bg-bg-subtle text-fg" : depth === 0 ? "text-fg hover:bg-bg-subtle" : "text-fg-muted hover:bg-bg-subtle hover:text-fg",
        )}
      >
        {node.title}
      </Link>
    );
  }

  const isTop = depth === 0;

  return (
    <div>
      <button
        type="button"
        aria-expanded={open}
        aria-label={`${open ? "折叠" : "展开"} ${node.title}`}
        onClick={() => setOpen((v) => !v)}
        className={cn(
          "flex min-h-11 w-full items-center justify-between rounded-sm px-3 py-2 text-left transition-colors",
          isTop ? "text-[15px] font-semibold tracking-tight text-fg" : "text-sm font-medium",
          open ? "bg-bg-subtle text-fg" : isTop ? "text-fg hover:bg-bg-subtle/80" : "text-fg-muted hover:bg-bg-subtle hover:text-fg",
        )}
      >
        <span className="min-w-0 flex-1 pr-2">{node.title}</span>
        <span
          className={cn(
            "flex size-6 shrink-0 items-center justify-center rounded-sm border transition-colors duration-200",
            open ? "border-accent/40 bg-accent/15 text-accent" : "border-border text-fg-subtle",
          )}
          aria-hidden
        >
          <ChevronDown className={cn("size-3.5 transition-transform duration-200", open ? "rotate-0" : "-rotate-90")} />
        </span>
      </button>
      <div
        className={cn("grid transition-[grid-template-rows] duration-200 ease-out", open ? "grid-rows-[1fr]" : "grid-rows-[0fr]")}
        aria-hidden={!open}
      >
        <div className={cn("min-h-0 overflow-hidden", !open && "pointer-events-none")}>
          <div className={cn("ml-2 border-l pl-1 transition-colors duration-200", open ? "border-accent/35" : "border-border")}>
            {node.children.map((c, i) => (
              <NavItem key={i} node={c} current={current} onNavigate={onNavigate} depth={depth + 1} />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

function AreaSwitcher({ currentArea, onPick }: { currentArea?: string; onPick?: () => void }) {
  const [open, setOpen] = useState(false);
  const area = AREAS.find((a) => a.id === currentArea);
  return (
    <div className="mb-3 px-1">
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className="flex min-h-11 w-full items-center justify-between rounded-md border border-border bg-bg-elevated px-3 text-left text-sm text-fg hover:border-border-strong"
      >
        <span className="truncate">{area ? area.title : "选择分区"}</span>
        <ChevronDown className={cn("size-3.5 shrink-0 text-fg-subtle", open ? "rotate-180" : "")} />
      </button>
      {open ? (
        <div className="mt-2 max-h-[50vh] overflow-y-auto rounded-md border border-border bg-bg-elevated p-2">
          {AREA_GROUPS.map((g) => (
            <div key={g.id} className="mb-2">
              <div className="px-2 py-1 text-[11px] tracking-[0.14em] text-fg-subtle uppercase">{g.title}</div>
              {AREAS.filter((a) => a.group === g.id).map((a) => (
                <Link
                  key={a.id}
                  to={`/${a.id}`}
                  onClick={() => {
                    setOpen(false);
                    onPick?.();
                  }}
                  className={cn(
                    "block rounded-sm px-2 py-1.5 text-sm",
                    a.id === currentArea ? "bg-bg-subtle text-fg" : "text-fg-muted hover:bg-bg-subtle hover:text-fg",
                  )}
                >
                  {a.title}
                </Link>
              ))}
            </div>
          ))}
        </div>
      ) : null}
    </div>
  );
}

function SearchModal({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [q, setQ] = useState("");
  const hits = useMemo(() => searchDocs(q), [q]);
  useEffect(() => {
    if (!open) setQ("");
  }, [open]);
  if (!open) return null;
  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center bg-bg/70 px-3 pt-[12vh]" onClick={onClose}>
      <div
        className="w-full max-w-xl overflow-hidden rounded-lg border border-border bg-bg-elevated shadow-overlay"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center gap-2 border-b border-border px-3">
          <Search className="size-4 text-fg-subtle" />
          <input
            autoFocus
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder="搜索手册…"
            className="h-12 w-full bg-transparent text-sm text-fg outline-none placeholder:text-fg-subtle"
          />
          <kbd className="hidden rounded-xs border border-border px-1.5 py-0.5 text-xs text-fg-subtle sm:block">ESC</kbd>
        </div>
        <div className="max-h-[50vh] overflow-y-auto py-2">
          {q && hits.length === 0 ? (
            <p className="px-4 py-6 text-sm text-fg-subtle">没有匹配的章节。</p>
          ) : (
            hits.map((h) => (
              <Link
                key={h.hash ? `${h.slug}#${h.hash}` : h.slug}
                to={hrefFor(h.slug)}
                hash={h.hash ?? ""}
                onClick={onClose}
                className="block px-4 py-2.5 hover:bg-bg-subtle"
              >
                <div className="text-sm text-fg">{h.titleLine}</div>
                <div className="mt-0.5 line-clamp-2 text-xs text-fg-subtle">{h.snippet}</div>
              </Link>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

function scrollToHash(raw: string, scroller?: HTMLElement | null) {
  const id = decodeURIComponent(raw.replace(/^#/, ""));
  if (!id) {
    (scroller ?? window).scrollTo({ top: 0 });
    return;
  }
  const el = document.getElementById(id);
  if (!el) return;
  if (scroller && scroller.contains(el)) {
    const top = el.getBoundingClientRect().top - scroller.getBoundingClientRect().top + scroller.scrollTop - 8;
    scroller.scrollTo({ top: Math.max(0, top), behavior: "smooth" });
    return;
  }
  el.scrollIntoView({ behavior: "smooth", block: "start" });
}

export function DocsShell({ slug }: { slug: string }) {
  const page = pageBySlug(slug);
  const md = getMarkdown(slug) ?? (slug === "home" ? "" : `# 未找到\n\n该章节尚未载入。`);
  const toc = useMemo(() => {
    if (slug === "sitemap") return SITEMAP_TOC;
    if (slug === "updates") return UPDATES_TOC;
    if (slug === "home") {
      return [
        { id: "intro", text: "这是什么系统", level: 2 },
        { id: "scenarios", text: "应用场景", level: 2 },
        { id: "levels", text: "按程度开始", level: 2 },
        { id: "beginner", text: "入门", level: 3 },
        { id: "advanced", text: "进阶", level: 3 },
        { id: "geek", text: "极客", level: 3 },
        { id: "areas", text: "分区", level: 2 },
      ];
    }
    return extractToc(md);
  }, [md, slug]);
  const { prev, next } = neighbors(slug);
  const [drawer, setDrawer] = useState(false);
  const [search, setSearch] = useState(false);
  const [colorful, setColorful] = useState(false);
  const mainRef = useRef<HTMLElement>(null);
  const hash = useRouterState({ select: (s) => s.location.hash });
  const areaId = areaIdOf(slug);
  const officialUrl = slug === "home" || slug === "blog" ? OFFICIAL_DOCS_SITE + (slug === "blog" ? "/blog/" : "/") : officialUrlFor(slug);

  const sidebarNodes: NavNode[] = [
    ...ADDITIVE_NAV,
    { kind: "label", title: areaId ? (AREAS.find((a) => a.id === areaId)?.title ?? "文档") : "分区" },
    ...(areaId
      ? (NAV_BY_AREA[areaId] ?? [])
      : AREAS.map((a) => ({ kind: "link" as const, slug: a.id, title: a.title, href: `/${a.id}` }))),
  ];

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setSearch(true);
      }
      if (e.key === "Escape") {
        setSearch(false);
        setDrawer(false);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  useEffect(() => {
    setDrawer(false);
  }, [slug]);

  useEffect(() => {
    const t = window.setTimeout(() => scrollToHash(hash || window.location.hash, mainRef.current), 40);
    return () => window.clearTimeout(t);
  }, [slug, hash, md]);

  useEffect(() => {
    const onHash = () => scrollToHash(window.location.hash, mainRef.current);
    window.addEventListener("hashchange", onHash);
    return () => window.removeEventListener("hashchange", onHash);
  }, []);

  useEffect(() => {
    const sync = () => setColorful(readStoredTheme() === "color");
    sync();
    const observer = new MutationObserver(sync);
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
    return () => observer.disconnect();
  }, []);

  return (
    <div className="flex h-svh flex-col overflow-hidden bg-bg text-fg">
      <header
        className={cn(
          "z-40 flex h-12 shrink-0 items-center gap-2 overflow-visible border-b bg-bg/90 px-2 backdrop-blur-md sm:gap-3 sm:px-3 md:px-4",
          colorful ? "border-accent" : "border-border",
        )}
      >
        <button
          type="button"
          className="flex size-11 shrink-0 items-center justify-center rounded-sm text-fg-muted hover:bg-bg-subtle md:hidden"
          onClick={() => setDrawer(true)}
          aria-label="打开目录"
        >
          <Menu className="size-5" />
        </button>
        <Link to="/" className="flex min-w-0 items-center gap-2">
          <img src={`${import.meta.env.BASE_URL}favicon.svg`} alt="" className="size-7 shrink-0 rounded-sm" />
          <span className="hidden truncate font-medium tracking-tight sm:inline">HA 贡献者手册</span>
        </Link>
        <span className="hidden text-xs text-fg-subtle lg:inline">非官方中文译本</span>
        <div className="ml-auto flex min-w-0 items-center gap-1.5 sm:gap-2">
          <UpdateEntry />
          <ThemeSwitch />
          <button
            type="button"
            onClick={() => setSearch(true)}
            className="flex size-11 shrink-0 items-center justify-center gap-2 rounded-md border border-border bg-bg-elevated text-xs text-fg-subtle hover:text-fg sm:h-11 sm:w-auto sm:px-3"
          >
            <Search className="size-3.5" />
            <span className="hidden sm:inline">搜索</span>
            <kbd className="hidden rounded-xs border border-border px-1 font-mono text-xs md:inline">⌘K</kbd>
          </button>
          <a
            href={officialUrl}
            target="_blank"
            rel="noreferrer"
            className="hidden h-11 items-center rounded-md px-2 text-xs text-fg-subtle hover:text-fg lg:flex"
          >
            英文原文
          </a>
        </div>
      </header>

      <div className="mx-auto flex min-h-0 w-full max-w-[1320px] flex-1">
        <aside className="hidden h-full w-64 shrink-0 overflow-y-auto overscroll-contain border-r border-border px-2 py-5 md:block">
          <AreaSwitcher currentArea={areaId} />
          <NavList nodes={sidebarNodes} current={slug} />
        </aside>

        {drawer ? (
          <div className="fixed inset-0 z-50 md:hidden">
            <button className="absolute inset-0 bg-bg/70" aria-label="关闭目录" onClick={() => setDrawer(false)} />
            <div className="absolute inset-y-0 left-0 w-[min(20rem,86vw)] overflow-y-auto border-r border-border bg-bg px-2 py-4">
              <div className="mb-3 flex items-center justify-between px-2">
                <span className="text-sm font-medium">目录</span>
                <button type="button" className="flex size-11 items-center justify-center" onClick={() => setDrawer(false)}>
                  <X className="size-5" />
                </button>
              </div>
              <AreaSwitcher currentArea={areaId} onPick={() => setDrawer(false)} />
              <NavList nodes={sidebarNodes} current={slug} onNavigate={() => setDrawer(false)} />
            </div>
          </div>
        ) : null}

        <main ref={mainRef} className="min-h-0 min-w-0 flex-1 overflow-y-auto overscroll-contain px-4 py-8 sm:px-8 lg:px-10">
          {page ? <p className="text-xs tracking-wide text-fg-subtle">{page.description}</p> : null}
          {md ? <Markdown source={md} /> : null}
          {slug === "home" ? <HomeBoard /> : null}
          {slug === "updates" ? <UpdateLogBoard /> : null}
          {slug === "sitemap" ? <SitemapBoard /> : null}
          {slug !== "home" ? <Pager prev={prev} next={next} current={slug} /> : null}
          <p className="mt-12 text-xs leading-5 text-fg-subtle">
            非官方译本。官方文档由 Home Assistant / Open Home Foundation 发布。译文按 CC BY-NC-SA 4.0 共享。
          </p>
        </main>

        <aside className="hidden h-full w-52 shrink-0 overflow-y-auto overscroll-contain py-8 pr-4 xl:block">
          <div className="text-xs font-medium tracking-[0.14em] text-fg-subtle uppercase">本页</div>
          <ul className="mt-3 space-y-1.5">
            {toc.map((t) => (
              <li key={t.id}>
                <a
                  href={`#${t.id}`}
                  className={cn("block text-xs leading-5 text-fg-subtle hover:text-fg", t.level === 3 && "pl-3")}
                >
                  {t.text}
                </a>
              </li>
            ))}
          </ul>
        </aside>
      </div>
      <SearchModal open={search} onClose={() => setSearch(false)} />
    </div>
  );
}

function Pager({ prev, next, current }: { prev?: DocLink; next?: DocLink; current: string }) {
  return (
    <div className="mt-14 grid gap-3 border-t border-border pt-6 sm:grid-cols-2">
      {prev && prev.slug !== current ? (
        <Link to={prev.href} className="rounded-md border border-border bg-bg-elevated px-4 py-3 hover:border-border-strong">
          <div className="text-xs text-fg-subtle">上一篇</div>
          <div className="mt-1 text-sm text-fg">{prev.title}</div>
        </Link>
      ) : (
        <span className="hidden sm:block" />
      )}
      {next ? (
        <Link
          to={next.href}
          className="rounded-md border border-border bg-bg-elevated px-4 py-3 text-right hover:border-border-strong"
        >
          <div className="text-xs text-fg-subtle">下一篇</div>
          <div className="mt-1 text-sm text-fg">{next.title}</div>
        </Link>
      ) : null}
    </div>
  );
}
