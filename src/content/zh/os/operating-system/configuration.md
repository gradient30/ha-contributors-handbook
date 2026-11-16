---
title: 配置主机
description: 使用 CONFIG USB 驱动器在 Home Assistant OS 上更改主机设置，或直接在主机的持久文件夹中更改。
sidebarLabel: 配置主机
sidebarGroup: 指南
order: 3
---

# 配置主机 {#configure-the-host}

Home Assistant OS 的根文件系统是只读的。需要在重启或更新后仍然保留的设置存放在覆盖分区上，并绑定挂载到相应位置。你可以通过两种方式更改它们：使用 `CONFIG` USB 驱动器，或直接在主机终端上操作。

大多数用户根本不需要涉及这些内容。Supervisor 通过 UI 和 `ha` 命令行管理网络、主机名、交换空间以及数据盘。本页内容涵盖那些 Supervisor 未覆盖的项目，以及开发和调试相关内容。

## CONFIG USB 驱动器 {#the-config-usb-drive}

将 USB 驱动器格式化为 FAT32、exFAT、ext4 或 NTFS，并将其标签命名为 `CONFIG`，使用大写字母。它必须是文件系统的标签：Home Assistant OS 会忽略分区名称。将你需要的文件放在其根目录下：

```text
network/
modules/
modprobe/
udev/
authorized_keys
timesyncd.conf
haos_<board>-<version>.raucb
```| 条目 | 功能 |
| --- | --- |
| `network/` | NetworkManager 连接文件。替换所有现有连接。参见 [配置网络](/os/operating-system/networking)。 |
| `modules/` | `/etc/modules-load.d` 文件，用于在启动时加载内核模块。替换现有文件。 |
| `modprobe/` | `/etc/modprobe.d` 文件，用于设置内核模块选项。替换现有文件。 |
| `udev/` | `/etc/udev/rules.d` 文件。替换现有规则。 |
| `authorized_keys` | root 的公共 SSH 密钥，并在端口 22222 上启动 SSH。参见 [调试主机](/os/operating-system/debugging)。 |
| `timesyncd.conf` | 你自己的时间服务器设置。作为 `/etc/systemd/timesyncd.conf.d/` 中的 drop-in 存储。 |
| `*.raucb` | 待安装的更新包。仅通过 USB 驱动，并且仅在系统启动 5 分钟后使用。 |在每个文本文件中使用 Unix 行结束符（LF）。Windows 行结束符（CRLF）会导致文件损坏。大多数代码编辑器，如 Visual Studio Code，可以切换文件的行结束符。

> [!警告]
> 导入会镜像驱动器。没有 `authorized_keys` 文件的驱动器会删除主机上的密钥，并停止 22222 端口上的 SSH。文件夹也是如此：`network/` 中的内容会替换主机上的所有连接。

### 当驱动器被读取时 {#when-the-drive-is-read}

`haos-config.service` 在每次启动时读取驱动器。要在运行中的系统上导入它，请运行以下命令之一：

```shell
# From the Home Assistant CLI {#from-the-home-assistant-cli}
ha os import

# From the host shell {#from-the-host-shell}
systemctl restart haos-config
```

导入时只需将驱动器插入。导入完成后可以拔出驱动器。

由于五分钟规则，更新包在启动时从不安装。在系统运行后插入驱动器，然后运行 `ha os import`。

### 没有 USB 驱动器 {#without-a-usb-drive}

你也可以在启动分区的根目录下创建一个 `CONFIG` 文件夹，并放入相同内容。对于虚拟机或在全新刷写的 SD 卡首次启动之前，这非常方便。只有在没有标记为 `CONFIG` 的 USB 驱动器时才使用该文件夹，并且导入完成后文件夹会被删除。更新包不会从该文件夹安装。

## 主机上的持久文件夹 {#persistent-folders-on-the-host}

在主机终端，这些路径是来自覆盖分区的绑定挂载。你在这里的更改会在重启和操作系统更新后保留：

| 路径 | 用途 |
| --- | --- |
| `/etc/NetworkManager/system-connections` | 网络连接 |
| `/etc/modules-load.d` | 启动时加载的内核模块 |
| `/etc/modprobe.d` | 内核模块选项 |
| `/etc/udev/rules.d` | udev 规则 |
| `/etc/sysctl.d` | 内核参数 |
| `/etc/systemd/timesyncd.conf.d` | 时间服务器设置 |
| `/etc/hostname`, `/etc/hosts` | 主机名和静态主机名 |
| `/etc/default` | 主机服务设置，例如交换文件 |
| `/etc/usb_modeswitch.d` | 调制解调器的 USB 模式切换 |
| `/root/.ssh` | root 用户的 SSH 密钥 |

`/etc` 下的其他所有内容都来自只读映像，那里进行的更改会在下次重启时丢失。

## 内核命令行 {#kernel-command-line}

在启动分区的 `cmdline.txt` 添加内核参数。引导加载程序会读取它并将其附加到内核命令行。在主机上，启动分区挂载在 `/mnt/boot`。在大多数板子上，当你将 SD 卡或硬盘插入另一台计算机时，它也是第一个显示的分区。

默认设置因板子而异。在许多板子上，`cmdline.txt` 设置控制台，参见 [调试主机](/os/operating-system/debugging#serial-console)。

## 时间服务器 {#time-servers}

Home Assistant OS 使用 systemd-timesyncd。它使用 DHCP 服务器发布的时间服务器，如果没有则回退到 `time.cloudflare.com`。要使用您自己的时间服务器，请将它们放入 `CONFIG` 驱动器上的 `timesyncd.conf` 文件中：

```ini
[Time]
NTP=ntp.example.com
```

或者直接在主机的 `/etc/systemd/timesyncd.conf.d/` 创建一个文件。

## 交换空间 {#swap}

Home Assistant OS 在数据分区上使用交换文件。默认情况下，它占内存的三分之一，至少为 1 GiB，最多为 4 GiB。可以通过 CLI 更改它：

```shell
ha os config swap options --swap-size=2G --swappiness=10
```

操作系统代理将大小存储在 `/etc/default/haos-swapfile` 中，作为 `SWAPSIZE`。大小为 0 会关闭交换文件。更改将在重启后生效，Supervisor 会提出修复问题以说明这一点。
