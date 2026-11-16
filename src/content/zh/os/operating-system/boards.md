---
title: 支持的主板
description: 每个板子Home Assistant OS都会为其构建目标、引导加载程序和机器类型进行构建。
sidebarGroup: 开发板
order: 1
---

# 支持的主板 {#supported-boards}

Home Assistant OS 为每个目标构建一个镜像。每个目标在 `buildroot-external/configs/<target>_defconfig` 中都有一个配置，并且在 [`buildroot-external/board/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/board) 中有一个包含其 [metadata](/os/operating-system/board-metadata) 的板文件夹。自 Home Assistant OS 17 起，每个目标都是 64 位的。

## 所有目标| 开发板 | 构建目标 | 引导加载程序 | 分区表 | 机器 | 备注 | {#all-targets}
| --- | --- | --- | --- | --- | --- |
| Home Assistant Green | `green` | U-Boot | 混合 | `green` | |
| Home Assistant Yellow | `yellow` | U-Boot | 混合 | `yellow` | 用于 Raspberry Pi Compute Module 4 和 5 的载板 |
| Raspberry Pi 3 | `rpi3_64` | U-Boot | 混合 | `raspberrypi3-64` | [Raspberry Pi](/os/operating-system/raspberry-pi) |
| Raspberry Pi 4 | `rpi4_64` | U-Boot | 混合 | `raspberrypi4-64` | [Raspberry Pi](/os/operating-system/raspberry-pi) |
| Raspberry Pi 5 | `rpi5_64` | Tryboot | GPT | `raspberrypi5-64` | [Raspberry Pi](/os/operating-system/raspberry-pi) |
| ODROID-C2 | `odroid_c2` | U-Boot | MBR | `odroid-c2` | [ODROID](/os/operating-system/odroid) |
| ODROID-C4 | `odroid_c4` | U-Boot | MBR | `odroid-c4` | [ODROID](/os/operating-system/odroid) |
| ODROID-M1 | `odroid_m1` | U-Boot | 混合 | `odroid-m1` | [ODROID](/os/operating-system/odroid) |
| ODROID-M1S | `odroid_m1s` | U-Boot | 混合 | `odroid-m1` | [ODROID](/os/operating-system/odroid) || ODROID-N2 和 N2 | `odroid_n2` | U-Boot | MBR | `odroid-n2` | [ODROID](/os/operating-system/odroid)，也有 Home Assistant Blue |
| Khadas VIM3 | `khadas_vim3` | U-Boot | MBR | `khadas-vim3` | |
| 通用 x86-64 | `generic_x86_64` | GRUB | GPT | `generic-x86-64` | [通用系统](/os/operating-system/generic) |
| 通用 aarch64 | `generic_aarch64` | GRUB | GPT | `qemuarm-64` | [通用系统](/os/operating-system/generic)，也有虚拟机镜像 |
| 虚拟机 | `ova` | GRUB | GPT | `qemux86-64` | [虚拟机](/os/operating-system/virtual-machine) |

构建目标是你传递给 `make` 的内容，详见 [构建镜像](/os/operating-system/build)。镜像文件名中的板卡标识符使用连字符，例如 `haos_rpi4-64-18.3.img.xz`。

## 内核 {#kernels}

大多数开发板运行主线 Linux 内核。Raspberry Pi 开发板和 Home Assistant Yellow 运行 [Raspberry Pi 分支](https://github.com/raspberrypi/linux)。当前版本在仓库中的 [`Documentation/kernel.md`](https://github.com/home-assistant/operating-system/blob/dev/Documentation/kernel.md)。

## 已移除的开发板 {#boards-that-were-removed}

32 位目标在 Home Assistant OS 17 中被移除：Raspberry Pi 2、Raspberry Pi 3 和 4 的 32 位版本、ODROID-XU4 和 ASUS Tinker Board。Raspberry Pi 1 和 Zero W 在此之前就已经被移除。这些开发板上的现有安装不再获取更新。

## 添加新开发板 {#adding-a-board}

支持哪些开发板是项目的决定，而不仅仅是代码的问题。[ADR-0015](https://github.com/home-assistant/architecture/blob/master/adr/0015-home-assistant-os.md) 定义了支持的硬件，[ADR-0017](https://github.com/home-assistant/architecture/blob/master/adr/0017-hardware-screening-os.md) 列出了新开发板必须满足的条件，如长期可用性和上游内核支持。在开始之前，请在 [架构仓库](https://github.com/home-assistant/architecture) 中提出新的开发板。
