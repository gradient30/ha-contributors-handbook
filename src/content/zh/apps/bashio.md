---
title: Bashio
description: 应用基础镜像中的 shell 函数库。如何加载它，它会对你的脚本产生哪些变化，以及它包含的每个函数。
order: 30
---


# Bashio {#bashio}
Bashio 是一个用于应用程序的 Bash 函数库。它可以读取应用程序的选项，按级别写入日志信息，并在 500 多个函数中封装 [Supervisor API](/apps/supervisor-api)，因此你的脚本无需自己处理 `curl`、令牌和 `jq`。它由 [Home Assistant 社区应用](https://github.com/hassio-addons/bashio) 制作，并随每个 Home Assistant 基础镜像提供。

下面页面上的函数列表是根据其源代码中的文档块生成的。

## 哪些镜像包含它 {#which-images-have-it}
Home Assistant 基础镜像和 S6 覆盖层都附带 Bashio：

- [`ghcr.io/home-assistant/base`](https://github.com/home-assistant/docker-base)，以及它的 Python、Debian 和 Ubuntu 变体
- [`ghcr.io/hassio-addons/base`](https://github.com/hassio-addons/app-base)，Home Assistant 社区应用的基础镜像

镜像包含哪些版本可以在其仓库的 Dockerfile 中查看。在镜像中，库位于 `/usr/lib/bashio`，`/usr/bin/bashio` 会加载它。

在另一镜像上构建？从这些 Dockerfile 中复制步骤：它们会下载 Bashio 的版本，将其 `lib` 文件夹移动到 `/usr/lib/bashio`，并将 `/usr/lib/bashio/bashio` 链接到 `/usr/bin/bashio`。

## 加载 Bashio {#load-bashio}
使用 `bashio` 作为你的脚本解释器，而不是 `bash`：

```bash
#!/command/with-contenv bashio

name=$(bashio::config 'name')
bashio::log.info "Hello ${name}!"
```

`bashio` 命令加载库，然后使用它运行你的脚本。`with-contenv` 来自 [S6 overlay](/apps/guides/s6-overlay#the-container-environment)：它为脚本提供容器的环境。Bashio 需要这个，因为它从中读取 `SUPERVISOR_TOKEN` 来调用 Supervisor API，甚至 `bashio::config` 也从该 API 获取你的选项。没有 `with-contenv`，S6 启动的脚本没有令牌，这些调用将失败。

`#!/usr/bin/with-contenv bashio` 在上述所有镜像中也能工作：它们安装 S6 overlay 为旧脚本提供的 `/usr/bin` 链接。对于不需要容器环境的脚本，`#!/usr/bin/env bashio` 就足够了。

## Bashio 在你的脚本中做的更改 {#what-bashio-changes-in-your-script}
Bashio 在运行你的脚本之前会开启严格的错误处理：

- `errexit`：当命令失败时，脚本会停止。
- `nounset`：当使用未设置的变量时，脚本会停止。
- `pipefail`：当管道中的任何命令失败时，管道就会失败，而不仅仅是最后一个命令。
- `errtrace` 和 `inherit_errexit`：相同的规则也适用于函数内部和 `$(...)`。

这样可以及早发现错误，但这也意味着预期的失败需要处理。一个 `grep` 找不到内容会返回 `1` 并停止你的脚本。添加 `|
| true`，在 `if` 中测试命令，或者使用 [`bashio::try`](/apps/bashio/logging#try)。

## 函数如何返回结果 {#how-the-functions-answer}
Bashio 函数有两种返回方式：

- 检查型函数，例如 `bashio::config.true` 或 `bashio::fs.file_exists`，不会打印任何内容。它们会返回退出状态 `0` 表示是，`1` 表示否，所以你可以在 `if` 中使用它们。
- 获取型函数，例如 `bashio::config` 或 `bashio::app.version`，会打印出值。使用 `$(...)` 来捕获它。

日志信息不会与捕获的值混在一起。Bashio 在加载时会保留一份标准输出的副本，并将日志信息写入那里。更多内容请参见 [logging](/apps/bashio/logging)。

大多数调用 Supervisor API 的函数会在文件 `/tmp/.bashio` 中缓存返回结果。容器中的每个脚本都可以共享该缓存。通过 API 更改设置的函数，例如 `bashio::app.options` 设置了新值，之后会清空整个缓存，因此你不会重新读取到旧的值。

## 环境变量 {#environment-variables}
Bashio 在加载时会读取这些变量：

| 变量 | 默认值 | 功能 |
| --- | --- | --- |
| `SUPERVISOR_TOKEN` | 空 | Supervisor API 的令牌。Supervisor 为每个应用程序设置它。 |
| `SUPERVISOR_API` | `http://supervisor` | Supervisor API 的地址。 |
| `LOG_LEVEL` | `5` (信息) | 日志级别，用数字表示，从 `0`（关闭）到 `8`（全部）。 |
| `LOG_FORMAT` | `[{TIMESTAMP}] {LEVEL}: {MESSAGE}` | 日志消息的格式。 |
| `LOG_TIMESTAMP` | `%T` | `{TIMESTAMP}` 的格式，类似 `date` 命令的格式。 |
| `CACHE_DIR` | `/tmp/.bashio` | 缓存存放的位置。 |
| `HIBP_ENDPOINT` | `https://api.pwnedpasswords.com/range` | 用于密码检查的 Have I Been Pwned API。 |

## 已弃用名称 {#deprecated-names}
应用程序以前被称为附加组件，Bashio 函数也是如此。每个 `bashio::app.*`、`bashio::apps` 和 `bashio::apps.*` 函数仍然有一个旧名称的别名：`bashio::addon.*`、`bashio::addons` 和 `bashio::addons.*`。别名会调用新函数，并在第一次使用时记录警告。别名可能会在将来的版本中被移除，因此在新代码中请使用新名称。

其他一些旧名称的工作方式也相同：`hass.die_if_true` 和 `hass.die_if_empty` 会调用 `bashio::exit.die_if_true` 和 `bashio::exit.die_if_empty`，而 `bashio::pwned.occurances` 会调用 `bashio::pwned.occurrences`。这些在每次调用时都会记录警告。

## 函数 {#functions}
函数按其作用对象分组。每个页面列出了其模块的所有公共函数，包括其参数和来源中的描述。

- [选项](/apps/bashio/config)：阅读并检查你的应用程序的选项。
- [日志记录、退出和错误](/apps/bashio/logging)：日志级别、有色输出、停止脚本，以及`bashio::try`。
- [应用](/apps/bashio/apps)：你自己的应用和其他应用：设置、状态、端口、入口和资源使用情况。
- [Supervisor 和系统](/apps/bashio/supervisor)：原始 API 调用、Supervisor、系统信息、更新、任务、备份、仓库、挂载、Docker 和安全设置。
- [核心、主机和操作系统](/apps/bashio/core-host-os)：Home Assistant Core、主机、Home Assistant OS、硬件和网络。
- [插件](/apps/bashio/plugins)：音频、CLI、DNS、多播和观察者。
- [服务、发现、认证和入口](/apps/bashio/services)：MQTT 和其他服务、发现消息、用户凭据以及入口会话。

- [变量、字符串、文件和 JSON](/apps/bashio/helpers)：用于值、字符串、文件、jq、缓存、端口以及“我是否被泄露过”的助手。

## 帮助和更改 {#help-and-changes}
缺少功能或发现错误？Bashio 有其自己的仓库：[hassio-addons/bashio](https://github.com/hassio-addons/bashio)。其 README 中指出某些部分的 Supervisor API 尚无功能。对于这些部分，请直接调用 [`bashio::api.supervisor`](/apps/bashio/supervisor#api)。
