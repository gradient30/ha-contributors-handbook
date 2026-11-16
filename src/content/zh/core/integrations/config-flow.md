---
title: 配置流量
description: 让用户通过配置流从UI中添加您的集成功能,并确保同一设备永远不会被设置两次.
sidebarGroup: 设置和配置
order: 2
---

# 配置流量 {#config-flow}

[配置流量](/glossary/config-flow) 是对话框用户在添加您的集成时所经过的: 收集需要的几个步骤, 检查它是否有效, 并创建 [配置条目](/core/integrations/config-entries) 。 当 Home Assistant 找到您的设备时, 发现开始相同的流量 。

由于该流量验证了条目存在之前的一切,所以您的集成不需要在每次启动时检查其配置.

核心中的每一个整合都需要一个配置流. 它必须做什么才能达到质量尺度,就像每个字段的 `data_description` 以及 `data` 和 `options` 之间的拆分一样, 在 [配置流量](/core/quality-scale/config-flow) 规则中 。

## 添加配置 我爱你们 {#add-a-config-flow}

1. 在 [显示](/core/integrations/manifest#config_flow) 中设置 `"config_flow": true` 。
2. 以扩展 `ConfigFlow` 的类创建 `config_flow.py` , 并通过您的域 。
3. 运行 `python3 -m script.hassfest` 一次, 所以 Home Assistant 知道你的整合有配置流 。

[脚手脚脚本](/core/integrations/create)三个都为你。

```python
from typing import Any

import probatio

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_HOST
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN

STEP_USER_SCHEMA = probatio.Schema({probatio.Required(CONF_HOST): str})

class ExampleConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Example."""

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle a flow started by the user."""
        errors: dict[str, str] = {}

        if user_input is not None:
            client = ExampleClient(
                user_input[CONF_HOST],
                session=async_get_clientsession(self.hass),
            )

            try:
                device = await client.get_device()
            except ExampleConnectionError:
                errors["base"] = "cannot_connect"
            else:
                await self.async_set_unique_id(device.serial_number)
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=device.model,
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_SCHEMA,
            errors=errors,
        )
```

每个步骤都是一种命名为`async_step_<step_id>`的方法. 它被调用一次而不输入来显示其形式,在用户提交时再次使用输入. 一个步骤返回接下来会发生什么:一个表单,一个菜单,一个新的条目,或者一个中止. [格式、菜单和进度](/core/integrations/flow-steps) 覆盖全部。

Schemas与 Probatio (`import probatio`) , 校验库 Home Assistant 使用, 经常与 [选择器](/glossary/selector) 合并 。

## 保留步骤 {#reserved-steps}

一些步名有固定的含义. 给他们打电话:

| 步骤 | 当它运行时 |
| --- | --- |
| `user` | 用户从UI中加入集成. 如果不执行匹配的发现步骤,也用于发现. |
| `reconfigure` | 用户重新配置一个已有条目 。 见[重新校正和重组](/core/integrations/reauth-reconfigure). |
| `reauth` | 你们的整合报告 其证书已经失效 |
| `bluetooth`, `dhcp`, `homekit`, `mqtt`, `ssdp`, `usb`, `zeroconf` | 您的装置在您的 [显示](/core/integrations/manifest#discovery) 中通过匹配器被发现 。 |
| `hassio` | 一个 Supervisor app 宣布加入您 |
| `integration_discovery` | 另一 另一个集成系统为您找到了一个设备。 见 { |
| `import` | 保留用于将 YAML 配置移动到配置条目 |
| `discovery` | 堕地. 当缺少源头的发现步骤时调用. |

## 独一无二的ID {#unique-ids}

一个独特的ID将一个配置条目连接到它背后的设备或账户,所以不能设置两次. 设置在 `async_set_unique_id` 的流中, 而配置项继承它 。 它只是需要独特的 在你的整合。

```python
# Abort if another flow for this device is already in progress {#abort-if-another-flow-for-this-device-is-already-in-progress}
await self.async_set_unique_id(device.serial_number)

# Abort if a config entry for this device already exists {#abort-if-a-config-entry-for-this-device-already-exists}
self._abort_if_unique_id_configured()
```

当流量因条目存在而中止时,用户会从您的 `strings.json` 中看到 `already_configured` 中止的原因 。 使用共享字符串 :

```json
{
  "config": {
    "abort": {
      "already_configured": "[%key:common::config_flow::abort::already_configured_device%]"
    }
  }
}
```

独一无二的ID也让用户忽略一个发现的设备,所以他们不会再被问到它. 这就是为什么发现需要一个。

### 更新苍蝇上的连接细节 {#update-connection-details-on-the-fly}

当本地网络上的设备获得一个新的IP地址时,独特的ID允许您从发现步骤中更新现有的条目. 将新值传递到 `_abort_if_unique_id_configured` 。 如果数据更改, Home Assistant 更新条目并重新加载 :

```python
await self.async_set_unique_id(serial_number)
self._abort_if_unique_id_configured(updates={CONF_HOST: host})
```

重装只发生在条目被装入或等待重试其设置时. 通过 `reload_on_update=False` 更新条目而无需重新装入 。 即使没有变化,发现也会重新装入一个正在等待重试其设置的条目:该设备显然再次在线.

### 是什么使得一个好的独特身份 {#what-makes-a-good-unique-id}

它必须是字符串,稳定,而不是用户可以改变的东西.

- **Good**:一个序列号,一个以`homeassistant.helpers.device_registry.format_mac`格式格式化的MAC地址,一个在设备上打印或被焚毁的独特标识符,或者一个纬度和经度.
- **有时对本地设备罚款**:主机名,如果其中部分包含一个好来源.
- ** 云服务有时罚款**:小写中的电子邮件地址,用户名(如果用户名不敏感,则小写),或无法碰撞的账户ID.
- **Never**:一个IP地址,设备名称,URL,或者用户可以更改的主机名.

从设备API或发现中获取MAC地址. 读取 ARP 缓存的工具, 如 `getmac`, 不在每个网络设置 Home Assistant 中工作 。

### 没有唯一身份的发现 {#discovery-without-a-unique-id}

如果你的一些设备没有独有的ID,请在发现步骤中叫这个。 发现还有效,只要你还没有加入:

```python
if device_unique_id:
    await self.async_set_unique_id(device_unique_id)
else:
    await self._async_handle_discovery_without_unique_id()
```

如果你永远得不到一个独特的身份, 离开发现步骤。 Home Assistant 然后在发现设备时调用您的 `user` 步骤, 只要您的整合还没有配置条目 。

## 虱子发现 我爱死你了 {#discovery-steps}

一个发现步骤会收到一个服务信息对象,里面有发现的东西,比如`ZeroconfServiceInfo`. 它必须:

- 确保没有其它流量已经设置了相同的设备. 设置独特的ID 通常处理。 当同一设备以多种方式可以给出不同的独特ID时,在您的流量上执行`is_matching(self, other_flow)`,并呼叫`self.hass.config_entries.flow.async_has_matching_flow(self)`. 然后调用 `is_matching` 用于在进行中的其他流量 。
- 确保设备尚未设置 。
- 总是要求用户确认. 发现步骤绝对不能自行创建条目.

```python
async def async_step_zeroconf(
    self, discovery_info: ZeroconfServiceInfo
) -> ConfigFlowResult:
    """Handle a discovered device."""
    serial_number = discovery_info.properties["serialno"]
    await self.async_set_unique_id(serial_number)
    self._abort_if_unique_id_configured(
        updates={CONF_HOST: discovery_info.host}
    )

    self._host = discovery_info.host
    self.context["title_placeholders"] = {"name": serial_number}

    return await self.async_step_discovery_confirm()

async def async_step_discovery_confirm(
    self, user_input: dict[str, Any] | None = None
) -> ConfigFlowResult:
    """Ask the user to confirm the discovered device."""
    if user_input is not None:
        return self.async_create_entry(
            title=self.unique_id, data={CONF_HOST: self._host}
        )

    self._set_confirm_only()

    return self.async_show_form(step_id="discovery_confirm")
```

`_set_confirm_only()`告诉前端这个步骤只要求确认. 查看 [发现](/core/integrations/discovery) 有关设备如何首先找到 。

### 没有认证的可发现集成 {#discoverable-integrations-without-authentication}

如果您的集成是可发现的且不需要认证, 您可能根本不需要写入一个流 。 `python3 -m script.scaffold integration` 当您回答您的设备是可发现且不需要认证时生成此流 。 对现有集成, 请运行 `python3 -m script.scaffold config_flow_discovery` 。 流程检查是否在完成之前可以找到任何设备,支持清单中的每一个发现方法,并允许一个单一的配置条目来照顾所有设备.

生成的 `config_flow.py` 没有流量类 。 它使用您的域名、 标题和函数调用 `config_entry_flow.register_discovery_flow()` 以返回是否可以找到任何设备 。 Home Assistant 只有在用户手动添加集成而未发现设备等待设置时才会调用该函数 。

#### 在流量和设置中扫描 {#scanning-in-the-flow-and-in-setup}

许多发现协议等待一个超时来收集每一个解答的设备. 您的功能只需要知道是否有至少一个, 然后 {H实情} 需要找到全部 。 这看起来像扫描两次。 使用此辅助工具的核心的整合接受这一点,并保持低成本:

- 函数没有找到任何设置 。 帮助者以空 `data` 创建条目, 并跳过从发现开始流时的函数 。 设置还运行在 Home Assistant 的每个启动上 。 所以设定总是做自己的发现,只有第一个设定通过手扫描两次.
- 一个设备一回答就立刻返回,而不是等待全部超时. Govee点亮地方民意调查 直到第一个设备出现,在超时。 德子问独住. Fjäråskupan 完全不扫描:它检查杏仁花 Bluetooth 设备 Home Assistant 已经看见了 。
- 在设置中,继续发现,并为日后出现的设备添加实体. Gree, Refoss, 和Zerproc 扫描在 `async_track_time_interval()` 的间隔上再次扫描. Govee灯 本地和Escea 保持一个听众运行。 晚答的装置仍然被添加.

Escea是两人共享工作的一个例外. 它的功能开始一个发现服务并在 `hass.data` 中存储, `async_setup_entry` 捡起运行的服务而不是启动第二个服务 。 当函数无任何发现时,它会再次停止服务. 只有在您的库里有一个发现服务, 只要该条目被装入, 才有意义 。

## 流程标题 {#the-flow-title}

UI中流名,与发现设备的名称一样,按此顺序选择:

1. 如果 `self.context` 中的流量设置为 `title_placeholders` , 并且不是空的 :
   1. 您的翻译中有  反对 `flow_title` , 使用该字符串, 并填入占位符 。
   2. 如果没有 `flow_title`,则使用 `name` 占位符, 如果有的话 。
2. 您翻译的 `title` 。
3. 名单的`name`
4. 域经.

重校正流由 `title_placeholders` 单独设置为 `{"name": <entry title>}` 。

## 文本和翻译 {#texts-and-translations}

所有流的文字都生活在 `strings.json`, 在 `config` 下 键:标题、说明、字段标签、错误和中止原因。 例如:

```json
{
  "config": {
    "step": {
      "user": {
        "data": {
          "host": "[%key:common::config_flow::data::host%]"
        },
        "data_description": {
          "host": "The hostname or IP address of your Example device."
        }
      }
    },
    "error": {
      "cannot_connect": "[%key:common::config_flow::error::cannot_connect%]"
    },
    "abort": {
      "already_configured": "[%key:common::config_flow::abort::already_configured_device%]"
    }
  }
}
```

开发时, 运行 `python3 -m script.translations develop` 以在 UI 中看到对 `strings.json` 的更改 。 每个键见[翻译](/core/integrations/translations#flows),规则见[使您的字符串可转换](/translate/guides/developers),步骤键见[窗体、菜单和进度](/core/integrations/flow-steps#labels-and-descriptions)。

## 继续到另一个流程 {#continue-in-another-flow}

一个流可以启动另一个流, 1860子一完成就让前端显示. 将 `next_flow` 传递到 `async_create_entry`, 并带有下一流的类型和ID :

```python
from homeassistant.config_entries import SOURCE_USER, FlowType

result = await self.hass.config_entries.flow.async_init(
    "other_domain", context={"source": SOURCE_USER}
)

return self.async_create_entry(
    title="Example",
    data={},
    next_flow=(FlowType.CONFIG_FLOW, result["flow_id"]),
)
```

子条目流量和选项流量需要配置条目在开始前存在. 继续其中之一, 覆盖 `async_on_create_entry` 。 它在条目创建后运行 :

```python
from homeassistant.config_entries import SubentryFlowContext

async def async_on_create_entry(
    self, result: ConfigFlowResult
) -> ConfigFlowResult:
    """Start adding a location right after the entry is created."""
    subentry_result = await self.hass.config_entries.subentries.async_init(
        (result["result"].entry_id, "location"),
        context=SubentryFlowContext(source=SOURCE_USER),
    )
    result["next_flow"] = (
        FlowType.CONFIG_SUBENTRIES_FLOW,
        subentry_result["flow_id"],
    )

    return result
```

## 与 SchemaConfig FlowHandler 的简单流程 {#simple-flows-with-schemaconfigflowhandler}

我来为帮助者和其他具有简单流量的集成,`SchemaConfigFlowHandler`将整个配置流量和选项流量定义为数据. 牢记其局限性:

- 所有输入都存储在条目的`options`中,而不是`data`中. 这使得它不适合连接细节或API密钥.
- 广泛的验证,独特的ID,或者重复检查,在正常的配置流中往往比较容易.
- 以 `user` 和 `import` 以外的步骤开始流则被劝阻 。

```python
from homeassistant.helpers.schema_config_entry_flow import (
    SchemaCommonFlowHandler,
    SchemaConfigFlowHandler,
    SchemaFlowError,
    SchemaFlowFormStep,
)

async def validate_options(
    handler: SchemaCommonFlowHandler, user_input: dict[str, Any]
) -> dict[str, Any]:
    """Validate the options."""
    if user_input[CONF_THRESHOLD] < 0:
        

# The error key must exist in strings.json {#test-your-config-flow}
        raise SchemaFlowError("negative_threshold")

    return user_input

OPTIONS_SCHEMA = probatio.Schema(
    {probatio.Required(CONF_THRESHOLD): NumberSelector()}
)

CONFIG_FLOW = {
    "user": SchemaFlowFormStep(
        probatio.Schema({probatio.Required(CONF_NAME): TextSelector()}),
        next_step="options",
    ),
    "options": SchemaFlowFormStep(
        OPTIONS_SCHEMA, validate_user_input=validate_options
    ),
}

OPTIONS_FLOW = {
    "init": SchemaFlowFormStep(
        OPTIONS_SCHEMA, validate_user_input=validate_options
    ),
}

class ExampleConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    """Handle a config flow for Example."""

    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    

# Reload the entry when the options change {#reload-the-entry-when-the-options-change}
    options_flow_reloads = True

    def async_config_entry_title(self, options: Mapping[str, Any]) -> str:
        """Return the title of the config entry."""
        return cast(str, options[CONF_NAME])
```

## 测试您的配置流 {#测试您的配置流}

整合核心需要全面测试覆盖`config_flow.py`. 测试每一个路径:成功,每一个错误,每一个中止,以及同一设备的第二个设置中止. 见[写作测试](/core/development/tests).
