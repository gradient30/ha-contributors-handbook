---
title: 虚拟机
description: ova目标,它构建的虚拟磁盘格式,以及虚拟机需要运行的Home Assistant OS.
sidebarGroup: 董事会
order: 5
---

# 虚拟机 {#virtual-machines}

`ova`目标为x86-64虚拟机建立Home Assistant OS. 它的棋盘文件在 [`buildroot-external/board/pc/ova/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/board/pc/ova) 中 。 它也是自动测试使用的目标,参见[测试洽谈](/os/operating-system/test).

## 伙计 {#formats}

一个建筑以多种形式产生同样的系统. 虚拟磁盘为32 GB.

| 格式 | 文件 | 对于 |
| --- | --- | --- |
| 奥瓦 | `.ova` | 导入为完整的虚拟机, 如 VMwareũ或 VirtualBox |
| VMDK 维基百科 | `.vmdk.zip` | VMware, 虚拟框 |
| VHDX 软件 | `.vhdx.zip` | 超强 五 |
| 自愿DI | `.vdi.zip` | 虚拟框 |
| QCOW | `.qcow2.xz` | QEMU、在处理 KVM、 Proxmox |

## 所需经费 {#requirements}

- UEFI脚。 遗产BIOS靴子不起作用。
- 一种64位的Linux宾客类型,内核4.x或较晚.
- 至少2个虚拟CPU和2GB的内存. 更多的帮助。
- 网络适配器.

图像包括常见的超卫视的嘉宾工具,如QEMU嘉宾代理和Hyper-V守护进程.

## 溶液 {#consoles}

控制台在虚拟屏幕上显示,并在第一个串行端口`ttyS0`上显示. GRUB 启动菜单允许您选择一个插槽或救援 shell, 见 [调试主机](/os/operating-system/debugging#rescue-shell) 。
