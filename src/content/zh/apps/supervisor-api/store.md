---
title: 存储端点
description: Supervisor 应用商店的 API 接口，用于浏览、安装和更新应用，以及管理应用仓库。
sidebarLabel: 商店
order: 2
---

# 存储端点 {#store-endpoints}

商店包含 Supervisor 知道的所有应用程序，无论是否已安装，来自所有已添加的仓库。`<app>` 是应用程序的别名，包括仓库前缀，例如 `core_mosquitto` 或 `a0d7b954_vscode`。| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/store` | 商店中的应用和仓库 |
| `POST` | `/store/reload` | 重新读取所有仓库 |
| `GET` | `/store/addons` | 列出商店中的应用 |
| `GET` | `/store/addons/<app>` | 应用详情 |
| `GET` | `/store/addons/<app>/<version>` | 应用详情 |
| `GET` | `/store/addons/<app>/availability` | 检查应用是否可以安装 |
| `POST` | `/store/addons/<app>/install` | 安装应用 |
| `POST` | `/store/addons/<app>/update` | 更新应用 |
| `GET` | `/store/addons/<app>/icon` | 应用图标 |
| `GET` | `/store/addons/<app>/logo` | 应用标志 |
| `GET` | `/store/addons/<app>/changelog` | 应用更新日志 |
| `GET` | `/store/addons/<app>/documentation` | 应用文档 |
| `GET` | `/store/repositories` | 列出仓库 |
| `POST` | `/store/repositories` | 添加仓库 |
| `GET` | `/store/repositories/<repository>` | 仓库详情 |
| `DELETE` | `/store/repositories/<repository>` | 移除仓库 |
| `POST` | `/store/repositories/<repository>/repair` | 重置损坏的仓库 |

## 商店 {#store}

### `GET /store` {#get-store}

返回商店中的所有应用和所有仓库。

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `addons` | 列表 | [商店应用模型](/apps/supervisor-api/models#store-app) 的列表 |
| `repositories` | 列表 | [仓库模型](/apps/supervisor-api/models#repository) 的列表 |

### `POST /store/reload` {#post-storereload}

重新读取所有仓库：拉取 Git 仓库的最新更改并读取本地应用文件夹。在更改本地应用的文件后使用它。

## 商店中的应用 {#apps-in-the-store}

### `GET /store/addons` {#get-storeaddons}

返回商店中的应用。

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `addons` | 列表 | [商店应用模型](/apps/supervisor-api/models#store-app) 的列表 |

```json
{
  "addons": [
    {
      "advanced": false,
      "arch": ["aarch64", "amd64"],
      "available": true,
      "build": false,
      "description": "An Open Source MQTT broker",
      "documentation": true,
      "homeassistant": null,
      "icon": true,
      "installed": true,
      "logo": true,
      "name": "Mosquitto broker",
      "repository": "core",
      "slug": "core_mosquitto",
      "stage": "stable",
      "update_available": false,
      "url": null,
      "version_latest": "6.5.1",
      "version": "6.5.1"
    }
  ]
}
```

### `GET /store/addons/<app>` {#get-storeaddons-1}

返回商店中应用的详细信息。`/store/addons/<app>/<version>` 路径返回相同内容：它会忽略版本。

[商店应用模型](/apps/supervisor-api/models#store-app) 的所有键，外加：| 键 | 类型 | 描述 |
| --- | --- | --- |
| `apparmor` | 字符串 | `disable`、`default` 或 `profile` |
| `auth_api` | 布尔值 | 可以检查用户凭证 |
| `detached` | 布尔值 | `true` 如果应用不再在任何存储库中 |
| `docker_api` | 布尔值 | 可以访问 Docker API |
| `full_access` | 布尔值 | 拥有完整硬件访问权限 |
| `hassio_api` | 布尔值 | 可以访问 Supervisor API |
| `hassio_role` | 字符串 | Supervisor API 角色 |
| `homeassistant_api` | 布尔值 | 可以访问 Home Assistant Core API 代理 |
| `host_network` | 布尔值 | 使用主机网络 |
| `host_pid` | 布尔值 | 使用主机 PID 命名空间 |
| `ingress` | 布尔值 | 使用入口 |
| `long_description` | 字符串或空 | `README.md` 的内容 |
| `rating` | 整数 | 安全评级，范围从 1 到 8。数值越高越安全 |
| `signed` | 布尔值 | 总是 `false` |

### `GET /store/addons/<app>/availability` {#get-storeaddonsavailability}

检查最新版本的应用程序是否可以安装在此系统上。如果可以安装，则返回成功。如果不能安装，则返回错误及原因，例如不支持的架构或机器，或者Home Assistant版本过旧。

### `POST /store/addons/<app>/install` {#post-storeaddonsinstall}

安装应用程序的最新版本。`POST /store/addons/<app>/install/<version>`的作用相同：它会忽略版本。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `background` | 布尔型 | 否 | 立即返回`job_id`而不是等待安装完成。默认`false` |

使用`background: true`时，响应如下：

```json
{
  "job_id": "e2b7a9c4f1d34e5a8b6c0d1e2f3a4b5c"
}
```

### `POST /store/addons/<app>/update` {#post-storeaddonsupdate}

将已安装的应用更新到最新版本。`POST /store/addons/<app>/update/<version>` 也执行相同操作：它会忽略版本。应用无法自我更新。在 Supervisor 仍在启动或恢复备份时会失败。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `backup` | 布尔值 | 否 | 在更新前备份应用。默认 `false` |
| `background` | 布尔值 | 否 | 立即返回 `job_id`，而不是等待更新完成。默认 `false` |

### `GET /store/addons/<app>/icon` {#get-storeaddonsicon}

以 PNG 图像的形式返回应用程序的 `icon.png`。

### `GET /store/addons/<app>/logo` {#get-storeaddonslogo}

以 PNG 图像的形式返回应用程序的 `logo.png`。

### `GET /store/addons/<app>/changelog` {#get-storeaddonschangelog}

以纯文本形式返回应用程序的 `CHANGELOG.md`。如果没有，则响应为一条简短的纯文本消息说明情况。

### `GET /store/addons/<app>/documentation` {#get-storeaddonsdocumentation}

以纯文本形式返回应用程序的 `DOCS.md`。如果没有，则响应为一条简短的纯文本消息说明情况。

## 仓库 {#repositories}

### `GET /store/repositories` {#get-storerepositories}

返回所有仓库的列表，格式为 [仓库模型](/apps/supervisor-api/models#repository)。

```json
[
  {
    "slug": "1a2b3c4d",
    "name": "Example repository",
    "source": "https://github.com/example/apps",
    "url": "https://github.com/example/apps",
    "maintainer": "Jane Doe <jane@example.com>"
  }
]
```

### `POST /store/repositories` {#post-storerepositories}

向商店添加一个仓库。Supervisor 克隆它并读取其应用程序。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `repository` | 字符串 | 是 | 仓库的 Git URL。添加 `#branch` 以使用非默认分支 |

```json
{
  "repository": "https://github.com/home-assistant/apps-example"
}
```

### `GET /store/repositories/<repository>` {#get-storerepositories-1}

返回一个 [仓库模型](/apps/supervisor-api/models#repository)。`<repository>` 是仓库的 slug。

### `DELETE /store/repositories/<repository>` {#delete-storerepositories}

从存储中移除一个仓库。如果是内置仓库，或者仓库中的应用程序仍然安装，则操作会失败。

### `POST /store/repositories/<repository>/repair` {#post-storerepositoriesrepair}

丢弃本地的仓库副本并重新克隆它。当仓库损坏或显示过时信息时使用此操作。
