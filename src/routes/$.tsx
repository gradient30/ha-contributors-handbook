import { createFileRoute } from "@tanstack/react-router";
import { DocsShell } from "@/components/docs/DocsShell";

export const Route = createFileRoute("/$")({ component: AreaPage });

function AreaPage() {
  const { _splat } = Route.useParams();
  const slug = (_splat ?? "").replace(/\/$/, "");
  return <DocsShell slug={slug || "home"} />;
}
