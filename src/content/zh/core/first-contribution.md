---
title: 您的首次贡献为核心
description: 设置开发环境, 找到小东西来修复, 然后打开您的第一个 pull request 到 Home Assistant Core 。
sidebarLabel: 你的第一次贡献
order: 1
---

# 您的首次贡献为核心 {#your-first-contribution-to-core}

您的第一个 pull request 到核心 不需要很大 。 一个小的bug修复,一个缺失的测试,或者一个日志信息中的打字是一个完美的开始. 重要的是你通过整个循环一次:环境,变化,测试,pull request和审查. 之后,其他一切更是一样.

计划一个晚上的设置。 第一次建造开发容器需要一段时间,你只需要做一次.

## 要求对你好 {#1-say-hi}

加入 [Home Assistant Discord](https://www.home-assistant.io/join-chat/) 。 在 **Channels & Locations ** 下,选择 ** I 想要为 Home Assistant 贡献 dev 技能来查看开发的渠道. 一般发展问题,如一体化是否属于核心,适合[发展中国家**](https://discord.com/channels/330944238910963714/554842238073700352). 当您卡在代码上, 请在 [编码支持**](https://discord.com/channels/330944238910963714/1257019582112334014) 中启动一条线程 。 您不需要允许开始, 但是它帮助您知道哪里可以问 当你被卡住。

## 选择环境 2. {#2-set-up-your-environment}

最快速的方式是开发容器:Visual Studio Code和Docker给您一个使用右 Python 版本的准备环境,所有依赖,以及linters.

1. 安装 [插头](https://docs.docker.com/get-docker/)、[视觉工作室代码](https://code.visualstudio.com/) 和[图形](https://git-scm.com/) 。
2. [叉芯存储器](https://github.com/home-assistant/core/fork) on GitHub.
3. 切开你的叉子 用视觉工作室代码打开:

```shell
   git clone https://github.com/YOUR_GitHub_USERNAME/core
   cd core
   git remote add upstream https://github.com/home-assistant/core.git
   code .
   ```

4. 当Visual Studio代码询问时,选择**在容器中重新打开**. 第一个建筑需要几分钟。
5. 打开命令调色板,选择**任务:运行任务**,然后**Run Home Assistant Core。 一旦输出平静下来,在您的浏览器中打开`http://localhost:8123` 。 您应该看到您自己的开发实例的登机屏幕。

在Windows上,在WSL2内部做这个. [发展环境](/core/development/environment) 指南有细节, 如果您不愿使用容器, 则要手动设置 。

## 寻找工作 {#3-find-something-to-work-on}

不错的地方找:

- 在核心寄存器中标注为 [不错的第一期](https://github.com/home-assistant/core/labels/good%20first%20issue) 的问题 。 并非总有很多,因此,如果名单很短,就不用担心。
- 你遇到的虫子,你使用的整合。 你已经知道如何复制它了 你可以用自己的设备来测试它
- 您使用的集成, 很少测试或缺少类型提示 。 测试是受欢迎的第一贡献,它们教你如何实现融合.

在开始前, 请检查是否有其他人为同一问题打开了 pull request 。 如果这个问题是旧的,你正在研究的评论可以避免双重工作。

## 做改变 {#4-make-the-change}

从 Home Assistant 的最新 `dev` 分支开始为您的更改创建分支 。 从不直接使用 `dev` :

```shell
git fetch upstream
git checkout -b fix-sensor-unit upstream/dev
```

### 查找代码 {#find-the-code}

每个集成都生活在自己的文件夹中,以它的[域名](/glossary/domain)命名:`homeassistant/components/<domain>/`. 它的测试在`tests/components/<domain>/`。 域名是集成文档页面地址的最后一部分. 飞 飞 P P P P P P - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

不知道哪个文件做什么? 解释他们, 和[如何融入](/core/integrations/concepts)解释他们背后的想法。

### 运行它 {#run-it}

以 ** Run Home Assistant Core 任务启动您的开发实例, 如步骤 2 。 它使用您退出的 `config/` 文件夹中的配置, 所以它与您的 Home Assistant 分开 。 添加您正在 ** 安排** > 下的整合 ** Devices & Services**,用户的方式。

Home Assistant 启动时装入您的代码 。 更改后, 从命令调色板中选择 ** 任务: 重新启动运行任务 ** 。 要通过代码,请按<kbd>F5</kbd>在调试器中启动Home Assistant,并设置断点。 见[调试](/core/development/environment#debugging).

### 打开调试日志 {#turn-on-debug-logging}

大多数集成记录他们在调试级别上所做的. 您的环境设置在 غ `logger` 中增加了 `logger` 区域 `config/configuration.yaml` 。 在 `logs` 下添加您的集成和它使用的库 :

```yaml
logger:
  default: info
  logs:
    homeassistant.components.hue: debug
```

库日志名列在 `loggers` 整合的 `manifest.json` 中 。 重新启动Home Assistant,调试消息出现在任务终端中. 您也可以打开来自 UI 的调试日志: 在整合的页面上, 打开三个点菜单并选择 ** Enable 调试日志 **.

### 到达自己的设备 {#reach-your-own-devices}

要复制一个bug,你往往需要真正的设备. 开发容器运行于多克,与多克的默认旷编网络:它不直接在您的家用网络上.

- 在容器中 Home Assistant 可以通过您的 IP 地址连接到您的网络上的设备 。 在添加集成时,输入设备的IP地址.
- 发现通常在容器内不起作用.冗余的Zeroconf和SSDP依靠多播,而多克的默认网络没有通过,所以用手加入设备.
- 设备可以通过您的计算机到达Home Assistant 。 容器发布端口8123,所以一个将数据推向Home Assistant的设备使用您的计算机的IP地址,比如`http://192.168.1.10:8123`. 它还在UDP上发布5683号港口,用于舍利一体化.
- USB棒和Bluetooth适配器只能通过一个Linux主机传递到容器. 在Windows和macOS上,容器不能直接访问该硬件.

在Windows上,容器在WSL2内部运行. 如果您的设备或浏览器无法到达, 请查看 [WSL 网络](/core/development/environment#networking-in-wsl) 。

### 试试看 {#test-it}

保持小的改变,专注于一件事。 然后进行你改变的整合测试:

```shell
pytest tests/components/YOUR_INTEGRATION
```

如果修复一个错误,添加一个没有修复的测试失败,并随它通过. 将如何使这些“或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或数或,使或数或数或数或,使或或

## 我以前说过的 {#5-commit-and-push}

犯规时自动运行 如果他们更改一个文件,请添加提交其并再次承诺.

```shell
git add .
git commit -m "Fix unit of the energy sensor in Example"
git push -u origin HEAD
```

`-u` 使您叉上的分支成为此分支的默认值 。 没有它,你的分支会一直跟随`upstream/dev`,一个后来的平原`git push`或`git pull`去错地方了.

将承诺信息写入 表单, 如“ Fix” 或“ Add 我们就用大写字母开头 。 24.

## 打开 pull request {#6-open-the-pull-request}

所提及的 GitHub 上, 从您的分支打开 pull request 对 `home-assistant/core` 的 `dev` 分支 。 在模板中填写, 不删除任何内容 :

- 请检查access-date=中的日期值 (帮助)
- 解释*为什么*需要改变,而不仅仅是它所做的。
- 将其视为您与 `fixes #12345` 修复的问题 。

机器人要求您在第一个 是我 28. 立刻做,没有它,没有人审查一个pull request。 而且,测试不会运行在您的第一个pull request 直到维护者批准它们。 这是正常的,只是等待。

## ➢ 那个眩晕症 {#7-work-through-the-review}

有人会检查你的pull request。 这需要一段时间,因为排队很长。 期待问题和要求改变:这就是每个pull request都好起来的原因,从来就不是个人楠。 当请求更改时, 您的 pull request 被移动到草稿 。 推动修正,然后标为**准备审查**。

等待时, 请检查其它 pull request 。 模板要求您审查两个,这是学习核心如何工作的最好方法.

## 接下来是什么 {#what-is-next}

- 读 [打开 pull request 后](/core/development/review-process) 要知道要期待什么 。
- 在您下次更改前看 [发展清单](/core/development/checklist) 。
- 想造更大的东西吗? 从[联合国系统](/core/integrations)开始. 将自己的新整合改为:第一:项目建议将[市场](/marketplace)作为其第一个家园。
