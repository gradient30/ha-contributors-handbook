---
title: 更新系统
description: Home Assistant OS如何更新自己与RAUC和两个启动插槽, 如何签名捆绑, 以及如何安装自己的构建 。
sidebarGroup: 参考
order: 2
---

# 更新系统 {#the-update-system}

Home Assistant OS 以 [乌拉圭](https://rauc.io/) 更新, 一个基于图像的更新系统, 用于嵌入式 Linux 。 更新不会更改运行中系统上的文件 。 它将一个完整的新内核和根文件系统写入未运行的插槽,并穿插其中. 如果这不起作用,设备会回到它来自的插槽.

[RAUC 文档](https://rauc.readthedocs.io/)解释RAUC本身。 此页面覆盖 Home Assistant OS 如何使用 。

## Update bundles {#update-bundles}

每个建筑都会为新安装产生磁盘映像,而RAUC更新捆绑,一个`.raucb`文件,用于现有的设备. 两者均由同一分区图像制成. 一个捆绑包含:

- 启动分区内容
- 内核图像
- 根文件系统
- 的主要内容

显示模板 [`buildroot-external/ota/manifest.raucm.gtpl`](https://github.com/home-assistant/operating-system/blob/dev/buildroot-external/ota/manifest.raucm.gtpl) 定义了内容 。 每块板子都一样 捆绑的`compatible`值是`haos-<board id>`,就像`haos-rpi4-64`,所以捆绑只安装在它为之建造的板上.

启动分区不是 A/B 计划的一部分: 更新将其写入 。 更新钩子 `buildroot-external/ota/rauc-hook` 将 `.txt` 文件保存在它上, 如 `cmdline.txt` 和 `config.txt`, 所以用户会更改这些幸存的更新 。

## 更新如何运行 {#how-an-update-runs}

实情如下: RAUC作为系统服务运行,并提供D-Bus API. 在正常使用中, Supervisor 驱动它 :

1. Supervisor下载新版本的捆绑 。
2. 它要求RAUC在D-Bus上空安装. 对于RAUC来说,这是从一个文件中获取的本地安装.
3. RAUC 写不活跃的插槽, 并告诉卸货者 尝试该插槽下一步。
4. 更新现已安装, 但未激活 。的支持率为: 2017年1月1日 - 2017年1月1日 - 2017年1月1日 - 2017年1月1日 - 2017年1月1日 - 2017年1月1日 - 2017年1月1日 - 2017年1月1日 - 2017年1月1日 - 2017年1月1日 - 2017年1月1日 - 2017年1月1日 - 2017年1月1日 - 2017年1月10日 - 2017年1月1日 - 20: 它本身不会重启。
5. 用户,或者任何开始更新的东西, 重新输入系统, 它会跳入新的插槽。
6. 一旦 Supervisor 开始, 它标志 启动的插槽是好的 。

也可以在主机壳上用手做同样的事情. 要安装捆绑, 要安装 shell , 请参见 [调试主机](/os/operating-system/debugging) :

```shell
cd /mnt/data
REPO=https://github.com/home-assistant/operating-system
curl -LO "$REPO/releases/download/18.3/haos_rpi4-64-18.3.raucb"
rauc install haos_rpi4-64-18.3.raucb
systemctl reboot
```

> [!NOTE]
> 在Raspberry Pi 5上,总是用`systemctl reboot`重启. 它将新插槽与固件的 tryboot 机制,它需要通过`systemctl reboot`的重启参数. 平原 `reboot` 重新开始旧位置 。

## 启动插槽 {#boot-slots}

塞族人有2个名额,A和B。 新安装的名额只有A。 第一次更新到B,第二次更新到A,等等.

`ha os info` 显示正在运行的槽 。 在主机外壳上, `rauc status` 显示全景 :

```text
=== System Info ===
Compatible:  haos-rpi4-64
Booted from: kernel.0 (A)

=== Slot States ===
x [kernel.0] (/dev/disk/by-partlabel/hassos-kernel0, raw, booted)
        bootname: A
        boot status: good
    [rootfs.0] (/dev/disk/by-partlabel/hassos-system0, raw, active)

o [kernel.1] (/dev/disk/by-partlabel/hassos-kernel1, raw, inactive)
        bootname: B
        boot status: good
    [rootfs.1] (/dev/disk/by-partlabel/hassos-system1, raw, inactive)
```

更新后,新装机尝试了有限的次数,三次在GRUB上. 如果它从来没有被标记为好, 卸货机掉回另一个插槽。 如何运作取决于装货机:

- ** GRUB** 保留其环境文件中的槽顺序和尝试, `EFI/BOOT/grubenv` 在启动分区上. 它的靴子菜单也让你用手选择一个插槽.
- **U-Boot** 使它们留在环境里,在`hassos-bootstate`分区上。
- **Raspberry Pi 5**通过自定义的RAUC后端使用固件的尝试启动机制.

要切换自己的槽,请使用`ha os boot-slot A`或`ha os boot-slot B`. 选中的插槽会保留默认值, 直到您再次更改它, 或者更新它 。

## 安全 {#security}

更新捆绑是签名的,RAUC在安装任何设备之前,对`/etc/rauc/keyring.pem`中的密钥环进行签名检查. Home Assistant OS拥有自己的公钥基础设施,拥有开发与发行证书权限. 所有公共建筑均由发布链签名.

图像信任的证书取决于其[将与](/os/operating-system/releases#deployment-types) :

- ** 制作和装配** 图像相信发放证书当局。
- ** 开发** 图像信任开发和发行证书当局。

除此之外,您所构建的每个图像都信任您自己签名的证书,在寄存器的根部是`cert.pem`. 见[建立图像](/os/operating-system/build#signing). 因此,你所建的图像接受你后期建筑的捆绑,仍然接受官方发布.

### 其目的在于安装自签名的构建 {#install-a-self-signed-build}

官方安装不信任您的证书 。 安装您的捆绑失败 :

```text
LastError: signature verification failed: Verify error:self signed certificate
```

Home Assistant OS虽然没有被锁定。 通过主机上的根,您可以将您的证书添加到当前启动的密钥环中. 将 `cert.pem` 从您的寄存器根复制到设备上的 `/mnt/data` :

```shell
cp -r /etc/rauc/ /tmp/rauc
cat /mnt/data/cert.pem >> /tmp/rauc/keyring.pem
mount -o bind /tmp/rauc/ /etc/rauc/
systemctl restart rauc
rauc install /mnt/data/haos_rpi4-64-18.4.dev0.raucb
```

绑定的挂载在重启后就消失了 但你的建筑在自己的密钥环里有你的证书 从那时起,设备接受你的后期构建, 官方发布太, 所以你可以随时更新到发布。
