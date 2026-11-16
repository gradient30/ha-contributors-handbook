import data from "./catalog-data.json" with { type: "json" };
import { ADDITIVE_SLUGS, handbookHref, officialHref } from "./official-map";

export type AreaGroupId = "start" | "build" | "shape" | "run" | "understand";

export type Area = {
  id: string;
  title: string;
  action: string;
  description: string;
  group: AreaGroupId;
  icon: string;
};

export type DocLink = {
  slug: string;
  title: string;
  description: string;
  href: string;
  officialUrl?: string;
  area?: string;
};

export type NavNode =
  | { kind: "label"; title: string }
  | { kind: "link"; slug: string; title: string; href: string }
  | {
      kind: "folder";
      title: string;
      children: NavNode[];
      collapsed?: boolean;
      href?: string;
      slug?: string;
    };

export const AREA_GROUPS: { id: AreaGroupId; title: string }[] = [
  { id: "start", title: "从这里开始" },
  { id: "build", title: "构建软件" },
  { id: "shape", title: "设计、撰写与翻译" },
  { id: "run", title: "运转项目" },
  { id: "understand", title: "理解它如何工作" },
];

export const AREAS: Area[] = (data as { areas: Area[] }).areas;

export const PAGES: DocLink[] = (data as { pages: DocLink[] }).pages;

export const NAV_BY_AREA: Record<string, NavNode[]> = (data as { navByArea: Record<string, NavNode[]> })
  .navByArea;

export const ADDITIVE_PAGES: DocLink[] = [
  { slug: "updates", title: "同步日志", description: "每次对照官网后单独记一笔：改了什么、中文站在哪一页。", href: "/docs/updates" },
  { slug: "sitemap", title: "对照表", description: "每页官网指纹与中文站路径。", href: "/docs/sitemap" },
  { slug: "architecture-site", title: "本站架构", description: "阅读器如何对照官网并发布到 GitHub Pages。", href: "/docs/architecture-site" },
  { slug: "blog", title: "博客（官网）", description: "官方贡献者博客尚未汉化，入口指向原文。", href: "/docs/blog" },
];

export const ADDITIVE_NAV: NavNode[] = [
  { kind: "label", title: "本站" },
  ...ADDITIVE_PAGES.map((p) => ({ kind: "link" as const, slug: p.slug, title: p.title, href: p.href })),
];

export function hrefFor(slug: string): string {
  if (!slug || slug === "home" || slug === "index") return "/";
  if (ADDITIVE_SLUGS.has(slug)) return `/docs/${slug === "home" ? "" : slug}`.replace(/\/$/, "") || "/";
  if (["updates", "sitemap", "architecture-site", "blog"].includes(slug)) return `/docs/${slug}`;
  return `/${slug}`;
}

export function pageBySlug(slug: string): DocLink | undefined {
  const key = slug === "" || slug === "docs" ? "home" : slug.replace(/\/$/, "");
  if (key === "home" || key === "index") {
    return {
      slug: "home",
      title: "Home Assistant 贡献者手册",
      description: "官方贡献者文档的非官方简体中文译本。",
      href: "/",
      officialUrl: officialHref("home"),
    };
  }
  const additive = ADDITIVE_PAGES.find((p) => p.slug === key);
  if (additive) return additive;
  return PAGES.find((p) => p.slug === key);
}

export function areaIdOf(slug: string): string | undefined {
  if (!slug || slug === "home" || slug === "index") return undefined;
  if (["updates", "sitemap", "architecture-site", "blog"].includes(slug)) return undefined;
  const page = PAGES.find((p) => p.slug === slug);
  if (page?.area) return page.area;
  const head = slug.split("/")[0];
  if (AREAS.some((a) => a.id === head)) return head;
  return undefined;
}

function flattenNav(nodes: NavNode[]): DocLink[] {
  const out: DocLink[] = [];
  for (const n of nodes) {
    if (n.kind === "link") {
      out.push({ slug: n.slug, title: n.title, description: "", href: n.href });
    } else if (n.kind === "folder") {
      if (n.collapsed && n.slug && n.href) {
        out.push({ slug: n.slug, title: n.title, description: "", href: n.href });
      }
      out.push(...flattenNav(n.children));
    }
  }
  return out;
}

export function areaPages(areaId: string): DocLink[] {
  return flattenNav(NAV_BY_AREA[areaId] ?? []);
}

export function neighbors(slug: string): { prev?: DocLink; next?: DocLink } {
  const area = areaIdOf(slug);
  const list = area ? areaPages(area) : [...ADDITIVE_PAGES, ...PAGES];
  const i = list.findIndex((p) => p.slug === slug);
  if (i < 0) return {};
  return { prev: list[i - 1], next: list[i + 1] };
}

export function officialUrlFor(slug: string): string {
  const page = PAGES.find((p) => p.slug === slug);
  if (page?.officialUrl) return page.officialUrl;
  return officialHref(slug);
}

export { handbookHref };
