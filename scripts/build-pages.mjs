#!/usr/bin/env node
/**
 * GitHub Pages static build. Does not change the live-preview `npm run dev` path.
 *
 * TanStack Start SPA emits a client shell. This script then writes an index.html
 * for every handbook slug so deep links work on GitHub Pages without relying
 * solely on 404.html fallback.
 */
import { spawn } from "node:child_process";
import {
  copyFileSync,
  cpSync,
  existsSync,
  mkdirSync,
  readFileSync,
  rmSync,
  writeFileSync,
} from "node:fs";
import { dirname, join } from "node:path";

process.env.GITHUB_PAGES = "1";
process.env.VITE_AUTH_ENABLED = "false";

const child = spawn(process.execPath, ["scripts/with-app-env.mjs", "vite", "build"], {
  stdio: "inherit",
  env: process.env,
});

child.on("exit", (code) => {
  if (code !== 0) process.exit(code ?? 1);

  const root = process.cwd();
  const publicDir = join(root, ".output", "public");
  const clientDir = join(publicDir, "client");
  const staging = join(root, ".output", "pages-staging");

  if (existsSync(clientDir)) {
    rmSync(staging, { recursive: true, force: true });
    cpSync(clientDir, staging, { recursive: true });
    rmSync(publicDir, { recursive: true, force: true });
    mkdirSync(publicDir, { recursive: true });
    cpSync(staging, publicDir, { recursive: true });
    rmSync(staging, { recursive: true, force: true });
  }

  const shell = join(publicDir, "_shell.html");
  const index = join(publicDir, "index.html");
  const notFound = join(publicDir, "404.html");
  if (existsSync(shell) && !existsSync(index)) {
    copyFileSync(shell, index);
  }
  if (existsSync(index) && !existsSync(notFound)) {
    copyFileSync(index, notFound);
  }
  writeFileSync(join(publicDir, ".nojekyll"), "");

  if (!existsSync(index)) {
    console.error("[build-pages] missing index.html in .output/public");
    process.exit(1);
  }

  const html = readFileSync(index, "utf8");
  const catalogPath = join(root, "src/lib/docs/catalog-data.json");
  const slugs = new Set();
  if (existsSync(catalogPath)) {
    const catalog = JSON.parse(readFileSync(catalogPath, "utf8"));
    for (const page of catalog.pages ?? []) {
      if (page?.slug) slugs.add(page.slug);
    }
    for (const area of catalog.areas ?? []) {
      if (area?.id) slugs.add(area.id);
    }
  }
  for (const slug of ["docs/updates", "docs/sitemap", "docs/architecture-site", "docs/blog"]) {
    slugs.add(slug);
  }

  let written = 0;
  for (const slug of slugs) {
    const dest = join(publicDir, slug, "index.html");
    mkdirSync(dirname(dest), { recursive: true });
    writeFileSync(dest, html);
    written += 1;
  }

  writeFileSync(join(publicDir, "404.html"), html);

  console.log(`[build-pages] wrote ${written} doc paths plus index.html and 404.html`);
  process.exit(0);
});
