---
title: 构建图像
description: 设置构建容器并为一个板构建 Home Assistant OS。
sidebarGroup: 指南
order: 1
---

# 构建图像 {#build-an-image}

Home Assistant OS 在基于 Debian 的容器中构建，该容器拥有 Buildroot 所需的所有工具。你不需要在自己的机器上安装 Buildroot 的依赖项，并且每个贡献者都在相同的环境中构建。

嵌入式 Linux 和 Buildroot 新手？[Bootlin](https://bootlin.com/docs/) 提供的免费培训资料是一个不错的起点。[Buildroot 手册](https://buildroot.org/downloads/manual/manual.html) 是你会不断参考的权威资料。

## 你需要的条件 {#what-you-need}

- 一台安装了 Docker 的 Linux 机器，并且有权限运行特权容器。无根 Docker 不可用：构建过程中会在容器内的循环设备上挂载文件系统镜像。
- 一个具有 `sudo` 的普通用户账户。构建脚本拒绝以 root 身份运行，但某些步骤需要提升权限。
- 磁盘空间和时间。第一次构建会下载并编译所有内容，根据你的机器不同，可能需要一小时或更长时间。

## 获取源代码 {#get-the-source}

该仓库将 Buildroot 作为 Git 子模块引入。使用子模块克隆：

```shell
git clone https://github.com/home-assistant/operating-system.git
cd operating-system
git submodule update --init
```

当你拉取新更改时，也需要更新子模块。Buildroot 会定期更新，如果不匹配会导致令人困惑的构建错误：

```shell
git pull
git submodule update
```

要丢弃你所有的本地更改并回到干净状态：

```shell
git reset --hard
git submodule update --init --force
```

## 为一个板子构建 {#build-for-a-board}

每个构建目标在 [`buildroot-external/configs/`](https://github.com/home-assistant/operating-system/tree/dev/buildroot-external/configs) 中都有一个配置文件，名为 `<target>_defconfig`。将目标名称传给 `make`，不要带上 `_defconfig` 部分。[ `scripts/enter.sh` ](https://github.com/home-assistant/operating-system/blob/dev/scripts/enter.sh) 构建构建容器并在其中运行命令：

```shell
scripts/enter.sh make rpi4_64
```

`make help` 列出所有目标。[支持的板子](/os/operating-system/boards) 解释了每个目标对应哪个板子。

构建输出位于 `output/`。完成的镜像位于 `output/images/`，以板子和版本命名，如 `haos_rpi4-64-18.4.dev0.img.xz`。磁盘镜像旁边是 RAUC 更新包 `.raucb`，可用于更新现有安装。详见 [测试你的构建](/os/operating-system/test)。

下载和编译器缓存保存在仓库之外的 `~/hassos-cache`。将 `CACHE_DIR` 设置到其他位置可修改存储位置。这样后续构建会更快。

## 构建多个目标 {#build-more-than-one-target}

一个输出文件夹对应一个目标。要从同一个检出构建多个板子，请为每个板子提供其自己的输出文件夹，并使用 `O=`：

```shell
scripts/enter.sh make O=output_rpi4_64 rpi4_64
scripts/enter.sh make O=output_ova ova
```

如果你为不同的目标重用输出文件夹，构建系统会发出警告并等待十秒。在这种情况下，先运行 `make distclean`。

## 重新构建软件包 {#rebuild-a-package}

Buildroot 从源代码构建软件包，并记住已经构建过的内容。第二次构建只会重新生成已更改的部分以及最终镜像。要强制重新构建软件包，请删除其构建文件夹：

```shell
rm -rf output/build/linux-custom/
```

不确定镜像中的某个文件来自哪个软件包？`output/build/packages-file-list.txt` 将每个文件映射到它所属的软件包。

## 在构建容器中工作 {#work-inside-the-build-container}

不带参数时，[`scripts/enter.sh`](https://github.com/home-assistant/operating-system/blob/dev/scripts/enter.sh) 会在构建容器中打开一个 shell。从那里，你可以运行相同的构建以及其他 Buildroot 目标：

```shell
scripts/enter.sh
make O=output_rpi4_64 rpi4_64
```

仓库的 `Makefile` 不知道的目标会传递给 Buildroot。例如，要交互式地更改目标配置，然后绘制软件包之间的依赖关系：

```shell
make O=output_rpi4_64 menuconfig
make O=output_rpi4_64 graph-depends
```

运行 `make buildroot-help` 可以查看 Buildroot 提供的所有内容。

## 签名 {#signing}

每次构建都会对其更新包进行签名。第一次构建时，会在仓库根目录创建一个自签名证书和密钥，分别为 `cert.pem` 和 `key.pem`，并将其添加到镜像中的密钥环中。之后的每次构建都会使用同一对证书和密钥。这样，你自己构建的镜像就能接受你后续构建的更新包。[更新系统](/os/operating-system/update-system#security) 中有详细信息。

如果你想继续更新运行你构建的设备，请保留这对证书和密钥。删除它们意味着会生成新的证书，而拥有旧证书的设备将拒绝你新的更新包。
