---
title: 为官方应用贡献
description: 帮助改进官方应用、基础镜像以及每个应用都依赖的构建工具。先构建你的第一个应用，然后选择要帮助的领域。
sidebarLabel: 你的第一次贡献
order: 1
---


# 为官方应用贡献 {#contribute-to-the-official-apps}
本地区的大多数人都是为自己或为了分享而开发自己的应用程序。这本身就是一种贡献。一旦你了解了应用程序的构建方式，你也可以帮助共享整个生态系统的部分内容：官方应用、基础镜像以及构建它们的工具。

本页面将分步骤引导你到达目标。从步骤1开始，根据你的需要随时停止。

## 1. 构建你的第一个应用 {#1-build-your-first-app}
请完成本区域下一页的 [你的第一个应用](/apps/first-app) 教程。你将构建一个小型应用程序，将其安装到你自己的 Home Assistant 上，并将其扩展为具有选项的 web 服务器。整个过程大约需要半小时，完成此步骤后，后续内容假设你已了解应用程序文件夹中的内容。

## 2. 选择帮助的地方 {#2-pick-where-to-help}
三个仓库包含每个应用开发者使用的内容。每个都是普通的 GitHub 仓库：先分叉它，创建一个分支，然后对 `master` 提交 pull request。

### 官方应用 {#the-official-apps}
[home-assistant/addons](https://github.com/home-assistant/addons) 包含官方应用程序，如 Mosquitto 代理、MariaDB、Samba 共享和 Z-Wave JS。每个应用都是一个文件夹，里面有教程中使用的相同文件：`config.yaml`、一个 `Dockerfile`、一个 `build.yaml`、其文档在 `DOCS.md`、一个 `CHANGELOG.md` 以及其翻译文件。

- **错误** 可以通过其 [issues](https://github.com/home-assistant/addons/issues) 中的错误报告表格来报告。该表格仅适用于支持的设置。带有可复现错误及其日志的问题是一个良好的起点。
- **功能请求** 应提交到 [功能请求讨论](https://github.com/orgs/home-assistant/discussions)，而不是 issues。
- **任务** 是一种单独的问题类型，仅供 Open Home Foundation 员工和授权贡献者使用。由其他人打开的任务问题会自动关闭。30天没有活动的问题会被标记为陈旧，并在7天后关闭。标有`pinned`、`security`或`Help wanted`的议题不受影响。

### 基础镜像 {#the-base-images}
[home-assistant/docker-base](https://github.com/home-assistant/docker-base) 构建基础镜像，Home Assistant 和大多数应用都是从这些镜像开始的：Alpine、基于 Alpine 的 Python、Debian 和 Ubuntu，适用于 `amd64` 和 `arm64`。它们自带 S6 overlay、Bashio 和 TempIO。README 中解释了如何使用 `docker buildx` 本地构建每个镜像。

此仓库没有问题跟踪器。更改以 pull request 的形式提交。

### 构建工具 {#the-build-tooling}
[home-assistant/builder](https://github.com/home-assistant/builder) 保存 GitHub Actions，用于构建、使用 Cosign 签名并发布多架构容器镜像。[发布指南](/apps/guides/publishing) 使用它们。它的 [问题](https://github.com/home-assistant/builder/issues) 可用于报告错误。

旧的 `home-assistant/builder` 操作，作为单步使用，已被弃用且不再维护。工作现由 [`actions/`](https://github.com/home-assistant/builder/tree/master/actions) 文件夹中的新操作承担。

## 3. 打开一个 pull request {#3-open-a-pull-request}
这三个仓库都没有自己的 pull request 模板或贡献指南。home-assistant 组织的 [贡献指南](https://github.com/home-assistant/.github/blob/master/CONTRIBUTING.md) 适用：

- 尽量让你的更改保持专注。彼此不依赖的更改应分开提交到不同的 pull request。
- 遵循风格和代码质量标准，并确保检查仍然通过。
- 编写良好的提交信息。

你可以使用 AI 工具提供帮助，但你必须理解并能够解释你提交的每一个更改。[AI 政策](https://github.com/home-assistant/addons/blob/master/AI_POLICY.md) 有详细说明。

## 在你的 pull request 之后 {#after-your-pull-request}
当你打开 pull request 时，会立即运行检查。它们需要通过才能合并：

| 仓库 | 在 pull request 上运行的内容 |
| --- | --- |
| addons | 对每个 `Dockerfile` 运行 hadolint，运行 yamllint，对脚本运行 ShellCheck。每个 `config.yaml`、`build.yaml`、`Dockerfile`、`apparmor.txt`、`data` 或 `rootfs` 有所更改的应用都会进行 `amd64` 和 `aarch64` 的测试构建。 |
| docker-base | 每个镜像都会被构建。不会发布任何内容：只有在发布版本时镜像才会被推送。 |
| builder | 当操作发生更改时，会使用它们构建一个测试应用。 |

然后，仓库的维护者会审查你的更改。预计会有问题，这是审查的工作方式。在 docker-base 和 builder 中，发布说明是从已合并的 pull request 起草的。

## 接下来做什么 {#what-is-next}
- 还没有开发应用程序？先从 [你的第一个应用](/apps/first-app) 开始，然后 [开发一个真实的应用](/apps/build-a-real-app)，并阅读 [应用程序如何工作](/apps/how-apps-work) 以了解 Supervisor 如何处理应用程序。
- 查看你面前任务的 [指南](/apps/guides)。
- 想要直接处理 Supervisor 本身？前往 [OS 与 Supervisor](/os/first-contribution) 。
