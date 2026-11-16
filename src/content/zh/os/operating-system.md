---
title: Home Assistant OS
description: Home Assistant OS 是由什么组成的，它如何启动，以及它的存储库是如何组织的。
order: 3
sidebarGroups:
- 指南
- 参考
- 董事会
---



# Home Assistant OS {#home-assistant-os}
Home Assistant OS 是一个 Linux 系统，只有一个任务：运行 Home Assistant。它不是基于像 Debian 或 Ubuntu 这样的发行版。它是用 [Buildroot](https://buildroot.org/) 从源码构建的，每块板子一个镜像，只包含 Home Assistant 需要的内容。

Buildroot 是一个构建系统，而不是发行版。它交叉编译工具链、内核、引导加载程序以及每个软件包，然后将它们组合成一个磁盘镜像。这使它非常适合小型 Arm 板，因为在设备上本地构建会花费很长时间。

## 它里面有什么- **引导加载程序**：UEFI 系统上的 [GRUB](https://www.gnu.org/software/grub/)（x86-64、通用 Arm 和虚拟机），大多数单板计算机上的 [U-Boot](https://docs.u-boot.org/)，以及 Raspberry Pi 5 上固件自带的 tryboot 机制。 {#what-is-in-it}
- **内核**：大多数板卡上的主线 Linux，以及 Raspberry Pi 和 Home Assistant Yellow 上的 Raspberry Pi 分支 Linux。[仓库](https://github.com/home-assistant/operating-system/blob/dev/Documentation/kernel.md) 中的 [`Documentation/kernel.md`] 列出了当前版本。
- **根文件系统**：[EROFS](https://docs.kernel.org/filesystems/erofs.html)，压缩且只读。
- **初始化及服务**：systemd，使用 NetworkManager 进行网络管理，systemd-timesyncd 用于时间同步，BlueZ 用于 Bluetooth。
- **容器**：Docker 引擎，运行 Supervisor 及其管理的所有内容。
- **更新**：[RAUC](https://rauc.io/)，具有两个系统槽位。详见 [更新系统](/os/operating-system/update-system)。
- **安全性**：[AppArmor](https://apparmor.net/) 内核安全模块，为 Supervisor 和应用提供配置文件。

- **内存**：`/var` 和 `/tmp` 使用 ZRAM，数据分区上有一个交换文件。
- **操作系统代理**：位于 [os-agent](https://github.com/home-assistant/os-agent) 仓库中的一个小程序。Supervisor 通过 D-Bus 使用它来执行主机任务，例如移动数据磁盘。

## 启动方式 {#how-it-boots}

1. 引导程序选择一个槽位，A 或 B，并启动其内核和根文件系统。
2. systemd 挂载 overlay 和数据分区，并将持久化文件夹绑定到适当位置。参见 [分区](/os/operating-system/partitions)。
3. `haos-config.service` 导入 `CONFIG` USB 驱动器（如果已插入）。参见 [配置主机](/os/operating-system/configuration)。
4. Docker 启动，`haos-supervisor.service` 启动 Supervisor 容器，`hassio_supervisor`。如果镜像缺失或损坏，该服务会先下载一个新的镜像。
5. Supervisor 使用 RAUC 将槽位标记为可用，并启动其插件、Home Assistant Core 和应用程序。

全新镜像已经包含 Supervisor 及其插件，但不包含 Home Assistant Core。它会附带一个小的起始页面。首次启动时，Supervisor 会下载最新的 Core，因此每个新安装的系统都会使用当前版本。

## 仓库 {#the-repository}

[home-assistant/operating-system](https://github.com/home-assistant/operating-system) 使用了 Buildroot 的 [br2-external 机制](https://buildroot.org/downloads/manual/manual.html#outside-br-custom)：所有与 Home Assistant OS 相关的内容都存放在 Buildroot 外部，在 [`buildroot-external/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external)。Buildroot 本身是 [`buildroot/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot) 中的一个 Git 子模块，指向 [home-assistant/buildroot](https://github.com/home-assistant/buildroot) 的分支。该分支在上游的基础上尽可能少地应用补丁。| 路径 | 内容 |
| --- | --- |
| [`buildroot-external/configs/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs) | 每个构建目标一个 `<target>_defconfig` |
| [`buildroot-external/board/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/board) | 每个板子: [元数据](/os/operating-system/board-metadata)、启动文件、内核配置和钩子 |
| [`buildroot-external/kernel/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/kernel) | 所有板子共享的内核配置片段 |
| [`buildroot-external/package/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/package) | 额外的软件包，例如 `hassio`（预加载 Supervisor）和 `os-agent` |
| [`buildroot-external/rootfs-overlay/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/rootfs-overlay) | 复制到每个镜像中的文件，例如 `haos-*` systemd 单元 |
| [`buildroot-external/genimage/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/genimage) | 磁盘布局，参见 [分区](/os/operating-system/partitions) |
| [`buildroot-external/ota/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/ota) | RAUC 配置、更新清单和证书 |
| `buildroot-external/meta` | 操作系统版本和部署类型 |
| [`scripts/`](https://github.com/home-assistant/operating-system/tree/dev/scripts) | 辅助脚本，例如构建容器的 `enter.sh` |
| [`tests/`](https://github.com/home-assistant/operating-system/tree/dev/tests) | 在 QEMU 中启动镜像的自动化测试 |

## 接下来去哪 {#where-to-go-next}

- [构建镜像](/os/operating-system/build) 以获得一个可用的设置。
- [支持的开发板](/os/operating-system/boards) 列出了所有构建目标。
- [发布和构建](/os/operating-system/releases) 解释了你的更改如何进入发布版本。

## 本节的所有页面 {#all-pages-in-this-section}

### 指南 {#guides}

- [构建镜像](/os/operating-system/build)：设置构建容器并为某个板子构建 Home Assistant OS。
- [测试你的构建](/os/operating-system/test)：在 QEMU 中启动你的镜像，运行自动化测试，并将你的构建安装到真实设备上。
- [配置主机](/os/operating-system/configuration)：使用 CONFIG USB 驱动器或直接在主机的持久化文件夹中修改 Home Assistant OS 的主机设置。
- [配置网络](/os/operating-system/networking)：Home Assistant OS 如何使用 NetworkManager 管理网络，以及如何配置 UI 不覆盖的部分。
- [调试主机](/os/operating-system/debugging)：通过 SSH 或控制台在 Home Assistant OS 上获取 root shell，并找到所需的日志。
- [版本和构建](/os/operating-system/releases)：描述 Home Assistant OS 的更改如何从 pull request 转变为发布版本，包括涉及的分支、版本号和构建流水线。

### 参考资料 {#reference}

- [分区](/os/operating-system/partitions)：Home Assistant OS 的磁盘布局，每个分区的内容，以及数据磁盘功能如何移动数据分区。
- [更新系统](/os/operating-system/update-system)：Home Assistant OS 如何使用 RAUC 和两个启动槽自我更新，软件包如何签名，以及如何安装你自己的构建。
- [板级元数据](/os/operating-system/board-metadata)：每块板的元文件中的变量，以及所有板共享的版本文件。

### 板卡 {#boards}

- [支持的板卡](/os/operating-system/boards)：每个 Home Assistant OS 构建的板卡，包括其构建目标、引导加载程序和机器类型。
- [Raspberry Pi](/os/operating-system/raspberry-pi)：Home Assistant OS 的 Raspberry Pi 相关信息，例如串行控制台、I2C 以及从 USB 启动。
- [ODROID](/os/operating-system/odroid)：Hardkernel ODROID 的Home Assistant OS 相关信息，例如 eMMC 安装、M1 和 M1S 的引导流程以及控制台。
- [通用系统](/os/operating-system/generic)：通用 x86-64 和 aarch64 目标，用于通过 UEFI 启动的 PC 和其他系统。
- [虚拟机](/os/operating-system/virtual-machine)：OVA 目标、它构建的虚拟磁盘格式，以及虚拟机运行 Home Assistant OS 所需的条件。
