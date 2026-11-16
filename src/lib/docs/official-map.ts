import raw from "./official-map.json" with { type: "json" };

export const OFFICIAL_DOCS_SITE = "https://contributors.home-assistant.io";
export const LLMS_TXT = "https://contributors.home-assistant.io/llms.txt";
export const SITEMAP = "https://contributors.home-assistant.io/sitemap-0.xml";
export const OFFICIAL_REPO = "https://github.com/home-assistant/contributors.home-assistant.io";

export type DocKind = "official" | "additive";

export type DocFingerprint = {
  slug: string;
  section: string;
  kind: DocKind;
  officialPath: string | null;
  size: number | null;
  lastSeenSha: string | null;
  translatedAtSha: string | null;
  contentSha?: string | null;
  webPath?: string;
  officialUrl?: string;
};

export type MapSnapshot = {
  capturedAt: string;
  officialRef: string;
  docsTreeSha: string;
  source: string;
  docs: DocFingerprint[];
  releases: unknown[];
};

export const MAP_SNAPSHOT = raw as MapSnapshot;

export const SECTION_META: { id: string; title: string }[] = [
  { id: "additive", title: "本站加页" },
  { id: "start", title: "开始贡献" },
  { id: "core", title: "核心与集成" },
  { id: "frontend", title: "前端" },
  { id: "apps", title: "应用" },
  { id: "marketplace", title: "应用市场" },
  { id: "companion", title: "伴侣应用" },
  { id: "os", title: "OS 与 Supervisor" },
  { id: "design", title: "设计" },
  { id: "brand", title: "品牌" },
  { id: "writing", title: "撰写文档" },
  { id: "translate", title: "翻译" },
  { id: "community", title: "社区" },
  { id: "releases", title: "发布" },
  { id: "roadmap", title: "路线图" },
  { id: "architecture", title: "架构" },
  { id: "security", title: "安全" },
  { id: "data", title: "数据" },
  { id: "glossary", title: "术语表" },
  { id: "other", title: "未分区" },
];

export type OfficialBlob = { path: string; sha: string; size: number };

export type DocStatus = "match" | "stale" | "added" | "removed" | "additive";

export type DocRow = {
  slug: string;
  section: string;
  kind: DocKind;
  officialPath: string | null;
  liveSha: string | null;
  lastSeenSha: string | null;
  translatedAtSha: string | null;
  size: number | null;
  status: DocStatus;
  webPath: string;
  officialUrl: string | null;
};

export const ADDITIVE_SLUGS = new Set(["home", "updates", "sitemap", "architecture-site", "blog"]);

export function officialHref(slug: string): string {
  if (ADDITIVE_SLUGS.has(slug) || slug === "home" || slug === "index") {
    return `${OFFICIAL_DOCS_SITE}/`;
  }
  return `${OFFICIAL_DOCS_SITE}/${slug}/`;
}

export function handbookHref(slug: string): string {
  if (slug === "home" || slug === "index" || slug === "") return "/";
  if (ADDITIVE_SLUGS.has(slug)) return `/docs/${slug}`;
  return `/${slug}`;
}

export function mdHref(slug: string): string {
  if (ADDITIVE_SLUGS.has(slug) || slug === "home" || slug === "index") {
    return `${OFFICIAL_DOCS_SITE}/llms.txt`;
  }
  return `${OFFICIAL_DOCS_SITE}/${slug}/index.md`;
}

export function shortSha(sha: string | null | undefined): string {
  if (!sha) return "—";
  return sha.slice(0, 7);
}

export function compareDocs(snapshot: MapSnapshot, liveBlobs: OfficialBlob[] | null): DocRow[] {
  const liveBySlug = new Map<string, OfficialBlob>();
  if (liveBlobs) {
    for (const blob of liveBlobs) {
      const slug = blob.path.replace(/\/index\.md$/, "").replace(/\.md$/, "");
      liveBySlug.set(slug, blob);
    }
  }
  const rows: DocRow[] = [];
  const seen = new Set<string>();

  for (const doc of snapshot.docs) {
    seen.add(doc.slug);
    if (doc.kind === "additive") {
      rows.push({
        slug: doc.slug,
        section: doc.section,
        kind: "additive",
        officialPath: null,
        liveSha: null,
        lastSeenSha: null,
        translatedAtSha: null,
        size: null,
        status: "additive",
        webPath: doc.webPath ?? handbookHref(doc.slug),
        officialUrl: null,
      });
      continue;
    }
    const live = liveBlobs ? liveBySlug.get(doc.slug) : undefined;
    const compareSha = live?.sha ?? doc.lastSeenSha;
    let status: DocStatus;
    if (liveBlobs && !live) status = "removed";
    else if (!doc.translatedAtSha) status = "stale";
    else if (compareSha && compareSha !== doc.translatedAtSha) status = "stale";
    else status = "match";
    rows.push({
      slug: doc.slug,
      section: doc.section,
      kind: "official",
      officialPath: doc.officialPath,
      liveSha: live?.sha ?? null,
      lastSeenSha: doc.lastSeenSha,
      translatedAtSha: doc.translatedAtSha,
      size: live?.size ?? doc.size,
      status,
      webPath: doc.webPath ?? handbookHref(doc.slug),
      officialUrl: doc.officialUrl ?? officialHref(doc.slug),
    });
  }

  if (liveBlobs) {
    for (const blob of liveBlobs) {
      const slug = blob.path.replace(/\/index\.md$/, "").replace(/\.md$/, "");
      if (seen.has(slug)) continue;
      rows.push({
        slug,
        section: slug.split("/")[0] ?? "other",
        kind: "official",
        officialPath: blob.path,
        liveSha: blob.sha,
        lastSeenSha: null,
        translatedAtSha: null,
        size: blob.size,
        status: "added",
        webPath: handbookHref(slug),
        officialUrl: officialHref(slug),
      });
    }
  }

  return sortDocRows(rows);
}

export function sortDocRows(rows: DocRow[]): DocRow[] {
  const sectionRank = new Map(SECTION_META.map((s, i) => [s.id, i]));
  return [...rows].sort((a, b) => {
    const sa = sectionRank.get(a.section) ?? 99;
    const sb = sectionRank.get(b.section) ?? 99;
    if (sa !== sb) return sa - sb;
    return a.slug.localeCompare(b.slug);
  });
}

export function formatDriftList(docs: DocRow[]): string {
  const stale = docs.filter((d) => d.status === "stale" || d.status === "added" || d.status === "removed");
  if (stale.length === 0) return "对照表：手册均无待办。";
  const lines = ["手册待办："];
  for (const row of stale) {
    const from = shortSha(row.translatedAtSha);
    const to = shortSha(row.liveSha ?? row.lastSeenSha);
    lines.push(
      `- ${row.status === "added" ? "新页" : row.status === "removed" ? "已删" : "待更新"} ${row.slug}  中文站 ${row.webPath}  ${from} → ${to}`,
    );
  }
  return lines.join("\n");
}

export function bakedDocsAsBlobs(snapshot: MapSnapshot): OfficialBlob[] {
  return snapshot.docs
    .filter((d) => d.kind === "official" && d.lastSeenSha)
    .map((d) => ({
      path: d.officialPath ?? `${d.slug}/index.md`,
      sha: d.lastSeenSha as string,
      size: d.size ?? 0,
    }));
}
