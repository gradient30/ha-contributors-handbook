import { Link } from "@tanstack/react-router";
import { cn } from "@/lib/cn";
import { MermaidBlock } from "./MermaidBlock";

type ListItem = { text: string; children?: Extract<Block, { t: "ul" | "ol" }> };
type Block =
  | { t: "h"; level: number; text: string; id: string }
  | { t: "p"; text: string }
  | { t: "ul"; items: ListItem[] }
  | { t: "ol"; items: ListItem[] }
  | { t: "quote"; text: string; kind?: string }
  | { t: "code"; lang: string; code: string }
  | { t: "table"; headers: string[]; rows: string[][] }
  | { t: "img"; src: string; alt: string }
  | { t: "hr" };

function slugify(s: string): string {
  return s
    .toLowerCase()
    .replace(/<[^>]+>/g, "")
    .replace(/[`*_]/g, "")
    .replace(/['’]/g, "")
    .replace(/[^a-z0-9\u4e00-\u9fff]+/g, "-")
    .replace(/-{2,}/g, "-")
    .replace(/^-|-$/g, "")
    .slice(0, 80);
}

export function extractToc(source: string): { id: string; text: string; level: number }[] {
  return parse(source)
    .filter((b): b is Extract<Block, { t: "h" }> => b.t === "h" && b.level >= 2 && b.level <= 3)
    .map((b) => ({ id: b.id, text: b.text.replace(/[*`]/g, ""), level: b.level }));
}

function parseHeading(line: string): Extract<Block, { t: "h" }> | null {
  const m = line.match(/^(#{1,4})\s+(.+)$/);
  if (!m) return null;
  const level = m[1]?.length ?? 1;
  let text = (m[2] ?? "").trim();
  let id = "";
  const idm = text.match(/^(.*?)\s*\{#([A-Za-z0-9_-]+)\}\s*$/);
  if (idm) {
    text = (idm[1] ?? "").trim();
    id = idm[2] ?? "";
  } else {
    id = slugify(text);
  }
  return { t: "h", level, text, id };
}

function parse(src: string): Block[] {
  const lines = src.replace(/\r\n/g, "\n").split("\n");
  const blocks: Block[] = [];
  let i = 0;
  while (i < lines.length) {
    const line = lines[i] ?? "";
    if (!line.trim()) {
      i += 1;
      continue;
    }
    const img = line.match(/^!\[([^\]]*)\]\(([^)]+)\)\s*$/);
    if (img) {
      blocks.push({ t: "img", src: img[2] ?? "", alt: img[1] ?? "" });
      i += 1;
      continue;
    }
    if (line.startsWith("```")) {
      const lang = line.slice(3).trim().split(/\s+/)[0] ?? "";
      const buf: string[] = [];
      i += 1;
      while (i < lines.length && !lines[i]?.startsWith("```")) {
        buf.push(lines[i] ?? "");
        i += 1;
      }
      i += 1;
      blocks.push({ t: "code", lang, code: buf.join("\n") });
      continue;
    }
    const heading = parseHeading(line);
    if (heading) {
      blocks.push(heading);
      i += 1;
      continue;
    }
    if (line.startsWith("> ") || line === ">") {
      const buf: string[] = [];
      while (i < lines.length && (lines[i]?.startsWith(">") ?? false)) {
        buf.push((lines[i] ?? "").replace(/^>\s?/, ""));
        i += 1;
      }
      let kind = "";
      if (/^\[!(NOTE|TIP|WARNING|IMPORTANT|CAUTION|NOTE|TIP)\]/i.test(buf[0] ?? "")) {
        kind = (buf.shift() ?? "").replace(/[\[\]!]/g, "").trim().toUpperCase();
      }
      blocks.push({ t: "quote", text: buf.join("\n"), kind });
      continue;
    }
    if (/^\|/.test(line) && lines[i + 1]?.includes("---")) {
      const headers = splitRow(line);
      i += 2;
      const rows: string[][] = [];
      while (i < lines.length && /^\|/.test(lines[i] ?? "")) {
        rows.push(splitRow(lines[i] ?? ""));
        i += 1;
      }
      blocks.push({ t: "table", headers, rows });
      continue;
    }
    if (/^(\s*)([-*] |\d+\. )/.test(line)) {
      const collected: string[] = [];
      while (i < lines.length) {
        const ln = lines[i] ?? "";
        if (/^(\s*)([-*] |\d+\. )/.test(ln)) {
          collected.push(ln);
          i += 1;
          continue;
        }
        if (!ln.trim() && i + 1 < lines.length && /^(\s+)([-*] |\d+\. )/.test(lines[i + 1] ?? "")) {
          i += 1;
          continue;
        }
        break;
      }
      blocks.push(parseList(collected));
      continue;
    }
    if (/^---+$/.test(line.trim())) {
      blocks.push({ t: "hr" });
      i += 1;
      continue;
    }
    const buf: string[] = [line];
    i += 1;
    while (
      i < lines.length &&
      (lines[i] ?? "").trim() &&
      !/^(#{1,4} |```|> |\| |[-*] |\d+\. |---)/.test(lines[i] ?? "")
    ) {
      buf.push(lines[i] ?? "");
      i += 1;
    }
    blocks.push({ t: "p", text: buf.join("\n") });
  }
  return blocks;
}

function listMarker(line: string): { indent: number; ordered: boolean; text: string } | null {
  const m = line.match(/^(\s*)([-*] |\d+\. )(.*)$/);
  if (!m) return null;
  return { indent: (m[1] ?? "").length, ordered: /^\d+\. $/.test(m[2] ?? ""), text: m[3] ?? "" };
}

function parseList(lines: string[]): Extract<Block, { t: "ul" | "ol" }> {
  const rootItems: ListItem[] = [];
  const stack: { indent: number; ordered: boolean; items: ListItem[] }[] = [];
  let rootOrdered = false;
  for (const line of lines) {
    const mark = listMarker(line);
    if (!mark) continue;
    if (stack.length === 0) {
      rootOrdered = mark.ordered;
      stack.push({ indent: mark.indent, ordered: mark.ordered, items: rootItems });
    }
    while (stack.length > 1 && mark.indent < stack[stack.length - 1]!.indent) {
      stack.pop();
    }
    const top = stack[stack.length - 1]!;
    if (mark.indent > top.indent) {
      const parent = top.items[top.items.length - 1];
      if (parent) {
        const childItems: ListItem[] = [];
        parent.children = { t: mark.ordered ? "ol" : "ul", items: childItems };
        stack.push({ indent: mark.indent, ordered: mark.ordered, items: childItems });
      }
    }
    stack[stack.length - 1]!.items.push({ text: mark.text });
  }
  return { t: rootOrdered ? "ol" : "ul", items: rootItems };
}

function splitRow(line: string): string[] {
  return line
    .replace(/^\||\|$/g, "")
    .split("|")
    .map((c) => c.trim());
}

function isInternalPath(path: string): boolean {
  if (!path.startsWith("/") || path.startsWith("//")) return false;
  const clean = path.split("?")[0] ?? path;
  if (/\.(png|jpe?g|gif|svg|webp|ico|pdf)$/i.test(clean)) return false;
  if (clean.startsWith("/images/") || clean.startsWith("/img/") || clean.startsWith("/static/")) return false;
  return true;
}

function DocLink({ href, label }: { href: string; label: string }) {
  const [path, hash] = href.split("#");
  const external = href.startsWith("http") || href.startsWith("mailto:") || href.startsWith("discord:");
  if (!path && hash) {
    return (
      <a href={`#${hash}`} className="text-accent underline-offset-2 hover:underline">
        {label}
      </a>
    );
  }
  if (!external && path && isInternalPath(path)) {
    return (
      <Link to={path} hash={hash} className="text-accent underline-offset-2 hover:underline">
        {label}
      </Link>
    );
  }
  return (
    <a
      href={href}
      target={external && href.startsWith("http") ? "_blank" : undefined}
      rel={external && href.startsWith("http") ? "noreferrer" : undefined}
      className="text-accent underline-offset-2 hover:underline"
    >
      {label}
    </a>
  );
}

function Inline({ text }: { text: string }) {
  const parts: Array<string | { href: string; label: string } | { code: string } | { strong: string }> = [];
  const re = /(\[([^\]]+)\]\(([^)]+)\))|(`([^`]+)`)|(\*\*([^*]+)\*\*)/g;
  let last = 0;
  let m: RegExpExecArray | null;
  while ((m = re.exec(text))) {
    if (m.index > last) parts.push(text.slice(last, m.index));
    if (m[1]) parts.push({ href: m[3] ?? "", label: m[2] ?? "" });
    else if (m[4]) parts.push({ code: m[5] ?? "" });
    else if (m[6]) parts.push({ strong: m[7] ?? "" });
    last = m.index + m[0].length;
  }
  if (last < text.length) parts.push(text.slice(last));
  return (
    <>
      {parts.map((p, i) => {
        if (typeof p === "string") return <span key={i}>{p}</span>;
        if ("code" in p)
          return (
            <code key={i} className="rounded-xs bg-bg-subtle px-1 py-0.5 font-mono text-sm text-accent">
              {p.code}
            </code>
          );
        if ("strong" in p)
          return (
            <strong key={i} className="font-medium text-fg">
              {p.strong}
            </strong>
          );
        return <DocLink key={i} href={p.href} label={p.label} />;
      })}
    </>
  );
}

const hClass: Record<number, string> = {
  1: "font-display text-3xl font-semibold tracking-tight text-fg",
  2: "mt-10 border-b border-border pb-2 font-display text-xl font-semibold tracking-tight text-fg",
  3: "mt-8 font-display text-lg font-medium text-fg",
  4: "mt-6 text-base font-medium text-fg",
};

function ListView({ block }: { block: Extract<Block, { t: "ul" | "ol" }> }) {
  const Tag = block.t === "ol" ? "ol" : "ul";
  return (
    <Tag
      className={
        block.t === "ol"
          ? "mt-3 list-decimal space-y-1.5 pl-5 text-base leading-7 text-fg-muted"
          : "mt-3 list-disc space-y-1.5 pl-5 text-base leading-7 text-fg-muted"
      }
    >
      {block.items.map((it, j) => (
        <li key={j}>
          <Inline text={it.text} />
          {it.children ? <ListView block={it.children} /> : null}
        </li>
      ))}
    </Tag>
  );
}

export function Markdown({ source }: { source: string }) {
  const blocks = parse(source);
  return (
    <div className="docs-prose max-w-3xl">
      {blocks.map((b, i) => {
        if (b.t === "h") {
          const Tag = `h${b.level}` as unknown as "h1";
          return (
            <Tag key={i} id={b.id} className={cn("scroll-mt-24", hClass[b.level])}>
              <Inline text={b.text} />
            </Tag>
          );
        }
        if (b.t === "p")
          return (
            <p key={i} className="mt-4 text-base leading-7 text-fg-muted">
              <Inline text={b.text} />
            </p>
          );
        if (b.t === "ul" || b.t === "ol")
          return <ListView key={i} block={b} />;
        if (b.t === "quote") {
          const kindLabel: Record<string, string> = {
            NOTE: "注意",
            TIP: "提示",
            WARNING: "警告",
            IMPORTANT: "重要",
            CAUTION: "小心",
          };
          return (
            <blockquote
              key={i}
              className="mt-5 rounded-md border border-border border-l-[3px] border-l-accent bg-bg-elevated px-4 py-3 text-sm leading-6 text-fg-muted"
            >
              {b.kind ? (
                <div className="mb-1 text-xs font-medium tracking-wide text-accent">
                  {kindLabel[b.kind] ?? b.kind}
                </div>
              ) : null}
              {b.text.split("\n").map((ln, j) => (
                <p key={j} className={j ? "mt-1" : ""}>
                  <Inline text={ln} />
                </p>
              ))}
            </blockquote>
          );
        }
        if (b.t === "code") {
          if (b.lang.trim().toLowerCase() === "mermaid") {
            return <MermaidBlock key={i} code={b.code} />;
          }
          return (
            <pre
              key={i}
              className="mt-4 overflow-x-auto rounded-md border border-border bg-bg-elevated p-4 font-mono text-sm leading-6 text-fg"
            >
              <code>{b.code}</code>
            </pre>
          );
        }
        if (b.t === "img") {
          const base = import.meta.env.BASE_URL || "/";
          const src =
            b.src.startsWith("/") && !b.src.startsWith("//")
              ? `${base}${b.src.replace(/^\//, "")}`
              : b.src;
          return (
            <figure key={i} className="mt-6 overflow-hidden rounded-md border border-border bg-bg-elevated">
              <img src={src} alt={b.alt} className="w-full" />
              {b.alt ? <figcaption className="px-3 py-2 text-sm text-fg-subtle">{b.alt}</figcaption> : null}
            </figure>
          );
        }
        if (b.t === "table")
          return (
            <div key={i} className="mt-4 overflow-x-auto rounded-md border border-border">
              <table className="w-full min-w-lg text-left text-sm">
                <thead className="bg-bg-subtle text-fg-muted">
                  <tr>
                    {b.headers.map((h, j) => (
                      <th key={j} className="px-3 py-2 font-medium">
                        <Inline text={h} />
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {b.rows.map((row, r) => (
                    <tr key={r} className="border-t border-border">
                      {row.map((c, j) => (
                        <td key={j} className="px-3 py-2 align-top text-fg-muted">
                          <Inline text={c} />
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          );
        return <hr key={i} className="my-8 border-border" />;
      })}
    </div>
  );
}
