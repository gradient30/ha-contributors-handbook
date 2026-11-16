---
title: 测试你的构建
description: 在 QEMU 中启动你的镜像，运行自动化测试，并将你的构建安装到真实设备上。
sidebarGroup: 指南
order: 2
---

# 测试你的构建 {#test-your-build}

完成的建筑物不是起作用的建筑物。 在打开 pull request 之前, 请启动您的图像 。 对于大多数变化来说,虚拟机器就足够了. 对于棋盘特定更改,你需要棋盘.

## 在QEMU启动 {#boot-it-in-qemu}

`ova`目标为虚拟机构建图像,包括一个压缩的QCOW2图像,QEMU一旦解开就会运行. `--keep` 将压缩文件留在原位上, 因为下面的自动测试再次打开它 。 Home Assistant OS需要UEFI,所以QEMU也需要UEFI的固件. 在Debian和Ubuntu上,`ovmf`包提供了它.

```shell
scripts/enter.sh make O=output_ova ova
unxz --keep output_ova/images/haos_ova-*.qcow2.xz
```

那就开始吧 固件文件的路径因分发而异, 所以检查您的 `ovmf` 包放在哪里 :

```shell
IMAGE=output_ova/images/haos_ova-18.4.dev0.qcow2
FIRMWARE=/usr/share/OVMF/OVMF_CODE.fd

qemu-system-x86_64 -enable-kvm -name haos -smp 2 -m 2G \
  -drive file="$IMAGE",if=virtio,format=qcow2 \
  -drive file="$FIRMWARE",if=pflash,format=raw,readonly=on
```

靴子结束于 Home Assistant CLI 迅速, `ha >` 。 键入 `login` 以获取主机上的根 shell 。

在Arm机上,使用`generic_aarch64`目标. 在它的磁盘图像旁边,它为Arm虚拟机构建了QCOW2,VMDK,以及VDI图像.

## 运行自动测试 {#run-the-automated-tests}

[`tests/`](https://github.com/home-assistant/operating-system/tree/dev/tests) 文件夹有在QEMU中启动 OVA 图像的测试, 并检查系统和 Supervisor 出现 。 它们使用[拉格丽德](https://labgrid.readthedocs.io/)和pytest. 测试设置预计图像为 `tests/haos.qcow2`, 而 OVMF 固件为 `/usr/share/ovmf/OVMF.fd` :

```shell
unxz -c output_ova/images/haos_ova-*.qcow2.xz > tests/haos.qcow2
tests/run_tests.sh
```

除非您已经在 Python 工作 虚拟环境,脚本在`tests/venv`中创建一个,并将测试依赖性安装到其中. 同样的测试在CI中运行,在每次发行都建立和在pull request上使用`run-ova-test`标签.

## 在设备上安装您的构建 {#install-your-build-on-a-device}

你可以像任何发行版一样,将磁盘图像闪到SD卡或磁盘上. 为了保存现有安装的数据,安装RAUC更新捆绑.

> [!IMPORTANT]
> 正式发行只信任发行证书签名的捆绑. 您的构建用您自己签名的证书签名, 因此安装失败, 并有签名错误 。 [其目的在于安装自签名的构建](/os/operating-system/update-system#install-a-self-signed-build) 显示如何让设备接受它 。

一旦设备接受您的证书, 将 `.raucb` 文件复制到设备上, 然后在主机 shell 上运行( 见 [调试主机](/os/operating-system/debugging) ):

```shell
cd /mnt/data
rauc install haos_rpi4-64-18.4.dev0.raucb
systemctl reboot
```

设备重新进入刚刚写好的插槽. 如果那个槽不启动,它会掉到另一个。 见[更新系统](/os/operating-system/update-system).

## 使用 26. 开发 {#use-a-development-build}

你并不总是需要建立自己。 `dev`分支的开发建设发布在[只是为了保护自己](https://os-artifacts.home-assistant.io/index.html)上. 它们是由与释放物相同的编撰的整个管道所建造和签署的,所以你可以尝试一个最近合并的改变,而不建立一个建筑. 解释它们是如何制造的。
