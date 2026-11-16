---
title: 通用系统
description: 用于 PC 及其他通过 UEFI 启动的系统的通用 x86-64 和 aarch64 目标。
sidebarLabel: 通用 x86-64 和 aarch64
sidebarGroup: 开发板
order: 4
---

# 通用系统 {#generic-systems}

两个目标不是为单个开发板设计的，而是为任何使用 UEFI 启动的系统设计的。

| 目标 | 构建目标 | 适用 |
| --- | --- | --- |
| 通用 x86-64 | `generic_x86_64` | 迷你 PC，例如 Intel NUC，以及其他 64 位 x86 计算机 |
| 通用 aarch64 | `generic_aarch64` | 带有 UEFI 的 64 位 Arm 系统，以及 Arm 虚拟机 |

两者都使用 GRUB、GPT 分区表以及主线 Linux 内核。它们的板文件位于 [`buildroot-external/board/pc/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/board/pc) 和 [`buildroot-external/board/arm-uefi/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/board/arm-uefi)。

## 要求 {#requirements}

- 合适架构的 64 位 CPU
- UEFI 启动，并关闭安全启动
- 内核支持的磁盘，如 SATA、NVMe 或 eMMC
- 受支持的网卡

x86-64 内核包含常用的 Intel 和 Realtek 以太网驱动，以及带固件的 Intel Wi-Fi。Bluetooth 在 Intel Wi-Fi 卡上可用。其他硬件取决于内核配置包括的内容：[`buildroot-external/kernel/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/kernel) 和板子文件夹中的 `kernel.config`。

## 安装 {#installation}

没有安装程序。您需要将镜像写入内部磁盘：

1. 将计算机从 USB 或网络启动进入 Linux live 系统。
2. 下载或复制镜像，并使用 `unxz` 解压。
3. 使用 `dd` 或类似 balenaEtcher 的工具将其写入内部磁盘。
4. 重启。

首次启动时，数据分区会扩展以填满整个磁盘。

## 控制台 {#consoles}

x86-64 镜像使用屏幕作为其控制台。如果系统没有显示控制台输出，可以在启动分区的 `cmdline.txt` 中添加 `nomodeset` 来帮助显示。aarch64 镜像在 `ttyS0` 上也有串行控制台。

## 虚拟机中的通用 aarch64 {#generic-aarch64-in-virtual-machines}

除了磁盘镜像外，aarch64 目标还构建虚拟磁盘镜像（VMDK、VDI 和 QCOW2），用于 Arm 主机上的虚拟机。[虚拟机](/os/operating-system/virtual-machine) 页面涵盖了要求，这些要求是相同的。
