---
title: 测试你的应用
description: 在你自己的电脑、真实设备或使用普通 Docker 上，运行你的应用程序，并拥有完整的 Supervisor 和 Home Assistant。
order: 8
---


# 测试你的应用 {#test-your-app}
你可以通过三种方式测试应用程序。开发容器是最完整且最舒适的。真正的设备是你进行硬件测试所需要的。普通的 Docker 是进行构建检查最快的方法。

## Devcontainer（开发容器） {#the-devcontainer}
[示例应用仓库](https://github.com/home-assistant/apps-example) 附带了用于 Visual Studio Code 的开发容器。它在你电脑上的容器中运行 Supervisor 和 Home Assistant，并且你仓库中的每个应用都能作为本地应用使用。它适用于 Windows、macOS 和 Linux。

1. 安装 [Visual Studio Code](https://code.visualstudio.com/)、Docker，以及 [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 扩展。
2. 将 `.devcontainer.json` 和 [`.vscode/tasks.json`](https://github.com/home-assistant/apps-example/blob/main/.vscode/tasks.json) 从示例仓库复制到你的仓库中。如果你是从示例仓库开始的，你已经拥有它们。
3. 在 Visual Studio Code 中打开你的仓库，当提示时选择 **在容器中重新打开**。第一次启动可能需要一些时间。
4. 运行任务 **启动 Home Assistant**：打开命令面板，选择 **任务: 运行任务**，然后选择它。这将启动 Supervisor 和 Home Assistant。
5. 打开 `http://localhost:7123/` 并完成入门引导。你的应用会显示在应用商店的 **本地应用** 下。`tasks.json` 中的其他任务会为你安装、启动和重建应用，使用 `ha apps` 命令。将你的应用的标识符添加到 `tasks.json` 底部的列表中以使用它们。

devcontainer 在 `--privileged` 中以 Docker 内运行 Docker，这就是它能够运行整个堆栈的原因。不过，它没有你的硬件。

## 真机设备 {#a-real-device}
对于任何需要真实硬件的情况，比如串口或 Bluetooth，请在具有 Home Assistant OS 的设备上测试。使用 [Samba 共享](https://my.home-assistant.io/redirect/supervisor_app/?app=core_samba) 或 [终端 & SSH](https://my.home-assistant.io/redirect/supervisor_app/?app=core_ssh) 应用，将你的应用文件夹复制到 `local_apps`，就像在 [你的第一个应用](/apps/first-app) 中一样。

如果你的 `config.yaml` 有 `image` 键，Supervisor 会拉取该镜像而不是构建本地更改。在开发时请将该键注释掉，并在发布前恢复：

```yaml
# image: "ghcr.io/me/my-app" {#image-ghcriomemy-app}
```

修改后，在应用商店中选择 **检查更新**，然后在应用页面点击 **重新构建**。通过 SSH，`ha apps rebuild --force local_my_app` 也执行相同操作。

## 纯 Docker {#plain-docker}
要检查你的镜像是否能构建，请在应用程序文件夹中使用 Docker BuildKit：

```bash
docker buildx build -t local/my-app .
```

要为其他架构构建，添加 `--platform`。Docker 对架构的命名不同：`amd64` 是 `linux/amd64`，`aarch64` 是 `linux/arm64`。跨架构构建需要 QEMU 仿真，参见 [Docker 关于多平台构建的文档](https://docs.docker.com/build/building/multi-platform/)。

```bash
docker buildx build --platform linux/arm64 -t local/my-app .
```

你也可以运行镜像，并将你自己的文件夹作为 `/data`。在该文件夹中放置一个 `options.json`，供直接读取它的程序使用：

```bash
docker run --rm -v /tmp/my-app-data:/data -p 8080:8080 local/my-app
```

没有 Supervisor，就没有 `SUPERVISOR_TOKEN` 也没有 Supervisor API，因此每个使用该 API 的 Bashio 调用都会失败。这包括 `bashio::config`，它从 API 而不是 `options.json` 获取选项。使用此方式进行快速检查，而不是完整测试。

## 日志 {#logs}
你的应用写入 `stdout` 和 `stderr` 的所有内容都会显示在应用的 **日志** 标签页中，以及使用 `ha apps logs local_my_app`。如果你的应用无法启动或完全没有显示，请在 **设置** > **系统** > **日志** 下检查 Supervisor 日志，并选择 **Supervisor**。
