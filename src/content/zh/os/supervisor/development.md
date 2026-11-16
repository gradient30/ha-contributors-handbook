---
title: 搭建开发环境
description: 运行 Supervisor 从源头运行在它的开发容器, 运行测试和linters, 并尝试您的构建在一个真正的系统上 。
sidebarLabel: 开发环境
sidebarGroup: 指南
order: 1
---

# 建立发展环境 {#set-up-a-development-environment}

Supervisor 拥有一个运行完整系统的开发容器: 您的Supervisor, Home Assistant Core, 插件, 和应用程序, 都在您的机器上的一个 Docker 容器内 。 对于大多数变化,这就是你所需要的。

## 设置开发是与 {#set-up-the-development-container}

您需要 [插头](https://docs.docker.com/get-docker/), [视觉工作室代码](https://code.visualstudio.com/) 与 Dev 容器扩展, [图形](https://git-scm.com/) 。 [核心发展环境](/core/development/environment)指南解释了如何在每个操作系统中安装它们. 在Windows上,在WSL2内部工作.

1. [叉 Supervisor 仓库](https://github.com/home-assistant/supervisor/fork),并克隆你的叉子。
2. 在 Visual Studio 代码中打开文件夹, 并选择 ** 在容器中重新打开 ** 。

集装箱运行特权,内部有自己的Docker引擎. 这就是它运行一个完整的Supervisor系统的原因。 设置安装了 Python 的依赖和预承诺钩.

## 运行 Supervisor {#run-the-supervisor}

打开命令调色板, 选择 ** 任务: 运行任务 **, 然后是 ** Run Supervisor 。 任务从工作副本中创建 Supervisor 图像, 并在容器内以 `hassio_supervisor` 开始 。 第一个开始下载Home Assistant Core和插件,需要一段时间.

| 地址 | 什麽? |
| --- | --- |
| `http://localhost:9123` | Home Assistant Core |
| `http://localhost:7357` | 观察员 |

** Run Supervisor CLI** 任务打开 `ha` 命令行对准您的 Supervisor 。 更改后再次运行 ** Run Supervisor: 它以您代码的新图像重新启动 Supervisor 。

开发容器遵循`dev`频道,因此Core和插件是最新的开发版本. 从源头构建的 { 我叫 Supervisor 有 `9999.09.9.dev9999` 的版本, 并且从来没有尝试更新自己 。

## 测试和穿孔 {#tests-and-linters}

测试对Docker,D-Bus,以及网络进行嘲讽,因此它们到处运行,没有运行Supervisor. 他们住在[`tests/`](https://github.com/home-assistant/supervisor/tree/main/tests),布局与[`supervisor/`](https://github.com/home-assistant/supervisor/tree/main/supervisor)相同:

```shell
pytest -qsx tests/resolution/
```

将新测试写入 plain `test_` 用 pytest 固定装置的函数 。 [`tests/conftest.py`](https://github.com/home-assistant/supervisor/blob/main/tests/conftest.py)提供了被嘲笑的`CoreSys`, 以及更多。

在您承诺之前, 运行线条和类型检查器 :

```shell
ruff check --fix supervisor tests
ruff format supervisor tests
pylint supervisor tests
mypy --ignore-missing-imports supervisor/
```

或将空闲的空闲的空闲的空闲的空闲的空闲的空闲的塞族人的空闲的空闲的

## 守则公约 {#code-conventions}

该寄存器对贡献者有自己的指令, 在 [`.github/copilot-instructions.md`](https://github.com/home-assistant/supervisor/blob/main/.github/copilot-instructions.md) 。 最重要的几个:

- 呱
- 的确使用来自 [`supervisor/const.py`](https://github.com/home-assistant/supervisor/blob/main/supervisor/const.py) 的常数, 或模块的 `const.py`, 而不是字数 。
- 通过`self.sys_*`到达系统的其他部分,参见[结构](/os/supervisor/architecture).
- 提高 [`supervisor/exceptions.py`](https://github.com/home-assistant/supervisor/blob/main/supervisor/exceptions.py) 的例外, 用 `from` 链条 。
- 在新代码和注释中说"app",而不是"add-on". 仅保留1个现有1个发展中国家和转型期经济国家或1个类别仍在使用它的地方。

## 测试真实系统 {#test-on-a-real-system}

有些事物只显示在真实的硬件上:一个板状特定的D-Bus API,一个磁盘,一个USB设备. 要在 Home Assistant OS 设备上运行您的 Supervisor :

1. 在设备上, 查找带有 `ha info` 的架构 : `amd64` 或 `aarch64` 。
2. 在你的信心电脑上,为这个架构构建一个图像,并把它推向一个您能够从中提取的注册,比如GitHub容器注册:

```shell
   docker build --platform linux/arm64 --push \
     --tag ghcr.io/YOUR_GitHub_USERNAME/aarch64-hassio-supervisor:dev .
   ```

   Docker调用架构 `linux/amd64` 和 `linux/arm64` 。 图像名称 那么你会用到 Home Assistant 的名字 `amd64` 和 `aarch64` 。

3. 在设备上,切换到 `dev` 通道, 所以 Supervisor 不用稳定释放来替换您的构建 :

```shell
   ha supervisor options --channel dev
   ```

4. 在主机外壳上,请见[调试主机](/os/operating-system/debugging),拉动您的图像,并标记为OS启动的图像 :

```shell
   docker pull ghcr.io/YOUR_GitHub_USERNAME/aarch64-hassio-supervisor:dev
   docker tag ghcr.io/YOUR_GitHub_USERNAME/aarch64-hassio-supervisor:dev \
     ghcr.io/home-assistant/aarch64-hassio-supervisor:latest
   ```

5. 重新启动 Supervisor 服务,并跟踪其输出 :

```shell
   systemctl restart haos-supervisor
   journalctl -fu haos-supervisor
   ```

服务看到图像有变化,并从中创建了一个新的 Supervisor 容器 。

GitHub 容器注册簿上的图像默认是私有的 。 要么在设备上登录 `docker login ghcr.io` , 要么在 GitHub 的设置中公开软件包 。

## 打开 pull request {#open-a-pull-request}

在 [Home Assistant/监督员](https://github.com/home-assistant/supervisor) 的 pull request 上打开您的 `main` , 并填写模板 。 对于大的变化,首先在一个问题中讨论方法。

如果您更改了 API, pull request 模板也要求:

- pull request 到[简历](https://github.com/home-assistant/cli) 寄存器, 如果`ha` 命令需要的话 。
- A pull request 到 [Python 客户端库](https://github.com/home-assistant-libs/python-supervisor-client), 核心使用 。
- 在 Apps 区域[Supervisor API](/apps/supervisor-api) 引用中更新的文件 。

## Supervisor 如何释放 {#how-the-supervisor-is-released}

1. 拉请求合并为`main`.
2. 虞 – 合并均建并发布到 `dev` 频道 。
3. 发布会发布一个版本,比如`2026.10.1`,到`beta`频道.
4. 一旦它证明了自己,版本寄存器中的[稳定。](https://github.com/home-assistant/version/blob/master/stable.json)就会更新,稳定的系统会把它捡起来.
