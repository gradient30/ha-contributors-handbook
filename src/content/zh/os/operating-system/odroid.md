---
title: ODROID
description: Hardkernel ODROID 对 Home Assistant OS 的具体信息，例如 eMMC 安装、M1 和 M1S 的启动流程，以及控制台。
sidebarGroup: 董事会
order: 3
---



# ODROID {#odroid}
Home Assistant OS 支持五款 Hardkernel ODROID 开发板。它们的板文件在 [`buildroot-external/board/hardkernel/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/board/hardkernel) 中。

| 开发板 | 构建目标 | SoC 系列 | 备注 |
| --- | --- | --- | --- |
| ODROID-C2 | `odroid_c2` | Amlogic | 已停止生产 |
| ODROID-C4 | `odroid_c4` | Amlogic | |
| ODROID-N2 和 N2  | `odroid_n2` | Amlogic | Home Assistant 蓝色是 ODROID-N2 |
| ODROID-M1 | `odroid_m1` | Rockchip | 自 Home Assistant OS 10 起 |
| ODROID-M1S | `odroid_m1s` | Rockchip | 自 Home Assistant OS 12 起 |

所有板子都使用 U-Boot 启动，并运行主线 Linux 内核。

## Wi-Fi 和 Bluetooth 模块 {#wi-fi-and-bluetooth-modules}

Hardkernel 的 [WiFi 模块 3](https://www.hardkernel.com/shop/wifi-module-3/) 和 [Bluetooth 模块 2](https://www.hardkernel.com/shop/bluetooth-module-2/) 曾在 Home Assistant OS 中进行测试。WiFi 模块 5A 没有上游驱动程序，不推荐使用。

## ODROID-C2、C4 和 N2 {#odroid-c2-c4-and-n2}

该镜像在 eMMC 上的工作方式与在 SD 卡上一样：将其刷入 eMMC 模块。

串行控制台在串行头上，`ttyAML0`，115200 波特率，位于 HDMI 控制台旁边。内核会将其信息发送到两者，但 systemd 启动信息只会发送到 `cmdline.txt` 中最后列出的控制台。默认情况下为 HDMI：

```text
console=ttyAML0,115200n8 console=tty0
```

如果要在串行控制台上查看启动信息，请交换两者。

在 ODROID-N2 上，GPIO 引脚 11 可用作电源按钮，低有效。有关 GPIO 接头的信息，请参阅 ODROID 维基上的 [C2](https://wiki.odroid.com/odroid-c2/hardware/expansion_connectors)、[C4](https://wiki.odroid.com/odroid-c4/hardware/expansion_connectors) 和 [N2](https://wiki.odroid.com/odroid-n2/hardware/expansion_connectors)。

## ODROID-M1 {#odroid-m1}

该镜像包含启动SoC所需的一切，无需使用Hardkernel的Petitboot。但M1会首先从其SPI闪存启动。要直接从SD卡或eMMC启动，请按住恢复按钮。最近的SPI闪存中的Petitboot也会自行找到Home Assistant OS的U-Boot，因此无需按按钮。

要通过SPI闪存从eMMC启动，你需要Petitboot版本20230328或更高。更新方法：

1. 从[Hardkernel的Petitboot镜像](http://ppa.linuxfactory.or.kr/images/petitboot/odroidm1/)下载SPI更新程序和SPI启动镜像。
2. 将更新程序刷入SD卡。
3. 将SPI启动镜像复制到该SD卡的FAT分区，并命名为`spiboot.img`。
4. 从该SD卡启动M1。HDMI输出会显示进度，并在成功时在左上角显示新版本。然后将 Home Assistant OS 刷入 eMMC。NVMe 驱动器不能从中启动，但可以作为 [数据磁盘](/os/operating-system/partitions#data-disk) 使用。

串行控制台位于 CON1 接口，波特率为 1500000。`cmdline.txt` 包含 `console=tty0`，因此 systemd 启动信息会显示在 HDMI 上，而不是在串行控制台上。

## ODROID-M1S {#odroid-m1s}

M1S 会先从 SD 卡启动，再从 eMMC 启动，因此带有 Home Assistant OS 的 SD 卡可以直接使用。即使 eMMC 上仍然保留着出厂加载程序，这也同样有效。

要在 eMMC 上安装，请使用 Hardkernel 的 [UMS 工具镜像](https://wiki.odroid.com/odroid-m1s/getting_started/os_installation_guide#user_installer)。它会将 M1S 转变为一个 USB 大容量存储设备，从而可以通过 Micro USB OTG 端口从电脑闪存 eMMC。

安装 Home Assistant OS 会将 eMMC 上的加载程序替换为主线版本。之后，UMS 工具镜像不再从 SD 卡启动。要恢复 UMS 模式，可以从 Home Assistant OS 主机 shell 将 Hardkernel 的镜像写入 eMMC：

```shell
dd if=/tmp/ODROID-M1S_EMMC2UMS.img of=/dev/mmcblk0
```

设备在下一次启动时无需 SD 卡即可进入 UMS 模式。在另一台电脑上下载镜像：Hardkernel 的下载网站会阻止脚本化下载。然后将其复制到设备，例如使用 `scp`。NVMe 驱动器无法用于启动，但可以作为数据盘使用。14 针扩展接口部分被主线内核支持，包括 UPS 和内部 USB。

串行控制台的波特率为 1500000。像在 M1 上一样，systemd 启动消息会显示在 HDMI 上。
