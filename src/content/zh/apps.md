---
title: 应用程序
description: 在Home Assistant旁运行的软件包，由Supervisor管理。构建一个应用程序，测试它，并与所有人分享。
---


# 应用程序 {#apps}
应用程序是运行在Home Assistant旁边的额外程序：一个MQTT代理、文件编辑器、数据库、媒体服务器。应用程序过去被称为插件，你仍然可以在代码、API以及较早的帖子中看到这个名称。它们运行在Home Assistant OS上，[Supervisor](/glossary/supervisor)在这里安装它们、启动它们、更新它们，并将它们包含在备份中。

在底层，应用程序是一个容器镜像加上一个小的配置文件。配置文件告诉Supervisor应用程序需要什么：哪些端口、哪些文件夹、哪些硬件，以及用户可以设置哪些选项。用户可以在**设置** > **应用程序**下的**应用商店**中安装应用程序，任何人都可以发布包含自己应用程序的仓库。

## 适用人群 {#who-this-is-for}
如果你想将软件打包成应用程序，无论是为自己还是为他人，这部分内容适合你。你需要熟悉终端、Docker 或其他容器工具，以及一些 shell 脚本。你不需要了解 Python 或 Home Assistant 代码库。

如果你想要在 Supervisor 本身工作，即运行应用程序的部分，请参见 [OS 与 Supervisor](/os)。

## 从这里开始 {#start-here}
按顺序执行以下步骤：

1. [为官方应用贡献](/apps/first-contribution)：你的第一次贡献，从你自己的应用到官方应用，基础镜像，以及构建工具。
2. [你的第一个应用](/apps/first-app)：构建一个“Hello world”应用，安装它，并将其发展成一个带有选项的小型网页服务器。大约半小时。
3. [构建一个真实的应用](/apps/build-a-real-app)：完整示例应用演练，包括服务、选项和使用 Bashio 的日志记录、翻译、文档、CI 和发布。
4. [应用是如何工作的](/apps/how-apps-work)：Supervisor、仓库、应用文件夹，以及应用启动时发生的事情。

## 指南- [构建容器镜像](/apps/guides/dockerfile)：基础镜像、构建参数和标签。 {#guides}
- [使用 S6 覆盖运行服务](/apps/guides/s6-overlay)：S6 覆盖是基础镜像中的进程管理器。它按顺序运行你的设置步骤和程序，重启它们，并在失败时停止容器。
- [添加选项](/apps/guides/options)：让用户配置你的应用，提供验证功能和翻译后的标签。
- [与 Home Assistant 和 Supervisor 交互](/apps/guides/communication)：内部网络、Core API 代理，以及 Supervisor API。
- [通过入口添加 Web 界面](/apps/guides/ingress)：在 Home Assistant UI 内显示你的应用。
- [共享服务并发现集成](/apps/guides/services-discovery)：向其他应用提供 MQTT 或 MySQL，并让 Home Assistant 为你的应用设置集成。
- [访问硬件和主机](/apps/guides/hardware)：串口、USB、GPIO、音频以及主机命名空间。

- [展示你的应用](/apps/guides/presentation)：README、文档、更新日志、图标和标志。
- [测试你的应用](/apps/guides/testing)：开发容器、真实设备以及普通 Docker。
- [保护你的应用](/apps/guides/security)：AppArmor、API 角色、保护模式和用户认证。
- [发布你的应用](/apps/guides/publishing)：为每个架构和版本的发布构建镜像。
- [创建并分享仓库](/apps/guides/repository)：将你的应用放在用户可以添加的地方。

## 参考文献 {#reference}
- [应用配置](/apps/reference/configuration)：`config.yaml` 的每个键。
- [Bashio](/apps/bashio)：基础镜像中 shell 库的每个函数，用于读取选项、写入日志以及调用 Supervisor API。
- [应用文件](/apps/reference/files)：应用文件夹和仓库中的文件。
- [运行环境](/apps/reference/environment)：应用容器内的环境变量、文件夹和网络地址。
- [安全评级](/apps/reference/security-rating)：Supervisor 对你的应用的评级。
- [Supervisor API](/apps/supervisor-api)：每个端点、其负载以及数据模型。

## 有用的仓库 {#useful-repositories}
- [hassio-addons/app-example](https://github.com/hassio-addons/app-example)：[Build a real app](/apps/build-a-real-app) 演示的示例应用程序，包含 S6 服务、Bashio、代码检查和发布。
- [home-assistant/apps-example](https://github.com/home-assistant/apps-example)：一个较小的示例仓库，带有 devcontainer 和构建其中每个应用的工作流。
- [hassio-addons/bashio](https://github.com/hassio-addons/bashio)：Bashio，应用程序的 Shell 函数库。
- [home-assistant/addons](https://github.com/home-assistant/addons)：官方应用程序。
- [hassio-addons](https://github.com/hassio-addons)：社区应用程序，以及许多优秀示例。
- [home-assistant/docker-base](https://github.com/home-assistant/docker-base)：基础镜像。
- [home-assistant/builder](https://github.com/home-assistant/builder)：构建和发布镜像的 GitHub Actions。
- [home-assistant/supervisor](https://github.com/home-assistant/supervisor)：Supervisor。有疑问时，以代码为准。

## 与谁交流 {#who-to-talk-to}
- 在 [Home Assistant Discord](https://www.home-assistant.io/join-chat/) 的 [**#developers**](https://discord.com/channels/330944238910963714/554842238073700352) 频道，应用开发者会互相帮助。有关 Supervisor 如何运行应用的问题，应发到 [**#operating-system**](https://discord.com/channels/330944238910963714/1475552965954900018) 频道，这是关于 Home Assistant OS 和 Supervisor 的频道。看不到这些频道？在 **Channels & Roles** 下，选择 **I want to contribute dev skills to Home Assistant**。
- 发现 Supervisor 处理应用时的 bug？在 [home-assistant/supervisor](https://github.com/home-assistant/supervisor/issues) 打开一个问题。
- 官方应用有问题？使用 [home-assistant/addons](https://github.com/home-assistant/addons/issues) 的问题追踪。
- 准备好向世界展示你的应用？在社区论坛的 [Share your Projects](https://community.home-assistant.io/c/projects/9) 分类中发布它。
