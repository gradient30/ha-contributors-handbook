---
title: 应用程序如何工作
description: 你的应用程序会Supervisor做什么，从存储库到运行中的容器，以及你在此过程中遇到的名称和文件夹。
order: 4
---


# 应用程序如何工作 {#how-apps-work}
应用程序是一个容器，由Supervisor为用户管理。了解Supervisor在每个步骤中做的事情会使大多数配置选项显而易见。本页面从存储库到运行的应用程序进行了详细说明。

## 组件 {#the-pieces}
- **Home Assistant OS** 在一个最小化操作系统上以容器形式运行所有内容。
- **Supervisor** 是管理所有其他容器的容器：Home Assistant Core、一些系统容器（称为插件）以及每个应用。它有一个 REST API，Core、UI 和应用都与之通信。[Supervisor 运行的内容](/os/supervisor#what-the-supervisor-runs) 列出了每个容器及其地址。
- **应用** 是一个包含 `config.yaml` 的文件夹，并且包含 `Dockerfile` 或指向已发布镜像的引用。
- **仓库** 是一个 Git 仓库，包含一个或多个应用文件夹和一个 `repository.yaml`。
- **应用商店** 显示用户在 **设置** > **应用** > **安装应用** 中添加的每个仓库的应用。

## 从仓库到应用商店 {#from-repository-to-app-store}
Supervisor 保留它知道的每个仓库的本地副本：

- **本地应用**：设备上的 `local_apps` 文件夹。不涉及 Git，这使其成为开发的场所。
- **官方应用**：[home-assistant/addons](https://github.com/home-assistant/addons)。
- 一些内置的社区仓库，例如 [community apps](https://github.com/hassio-addons/repository)、ESPHome 和 Music Assistant。
- 用户通过 URL 添加的每个仓库。

当商店重新加载时，Supervisor 会在每个仓库中搜索名为 `config.yaml`、`config.yml` 或 `config.json` 的文件，搜索深度不限，跳过隐藏文件夹和名为 `rootfs` 的文件夹。它找到的每个文件都是一个应用。它根据配置模式验证文件；配置无效的应用会被跳过，并在 Supervisor 日志中发出警告。

## 名称和 ID {#names-and-ids}
Supervisor 通过其仓库和 slug 识别已安装的应用，两者用下划线连接: `{repository}_{slug}`。

- **slug** 来自 `config.yaml`。它可能包含字母、数字、`-`、`_` 和 `.`，并且在其仓库中必须唯一。
- **仓库 ID** 对于本地应用是 `local`，对于官方应用是 `core`。对于通过 URL 添加的仓库，它是小写 URL（包括分支）的 SHA-1 哈希的前 8 个字符，例如社区应用的 `a0d7b954`。

因此你本地文件夹中的 `hello_world` 会变成 `local_hello_world`。你可以在 API、CLI (`ha apps info local_hello_world`) 和 [我的链接](/glossary/my-link) 中看到这个完整 ID。它也是内部网络主机名的基础：将 `_` 替换为 `-`，`local_hello_world` 可通过 `local-hello-world` 访问。

## 安装和构建 {#installing-and-building}
当用户安装应用时，Supervisor 会以两种方式之一获取其镜像：

- **拉取**：如果 `config.yaml` 有 `image` 密钥，Supervisor 会以 `version` 作为标签拉取该镜像。这就是已发布应用的工作方式：快速且可靠。请参阅 [发布你的应用](/apps/guides/publishing)。
- **构建**：如果没有 `image`，Supervisor 会在设备上从你的 `Dockerfile` 构建镜像，使用 Docker BuildKit。这是在开发期间本地应用发生的情况。

在安装任何内容之前，Supervisor 会检查应用是否适合系统：CPU 架构必须在 `arch` 中，如果你设置了机器类型，则必须与 `machine` 匹配，并且 Home Assistant 必须至少是 `homeassistant` 中的版本。

## 启动 {#starting}
当应用程序启动时，Supervisor：

1. 根据你的 `schema` 验证用户的选项，并将其写入 `/data/options.json`。
2. 创建容器，并包含 `config.yaml` 要求的所有内容：端口、映射的文件夹、设备、能力、AppArmor 配置文件，以及环境变量，包括对该应用程序唯一的 `SUPERVISOR_TOKEN`。
3. 将容器添加到内部网络，并在内部 DNS 中注册其主机名。
4. 启动容器并等待其运行。

在开机时，应用程序按其 `startup` 值分阶段启动：

| `startup` | 启动 |
| --- | --- |
| `initialize` | 首先，当 Supervisor 启动时 |
| `system` | 在服务之前，用于数据库等事物 |
| `services` | 在 Home Assistant Core 之前 |
| `application` | 在 Home Assistant Core 之后。这是默认设置 |
| `once` | 开机时从不启动。用于执行任务后退出的应用程序 |应用程序只有在用户保持 **开机启动** 打开的情况下才会在启动时启动。在 `boot: manual` 中，默认是关闭的；在 `boot: manual_only` 中，用户根本无法开启它。

## 运行时 {#while-running}
- 你的应用写入 `stdout` 和 `stderr` 的所有内容最终都会出现在 **日志** 标签中。
- 如果用户打开 **看门狗**，当容器失败时 Supervisor 会重启你的应用。如果你设置了 `watchdog` URL，它还会检查该 URL，并在停止响应时重启应用。
- `/data` 是你应用的私有持久存储。它在重启和更新后仍然存在，并且是你应用每次备份的一部分。容器重新创建时，`/data` 和映射文件夹之外的所有内容都会丢失。

## 备份 {#backups}
应用程序的备份包含其配置、`/data` 文件夹，如果你映射了 `app_config`，还包含其公共配置文件夹。默认情况下，备份是热备份：你的应用程序保持运行。如果你的应用程序需要磁盘上的一致状态，你有两个选项：

- 将 `backup_pre` 和 `backup_post` 设置为在备份前后在容器内运行的命令，例如将数据库刷新到磁盘。
- 设置 `backup: cold`，Supervisor 会在备份期间停止你的应用程序。

使用 `backup_exclude` 来排除不需要恢复的文件，例如缓存。有关详细信息，请参见 [应用程序配置](/apps/reference/configuration#backups)。

## 更新 {#updating}
当你在 `config.yaml` 中提升 `version` 时，用户会看到更新。更新会拉取（或构建）新的镜像并重新创建容器；`/data` 会保持不变。用户可以为每个应用开启自动更新。如果某个版本需要他们关注，请在 `breaking_versions` 中列出，而 Supervisor 不会自动更新。

## 下一步去向 {#where-to-go-from-here}
- [指南](/apps/guides) 每个覆盖一个任务，从容器镜像到发布你的应用。
- [与 Home Assistant 和 Supervisor 交流](/apps/guides/communication) 解释了内部网络和 API。
- [运行时环境](/apps/reference/environment) 列出了容器从 Supervisor 获取的所有内容。
- [应用配置](/apps/reference/configuration) 包含 `config.yaml` 的所有键。
