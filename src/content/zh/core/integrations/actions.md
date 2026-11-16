---
title: 一体化行动
description: 注册用户从自动化,脚本和仪表板调用的动作,在服务中加以描述. 雅姆尔,并返回回复数据。
sidebarGroup: 融合特征
order: 1
sidebarLabel: 动作
---

# 一体化行动 {#actions-in-integrations}

[动作](/glossary/action)是用户可以从自动化,脚本,或开发工具的**Actions**标签中调用的东西,如`light.turn_on`. 实体一体化,如`light`,提供共同行动。 您的整合可以注册它自己的, 对于它特有的事物, 如 `sonos.set_sleep_timer` 。

此页面是关于您整合的附加动作 。 下方的动作注册系统如何运作,操作者得到什么,如何从代码中调用动作,是在[核心如何发挥作用:行动](/core/internals/actions)上.

首先在自己的整合中添加一个动作,而不是改变一个共享的动作. 当一个模式在整合过程中出现时,它可以在以后成为共同行动.

> [!NOTE]
> 在代码中,动作仍然被称为服务:`hass.services`,`ServiceCall`,和`services.yaml`. 这是同样的事情。

## 在 async setup 中注册动作 {#register-actions-in-asyncsetup}

在 `async_setup` 中注册您整合的动作, 不在 `async_setup_entry` 中, 而不是在一个平台中 。 这样即使没有配置条目被装入,它们也存在,因此使用它们的自动化可以编辑和验证,用户得到一个明显的错误而不是一个未知的动作. 这是[质量尺度](/core/quality-scale)的青铜级规则。

将注册设置在 `services.py` 中, 在一个名为 `async_setup_services` 的函数中, 并从 `async_setup` 调用该函数 。 它是一个同步函数,由`@callback`装饰,只需要`hass`。 Pylint 警告在 `services.py` (`home-assistant-action-registered-outside-services-module`) 之外注册的动作, 并警告一个带有另一个形状的 `async_setup_services` (`home-assistant-invalid-setup-services`) 。

由于您的整合现在有 `async_setup`, 它需要 `CONFIG_SCHEMA` 。 见[没有YAML的集成](/core/integrations/yaml#integrations-without-yaml).

## 选择正确的目标 {#choose-the-right-target}

行动的目标在正确的层面上。 不要使用更高或更低的级别,即使一个可以解决到另一个.

- 在此操作中, 使用“ 睡眠计时器” 。 注册 [实体行动](/core/integrations/actions#entity-actions) 。
- **Device**:动作需要整个设备,就像重启一样. 使用 `device_id` 字段 。 不要使用实体ID作为设备的备用。
- **Config 条目**:动作需要集成实例,比如在云服务中创建账户中的东西. 使用 `config_entry_id` 字段 。 不使用设备或实体ID作为其配置条目的站点。

当某项行动需要目标时,就要求它。 不要回到默认目标:当用户添加第二个设备时,今天工作的自动化会默默地做别的事情.

## 配置条目动作 {#actions-for-a-config-entry}

```python title="services.py"
import probatio

from homeassistant.const import ATTR_CONFIG_ENTRY_ID
from homeassistant.core import (
    HomeAssistant,
    ServiceCall,
    ServiceResponse,
    SupportsResponse,
    callback,
)
from homeassistant.helpers import config_validation as cv, service

from .const import DOMAIN

GET_FORECAST_SCHEMA = probatio.Schema(
    {
        probatio.Required(ATTR_CONFIG_ENTRY_ID): cv.string,
        probatio.Required("days"): cv.positive_int,
    }
)

@callback
def async_setup_services(hass: HomeAssistant) -> None:
    """Register the actions of the Example integration."""

    async def async_get_forecast(call: ServiceCall) -> ServiceResponse:
        """Return the forecast for the coming days."""
        entry: ExampleConfigEntry = service.async_get_config_entry(
            hass, DOMAIN, call.data[ATTR_CONFIG_ENTRY_ID]
        )
        forecast = await entry.runtime_data.client.get_forecast(
            call.data["days"]
        )

        return {"forecast": [day.as_dict() for day in forecast]}

    hass.services.async_register(
        DOMAIN,
        "get_forecast",
        async_get_forecast,
        schema=GET_FORECAST_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )
```

```python title="__init__.py"
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN
from .services import async_setup_services

CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Example integration."""
    async_setup_services(hass)
    return True
```

`service.async_get_config_entry` 检查配置项是否存在, 属于您的整合, 并被装入 。 如果没有,它会发出`ServiceValidationError` 并带有一个翻译信件 。 对于设备目标, `service.async_get_device_and_config_entry(hass, DOMAIN, device_id)` 对一个设备和拥有它的配置条目都一样 。

## 实体行动 {#entity-actions}

实体对用户目标实体采取行动。 用户可以通过实体,设备,区域,地板或标签来瞄准它们,并且Home Assistant将它解决给您的实体. 用 {H 我叫 `async_register_platform_entity_service` 注册它们, 在您自己的域( 如 `sonos`) 下, 不在实体域( 如 `media_player`) 下 :

```python title="services.py"
import probatio

from homeassistant.components.media_player import (
    DOMAIN as MEDIA_PLAYER_DOMAIN,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import config_validation as cv, service

from .const import DOMAIN

@callback
def async_setup_services(hass: HomeAssistant) -> None:
    """Register the actions of the Sonos integration."""
    service.async_register_platform_entity_service(
        hass,
        DOMAIN,
        "set_sleep_timer",
        entity_domain=MEDIA_PLAYER_DOMAIN,
        schema={probatio.Required("sleep_time"): cv.positive_int},
        func="set_sleep_timer",
    )
```

这叫 `set_sleep_timer` 每个目标实体的 `sleep_time` 作为关键词参数的方法 。 `func`不是方法名称,而是可以是一个接收实体和`ServiceCall`的ASync函数. 计划可以是一个词典, 它被转化为一个实体 动作计划给你。 只允许具有某些特性的实体,通过`required_features`.

## 仅管理动作 {#admin-only-actions}

只能向管理人员提供可改变配置或具有其他安全影响的行动。 用`async_register_admin_service`从`homeassistant.helpers.service`登记,而不是`hass.services.async_register`。 它首先需要`hass`,然后是相同的参数,并检查在您的处理器运行前,该呼叫的用户是管理员.

## 提出错误 {#raise-errors}

当动作失败时, 提出一个减缓贫穷的例外, 所以用户会看到出错 : `ServiceValidationError` 当用户做错事时, `HomeAssistantError` 对于其它任何事情 。 使用翻译信件 。 见[行动中的例外情况](/core/integrations/setup-failures#exceptions-in-actions-and-entity-methods).

## 返回回复数据 {#return-response-data}

动作可以返回数据,用于比实体状态更需要的自动化,如日历事件列表或搜索结果. 不要用于符合实体状态的数据:温度是传感器,而不是反应.

茸发响应数据是一个`dict`,可以序列化为JSON. 当您注册动作时通过 `supports_response` :

| 数值 | 含义 |
| --- | --- |
| `SupportsResponse.NONE` | 动作回报什么。 默认. |
| `SupportsResponse.OPTIONAL` | 动作有所作为,也可以返回数据. 检查 `call.return_response` 查看打电话者是否想要它, 如果没有, 返回 `None` 。 |
| `SupportsResponse.ONLY` | 动作只做回数据 |

错误总是例外,在响应中从不错误代码. 用户在自动化中不应需要处理错误。

## 描述 56. 服务业的行动。 雅 56. {#describe-actions-in-servicesyaml}

用户只使用可以找到的动作. 描述 `services.yaml` 中的每个动作, 因此 UI 可以显示正确的字段和选择器 。 关键是动作名称, 没有您的域名 :

```yaml
set_speed:
  target:
    entity:
      domain: fan
      supported_features:
        - fan.FanEntityFeature.SET_SPEED
  fields:
    speed:
      required: true
      example: "low"
      selector:
        select:
          translation_key: "fan_speed"
          options:
            - "off"
            - "low"
            - "medium"
            - "high"
    advanced_options:
      collapsed: true
      fields:
        speed_pct:
          selector:
            number:
              min: 0
              max: 100
```

- `target`: 对于采取实体的行动。 它允许用户选择实体,设备,和区域. 没有过滤器, 它提供每个实体, 所以缩小它与 `entity`[选择器](/glossary/selector) 。 Hassfest 拒绝目标上的 `device` 过滤器 : 在字段中为此使用设备选择器 。 在 `target` 中, 不要添加 `entity_id` 字段 。
- `supported_features` : 只提供至少支持其中一个特性的实体 。 要需要多个特征,将它们放在一个嵌入的列表中.
- `fields`:每个字段一个条目,有`required`,一个`example`,一个`default`,和一个`selector`,决定UI中的输入.
- 区域:一个键,带有 `collapsed` 和它自己的 `fields` 组合字段在一个可折叠的段落中 。 它只会改变字段的外观:数据没有嵌入,所以上面的动作得到`{"speed_pct": 50}`.

### 仅在应用时显示字段 {#show-fields-only-when-they-apply}

一个字段上的 `filter` 只当至少有一个选定的实体支持时才会显示它 。 过滤器只在使用 `target` 的动作中工作, 因为他们查看了选中的实体 : 在其它动作中 hasfest 拒绝它们 。 使用 `supported_features` 或 `attribute`, 而不是同时使用 :

```yaml
temperature:
  filter:
    supported_features:
      - climate.ClimateEntityFeature.TARGET_TEMPERATURE
color_temp:
  filter:
    attribute:
      supported_color_modes:
        - light.ColorMode.COLOR_TEMP
        - light.ColorMode.HS
```

使用 `attribute` 过滤器,当一个选定实体的属性有一个列出的值时显示字段 。 如果属性是一个列表,一个匹配的项目就足够了.

### 名称和说明 {#names-and-descriptions}

每个动作和每个字段的名称和描述不在`services.yaml`中:它们位于`strings.json`,在`services`下,每个动作和字段都需要一个. 使用描述占位符保存翻译的 URL, 在您注册动作时通过 :

```python
hass.services.async_register(
    DOMAIN,
    "get_forecast",
    async_get_forecast,
    schema=GET_FORECAST_SCHEMA,
    supports_response=SupportsResponse.ONLY,
    description_placeholders={"docs_url": "https://example.com/forecast"},
)
```

格式参见[翻译](/core/integrations/translations#actions), 而[使您的字符串可转换](/translate/guides/developers) 。

### 图标 {#icons}

辫子 : 区域也可以有一个图标:

```json
{
  "services": {
    "start_brewing": {
      "service": "mdi:flask",
      "sections": {
        "advanced_options": "mdi:test-tube"
      }
    }
  }
}
```

## 试试看 {#try-it}

打开开发工具的 ** 动作 ** 标签, 选择您的动作, 填入字段, 并选择 ** 效果动作 ** 。
