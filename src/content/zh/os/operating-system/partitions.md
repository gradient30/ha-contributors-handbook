---
title: 分区
description: Home Assistant OS 的磁盘布局、每个分区包含的内容，以及数据磁盘功能如何移动数据分区。
sidebarGroup: 参考
order: 1
---

# 分区 {#partitions}

Home Assistant OS 的磁盘布局与典型的 Linux 系统不同。系统本身被存储了两次，以便安全更新，所有变化的内容都存放在独立的分区上。

## 分区表 {#partition-table}

Home Assistant OS 在可能的情况下使用 GPT 分区表。一些主板的启动固件需要磁盘的第二个块，而 GPT 会在该位置存储其头信息。这些主板会使用混合表，即 GPT 与 MBR 并存，或者使用普通的 MBR 表。[板卡元数据](/os/operating-system/board-metadata) 中的 `PARTITION_TABLE_TYPE` 用于设置使用哪一种。

## 布局 {#layout}

| 分区 | 标签 | 大小 | 内容 |
| --- | --- | --- | --- |
| Boot | `hassos-boot` | 每块板 16 到 64 MB | 引导加载程序文件、`cmdline.txt` 和引导配置 |
| Kernel A | `hassos-kernel0` | 24 MB | 槽 A 的内核 |
| System A | `hassos-system0` | 256 MB | 槽 A 的根文件系统 |
| Kernel B | `hassos-kernel1` | 24 MB | 槽 B 的内核 |
| System B | `hassos-system1` | 256 MB | 槽 B 的根文件系统 |
| Boot state | `hassos-bootstate` | 8 MB | U-Boot 环境，在 U-Boot 板上 |
| Overlay | `hassos-overlay` | 96 MB | 持久化主机设置 |
| Data | `hassos-data` | 剩余磁盘空间 | 容器、Home Assistant、应用程序和用户数据 |带有二级程序加载器（SPL）的板卡也会在磁盘开始位置为其预留空间，位于启动分区之前。大小在 [`buildroot-external/scripts/hdd-image.sh`](https://github.com/home-assistant/operating-system/blob/dev/buildroot-external/scripts/hdd-image.sh) 和板卡元数据中设置。布局本身在 [`buildroot-external/genimage/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/genimage)中。

分区名称保留了旧的 `hassos` 前缀。OS 与 Supervisor 中的许多代码都是通过这些标签来查找分区的。

## 启动分区 {#boot-partition}

一个 FAT 分区，挂载在 `/mnt/boot`。在 UEFI 系统上，它是 EFI 系统分区，包含 GRUB 及其环境文件。在其他板子上，它包含 U-Boot 或 Raspberry Pi 固件文件。它还包含 `cmdline.txt`，在 Raspberry Pi 上，还包含 `config.txt`。

## 内核和系统分区 {#kernel-and-system-partitions}

每个插槽都有一个内核分区和一个系统分区。系统分区存放根文件系统，即只读的压缩 EROFS 镜像。在正常使用中，这两个分区都不会被写入。仅在更新时才会写入，而且只会写入未运行的插槽。见 [更新系统](/os/operating-system/update-system)。

## 覆盖分区 {#overlay-partition}

一个 ext4 文件系统，挂载在 `/mnt/overlay`。它存放需要持久化的主机设置，如网络连接、主机名和 SSH 密钥。在启动时，它们被绑定挂载到 `/etc` 及其他位置。[配置主机](/os/operating-system/configuration#persistent-folders-on-the-host) 列出了这些内容。

## 数据分区 {#data-partition}

一个 ext4 文件系统，挂载在 `/mnt/data`。它存放了除操作系统之外的所有内容：Docker 存储（绑定到 `/var/lib/docker`）、Supervisor 的数据在 `/mnt/data/supervisor`、系统日志以及交换文件。它的读写量最大，因此最能受益于快速存储。

镜像中的数据分区很小。首次启动时，`haos-expand` 会将其扩大以填满磁盘的其余部分。

一个全新的镜像已经在数据分区上包含了 Supervisor 及其插件，但没有 Home Assistant Core。它只有一个小的登录页面。Supervisor 在首次启动时会下载当前的 Core，因此新的安装总是从最新版本开始。

## 数据磁盘 {#data-disk}

用户可以将数据分区移动到另一块磁盘，例如与 SD 卡相邻的 USB SSD。Supervisor 和操作系统代理会准备目标磁盘，并创建一个标记为 `hassos-data-external` 的分区，然后重新启动。

在下一次启动时，`haos-data.service` 使用 `e2image` 将数据分区复制到新磁盘，并将旧分区的标签更改为 `hassos-data-old`。新的分区随后成为唯一带有 `hassos-data` 标签的分区，因此它会被挂载。如果复制失败，新分区会被标记为 `hassos-data-fail`，系统将继续使用旧分区。在全新安装的第一次启动时，`haos-data-disk-detach.service` 会搜索其他磁盘上的 `hassos-data` 分区，例如前一次安装遗留的数据盘。它会将它们重命名为 `hassos-data-dis`，以便新安装不会挂载它们。Home Assistant Yellow 是例外：其第一块 NVMe 磁盘上的数据分区会被保留，并优先于 eMMC 上的分区。
