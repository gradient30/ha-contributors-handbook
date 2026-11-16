---
title: 应用配置
description: 应用程序的 config.yaml 的每个键、它的作用以及 Supervisor 接受的内容。
order: 1
---

# 应用配置 {#app-configuration}

每个应用程序在其文件夹中都有一个配置文件，用于告诉Supervisor应用程序是什么以及它需要什么。本页列出了Supervisor接受的每个键。它遵循Supervisor代码中的模式（[`supervisor/apps/validate.py`](https://github.com/home-assistant/supervisor/blob/main/supervisor/apps/validate.py)）。

该文件称为`config.yaml`、`config.yml`或`config.json`。这里的所有示例都使用 YAML。因为Supervisor会在存储库中任意深度搜索这些名称，所以不要将`config.yaml`用于应用程序的其他用途，除非它在名为`rootfs`的文件夹或隐藏文件夹内。

```yaml
name: "Hello world"
version: "1.1.0"
slug: "hello_world"
description: "My first real app!"
url: "https://github.com/me/my-apps/tree/main/hello_world"
arch:
  - aarch64
  - amd64
init: false
ports:
  8000/tcp: 8000
map:
  - type: share
    read_only: false
  - type: homeassistant_config
    path: /custom/config/path
image: "ghcr.io/me/hello-world"
```

Supervisor不知道的键会被忽略而不发出警告，所以请检查拼写。

## 必填键 {#required-keys}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `name` | 字符串 | 应用的名称，在应用商店和用户界面中显示。 |
| `version` | 字符串 | 应用的版本。当使用 `image` 时，这也是 Supervisor 所提取的标签。请用引号引起来，以免 YAML 将 `1.10` 解析为数字。 |
| `slug` | 字符串 | 应用的 ID。仅限字母、数字、`-`、`_` 和 `.`。在仓库中必须唯一。 |
| `description` | 字符串 | 简短描述，在应用商店显示。 |
| `arch` | 列表 | 应用支持的 CPU 架构：`aarch64` 和 `amd64`。仍然接受已弃用的值 `armhf`、`armv7` 和 `i386`，但会显示警告。 |

## 信息与行为| 键 | 类型 | 默认值 | 描述 | {#information-and-behavior}
| --- | --- | --- | --- |
| `url` | URL | | 应用的主页，如仓库或论坛帖子。在应用页面显示。 |
| `machine` | 列表 | all | 应用运行的机器类型。见 [machine](/apps/reference/configuration#machine)。 |
| `homeassistant` | 字符串 | | 应用所需的最低 Home Assistant Core 版本，如 `2026.10.0`。 |
| `startup` | 字符串 | `application` | 应用在启动时的行为：`initialize`、`system`、`services`、`application` 或 `once`。见 [应用如何工作](/apps/how-apps-work#starting)。 |
| `boot` | 字符串 | `auto` | `auto` 在启动时启动应用。`manual` 默认关闭 **启动时启动**。`manual_only` 关闭它并不允许用户开启。 |
| `stage` | 字符串 | `stable` | 应用所处的生命周期阶段：`stable`、`experimental` 或 `deprecated`。 || `init` | 布尔值 | `true` | 使用 Docker 的默认 init 进程运行容器。当镜像有自己的 init 时设置为 `false`，Home Assistant 基础镜像的情况都是如此（否则 S6 overlay 版本 3 无法启动）。 |
| `timeout` | 整数 | `10` | Supervisor 等待应用程序停止的秒数，然后才会杀掉容器。范围在 10 到 300 之间。 |
| `breaking_versions` | 列表 | | 需要用户注意的版本。自动更新不会安装或跨越这些版本中的任意一个。 |
| `environment` | 映射 | | 容器的额外环境变量。 |
| `legacy` | 布尔值 | `false` | 对于没有 Home Assistant 标签的镜像：也会将顶级选项（如果它们是字符串或数字）作为环境变量传递。 || `stdin` | 布尔值 | `false` | 保持容器的标准输入打开，以便 Home Assistant 可以通过 `hassio.app_stdin` 操作发送数据。 |
| `tmpfs` | 布尔值 | `false` | 将 `/tmp` 挂载为 tmpfs，一个内存中的文件系统。 |

### 机器 {#machine}

没有 `machine` 时，该应用程序在每台机器上都可用。 有了它后，该应用程序只在您列出的机器类型上可用。 前面带有 `!` 的条目，如 `!raspberrypi5-64`，明确排除了某种机器类型。

接受的值有 `generic-aarch64`、`generic-x86-64`、`green`、`intel-nuc`、`khadas-vim3`、`odroid-c2`、`odroid-c4`、`odroid-m1`、`odroid-n2`、`qemuarm-64`、`qemux86-64`、`raspberrypi3-64`、`raspberrypi4-64`、`raspberrypi5-64` 和 `yellow`。 已弃用的值 `odroid-xu`、`qemuarm`、`qemux86`、`raspberrypi`、`raspberrypi2`、`raspberrypi3`、`raspberrypi4` 和 `tinker` 仍然被接受，但会有警告。

## 图片 {#image}

| 键 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `image` | 字符串 | | 要拉取的镜像，不带标签，例如 `ghcr.io/me/my-app`。标签始终是 `version`。没有 `image` 时，Supervisor 会在设备上构建应用。 |

使用多架构镜像的名称。对于按架构发布的镜像，比如 `ghcr.io/me/{arch}-my-app`，占位符 `{arch}` 仍然受支持。请参阅 [发布您的应用](/apps/guides/publishing)。

## 选项 {#options}

| 键 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `options` | 映射 | `{}` | 应用的选项及其默认值。 |
| `schema` | 映射或 `false` | `{}` | 每个选项的类型，用于验证用户输入并在用户界面中构建表单。`false` 关闭验证和表单。 |

类型和规则在 [添加选项](/apps/guides/options#schema-types) 中。

## 网络 {#network}

| 键 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `ports` | 映射 | | 在主机上要暴露的端口，如 `"container-port/protocol": host-port`，例如 `8080/tcp: 8080`。协议是 `tcp` 或 `udp`。主机端口为 `null`（或无值）表示默认情况下端口关闭；用户可以开启它。 |
| `ports_description` | 映射 | | 每个端口的描述，使用与 `ports` 相同的键。优先使用 [翻译](/apps/guides/presentation#translations)。 |
| `host_network` | 布尔值 | `false` | 在主机网络上运行应用，而不是在内部网络上。 |
| `webui` | 字符串 | | Web 界面的 URL，用于 **Open Web UI** 按钮。请参阅 [URL 模板](/apps/reference/configuration#url-templates)。 |
| `watchdog` | 字符串 | | watchdog 检查应用是否健康的 URL。请参阅 [URL 模板](/apps/reference/configuration#url-templates)。 |

### URL 模板 {#url-templates}

`webui` 和 `watchdog` 使用占位符，由 Supervisor 填充：

- `[HOST]`：主机。对于 **Open Web UI**，这是用户访问 Home Assistant 的地址；看门狗使用应用的 IP 地址。
- `[PORT:8080]`：对于 **Open Web UI**，主机上映射到容器端口 8080 的端口。看门狗连接到应用的 IP 地址，所以它本身使用容器端口 8080，除非应用在主机网络上运行。
- `[PROTO:option]`：如果名为 `option` 的选项是 `true`，则为 `https`，否则为 `http`。

```yaml
webui: "[PROTO:ssl]://[HOST]:[PORT:8080]/dashboard"
watchdog: "http://[HOST]:[PORT:8080]/health"
```

`webui` 的格式是 `http`、`https` 或 `[PROTO:option]`，然后是 `://[HOST]:[PORT:number]`，然后是可选路径。`watchdog` 接受相同的格式，也接受 `tcp://[HOST]:[PORT:number]` 仅检查该端口是否接受连接。在 `watchdog` 中，端口也可以是单独的数字。HTTP 看门狗将任何低于 300 的响应视为正常。

## 入口| 键 | 类型 | 默认值 | 描述 | {#ingress}
| --- | --- | --- | --- |
| `ingress` | 布尔型 | `false` | 在 Home Assistant 内显示应用的网页界面。请参见 [通过 Ingress 添加网页界面](/apps/guides/ingress)。 |
| `ingress_port` | 整数 | `8099` | 容器内网页服务器监听的端口。`0` 允许 Supervisor 在 62000 到 65500 之间选择一个空闲端口，应用可通过 API 获取。主要用于主机网络上的应用。 |
| `ingress_entry` | 字符串 | | Ingress URL 的起始路径，如果不是 `/`。 |
| `ingress_stream` | 布尔型 | `false` | 将请求体直接流式传输到应用，而不是先读入内存。大文件上传时需要。 |
| `panel_icon` | 字符串 | `mdi:puzzle` | 应用在侧边栏的图标，来源于 [Material Design 图标](https://pictogrammers.com/library/mdi/)。 |
| `panel_title` | 字符串 | 应用名称 | 应用在侧边栏的标题。 || `panel_admin` | 布尔值 | `true` | 仅在管理员的侧边栏中显示该应用。 |

具有 `ingress_port: 0` 的应用在 `ports` 中不得暴露 62000 至 65500 之间的任何端口；Supervisor 会拒绝该配置。

## 文件夹 {#folders}

`map` 列出了要在容器中挂载的主机文件夹。每个条目都有一个 `type`，可选的还有 `read_only`（默认 `true`）和 `path`（容器中的挂载点）。

```yaml
map:
  - type: share
    read_only: false
  - type: ssl
  - type: media
    path: /mnt/media
```| 类型 | 挂载于 | 内容 |
| --- | --- | --- |
| `homeassistant_config` | `/homeassistant` | Home Assistant 的配置文件夹 |
| `app_config` | `/config` | 此应用的公共配置文件夹。请参见 [用户配置文件](/apps/guides/options#configuration-files-for-users) |
| `all_app_configs` | `/app_configs` | 所有应用的公共配置文件夹 |
| `local_apps` | `/local_apps` | 本地应用文件夹 |
| `ssl` | `/ssl` | 证书 |
| `share` | `/share` | Home Assistant 与应用共享的文件 |
| `media` | `/media` | 媒体文件 |
| `backup` | `/backup` | 备份 |
| `data` | `/data` | 此应用的私有数据。始终以读写方式挂载；仅使用此类型来更改 `path` |

如果设置 `path`，它不能为空，不能为 `/`，也不能与其他条目的路径相同。旧名称仍然被接受，但会有警告：`addons` 对于 `local_apps`（安装在 `/addons`），`all_addon_configs` 对于 `all_app_configs`（安装在 `/addon_configs`），以及 `addon_config` 对于 `app_config`。旧的 `config` 类型在 `/config` 安装 Home Assistant 配置；请改用 `homeassistant_config`。旧的简写形式，例如 `share:rw`，仍然有效。

## 硬件| 键 | 类型 | 默认值 | 描述 | {#hardware}
| --- | --- | --- | --- |
| `devices` | 列表 | | 映射到容器的设备路径，例如 `/dev/ttyAMA0`。 |
| `uart` | 布尔 | `false` | 将所有串行设备映射到容器中。 |
| `usb` | 布尔 | `false` | 将原始 USB 设备（`/dev/bus/usb`）映射到容器中，并支持热插拔。 |
| `gpio` | 布尔 | `false` | 在支持的系统上将 `/sys/class/gpio` 映射到容器中。 |
| `udev` | 布尔 | `false` | 以只读方式挂载主机的 udev 数据库（`/run/udev`）。 |
| `devicetree` | 布尔 | `false` | 将主机的设备树挂载到 `/device-tree`。 |
| `video` | 布尔 | `false` | 访问所有视频设备。 |
| `audio` | 布尔 | `false` | 通过 PulseAudio 将应用程序连接到 Home Assistant 的音频系统。 || `kernel_modules` | 布尔值 | `false` | 挂载主机的内核模块（`/lib/modules`），只读，并添加 `SYS_MODULE` 功能。 |
| `full_access` | 布尔值 | `false` | 完全访问所有硬件。仅在保护模式关闭时有效。不要将其与 `devices`、`uart`、`usb` 或 `gpio` 结合使用；这些将被忽略。 |

有关每个选项的更多信息，请参见 [访问硬件和主机](/apps/guides/hardware)。

## 主机和权限| 键 | 类型 | 默认值 | 描述 | {#host-and-privileges}
| --- | --- | --- | --- |
| `privileged` | 列表 | | 要添加的 Linux 功能。请参阅 [特权](/apps/reference/configuration#privileged)。 |
| `apparmor` | 布尔值 | `true` | 使用 AppArmor 运行应用程序。在应用程序文件夹中有 `apparmor.txt` 时，Supervisor 会使用该配置文件；否则使用 Docker 的默认配置文件。 |
| `host_dbus` | 布尔值 | `false` | 挂载主机的 D-Bus 系统总线 (`/run/dbus`)，只读。 |
| `host_pid` | 布尔值 | `false` | 使用主机的 PID 命名空间。仅在保护模式关闭时有效。不适用于 S6 覆盖。 |
| `host_uts` | 布尔值 | `false` | 使用主机的 UTS 命名空间（主机名）。 |
| `host_ipc` | 布尔值 | `false` | 当 `false` 时，应用程序在内存中获得自己的私有 `/dev/shm`。设置为 `true` 以将 `/dev/shm` 保留为容器默认值。 || `realtime` | 布尔值 | `false` | 允许实时调度：在系统支持的情况下，添加 `SYS_NICE`、实时优先级限制和实时 CPU 配额。 |
| `journald` | 布尔值 | `false` | 在 `/var/log/journal` 和 `/run/log/journal` 挂载主机的系统日志（只读）。检查哪个有内容，因为每个系统可能不同。 |
| `ulimits` | 映射 | | 容器的资源限制。请参阅 [ulimits](/apps/reference/configuration#ulimits)。 |

### 特权 {#privileged}

您可以添加的功能包括 `AUDIT_WRITE`、`BPF`、`CHECKPOINT_RESTORE`、`DAC_READ_SEARCH`、`IPC_LOCK`、`MKNOD`、`NET_ADMIN`、`NET_RAW`、`PERFMON`、`SETFCAP`、`SYS_ADMIN`、`SYS_MODULE`、`SYS_NICE`、`SYS_PTRACE`、`SYS_RAWIO`、`SYS_RESOURCE` 和 `SYS_TIME`。只请求您的应用需要的功能：其中许多会降低 [安全评级](/apps/reference/security-rating)。

`AUDIT_WRITE`、`MKNOD`、`NET_RAW` 和 `SETFCAP` 是当今 Docker 默认配置的一部分。Supervisor 正在转向更小的默认集，不包含它们，并且在默认情况下关闭的两个功能标志：`app_drop_net_raw` 会删除 `NET_RAW`，`app_reduced_capabilities` 会删除其他三项。如果您的应用需要其中一项，请现在在 `privileged` 中列出；您请求的功能永远不会被删除。

### ulimits {#ulimits}

每个限制都是一个数字，或一个包含 `soft` 和 `hard` 的映射：

```yaml
ulimits:
  nofile:
    soft: 65535
    hard: 65535
  nproc: 4096
```

一个值不能高于主机的硬限制。在 Home Assistant OS 上，`nofile` 的硬限制是 524288；主机上的 `ulimit -Ha` 显示了它们全部。

## API 访问 {#api-access}

| 键 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `homeassistant_api` | bool | `false` | 通过位于 `http://supervisor/core/api` 的代理访问 Home Assistant Core API。通过代理，您的应用程序充当 Home Assistant 的管理员。参考 [Home Assistant Core](/apps/guides/communication#home-assistant-core)。 |
| `hassio_api` | bool | `false` | 超出基础功能访问 Supervisor API，受 `hassio_role` 限制。 |
| `hassio_role` | string | `default` | 应用在 Supervisor API 中的角色：`default`、`homeassistant`、`backup`、`manager` 或 `admin`。参考 [API 角色](/apps/guides/security#api-roles)。 |
| `auth_api` | bool | `false` | 访问身份验证 API，以检查用户名称和密码是否在 Home Assistant 中。 |
| `docker_api` | bool | `false` | 挂载 Docker 套接字，只读。仅在关闭保护模式时有效。 |

更多信息请参见 [与 Home Assistant 和 Supervisor 交流](/apps/guides/communication)。

## 服务与发现 {#services-and-discovery}

| 关键 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `services` | 列表 | | 应用提供或使用的服务，如 `service:role`。这些服务是 `mqtt` 和 `mysql`，角色是 `provide`、`want` 和 `need`。 |
| `discovery` | 列表 | | 应用可以按域发送发现消息的集成，例如 `adguard`。 |

参见 [共享服务和发现集成](/apps/guides/services-discovery)。

## 备份 {#backups}

| 键 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `backup` | 字符串 | `hot` | `hot` 会在应用运行时进行备份。`cold` 会在备份期间停止应用。 |
| `backup_pre` | 字符串 | | 在热备份前在容器中运行的命令。 |
| `backup_post` | 字符串 | | 在热备份后在容器中运行的命令。 |
| `backup_exclude` | 列表 | | 在备份中排除的文件的通配符模式，例如 `*.log` 或 `cache/*`。 |

使用 `backup: cold` 时，`backup_pre` 和 `backup_post` 会被忽略。

## 已弃用的键 {#deprecated-keys}

Supervisor 仍然会读取一些旧键并将其转换或忽略，同时会发出警告：

- `advanced` 被忽略。
- `codenotary` 被忽略。
- `snapshot`、`snapshot_pre`、`snapshot_post` 和 `snapshot_exclude` 被读取为它们的 `backup` 对应项。
- `auto_uart` 被读取为 `uart`。
- `startup: before` 和 `startup: after` 被读取为 `services` 和 `application`。
- 旧 `host:container:permissions` 格式中的 `devices` 条目被简化为主机路径。

一个单独的 `build.yaml`（或 `build.json`）也已弃用。请参见 [构建容器镜像](/apps/guides/dockerfile#buildyaml)。
