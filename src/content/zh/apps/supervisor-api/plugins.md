---
title: 插件端点
description: Supervisor API 端点用于运行在 Home Assistant、音频服务器、CLI、DNS、多播和观察者旁的插件。
sidebarLabel: 插件
order: 6
---

# 插件端点 {#plugin-endpoints}

插件是 Supervisor 运行以支持系统的容器：音频服务器、CLI、DNS 服务器、多播代理和观察者。每个插件都有相同的基本端点，以及一些它自己的端点。

要使用它们，你的应用需要具有 `manager` 或 `admin` 角色的 `hassio_api: true`。`/info` 端点可与任何角色一起使用。

## 共享端点 {#shared-endpoints}

每个插件都有这些端点。将 `<plugin>` 替换为 `audio`、`cli`、`dns`、`multicast` 或 `observer`。

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/<plugin>/info` | 版本信息，以及下面列出的每个插件的详细信息 |
| `GET` | `/<plugin>/stats` | 插件的资源使用情况 |
| `POST` | `/<plugin>/update` | 更新插件 |

`GET /<plugin>/info` 总是返回：

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `version` | string | 已安装版本 |
| `version_latest` | string | 可用最新版本 |
| `update_available` | boolean | 如果有更新可用，则 `true` |

`GET /<plugin>/stats` 返回一个 [统计模型](/apps/supervisor-api/models#stats)。添加 `one_shot` 查询参数以获取单个快速样本。`POST /<plugin>/update` 安装新版本。当 Supervisor 仍在启动或恢复备份时会失败。音频、DNS 和多播插件也拒绝已安装的版本。

| 键 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| `version` | 字符串 | 否 | 要安装的版本。默认是最新版本 |

音频、DNS 和多播插件也有 `POST /<plugin>/restart`，当 Supervisor 仍在启动或恢复备份时会失败，以及 `/<plugin>/logs` 下的 [日志端点](/apps/supervisor-api#log-endpoints)。

## 音频 {#audio}

音频插件运行 PulseAudio，`audio: true` 的应用程序使用它。

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/audio/info` | 音频设备和流 |
| `POST` | `/audio/reload` | 重新读取音频设备 |
| `POST` | `/audio/restart` | 重启音频服务器 |
| `POST` | `/audio/profile` | 切换声卡配置文件 |
| `POST` | `/audio/default/<source>` | 设置默认设备 |
| `POST` | `/audio/volume/<source>` | 设置设备音量 |
| `POST` | `/audio/volume/<source>/application` | 设置应用程序流音量 |
| `POST` | `/audio/mute/<source>` | 静音设备 |
| `POST` | `/audio/mute/<source>/application` | 静音应用程序流 |

`<source>` 是 `input` 或 `output`。

### `GET /audio/info` {#get-audioinfo}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `host` | 字符串 | 内部网络上音频服务器的 IP 地址 |
| `audio` | 字典 | 一个 [音频模型](/apps/supervisor-api/models#audio) |

加上 `version`、`version_latest` 和 `update_available`。

### `POST /audio/profile` {#post-audioprofile}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `card` | 字符串 | 是 | 声卡名称 |
| `name` | 字符串 | 是 | 配置文件名称 |

### `POST /audio/default/<source>` {#post-audiodefault}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | 字符串 | 是 | 设备名称 |

### `POST /audio/volume/<source>` {#post-audiovolume}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `index` | 整数 | 是 | 设备索引，或 `application` 路径的流索引 |
| `volume` | 浮点数 | 是 | 音量，从 0 到 1 |

### `POST /audio/mute/<source>` {#post-audiomute}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `index` | 整数 | 是 | 设备索引，或 `application` 路径的流索引 |
| `active` | 布尔值 | 是 | `true` 用于静音 |

## CLI {#cli}

CLI 插件运行 `ha` 命令行工具。它只有共享端点。

## DNS {#dns}

DNS 插件运行 CoreDNS。内部网络上的每个容器都使用它来解析名称，包括应用程序的名称。

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/dns/info` | DNS 设置 |
| `POST` | `/dns/options` | 更改 DNS 设置 |
| `POST` | `/dns/restart` | 重启 DNS 服务器 |
| `POST` | `/dns/reset` | 将 DNS 设置重置为默认值 |

### `GET /dns/info` {#get-dnsinfo}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `host` | 字符串 | 内部网络中 DNS 服务器的 IP 地址 |
| `servers` | 列表 | 您设置的 DNS 服务器 |
| `locals` | 列表 | 主机的 DNS 服务器 |
| `mdns` | 布尔值 | `true` 如果 mDNS 名称被解析 |
| `llmnr` | 布尔值 | `true` 如果 LLMNR 名称被解析 |
| `fallback` | 布尔值 | `true` 如果在其他 DNS 失败时使用公共 DNS 服务器 |

另外还有 `version`、`version_latest` 和 `update_available`。

### `POST /dns/options` {#post-dnsoptions}

更改会重启 DNS 服务器。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `servers` | 列表 | 否 | 最多 8 个 DNS 服务器，写作 `dns://` 带 IPv4 地址的格式，如 `dns://1.1.1.1`。不接受 IPv6 地址 |
| `fallback` | 布尔值 | 否 | 当其他 DNS 失败时使用公共 DNS 服务器 |

## 多播 {#multicast}

多播插件在主机网络和内部网络之间转发 mDNS。

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/multicast/info` | 多播信息 |
| `POST` | `/multicast/options` | 打开或关闭插件 |
| `POST` | `/multicast/restart` | 重启插件 |

`GET /multicast/info` 向共享密钥中添加 `enabled`（布尔值）。

### `POST /multicast/options` {#post-multicastoptions}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `enabled` | 布尔型 | 否 | 打开或关闭插件 |

当插件关闭时，更新端点会失败。

## 观察者 {#observer}

观察者是一个小型网页，用于显示系统状态，即使 Home Assistant 本身没有启动。它只包含共享端点。`GET /observer/info` 添加 `host`，它在内部网络上的 IP 地址。
