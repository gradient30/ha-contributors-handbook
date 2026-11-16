---
title: 备份端点
description: Supervisor API 端点用于创建、恢复、上传、下载和管理备份。
sidebarLabel: 备份
order: 3
---

# 备份端点 {#backup-endpoints}

通过这些端点，您的应用可以创建和恢复备份，就像一个将备份复制到其他位置的备份应用。您的应用需要`hassio_api: true`和`backup`角色，或者`manager`或`admin`角色。

`<backup>`是备份的标识符，一个像`a1b2c3d4`一样的简短随机ID。| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/backups` | 列出备份 |
| `GET` | `/backups/info` | 列出备份及备份设置 |
| `POST` | `/backups/options` | 更改备份设置 |
| `POST` | `/backups/reload` | 重新读取备份位置 |
| `POST` | `/backups/new/full` | 执行完整备份 |
| `POST` | `/backups/new/partial` | 执行部分备份 |
| `POST` | `/backups/new/upload` | 上传备份文件 |
| `GET` | `/backups/<backup>/info` | 备份详情 |
| `GET` | `/backups/<backup>/download` | 下载备份文件 |
| `DELETE` | `/backups/<backup>` | 删除备份 |
| `POST` | `/backups/<backup>/restore/full` | 从备份中恢复所有内容 |
| `POST` | `/backups/<backup>/restore/partial` | 恢复部分备份内容 |
| `POST` | `/backups/freeze` | 为外部备份准备系统 |
| `POST` | `/backups/thaw` | 撤销冻结 |

## 位置 {#locations}

备份可以存储在多个位置。位置可以是以下之一：

- `null` 或 `.local`：系统的本地备份文件夹
- 用于备份的 [网络挂载](/apps/supervisor-api/host#mounts) 的名称
- `.cloud_backup`：Home Assistant Link。只有 Home Assistant Core 可以使用此位置

## 文件夹 {#folders}

备份可以包含这些文件夹：`share`、`ssl`、`media` 和 `addons/local`（本地应用）。API 也接受本地应用的 `apps/local`。在请求中，文件夹 `homeassistant` 与 `homeassistant: true` 含义相同。

## 列表和设置 {#list-and-settings}

### `GET /backups` {#get-backups}

返回备份。

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `backups` | 列表 | [备份模型](/apps/supervisor-api/models#backup) 列表 |

```json
{
  "backups": [
    {
      "slug": "a1b2c3d4",
      "name": "Before the update",
      "date": "2026-10-01T09:30:00.000000+00:00",
      "type": "partial",
      "size": 0.17,
      "size_bytes": 178257,
      "location": null,
      "locations": [null],
      "protected": false,
      "location_attributes": {
        ".local": {
          "protected": false,
          "size_bytes": 178257
        }
      },
      "compressed": true,
      "content": {
        "homeassistant": false,
        "addons": ["core_mosquitto"],
        "folders": ["share"]
      }
    }
  ]
}
```

### `GET /backups/info` {#get-backupsinfo}

返回与 `GET /backups` 相同的列表，加上备份设置。

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `backups` | 列表 | [备份模型](/apps/supervisor-api/models#backup) 的列表 |
| `days_until_stale` | 整数 | 多少天后备份算作旧备份 |

### `POST /backups/options` {#post-backupsoptions}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `days_until_stale` | 整数 | 否 | 备份被认为是旧备份的天数。至少为1 |

### `POST /backups/reload` {#post-backupsreload}

再次读取所有备份位置，以获取在Supervisor之外添加或移除的备份文件。

## 进行备份 {#make-a-backup}

### `POST /backups/new/full` {#post-backupsnewfull}

备份所有内容：Home Assistant、所有应用程序和所有文件夹。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | 字符串 | 否 | 备份名称 |
| `filename` | 字符串 | 否 | 备份文件名。必须以`.tar`结尾且不能包含斜杠 |
| `password` | 字符串或空值 | 否 | 用于加密备份的密码 |
| `compressed` | 布尔值或空值 | 否 | 是否压缩备份。默认`true` |
| `location` | 字符串、空值或列表 | 否 | 备份存储位置。如果是列表，第一个条目为主位置，其他副本将存储到其余位置 |
| `homeassistant_exclude_database` | 布尔值 | 否 | 排除Home Assistant数据库 |
| `background` | 布尔值 | 否 | 立即返回`job_id`而不等待。默认`false` |
| `extra` | 字典 | 否 | 与备份一起存储的额外数据 |当备份完成时，响应包含新备份的`job_id`和`slug`：

```json
{
  "job_id": "e2b7a9c4f1d34e5a8b6c0d1e2f3a4b5c",
  "slug": "a1b2c3d4"
}
```

### `POST /backups/new/partial` {#post-backupsnewpartial}

备份您选择的部分。采用 `POST /backups/new/full` 的所有键，以及：

| 键 | 类型 | 必需 | 描述 |
| --- | --- | --- | --- |
| `addons` | 列表或字符串 | 否 | 包含的应用程序 slug，或 `ALL` 表示所有已安装的应用程序 |
| `folders` | 列表 | 否 | 要包含的 [文件夹](/apps/supervisor-api/backups#folders) |
| `homeassistant` | 布尔值 | 否 | 是否包含 Home Assistant |

```json
{
  "name": "Mosquitto and share",
  "addons": ["core_mosquitto"],
  "folders": ["share"]
}
```

### `POST /backups/new/upload` {#post-backupsnewupload}

上传备份文件。将 `.tar` 文件作为 `multipart/form-data` 发送。响应备份的 `slug`。

| 查询参数 | 描述 |
| --- | --- |
| `location` | 存储备份的位置。可重复以在多个位置存储副本 |
| `filename` | 用于存储备份的文件名。必须以 `.tar` 结尾 |

## 使用备份 {#use-a-backup}

### `GET /backups/<backup>/info` {#get-backupsinfo-1}

返回备份的详细信息。| 键 | 类型 | 描述 |
| --- | --- | --- |
| `slug` | 字符串 | 备份的 ID |
| `type` | 字符串 | `full` 或 `partial` |
| `name` | 字符串 | 备份的名称 |
| `date` | 字符串 | 备份创建时间，ISO 8601 格式 |
| `size` | 浮点数 | 大小 (MB) |
| `size_bytes` | 整数 | 大小 (字节) |
| `compressed` | 布尔值 | 如果备份已压缩则为 `true` |
| `protected` | 布尔值 | 如果备份有密码则为 `true` |
| `location_attributes` | 字典 | `protected` 和每个位置的 `size_bytes` 。本地文件夹是 `.local` |
| `supervisor_version` | 字符串 | 创建备份的 Supervisor 版本 |
| `homeassistant` | 字符串或空 | 备份中 Home Assistant 的版本，如果未包含则为 `null` |
| `location` | 字符串或空 | 主要位置 |
| `locations` | 列表 | 备份存储的所有位置 ||`addons` |列表 |备份中的应用，每个应用都有`slug`、`name`、`version`和`size` |
|`repositories` |列表 |当时添加的应用仓库网址 |
|`folders` |列表 |备份中的文件夹 |
|`homeassistant_exclude_database` |布尔 |`true` 如果Home Assistant数据库被遗漏 |
|`extra` |词典 |备份中存储的额外数据 |

### `GET /backups/<backup>/download` {#get-backupsdownload}

以 `.tar` 文件格式返回备份。使用 `location` 查询参数选择要下载的副本。若不使用，则获取主位置中的副本。

### `DELETE /backups/<backup>` {#delete-backups}

删除备份。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `location` | 字符串、空值或列表 | 否 | 仅删除这些位置的副本。若未指定，则删除所有副本 |

### `POST /backups/<backup>/restore/full` {#post-backupsrestorefull}

恢复备份中的所有内容。Home Assistant 和应用在恢复过程中会重启。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `password` | 字符串或空值 | 否 | 备份的密码 |
| `location` | 字符串或空值 | 否 | 要恢复的副本 |
| `background` | 布尔值 | 否 | 立即返回 `job_id`，而不等待。默认 `false` |

响应包含恢复的 `job_id`。

### `POST /backups/<backup>/restore/partial` {#post-backupsrestorepartial}

恢复您选择的部分。包含完整恢复的所有键，以及：

| 键 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| `addons` | 列表 | 否 | 要恢复的应用程序的标识 |
| `folders` | 列表 | 否 | 要恢复的[文件夹](/apps/supervisor-api/backups#folders) |
| `homeassistant` | 布尔值 | 否 | 恢复 Home Assistant |

## 外部备份 {#external-backups}

### `POST /backups/freeze` {#post-backupsfreeze}

为在 Supervisor 之外进行的备份（如虚拟机快照）准备系统。Home Assistant 和正在运行的应用程序为备份做好准备，就像执行普通备份一样。具有 `backup: cold` 的应用程序会停止。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `timeout` | 整数 | 否 | 系统自动解冻的秒数。默认值为 600 |

### `POST /backups/thaw` {#post-backupsthaw}

结束冻结。Home Assistant 和应用程序恢复正常。
