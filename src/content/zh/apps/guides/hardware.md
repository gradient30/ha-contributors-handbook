---
title: 访问硬件和主机
description: 让你的应用访问串口、USB 设备、GPIO、音频和主机的部分功能，并且只访问它所需要的部分。
order: 4
---


# 访问硬件和主机 {#access-hardware-and-the-host}
默认情况下，应用程序看不到硬件，对主机的访问也很少。这是有意为之：你增加的每一位访问权限都可能被应用程序中的错误滥用。本指南展示了从窄到宽的选项。选择能工作的最窄选项。

## 让用户选择设备 {#let-the-user-pick-a-device}
对于 USB 设备或串行适配器，最佳选择通常不在 `config.yaml` 中，而是在你的选项中。`device` 选项会向用户显示系统上的设备下拉列表，而 Supervisor 将选择的设备映射到你的容器中：

```yaml
options:
  device:
schema:
  device: "device(subsystem=tty)"
```

用户选择设备后，它可以在重启后继续工作，因为下拉列表提供了系统已有的稳定 `/dev/serial/by-id/...` 路径，并且你的应用程序只访问该设备。这就是官方 Z-Wave JS 应用程序的做法。

## 固定设备 {#fixed-devices}
如果你的应用程序总是使用相同的设备，请在 `devices` 中列出其路径：

```yaml
devices:
  - /dev/ttyAMA0
```

## 设备组 {#groups-of-devices}
这些选项映射了整个类别的设备，包括应用启动后插入的设备：

| 键 | 访问 |
| --- | --- |
| `uart: true` | 所有串行设备 |
| `usb: true` | 通过 `/dev/bus/usb` 进行原始 USB 访问 |
| `video: true` | 所有视频设备 |
| `gpio: true` | GPIO，通过 `/sys/class/gpio`。一些库还需要 `/dev/mem` 和 `SYS_RAWIO` 功能 |
| `udev: true` | 主机的 udev 数据库，只读，用于查询设备详细信息 |
| `devicetree: true` | 主机的设备树，位于 `/device-tree` |

在使用 AppArmor 的系统上，GPIO 访问通常还需要自定义 AppArmor 配置文件。请参阅 [保护你的应用](/apps/guides/security#apparmor)。

## 音频 {#audio}
通过 `audio: true`，你的应用程序通过 PulseAudio 连接到 Home Assistant 的音频系统，用户可以在应用页面上选择输入和输出设备。如果你的软件只支持 ALSA，请为 ALSA 安装 PulseAudio 插件：Alpine 上为 `alsa-plugins-pulse`，Debian 和 Ubuntu 上为 `libasound2-plugins`。

## 主机 {#the-host}
有些应用比设备更需要主机资源：

| 键 | 提供内容 |
| --- | --- |
| `host_network: true` | 主机的网络。用于像 mDNS 这样的发现协议以及必须看到真实网络接口的软件。降低安全等级。 |
| `host_dbus: true` | 主机的 D-Bus 系统总线，只读，用于与 NetworkManager 或 BlueZ 等服务通信。 |
| `journald: true` | 系统日志，只读。在某些系统上位于 `/var/log/journal`，在其他系统上位于 `/run/log/journal`，所以两者都要检查。 |
| `kernel_modules: true` | 主机的内核模块，只读，以及加载它们的权限。 |
| `realtime: true` | 实时调度，用于需要低延迟的音频软件。 |
| `host_uts: true` | 主机的主机名。 |

完整列表，包括使用 `privileged` 的功能，请参见 [应用配置](/apps/reference/configuration#host-and-privileges)。

## 保护模式 {#protection-mode}
有些选项仅在**保护模式**关闭时有效：`full_access`、`docker_api` 和 `host_pid`。保护模式默认开启，当关闭时，UI 会提醒用户。当保护模式关闭并设置了这些选项时，你的应用几乎可以对系统进行任何操作。

这些选项仅用于那些管理系统本身的应用，并在你的文档中解释为什么应用需要它。特别是 `full_access` 给了访问所有设备的权限，使 `devices`、`uart`、`usb` 和 `gpio` 变得毫无意义。`full_access` 和 `docker_api` 将 [安全等级](/apps/reference/security-rating) 设置为 1，而 `host_pid` 将其降低 2。
