---
title: 你要我怎样?
description: 一步一步地构建一个小的,完全的集成,从脚手架到一个配置流,一个协调器,传感器,测试,和一个满足青铜级的pull request.
sidebarLabel: 教学
sidebarGroup: 开始
order: 2
---

# 你要我怎样? {#build-your-first-integration}

在这个教程中,您为您本地网络上的空气质量显示器构建一个完整的集成. 它由UI建立,每分钟对显示器进行投票,并显示其温度,湿度和细微的尘埃作为传感器. 在路上,你触及核心需求新整合的每个部分:一个库,一个配置流程,一个协调员,实体,测试,文档,一个品牌,和一个pull request.

最终,您的整合满足了 [质量尺度](/core/quality-scale) 的青铜级的所有规则, 也就是核心中新整合的最小规则 。 每一步都说它要遵守什么规则 最后一步都检查完

显示器及其库 `exampleair` 为此教程补齐 。 跟随您自己的设备及其库:代码的形状相同,只有名称和数据变化. 该代码在{H1极为重视}上建模,是最近加入核心的局部设备的一种小青铜器集成,带有感应平台,协调器,以及同一套测试. 在它帮助的地方,打开它在这个页面旁边的代码.

配置条目、平台或协调符的新词 ? 先读[如何融入](/core/integrations/concepts). 需要五分钟

## 在你开始之前 {#before-you-start}

- ** 发展环境。 ** 设置 [缔造和平](/core/first-contribution#2-set-up-your-environment) 或 [发展环境](/core/development/environment) 向导 。 运行此页面上的每一个命令 从您核心检查的根, 在那个环境中。
- ** 符合核心的设备或服务。 ** 它今天必须可供人们购买和使用,并具有实际的用户基础。 见[创建集成](/core/integrations/create#does-it-belong-in-core). 对于新的整合,项目建议您先在[市场](/marketplace)中发布. 定制的集成方式是相同的,所以你在这里学到的一切都会继续。
- ** 一些Python。 ** 您应该对课程、 `async` 和`await` 以及输入提示感到舒服 。 您不需要知道 Home Assistant 的代码 。
- ** 时间。 **或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或。、、、、、、、、、、、、、 这是正常的。

然后为您的整合创建一个分支, 从 Home Assistant 的最新 `dev` 分支开始 。 先做这个:核心的预承诺钩包括`no-commit-to-branch`,它拒绝在`dev`,`rc`和`master`上的每一项承诺.

```shell
git fetch upstream
git checkout -b add-example-air upstream/dev
```

`upstream` 是您在[缔造和平](/core/first-contribution#2-set-up-your-environment) 中添加的 `home-assistant/core` 的远程 。

## 开始使用库 {#1-start-with-the-library}

你的整合从不跟设备本身说话 PyPI 上的 Python 库就是这样做的, 您的集成只在库和 Home Assistant 之间翻译 。 如果您的设备还没有库, 请先写一个 : [创建 Python 库](/core/integrations/api-library) 解释它是如何, 在核心接受它之前必须满足什么 。

此教程使用一个带有此接口的小型 Aync 库 :

```python
from dataclasses import dataclass

from aiohttp import ClientSession

@dataclass
class Status:
    """The status of an Example Air monitor."""

    serial_number: str
    name: str
    firmware: str
    temperature: float
    humidity: float
    pm25: int

class ExampleAirError(Exception):
    """Base error of the library."""

class ExampleAirConnectionError(ExampleAirError):
    """The monitor could not be reached."""

class ExampleAirClient:
    """Talk to an Example Air monitor."""

    def __init__(self, host: str, session: ClientSession) -> None:
        """Initialize the client."""

    async def get_status(self) -> Status:
        """Return the current status of the monitor."""
```

三件事对Home Assistant很重要:

- 这是Aync,所以它从不屏蔽[事件循环](/glossary/event-loop)。
- 它接受来自呼叫者的`aiohttp`会话,因此可以使用Home Assistant的共享会话.
- 它提出了自己的例外,因此整合可以从其他问题中分辨出一个无法接触的设备.

Core也询问图书馆是如何出版的. 这是[依赖透明度](/core/quality-scale/dependency-transparency)规则 :

- 该消息来源在一个公共寄存处,根据OSI批准的许可,如麻省理工学院或Apache 2.0.
- 每一份发行都在PyPI上,由公共CI管道建造和发布,而不是手工上传.
- PyPI上的每一版本都符合该寄存器中标记的发布.

在你开始整合前先设置这个 您在 pull request 中链接发布工作流程和标签, 并检查 。

在开发时,将您的库安装在可编辑模式中,这样您就可以立刻更改库和集成. 图书馆住的地方取决于你的设置。

用手动设置,一切直接运行在你的电脑上。 将库保存在您核心检出旁边的文件夹中, 激活虚拟环境, 从核心检出中安装 :

```shell
uv pip install -e ../exampleair
```

开发容器只挂载了您的核心检查, 因此 `../exampleair` 不存在 。 切换到容器内的库,比如在你的家文件夹中,然后从那里安装:

```shell
git clone https://github.com/YOUR_GitHub_USERNAME/exampleair ~/exampleair
uv pip install -e ~/exampleair
```

推动您的库经常变化: 当容器重建时, 核心检出以外的一切都消失了 。 一旦您的库在 PyPI 上发布,您也可以跳过可编辑的安装,并用 `uv pip install exampleair==0.1.0` 安装已发布的版本.

## 2.  启动集成 {#2-generate-the-integration}

运行脚手架脚本 :

```shell
python3 -m script.scaffold integration
```

它问了一些问题。 对于这个教程,答案 没完没了:

| 问题 | 答复 |
| --- | --- |
| 是什么领域? | `example_air` |
| 你们的融合或其它什么名字? | `Example Air` |
| 您的 GitHub 手柄是什么 ? | 您的 GitHub 用户名 |
| 您依赖什么 PyPI做出的承诺和版本 ? | `exampleair==0.1.0` |
| 您的整合将如何收集数据? | `local_polling` |
| Home Assistant 需要用户认证吗 ? | `no` |
| 该设备/服务能否在立足于本地的网络上发现? | `no` |
| 进行监督的类型是什么? | `device` |
| 用户可以使用OAuth2认证设备吗? | `no` |

域名是永久的:它成为文件夹名称,永远无法更改. 见[显示](/core/integrations/manifest#domain).

由于显示器是无法发现的,脚本会生成带有窗体的配置流. 然后运行繁忙,以验证结果,更新所需文件,并生成英文翻译. 你现在有:

```text
homeassistant/components/example_air/
├── __init__.py
├── config_flow.py
├── const.py
├── manifest.json
├── quality_scale.yaml
└── strings.json
tests/components/example_air/
├── __init__.py
├── conftest.py
└── test_config_flow.py
```

生成的代码有效, 但是它是一个模板 : 它有 `TODO` 注释和 `PlaceholderHub` 类, 您的库所在 。 接下来的步骤取代了这一切。

## 检查清单 {#3-check-the-manifest}

打开`manifest.json`。 脚手架从你的回答中填满了它,并添加了一些空键,用于依赖和发现. 删除空密钥: 核心中的几乎所有集成都将其排除在外 。 还有什么:

```json
{
  "domain": "example_air",
  "name": "Example Air",
  "codeowners": ["@your-github-username"],
  "config_flow": true,
  "documentation": "https://www.home-assistant.io/integrations/example_air",
  "integration_type": "device",
  "iot_class": "local_polling",
  "quality_scale": "bronze",
  "requirements": ["exampleair==0.1.0"]
}
```

- `quality_scale`是`bronze`从开始:新的整合必须至少达到青铜. 直到`quality_scale.yaml`中的每个青铜器规则都是`done`或`exempt`时,都会报告一个错误。 你到了第11步就到那里了。 。
- `requirements` 将您的库固定在 `==` 的精确版本 。 Hassfest要求这样,这是[依赖透明度](/core/quality-scale/dependency-transparency)的另一半。

[名单](/core/integrations/manifest)解释 Antwerp1键。

## 4.  构建配置流 {#4-build-the-config-flow}

[配置流量](/core/integrations/config-flow) 是对话框用户在添加集成时看到的 。 它要求主机,连接到显示器上检查它是否有效,并确保同一显示器不会被添加两次.

将`config_flow.py`替换为:

```python
"""Config flow for the Example Air integration."""

import logging
from typing import Any, override

from exampleair import ExampleAirClient, ExampleAirConnectionError
import probatio

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_HOST
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = probatio.Schema(
    {probatio.Required(CONF_HOST): str}
)

class ExampleAirConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Example Air."""

    VERSION = 1

    @override
    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle a flow started by the user."""
        errors: dict[str, str] = {}

        if user_input is not None:
            client = ExampleAirClient(
                user_input[CONF_HOST],
                session=async_get_clientsession(self.hass),
            )

            try:
                status = await client.get_status()
            except ExampleAirConnectionError:
                errors["base"] = "cannot_connect"
            except Exception:
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                await self.async_set_unique_id(status.serial_number)
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=status.name, data=user_input
                )

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )
```

这里发生了什么:

- 第一次,`user_input`是`None`,步骤显示形式.
- 当用户提交时,流量会连接到显示器. 如果失败, 它会再次以错误显示窗体 。 这是[提交的文件 你还好吗?](/core/quality-scale/test-before-configure)的规则。
- 序列号成为配置条目的唯一ID. `_abort_if_unique_id_configured` 当监视器已经设置时停止流量 。 这是[唯一配置输入](/core/quality-scale/unique-config-entry)的规则。 永远不要使用IP地址作为唯一的ID:它会改变.
- 斤`async_get_clientsession` 给你Home Assistant的共享网页会话.
- 减缓贫穷 `@override` 告诉类型检查员,  我们会用这种方法来替换一个父类 。 Core的神秘配置要求它。

核心中的Schemas与 Probatio, 校验库 Home Assistant 使用 。 导入为 `probatio` , 没有别名 。

用户看到的所有文本都在 `strings.json` 中存在, 从来没有在代码中 。 改为:

```json
{
  "config": {
    "step": {
      "user": {
        "data": {
          "host": "[%key:common::config_flow::data::host%]"
        },
        "data_description": {
          "host": "The hostname or IP address of your Example Air monitor."
        }
      }
    },
    "error": {
      "cannot_connect": "[%key:common::config_flow::error::cannot_connect%]",
      "unknown": "[%key:common::config_flow::error::unknown%]"
    },
    "abort": {
      "already_configured": "[%key:common::config_flow::abort::already_configured_device%]"
    }
  },
  "exceptions": {
    "update_failed": {
      "message": "An error occurred while fetching data from the monitor."
    }
  }
}
```

`[%key:...%]` 引用已翻译成每种语言的再利用字符串 。 `data_description` 解释每个字段, 这是[配置流量](/core/quality-scale/config-flow) 规则要求的 。 `exceptions` 一节是下一步给协调员的。 在每次更改为 `strings.json` 后, 重新生成 Home Assistant 和测试的英文译文 :

```shell
python3 -m script.translations develop --integration example_air
```

请参看[翻译](/core/integrations/translations) 文件的每个部分, 和[使您的字符串可转换](/translate/guides/developers) 如何写它们 。

## 5.  将数据与协调员对比 {#5-fetch-the-data-with-a-coordinator}

显示器在一个请求中返回所有值 。 A [协调员](/core/integrations/fetching-data) 每分钟提出一个请求,然后将结果交给所有实体。 当显示器停止响应时,它也标记了它们无法使用,并且只记录一次。

创建 曙光 `coordinator.py` :

```python
"""Coordinator for the Example Air integration."""

from datetime import timedelta
import logging
from typing import override

from exampleair import ExampleAirClient, ExampleAirError, Status

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

type ExampleAirConfigEntry = ConfigEntry[ExampleAirCoordinator]

class ExampleAirCoordinator(DataUpdateCoordinator[Status]):
    """Fetch the status of an Example Air monitor."""

    config_entry: ExampleAirConfigEntry

    def __init__(
        self,
        hass: HomeAssistant,
        config_entry: ExampleAirConfigEntry,
        client: ExampleAirClient,
    ) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            config_entry=config_entry,
            name=DOMAIN,
            update_interval=timedelta(minutes=1),
        )
        self.client = client

    @override
    async def _async_update_data(self) -> Status:
        """Fetch the latest status from the monitor."""
        try:
            return await self.client.get_status()
        except ExampleAirError as err:
            raise UpdateFailed(
                translation_domain=DOMAIN,
                translation_key="update_failed",
            ) from err
```

- `ExampleAirConfigEntry` 是已输入配置的条目 。 它的`runtime_data`是协调器,所以您的平台免费获得一个打字的协调器.
- `update_interval` 由整合固定 。 用户不能更改它,而配置流不得要求它. 选择符合数据的间隔 : 见[适当定价](/core/quality-scale/appropriate-polling) 。
- `UpdateFailed` 告诉协调员更新失败 。 其消息翻译自`exceptions` `strings.json` 的 `exceptions` 一节 。
- 协调员居住在`coordinator.py`,而基准实体位于`entity.py`。 这是[常用模块](/core/quality-scale/common-modules)的规则。

## 设置配置条目 {#6-set-up-the-config-entry}

`__init__.py`连接所有。 Home Assistant为每个配置条目拨打`async_setup_entry`:在启动时,以及用户添加显示器时. 文件替换为:

```python
"""The Example Air integration."""

from exampleair import ExampleAirClient

from homeassistant.const import CONF_HOST, Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .coordinator import ExampleAirConfigEntry, ExampleAirCoordinator

_PLATFORMS: list[Platform] = [Platform.SENSOR]

async def async_setup_entry(
    hass: HomeAssistant, entry: ExampleAirConfigEntry
) -> None:
    """Set up Example Air from a config entry."""
    client = ExampleAirClient(
        entry.data[CONF_HOST], session=async_get_clientsession(hass)
    )

    coordinator = ExampleAirCoordinator(hass, entry, client)
    await coordinator.async_config_entry_first_refresh()

    entry.runtime_data = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, _PLATFORMS)

async def async_unload_entry(
    hass: HomeAssistant, entry: ExampleAirConfigEntry
) -> None:
    """Unload a config entry."""
    await hass.config_entries.async_unload_platforms_or_raise(
        entry, _PLATFORMS
    )
```

- `async_config_entry_first_refresh` 在任何实体存在之前获取第一个数据。 当显示器离线时,它会提高`ConfigEntryNotReady`,而Home Assistant稍后会重试设置. 这是[设置前测试](/core/quality-scale/test-before-setup)的规则。
- 协调员进入`entry.runtime_data`,而不是`hass.data`。 这是[运行时间数据](/core/quality-scale/runtime-data)的规则。
- `_PLATFORMS`有一个平台。 新的整合始于:更多平台 你能不能跟进pull requests。
- `async_unload_entry` 让用户删除或重新装入集成而不重新启动 。
- 没有`async_setup`,因为这个集成本身没有添加[动作](/glossary/action). 如果有的话,请在`async_setup`登记,不要在这里。 这是[动作设置](/core/quality-scale/action-setup)规则,对于这种整合,它可以免除。

## 7.  添加实体 {#7-add-the-entities}

首先,在`entity.py`中有一个基础实体. 显示器的每个实体都共享同一个装置和同一个协调员:

```python
"""Base entity for the Example Air integration."""

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import ExampleAirCoordinator

class ExampleAirEntity(CoordinatorEntity[ExampleAirCoordinator]):
    """Base class for Example Air entities."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: ExampleAirCoordinator) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)
        status = coordinator.data

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, status.serial_number)},
            manufacturer="Example",
            model="Example Air",
            name=status.name,
            serial_number=status.serial_number,
            sw_version=status.firmware,
        )
```

- `CoordinatorEntity` 向协调员订阅该实体, 并在更新失败时使其无法使用 。
- `_attr_has_entity_name = True`在其设备上下文中命名每个实体,如"生活室温度". 这是[有实体名称](/core/quality-scale/has-entity-name)的规则。
- `DeviceInfo` 将显示器放入 [设备注册](/core/integrations/device-registry) 中, 因此用户看到一个带有所有传感器的设备 。
- 这些实体本身不签署任何协议。 `CoordinatorEntity` 在 `async_added_to_hass` 中订阅协调员, 并在实体被删除时取消订阅 。 如果您曾像图书馆所推动的更新一样添加自己的订阅, 请遵守 [实体活动设置](/core/quality-scale/entity-event-setup) 规则 。 对于这种一体化,该规则是例外的。

然后传感器平台, 在 `sensor.py` 中 :

```python
"""Sensor platform for the Example Air integration."""

from collections.abc import Callable
from dataclasses import dataclass
from typing import override

from exampleair import Status

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import (
    UnitOfDensity,
    UnitOfRatio,
    UnitOfTemperature,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import (
    AddConfigEntryEntitiesCallback,
)

from .coordinator import ExampleAirConfigEntry, ExampleAirCoordinator
from .entity import ExampleAirEntity

@dataclass(frozen=True, kw_only=True)
class ExampleAirSensorEntityDescription(SensorEntityDescription):
    """Describe an Example Air sensor."""

    value_fn: Callable[[Status], float | int]

SENSORS: tuple[ExampleAirSensorEntityDescription, ...] = (
    ExampleAirSensorEntityDescription(
        key="temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda status: status.temperature,
    ),
    ExampleAirSensorEntityDescription(
        key="humidity",
        device_class=SensorDeviceClass.HUMIDITY,
        native_unit_of_measurement=UnitOfRatio.PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda status: status.humidity,
    ),
    ExampleAirSensorEntityDescription(
        key="pm25",
        device_class=SensorDeviceClass.PM25,
        native_unit_of_measurement=UnitOfDensity.MICROGRAMS_PER_CUBIC_METER,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda status: status.pm25,
    ),
)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ExampleAirConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the Example Air sensors."""
    coordinator = entry.runtime_data

    async_add_entities(
        ExampleAirSensor(coordinator, description)
        for description in SENSORS
    )

class ExampleAirSensor(ExampleAirEntity, SensorEntity):
    """A sensor of an Example Air monitor."""

    entity_description: ExampleAirSensorEntityDescription

    def __init__(
        self,
        coordinator: ExampleAirCoordinator,
        description: ExampleAirSensorEntityDescription,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = (
            f"{coordinator.data.serial_number}_{description.key}"
        )

    @property
    @override
    def native_value(self) -> float | int:
        """Return the value of the sensor."""
        return self.entity_description.value_fn(self.coordinator.data)
```

- [实体描述](/glossary/entity-description)将每个传感器描述为数据:其设备类,单位,以及如何获得其值. 稍后添加一个传感器是`SENSORS`中的另一个条目.
- 设备类给出了每个传感器的名称,图标,以及正确的单位转换. 因为这些传感器有设备类,不需要自己的名字.
- 独特的ID将序列号与密钥结合. 它永远不会改变,它让用户重新命名实体。 这是[实体- 唯一](/core/quality-scale/entity-unique-id)的规则。

[实体和平台](/core/entities) 每个实体类型都有页面, 如 [传感器实体](/core/entities/sensor) 。

## 试试看 {#8-try-it}

在 Home Assistant 显示您在列表中的整合之前, 重新生成列出所有整合的文件 :

```shell
python3 -m script.hassfest --skip-plugins quality_scale
```

没有 `--integration-path`, 便会验证每个生成的集成和更新文件, 如 `CODEOWNERS` 和 [`homeassistant/generated/config_flows.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/generated/config_flows.py) 。 这些变化属于您的pull request 。 它只有在没有发现错误时才会写出来,而你的`quality_scale.yaml`仍然是`todo`。 这就是为什么这个运行跳过质量尺度检查,就像脚手架脚本一样. 从第11步开始,你运行它没有`--skip-plugins`。

现在开始你的开发实例。 在开发容器中,打开命令调色板,选择**任务:运行任务**,然后是**Run Home Assistant Core。 转到 `http://localhost:8123` , 在 ** 安排 ** > **Devices & Services**,选择**Add集成**和搜索**示例空气**. 输入显示器的地址,您应该看到带有三个传感器的新设备。

事情不起作用吗? 在 `config/configuration.yaml` 启用您的集成和库的调试日志, 并重新启动 :

```yaml
logger:
  default: info
  logs:
    homeassistant.components.example_air: debug
    exampleair: debug
```

不在名单上的整合? 检查日志中的错误, 然后对您的浏览器进行硬刷新: 前端缓存 。 [你的第一次贡献](/core/first-contribution#4-make-the-change) 更多研讨您的代码 其他操作和调试, 包括如何从开发容器中到达您的网络上的设备 。

## 9.  写测试 {#9-write-the-tests}

核心中的每一个新整合都伴随着测试,配置流需要全覆盖. 没有真设备的测试会运行:你嘲笑库,让Home Assistant真实运行. 解释背后的想法。

在 `tests/components/example_air/conftest.py` 中从共享的固定装置开始 :

```python
"""Common fixtures for the Example Air tests."""

from collections.abc import Generator
from unittest.mock import AsyncMock, MagicMock, patch

from exampleair import Status
import pytest
from pytest_homeassistant.common import MockConfigEntry

from homeassistant.components.example_air.const import DOMAIN
from homeassistant.const import CONF_HOST

@pytest.fixture
def mock_setup_entry() -> Generator[AsyncMock]:
    """Override async_setup_entry."""
    with patch(
        "homeassistant.components.example_air.async_setup_entry",
        return_value=None,
    ) as mock_setup_entry:
        yield mock_setup_entry

@pytest.fixture
def mock_example_air_client() -> Generator[MagicMock]:
    """Mock the Example Air client."""
    with (
        patch(
            "homeassistant.components.example_air.ExampleAirClient",
            autospec=True,
        ) as mock_client,
        patch(
            "homeassistant.components.example_air.config_flow"
            ".ExampleAirClient",
            new=mock_client,
        ),
    ):
        client = mock_client.return_value
        client.get_status.return_value = Status(
            serial_number="EA123456",
            name="Living room",
            firmware="1.2.0",
            temperature=21.5,
            humidity=45.0,
            pm25=8,
        )
        yield client

@pytest.fixture
def mock_config_entry() -> MockConfigEntry:
    """Return the config entry of a monitor."""
    return MockConfigEntry(
        domain=DOMAIN,
        title="Living room",
        unique_id="EA123456",
        data={CONF_HOST: "192.168.1.50"},
    )
```

客户端被补丁到您的集成导入位置: 在 `__init__.py` 中一次, 在 `config_flow.py` 中一次 。

### 测试配置流 {#test-the-config-flow}

替换`test_config_flow.py`。 测试快乐的路径,每一个错误, 和重复检查。 每个错误测试都以创建的条目结尾,以证明流量恢复:

```python
"""Test the Example Air config flow."""

from unittest.mock import MagicMock

from exampleair import ExampleAirConnectionError
import pytest
from pytest_homeassistant.common import MockConfigEntry

from homeassistant.components.example_air.const import DOMAIN
from homeassistant.config_entries import SOURCE_USER
from homeassistant.const import CONF_HOST
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResultType

@pytest.mark.usefixtures("mock_setup_entry", "mock_example_air_client")
async def test_user_flow(hass: HomeAssistant) -> None:
    """Test adding a monitor."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )
    assert result["type"] is FlowResultType.FORM
    assert result["errors"] == {}

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {CONF_HOST: "192.168.1.50"}
    )

    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["title"] == "Living room"
    assert result["data"] == {CONF_HOST: "192.168.1.50"}
    assert result["result"].unique_id == "EA123456"

@pytest.mark.usefixtures("mock_setup_entry")
@pytest.mark.parametrize(
    ("exception", "error"),
    [
        pytest.param(
            ExampleAirConnectionError, "cannot_connect", id="cannot_connect"
        ),
        pytest.param(Exception, "unknown", id="unknown"),
    ],
)
async def test_user_flow_errors(
    hass: HomeAssistant,
    mock_example_air_client: MagicMock,
    exception: type[Exception],
    error: str,
) -> None:
    """Test errors, and that the flow recovers from them."""
    mock_example_air_client.get_status.side_effect = exception

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {CONF_HOST: "192.168.1.50"}
    )

    assert result["type"] is FlowResultType.FORM
    assert result["errors"] == {"base": error}

    mock_example_air_client.get_status.side_effect = None

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {CONF_HOST: "192.168.1.50"}
    )

    assert result["type"] is FlowResultType.CREATE_ENTRY

@pytest.mark.usefixtures("mock_example_air_client")
async def test_already_configured(
    hass: HomeAssistant, mock_config_entry: MockConfigEntry
) -> None:
    """Test that the same monitor cannot be added twice."""
    mock_config_entry.add_to_hass(hass)

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {CONF_HOST: "192.168.1.60"}
    )

    assert result["type"] is FlowResultType.ABORT
    assert result["reason"] == "already_configured"
```

这些测试是 [配置- 流量- 测试- 覆盖](/core/quality-scale/config-flow-test-coverage) 的规则 :

- 快乐的路径检查创建的条目,包括其独特的ID. 当独特的ID构建方式发生意外变化时,这个测试就抓住了它.
- 表格可以显示的每一个错误都有一个测试,这些测试中每一个都以一个创建的条目结尾. 这证明用户可以解决问题并完成设置. Pylint警告说,一个从未完成流量的错误测试.
- 重复测试输入不同的主机,用于一个序列号相同的显示器,并期望流量以 `already_configured` 中止. 每个测试都以最终结果结束:一个创建的条目或者一个中止.
- 它们一起运行着每行的`config_flow.py`. 你看看下面的报导

### 测试设置 {#test-the-setup}

在`test_init.py`中,测试集成负载和卸载,以及安装在显示器下线时的重试:

```python
"""Test the setup of the Example Air integration."""

from unittest.mock import MagicMock

from exampleair import ExampleAirConnectionError
import pytest
from pytest_homeassistant.common import MockConfigEntry

from homeassistant.config_entries import ConfigEntryState
from homeassistant.core import HomeAssistant

@pytest.mark.usefixtures("mock_example_air_client")
async def test_load_unload(
    hass: HomeAssistant, mock_config_entry: MockConfigEntry
) -> None:
    """Test loading and unloading a config entry."""
    mock_config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(mock_config_entry.entry_id)
    await hass.async_block_till_done()

    assert mock_config_entry.state is ConfigEntryState.LOADED

    await hass.config_entries.async_unload(mock_config_entry.entry_id)
    await hass.async_block_till_done()

    assert mock_config_entry.state is ConfigEntryState.NOT_LOADED

async def test_setup_retry_when_offline(
    hass: HomeAssistant,
    mock_example_air_client: MagicMock,
    mock_config_entry: MockConfigEntry,
) -> None:
    """Test that setup is retried when the monitor is offline."""
    mock_example_air_client.get_status.side_effect = (
        ExampleAirConnectionError
    )
    mock_config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(mock_config_entry.entry_id)
    await hass.async_block_till_done()

    assert mock_config_entry.state is ConfigEntryState.SETUP_RETRY
```

### 测试传感器 {#test-the-sensors}

在 `test_sensor.py` 中, 即时测试检查每个传感器: 其状态、 单位、 设备类别和登记项 :

```python
"""Test the Example Air sensors."""

import pytest
from pytest_homeassistant.common import MockConfigEntry, snapshot_platform
from syrupy.assertion import SnapshotAssertion

from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er

@pytest.mark.usefixtures("mock_example_air_client")
async def test_sensors(
    hass: HomeAssistant,
    mock_config_entry: MockConfigEntry,
    entity_registry: er.EntityRegistry,
    snapshot: SnapshotAssertion,
) -> None:
    """Test the sensors of a monitor."""
    mock_config_entry.add_to_hass(hass)

    await hass.config_entries.async_setup(mock_config_entry.entry_id)
    await hass.async_block_till_done()

    await snapshot_platform(
        hass, entity_registry, snapshot, mock_config_entry.entry_id
    )
```

### 运行他们 {#run-them}

第一次的快照测试创造了快照. 然后用覆盖报告进行所有测试:

```shell
pytest tests/components/example_air --snapshot-update
pytest tests/components/example_air \
  --cov=homeassistant.components.example_air \
  --cov-report term-missing
```

打开 `tests/components/example_air/snapshots/test_sensor.ambr` 读它: 当您检查它是否正确时, 一个快照只会证明一些事情 。 覆盖报告显示没有达到测试的线。 `config_flow.py`必须是100%。 [运行测试](/core/development/testing)还有更多的操作方法。

## 添加品牌和文件 {#10-add-the-brand-and-the-documentation}

七青铜器规则与核心中的代码完全无关. 他们在另外两个仓库里相遇了 和你的一样 现在就开始:他们分别接受审查,而你的核心pull request在他们已经到达时更容易接受审查.

### 这个品牌 {#the-brand}

您整合的图标和标志在 [品牌存储器](https://github.com/home-assistant/brands) 中, 在一个以您的域名命名的文件夹中 : `core_integrations/example_air/` 。 至少添加 `icon.png` 和 `icon@2x.png` , 如果品牌有宽的标志 。 [品牌和品牌形象](/core/integrations/brands#brand-images-for-core-integrations) 列出每个文件和图像要求 。 这是[品牌](/core/quality-scale/brands)的规则。

### 文 件 {#the-documentation}

每个集成都有一个页面在[Home Assistant.io](https://www.home-assistant.io/)上. 以 pull request 写到 [Home Assistant.io仓库](https://github.com/home-assistant/home-assistant.io), 相对 `next` 分支, 从整合页面模板开始 。 一步一步的走过去

对于青铜器来说,页面需要三件事,每件事都有自己的规则:

- ** 产品说明**,第一行,与制造商有联系。 这是[高层次文件描述](/core/quality-scale/docs-high-level-description)。
- ** 步骤** 作为先决条件,用户必须先做任何事情。 这是[设置文件](/core/quality-scale/docs-installation-instructions)。
- ** 如何去除整合**,包括Home Assistant外面留下的任何东西。 这是[证件 -- -- 搬运](/core/quality-scale/docs-removal-instructions)。

对于“实例空气”,`source/_integrations/example_air.markdown`的这些部分可能看起来是这样:

```markdown
The **Example Air** {% term integration %} connects Home Assistant to
the air quality monitors of [Example](https://www.example.com). It shows
the temperature, humidity, and fine dust that your monitor measures.

## Prerequisites {#prerequisites}

1. Set up your monitor with the **Example** app, and connect it to your
   network.
2. In the app, look up the IP address of your monitor.

{% include integrations/config_flow.md %}

## Removing the integration {#removing-the-integration}

This integration follows standard integration removal. No extra steps
are required.

{% include integrations/remove_device_service.md %}
```

青铜器,[文件行动](/core/quality-scale/docs-actions),[文件触发](/core/quality-scale/docs-triggers)和[文件条件](/core/quality-scale/docs-conditions)的另外三个docs规则,是关于记录动作,触发器,以及整合的条件. 例空无一,所以这些规则是免责的.

## 11.  在质量尺度中还包括 {#11-fill-in-the-quality-scale}

打开`quality_scale.yaml`。 脚手架把每个规则都列为`todo`. Hassfest要求质量尺度的每个规则都要在文件中,每个青铜规则都必须是`done`,或者`exempt`,并附有一条说明原因的评论. 你们的融合现在满足了他们所有人:

| 规则 | 状态 | 何处 |
| --- | --- | --- |
| [动作设置](/core/quality-scale/action-setup) | 豁免 | 没有动作, [步骤 6](/core/integrations/tutorial#6-set-up-the-config-entry) |
| [适当定价](/core/quality-scale/appropriate-polling) | 写好了 | 一分钟,[步骤5](/core/integrations/tutorial#5-fetch-the-data-with-a-coordinator) |
| [品牌](/core/quality-scale/brands) | 写好了 | [步骤10](/core/integrations/tutorial#the-brand) |
| [常用模块](/core/quality-scale/common-modules) | 写好了 | `coordinator.py`和`entity.py`,步骤5和7 |
| [配置流量](/core/quality-scale/config-flow) | 写好了 | [波 乐](/core/integrations/tutorial#4-build-the-config-flow) |
| [配置- 流量- 测试- 覆盖](/core/quality-scale/config-flow-test-coverage) | 写好了 | [步骤9](/core/integrations/tutorial#test-the-config-flow) |
| [依赖透明度](/core/quality-scale/dependency-transparency) | 写好了 | 步骤[1](/core/integrations/tutorial#1-start-with-the-library)和[3](/core/integrations/tutorial#3-check-the-manifest) |
| [文件行动](/core/quality-scale/docs-actions) | 豁免 | 无动作 |
| [文件条件](/core/quality-scale/docs-conditions) | 豁免 | 无条件 |
| [高层次文件描述](/core/quality-scale/docs-high-level-description) | 写好了 | [步骤10](/core/integrations/tutorial#the-documentation) |
| [设置文件](/core/quality-scale/docs-installation-instructions) | 写好了 | [步骤10](/core/integrations/tutorial#the-documentation) |
| [证件 -- -- 搬运](/core/quality-scale/docs-removal-instructions) | 写好了 | [步骤10](/core/integrations/tutorial#the-documentation) |
| [文件触发](/core/quality-scale/docs-triggers) | 豁免 | 无触发器 |
| [实体活动设置](/core/quality-scale/entity-event-setup) | 豁免 | 只有协调员公民资格 [步骤 7](/core/integrations/tutorial#7-add-the-entities) |
| [实体- 唯一](/core/quality-scale/entity-unique-id) | 写好了 | [步骤7](/core/integrations/tutorial#7-add-the-entities) |
| [有实体名称](/core/quality-scale/has-entity-name) | 写好了 | [步骤7](/core/integrations/tutorial#7-add-the-entities) |
| [运行时间数据](/core/quality-scale/runtime-data) | 写好了 | [步骤6](/core/integrations/tutorial#6-set-up-the-config-entry) |
| [提交的文件 你还好吗?](/core/quality-scale/test-before-configure) | 写好了 | [波 乐](/core/integrations/tutorial#4-build-the-config-flow) |
| [设置前测试](/core/quality-scale/test-before-setup) | 写好了 | [步骤6](/core/integrations/tutorial#6-set-up-the-config-entry) |
| [唯一配置输入](/core/quality-scale/unique-config-entry) | 写好了 | [波 乐](/core/integrations/tutorial#4-build-the-config-flow) |

文件替换为:

```yaml
rules:
  

# Bronze {#check-it-yourself}
  action-setup:
    status: exempt
    comment: "The integration does not register actions."
  appropriate-polling: done
  brands: done
  common-modules: done
  config-flow-test-coverage: done
  config-flow: done
  dependency-transparency: done
  docs-actions:
    status: exempt
    comment: "The integration does not register actions."
  docs-conditions:
    status: exempt
    comment: "The integration does not provide conditions."
  docs-high-level-description: done
  docs-installation-instructions: done
  docs-removal-instructions: done
  docs-triggers:
    status: exempt
    comment: "The integration does not provide triggers."
  entity-event-setup:
    status: exempt
    comment: "Entities only subscribe to the coordinator."
  entity-unique-id: done
  has-entity-name: done
  runtime-data: done
  test-before-configure: done
  test-before-setup: done
  unique-config-entry: done

  

# Silver {#12-open-the-pull-request}
  action-exceptions: todo
  config-entry-unloading: todo
  docs-configuration-parameters: todo
  docs-installation-parameters: todo
  entity-unavailable: todo
  integration-owner: todo
  log-when-unavailable: todo
  parallel-updates: todo
  reauthentication-flow: todo
  test-coverage: todo

  

# Gold {#what-is-next}
  devices: todo
  diagnostics: todo
  discovery-update-info: todo
  discovery: todo
  docs-data-update: todo
  docs-examples: todo
  docs-known-limitations: todo
  docs-supported-devices: todo
  docs-supported-functions: todo
  docs-troubleshooting: todo
  docs-use-cases: todo
  dynamic-devices: todo
  entity-category: todo
  entity-device-class: todo
  entity-disabled-by-default: todo
  entity-translations: todo
  exception-translations: todo
  icon-translations: todo
  reconfiguration-flow: todo
  repair-issues: todo
  stale-devices: todo

  

# Platinum {#platinum}
  async-dependency: todo
  inject-websession: todo
  strict-typing: todo
```

银、金和白金规则暂时不变 其中一些已经到达,但留待以后的pull request。 只在规则 `done` 真正是时标记: 规则是 `done` 在繁忙和平坦中打开额外的检查, 而审查者检查其余部分 。

文档和品牌规则在此文件中为`done`,但在其他的pull requests中则被满足. 评论员检查这些 pull requests, 所以联系他们 在你的。

### 你自己去检查一下 {#你自己去检查一下}

不取此页之言. 验证您的整合方式 :

```shell
python3 -m script.hassfest \
  --integration-path homeassistant/components/example_air
pytest tests/components/example_air \
  --cov=homeassistant.components.example_air \
  --cov-report term-missing
```

Hassfest 现在运行您标记的 `done` 规则的验证符, 如 `config-flow`, `runtime-data`, `test-before-setup` 和`unique-config-entry` 。 覆盖报告必须显示`config_flow.py`的100%。 [所有规则列表](/core/quality-scale/rules) 在一行中解释每个规则, [自己去检查一下](/core/quality-scale/raise-tier#check-it-yourself) 解释每个检查所证明的, 以及它所没有的 。

## 打开 pull request {#打开-pull-request}

先在市场出版? 遵循 [发布自定义集成](/marketplace/guides/integrations) 相反, 一旦您的整合成熟并拥有用户基础, 请回到这个步骤 。

在你推前,运行所有的东西的插座, 运行的节奏最后一次,没有跳过任何东西。 包含它们更改的每个文件, 也在您的集成文件夹之外 :

```shell
prek run --all-files
python3 -m script.hassfest
```

您的 pull request 现在包含您的集成, 其测试, 生成的文件, 以及更新的要求文件 。 把它交到您在开始时创建的分支上, 推到您的叉上, 并打开 pull request 对准 `dev` [Home Assistant/核心人员](https://github.com/home-assistant/core) 的分支 。 [提交 pull request](/core/development/submitting) 通过模板 。 为了新的一体化:

- 选择 ** 新集成** 作为变化的类型。
- 解释设备或服务是什么,并链接到您的库的源寄存器,其发布工作流程,以及您所依赖的发布标记.
- 链接文档和品牌的 pull request 。
- 保持你在这里建造的东西:一个平台,没有别的了。 诊断 动作 重新校正 和选择权 一次一个 pull request

然后等待开始。 对新一体化的审查需要时间,有时是几周。 当你等待时,请检查其它的pull requests:这是学习的最好方法,它让排队为每个人移动. 解释接下来会发生什么。

## 接下来是什么 {#接下来是什么}

你们的融合已经进入了 现在让它更好,一个小pull request一次:

- [提高等级](/core/quality-scale/raise-tier) 到 Silver : 优雅地处理一个离线设备, 如果您的设备需要资质的话, 加入重校正, 并达到95%以上的测试覆盖率 。
- 添加[诊断](/core/integrations/diagnostics),这样用户就可以分享集成在报告错误时所看到的.
- 支持 [发现](/core/integrations/discovery), 因此 Home Assistant 自己找到监视器 。
- 添加第二个平台, 如 [二进制传感器](/core/entities/binary-sensor) 用于空气质量提醒 。
