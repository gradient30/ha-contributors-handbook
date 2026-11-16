---
title: 应用端点
description: Supervisor 已安装应用的 API 端点、它们的选项、状态及日志。
sidebarLabel: 应用
order: 1
---

# 应用端点 {#apps-endpoints}

这些端点适用于已安装的应用程序。要浏览和安装应用，请使用 [store endpoints](/apps/supervisor-api/store)。

`<app>` 是已安装应用的标识符，例如 `core_mosquitto` 或 `local_hello_world`。您的应用程序始终可以使用 `self` 来指代自身。调用 `/addons/self/...` 不需要额外权限，详见 [您的应用可以调用的内容](/apps/supervisor-api#what-your-app-may-call)。| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/addons` | 列出已安装的应用 |
| `POST` | `/addons/reload` | 重新加载应用商店 |
| `GET` | `/addons/<app>/info` | 应用详情 |
| `POST` | `/addons/<app>/options` | 更改应用选项 |
| `POST` | `/addons/<app>/options/validate` | 验证选项 |
| `GET` | `/addons/<app>/options/config` | 读取您自己的已验证选项 |
| `POST` | `/addons/<app>/sys_options` | 将应用标记为由 Home Assistant 管理 |
| `POST` | `/addons/<app>/security` | 打开或关闭保护模式 |
| `POST` | `/addons/<app>/start` | 启动应用 |
| `POST` | `/addons/<app>/stop` | 停止应用 |
| `POST` | `/addons/<app>/restart` | 重启应用 |
| `POST` | `/addons/<app>/rebuild` | 重建本地构建的应用 |
| `POST` | `/addons/<app>/uninstall` | 卸载应用 |
| `POST` | `/addons/<app>/stdin` | 写入应用的标准输入 |
| `GET` | `/addons/<app>/stats` | 应用的资源使用情况 |
| `GET` | `/addons/<app>/logs` | 应用日志，以及其他 [日志端点](/apps/supervisor-api#log-endpoints) || `POST` | `/addons/<app>/install` | [商店安装](/apps/supervisor-api/store#post-storeaddonsappinstall) 的旧路径 |
| `POST` | `/addons/<app>/update` | [商店更新](/apps/supervisor-api/store#post-storeaddonsappupdate) 的旧路径 |
| `GET` | `/addons/<app>/icon` | [商店图标](/apps/supervisor-api/store#get-storeaddonsappicon) 的旧路径 |
| `GET` | `/addons/<app>/logo` | [商店标志](/apps/supervisor-api/store#get-storeaddonsapplogo) 的旧路径 |
| `GET` | `/addons/<app>/changelog` | [商店更新日志](/apps/supervisor-api/store#get-storeaddonsappchangelog) 的旧路径 |
| `GET` | `/addons/<app>/documentation` | [商店文档](/apps/supervisor-api/store#get-storeaddonsappdocumentation) 的旧路径 |

## 列表与重新加载 {#list-and-reload}

### `GET /addons` {#get-addons}

返回已安装的应用程序。

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `addons` | 列表 | 一个 [应用模型](/apps/supervisor-api/models#app) 列表 |

```json
{
  "addons": [
    {
      "name": "Hello world",
      "slug": "local_hello_world",
      "description": "My first real app!",
      "advanced": false,
      "stage": "stable",
      "version": "1.1.0",
      "version_latest": "1.1.0",
      "update_available": false,
      "available": true,
      "detached": false,
      "homeassistant": null,
      "state": "started",
      "repository": "local",
      "build": true,
      "url": null,
      "icon": false,
      "logo": false,
      "system_managed": false
    }
  ]
}
```

### `POST /addons/reload` {#post-addonsreload}

重新加载应用商店：重新读取所有仓库并查找新版本。效果与 [`POST /store/reload`](/apps/supervisor-api/store#post-storereload) 相同。

## 信息和选项 {#information-and-options}

### `GET /addons/<app>/info` {#get-addonsinfo}

返回应用的详细信息。当应用未安装时，会回退到应用的商店信息，同时 `state` 设置为 `unknown` 并使用默认选项。| 键 | 类型 | 描述 |
| --- | --- | --- |
| `name` | 字符串 | 应用名称 |
| `slug` | 字符串 | 应用的标识，包括存储库前缀 |
| `hostname` | 字符串 | 应用在内部网络上的主机名 |
| `dns` | 列表 | 应用的 DNS 名称 |
| `description` | 字符串 | 简短描述 |
| `long_description` | 字符串或空值 | `README.md` 的内容 |
| `advanced` | 布尔值 | 已弃用，总是 `false` |
| `stage` | 字符串 | `stable`、`experimental` 或 `deprecated` |
| `repository` | 字符串 | 应用来源的存储库标识 |
| `version` | 字符串 | 已安装版本 |
| `version_latest` | 字符串 | 可用的最新版本 |
| `update_available` | 布尔值 | 如果有更新，`true` |
| `protected` | 布尔值 | 如果保护模式开启，`true` |
| `rating` | 整数 | 安全评级，从 1 到 8 || `boot_config` | 字符串 | 来自应用配置的启动模式：`auto`、`manual` 或 `manual_only` |
| `boot` | 字符串 | 用户设置的启动模式：`auto` 或 `manual` |
| `options` | 字典 | 应用的选项。当其他应用请求时为空，除非该应用具有 `manager` 或 `admin` 角色。选项可以包含密码 |
| `schema` | 列表或空 | 选项模式，为 UI 中的选项表单准备 |
| `arch` | 列表 | 支持的架构 |
| `machine` | 列表 | 支持的机器类型 |
| `homeassistant` | 字符串或空 | 最低 Home Assistant 版本 |
| `url` | 字符串或空 | 应用的网站 |
| `detached` | 布尔值 | 如果应用不再存在于任何存储库中，则为 `true` |
| `available` | 布尔值 | 如果应用可以在此系统上运行，则为 `true` |
| `build` | 布尔值 | 如果应用是本地构建的，则为 `true` || `network` | 字典或空值 | 端口映射，容器端口到主机端口 |
| `network_description` | 字典或空值 | 每个端口的描述 |
| `host_network` | 布尔值 | 使用主机网络 |
| `host_pid` | 布尔值 | 使用主机 PID 命名空间 |
| `host_ipc` | 布尔值 | 使用主机 IPC 命名空间 |
| `host_uts` | 布尔值 | 使用主机 UTS 命名空间 |
| `host_dbus` | 布尔值 | 具有访问主机 D-Bus 的权限 |
| `privileged` | 列表 | 额外的 Linux 功能 |
| `full_access` | 布尔值 | 拥有完整硬件访问权限 |
| `apparmor` | 字符串 | `disable`、`default` 或 `profile` |
| `icon` | 布尔值 | 拥有图标 |
| `logo` | 布尔值 | 拥有标志 |
| `changelog` | 布尔值 | 拥有更新日志 |
| `documentation` | 布尔值 | 拥有文档 |
| `stdin` | 布尔值 | 接受标准输入 |
| `hassio_api` | 布尔值 | 具有访问 Supervisor API 的权限 || `hassio_role` | 字符串 | Supervisor API 角色 |
| `auth_api` | 布尔值 | 可以检查用户凭证 |
| `homeassistant_api` | 布尔值 | 可以访问 Home Assistant Core API 代理 |
| `gpio` | 布尔值 | 可以访问 GPIO |
| `usb` | 布尔值 | 可以访问 USB |
| `uart` | 布尔值 | 可以访问串行设备 |
| `kernel_modules` | 布尔值 | 可以访问内核模块 |
| `devicetree` | 布尔值 | 可以访问设备树 |
| `udev` | 布尔值 | 可以访问 udev 数据库 |
| `docker_api` | 布尔值 | 可以访问 Docker API |
| `video` | 布尔值 | 可以访问视频设备 |
| `audio` | 布尔值 | 使用音频系统 |
| `startup` | 字符串 | `initialize`、`system`、`services`、`application` 或 `once` |
| `services` | 列表 | 应用提供或使用的服务，如 `mqtt:provide` |
| `discovery` | 列表 | 应用可以发送发现消息的集成 || `translations` | 字典 | 应用程序的翻译文件，按语言分类 |
| `ingress` | 布尔值 | 是否使用入口 |
| `ingress_entry` | 字符串或空值 | 应用程序的入口路径 |
| `ingress_url` | 字符串或空值 | 完整入口 URL，包括入口点 |
| `ingress_port` | 整数或空值 | 应用程序监听入口的端口 |
| `ingress_panel` | 布尔值或空值 | `true` 如果应用程序显示在侧边栏中 |
| `signed` | 布尔值 | 始终 `false`，不检查镜像签名 |
| `state` | 字符串 | `startup`、`started`、`stopped`、`unknown` 或 `error` |
| `webui` | 字符串或空值 | Web界面的URL，带占位符 |
| `audio_input` | 字符串或空值 | 选定的音频输入设备 |
| `audio_output` | 字符串或空值 | 选定的音频输出设备 |
| `auto_update` | 布尔值 | `true` 如果应用程序自动更新 || `ip_address` | 字符串 | 内部网络的 IP 地址 |
| `watchdog` | 布尔值 | 如果看门狗开启则为 `true` |
| `devices` | 列表 | 映射到应用程序的设备路径 |
| `system_managed` | 布尔值 | 如果 Home Assistant 管理该应用程序则为 `true` |
| `system_managed_config_entry` | 字符串或 null | 管理该应用程序的配置条目的 ID |

### `POST /addons/<app>/options` {#post-addonsoptions}

更改应用程序的设置。只发送您想更改的键。要将 `network`、`audio_input`、`audio_output` 或 `options` 重置为默认值，请发送 `null`。

| 键 | 类型 | 必需 | 描述 |
| --- | --- | --- | --- |
| `boot` | 字符串 | 否 | `auto` 或 `manual`。当应用程序使用 `manual_only` 时会失败 |
| `auto_update` | 布尔值 | 否 | 自动更新应用程序 |
| `network` | 字典或 null | 否 | 端口映射，如 `"8000/tcp": 8000`。`null` 端口会禁用该映射 |
| `options` | 字典或 null | 否 | 应用程序选项，根据应用程序的 schema 验证 |
| `audio_input` | 字符串或 null | 否 | 音频输入设备 |
| `audio_output` | 字符串或 null | 否 | 音频输出设备 |
| `ingress_panel` | 布尔值 | 否 | 在侧边栏显示应用程序 |
| `watchdog` | 布尔值 | 否 | 打开或关闭 watchdog |选项可以使用`!secret name`引用Home Assistant的`secrets.yaml`中的条目。Supervisor存储该引用并为应用程序提供解析后的值。

```json
{
  "boot": "manual",
  "options": {
    "name": "world",
    "beer": true
  },
  "watchdog": true
}
```

对`options`的更改将在应用程序下次启动时生效。

### `POST /addons/<app>/options/validate` {#post-addonsoptionsvalidate}

根据应用程序的模式验证选项。将要检查的选项作为正文发送，或不发送任何内容以检查已存储的选项。当该检查开启时，还会检查密码是否存在已知泄露，请参见 [`/security`](/apps/supervisor-api/supervisor#security)。

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `message` | string | 出错的内容，或者为空 |
| `valid` | boolean | `true` 如果选项有效 |
| `pwned` | boolean 或 null | `true` 如果密码已知被泄露，`null` 如果检查失败 |

### `GET /addons/<app>/options/config` {#get-addonsoptionsconfig}

返回您自己应用程序的选项，已验证，填充了默认值并解析了 `!secret` 引用。仅适用于 `self`：没有应用可以读取其他应用的渲染选项。

### `POST /addons/<app>/sys_options` {#post-addonssysoptions}

将应用标记为由 Home Assistant 管理。只有 Home Assistant Core 可以调用此项。

| 键 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| `system_managed` | 布尔值 | 否 | 如果 Home Assistant 管理该应用，则为 `true` |
| `system_managed_config_entry` | 字符串或空 | 否 | 管理该应用的配置项 ID |

### `POST /addons/<app>/security` {#post-addonssecurity}

开启或关闭应用的保护模式。需要 `admin` 角色，即使应用通过 `self` 为自身调用也需要。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `protected` | 布尔值 | 否 | `true` 以开启保护模式 |

## 运行应用 {#running-the-app}

### `POST /addons/<app>/start` {#post-addonsstart}

启动应用。等待直到应用运行。若 Supervisor 仍在启动或恢复备份时会失败。

### `POST /addons/<app>/stop` {#post-addonsstop}

停止应用。

### `POST /addons/<app>/restart` {#post-addonsrestart}

重启应用。若 Supervisor 仍在启动或恢复备份时会失败。

### `POST /addons/<app>/rebuild` {#post-addonsrebuild}

重新构建本地构建应用的镜像并重启。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `force` | 布尔值 | 否 | 即使应用使用预构建镜像也重新构建。默认 `false` |

### `POST /addons/<app>/uninstall` {#post-addonsuninstall}

卸载应用程序。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `remove_config` | 布尔值 | 否 | 同时删除应用程序的公共配置文件夹（`app_config`）。默认值 `false` |

### `POST /addons/<app>/stdin` {#post-addonsstdin}

将原始请求体写入应用程序的标准输入。应用程序需要在其配置中使用 `stdin: true`。

## 使用方法和日志 {#usage-and-logs}

### `GET /addons/<app>/stats` {#get-addonsstats}

以 [stats 模型](/apps/supervisor-api/models#stats) 的形式返回应用程序的资源使用情况。添加 `one_shot` 查询参数可获取单次快速样本。在一次性采样中，`cpu_percent` 等于 `null`。

```json
{
  "cpu_percent": 14.0,
  "cpu_usage": 3412000000,
  "cpu_system_usage": 98231000000000,
  "online_cpus": 4,
  "memory_usage": 288888,
  "memory_limit": 322222,
  "memory_percent": 32.4,
  "network_tx": 110,
  "network_rx": 902,
  "blk_read": 12,
  "blk_write": 27
}
```

### `GET /addons/<app>/logs` {#get-addonslogs}

返回应用程序的日志。`follow`、`latest` 和 `boots` 变体也存在。它们的工作方式与其他 [日志端点](/apps/supervisor-api#log-endpoints) 相同。
