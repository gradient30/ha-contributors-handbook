---
title: 如何融入
description: 每个集成的一小撮思想都是用简单的语言构建的,与网页 行了更深入的链接。
sidebarLabel: 如何融入
sidebarGroup: 开始
order: 1
---

# 如何融入 {#how-an-integration-fits-in}

在你写集成之前,它帮助人们知道这些词. 只有极少数,每一个整合都以同样的方式使用它们. 本页用几句话来解释每一个,并链接到更深的页面. 读一次,然后在 [教程](/core/integrations/tutorial) 中构建一些东西 。

## 图片 {#the-picture}

说你的网络上有空气质量监视器 进入 Home Assistant :

1. 一个Python** 图书馆** 知道怎么跟监视器说话。
2. 您的** 整合** 使用该库, 从UI 设置, 带有** 配置流**。
3. 配置流程创建了 ** 配置条目 **: 一个显示器,及其地址.
4. 对于这个ظار ,** 协调员** 要求显示器 每分钟提供新的数据。
5. 一个**平台**,像`sensor`,将数据变成**实体**:温度传感器,湿度传感器.
6. 这些实体属于**装置**:显示器本身。

全部运行在一个**事件循环**上,全部通过一个对象到达Home Assistant的其余部分:\\H0}.

## 一体化 {#integration}

[融合](/glossary/integration) 是将Python代码连接到设备、服务或想法的 Home Assistant 的文件夹 。 将与 Home Assistant 的舰只融合到 `homeassistant/components/<domain>/` 的 [核心存储器](https://github.com/home-assistant/core) 中, 和他们的测试在 `tests/components/<domain>/` 中。

[域名](/glossary/domain)是集成的短而独特的名称,如`hue`或`airgradient`. 它是文件夹的名称,它永远不能改变,它出现在整合动作的名称中.

每个集成都有一个`manifest.json`来描述它:它的名称,集成所有者,它需要的库,以及如何发现它. 见[显示](/core/integrations/manifest)和[文件结构](/core/integrations/file-structure)。

## 图书馆 {#library}

集成从不直接对设备或服务说话. 所有协议代码,如 HTTP 请求或解析包, 都生活在 PyPI 上单独的 Python 库中 。 集成只翻译在该库和Home Assistant之间. 这就使得整合规模小,易于审查,让其他人也使用图书馆. 见[创建 Python 库](/core/integrations/api-library).

## 配置流量和配置条目 {#config-flow-and-config-entry}

[配置流量](/glossary/config-flow) 是对话框用户在 **Settings ** > 下添加您的整合时所经过的 。 ** 设备和服务**。 它要求需要什么,比如一个主机名,测试连接,然后创建一个配置条目.

A [配置条目](/glossary/config-entry) 是您整合的一个设置实例: 一个监视器,一个账户,一个中枢. 它存储了所收集的配置流. Home Assistant 在您的`__init__.py` 中为每个配置条目拨打 `async_setup_entry`, 启动时和用户添加新条目时。 运行时, 您的整合会像 API 客户端一样, 在 `entry.runtime_data` 中保持它所需要的 。

见[配置流量](/core/integrations/config-flow)和[配置条目](/core/integrations/config-entries)。

## 平台和实体 {#platform-and-entity}

[实体](/glossary/entity)是Home Assistant可以显示,测量,或控制的一个东西:温度传感器,光线,开关. 每个实体都有状态,如`21.5`或`on`,用户在实体上建立他们的仪表板和自动化.

[平台](/glossary/platform) 是您的整合如何提供一类实体 。 要提供传感器,请添加`sensor.py`。 要提供灯光,请添加`light.py`。 每个平台文件都有自己的`async_setup_entry`创建实体. 您的集成将其配置条目转发到其所支持的平台.

每个实体需要一个 [唯一标识](/glossary/unique-id) , 永远不变 。  一切都会改变。

见[实体和平台](/core/entities)和[实体类别](/core/entities/entity-class)。

## 设备 {#device}

[设备](/glossary/device) 是实体所属的物理物质或服务。 空气质量显示器是一个有多个实体的设备. 您的实体用 `DeviceInfo` 描述其设备, 并且 Home Assistant 把它放到设备注册 。 用户视其为所有实体的设备页面. 见[设备注册](/core/integrations/device-registry)。

## 协调员 {#coordinator}

大多数设备在一个请求中返回全部数据. A[协调员](/glossary/coordinator) ( 我们走 `DataUpdateCoordinator` 类) 一次获取数据, 按时间表, 并把它交给所有实体 。 它也会处理错误: 当更新失败时, 它会标记无法使用的实体, 然后再尝试 。 见[获取数据](/core/integrations/fetching-data)。

## 事件循环和同步 {#the-event-loop-and-async}

Home Assistant运行于Python的`asyncio`。 几乎每件事情都发生在一个线条中,[事件循环](/glossary/event-loop),一次只有一个代码运行在那里. 只要没有人   > 屏蔽它。 当您的代码等待没有 `await` 的网络时, Home Assistant 中的所有东西都会等待它 。

有两个原因:

- 使用 aync 库, 和 `await` 其调用 。 屏蔽调用到 `hass.async_add_executor_job` 的线程 。
- 名称以 `async_` 开头的函数, 如 `async_setup_entry` 或 `async_add_entities` , 必须在事件循环中运行 。 这是核心中的命名公约,所以可以从函数所属的名称中分辨出来.

见[显示在 Home Assistant](/core/internals/asyncio).

## 隐藏对象 {#the-hass-object}

每个设置函数都得到`hass`,运行中的Home Assistant实例. 您与系统其它部分丈量的整合都经过它: `hass.states` 持有每个有助于加强实体的状态 `hass.bus` 携带事件 `hass.services` 持有动作 `hass.config_entries` 管理配置条目 。 在一个实体或一个流中,它是`self.hass`。 见[对象](/core/internals/hass).

## 下一步 {#next-steps}

- 在 [教程](/core/integrations/tutorial) 中从开始到完成建立小集成 。
- 想要解决 làm一体化的问题吗? 从{L làm}开始.
