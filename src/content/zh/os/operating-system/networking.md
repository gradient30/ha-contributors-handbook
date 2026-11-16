---
title: 配置网络
description: 如何 Home Assistant OS 使用 NetworkManager 管理网络，以及如何配置 UI 未涵盖的内容。
sidebarLabel: 配置网络
sidebarGroup: 指南
order: 4
---

# 配置网络 {#configure-networking}

Home Assistant OS 使用 [NetworkManager](https://networkmanager.dev/) 来管理主机网络。开箱即用时没有任何连接配置文件：NetworkManager 会自动连接有线接口，IPv4 使用 DHCP，IPv6 使用自动配置。

## 三种配置方式 {#three-ways-to-configure-it}

1. **图形界面（UI）**：在 **设置** > **系统** > **网络** 下。大多数用户不需要其他方式。
2. **命令行界面（CLI）**：`ha network` 涵盖了图形界面所做的功能，以及更多功能，例如 VLAN。
3. **直接使用 NetworkManager**：`CONFIG` USB 驱动器上的连接文件，或主机上的 `nmcli`。用于前两种方式不支持的任何操作。

当你通过图形界面或命令行修改设置时，Supervisor 会更新该接口的活动连接配置文件。如果没有，它会创建一个名为 `Supervisor <interface>` 的配置文件，如 `Supervisor eth0`。因此，你自己编写的配置文件以后可以由用户通过图形界面修改。

## 使用命令行界面 {#with-the-cli}

`ha network info` 列出接口。`default` 是主接口的快捷方式。要将其改回 DHCP：

```shell
ha network update default --ipv4-method auto
```

一个静态 IPv4 地址：

```shell
ha network update eth0 --ipv4-method static \
  --ipv4-address 192.168.1.10/24 --ipv4-gateway 192.168.1.1 \
  --ipv4-nameserver 192.168.1.1
```

Wi-Fi 也可使用，在具有 Wi-Fi 的开发板上。 有线连接更可靠，因此如果可能，建议使用有线连接：

```shell
ha network update wlan0 --ipv4-method auto \
  --wifi-mode infrastructure --wifi-ssid "My network" \
  --wifi-auth wpa-psk --wifi-psk "My password"
```

对每个选项运行 `ha network update --help`。

## 使用连接文件 {#with-connection-files}

NetworkManager 从 `/etc/NetworkManager/system-connections` 读取其 keyfile 格式的连接配置文件，这些文件是持久的。你可以在主机 shell 上将文件放在那里，或者将它们放入 [CONFIG USB 驱动器](/os/operating-system/configuration#the-config-usb-drive) 的 `network/` 文件夹中。该驱动器会用自己的配置替换所有现有的连接。

只支持连接文件。不支持对 `NetworkManager.conf` 本身的更改，它是只读镜像的一部分。[NetworkManager 设置参考](https://networkmanager.dev/docs/api/latest/nm-settings-keyfile.html) 记录了每个选项。

为每个连接分配自己的 UUID，只生成一次，就像 `uuidgen` 中一样。没有固定 UUID，连接会改变身份，并且每次启动后可能获得不同的地址。请使用 Unix 换行符 (LF) 保存文件。

### 有线连接，使用 DHCP {#wired-with-dhcp}

```ini
[connection]
id=my-network
uuid=d55162b4-6152-4310-9312-8f4c54d86afa
type=ethernet

[ipv4]
method=auto

[ipv6]
addr-gen-mode=stable-privacy
method=auto
```

### 静态 IPv4 地址 {#static-ipv4-address}

替换 `[ipv4]` 部分：

```ini
[ipv4]
method=manual
address1=192.168.1.111/24,192.168.1.1
dns=192.168.1.1;
```

`address1` 是带有前缀长度的地址，然后是网关。

### 带 WPA 的 Wi-Fi {#wi-fi-with-wpa}

```ini
[connection]
id=my-wifi
uuid=72111c67-4a5d-4d5c-925e-f8ee26efb3c3
type=wifi

[wifi]
mode=infrastructure
ssid=MY_SSID
# Uncomment when the network does not broadcast its name {#uncomment-when-the-network-does-not-broadcast-its-name}
# hidden=true {#hiddentrue}

[wifi-security]
auth-alg=open
key-mgmt=wpa-psk
psk=MY_PASSWORD

[ipv4]
method=auto

[ipv6]
addr-gen-mode=stable-privacy
method=auto
```

Home Assistant OS 默认关闭 Wi-Fi 省电功能。要为某个连接开启它，请在其 `[wifi]` 部分添加 `powersave=3`。

## 在主机上使用 nmcli {#with-nmcli-on-the-host}

在主机终端中，`nmcli` 会显示所有的 NetworkManager。`nmcli con show` 列出配置文件。例如，要在名为 `Supervisor eth0` 的配置文件上设置静态地址：

```shell
nmcli con mod "Supervisor eth0" ipv4.method manual \
  ipv4.addresses 192.168.1.10/24 ipv4.gateway 192.168.1.1 \
  ipv4.dns 192.168.1.1
nmcli con up "Supervisor eth0"
```

如果还没有配置文件，可以用 `nmcli con add` 创建一个，或者先通过 CLI 设置一次接口。

## 重置网络 {#reset-the-network}

要丢弃所有连接配置文件并恢复默认设置，在主机终端中删除它们并重启：

```shell
rm -r /mnt/overlay/etc/NetworkManager/system-connections/*
reboot
```

## 值得了解的默认设置 {#defaults-worth-knowing}

这些大多数来自图像中的 `NetworkManager.conf`：

- 每个连接都会启用 mDNS 和 LLMNR，因此系统会响应 `homeassistant.local`。
- NetworkManager 每 10 分钟检查一次连通性，针对 `checkonline.home-assistant.io`。
- Docker 的桥接和虚拟接口不由 NetworkManager 管理。
- DHCP 服务器公告的时间服务器会通过 NetworkManager 调度脚本 `10-ntp` 传递给 systemd-timesyncd。
