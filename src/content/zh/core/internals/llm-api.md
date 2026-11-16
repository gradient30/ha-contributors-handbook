---
title: LLM API 语言
description: Home Assistant如何将工具暴露于大型语言模型,集成如何贡献工具或整个API,以及如何通过MCP服务API.
sidebarLabel: LLM API 语言
sidebarGroup: 语音与 AI
order: 54
---

# LLM API 语言 {#llm-api}

大语言模型(LLMs)在获得工具时可以做比聊天更多的工作. Home Assistant 中的 LLM API 是一组工具, 加上一个解释如何使用它们的提示 。 一个将语言模型包起来的对话代理将用户选择的API工具交给模型,并运行模型调用的工具.

Home Assistant随着两个API的构建而来,集成可以向它们添加工具,或者注册自己的API.

这有三个方面:

- ** 使用API**,在谈话代理。 这被[实情](/core/entities/conversation)覆盖,有`chat_log.async_provide_llm_data`。
- ** 向现有的API提供工具**。 见[贡献工具](/core/internals/llm-api#contribute-tools).
- ** 创建了自己的API**。见[创建自己的 API](/core/internals/llm-api#build-your-own-api)。

## 内置的 APIs {#the-built-in-apis}

`llm`的整合注册了两个API. 自己的工具也没有:它们的所有工具都来自`llm.py`集成平台,在[贡献工具](/core/internals/llm-api#contribute-tools)中描述.

- XQH3}**,带有ID `assist`并显示为用户的"Device control",控制并读取用户接触到Assist的实体. `intent`集成向它提供常见的[意图](/core/internals/intents)作为工具,如`HassTurnOn`和定时器意图,实体集成提供自己的,如设定一个扇的速度. 它不能做任何行政工作。
- XQH1}**,带有ID`homeassistant`,管理Home Assistant本身,像注册,系统日志,自动化,和配置条目一样. 它不限于被曝光的实体,只有管理员才能使用.

登记意图并不使其成为一种工具。 为表达对模型的意向, 请从您的 `llm.py` 平台返回 `llm.IntentTool` 处理器 。essa 工具使用您意图处理器的 `description`, 所以写给模型: 这就是它用来决定何时称呼它的内容 。

## 让用户选择 API {#let-the-user-pick-an-api}

与语言模型交谈的集成让用户在其选项流中选择API. 将选中的 API ID 保存在 `CONF_LLM_HASS_API` 从 `homeassistant.const` 中, 作为列表 。 如果用户选择无,则将密钥留出.

```python
from homeassistant.const import CONF_LLM_HASS_API
from homeassistant.helpers import llm
from homeassistant.helpers.selector import (
    SelectOptionDict,
    SelectSelector,
    SelectSelectorConfig,
)

apis = [
    SelectOptionDict(label=api.name, value=api.id)
    for api in llm.async_get_apis(hass)
]
schema = probatio.Schema(
    {
        probatio.Optional(
            CONF_LLM_HASS_API,
            description={"suggested_value": options.get(CONF_LLM_HASS_API)},
        ): SelectSelector(SelectSelectorConfig(options=apis, multiple=True)),
    }
)
```

当用户选择多个API时,Home Assistant将它们合并为一个模型.

## 贡献工具 {#contribute-tools}

一个集成可以不拥有一个,使用`llm.py`平台,为API添加工具. 它有一个 `async_get_tools` 调回, `llm` 集成需要每个请求, 并结合该请求和正在整理的 API ID 。 返回该 API 的工具, 并附带一个可选的提示, 或者 `None` 以不贡献 。

用您的域名和两个下划线启动您以此方式贡献的每个工具的名称, 如 `my_integration__coffee_count` 。 Home Assistant 报告日志中没有该前缀的工具, 它们停止工作 Home Assistant 2027.3 。

```python
from homeassistant.components import llm
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.llm import LLMContext

@callback
def async_get_tools(
    hass: HomeAssistant, llm_context: LLMContext, api_id: str
) -> llm.LLMTools | None:
    """Return the tools of my integration."""
    if api_id != "assist":
        return None

    return llm.LLMTools(
        tools=[CoffeeCountTool()],
        prompt="Use my_integration__coffee_count for coffee questions.",
    )
```

由于它运行每个请求,工具可以依赖于上下文:请求来自的设备,助手,或者API. 该平台只有在需要时才导入,您的集成不需要依赖`llm`.

## 工具 {#tools}

一个有望顺应坚定地致力于向秘书处提交 `llm.Tool` 的子类:

```python
import probatio

from homeassistant.core import HomeAssistant
from homeassistant.helpers import llm
from homeassistant.util import dt as dt_util

from .const import DOMAIN

class TimeTool(llm.Tool):
    """Tell the time."""

    name = "GetTime"
    title = "Get the time"
    description = "Returns the current time."
    integration = DOMAIN
    annotations = llm.ToolAnnotations(
        read_only=True,
        destructive=False,
        idempotent=True,
        open_world=False,
    )
    parameters = probatio.Schema({probatio.Optional("timezone"): str})

    async def async_call(
        self,
        hass: HomeAssistant,
        tool_input: llm.ToolInput,
        llm_context: llm.LLMContext,
    ) -> llm.ToolResult:
        """Return the current time."""
        tzinfo = dt_util.DEFAULT_TIME_ZONE
        if timezone := tool_input.tool_args.get("timezone"):
            tzinfo = dt_util.get_time_zone(timezone)

        return llm.ToolResult(
            data={"time": dt_util.now(tzinfo).isoformat()}
        )
```

| 属性 | 说明 |
| --- | --- |
| `name` | 要求。 模型的名称称工具通过. |
| `integration` | 要求。 提供工具的集成领域. |
| `description` | 工具做什么,写给模型。 可选,但模型没有它就丢失了. |
| `title` | 名示众生. 可选的 |
| `parameters` | 辩 反对的策略 默认 反对 。 |
| `annotations` | 一个`ToolAnnotations`说工具是如何表现的。 |

报告一个没有youngn `integration`的工具:作为核心集成的一个错误,并作为自定义集成的日志中的警告,直到它停止在Home Assistant2027.10中工作.

### 调用工具 {#calling-a-tool}

得到请求的 `hass`, a `ToolInput` 和 `LLMContext` :

- `ToolInput`有 `tool_name`, `tool_args` (对 `parameters` 的验证), 一个 `id` 的呼叫,和 `external` 。 外部调用是其它东西已经处理的调用,所以聊天日志记录了它,但没有通过LLM API运行. 一个对话代理设定它用于其模型提供者运行的工具,如网络搜索,内置的对话代理设定它用于它自己处理的意图. 调用您工具的聊天日志已设置为 `external` `False` 。
- `LLMContext`有`platform`(代理的域),`context`与用户,`language`,`assistant`被曝光的实体适用,`device_id`请求来自.

返回一个`ToolResult`。 它的`data`必须是可以连载到JSON的词典. 回归平原字典堕落 2027.11停工.

当工具无法完成任务时, 升起 `HomeAssistantError` 。 Home Assistant抓住它并告诉模型 呼叫失败。 要表达模型本身的失败, 请用 `error` 设定返回结果 :

```python
return llm.ToolResult(data={"error": "Calendar not found"}, error=True)
```

### 说明 {#annotations}

说明告诉模型如何小心。 它们匹配[示范背景协议](https://modelcontextprotocol.io)的工具说明, 这次MCP服务器语言集成传递它们.

| 注释 | 含义 | 默认 |
| --- | --- | --- |
| `read_only` | 工具改变不了什么。 | `False` |
| `destructive` | 该工具可以改变或删除已经存在的东西. | `True` |
| `idempotent` | 用同样的论据再次称呼它,没有什么改变。 | `False` |
| `open_world` | 该工具到达 Home Assistant 外部 。 | `True` |

默认假设最坏, 所以声明您的工具是真实的 。

## 构建自己的 API {#build-your-own-api}

API是`llm.API`的子类. 它返回 `APIInstance` : 工具, 以及告诉模型如何使用的工具的提示 。

```python
from homeassistant.helpers import llm

class MyAPI(llm.API):
    """An LLM API of my integration."""

    async def async_get_api_instance(
        self, llm_context: llm.LLMContext
    ) -> llm.APIInstance:
        """Return the tools for this request."""
        return llm.APIInstance(
            api=self,
            api_prompt="Use the tools to look up data in my service.",
            llm_context=llm_context,
            tools=[TimeTool()],
        )

async def async_setup_entry(
    hass: HomeAssistant, entry: MyConfigEntry
) -> None:
    """Set up my integration."""
    entry.async_on_unload(
        llm.async_register_api(
            hass,
            MyAPI(
                hass=hass,
                id=f"my_integration-{entry.entry_id}",
                name=entry.title,
            ),
        )
    )
```

`llm.API` 只取关键词参数 : `hass`, 一个独特的 `id`, 而 `name` 用户看到 。 设置 `requires_admin=True` 的 API , 只有管理员可以使用 。 `async_register_api` 返回未注册 API 的函数: 当 API 属于一个配置项时, 在卸载时呼叫它, 如上 。

`APIInstance` 也可以取 `custom_serializer` : 将您工具的策略像选择器一样转换成模型预期的 JSON 策略的函数 。

## 服务于MCP {#served-over-mcp}

每个注册的API一旦用户设置了 [MCP 服务器集成](https://www.home-assistant.io/integrations/mcp_server/) 就可以在 [示范背景协议](https://modelcontextprotocol.io) 上获取 。 你不需要为此做任何事。

每个API都有自己的流式HTTP端点,位于`/api/mcp/<API ID>`. Assist API 在 `/api/mcp/assist` 。 除 Assist 外, 所有 API 都需要一个管理员的访问符 。 集成还为用户配置在 `/api/mcp` 的 API 服务, 用于不选一个的客户端 。

要找到哪些 API 存在, 管理员可以在 WebSocket 上列出 。 API,按照登记顺序:

```json
{
  "id": 1,
  "type": "llm/api/list"
}
```

```json
{
  "id": 1,
  "type": "result",
  "success": true,
  "result": {
    "apis": [
      {"id": "assist", "name": "Device control", "requires_admin": false}
    ]
  }
}
```
