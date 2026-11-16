---
title: 主机和操作系统端点
description: Supervisor 主机系统、Home Assistant OS、硬件、网络、时间、挂载点和 Docker 的 API 端点。
sidebarLabel: 主机和操作系统
order: 5
---

# 主机和操作系统端点 {#host-and-os-endpoints}

这些终端接触到容器以下的部分：主机系统及其操作系统。大多数需要 `hassio_api: true` 和 `manager` 或 `admin` 角色。`/info` 终端，如 `GET /host/info`，可以与任何角色一起使用。

有些终端只存在于 Home Assistant OS 上，或者需要其较新版本。如果它们不可用，将返回 `404`。

## 主机 {#host}

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/host/info` | 有关主机的信息 |
| `POST` | `/host/options` | 更改主机设置 |
| `POST` | `/host/reboot` | 重启主机 |
| `POST` | `/host/shutdown` | 关闭主机 |
| `POST` | `/host/reload` | 重新读取主机信息 |
| `GET` | `/host/services` | 列出 systemd 服务 |
| `GET` | `/host/disks` | 列出可挂载的磁盘 |
| `GET` | `/host/disks/<disk>/usage` | 磁盘使用情况 |
| `GET` | `/host/logs` | 主机日志 |
| `GET` | `/host/logs/boots` | 列出日志中的启动信息 |
| `GET` | `/host/logs/identifiers` | 列出日志中的 syslog 标识符 |
### `GET /host/info` {#get-hostinfo}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `agent_version` | 字符串或空 | OS Agent 的版本 |
| `apparmor_version` | 字符串或空 | AppArmor 的版本 |
| `chassis` | 字符串或空 | 底盘类型，例如 `embedded` 或 `vm` |
| `virtualization` | 字符串或空 | 虚拟化类型，没有则为空 |
| `cpe` | 字符串或空 | 操作系统的 CPE 名称 |
| `deployment` | 字符串或空 | 部署类型，例如 `production` 或 `development` |
| `disk_free` | 浮点数 | 可用磁盘空间（GiB） |
| `disk_total` | 浮点数 | 磁盘总空间（GiB） |
| `disk_used` | 浮点数 | 已用磁盘空间（GiB） |
| `disk_life_time` | 浮点数或空 | 数据盘使用寿命百分比，当磁盘有报告时 |
| `features` | 列表 | 主机支持的功能，例如 `reboot`、`network` 或 `haos` |
| `all_features` | 列表 | 所有功能。`features` 对旧客户端会省略 `ntp` || `hostname` | 字符串或空值 | 主机名 |
| `llmnr_hostname` | 字符串或空值 | LLMNR 主机名 |
| `kernel` | 字符串或空值 | 内核版本 |
| `operating_system` | 字符串或空值 | 操作系统名称 |
| `timezone` | 字符串或空值 | 主机时区 |
| `dt_utc` | 字符串 | 当前 UTC 时间，ISO 8601 格式 |
| `dt_synchronized` | 布尔值或空值 | 如果时钟已同步则为 `true` |
| `use_ntp` | 布尔值或空值 | 如果主机使用 NTP 则为 `true` |
| `startup_time` | 浮点数或空值 | 上次启动所用秒数 |
| `boot_timestamp` | 整数或空值 | 上次启动的时间戳（微秒），由 systemd 报告 |
| `broadcast_llmnr` | 布尔值或空值 | 如果主机通过 LLMNR 宣布自己则为 `true` |
| `broadcast_mdns` | 布尔值或空值 | 如果主机通过 mDNS 宣布自己则为 `true` |

### `POST /host/options` {#post-hostoptions}

| 键 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| `hostname` | 字符串 | 否 | 新主机名 |

### `POST /host/reboot` {#post-hostreboot}

重新启动主机。在 Home Assistant 运行数据库迁移时会失败，除非强制执行。

| 键 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| `force` | 布尔值 | 否 | 即使在数据库迁移期间也重启。默认 `false` |

### `POST /host/shutdown` {#post-hostshutdown}

关闭主机。使用与 `POST /host/reboot` 相同的 `force` 键。

### `POST /host/reload` {#post-hostreload}

再次读取主机信息。

### `GET /host/services` {#get-hostservices}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `services` | 列表 | [主机服务模型](/apps/supervisor-api/models#host-service) 列表 |

### `GET /host/disks` {#get-hostdisks}

返回具有可用于 [磁盘挂载](/apps/supervisor-api/host#mounts) 的分区的磁盘。

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `disks` | 列表 | 磁盘，每个磁盘包含 `name`、`vendor`、`model`、`serial`、`size`、`id`、`dev_path`、`connection_bus`、`removable`、`ejectable` 和 `partitions` |

每个分区具有 `device`、`uuid`、`label`、`filesystem`、`size`、`read_only` 和 `mountable`。

### `GET /host/disks/<disk>/usage` {#get-hostdisksusage}

以字节为单位返回磁盘空间的使用情况。将 `default` 用作 `<disk>` 来表示系统磁盘，或使用挂载的名称。`default` 总是表示系统磁盘，因此名为 `default` 的挂载在此无法测量。

| 查询参数 | 描述 |
| --- | --- |
| `max_depth` | 要分解的文件夹层级数。系统磁盘默认为 1，挂载默认为 0 |

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `id` | string | 条目的 ID |
| `label` | string | 条目的名称 |
| `total_bytes` | integer | 磁盘大小。仅适用于顶层条目 |
| `used_bytes` | integer | 已用空间 |
| `children` | list | 每个部分的相同结构。当没有进一步分解时会省略 |对于系统磁盘，子项是 `system`、`addons_data`、`addons_config`、`media`、`share`、`backup`、`ssl` 和 `homeassistant`，`max_depth` 设置了它们内部分解的深度。

一个挂载点没有这样的固定部分，所以 Supervisor 会遍历它的文件夹。一个 `max_depth` 为 0 或 1 会只返回总计，2 会添加第一层文件夹，每下一层则需要再加 1。一个 `other` 子项保存不在文件夹中的内容，比如挂载点顶层的文件。当遍历过程中文件发生变化且文件夹总数超过 `used_bytes` 时，分解将被省略。Supervisor 通过访问挂载点来测量挂载点，如果挂载点尚未挂载，则会先挂载。不存在的挂载点会返回 `404`。无法读取或不再挂载的挂载点会返回错误。当测量时间超过 60 秒时，请求会返回错误，但测量仍会继续进行。在测量进行中，如果对同一个挂载点和 `max_depth` 发起新的请求，该请求会等待当前测量完成，而不会启动另一个测量。`max_depth` 小于 2 被视为相同深度。

### 主机日志 {#host-logs}

`GET /host/logs` 返回主机的日志，工作方式类似其他 [日志端点](/apps/supervisor-api#log-endpoints)。默认情况下，它显示最重要的服务，每一行都带有时间戳和进程信息，就像 `verbose` 一样。这些端点可以缩小范围：

| 路径 | 返回 |
| --- | --- |
| `/host/logs/follow` | 日志，然后流式传输新行 |
| `/host/logs/boots/<bootid>` | 一次启动的日志 |
| `/host/logs/boots/<bootid>/follow` | 一次启动的日志，然后流式传输新行 |
| `/host/logs/identifiers/<identifier>` | 一个 syslog 标识符的日志 |
| `/host/logs/identifiers/<identifier>/follow` | 一个标识符的日志，然后流式传输新行 |
| `/host/logs/boots/<bootid>/identifiers/<identifier>` | 一次启动中一个标识符的日志 |
| `/host/logs/boots/<bootid>/identifiers/<identifier>/follow` | 同上，然后流式传输新行 |

### `GET /host/logs/boots` {#get-hostlogsboots}

按偏移返回日志中的启动记录。`0` 是当前启动。

@@H@@

### `GET /host/logs/identifiers` {#get-hostlogsidentifiers}

返回日志中 syslog 的标识符，作为 `identifiers`。有用的包括用于网络问题的 `NetworkManager`，用于 Bluetooth 的 `bluetoothd`，以及在处理 AppArmor 配置文件时使用的 `audit`。

## Home Assistant OS {#home-assistant-os}

这些仅适用于 Home Assistant OS。| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/os/info` | 操作系统信息 |
| `POST` | `/os/update` | 更新操作系统 |
| `POST` | `/os/config/sync` | 从 USB 设备加载配置 |
| `GET` | `/os/config/swap` | 交换设置 |
| `POST` | `/os/config/swap` | 更改交换设置 |
| `POST` | `/os/boot-slot` | 切换启动槽并重启 |
| `GET` | `/os/datadisk/list` | 数据可以移动到的磁盘 |
| `POST` | `/os/datadisk/move` | 将数据移动到另一块磁盘 |
| `POST` | `/os/datadisk/wipe` | 清除数据磁盘 |
| `GET` | `/os/boards/<board>` | 检查主板 |
| `GET` | `/os/boards/yellow` | Home Assistant Yellow 的设置 |
| `POST` | `/os/boards/yellow` | 更改 Home Assistant Yellow 的设置 |
| `GET` | `/os/boards/green` | Home Assistant Green 的设置 |
| `POST` | `/os/boards/green` | 更改 Home Assistant Green 的设置 |
| `GET` | `/os/boards/raspberrypi/firmware` | 树莓派固件状态 || `POST` | `/os/boards/raspberrypi/firmware/update` | 更新 Raspberry Pi 固件 |
| `GET` | `/os/ssh/authorized_keys` | 列出主机的 SSH 密钥 |
| `POST` | `/os/ssh/authorized_keys` | 向主机添加 SSH 密钥 |
| `DELETE` | `/os/ssh/authorized_keys` | 删除主机的所有 SSH 密钥 |

### `GET /os/info` {#get-osinfo}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `version` | 字符串 | 已安装的版本 |
| `version_latest` | 字符串 | 可用的最新版本 |
| `version_pending` | 字符串或空值 | 已安装但等待重启的版本 |
| `update_available` | 布尔值 | 如果有更新可用则为 `true` |
| `board` | 字符串 | 主板名称，如 `generic-x86-64` 或 `yellow` |
| `boot` | 字符串 | 当前激活的启动槽 |
| `data_disk` | 字符串 | 数据盘的ID |
| `boot_slots` | 字典 | 每个启动槽 (`A` 和 `B`) 的 [启动槽模型](/apps/supervisor-api/models#boot-slot)。使用这些名称用于 `POST /os/boot-slot` |

### `POST /os/update` {#post-osupdate}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `version` | 字符串 | 否 | 要安装的版本。默认是最新版本 |

将更新安装到非活动槽中，然后返回。它不会重启：新版本将在 `GET /os/info` 的 `version_pending` 中等待系统重启，例如通过 `POST /host/reboot`。在此之前，`version` 仍然是正在运行的版本。对于 Home Assistant Core 在 2026.8 之前的版本，`version` 会报告待定版本，因此更新不会再次提供。

### `POST /os/config/sync` {#post-osconfigsync}

从 USB 设备加载配置，比如网络设置。

### `GET /os/config/swap` {#get-osconfigswap}

需要 Home Assistant OS 15.0 或更高版本。

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `swap_size` | 字符串 | 交换文件大小，例如 `1G` |
| `swappiness` | 整数 | 内核交换性，从 0 到 200 |

### `POST /os/config/swap` {#post-osconfigswap}

使用相同的键。`swap_size` 是一个带可选单位的数值：`B`、`K`、`M` 或 `G`，可选地后跟 `B` 或 `iB`。小于 40 kB 的大小将关闭交换。更改会创建需要重启的问题。

### `POST /os/boot-slot` {#post-osboot-slot}

切换到另一个启动槽并重启进入。

| 键 | 类型 | 必需 | 描述 |
| --- | --- | --- | --- |
| `boot_slot` | 字符串 | 是 | `A` 或 `B` |

### `GET /os/datadisk/list` {#get-osdatadisklist}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `devices` | 列表 | 数据可以移动到的磁盘 ID |
| `disks` | 列表 | [磁盘型号](/apps/supervisor-api/models#disk) 列表 |

### `POST /os/datadisk/move` {#post-osdatadiskmove}

将数据分区移动到另一块磁盘，并重启系统。

| 键 | 类型 | 必需 | 描述 |
| --- | --- | --- | --- |
| `device` | string | 是 | 目标磁盘的 ID 或设备路径 |

### `POST /os/datadisk/wipe` {#post-osdatadiskwipe}

抹掉数据磁盘并重启。只有具有 `admin` 角色的应用可以调用此操作。

该抹除操作会格式化数据分区和覆盖分区。这样会移除 Home Assistant、所有应用、备份以及数据磁盘上的媒体，以及主机设置（如网络连接）。操作系统及其启动槽保持不变。重启后，系统会再次下载 Home Assistant 并开始首次使用引导，就像新安装一样。你可能需要重新设置网络以便访问它。

### `GET /os/boards/<board>` {#get-osboards}

当 `<board>` 是所使用的主板时，返回成功并带有空数据，否则返回错误。`<board>` 是 `GET /os/info` 的 `board` 值。

### `GET /os/boards/yellow` {#get-osboardsyellow}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `disk_led` | 布尔型 | 磁盘活动指示灯开启 |
| `heartbeat_led` | 布尔型 | 心跳指示灯开启 |
| `power_led` | 布尔型 | 电源指示灯开启 |

`POST /os/boards/yellow` 接受相同的键，全部为可选。更改会导致需要重启的问题。

### `GET /os/boards/green` {#get-osboardsgreen}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `activity_led` | 布尔值 | 活动 LED 灯亮 |
| `power_led` | 布尔值 | 电源 LED 灯亮 |
| `system_health_led` | 布尔值 | 系统健康 LED 灯亮 |

`POST /os/boards/green` 接受相同的键，全部为可选。

### `GET /os/boards/raspberrypi/firmware` {#get-osboardsraspberrypifirmware}

返回树莓派引导加载程序固件的状态，以及板载有 VL805 USB 控制器时该控制器固件的状态。当板上没有固件可管理，或操作系统代理版本低于 1.9.0 时，返回 `404`。

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `current_version` | 字符串或空值 | 已安装的固件版本 |
| `latest_version` | 字符串或空值 | 随操作系统提供的最新固件版本 |
| `update_available` | 布尔值 | 如果有更新可用则为 `true` |
| `update_blocked` | 布尔值 | 如果启动设备不允许更新则为 `true` |
| `update_pending` | 布尔值 | 如果更新等待重启则为 `true` |
| `blocked_reason` | 字符串或空值 | 更新被阻止的原因，如果没有则为 `null`。目前无论原因如何总是 `unsupported_boot_device` |

### `POST /os/boards/raspberrypi/firmware/update` {#post-osboardsraspberrypifirmwareupdate}

将树莓派固件更新到操作系统自带的版本。当 `update_blocked` 为 `true` 时返回错误。新的固件在重启后运行，因此成功更新会产生需要重启的问题。

### 主机的 SSH 密钥 {#ssh-keys-of-the-host}

`/os/ssh/authorized_keys` 管理主机上 `root` 用户的 SSH 密钥，用于 [端口 22222 的 SSH 服务器](/os/operating-system/debugging)。只有 Home Assistant Core 可以调用这些端点，应用程序无法调用。

- `GET` 以 `keys` 的形式返回密钥，每行对应文件中的一个条目，不包括空行和注释行。需要 OS Agent 1.11.0 或更高版本，否则返回 `404`。
- `POST` 会将你发送的 `key` 密钥添加到已有密钥中，形式类似 `ssh-ed25519 AAAA...`。密钥长度不得超过 3000 字节，且不能包含控制字符。从 OS Agent 1.10.0 起，密钥还必须是 OpenSSH `authorized_keys` 文件的一行有效内容，包括选项。添加密钥也会启动主机的 SSH 服务器。
- `DELETE` 会删除所有密钥。同时也会停止 SSH 服务器，从而终止当前打开的会话。

## 硬件 {#hardware}

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/hardware/info` | 设备和驱动器 |
| `GET` | `/hardware/audio` | 音频设备 |

### `GET /hardware/info` {#get-hardwareinfo}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `devices` | list | [设备型号](/apps/supervisor-api/models#device) 列表 |
| `drives` | list | [驱动器型号](/apps/supervisor-api/models#drive) 列表 |

### `GET /hardware/audio` {#get-hardwareaudio}

返回主机的音频设备，包括名称和描述。

```json
{
  "audio": {
    "input": {
      "0,0": "Mic"
    },
    "output": {
      "1,0": "Jack",
      "0,1": "HDMI"
    }
  }
}
```

## 网络 {#network}

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/network/info` | 所有接口和内部网络 |
| `POST` | `/network/reload` | 再次读取网络状态 |
| `GET` | `/network/interface/<interface>/info` | 单个接口 |
| `POST` | `/network/interface/<interface>/update` | 更改接口 |
| `GET` | `/network/interface/<interface>/accesspoints` | 扫描 Wi-Fi 网络 |
| `POST` | `/network/interface/<interface>/vlan/<id>` | 创建 VLAN |

`<interface>` 是接口的名称，例如 `eth0`，或主接口`default`。

### `GET /network/info` {#get-networkinfo}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `interfaces` | 列表 | 一系列 [网络接口模型](/apps/supervisor-api/models#network-interface) |
| `docker` | 字典 | 内部网络: `interface`, `address`, `gateway`, 和 `dns` |
| `host_internet` | 布尔值或空 | 如果主机可以连接互联网，则为 `true` |
| `supervisor_internet` | 布尔值 | 如果 Supervisor 可以连接互联网，则为 `true` |

```json
{
  "interfaces": [
    {
      "interface": "eth0",
      "type": "ethernet",
      "enabled": true,
      "connected": true,
      "primary": true,
      "mac": "52:54:00:12:34:56",
      "ipv4": {
        "method": "auto",
        "address": ["192.168.1.100/24"],
        "nameservers": ["192.168.1.1"],
        "gateway": "192.168.1.1",
        "route_metric": null,
        "ready": true
      },
      "ipv6": null,
      "wifi": null,
      "vlan": null,
      "mdns": "default",
      "llmnr": "default"
    }
  ],
  "docker": {
    "interface": "hassio",
    "address": "172.30.32.0/23",
    "gateway": "172.30.32.1",
    "dns": "172.30.32.3"
  },
  "host_internet": true,
  "supervisor_internet": true
}
```

### `POST /network/reload` {#post-networkreload}

再次读取网络状态，并检查互联网连接。

### `GET /network/interface/<interface>/info` {#get-networkinterfaceinfo}

返回一个 [网络接口模型](/apps/supervisor-api/models#network-interface)。

### `POST /network/interface/<interface>/update` {#post-networkinterfaceupdate}

更改接口的配置。至少发送一个键。您发送的一个块将替换该块的整个配置，因此请发送该块的所有键。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `enabled` | 布尔值 | 否 | 打开或关闭接口 |
| `ipv4` | 字典 | 否 | IPv4 设置，见下文 |
| `ipv6` | 字典 | 否 | IPv6 设置，见下文 |
| `wifi` | 字典 | 否 | Wi-Fi 设置，见下文 |
| `mdns` | 字符串 | 否 | `default`、`off`、`resolve` 或 `announce` |
| `llmnr` | 字符串 | 否 | `default`、`off`、`resolve` 或 `announce` |

`ipv4` 和 `ipv6` 块包含：| 键 | 类型 | 描述 |
| --- | --- | --- |
| `method` | 字符串 | `auto`、`static` 或 `disabled`。默认 `static` |
| `address` | 列表 | 带前缀的地址，如 `192.168.1.100/24` |
| `gateway` | 字符串 | 网关 |
| `nameservers` | 列表 | DNS 服务器 |
| `route_metric` | 整数 | 路由指标，值越低优先级越高 |
| `addr_gen_mode` | 字符串 | 仅 IPv6：`eui64`、`stable-privacy`、`default-or-eui64` 或 `default` |
| `ip6_privacy` | 字符串 | 仅 IPv6：`disabled`、`enabled-prefer-public`、`enabled` 或 `default` |

`wifi` 块包含：

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `mode` | 字符串 | `infrastructure`、`mesh`、`adhoc` 或 `ap`。默认 `infrastructure` |
| `auth` | 字符串 | `open`、`wep` 或 `wpa-psk`。默认 `open` |
| `ssid` | 字符串 | 网络名称 |
| `psk` | 字符串 | 网络密码 |

```json
{
  "ipv4": {
    "method": "static",
    "address": ["192.168.1.100/24"],
    "gateway": "192.168.1.1",
    "nameservers": ["192.168.1.1"]
  }
}
```

### `GET /network/interface/<interface>/accesspoints` {#get-networkinterfaceaccesspoints}

扫描 Wi-Fi 网络。仅在无线接口上有效。

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `accesspoints` | 列表 | 一个 [接入点型号](/apps/supervisor-api/models#access-point) 列表 |

### `POST /network/interface/<interface>/vlan/<id>` {#post-networkinterfacevlan}

在以太网接口上创建 VLAN。`<id>` 是 VLAN ID，范围为 0 到 4094。接受更新端点的 `ipv4`、`ipv6`、`mdns` 和 `llmnr` 键。在这里，`method` 默认为 `auto`，而不是 `static`。

## 时间 {#time}

这些端点设置主机用于同步其时钟的 NTP 服务器。它们需要 Home Assistant OS 18.3 或更高版本，否则将返回 `404`。当它们可用时，`all_features` 的 `GET /host/info` 列出 `ntp`。

### `GET /time/info` {#get-timeinfo}

返回 Supervisor 配置的服务器，作为 `config`。主机还可以从其他地方获取服务器，例如 DHCP，因此使用的服务器可能不同。

```json
{
  "config": {
    "servers": ["time.cloudflare.com"],
    "fallback_servers": []
  }
}
```

### `POST /time/options` {#post-timeoptions}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `servers` | 列表 | 否 | 使用的 NTP 服务器 |
| `fallback_servers` | 列表 | 否 | 当其他服务器不可达时使用的 NTP 服务器 |

如果你省略某个键，它将保持当前值。空列表会清除已配置的服务器。每个服务器可以是主机名或 IP 地址。更改后，主机的时间同步服务将重新启动。

## 挂载点 {#mounts}

挂载点将网络共享和本地磁盘添加到系统中，用于备份、媒体或共享文件夹。

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/mounts` | 列出挂载点 |
| `POST` | `/mounts/options` | 修改挂载设置 |
| `POST` | `/mounts` | 添加挂载点 |
| `PUT` | `/mounts/<name>` | 修改挂载点 |
| `DELETE` | `/mounts/<name>` | 移除挂载点 |
| `POST` | `/mounts/<name>/reload` | 重新挂载 |

### `GET /mounts` {#get-mounts}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `default_backup_mount` | 字符串或空值 | 默认备份的挂载名称，`null` 表示本地 |
| `mounts` | 列表 | [挂载模型](/apps/supervisor-api/models#mount) 的列表 |

### `POST /mounts/options` {#post-mountsoptions}

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `default_backup_mount` | 字符串或空值 | 否 | 备份挂载的名称，`null` 表示本地备份 |

### `POST /mounts` {#post-mounts}

添加一个坐骑。该坐骑的本体是一个 [坐骑模型](/apps/supervisor-api/models#mount)。

```json
{
  "name": "nas_backups",
  "usage": "backup",
  "type": "cifs",
  "server": "nas.local",
  "share": "backups",
  "username": "homeassistant",
  "password": "secret"
}
```

你添加的第一个备用坐骑将成为默认的备用位置。

### `PUT /mounts/<name>` {#put-mounts}

替换坐骑的配置。使用与 `POST /mounts` 相同的主体。无法更改名称。

### `DELETE /mounts/<name>` {#delete-mounts}

移除坐骑。

### `POST /mounts/<name>/reload` {#post-mountsreload}

检查坐骑是否响应。响应的坐骑保持不变。否则，Supervisor 会使用相同的配置重新挂载它，如果仍无法访问，则返回错误。当共享不可达时，这个功能很有用。

## Docker {#docker}

| 方法 | 路径 | 描述 |
| --- | --- | --- |
| `GET` | `/docker/info` | Docker 信息 |
| `POST` | `/docker/options` | 更改 Docker 设置 |
| `GET` | `/docker/registries` | 列出带有凭据的容器注册表 |
| `POST` | `/docker/registries` | 为注册表添加凭据 |
| `DELETE` | `/docker/registries/<hostname>` | 删除注册表的凭据 |
| `POST` | `/docker/migrate-storage-driver` | 切换存储驱动 |
| `POST` | `/docker/reset-storage` | 在下次重启时重置 Docker 存储 |

### `GET /docker/info` {#get-dockerinfo}

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `version` | 字符串 | Docker 版本 |
| `enable_ipv6` | 布尔值或空 | 如果内部网络启用了 IPv6，则为 `true` |
| `mtu` | 整数或空 | 内部网络的 MTU |
| `storage` | 字符串 | 存储驱动 |
| `logging` | 字符串 | 日志驱动 |
| `registries` | 字典 | 带凭证的注册表，按主机名列出，并含有 `username` |

### `POST /docker/options` {#post-dockeroptions}

更改需要重启才能生效，并会创建一个需要重启的问题。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `enable_ipv6` | 布尔值或空 | 否 | 为内部网络启用 IPv6 |
| `mtu` | 整数或空 | 否 | 内部网络的 MTU，范围从 68 到 65535 |

### `GET /docker/registries` {#get-dockerregistries}

```json
{
  "registries": {
    "ghcr.io": {
      "username": "octocat"
    }
  }
}
```

### `POST /docker/registries` {#post-dockerregistries}

为容器注册表添加凭据。Supervisor 使用这些凭据来拉取镜像。对于 Docker Hub，请使用 `docker.io` 作为主机名。

```json
{
  "ghcr.io": {
    "username": "octocat",
    "password": "ghp_secret"
  }
}
```

### `DELETE /docker/registries/<hostname>` {#delete-dockerregistries}

移除注册表的凭据。

### `POST /docker/migrate-storage-driver` {#post-dockermigrate-storage-driver}

在下次重启时切换 Docker 存储驱动，并创建一个需要重启的问题。需要 Home Assistant OS 17.0 或更高版本，否则返回 `404`。

| 键 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `storage_driver` | string | 是 | `overlayfs` |

### `POST /docker/reset-storage` {#post-dockerreset-storage}

在下次重启时丢弃所有镜像和容器，并创建一个需要重启的问题。重启后，系统会再次下载 Supervisor、Home Assistant Core、插件和应用的镜像，因此需要互联网访问。需要 Home Assistant OS 18.3 或更高版本，否则返回 `404`。
