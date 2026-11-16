---
title: 调试主机
description: 通过 SSH 或控制台在 Home Assistant OS 上获取 root shell，并找到你需要的日志。
sidebarLabel: 调试主机
sidebarGroup: 指南
order: 5
---

# 调试主机 {#debug-the-host}

要调试操作系统，您需要在主机本身上使用 shell，而不是在容器内。本页展示了进入的方式，以及一旦到达后应该查看的位置。

> [!重要]
> 这是面向开发者的。希望使用终端的用户应改用 **Terminal & SSH** 应用。该应用在具有受限权限的容器中运行。本页内容会为您提供对主机的完整 root 访问权限，而对以这种方式更改的系统无人可提供支持。

## 22222 端口上的 SSH {#ssh-on-port-22222}

Home Assistant OS 为开发者提供了 SSH 服务器 [Dropbear](https://matt.ucc.asn.au/dropbear/dropbear.html)，运行在 22222 端口。它与任何 SSH 应用程序是分开的，只有当 root 至少有一个授权密钥时才会运行。不支持密码登录。

### 添加你的密钥 {#add-your-key}

1. 如果你还没有 SSH 密钥，请使用 `ssh-keygen -t ed25519` 创建一个。GitHub 的 [生成新的 SSH 密钥](https://docs.github.com/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) 指南涵盖了所有操作系统。
2. 将 USB 驱动器格式化并命名为 `CONFIG`，请参阅 [CONFIG USB 驱动器](/os/operating-system/configuration#the-config-usb-drive)。
3. 在驱动器根目录下创建一个名为 `authorized_keys` 的文件，不带扩展名。将你的*公钥*放入其中，文件内容以 `.pub` 结尾，每行一个密钥。使用 Unix 换行符（LF），并使用纯 ASCII。
4. 将驱动器插入设备，并运行 `ha os import`，或在驱动器插入的情况下重启。

自 Supervisor 2026.09.0 起，Supervisor API 也可以管理这些密钥，使用 `/os/ssh/authorized_keys` 端点。请参阅 [Apps](/apps) 区域的 Supervisor API 参考。

### 连接 {#connect}

```shell
ssh root@homeassistant.local -p 22222
```

更改了主机名，或者您的网络上没有 mDNS？请改为使用设备的 IP 地址。

### 再次关闭 {#turn-it-off-again}

导入一个 *没有* `authorized_keys` 文件的 `CONFIG` 驱动器。导入会删除所有密钥并停止 SSH 服务器。通过 API，`/os/ssh/authorized_keys` 上的 `DELETE` 会删除 root 的所有授权密钥。

## 本地控制台 {#the-local-console}

在屏幕和键盘上，或在虚拟机控制台上，设备会显示 Home Assistant CLI，`ha >`。输入 `login` 可获得主机的 root shell。

如果 CLI 在三分钟内未启动，或者在等待时按下 <kbd>Ctrl</kbd> <kbd>C</kbd>，则会进入紧急 shell。当 Supervisor 未启动时，这是进入的方法。

## 串行控制台 {#serial-console}

许多开发板也有串行控制台。它显示启动信息，并给你一个登录提示：以 `root` 登录，无需密码。

控制台在启动分区的 `cmdline.txt` 中设置。各板的默认值如下：

| 开发板 | 串行控制台 |
| --- | --- |
| Home Assistant Green | `ttyS2`，1500000 波特率 |
| Home Assistant Yellow | `ttyAMA2`，115200 波特率 |
| ODROID-C2、ODROID-C4、ODROID-N2、Khadas VIM3 | `ttyAML0`，115200 波特率 |
| 通用 aarch64、虚拟机 | `ttyS0` |内核将其消息写入 `cmdline.txt` 中的每个控制台，但 systemd 启动消息只会发送到最后列出的那个。在每块带屏幕的板子上，这是 `console=tty0`，所以它们会显示在屏幕上。Home Assistant Yellow 没有 HDMI 端口，所以它将串口控制台列在最后。要在其他板子的串口控制台上查看启动消息，请将其 `console=` 条目移动到行末。在表中没有列出的板子上，请自行添加串口控制台，参见 [板子页面](/os/operating-system/boards)。

## 救援 shell {#rescue-shell}

在带有 GRUB（通用 x86-64、通用 aarch64 和虚拟机）的主板上，启动菜单为每个槽位提供一个救援 shell 选项。它会将系统引导到 systemd 的恢复目标，并输出调试信息。当系统无法启动到控制台时非常有用。

## 日志 {#logs}

日志存储在数据分区上，因此可以在重新启动后保留。在主机 shell 上：

```shell
# The service that starts the Supervisor {#the-service-that-starts-the-supervisor}
journalctl -u haos-supervisor -f

# The Supervisor itself {#the-supervisor-itself}
docker logs -f hassio_supervisor

# Home Assistant Core {#home-assistant-core}
docker logs -f homeassistant

# Everything, newest last {#everything-newest-last}
journalctl -e
```

没有主机访问权限时，CLI 也显示大部分内容：`ha supervisor logs`、`ha core logs` 和 `ha host logs`。添加 `--help` 可以查看选项，例如选择启动项。

## 查看容器内部 {#look-inside-a-container}

系统的每个部分都是一个 Docker 容器。要在某个容器中打开 shell：

```shell
docker ps
docker exec -it homeassistant /bin/bash
```

[Supervisor 概述](/os/supervisor#what-the-supervisor-runs) 列出了容器及其名称。
