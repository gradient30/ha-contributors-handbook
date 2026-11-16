---
title: 运行时环境
description: 应用容器从Supervisor获得什么。环境变量、文件夹、主机名和网络地址。
order: 4
---


# 运行时环境 {#runtime-environment}
当 Supervisor 启动你的应用时，它会配置容器，使你的代码可以依赖几样东西。本页列出了它们。

## 环境变量 {#environment-variables}
| 变量 | 内容 |
| --- | --- |
| `SUPERVISOR_TOKEN` | 你的应用的令牌，用于 Supervisor API 和 Home Assistant Core API 代理。每个应用都是唯一的。 |
| `HASSIO_TOKEN` | 相同的令牌，旧名称形式。在新代码中使用 `SUPERVISOR_TOKEN`。 |
| `TZ` | 系统的时区，如 `Europe/Amsterdam`。 |

你从 `environment` 在 `config.yaml` 中定义的变量也会被添加。使用 `legacy: true` 时，顶级选项里是字符串或数字的也会作为变量传入。

基础镜像使用 S6 overlay，它将容器的环境保持在一个单独的位置。以 `#!/command/with-contenv bashio`（或 `with-contenv bash`）开头的脚本可以获取这些变量；由 S6 启动的其他脚本可能不会。请参阅 [容器环境](/apps/guides/s6-overlay#the-container-environment)。

## 文件夹 {#folders}
| 路径 | 内容 |
| --- | --- |
| `/data` | 你应用的私有、持久存储。可读写，包含在备份中。 |
| `/data/options.json` | 用户的选项，根据你的 `schema` 进行验证。每次启动前写入。 |

通过 `map` 映射的文件夹会挂载在这些路径下，除非你设置了不同的 `path`：

| 类型 | 路径 |
| --- | --- |
| `homeassistant_config` | `/homeassistant` |
| `app_config` | `/config` |
| `all_app_configs` | `/app_configs` |
| `local_apps` | `/local_apps` |
| `ssl` | `/ssl` |
| `share` | `/share` |
| `media` | `/media` |
| `backup` | `/backup` |

映射的文件夹为只读，除非你设置了 `read_only: false`。

根据 `config.yaml` 中的其他键，Supervisor 会挂载更多：|说明 |已装甲 |
|--- |--- |
|`tmpfs: true` |`/tmp` 作为 TMPFS，在记忆中 |
|`host_ipc: false` |私人`/dev/shm`，纪念 |
|`audio: true` |`/etc/pulse/client.conf`、`/run/audio`和`/etc/asound.conf` |
|`devicetree: true` |`/device-tree` |
|`gpio: true` |`/sys/class/gpio`，关于支持它的系统 |
|`udev: true` |`/run/udev`，只读 |
|`kernel_modules: true` |`/lib/modules`，只读 |
|`host_dbus: true` |`/run/dbus`，只读 |
|`journald: true` |`/var/log/journal` 和 `/run/log/journal`，只读 |
|`docker_api: true` |`/run/docker.sock`，只读，仅在关闭保护模式时 |

## 网络 {#network}
除非你设置 `host_network`，否则你的应用将在内部网络中运行，`172.30.32.0/23`，与 Supervisor 及其他应用一起运行。Home Assistant Core 从内部网络也可以访问。

| 名称 | 它是什么 |
| --- | --- |
| `supervisor` | Supervisor，带有其 API。总是 `172.30.32.2`。`hassio` 是别名。 |
| `homeassistant` | Home Assistant Core。它运行在主机网络上，可通过内部网络网关 `172.30.32.1` 访问。 |
| `{repository}-{slug}` | 另一个应用，如 `core-mosquitto` 或 `local-hello-world`。 |

你自己容器的主机名是你的应用 ID，将 `_` 替换为 `-`。有了 `host_uts: true`，它就是主机的主机名。

`supervisor` 和 `hassio` 已添加到你容器的 hosts 文件中，因此它们在主机网络上也可用。运行在主机网络上的应用仍会在内部 DNS 中按名称注册，指向网关 `172.30.32.1`，所以其他应用也能通过名称访问它。入口请求总是来自 Supervisor、`172.30.32.2`。

## 初始化 {#init}
Home Assistant 基础镜像使用 S6 overlay 作为它们的初始化系统，`/init` 作为入口点。在 `config.yaml` 中设置 `init: false`，以便 Docker 不在它前面添加自己的初始化进程。参见 [使用 S6 overlay 运行服务](/apps/guides/s6-overlay)。
