import { createFileRoute } from "@tanstack/react-router";
import { DocsShell } from "@/components/docs/DocsShell";

export const Route = createFileRoute("/")({ component: HomePage });

function HomePage() {
  return <DocsShell slug="home" />;
}
