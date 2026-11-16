---
title: 图标
description: 前端寄存器的每一个命令,它做什么,以及它使用的端口.
order: 1
---

# 图标 {#commands}

从 [前端仓库](https://github.com/home-assistant/frontend) 的根运行这些 。

## 设置 {#setup}

| 命令 | 它会做什么 |
| --- | --- |
| `script/setup` | 安装依赖关系。 在代管器中,也是右节点.js. |
| `script/core` | 仅在解析器中:从它的 `dev` 分支安装并启动 Home Assistant Core, 配置使用您的前端 。 `-r <ref>` 选择另一个分支或标记, `-s` 跳过安装 。 |
| `script/setup_translations` | 获取最新译名, 并第一次请求 GitHub 授权 。 |

## 开发服务器 {#development-servers}

| 命令 | 端口 | 它所服务 |
| --- | --- | --- |
| `pnpm dev` | | 将眷顾的应用程序构建为 `hass_frontend/`, 用于设定 `development_repo` 的核心 。 在核心港打开 |
| `pnpm dev:serve` | 8124 | 构建并服务应用程序,连接到一个核心. `-c <url>` 设置核心( 默认 `http://localhost:8123`) , `-p <port>` 端口 。 在Devcontainer中,默认端口为8123,即您的计算机上的8124. |
| `pnpm dev:demo` | 8090 | 那个[演示](/frontend/development/gallery-and-demo#the-demo)。 |
| `pnpm dev:gallery` | 8100 | 那个[画廊](/frontend/development/gallery-and-demo#the-gallery)。 |
| `pnpm test:e2e:app:dev` | 8095 | 用于端到端测试的应用套装. |

所有开发服务器接受`--background`,`--status`,`--logs [--follow]`和`--stop`. 除了端到端的牵引装置都接受`--fetch-translations`. 见[运行前端](/frontend/development/run#keep-a-server-running-in-the-background).

## 检查和测试 {#checks-and-tests}

| 命令 | 它会做什么 |
| --- | --- |
| `pnpm lint` | ES所拥有的 ESLint, Pretier, TypeScript 编译器,以及 Lit 分析器. |
| `pnpm format` | 修复ESLint和Pretier可以修复的东西. |
| `pnpm lint:types` | 只有TypeScript编译器。 从不通过文件。 |
| `pnpm lint:lit` | 只有液态分析器 |
| `pnpm test` | 单位测试,与Vitest。 |
| `pnpm test:coverage` | 单位检验,附覆盖报告. |
| `pnpm test:e2e:app` | 应用软件的制度端对端测试. |
| `pnpm test:e2e:demo` | 演示的端对端测试. |
| `pnpm test:e2e:gallery` | 展馆的端对端测试. |
| `pnpm test:e2e` | 所有三个端对端套房. |
| `pnpm test:e2e:show-report` | 打开合并的端对端报告。 |

## 构建 {#builds}

| 命令 | 它会做什么 |
| --- | --- |
| `pnpm build` | 一个完整的生产构建到`hass_frontend/`。 接受背景旗帜。 |
| `pnpm build --modern` | 只有现代建筑,用于大小和性能比较. |
| `script/gen_demo_core_data` | 重新生成来自Core的演示数据. |
