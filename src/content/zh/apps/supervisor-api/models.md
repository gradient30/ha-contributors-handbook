---
title: Supervisor API 模型
description: 几个 Supervisor API 端点返回的对象，如应用程序、备份、作业、网络接口和挂载点。
sidebarLabel: 模型
order: 9
---

# Supervisor API 模型 {#supervisor-api-models}

这些是来自多个端点的对象。端点页面链接到这里。

## 应用 {#app}

已安装的应用，如 [`GET /addons`](/apps/supervisor-api/apps#get-addons) 所列。[`GET /addons/<app>/info`](/apps/supervisor-api/apps#get-addonsappinfo) 返回更多。| 键 | 类型 | 描述 |
| --- | --- | --- |
| `name` | 字符串 | 应用名称 |
| `slug` | 字符串 | 应用别名 |
| `description` | 字符串 | 简短描述 |
| `advanced` | 布尔值 | 已弃用，总是 `false` |
| `stage` | 字符串 | `stable`、`experimental` 或 `deprecated` |
| `version` | 字符串 | 已安装版本 |
| `version_latest` | 字符串 | 最新可用版本 |
| `update_available` | 布尔值 | 如果有更新则为 `true` |
| `available` | 布尔值 | 如果应用可以在此系统上运行则为 `true` |
| `detached` | 布尔值 | 如果应用不再存在于任何仓库则为 `true` |
| `homeassistant` | 字符串或空值 | 最低 Home Assistant 版本 |
| `state` | 字符串 | `startup`、`started`、`stopped`、`unknown` 或 `error` |
| `repository` | 字符串 | 仓库别名 |
| `build` | 布尔值 | 如果应用是本地构建则为 `true` |
| `url` | 字符串或空值 | 应用网站 || `icon` | 布尔值 | `true` 如果应用程序有图标 |
| `logo` | 布尔值 | `true` 如果应用程序有徽标 |
| `system_managed` | 布尔值 | `true` 如果 Home Assistant 管理该应用程序 |

## 商店应用 {#store-app}

商店中的应用，无论是否已安装，均如 [`GET /store/addons`](/apps/supervisor-api/store#get-storeaddons) 所列。| 键 | 类型 | 描述 |
| --- | --- | --- |
| `name` | 字符串 | 应用名称 |
| `slug` | 字符串 | 应用别名 |
| `description` | 字符串 | 简短描述 |
| `advanced` | 布尔值 | 已弃用，总是 `false` |
| `arch` | 列表 | 支持的架构 |
| `available` | 布尔值 | `true` 如果应用可以安装在此系统上 |
| `build` | 布尔值 | `true` 如果应用是本地构建 |
| `documentation` | 布尔值 | `true` 如果应用有文档 |
| `homeassistant` | 字符串或空值 | 最低 Home Assistant 版本 |
| `icon` | 布尔值 | `true` 如果应用有图标 |
| `logo` | 布尔值 | `true` 如果应用有标志 |
| `installed` | 布尔值 | `true` 如果应用已安装 |
| `repository` | 字符串 | 仓库别名 |
| `stage` | 字符串 | `stable`, `experimental`, 或 `deprecated` |
| `update_available` | 布尔值 | `true` 如果有可用更新 || `url` | 字符串或空 | 应用程序的网站 |
| `version` | 字符串或空 | 已安装的版本，`null` 如果未安装 |
| `version_latest` | 字符串 | 最新可用版本 |

## 仓库 {#repository}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `slug` | 字符串 | 仓库的别名 |
| `name` | 字符串 | 仓库的名称 |
| `source` | 字符串 | Git URL，或者内置仓库的 `local` 和 `core` |
| `url` | 字符串 | 仓库的网站。当仓库未设置时，与 `source` 相同 |
| `maintainer` | 字符串 | 仓库的维护者 |

## 备份 {#backup}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `slug` | 字符串 | 备份的ID |
| `name` | 字符串 | 备份的名称 |
| `date` | 字符串 | 备份创建时间，ISO 8601格式 |
| `type` | 字符串 | `full` 或 `partial` |
| `size` | 浮点数 | 大小，单位MB |
| `size_bytes` | 整数 | 大小，单位字节 |
| `location` | 字符串或空 | 主要位置。`null` 是本地备份文件夹 |
| `locations` | 列表 | 备份存储的所有位置 |
| `protected` | 布尔值 | 如果备份有密码，则为 `true` |
| `location_attributes` | 字典 | 每个位置的 `protected` 和 `size_bytes`。本地文件夹是 `.local` |
| `compressed` | 布尔值 | 如果备份被压缩，则为 `true` |
| `content` | 字典 | 备份内容：`homeassistant`（布尔值）、`addons`（slug列表）和 `folders`（列表） |

## 统计数据 {#stats}

容器的资源使用情况。

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `cpu_percent` | 浮点数或空 | CPU 使用率百分比，`null` 用于一次性采样 |
| `cpu_usage` | 整数 | 容器的总 CPU 时间 |
| `cpu_system_usage` | 整数 | 系统的总 CPU 时间 |
| `online_cpus` | 整数 | CPU 数量 |
| `memory_usage` | 整数 | 内存使用量（字节） |
| `memory_limit` | 整数 | 内存限制（字节） |
| `memory_percent` | 浮点数 | 内存使用占限制的百分比 |
| `network_rx` | 整数 | 接收的字节数 |
| `network_tx` | 整数 | 发送的字节数 |
| `blk_read` | 整数 | 从磁盘读取的字节数 |
| `blk_write` | 整数 | 写入磁盘的字节数 |

## 服务 {#service}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `slug` | 字符串 | 服务的名称，例如 `mqtt` |
| `available` | 布尔值 | 如果一个应用提供该服务则为 `true` |
| `providers` | 列表 | 可以提供该服务的应用的标识符 |

## 发现 {#discovery}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `addon` | 字符串 | 发送消息的应用程序的简写 |
| `service` | 字符串 | 集成的域 |
| `uuid` | 字符串 | 消息的ID |
| `config` | 字典 | 集成连接所需的信息 |

## 面板 {#panel}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `title` | 字符串 | 侧边栏中的标题 |
| `icon` | 字符串 | 侧边栏中的图标 |
| `admin` | 布尔值 | 如果只有管理员能看到面板，则 `true` |
| `enable` | 布尔值 | 如果面板显示在侧边栏，则 `true` |

## 用户 {#user}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `username` | 字符串 | 用于登录的用户名 |
| `name` | 字符串 | 显示名称 |
| `is_owner` | 布尔值 | `true` 是否为用户所有者 |
| `is_active` | 布尔值 | `true` 用户是否可以登录 |
| `local_only` | 布尔值 | `true` 用户是否只能从本地网络登录 |
| `group_ids` | 列表 | 用户所属的组，如 `system-admin` |

## 任务 {#job}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `name` | 字符串 | 任务的名称 |
| `reference` | 字符串或空值 | 任务操作的对象，如应用标识或备份ID |
| `uuid` | 字符串 | 任务的ID |
| `progress` | 浮点数 | 任务能够报告时的进度，从0到100 |
| `stage` | 字符串或空值 | 任务所在的阶段 |
| `done` | 布尔值或空值 | 任务完成时`true`，任务未开始时`null` |
| `created` | 字符串 | 任务创建时间，ISO 8601格式 |
| `errors` | 列表 | [任务错误](/apps/supervisor-api/models#job-error) |
| `extra` | 字典或空值 | 关于任务或其阶段的附加信息 |
| `child_jobs` | 列表 | 此任务启动的任务 |

### 作业错误 {#job-error}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `type` | 字符串 | 错误类型 |
| `message` | 字符串 | 出了什么问题 |
| `stage` | 字符串或空 | 作业所在的阶段 |
| `error_key` | 字符串或空 | 错误的稳定键 |
| `extra_fields` | 字典或空 | 与 `error_key` 相关的值 |

## 问题 {#issue}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `uuid` | 字符串 | 问题的ID |
| `type` | 字符串 | 问题的类型 |
| `context` | 字符串 | 问题所在的位置，例如 `addon`、`core` 或 `system` |
| `reference` | 字符串或空值 | 相关内容，例如一个应用slug |
| `reference_extra` | 字典或空值 | 额外详情，例如冲突的端口 |

## 建议 {#suggestion}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `uuid` | 字符串 | 建议的ID |
| `type` | 字符串 | 修复的类型 |
| `context` | 字符串 | 修复适用的位置 |
| `reference` | 字符串或空值 | 相关内容，例如一个应用slug |
| `reference_extra` | 字典或空值 | 额外详情 |
| `auto` | 布尔值 | 如果 Supervisor 自行应用修复，则为 `true` |

## 检查 {#check}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `slug` | 字符串 | 检查的标识符 |
| `enabled` | 布尔值 | `true` 如果检查运行

## 主机服务 {#host-service}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `name` | 字符串 | systemd 单元的名称 |
| `description` | 字符串 | 单元的描述 |
| `state` | 字符串 | 单元的状态，例如 `active` |

## 网络接口 {#network-interface}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `interface` | 字符串 | 接口名称，例如 `eth0` |
| `type` | 字符串 | `ethernet`、`wireless` 或 `vlan` |
| `enabled` | 布尔值 | 如果接口开启则为 `true` |
| `connected` | 布尔值 | 如果接口已连接则为 `true` |
| `primary` | 布尔值 | 如果这是主接口则为 `true` |
| `mac` | 字符串 | MAC 地址 |
| `ipv4` | 字典或空值 | [IP 配置](/apps/supervisor-api/models#ip-configuration) |
| `ipv6` | 字典或空值 | [IP 配置](/apps/supervisor-api/models#ip-configuration) |
| `wifi` | 字典或空值 | [Wi-Fi 配置](/apps/supervisor-api/models#wi-fi-configuration) |
| `vlan` | 字典或空值 | [VLAN 配置](/apps/supervisor-api/models#vlan-configuration) |
| `mdns` | 字符串 | `default`、`off`、`resolve` 或 `announce` |
| `llmnr` | 字符串 | `default`、`off`、`resolve` 或 `announce` |

### IP 配置 {#ip-configuration}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `method` | 字符串 | `auto`, `static` 或 `disabled` |
| `address` | 列表 | 带前缀的地址 |
| `gateway` | 字符串或空 | 网关 |
| `nameservers` | 列表 | DNS 服务器 |
| `route_metric` | 整数或空 | 路由度量值，值越低优先级越高 |
| `ready` | 布尔值 | 如果配置已激活，则为 `true` |
| `addr_gen_mode` | 字符串 | 仅限 IPv6: `eui64`, `stable-privacy`, `default-or-eui64` 或 `default` |
| `ip6_privacy` | 字符串 | 仅限 IPv6: `disabled`, `enabled-prefer-public`, `enabled` 或 `default` |

### Wi-Fi 配置 {#wi-fi-configuration}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `mode` | 字符串 | `infrastructure`, `mesh`, `adhoc` 或 `ap` |
| `auth` | 字符串 | `open`, `wep`, `wpa-psk` 或 `unsupported` |
| `ssid` | 字符串 | 网络名称 |
| `signal` | 整数或空 | 信号强度（百分比） |

### VLAN 配置 {#vlan-configuration}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `id` | 整数 | VLAN ID |
| `parent` | 字符串 | VLAN 运行的接口 |

## 接入点 {#access-point}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `mode` | 字符串 | `infrastructure`、`mesh` 或 `adhoc` |
| `ssid` | 字符串 | 网络名称 |
| `frequency` | 整数 | 频率（MHz） |
| `signal` | 整数 | 信号强度（百分比） |
| `mac` | 字符串 | 接入点的 MAC 地址 |

## 挂载 {#mount}

相同的对象进入 `POST /mounts` 并从 `GET /mounts` 返回。有些钥匙只能单向使用。| 键 | 类型 | 方向 | 描述 |
| --- | --- | --- | --- |
| `name` | 字符串 | 双向 | 挂载点名称：字母、数字和下划线 |
| `type` | 字符串 | 双向 | `cifs`、`nfs` 或 `disk` |
| `usage` | 字符串 | 双向 | `backup`、`media` 或 `share` |
| `read_only` | 布尔值 | 双向 | 挂载只读。不允许用于备份挂载。默认 `false` |
| `server` | 字符串 | 双向 | CIFS 和 NFS：服务器的主机名或 IP 地址 |
| `port` | 整数 | 双向 | CIFS 和 NFS：端口，如果不是默认端口 |
| `share` | 字符串 | 双向 | CIFS：共享名称 |
| `version` | 字符串或空值 | 双向 | CIFS：`1.0` 或 `2.0` 强制使用旧协议版本 |
| `username` | 字符串 | 请求 | CIFS：用户名。与 `password` 一起发送，或者两者都不填 |
| `password` | 字符串 | 请求 | CIFS：密码 || `path` | 字符串 | 两者 | NFS：服务器上的路径 |
| `uuid` | 字符串 | 两者 | 磁盘：分区的 UUID，来自 [`GET /host/disks`](/apps/supervisor-api/host#get-hostdisks) |
| `device` | 字符串 | 请求 | 磁盘：分区的设备路径。发送 `uuid`、`device` 或两者 |
| `filesystem` | 字符串 | 响应 | 磁盘：分区的文件系统 |
| `state` | 字符串或 null | 响应 | 挂载状态，如 `active` 或 `failed` |
| `user_path` | 字符串或 null | 响应 | 应用程序找到挂载的位置，如 `/media/nas` |

## 启动槽 {#boot-slot}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `state` | 字符串 | 插槽的状态，由 RAUC 报告，例如 `booted`、`active` 或 `inactive` |
| `status` | 字符串或空值 | 来自此插槽的上一次启动结果：`good` 或 `bad` |
| `version` | 字符串或空值 | 此插槽中的操作系统版本 |

## 磁盘 {#disk}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `name` | 字符串 | 磁盘名称 |
| `vendor` | 字符串 | 厂商 |
| `model` | 字符串 | 型号 |
| `serial` | 字符串 | 序列号 |
| `size` | 整数 | 大小（字节） |
| `id` | 字符串 | 磁盘 ID：UDisks2 驱动 ID，或在没有时使用设备路径 |
| `dev_path` | 字符串 | 设备路径 |

## 设备 {#device}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `name` | 字符串 | 设备名称 |
| `sysfs` | 字符串 | sysfs 中的路径 |
| `dev_path` | 字符串 | `/dev` 中的路径 |
| `subsystem` | 字符串或空 | 子系统，如 `tty`、`input` 或 `sound` |
| `by_id` | 字符串或空 | `/dev/serial/by-id` 风格的链接 |
| `attributes` | 字典 | udev 属性 |
| `children` | 列表 | sysfs 中子设备的路径 |

## 驱动器 {#drive}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `vendor` | 字符串 | 供应商 |
| `model` | 字符串 | 型号 |
| `revision` | 字符串 | 固件版本 |
| `serial` | 字符串 | 序列号 |
| `id` | 字符串 | 驱动器ID |
| `size` | 整数 | 大小（字节） |
| `time_detected` | 字符串 | 驱动器发现时间，ISO 8601格式 |
| `connection_bus` | 字符串 | 总线，如 `usb` |
| `seat` | 字符串 | 驱动器所属插槽 |
| `removable` | 布尔值 | `true` 用户是否可以移除驱动器 |
| `ejectable` | 布尔值 | `true` 系统是否可以弹出驱动器 |
| `filesystems` | 列表 | 驱动器上的[文件系统](/apps/supervisor-api/models#filesystem) |

### 文件系统 {#filesystem}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `device` | 字符串 | 设备文件，如 `/dev/sda1` |
| `id` | 字符串 | 文件系统的 ID |
| `size` | 整数 | 以字节为单位的大小 |
| `name` | 字符串 | 文件系统的标签 |
| `system` | 布尔值 | 如果是系统文件系统则为 `true` |
| `mount_points` | 列表 | 文件系统的挂载位置 |

## 音频 {#audio}

[`GET /audio/info`](/apps/supervisor-api/plugins#get-audioinfo) 的 `audio` 对象。

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `card` | 列表 | [声卡](/apps/supervisor-api/models#sound-card) |
| `input` | 列表 | 用于输入的 [音频设备](/apps/supervisor-api/models#audio-device) |
| `output` | 列表 | 用于输出的 [音频设备](/apps/supervisor-api/models#audio-device) |
| `application` | 列表 | [应用程序流](/apps/supervisor-api/models#application-stream) |

### 声卡 {#sound-card}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `name` | 字符串 | 声卡名称 |
| `index` | 整数 | 声卡的 PulseAudio 索引 |
| `driver` | 字符串 | 声卡驱动 |
| `profiles` | 列表 | 配置文件，每个包含 `name`、`description` 和 `active` |

### 音频设备 {#audio-device}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `name` | 字符串 | 设备名称 |
| `index` | 整数 | 设备的 PulseAudio 索引 |
| `description` | 字符串 | 描述 |
| `volume` | 浮点数 | 音量，从 0 到 1 |
| `mute` | 布尔值 | 如果静音则为 `true` |
| `default` | 布尔值 | 如果为默认设备则为 `true` |
| `card` | 整数 或 空值 | 声卡索引 |
| `applications` | 列表 | 此设备上的 [应用程序流](/apps/supervisor-api/models#application-stream) |

### 应用流 {#application-stream}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `name` | 字符串 | 应用名称 |
| `index` | 整数 | 流的 PulseAudio 索引 |
| `stream_index` | 字符串 | 流播放的设备索引 |
| `stream_type` | 字符串 | `input` 或 `output` |
| `volume` | 浮点数 | 音量，从 0 到 1 |
| `mute` | 布尔值 | 如果静音则为 `true` |
| `app` | 字符串 | 流所属应用的标识符 |
