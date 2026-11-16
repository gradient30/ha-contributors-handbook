---
title: 在Home Assistant Core里面
description: 参观位于Home Assistant核心的Python应用程序，以及通向每个部分细节的方式。
order: 10
sidebarLabel: 内部核心
---


# 在Home Assistant Core里面 {#inside-home-assistant-core}
[Home Assistant Core](/glossary/core) 是一个单一的 Python 应用程序。每次安装都会运行它，无论周围运行的是什么。它保存家的状态，运行集成，并响应前端、应用程序和语音助手。

本页面是指南：介绍各部分是什么，以及它们如何协同工作。每个部分的详细信息位于下方链接的 [核心与集成](/core) 区域。

## 部件| 部分 | 一句话说明 | 详细信息 | {#the-parts}
| --- | --- | --- |
| 事件循环 | 在一个线程上一次运行一件事，运行所有内容 | [异步在 Home Assistant](/core/internals/asyncio), [阻塞操作](/core/internals/blocking-operations) |
| `hass` 对象 | 唯一的所有其他内容依赖的对象 | [hass 对象](/core/internals/hass) |
| 状态机 | 保存每个实体的当前状态 | [状态](/core/internals/states) |
| 事件总线 | 告诉每个人刚刚发生了什么 | [事件](/core/internals/events) |
| 操作注册表 | 了解 Home Assistant 可以做的所有操作 | [操作](/core/internals/actions) |
| 注册表 | 记住实体、设备和区域，以及用户修改的内容 | [注册表和存储](/architecture/core/registries) |
| 集成 | 将所有内容连接到外部世界 | [构建集成](/core/integrations) |
| 实体 | 集成与 Home Assistant 其余部分的交汇点 | [实体](/core/entities) |
| 记录器 | 保存历史 | [历史和统计](/architecture/core/history) |

## 它们如何协同工作 {#how-they-work-together}
以一盏通过自身开关打开的灯为例：

1. 灯的集成通过网络得知它的存在。
2. 灯的 [实体](/glossary/entity) 将其新状态写入状态机。
3. 状态机在事件总线上触发一个 `state_changed` 事件。
4. 监听事件的所有人都会作出反应：前端显示灯已打开，记录器将其写入历史记录，而等待该事件的自动化则执行一个动作。
5. 该动作通过动作注册表返回到一个集成，由它告诉另一个设备该做什么。

这些部分彼此之间并不了解，它们在状态机和事件总线上相遇。这就是为什么一个新的集成从第一天起就能与所有仪表盘、自动化和语音助手协同工作。

## 集成的类型 {#kinds-of-integrations}
集成有不同的功能，大多数执行以下其中之一：- **定义一种设备**：像 `light` 这样的实体集成决定在 Home Assistant 中什么是灯，它拥有哪些数据以及以何种格式，以及哪些操作可以控制它。一个新的设备从 [架构讨论](https://github.com/home-assistant/architecture/discussions) 中提议开始，包含它持有的数据，它如何被控制，以及来自多个品牌的示例。
- **连接设备和服务**：像 `hue` 这样的集成与飞利浦Hue通信，并将其灯光作为 `light` 实体提供。这些集成通常不使用其他集成的实体状态。例外是具有位置的实体，例如 `zone` 和 `device_tracker` 的实体。
- **提供虚拟或计算数据**：`input_boolean` 是一个仅存在于 Home Assistant 中的开关。`template` 和 `utility_meter` 从 Home Assistant 中的其他数据计算其实体。

- **自动化**：`automation` 运行用户的自动化，而一个更具体的，比如 `flux`，会根据太阳的位置调整灯光。

## Home Assistant 本身的生命周期 {#the-lifecycle-of-home-assistant-itself}
- [从启动到运行](/architecture/core/startup)：Home Assistant 如何分阶段启动，这样一个损坏的集成也不能阻止整个系统，以及它是如何关闭的。
- [获取数据](/architecture/core/data-updates)：集成如何通过推送或轮询了解变化，以及协调器的作用。
- [注册表和存储](/architecture/core/registries)：Home Assistant 如何在重启之间记住信息。
- [历史和统计](/architecture/core/history)：过去的数据如何被保存，以及保存多久。

## 仓库 {#the-repository}
Home Assistant Core 位于 [home-assistant/core](https://github.com/home-assistant/core) 仓库中：

| 文件夹 | 内容 |
| --- | --- |
| [`homeassistant/`](https://github.com/home-assistant/core/tree/dev/homeassistant) | 核心本身：`core.py`, `bootstrap.py`, `config_entries.py`, `loader.py` |
| [`homeassistant/components/`](https://github.com/home-assistant/core/tree/dev/homeassistant/components) | 每个内置集成，各自一个文件夹 |
| [`homeassistant/helpers/`](https://github.com/home-assistant/core/tree/dev/homeassistant/helpers) | 共享构建模块：实体、注册表、协调器、存储 |
| [`homeassistant/util/`](https://github.com/home-assistant/core/tree/dev/homeassistant/util) | 小型工具，无 Home Assistant：日期、单位、颜色 |
| [`tests/`](https://github.com/home-assistant/core/tree/dev/tests) | 测试，以相同布局组织 |
| [`script/`](https://github.com/home-assistant/core/tree/dev/script) | 工具，例如 hassfest，用于检查每个集成 |

它要求 Python 3.14 或更新版本，有类型标注，并在每个 pull request 上使用 Ruff、mypy 和 pylint 等工具进行检查。用于配置和操作的模式(schema)是用 [probatio](https://pypi.org/project/probatio/) 编写的。

## 从这里开始工作 {#work-on-this}
- 新手使用 Core？从[your first contribution to Core](/core/first-contribution)开始。
- [构建集成](/core/integrations)：连接设备或服务。
- [Core 的工作原理](/core/internals)：本页中每个部分的详细信息。
