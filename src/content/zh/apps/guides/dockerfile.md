---
title: 构建容器镜像
description: 编写你应用的 Dockerfile。选择一个基础镜像，添加你的服务和脚本，并设置构建参数和标签。
order: 1
---


# 构建容器镜像 {#build-the-container-image}
每个应用都是一个容器镜像。你可以像描述其他镜像一样，在应用文件夹中的`Dockerfile`中描述它。Supervisor会在开发过程中在设备上构建它，而[构建器操作](/apps/guides/publishing)会在你发布时为每种架构构建它。

## 一个最简的 Dockerfile {#a-minimal-dockerfile}
```dockerfile
FROM ghcr.io/home-assistant/base:3.24

# Install what your app needs {#install-what-your-app-needs}
RUN apk add --no-cache nginx

# Copy your files into the image {#copy-your-files-into-the-image}
COPY rootfs /
```

当你的服务在`rootfs`中设置好了，这就足够了，如下面的[S6 overlay](/apps/guides/dockerfile#s6-overlay)中所解释的。你也可以更简单地运行单个脚本与`CMD`，就像在[你的第一个应用](/apps/first-app)中一样。

## 基础镜像 {#base-images}
Home Assistant 基础镜像来自 [home-assistant/docker-base](https://github.com/home-assistant/docker-base)，包含了大多数应用所需的一切。它们以多架构镜像的形式发布，适用于 `amd64` 和 `aarch64`。

| 镜像 | 基于 | 示例标签 |
| --- | --- | --- |
| `ghcr.io/home-assistant/base` | Alpine Linux | `3.24` |
| `ghcr.io/home-assistant/base-python` | 带有 Python 的 Alpine Linux | `3.14-alpine3.24` |
| `ghcr.io/home-assistant/base-debian` | Debian | `trixie` |
| `ghcr.io/home-assistant/base-ubuntu` | Ubuntu | `26.04` |

仓库的 README 列出了支持的标签。推荐使用 Alpine：它体积小，这在使用 SD 卡的树莓派上很重要。当你的软件需要 glibc 时，可以使用 Debian 或 Ubuntu。

每个基础镜像都包含：- [S6 覆盖层]（https://github.com/just-containers/s6-overlay）版本3，作为初始化系统和服务监督者。
- [Bashio]（https://github.com/hassio-addons/bashio），一个应用壳函数库。
- [Tempio]（https://github.com/home-assistant/tempio），用于从模板渲染配置文件。
- `bash`、`curl`、`jq`、`tzdata`和CA证书。
- jemalloc，在Alpine图像中。使用时，为你的应用设置`LD_PRELOAD="/usr/local/lib/libjemalloc.so.2"`。

把基础图片的版本钉顶，比如 `base:3.24`，而不是`latest`。这样你的构建可以保持可复现性，像 Renovate 或 Dependabot 这样的工具可以帮你更新标签。

你不必使用这些镜像。只要能在你`arch`的架构上运行，任何镜像都可以。没有 S6 覆盖层，保持默认`init: true`，这样 Docker 会添加初始化进程，省略下面的 Bashio 部分。

## S6 覆盖层 {#s6-overlay}
基础镜像使用 S6 覆盖层作为它们的 init：`/init` 是入口点，它启动并管理你的服务。由此有两个注意事项：

- 在 `config.yaml` 中设置 `init: false`。S6 覆盖层必须是容器中的进程 1，如果 Docker 在它前面添加自己的 init，它将无法启动。
- 不要设置 `host_pid: true`。S6 覆盖层无法在主机的 PID 命名空间中工作。

你在应用的 `rootfs` 文件夹中描述你的服务。一次性运行的步骤是 oneshot 服务，你的程序是 longrun 服务，而 `finish` 脚本决定是否因崩溃而停止容器：

```text
rootfs/etc/s6-overlay/
├── s6-rc.d/
│   ├── init-my-app/
│   │   ├── dependencies.d/base
│   │   ├── run
│   │   ├── type
│   │   └── up
│   └── my-app/
│       ├── dependencies.d/init-my-app
│       ├── finish
│       ├── run
│       └── type
└── user-bundles.d/user/contents.d/
    ├── init-my-app
    └── my-app
```

[使用 S6 覆盖层运行服务](/apps/guides/s6-overlay) 解释了每个文件、较旧的 `/etc/services.d` 格式、完成脚本，以及容易犯的错误。

## Bashio {#bashio}
Bashio 可以帮你免去手动解析 JSON 和调用 Supervisor API 的麻烦。使用 `bashio` 作为脚本的解释器，并在前面加上 `with-contenv`，这样脚本就能获取容器的环境。几个你经常使用的函数：

```bash
#!/command/with-contenv bashio

# Read an option {#read-an-option}
port=$(bashio::config 'port')

# Check if an optional option is set {#check-if-an-optional-option-is-set}
if bashio::config.has_value 'username'; then
  bashio::log.info "Username is set"
fi

# Stop with an error if a required option is empty {#stop-with-an-error-if-a-required-option-is-empty}
bashio::config.require 'password'

# Logging, with levels the user can filter on {#logging-with-levels-the-user-can-filter-on}
bashio::log.debug "Only shown with debug logging"
bashio::log.warning "Something looks off"
```

Bashio 还封装了大部分 Supervisor API，比如 `bashio::services 'mqtt' 'host'` 和 `bashio::app.ingress_port`。每个函数都可以在 [Bashio 参考](/apps/bashio) 中找到。

## 构建参数 {#build-arguments}
Supervisor 和构建器操作传递两个构建参数：

| 参数 | 内容 |
| --- | --- |
| `BUILD_ARCH` | 构建的体系结构：`aarch64` 或 `amd64` |
| `BUILD_VERSION` | 来自 `config.yaml` 的 `version` |

在使用它们之前，用 `ARG` 声明它们：

```dockerfile
ARG BUILD_ARCH
RUN echo "Building for ${BUILD_ARCH}"
```

两者都使用 Docker BuildKit 构建，因此标准的 `TARGETARCH` 参数也可用。请注意，它显示为 `arm64`，而 Home Assistant 显示为 `aarch64`。

如果每种架构需要不同的 `Dockerfile`，请将其命名为 `Dockerfile.aarch64` 或 `Dockerfile.amd64`。Supervisor 会在该架构中使用它，而不是 `Dockerfile`。

> [!注意]
> 自 Supervisor 2026.04.0 版本起，`BUILD_FROM` 不再默认传递。如果你的 `Dockerfile` 以 `FROM ${BUILD_FROM}` 开始，请为该参数设置默认值，或用固定的 `FROM` 替换它。

## 标签 {#labels}
Supervisor 从图像中读取了一些标签：

| 标签 | 内容 |
| --- | --- |
| `io.hass.version` | 应用程序的版本 |
| `io.hass.arch` | 图像的架构 |
| `io.hass.type` | `app` |

在大多数情况下，你不需要自己设置它们。当 Supervisor 构建一个应用程序时，它会添加所有三个。构建器的 `build-image` 操作会添加 `io.hass.version` 和 `io.hass.arch`。如果你以其他方式构建图像，请使用 `LABEL` 添加它们：

```dockerfile
LABEL \
  io.hass.version="1.0.0" \
  io.hass.type="app" \
  io.hass.arch="aarch64"
```

对于没有这些标签的现有图像，在 `config.yaml` 中设置 `legacy: true`。

## build.yaml {#buildyaml}
较旧的应用程序在 `config.yaml` 旁边有一个 `build.yaml`，每个架构的基础镜像为 (`build_from`)，额外的构建参数为 (`args`)，标签为 (`labels`)。此文件已弃用。Supervisor 仍然会读取它，但会显示警告，但请将所有内容放在 `Dockerfile` 中：

- `build_from`: 一行 `FROM`，或者带有默认值的 `ARG BUILD_FROM=...`。
- `args`: 带默认值的 `ARG` 多行。
- `labels`: `LABEL` 多行。
- `squash`: 没有替代；BuildKit 不支持它。
