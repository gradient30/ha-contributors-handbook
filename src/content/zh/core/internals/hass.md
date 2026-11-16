---
title: Python 中的 hass 对象
description: HomeAssist 每一个集成都得到的实例, 挂在其中的是什么, 核心配置在 has. config上 。
sidebarLabel: hass 对象
sidebarGroup: 核心
order: 1
---

# Python 中的有位对象 {#the-hass-object-in-python}

读取任何集成后, 您可以看到一个名为 `hass` 的变量 。 这是运行中的 Home Assistant 实例, 类 `HomeAssistant` 从 [`homeassistant/core.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/core.py) 中的对象 。 你的代码和系统的其他部分 都经过它

## 挂断的 {#what-hangs-off-hass}

| 属性 | 这是什么 |
| --- | --- |
| `hass.bus` | 那个[事件总线](/core/internals/events) 纵火事件并听听 |
| `hass.states` | 那个[状态机器](/core/internals/states)。 读写实体状态. |
| `hass.services` | 那个[行动登记册](/core/internals/actions)。 登记和呼吁行动。 名字比"动作"更古老. |
| `hass.config` | 核心配置:位置,单位,时区,语言,路径. 见[下级](/core/internals/hass#the-core-configuration). |
| `hass.config_entries` | 所有整合的配置条目 。 |
| `hass.auth` | [认证管理器](/core/internals/auth):用户,组,和符. |
| `hass.data` | 用于共享实例的数据词典。 使用从 `homeassistant.util.hass_dict` 输入的 `HassKey` 作为密钥 。 属于一个配置项的数据在`entry.runtime_data`中进行。 |
| `hass.loop` | Ayncio事件 循环一切运行。 |
| `hass.state` | 凡 Home Assistant 在其生命中: a `CoreState`, 如 `CoreState.starting`, `CoreState.running`, 或 `CoreState.stopping` 。 |

除此之外,`hass`还有安排工作的方法:`async_create_task`,`async_create_background_task`和`async_add_executor_job`. [在 Home Assistant 中同步](/core/internals/asyncio) 解释何时使用 。

## 核心的四个部分 {#the-four-parts-of-core}

核心是一台小机器,有四个部分:

- 活动公交车**载着发生的一切. 其它零件在它上点燃事件,任何东西都可以听.
- ** 状态机器** 持有每个实体的当前状态, 当一个变化时, 启动 `state_changed` 事件 。
- ** 行动登记处** 将每项行动都登记为一体化。 调用动作点火 `call_service` 事件, 然后运行处理器 。
- ** 配置** 描述了实例:它在哪里、它使用的单元和装载什么。

其他的,从实体到自动化,都建立在这些之上,作为帮助者和集成物.

## 你从哪里来? {#where-you-get-hass-from}

您从未创建 `hass` 自己 。 把手拿给你:

- ** 集成设置** : `async_setup_entry(hass, entry)` 在 `__init__.py` 中, 当设置一个配置条目时得到它 。 在启动时也设置了某种内容的整合在 `async_setup(hass, config)` 中获取 。
- **Platforms**:`async_setup_entry(hass, entry, async_add_entities)`在一个平台文件中,像`sensor.py`.
- ** 实体**:`self.hass`,一旦实体被添加到Home Assistant。 尚未设置于`__init__` 。
- ** 组合流量** 和 ** 选项流量** :`self.hass`。
- ** 行动处理器意见交流。

如何在这些入境点周围进行整合,见[构建集成](/core/integrations)。

## 核心配置 {#the-core-configuration}

`hass.config` 是 `Config` 从 [`homeassistant/core_config.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/core_config.py) 起的一个实例 。 用户将其大部分设置在**Settings** > **System** > ** General**下. 读它,不要写它:核心拥有这些值并为你存储.

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| `latitude` | `float` | 家经纬. |
| `longitude` | `float` | 家经度. |
| `elevation` | `int` | 升起家,总是用米. |
| `radius` | `int` | 母区进行过半径,总以米计. |
| `location_name` | `str` | 实例名称. 默认为 `Home` 。 |
| `time_zone` | `str` | 时代区名,如`Europe/Amsterdam`. |
| `units` | `UnitSystem` | 单位系统,公制或美国惯例。 |
| `currency` | `str` | 货币代码,如`EUR`。 |
| `country` | `str \| None` | 家的乡村代码,如果设置。 |
| `language` | `str` | 实例的语言, 如 `en` 。 |
| `internal_url` | `str \| None` | 为本地网络配置的用户 URL 。 |
| `external_url` | `str \| None` | URL 用户配置到网络外 。 |
| `config_dir` | `str` | 配置目录的路径 。 |
| `api` | `ApiConfig \| None` | HTTP 服务器的配置, 一旦 `http` 集成设置了它 。 |
| `components` | `set[str]` | 装入的整合 。 |
| `config_source` | `ConfigSource` | 配置来源于: `default`,`discovered`,`storage`(设置在UI),或`yaml`. |
| `allowlist_external_dirs` | `set[str]` | 文件夹集成可读取文件 。 |
| `allowlist_external_urls` | `set[str]` | URL集成可能会从中获取文件. |
| `media_dirs` | `dict[str, str]` | 媒体文件夹,按名称排列. |
| `skip_pip` | `bool` | 如果 `True` , 启动时不安装要求 。 |
| `skip_pip_packages` | `list[str]` | 安装要求时要跳过的软件包 。 |
| `recovery_mode` | `bool` | Home Assistant 是否在恢复模式中运行 。 |
| `safe_mode` | `bool` | Home Assistant 是否在安全模式下运行, 没有自定义的集成 。 |
| `debug` | `bool` | 既往不咎。 |

有几个帮助方法值得了解:

- `hass.config.path("my_file.json")` 返回配置目录中的路径 。
- `hass.config.cache_path("my_cache")` 返回缓存目录中的路径, 用于重生成且不属于备份的数据 。
- `hass.config.is_allowed_path(path)`和`hass.config.is_allowed_external_url(url)` 对照许可列表检查 。 在触摸来自用户的路径或URL之前使用它们. `is_allowed_path` 屏蔽 I/O : 用 `hass.async_add_executor_job` 在执行器中调用它, 而不是在事件循环中 。
- `hass.config.distance(lat, lon)`返回离家的距离,单位系统的长度单位(公里或英里).

不直接读取 URL 来构建链接 。 从 `homeassistant.helpers.network` 使用 `get_url(hass)` : 它选择了合适的 URL 来描述这种情况, 并且知道 Home Assistant Link 。
