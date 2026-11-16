# Home Assistant 贡献者手册（中文）

[Home Assistant 贡献者文档](https://contributors.home-assistant.io/) 的**非官方**简体中文阅读站：如何以代码、设计、文档、翻译和社区工作的方式参与项目。

**在线阅读：** [https://gradient30.github.io/ha-contributors-handbook/](https://gradient30.github.io/ha-contributors-handbook/)

- 官方文档：[contributors.home-assistant.io](https://contributors.home-assistant.io/)
- 英文源：官网 Markdown（任意文档页加 `index.md`，例如 [start/index.md](https://contributors.home-assistant.io/start/index.md)）、[llms.txt](https://contributors.home-assistant.io/llms.txt)、[sitemap-0.xml](https://contributors.home-assistant.io/sitemap-0.xml) 与源仓库 [home-assistant/contributors.home-assistant.io](https://github.com/home-assistant/contributors.home-assistant.io)
- 本仓库：**非官方**译本与阅读器。产品名、命令、代码块、仓库路径与官网对齐；本站路径与官网分区一致（例如 `/start/github`）
- 发布：GitHub Pages（`main` 推送后自动构建；工作流 `.github/workflows/pages.yml`）
- 同步：每 6 小时对照官网 sitemap 与各页 `index.md` 指纹。哈希一变，就新增一条[同步日志](src/content/zh/updates.md)，写明改了什么、中文站在哪一页。**仅更新指纹时，不会把尚未重译的页面写成已经对齐。**
- 风格：明 / 暗 / 彩，切换结果保存在浏览器本地
- 官方博客本期未汉化，本站只提供[指向官网博客的入口](https://contributors.home-assistant.io/blog/)

## 发布方式

当前线上站点由 **`gh-pages` 分支**静态发布（已启用并可用）：

- 站点：https://gradient30.github.io/ha-contributors-handbook/
- 源码：`main` 分支
- 构建产物：推送到 `gh-pages`

仓库里保留了 Actions 工作流样例 `.github/workflows/pages.yml`（本地未推送）。若要改成 **GitHub Actions** 自动构建：

1. 用带 `workflow` 权限的 token / PAT 把 `.github/workflows/pages.yml` 推到 `main`
2. 打开 [Settings → Pages](https://github.com/gradient30/ha-contributors-handbook/settings/pages)
3. Build and deployment → Source 选择 **GitHub Actions**
4. 到 [Actions](https://github.com/gradient30/ha-contributors-handbook/actions) 运行 *Deploy GitHub Pages*

## 内容

| 部分 | 说明 |
| --- | --- |
| 从这里开始 | 第一次贡献、GitHub、讨论渠道、AI 政策、许可与 CLA |
| 构建软件 | 核心与集成、前端、应用、应用市场、伴侣应用、OS 与 Supervisor |
| 设计、撰写与翻译 | 设计系统、品牌、home-assistant.io 文档、翻译与语音 |
| 运转项目 | 社区、发布、路线图 |
| 理解它如何工作 | 架构、安全、数据、术语表 |
| [同步日志](src/content/zh/updates.md) | 每次官网变动单独一条：改了什么、本站哪个 URL |
| [对照表](src/content/zh/sitemap.md) | 官网页指纹与中文站位置 |
| [本站架构](src/content/zh/architecture-site.md) | 阅读器与指纹同步如何工作 |

常用入口：

- `/` — 分区总览
- `/start` — 开始贡献
- `/docs/updates` — 同步日志（顶栏「同步」进入）
- `/docs/sitemap` — 对照表
- `/docs/architecture-site` — 本站架构

## 本地运行

```bash
npm install
npm run dev
```

GitHub Pages 静态构建：

```bash
npm run build:pages
```

同步官方文档指纹（有变动会写入同步日志，不会自动重写译文）：

```bash
npm run sync:docs
```

某页补译完成后，把指纹标成已对齐：

```bash
npm run sync:docs -- --mark-translated start,start/github
```

产物在 `.output/public`。

## 技术栈

TanStack Start + Vite + Tailwind v4。正文是 `src/content/zh/**/*.md`，由 `src/lib/docs/catalog.ts` 建目录、`src/components/docs/Markdown.tsx` 渲染。

GitHub Pages 构建会设置 `VITE_AUTH_ENABLED=false`，不依赖登录或数据库。

## 许可与归属

Home Assistant 与 Open Home Foundation 是 [Open Home Foundation](https://www.openhomefoundation.org/) 的项目。本仓库仅提供中文阅读与对照，不替代官方文档。

译文按 [CC BY-NC-SA 4.0](LICENSE) 共享。详见官网 [许可与 CLA](https://contributors.home-assistant.io/start/licensing/)。
