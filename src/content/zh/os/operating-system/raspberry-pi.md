---
title: 树莓派
description: 针对 Home Assistant OS 的树莓派详细信息，如串行控制台、I2C 和从 USB 启动。
sidebarGroup: 董事会
order: 2
---

# 树莓派 {#raspberry-pi}

Home Assistant OS 支持 Raspberry Pi 3、4 和 5，全部为 64 位。Home Assistant Yellow 建立在相同的板级支持上，可使用 Compute Module 4 或 5。

| 板卡 | 构建目标 | 引导加载程序 |
| --- | --- | --- |
| Raspberry Pi 3 型 B 和 B+ | `rpi3_64` | U-Boot |
| Raspberry Pi 4 型 B | `rpi4_64` | U-Boot |
| Raspberry Pi 5 | `rpi5_64` | Firmware tryboot |
| Home Assistant Yellow | `yellow` | U-Boot |

它们全部使用 [Raspberry Pi Linux 内核](https://github.com/raspberrypi/linux)，而非主线内核。板级文件在 [`buildroot-external/board/raspberrypi/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/board/raspberrypi) 中。

## 它们如何启动 {#how-they-boot}

在 Raspberry Pi 3 和 4 上，Raspberry Pi 固件加载 U-Boot（`kernel=u-boot.bin` 在 `config.txt` 中），然后 U-Boot 选择启动槽。Raspberry Pi 5 不使用 U-Boot 启动：固件直接加载活动槽的内核，更新时使用固件的 tryboot 机制测试新槽。在手动更新后总是使用 `systemctl reboot` 重启 Raspberry Pi 5，参见 [更新系统](/os/operating-system/update-system#how-an-update-runs)。

`config.txt` 和 `cmdline.txt` 位于启动分区。对它们的修改在操作系统更新中会保留。

## 串行控制台 {#serial-console}

在 Raspberry Pi 3 和 4 上，串行控制台默认未启用。要在 GPIO 接口上启用它（引脚 6 为地，8 为 TX，10 为 RX）：

1. 将 `enable_uart=1` 和 `dtoverlay=disable-bt` 添加到 `config.txt` 。该覆盖会将 Bluetooth 从主 UART 移开。
2. 将 `console=ttyAMA0,115200` 添加到 `cmdline.txt` 。

Home Assistant Yellow 已启用其串行控制台，在 `ttyAMA2` 以 115200 波特率运行。

## I2C {#i2c}

1. 将 `dtparam=i2c_arm=on` 添加到 `config.txt` 。
2. 在启动时加载 `i2c-dev` 模块：在 [CONFIG USB 驱动器](/os/operating-system/configuration#the-config-usb-drive) 的 `modules/` 文件夹中创建一个包含 `i2c-dev` 行的文件，或在主机上的 `/etc/modules-load.d/`。

## 从 USB 启动 {#boot-from-usb}

Raspberry Pi 4 和 5 可以从 USB 驱动器启动，如果它们的 EEPROM 中的引导加载程序足够新。Home Assistant OS 包含 EEPROM 工具。`ha os boards raspberrypi firmware update` 可以从 CLI 更新引导加载程序。

一些需要注意的事情：

- 移除所有可启动的 SD 卡。固件会优先尝试 SD 卡。
- 启动速度较慢，因为固件会先查看 SD 卡再查看 USB。
- 不是所有 USB 转 SATA 适配器都能工作。在 Raspberry Pi 4 上，`cmdline.txt` 已经包含`usb-storage.quirks`，适用于已知需要它们的适配器。Raspberry Pi 5 镜像没有此项。如果你的适配器表现异常，找到它的 USB ID 并为其添加特殊处理。
- 如果没有 SD 卡，向 `config.txt` 添加 `dtparam=sd_poll_once=on`，以阻止内核轮询空插槽。

Raspberry Pi 3 型 B 在 `program_usb_boot_mode=1` 在 `config.txt` 中设置一次后可以从 USB 启动。此更改是永久性的：它会写入一次性可编程存储器。

## Bluetooth {#bluetooth}

Bluetooth 默认是开启的。如果你不需要它，可以在 `config.txt` 中的 `dtoverlay=disable-bt` 将其关闭。
