---
title: 格式、菜单和进度
description: 从表格和章节到菜单、外部步骤和进展的配置流程、选项流程和修复流程的组成部分。
sidebarLabel: 格式、菜单和进度
sidebarGroup: 设置与配置
order: 3
---

# 格式、菜单和进度 {#forms-menus-and-progress}

配置流, [选项流动](/core/integrations/options-flow), [子条目流量](/core/integrations/subentries) 和[修补流程](/core/integrations/repairs) 都建在同一框架上: 数据输入流, 以 `homeassistant.data_entry_flow` 表示 。 一流是一系列步骤. 每一步返回此页面的一个结果,结果决定了用户接下来看到什么.

| 结果下列方面: | 就在那时 | 用户看到的 |
| --- | --- | --- |
| 表格 | `async_show_form` | 要填写的表格 |
| 菜单 | `async_show_menu` | 下一个步骤列表 |
| 创建条目 | `async_create_entry` | 师成功. 流转已成. |
| 中止 | `async_abort` | 一个信息,为什么流动停止 |
| 外部步骤 | `async_external_step` | 一个在另一个网站上完成的链接 |
| 进展 | `async_show_progress` | 长任务运行时旋转器 |

## 显示窗体 {#show-a-form}

表格有阶梯ID,图案以及可选错误. 球场按计划顺序出现. 一旦用户提交有效数据,该步骤法就随输入再次调用.

```python
async def async_step_user(
    self, user_input: dict[str, Any] | None = None
) -> ConfigFlowResult:
    """Ask for the login details."""
    errors: dict[str, str] = {}

    if user_input is not None:
        try:
            await validate_login(self.hass, user_input)
        except InvalidAuth:
            errors["base"] = "invalid_auth"
        else:
            return self.async_create_entry(
                title=user_input[CONF_USERNAME], data=user_input
            )

    return self.async_show_form(
        step_id="user",
        data_schema=probatio.Schema(
            {
                probatio.Required(CONF_USERNAME): str,
                probatio.Required(CONF_PASSWORD): str,
            }
        ),
        errors=errors,
    )
```

### 验证和错误 {#validation-and-errors}

你的台阶只得到娴殷的输入 任何其它的,娴殷的密码都由你决定 再次用 `errors` 字典返回窗体: 键是有问题的字段, 或 `base` 对于一个不包含一个字段的错误 。 该值是您翻译 `error` 一节中的密钥 。

### 多个步骤 {#multiple-steps}

为了进入下一步,返回该步骤的结果。 在流体上保留您需要的早期步骤 :

```python
if user_input is not None:
    self._host = user_input[CONF_HOST]
    return await self.async_step_credentials()
```

将 `last_step=False` 传到 `async_show_form` 显示 ** Next ** 而不是 ** Submit ** 。

### 节 {#sections}

组合字段为 `section` 。 一节会改变窗体的外观和输入的结构:一节的字段会在嵌入词典中到达. 区域不能筑巢。

```python
from homeassistant.data_entry_flow import section

DATA_SCHEMA = probatio.Schema(
    {
        probatio.Required(CONF_HOST): str,
        probatio.Required("ssl_options"): section(
            probatio.Schema(
                {
                    probatio.Required(CONF_SSL, default=True): bool,
                    probatio.Required(CONF_VERIFY_SSL, default=True): bool,
                }
            ),
            

# Show the section collapsed. The default is False. {#labels-and-descriptions}
            {"collapsed": True},
        ),
    }
)
```

该表单的输入看起来像`{"host": "...", "ssl_options": {"ssl": True, "verify_ssl": False}}`. 一节可以有一个图标, 在 `icons.json` 中 :

```json
{
  "config": {
    "step": {
      "user": {
        "sections": {
          "ssl_options": "mdi:lock"
        }
      }
    }
  }
}
```

### 标签和说明 {#defaults-and-suggested-values}

表格的文本在 `strings.json` 中, 在步骤 ID 下 :

| 密钥 | 这是什么 |
| --- | --- |
| `title` | 表格的标题。 不包括品牌名称:Home Assistant从清单中添加. |
| `description` | 训导. 可选的 不要链接到文件,文件是自动链接的,不要说明明显的,比如"在这里你可以设置X". |
| `data` | 字段的标签 。 保持简短,并与其他一体化保持一致。 |
| `data_description` | 下面每个字段的说明 |
| `sections` | 每个区域: `name`、`description` 以及其域 至少 `data` 和`data_description` |

```json
{
  "config": {
    "step": {
      "user": {
        "description": "Enter the details of your Example hub.",
        "data": {
          "host": "[%key:common::config_flow::data::host%]"
        },
        "data_description": {
          "host": "The hostname or IP address of your hub."
        },
        "sections": {
          "ssl_options": {
            "name": "Security options",
            "data": {
              "verify_ssl": "Verify the SSL certificate"
            }
          }
        }
      }
    }
  }
}
```

好弦规则参见[使您的字符串可转换](/translate/guides/developers).

### 默认和建议的值 {#read-only-fields}

预填一个字段有两种方法:

- `default` 填充字段, 当用户离开时也会使用 。
- 一个建议值填补了字段,但用户仍然可以清除.

```python
probatio.Optional(CONF_PORT, default=80): int
probatio.Optional(
    CONF_NAME, description={"suggested_value": "Living room"}
): str
```

`add_suggested_values_to_schema` 以您已有的值填充静态计划, 对于选项流来说是理想的 :

```python
return self.async_show_form(
    step_id="init",
    data_schema=self.add_suggested_values_to_schema(
        OPTIONS_SCHEMA, self.config_entry.options
    ),
)
```

已选择使用 `probatio.In(...)` 和没有 `default` 构建的选定字段 。

### 只读字段 {#browser-autofill}

一些设置在设置后无法更改 。 您仍然可以在一个选项流中显示它们, 因此用户记得自己选的: 添加一个有 `read_only=True` 的选定器的字段 。

```python
probatio.Optional(CONF_ENTITY_ID): EntitySelector(
    EntitySelectorConfig(read_only=True)
)
```

### 浏览器自动填充 {#options-that-depend-on-another-field}

帮助浏览器和密码管理器填写您的表格 。 前端将右 `autocomplete` 属性添加到命名为 `username` 和 `password` 的字段中 。 其它任何情况下,请使用 `autocomplete` 的文本选择器 :

```python
probatio.Required(CONF_USERNAME): TextSelector(
    TextSelectorConfig(type=TextSelectorType.EMAIL, autocomplete="username")
),
probatio.Required(CONF_PASSWORD): TextSelector(
    TextSelectorConfig(
        type=TextSelectorType.PASSWORD, autocomplete="current-password"
    )
),
```

### 依赖于其它字段的选项 {#fields-that-show-based-on-another-field}

一些选择者根据另一个字段的相同形式值来缩小他们的选项. 它们在其配置中使用 `context`, 它绘制了提供其价值的字段名称的上下文密钥 。 例如,测量选择器的单位支持`filter_device_class`和`filter_state_class`。 它们指向一个使用设备类或状态类选择器的字段. 选择器配置拒绝它不知道的上下文密钥, 您不能将 `filter_device_class` 与 `device_classes` 合并, 或 `filter_state_class` 与 `state_classes` 合并 :

```python
probatio.Optional(CONF_UNIT_OF_MEASUREMENT): UnitOfMeasurementSelector(
    UnitOfMeasurementSelectorConfig(
        context={
            "filter_device_class": CONF_DEVICE_CLASS,
            "filter_state_class": CONF_STATE_CLASS,
        }
    )
)
```

内容仅对前端提供的内容有变化。 选择者不对照其它字段检查所提交的值,所以您的步骤仍然需要检查组合是否合理 。

### 基于其它字段显示的字段 {#advanced-options}

一个字段只能显示,而同一步骤的其他字段有一定值. 这样可以节省你额外的一步,或者在提交后再次显示表格,只是为了显示或隐藏几个字段. 使用来自 `homeassistant.data_entry_flow` 的 `Required` 和 `Optional` 标记并给他们 `visible` 条件 :

```python
from homeassistant import data_entry_flow
from homeassistant.helpers.selector import BooleanSelector

DATA_SCHEMA = probatio.Schema(
    {
        probatio.Required(CONF_HOST): str,
        probatio.Required(CONF_SSL, default=False): BooleanSelector(),
        data_entry_flow.Required(
            CONF_VERIFY_SSL,
            default=True,
            visible={"field": CONF_SSL, "value": True},
        ): BooleanSelector(),
    }
)
```

** 校验 SSL 证书** 的复选框仅在检查 ** 使用 SSL ** 时显示 。 一个条件比较了同一步的另一个字段的值. `operator` 密钥选择比较, 而`exists` 和`not_exists` 则不取`value` :

| 运算符 | 匹配字段时 |
| --- | --- |
| `eq` (默认) | 等于 谢谢 {姻缘} |
| `not_eq` | 不等于 `value` |
| `in` | 是 `value` 列表中的值之一 |
| `not_in` | 不是 `value` 中的值 列表 |
| `exists` | 有值: 它不是缺失, `None` 或空字符串 |
| `not_exists` | 没有值 |

`visible` 还要列出一个条件列表, 所有条件都必须匹配, 或者一个普通的`True` 或`False` 。

隐藏字段不显示, 不需要, 并且不包含 `user_input`, 包含默认值 。 对于其它字段的条件来说,它算作是空的. 所提交输入中缺失的字段以其默认值来评价,而所提交的带有空值的字段则保留该值.

由于 9⁄4 ̄ ̧漯B 以`.get()`和一个倒背读,如`entry.data.get(CONF_VERIFY_SSL, True)`.

在 [再一次调整](/core/integrations/flow-steps#sections) 中, 条件查看该部分的字段 。 要隐藏整个部分, 请在部分的标记上 `visible` :

```python
data_entry_flow.Required(
    "ssl_options",
    visible={"field": CONF_SSL, "value": True},
): section(
    probatio.Schema(
        {
            probatio.Required(CONF_VERIFY_SSL, default=True): BooleanSelector(),
            probatio.Optional("ca_cert"): str,
        }
    ),
),
```

### 高级选项 {#create-an-entry}

`show_advanced_options`财产已贬值,将在Home Assistant2027.6. 在此之前它总是返回`True`. 将大多数用户不需要的选项放到崩溃的 [再一次调整](/core/integrations/flow-steps#sections) 中 。

## 创建条目 {#abort}

`async_create_entry`结束流。 在配置流中,它从标题和 `data` 创建配置条目,并且可选的 `options` :

```python
return self.async_create_entry(
    title="Office hub",
    data={CONF_HOST: host, CONF_TOKEN: token},
    options={CONF_SHOW_GUESTS: False},
)
```

两者都必须是JSON系列的。 在 `data` 中设置连接所需的内容, 在 `options` 中设置哪些用户可以调整 。 更改证书为 [重新校正](/core/integrations/reauth-reconfigure), 更新 `data` 。

## 中止 {#show-a-menu}

当流量无法完成时, 以某种理由中止它 。 用户从翻译 `abort` 部分看到匹配的文本 :

```python
return self.async_abort(reason="not_supported")
```

## 显示菜单 {#external-steps}

菜单让用户选择下一步 。 每个选项都是步骤 ID:

```python
return self.async_show_menu(
    step_id="user",
    menu_options=["discovery", "manual"],
    description_placeholders={"model": "Example model"},
)
```

这些标签来自您的翻译 `menu_options`, 以及 `menu_option_descriptions` 的可选描述 。 也可以通过步骤ID和标签的词典而不是列表. 通过 `sort=True` 用用户的语言按其标签排序选项 。

```json
{
  "config": {
    "step": {
      "user": {
        "menu_options": {
          "discovery": "Search the network",
          "manual": "Enter the address of the {model}"
        },
        "menu_option_descriptions": {
          "discovery": "Find hubs on your network automatically."
        }
      }
    }
  }
}
```

## 外部步骤 {#show-progress}

有时用户必须在另一个网站上完成一些东西,比如登录. 对于 OAuth 2.0, 请使用 [OAuth 2.0 帮助器](/core/integrations/oauth2), 它为你做这一切 。 对于其他的事情:

1. 步骤返回 {HH0} 并打开 URL 。 包含其中的流量ID,这样结果就可以找到回路.
2. 用户在另一个网站上完成,将浏览器重定向到Home Assistant中您整合的终点.
3. 该端点呼叫 `hass.config_entries.flow.async_configure(flow_id, data)` 并返回 `<script>window.close()</script>` 关闭窗口 。
4. 步骤随数据再次调用, 返回 `async_external_step_done` 与下一步 。

```python
async def async_step_user(
    self, user_input: dict[str, Any] | None = None
) -> ConfigFlowResult:
    """Send the user to the external website."""
    if not user_input:
        return self.async_external_step(
            step_id="user",
            url=f"https://example.com/link?flow_id={self.flow_id}",
        )

    self._data = user_input

    return self.async_external_step_done(next_step_id="finish")
```

在下一步对返回的数据进行工作,而不是在结束点上,在标出已完成的步骤之前。 用户然后在运行时看到旋转器,而不是空白窗口或 stale 形式.

## 显示进度 {#start-a-flow-from-code}

对于一个需要一段时间的一步,像固件检查一样,在任务中运行工作并显示进展直到完成:

```python
async def async_step_user(
    self, user_input: dict[str, Any] | None = None
) -> ConfigFlowResult:
    """Wait for the device to pair."""
    if not self._pair_task:
        self._pair_task = self.hass.async_create_task(self._async_pair())

    if not self._pair_task.done():
        return self.async_show_progress(
            step_id="user",
            progress_action="pairing",
            progress_task=self._pair_task,
        )

    return self.async_show_progress_done(next_step_id="finish")
```

Home Assistant任务完成后再次调用该步骤,但它也可以更早调用,例如前端重装时. 所以永远不要开始第二个任务:检查一个任务是否存在。 `progress_action` 是您翻译的`progress` 一节中的文本键 。 要显示任务进度有多远, 请拨打 `self.async_update_progress(0.5)`, 值在 0 到 1 之间 。

## 从代码开始流 {#从代码开始流}

融合与发现在上下文中从源开始流动. 流量从该源的名称开始, 而不是在 `user` :

```python
await hass.config_entries.flow.async_init(
    DOMAIN, context={"source": SOURCE_IMPORT}, data=config
)
```

流量可以检查其来源于`self.source`. 要启动已发现设备的流量, 请使用 [发现流程帮助工具](/core/integrations/discovery#discovery-by-another-integration) 。
