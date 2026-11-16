import { Link } from "@tanstack/react-router";
import {
  BatteryCharging,
  BookOpen,
  Calendar,
  Code2,
  Cpu,
  FileText,
  Flag,
  Globe,
  Layers,
  Layout,
  Lightbulb,
  Lock,
  Map,
  MessageSquare,
  Mic,
  Package,
  PenTool,
  Shield,
  ShoppingBag,
  Smartphone,
  Sun,
  Tag,
  Thermometer,
  Users,
  Wrench,
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

const SCENARIOS: { icon: LucideIcon; title: string; body: string }[] = [
  {
    icon: Sun,
    title: "照明与氛围",
    body: "按日出日落、有人到家或睡眠模式，自动开关灯和调节亮度。",
  },
  {
    icon: Thermometer,
    title: "气候与环境",
    body: "按房间和时段调节空调、地暖与新风，减少空转，也让湿度更稳。",
  },
  {
    icon: Lock,
    title: "安防与提醒",
    body: "门窗、漏水、烟雾或异常活动触发时，把通知推到手机或扬声器。",
  },
  {
    icon: BatteryCharging,
    title: "能源与用电",
    body: "看清家里用了多少电，配合电价、太阳能或充电桩做更细的调度。",
  },
  {
    icon: Mic,
    title: "影音与语音",
    body: "把播放器和语音助手放进同一套界面，用 Assist 在本地下指令。",
  },
  {
    icon: Lightbulb,
    title: "日常场景",
    body: "离家、入睡、观影、访客等场景一键切换，把多台设备编成一套动作。",
  },
];

const LEVELS: {
  id: string;
  label: string;
  title: string;
  body: string;
  icon: LucideIcon;
  links: { href: string; label: string }[];
}[] = [
  {
    id: "beginner",
    label: "入门",
    title: "先让家里跑起来",
    body: "适合刚装上 Home Assistant Green、Yellow，或第一次使用 Home Assistant OS 的人。用官方集成接入灯、传感器和开关，在界面里搭仪表盘、写简单自动化，不必先写代码。想参与项目，也可以从改正文案、翻译界面或帮忙回答问题开始。",
    icon: Flag,
    links: [
      { href: "/start", label: "开始贡献" },
      { href: "/start/first-contribution", label: "第一次贡献" },
      { href: "/translate", label: "翻译" },
      { href: "/writing", label: "写文档" },
    ],
  },
  {
    id: "advanced",
    label: "进阶",
    title: "把自动化写细，扩展系统",
    body: "适合已经能稳定运行，并想把规则做得更精确的人。可以用模板、脚本和自定义仪表盘，接入 MQTT 或附加组件，用 HACS 安装社区卡片与集成，同时把备份、更新和更复杂的设备组合管起来。",
    icon: Wrench,
    links: [
      { href: "/frontend", label: "前端" },
      { href: "/marketplace", label: "市场" },
      { href: "/apps", label: "应用" },
      { href: "/core", label: "核心与集成" },
    ],
  },
  {
    id: "geek",
    label: "极客",
    title: "改系统本身，参与上游",
    body: "适合要写集成、改前端、做附加组件，或参与 OS、Supervisor 和 Companion 应用的人。可以从架构和安全分区理解整体，再向 Home Assistant Core、前端或其他仓库提交改动。本手册的构建与理解类文档就是为此准备的。",
    icon: Code2,
    links: [
      { href: "/architecture", label: "架构" },
      { href: "/core", label: "核心" },
      { href: "/frontend", label: "前端" },
      { href: "/os", label: "OS 与 Supervisor" },
    ],
  },
];

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
    <div className="mt-8 max-w-3xl space-y-12">
      <section id="intro" className="scroll-mt-4">
        <h2 className="font-display text-lg font-medium text-fg">这是什么系统</h2>
        <div className="mt-3 space-y-4 text-sm leading-7 text-fg-muted">
          <p>
            Home Assistant 是一个开源的智能家居系统，由 Open Home Foundation 支持。它把灯、门锁、空调、传感器、媒体和能源等设备放进同一个本地控制的平台里，数据默认留在家里，不必绑定单一厂商云。你可以只用界面完成日常自动化，也可以深入到仪表盘定制、集成开发和操作系统层面。它已经用在全球数百万家庭中。
          </p>
          <p>
            本站是{" "}
            <a
              href="https://contributors.home-assistant.io/"
              target="_blank"
              rel="noreferrer"
              className="text-accent underline-offset-2 hover:underline"
            >
              贡献者官方手册
            </a>
            的<strong className="font-medium text-fg">非官方</strong>
            简体中文译本，说明如何以代码、设计、文档、翻译和社区工作参与项目。路径与官网一致，产品名、命令、代码和仓库名保留英文。
          </p>
        </div>
      </section>

      <section id="scenarios" className="scroll-mt-4">
        <h2 className="font-display text-lg font-medium text-fg">应用场景</h2>
        <p className="mt-3 text-sm leading-7 text-fg-muted">
          最常见的用法是把家里已经有的设备连在一起，按生活节奏自动工作。下面这些场景，从入门到极客都可以做，只是实现方式会越来越深。
        </p>
        <div className="mt-4 grid gap-3 sm:grid-cols-2">
          {SCENARIOS.map((item) => {
            const Icon = item.icon;
            return (
              <div key={item.title} className="rounded-lg border border-border bg-bg-elevated p-4">
                <div className="flex items-center gap-2 text-fg">
                  <span className="flex size-8 items-center justify-center rounded-sm border border-border bg-bg-subtle text-accent">
                    <Icon className="size-4" />
                  </span>
                  <div className="font-medium">{item.title}</div>
                </div>
                <p className="mt-3 text-sm leading-6 text-fg-muted">{item.body}</p>
              </div>
            );
          })}
        </div>
      </section>

      <section id="levels" className="scroll-mt-4">
        <h2 className="font-display text-lg font-medium text-fg">按程度开始</h2>
        <p className="mt-3 text-sm leading-7 text-fg-muted">
          不必一次读完整本手册。可以按自己现在的程度选一条路：先把家用起来，再把自动化写细，或直接参与上游开发。
        </p>
        <div className="mt-4 space-y-3">
          {LEVELS.map((level) => {
            const Icon = level.icon;
            return (
              <article
                key={level.id}
                id={level.id}
                className="scroll-mt-4 rounded-lg border border-border bg-bg-elevated p-5"
              >
                <div className="flex items-start gap-3">
                  <span className="flex size-9 shrink-0 items-center justify-center rounded-sm border border-border bg-bg-subtle text-accent">
                    <Icon className="size-4" />
                  </span>
                  <div className="min-w-0 flex-1">
                    <div className="text-xs tracking-[0.14em] text-accent uppercase">{level.label}</div>
                    <h3 className="mt-1 font-medium text-fg">{level.title}</h3>
                    <p className="mt-2 text-sm leading-7 text-fg-muted">{level.body}</p>
                    <div className="mt-3 flex flex-wrap gap-2">
                      {level.links.map((link) => (
                        <Link
                          key={link.href + link.label}
                          to={link.href}
                          className="rounded-md border border-border bg-bg px-2.5 py-1 text-xs text-fg hover:border-border-strong hover:text-accent"
                        >
                          {link.label}
                        </Link>
                      ))}
                    </div>
                  </div>
                </div>
              </article>
            );
          })}
        </div>
      </section>

      <div className="rounded-md border border-border bg-bg-elevated px-4 py-3 text-sm leading-6 text-fg-muted">
        本站便于阅读，不替代官方文档。原文由 Home Assistant 与 Open Home Foundation 维护。官方博客本期未汉化，见
        <Link to="/docs/blog" className="text-accent underline-offset-2 hover:underline">
          博客入口
        </Link>
        。
      </div>

      <div id="areas" className="scroll-mt-4 space-y-10">
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
    </div>
  );
}
