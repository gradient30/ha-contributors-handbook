---
title: 板元数据
description: 每个板的元文件中的变量，以及所有板共享的版本文件。
sidebarGroup: 参考
order: 3
---

# 板元数据 {#board-metadata}

[`buildroot-external/board/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/board)中的每个板子文件夹都有一个名为`meta`的文件。它向构建脚本描述板子信息：如何命名镜像、使用哪种引导程序和分区表，以及拉取哪些Supervisor镜像。构建脚本将其作为shell变量读取，同时配合共享的`buildroot-external/meta`。

下面是Home Assistant Green的内容：

```shell
BOARD_ID=green
BOARD_NAME="Home Assistant Green"
CHASSIS=embedded
BOOTLOADER=uboot
KERNEL_FILE=Image
PARTITION_TABLE_TYPE=hybrid
BOOT_SIZE=16M
BOOT_SPL=true
BOOT_SPL_SIZE=16M
BOOT_ENV_SIZE=0x8000
SUPERVISOR_MACHINE=green
SUPERVISOR_ARCH=aarch64
```

## 板子 {#board}

| 变量 | 含义 |
| --- | --- |
| `BOARD_ID` | 板子标识符，小写。用于镜像文件名，如`haos_green-18.3.img.xz`，用于RAUC `compatible`的值，以及作为`VARIANT_ID`在`/usr/lib/os-release`中使用。 |
| `BOARD_NAME` | 人类可读名称。用于`VERSION`和`VARIANT`在`/usr/lib/os-release`中。 |
| `CHASSIS` | systemd底盘类型，写入`/etc/machine-info`。`embedded`用于板子，`vm`用于虚拟机镜像。 |

## 引导| 变量 | 含义 | {#boot}
| --- | --- |
| `BOOTLOADER` | `uboot`、`grub` 或 `tryboot`。GRUB 用于 UEFI 系统，tryboot 用于 Raspberry Pi 5，其它地方使用 U-Boot。它设置 RAUC 启动加载程序后台，详见 [更新系统](/os/operating-system/update-system#boot-slots)。 |
| `KERNEL_FILE` | 内核二进制文件名：aarch64 使用 `Image`，x86-64 使用 `bzImage`。 |
| `PARTITION_TABLE_TYPE` | `gpt`、`hybrid` 或 `mbr`。Home Assistant OS 尽可能使用 GPT。GPT 需要磁盘的第二个块作为其头部。一些启动 ROM 自身也需要该块，然后板子使用 `mbr`。`hybrid` 写入两个表，用于 GPT 可用但固件仍读取 MBR 的板子。详见 [分区](/os/operating-system/partitions)。 |
| `BOOT_SIZE` | 启动分区的大小，例如 `32M`。 || `BOOT_SPL` | `true` 或 `false`。板子是否有二级程序加载器（SPL），这是 U-Boot 为某些板子构建的小型第一阶段加载器。有了 `true`，镜像会为其保留空间，并且更新包会包含它。 |
| `BOOT_SPL_SIZE` | SPL 保留的空间，比如 `8M`。仅在 `BOOT_SPL=true` 下有。 |
| `BOOT_ENV_SIZE` | U-Boot 环境的大小，十六进制表示，例如 `0x4000`。RAUC 需要它来读取和写入 `hassos-bootstate` 分区上的环境。仅适用于 U-Boot 板子。 |

## Supervisor {#supervisor}

| 变量 | 含义 |
| --- | --- |
| `SUPERVISOR_MACHINE` | 机器类型。Supervisor 使用它来选择正确的 Home Assistant Core 镜像，应用程序使用它来限制它们支持的机器。多个主板可以共享一个，例如 ODROID-M1 和 M1S 的 `odroid-m1`。当前值列在 [支持的主板](/os/operating-system/boards) 上。 |
| `SUPERVISOR_ARCH` | 容器的 CPU 架构：`aarch64` 或 `amd64`。32位架构已不再支持。 |

两者最终都进入 `/usr/lib/os-release`。`haos-supervisor` 服务使用架构来选择 Supervisor 镜像，并将机器信息传递给 Supervisor 容器。

## 共享版本文件 {#the-shared-version-file}

`buildroot-external/meta` 适用于每块开发板：

```shell
VERSION_MAJOR="18"
VERSION_MINOR="4"
VERSION_SUFFIX="dev0"

HAOS_NAME="Home Assistant OS"
HAOS_ID="haos"

DEPLOYMENT="development"
```

| 变量 | 含义 |
| --- | --- |
| `VERSION_MAJOR`, `VERSION_MINOR`, `VERSION_SUFFIX` | 它们共同组成版本，例如 `18.4.dev0`，或没有后缀的 `18.4`。参见 [版本和构建](/os/operating-system/releases#version-numbers)。 |
| `HAOS_NAME`, `HAOS_ID` | 操作系统的名称和标识符，用于 `/usr/lib/os-release` 和镜像文件名。 |
| `DEPLOYMENT` | `development`, `staging`, 或 `production`。设置镜像在更新时信任的证书，参见 [更新系统](/os/operating-system/update-system#security)。 |
