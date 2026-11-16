import { Link } from "@tanstack/react-router";
import {
  BookOpen,
  Calendar,
  Code2,
  Cpu,
  FileText,
  Flag,
  Globe,
  Layers,
  Layout,
  Map,
  MessageSquare,
  Package,
  PenTool,
  Shield,
  ShoppingBag,
  Smartphone,
  Tag,
  Users,
  type LucideIcon,
} from "lucide-react";
import { AREA_GROUPS, AREAS, type Area } from "@/lib/docs/catalog";

const ICONS: Record<string, LucideIcon> = {
  flag: Flag,
  code: Code2,
  layout: Layout,
  package: Package,
  "shopping-bag": ShoppingBag,
  smartphone: Smartphone,
  cpu: Cpu,
  pen: PenTool,
  message: MessageSquare,
  file: FileText,
  globe: Globe,
  users: Users,
  tag: Tag,
  map: Map,
  layers: Layers,
  shield: Shield,
  chart: BookOpen,
  book: BookOpen,
  calendar: Calendar,
};

function AreaTile({ area }: { area: Area }) {
  const Icon = ICONS[area.icon] ?? BookOpen;
  return (
    <Link
      to={`/${area.id}`}
      className="group flex flex-col rounded-lg border border-border bg-bg-elevated p-4 transition-colors hover:border-border-strong"
    >
      <div className="flex items-center gap-2">
        <span className="flex size-8 items-center justify-center rounded-sm border border-border bg-bg-subtle text-accent">
          <Icon className="size-4" />
        </span>
        <div className="min-w-0">
          <div className="font-medium text-fg">{area.title}</div>
          <div className="text-xs text-accent">{area.action}</div>
        </div>
      </div>
      <p className="mt-3 text-sm leading-6 text-fg-muted">{area.description}</p>
    </Link>
  );
}

export function HomeBoard() {
  return (
    <div className="mt-8 max-w-3xl space-y-10">
      <div className="rounded-md border border-border bg-bg-elevated px-4 py-3 text-sm leading-6 text-fg-muted">
        这是 <strong className="font-medium text-fg">非官方</strong> 简体中文译本，便于阅读，不替代官方文档。内容对照
        <a
          href="https://contributors.home-assistant.io/"
          target="_blank"
          rel="noreferrer"
          className="text-accent underline-offset-2 hover:underline"
        >
          contributors.home-assistant.io
        </a>
        ，由 Home Assistant 与 Open Home Foundation 维护原文。产品名、命令、代码和仓库路径保持英文。官方博客本期未汉化。
      </div>
      {AREA_GROUPS.map((group) => {
        const areas = AREAS.filter((a) => a.group === group.id);
        return (
          <section key={group.id}>
            <h2 className="font-display text-sm font-medium tracking-[0.14em] text-fg-subtle uppercase">
              {group.title}
            </h2>
            <div className="mt-3 grid gap-3 sm:grid-cols-2">
              {areas.map((area) => (
                <AreaTile key={area.id} area={area} />
              ))}
              {group.id === "run" ? (
                <a
                  href="https://contributors.home-assistant.io/community/reference/events/"
                  target="_blank"
                  rel="noreferrer"
                  className="flex flex-col rounded-lg border border-border bg-bg-elevated p-4 hover:border-border-strong"
                >
                  <div className="flex items-center gap-2">
                    <span className="flex size-8 items-center justify-center rounded-sm border border-border bg-bg-subtle text-accent">
                      <Calendar className="size-4" />
                    </span>
                    <div>
                      <div className="font-medium text-fg">活动与日历</div>
                      <div className="text-xs text-accent">参加活动（官网）</div>
                    </div>
                  </div>
                  <p className="mt-3 text-sm leading-6 text-fg-muted">
                    社区例会与发布日，以及如何加入你自己的日历。此快捷入口指向官网。
                  </p>
                </a>
              ) : null}
            </div>
          </section>
        );
      })}
    </div>
  );
}
