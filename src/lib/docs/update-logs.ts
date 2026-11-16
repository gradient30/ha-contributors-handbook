export type ChangeKind = "added" | "updated" | "removed" | "site";

export type UpdateChange = {
  kind: ChangeKind;
  slug: string;
  title: string;
  webPath: string;
  officialUrl?: string;
  detail: string;
};

export type UpdateLog = {
  id: string;
  date: string;
  title: string;
  summary: string;
  sourceHint: string;
  changes: UpdateChange[];
};

export const UPDATE_LOGS: UpdateLog[] = [
  {
    id: "2026-11-16-initial",
    date: "2026-11-16",
    title: "首次发布：18 个分区共 715 页汉化上线",
    summary: "对照官网 contributors.home-assistant.io，发布全部 18 个文档分区的简体中文译本（715 页）。官方博客本期未收入。",
    sourceHint: "https://contributors.home-assistant.io/llms.txt · https://contributors.home-assistant.io/sitemap-0.xml · 源仓库 main@2438d10",
    changes: [
      {
        kind: "site",
        slug: "home",
        title: "手册上线",
        webPath: "/",
        officialUrl: "https://contributors.home-assistant.io/",
        detail: "新建非官方中文阅读站，路径与官网分区对齐。中文站：/。",
      },
      {
        kind: "added",
        slug: "apps",
        title: "应用",
        webPath: "/apps",
        officialUrl: "https://contributors.home-assistant.io/apps/",
        detail: "汉化分区 应用：42 页。中文站：/apps。",
      },
      {
        kind: "added",
        slug: "architecture",
        title: "架构",
        webPath: "/architecture",
        officialUrl: "https://contributors.home-assistant.io/architecture/",
        detail: "汉化分区 架构：18 页。中文站：/architecture。",
      },
      {
        kind: "added",
        slug: "brand",
        title: "品牌",
        webPath: "/brand",
        officialUrl: "https://contributors.home-assistant.io/brand/",
        detail: "汉化分区 品牌：6 页。中文站：/brand。",
      },
      {
        kind: "added",
        slug: "community",
        title: "社区",
        webPath: "/community",
        officialUrl: "https://contributors.home-assistant.io/community/",
        detail: "汉化分区 社区：12 页。中文站：/community。",
      },
      {
        kind: "added",
        slug: "companion",
        title: "伴侣应用",
        webPath: "/companion",
        officialUrl: "https://contributors.home-assistant.io/companion/",
        detail: "汉化分区 伴侣应用：37 页。中文站：/companion。",
      },
      {
        kind: "added",
        slug: "core",
        title: "核心与集成",
        webPath: "/core",
        officialUrl: "https://contributors.home-assistant.io/core/",
        detail: "汉化分区 核心与集成：191 页。中文站：/core。",
      },
      {
        kind: "added",
        slug: "data",
        title: "数据",
        webPath: "/data",
        officialUrl: "https://contributors.home-assistant.io/data/",
        detail: "汉化分区 数据：14 页。中文站：/data。",
      },
      {
        kind: "added",
        slug: "design",
        title: "设计",
        webPath: "/design",
        officialUrl: "https://contributors.home-assistant.io/design/",
        detail: "汉化分区 设计：108 页。中文站：/design。",
      },
      {
        kind: "added",
        slug: "frontend",
        title: "前端",
        webPath: "/frontend",
        officialUrl: "https://contributors.home-assistant.io/frontend/",
        detail: "汉化分区 前端：37 页。中文站：/frontend。",
      },
      {
        kind: "added",
        slug: "glossary",
        title: "术语表",
        webPath: "/glossary",
        officialUrl: "https://contributors.home-assistant.io/glossary/",
        detail: "汉化分区 术语表：129 页。中文站：/glossary。",
      },
      {
        kind: "added",
        slug: "marketplace",
        title: "应用市场",
        webPath: "/marketplace",
        officialUrl: "https://contributors.home-assistant.io/marketplace/",
        detail: "汉化分区 应用市场：16 页。中文站：/marketplace。",
      },
      {
        kind: "added",
        slug: "os",
        title: "OS 与 Supervisor",
        webPath: "/os",
        officialUrl: "https://contributors.home-assistant.io/os/",
        detail: "汉化分区 OS 与 Supervisor：26 页。中文站：/os。",
      },
      {
        kind: "added",
        slug: "releases",
        title: "发布",
        webPath: "/releases",
        officialUrl: "https://contributors.home-assistant.io/releases/",
        detail: "汉化分区 发布：11 页。中文站：/releases。",
      },
      {
        kind: "added",
        slug: "roadmap",
        title: "路线图",
        webPath: "/roadmap",
        officialUrl: "https://contributors.home-assistant.io/roadmap/",
        detail: "汉化分区 路线图：3 页。中文站：/roadmap。",
      },
      {
        kind: "added",
        slug: "security",
        title: "安全",
        webPath: "/security",
        officialUrl: "https://contributors.home-assistant.io/security/",
        detail: "汉化分区 安全：15 页。中文站：/security。",
      },
      {
        kind: "added",
        slug: "start",
        title: "开始贡献",
        webPath: "/start",
        officialUrl: "https://contributors.home-assistant.io/start/",
        detail: "汉化分区 开始贡献：13 页。中文站：/start。",
      },
      {
        kind: "added",
        slug: "translate",
        title: "翻译",
        webPath: "/translate",
        officialUrl: "https://contributors.home-assistant.io/translate/",
        detail: "汉化分区 翻译：20 页。中文站：/translate。",
      },
      {
        kind: "added",
        slug: "writing",
        title: "撰写文档",
        webPath: "/writing",
        officialUrl: "https://contributors.home-assistant.io/writing/",
        detail: "汉化分区 撰写文档：17 页。中文站：/writing。",
      },
    ],
  },
];

export const LATEST_UPDATE = UPDATE_LOGS[0]!;

export function kindLabel(kind: ChangeKind): string {
  switch (kind) {
    case "added":
      return "新增";
    case "updated":
      return "更新";
    case "removed":
      return "移除";
    case "site":
      return "站点";
  }
}
