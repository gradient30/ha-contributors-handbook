---
title: 你的第一个应用
description: 构建一个“Hello world”应用，将其安装在你自己的Home Assistant上，并将其发展成一个带有选项的小型网络服务器。
order: 2
---


# 你的第一个应用 {#your-first-app}
理解应用程序最快的方法是自己构建一个。在本教程中，你将编写一个小型应用程序，将其安装在你自己的Home Assistant上，然后逐步扩展它。大约需要半小时。

你需要一个可以运行应用程序的Home Assistant安装，这意味着Home Assistant OS，以及一种将文件放到它上的方法。

## 1. 访问本地应用程序文件夹 {#1-get-access-to-the-local-apps-folder}
Supervisor 会在名为 `local_apps` 的文件夹中查找你自己构建的应用程序。那里每个应用程序都会显示在应用商店的 **本地应用** 下。要访问该文件夹，请先安装以下任意一个应用程序：

- [Samba 共享](https://my.home-assistant.io/redirect/supervisor_app/?app=core_samba)：你的 Home Assistant 会在计算机上显示为网络共享，其中有一个名为 `local_apps` 的文件夹。在 macOS 上，如果没有显示，请打开 Finder，按 <kbd>Cmd</kbd> <kbd>K</kbd>，然后输入 `smb://homeassistant.local`。
- [终端 & SSH](https://my.home-assistant.io/redirect/supervisor_app/?app=core_ssh)：打开它的网络终端，或通过 SSH 登录，并在 `/local_apps` 中操作。对于 SSH，请先将你的公钥添加到应用配置中，详见其文档。

## 2. 创建应用程序 {#2-create-the-app}
在 `local_apps` 中，创建一个名为 `hello_world` 的文件夹，并包含三个文件：`Dockerfile`、`config.yaml` 和 `run.sh`。

`Dockerfile` 描述了你的应用程序的容器镜像。它以 Home Assistant 基础镜像为起点，该镜像已经包含了大多数应用程序所需的工具：

```dockerfile
FROM ghcr.io/home-assistant/base:3.24

# Copy the start script into the image {#copy-the-start-script-into-the-image}
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
```

`config.yaml` 告诉 Supervisor 你的应用程序是什么以及它需要什么：

```yaml
name: "Hello world"
description: "My first real app!"
version: "1.0.0"
slug: "hello_world"
init: false
arch:
  - aarch64
  - amd64
```

`run.sh` 脚本在你的应用程序启动时运行：

```bash
#!/command/with-contenv bashio

bashio::log.info "Hello world!"
```

> [!重要]
> 请使用 Unix 换行符 (LF) 保存 `run.sh`，而不是 Windows 换行符 (CRLF)。使用 CRLF 时，脚本启动会失败，并且错误信息中不会提到换行符问题。

关于这些文件，有几点值得了解：- `slug` 是你的应用程序的 ID。它在仓库中必须是唯一的，并且最好给文件夹起相同的名字。
- 需要 `init: false` 因为基础镜像自带自己的初始化系统，S6 overlay。[使用 S6 overlay 运行服务](/apps/guides/s6-overlay) 解释了原因。
- `run.sh` 的第一行加载了 [Bashio](/apps/bashio)，这是一个针对应用的 shell 函数库，并使用容器的环境。`bashio::log.info` 写入一行包含时间和级别的日志。在步骤 6 中，你也使用 Bashio 来读取选项。

## 3. 安装并启动你的应用程序 {#3-install-and-start-your-app}
1. 在 Home Assistant 中，转到 **设置** > **应用程序**，然后选择 **安装应用程序**。这将打开 **应用商店**。
2. 在右上角菜单中，选择 **检查更新**。如有需要，请刷新页面。
3. 一个新的部分 **本地应用** 会显示你的应用程序。选择它。
4. 选择 **安装**。Supervisor 现在会从你的 `Dockerfile` 构建镜像，这需要一些时间。
5. 选择 **启动**，然后打开 **日志** 标签页。你会看到类似 `[12:34:56] INFO: Hello world!` 的一行。

### 我的应用程序没有显示 {#my-app-does-not-show-up}
首先，刷新你的浏览器，Windows 和 Linux 系统使用 <kbd>Ctrl</kbd>   <kbd>F5</kbd>，macOS 系统使用 <kbd>Cmd</kbd>   <kbd>Shift</kbd>   <kbd>R</kbd>。如果它仍然没有显示，Supervisor 无法读取你的 `config.yaml`。它可能是无效的 YAML，或者其中一个键的值是 Supervisor 不接受的。

Supervisor 日志会告诉你是哪一个。前往 **设置** > **系统** > **日志**，在右上角菜单中选择 **Supervisor**，并查找提到你的应用程序的行。修复问题后，再次在应用商店中选择 **检查更新**。

## 4. 提供网页服务 {#4-serve-a-web-page}
一个只能打印一行的应用程序还不够实用。让我们将其变成一个 Web 服务器，使用 Python 自带的 HTTP 服务器。

在 `Dockerfile` 中安装 Python，并将 `/data` 设置为工作目录。`/data` 是应用程序的持久化存储；稍后会详细说明。

```dockerfile
FROM ghcr.io/home-assistant/base:3.24

# Install the requirements of the app {#install-the-requirements-of-the-app}
RUN apk add --no-cache python3

# The Python HTTP server serves the working directory {#the-python-http-server-serves-the-working-directory}
WORKDIR /data

COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
```

在 `run.sh` 中启动服务器：

```bash
#!/command/with-contenv bashio

bashio::log.info "Hello world!"

python3 -m http.server 8000
```

然后将容器的 8000 端口映射到主机的 8000 端口，并升级版本：

```yaml
name: "Hello world"
description: "My first real app!"
version: "1.1.0"
slug: "hello_world"
init: false
arch:
  - aarch64
  - amd64
startup: services
ports:
  8000/tcp: 8000
```

## 5. 安装更新 {#5-install-the-update}
因为你已经提出 `version`，Home Assistant 为你的应用提供了更新。如果你还没有看到更新，请在应用商店中选择 **检查更新**，然后更新应用。Supervisor 会根据你的更改重新构建镜像。你忘记提高版本了吗？那就卸载然后重新安装应用。

启动应用并在浏览器中打开 `http://homeassistant.local:8000`。你会看到一个文件列表，其中有一个文件：`options.json`。

## 6. 添加选项 {#6-add-options}
`options.json` 保存了用户为你的应用选择的设置。Supervisor 会在你的应用启动前将其写入 `/data`。现在它是空的，因为你的应用还没有任何选项。向 `config.yaml` 添加一些选项：`options` 保存默认值，`schema` 说明每个选项的类型。

```yaml
options:
  name: "world"
  beer: true
  year: 2017
schema:
  name: str
  beer: bool
  year: int
```

再次提升版本并更新应用。你应用的 **配置** 选项卡现在显示一个包含这三个选项的表单。更改一个选项，保存，然后重启应用。从你的网络服务器下载 `options.json`，你会在其中看到你的值。

你的脚本可以使用 Bashio 读取这些选项。修改 `run.sh`：

```bash
#!/command/with-contenv bashio

name=$(bashio::config 'name')
bashio::log.info "Hello ${name}!"

if bashio::config.true 'beer'; then
  bashio::log.info "Cheers, it is $(bashio::config 'year')."
fi

python3 -m http.server 8000
```提升版本、更新，并再次启动应用程序。日志现在会显示你设置的名字。`bashio::config` 从 Supervisor 获取选项，这也是脚本以 `with-contenv` 开始的原因之一：那会给它询问所需的令牌。[Bashio options reference](/apps/bashio/config) 包含了所有选项功能。

## 接下来是什么 {#what-is-next}
你现在已经掌握了基础：一个 `Dockerfile`、一个 `config.yaml`、选项、日志记录和一个端口。

接下来：[构建一个真实的应用](/apps/build-a-real-app)。它演示了一个完整的示例应用，包括按顺序启动的服务、使用 Bashio 的选项和日志记录、翻译、文档、CI 和发布。这就是设置其他人可以安装的应用的方法。

之后，[应用是如何工作的](/apps/how-apps-work) 解释了 Supervisor 如何处理你的应用。

从这里可以去的其他地方：- 使用 [ingress](/apps/guides/ingress) 在 Home Assistant 界面中显示你的网络服务器，而不是打开端口。
- 复制 [示例应用仓库](https://github.com/home-assistant/apps-example) 作为你自己的起点。它包含构建工作流、文档文件和已准备好的 AppArmor 配置文件。
- 查阅 [应用配置](/apps/reference/configuration) 参考中的每个键。
- 准备好协助官方应用或其背后的工具吗？继续阅读 [贡献官方应用](/apps/first-contribution#2-pick-where-to-help)。
