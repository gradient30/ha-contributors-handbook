---
title: 从开始到运行
description: Home Assistant Core 在它开始的那一刻和你的家准备好之间所做的事情，以及它如何再次关闭。
order: 2
---


# 从开始到运行 {#from-start-to-running}
当 Home Assistant 启动时，它不会一次加载所有内容。它分阶段加载，因此最重要的部分会先准备好，而一个出错的集成不会阻止房子的其他部分启动。

了解这些阶段有助于你理解为什么你的集成必须等待某些内容，或者为什么启动需要那么长时间。

## 简而言之 {#in-short}
1. Python 启动，并且 Home Assistant 创建它的 [事件循环](/core/internals/asyncio)。
2. 日志记录、配置和注册表加载。
3. 集成分阶段设置：首先是基本部分，如日志记录、前端和数据库，然后是发现和云，然后是其他所有部分。
4. Home Assistant 触发 `homeassistant_start`，运行启动任务，并且正在运行。然后它触发 `homeassistant_started`。

关闭的过程也是相反顺序进行，分阶段且有时间限制，因此总是能完成。

## 详细步骤 {#the-steps-in-detail}
### 在任何内容加载之前 {#before-anything-loads}
`hass` 命令运行 [`homeassistant/__main__.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/__main__.py)。它会检查 Python 版本和操作系统，确保配置文件夹存在，并获取一个锁文件 `.ha_run.lock`，以防止两个副本在同一配置上运行。

然后 `runner.py` 创建 asyncio 事件循环，为阻塞工作的线程池最多可包含 64 个工作线程，并将控制权交给 `bootstrap.py`。

### 引导程序 {#bootstrap}
`bootstrap.py` 设置了其他所有部分所需的内容：

1. **日志记录**，用于 `home-assistant.log` 在配置文件夹中。
2. **配置**：`configuration.yaml` 被读取，包括其密钥和包。
3. **基础部分**：注册表（区域、设备、实体、楼层、标签、类别和问题）、恢复状态和配置条目并行加载。
4. **核心集成**：`homeassistant` 本身和 `persistent_notification`。

从这里开始，Home Assistant 还会监视阻塞事件循环的代码。

### 集成，分阶段进行 {#integrations-in-stages}
哪些集成会加载，是三部分的总和：`configuration.yaml` 中的所有内容、每个有 [配置条目](/glossary/config-entry) 的集成，以及一组默认集成，如前端、自动化、脚本和辅助工具。在 Home Assistant OS，`hassio` 集成也会加入。

它们分三个阶段加载：

| 阶段 | 加载内容 | 时间限制 |
| --- | --- | --- |
| 0 | 日志、前端、记录器和 zeroconf，按此顺序 | 基本没有：数据库迁移不得中断 |
| 1 | 发现 (Bluetooth、DHCP、SSDP、USB)、云和 Supervisor | 120 秒 |
| 2 | 其他所有内容 | 300 秒 |在一个阶段内，集成按照它们所依赖的集成之后并行设置。当一个阶段耗尽时间时，Home Assistant 会记录哪些集成仍在忙碌，并继续进行。一个缓慢的集成会使启动变慢，但不会阻止启动。

### 运行 {#running}
当各阶段完成后，Home Assistant:

1. 将其状态更改为启动中，并触发 `homeassistant_start`。
2. 运行集成注册的启动作业。
3. 将其状态更改为运行中，并触发 `homeassistant_started`。

需要等待其他一切准备就绪的集成，例如查看所有实体的集成，会等待 `homeassistant_started`。助手 `async_at_start` 和 `async_at_started` 会在适当的时刻运行代码，也会在集成在启动后加载时运行。

### 恢复模式 {#recovery-mode}
当无法读取配置、核心集成无法设置或前端无法加载时，Home Assistant 会以恢复模式启动。只有前端、备份和云加载，因此用户仍然可以进入并修复问题。

## 关闭 {#shutting-down}
关闭分为四个阶段，每个阶段都有时间限制，因此一个卡住的集成不会阻止系统重启：

| 阶段 | 发生的事情 | 时间限制 |
| --- | --- | --- |
| 1 | 关闭集成注册的任务 | 20 秒 |
| 2 | 取消后台任务，`homeassistant_stop` 触发，集成关闭它们的连接 | 100 秒 |
| 3 | `homeassistant_final_write` 触发：保存数据的最后机会，比如记录器执行的动作 | 60 秒 |
| 4 | `homeassistant_close` 触发，剩下的任务被取消 | 30 秒 |

## Home Assistant 的状态 {#the-states-of-home-assistant}
`hass.state` 告诉 Home Assistant 在哪里：`not_running`、`starting`、`running`、`stopping`、`final_write` 或 `stopped`。代码还可以检查 `hass.is_running` 和 `hass.is_stopping`。

## 在代码中 {#in-the-code}
| 什么 | 在哪里 |
| --- | --- |
| 命令及其选项 | [`homeassistant/__main__.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/__main__.py) |
| 事件循环和工作线程 | [`homeassistant/runner.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/runner.py) |
| 阶段、默认集成、时间限制 | [`homeassistant/bootstrap.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/bootstrap.py) |
| 启动和停止、`CoreState` | [`homeassistant/core.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/core.py) |
| `async_at_start`、`async_at_started` | [`homeassistant/helpers/start.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/helpers/start.py) |

## 参与其中 {#work-on-this}
- Core 新手？从 [你对 Core 的第一次贡献](/core/first-contribution) 开始。
- [配置失败和异常](/core/integrations/setup-failures)：当你的集成尚无法设置时会发生什么。
- [阻塞操作](/core/internals/blocking-operations)：事件循环看门狗会检查什么。
