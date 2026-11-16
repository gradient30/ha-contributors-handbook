---
title: 综合翻译
description: 一个集成的每个部分的字符串. json, 参考文献和占位符是如何工作的, 以及定制集成如何运送自己的翻译.
sidebarGroup: 参考
order: 3
sidebarLabel: 翻译
---

# 综合翻译 {#integration-translations}

您的整合向用户显示的每个文本都在 `strings.json` 中, 在您的整合文件夹中 。 代码从不包含面临文本的用户:它指的是密钥,而Home Assistant用用户的语言查看文本. 包括配置流程、实体名称和状态、错误、修复问题、行动等等。

`strings.json` 持有英语源文本 。 在您的 pull request 合并后, 英文字符串会被上传到 [Lokalise](/glossary/lokalise), 翻译者将其翻译, 翻译被拉回核心 。 你不需要为此做任何事。 见[翻译工作如何](/translate/how-it-works) 整个旅程, 和[使您的字符串可转换](/translate/guides/developers) 如何写出翻译可以合作的字符串 。

此页面是文件本身的参考: 哪些章节存在, 以及其中的内容 。 结构由hassfest([`script/hassfest/translations.py`](https://github.com/home-assistant/core/blob/dev/script/hassfest/translations.py)在核心中)检查,因此当此页面和hastfest有分歧时,hastfest获胜.

## 见您的更改 {#see-your-changes}

Home Assistant 不直接读作`strings.json` 。 它读取整合的`translations`文件夹中编译的文件,这些文件是生成的,而不是承诺的. 编译您的字符串以在用户界面中看到它们 :

```shell
python3 -m script.translations develop --integration example
```

省略 `--integration` 要被请求的 `--all` , 或对所有集成使用 `--all` 。 如果更改未显示, 请重新启动 Home Assistant 并清除浏览器的缓存 。

## 这些章节 {#the-sections}

所有章节都是可选的。 加入那些你需要的整合。

| 节次 | 翻译的是什么 |
| --- | --- |
| `title` | 整合的名称,只有当它不是品牌名称时 |
| `common` | 将您的集成复用字符串到多个位置 |
| `config` | 那个[配置流量](/core/integrations/config-flow) |
| `options` | 那个[选项流动](/core/integrations/options-flow) |
| `config_subentries` | [子条目](/core/integrations/subentries) 的流量 |
| `selector` | 流程、动作、触发器和条件中选择者的选项和标签 |
| `entity` | 名称、状态、状态属性和单位 |
| `entity_component` | 国家和实体域的属性,用于一个整合,如`sensor` |
| `device` | 设备名称 |
| `exceptions` | 你提出的例外信息 |
| `issues` | 问题及其修复流量 |
| `services` | [动作](/core/integrations/actions) 及其字段的名称和描述 |
| `triggers` | 您的[触发](/core/integrations/triggers-and-conditions) 名称和描述 |
| `conditions` | 您的[他们是条件](/core/integrations/triggers-and-conditions) 名称和描述 |
| `device_automation` | [设备触发器、条件和行动](/core/integrations/device-automations) |
| `system_health` | [系统保健](/core/integrations/system-health) 页上的标签 |
| `application_credentials` | [申请证书](/core/integrations/oauth2#help-users-create-credentials) 对话框中的解释 |
| `preview_features` | 首尾部分 |

还有一些章节用于特定的集成: `config_panel`用于带来自己配置面板的集成,如ZHA和KNX, `conversation`用于对话集成. `auth`,`onboarding`和`homeassistant_hardware`的集成各有各自的计划.

## 标题 {#title}

smith)的整合名称来源于[显示](/core/integrations/manifest),在几乎所有情况下都是品牌名称. 品牌名称没有翻译,所以请离开`title`。

只有在名称是描述而不是品牌时才添加`title`,如"本地日历". 对于核心集成,hansfest拒绝一个`title`在表单中等于名称,除非集成在其允许列表中.

## 流量 {#flows}

`config`, `options`, 以及 `config_subentries` 下的每个类型 共享一个格式 :

```json
{
  "config": {
    "flow_title": "{name} ({host})",
    "step": {
      "user": {
        "title": "Connect to your hub",
        "description": "Enter the address of your Example hub.",
        "data": {
          "host": "[%key:common::config_flow::data::host%]"
        },
        "data_description": {
          "host": "The hostname or IP address of your hub."
        }
      }
    },
    "error": {
      "cannot_connect": "[%key:common::config_flow::error::cannot_connect%]"
    },
    "abort": {
      "no_devices_found": "[%key:common::config_flow::abort::no_devices_found%]"
    }
  }
}
```

| 密钥 | 这是什么 |
| --- | --- |
| `flow_title` | 已发现设备列表中的流名. 见[流程标题](/core/integrations/config-flow#the-flow-title). |
| `step` | 每个步骤 ID: `title`,`description`,`data`,`data_description`,`sections`,`menu_options`,`menu_option_descriptions`,和`submit`(提交按钮的标签) |
| `error` | 在窗体上显示错误, 按键为返回错误 |
| `abort` | 导致流量中止。 支持马克当. |
| `progress` | 进度步骤信件, 按`progress_action` 键 |
| `create_entry` | 创建条目时显示的信件 。 `default` 在您没有通过描述时使用 。 |
| `initiate_flow` | 启动流的按钮的标签 。 当您添加时需要 `user` 。 |

`data_description` 中的每个密钥都需要在 `data` 中的匹配密钥 。 一步键在[窗体、菜单和进度](/core/integrations/flow-steps#labels-and-descriptions)中解释.

子条目类型也需要 `entry_type` 和 `initiate_flow`。 见 [子条目](/core/integrations/subentries#texts-and-translations) 。 帮助者集成必须给其`user`步骤`description`.

## 选择器 {#selectors}

在流程、动作、触发器或条件中的选择者在配置中通过 `translation_key` 获得自己的文本。 文本在 `selector` 下, 按下翻译键 :

```json
{
  "selector": {
    "fan_speed": {
      "options": {
        "off": "[%key:common::state::off%]",
        "low": "Low",
        "high": "High"
      }
    }
  }
}
```

```python
SelectSelector(
    SelectSelectorConfig(
        options=["off", "low", "high"],
        translation_key="fan_speed",
    )
)
```

哪些密钥的适用取决于选择器 :

- `options`: 选定选择器的选项
- `unit_of_measurement`: 数字选择器的单位
- `choices`: 选择选择器的选择
- `fields`:示例对象的字段,每个字段有一个{H1很有可能的},一个可选的`description`和一个可选的`overview_label`

对象选择器在内显示您作为列表添加的项目及其字段的值。 字段的 `overview_label` 在列表中设置其值的文本 。 它必须包含 `{value}` 占位符而不是其他占位符 。 前端填充了字段格式化的值,所以您的代码没有传递任何信息. 没有`overview_label`,列表只显示值 。

```json
{
  "selector": {
    "sensor_offsets": {
      "fields": {
        "uncompensated": {
          "name": "Uncompensated value",
          "description": "The value before the offset is applied.",
          "overview_label": "Uncompensated value: {value}"
        }
      }
    }
  }
}
```

## 实体 {#entities}

`entity` 区域翻译您的实体, 按实体域键, 然后按实体的 [翻译密钥](/glossary/translation-key) 键 :

```json
{
  "entity": {
    "sensor": {
      "operating_mode": {
        "name": "Operating mode",
        "state": {
          "eco": "Eco",
          "boost": "Boost"
        },
        "state_attributes": {
          "fan_mode": {
            "name": "Fan mode",
            "state": {
              "quiet": "Quiet"
            }
          }
        }
      },
      "goal": {
        "name": "Goal",
        "unit_of_measurement": "steps"
      }
    }
  }
}
```

- `name`:实体名称. 见[翻译名称](/core/entities/naming#translated-names),包括地名中的占位符。
- `state`:每个州的文字. 状态是小写密钥, 如 `eco`, 绝不是文本 。 例如,见[选择](/core/entities/select)实体。
- `state_attributes`:属性的名称和状态.
- `unit_of_measurement`:一个单位是一个单词,像"步骤". 具有翻译单位的实体不设置 `native_unit_of_measurement` 。 见[传感器](/core/entities/sensor).

国家、国家属性和单位不能包含占位符。 图标使用相同的翻译密钥, 在 `icons.json` 中. 见[帖式图标](/core/entities/icons).

实体翻译是质量尺度的黄金级规则:参见[实体翻译](/core/quality-scale/entity-translations).

## 实体构成部分 {#entity-components}

仍处于相位时的相位与相位时的相位,按设备类键。 键 `_` 是针对没有设备类的实体 :

```json
{
  "entity_component": {
    "_": {
      "name": "Binary sensor",
      "state": {
        "off": "[%key:common::state::off%]",
        "on": "[%key:common::state::on%]"
      }
    },
    "door": {
      "name": "Door",
      "state": {
        "off": "[%key:common::state::closed%]",
        "on": "[%key:common::state::open%]"
      }
    }
  }
}
```

每个设备类可以有一个`name`,`state`和`state_attributes`,形状与`entity`下的相同. 其他集成则重复这些字符串的引用,如`[%key:component::sensor::entity_component::temperature::name%]`.

## 设备 {#devices}

页:1

```json
{
  "device": {
    "power_strip": {
      "name": "Power strip with {socket_count} sockets"
    }
  }
}
```

带有翻译密钥,设备信息的{茹H0}会被忽略. 如果密钥没有翻译,翻译密钥本身就变成了名称. 以 `translation_placeholders` 填充占位符 。 见[设备注册](/core/integrations/device-registry).

## 例外 {#exceptions}

延伸 `HomeAssistantError` 的例外为 `translation_domain` 、`translation_key` 和 `translation_placeholders` 。 他们的消息在 `exceptions` 下 :

```json
{
  "exceptions": {
    "cannot_connect": {
      "message": "Could not connect to {host}."
    }
  }
}
```

请参看[设置失败和例外](/core/integrations/setup-failures) 在哪里提高它们, 和[例外翻译](/core/quality-scale/exception-translations) 质量尺度规则 。

## 问题 {#issues}

修复问题在 `issues` 下, 由 问题 的 翻译 密钥 键 。 每期都有一个`title`,一个可选的`short_title`,或者一个`description`或者一个`fix_flow`,从不同时出现. A `fix_flow` 的格式与 [流动](/core/integrations/translations#flows) 相同 。 见[维修](/core/integrations/repairs)。

## 动作 {#actions}

您的行动名称和描述在 `services` 下 :

```json
{
  "services": {
    "set_speed": {
      "name": "Set speed",
      "description": "Sets the speed of the fan.",
      "fields": {
        "speed": {
          "name": "Speed",
          "description": "The speed to set."
        }
      },
      "sections": {
        "advanced": {
          "name": "Advanced options"
        }
      }
    }
  }
}
```

每个动作都需要`name`和`description`,每个字段都需要`name`. 字段也可以有一个`example`. 相撞区域内的字段仍然在 `fields` 下; `sections` 仅命名区域 。 见[动作](/core/integrations/actions#names-and-descriptions).

## B. 触发因素和条件 {#triggers-and-conditions}

`triggers`和`conditions`一样工作 `services`:每个触发器或条件,一个`name`,一个`description`,和一个`fields`,有一个`name`,一个可选的`description`,一个可选的`example`。 他们没有`sections`。 如何命名它们, 请见[触发和条件](/core/integrations/triggers-and-conditions) 。

## 设备自动化 {#device-automations}

设备触发器、条件和行动在`device_automation`、`trigger_type`、`trigger_subtype`、`condition_type`和`action_type`下。 设备自动化的额外字段在`extra_fields`中获取标签,在`extra_fields_descriptions`中获取描述. 见[设备自动化](/core/integrations/device-automations#texts).

## 其他各节 {#other-sections}

- `system_health`:您系统健康信息的标签, 在`info` 下。 见[系统保健](/core/integrations/system-health#texts).
- `application_credentials`: 用于用户输入其证书的对话框 `description` 。 见[奥奥特2.0](/core/integrations/oauth2#help-users-create-credentials).
- `preview_features`:每个特性一个`name`和`description`,加上可选的`enable_confirmation`和`disable_confirmation`。 描述可以包含链接,但没有占位符. 见[实验室](/core/development/labs).

## 参考资料 {#references}

许多字符串已经存在,如"连接失败"或"Device已经配置了". 不要再写了 : 用引用指向它们, 写为 `[%key:<path>%]` 。 译者然后翻译字符串一次,对于每一个使用它的综合.

路径使用 `::` 各部分之间 :

- `common::...` 指核中的 [`homeassistant/strings.json`](https://github.com/home-assistant/core/blob/dev/homeassistant/strings.json) 中的共享字符串, 如 `[%key:common::config_flow::data::host%]` 。
- `component::<domain>::...`指任何整合,包括你自己的整合,之间的平衡如`[%key:component::example::config::step::user::title%]`.

对于您多次使用的字符串, 请把它们放在您侬的 `common` 区域, 用 `[%key:component::example::common::<key>%]` 来引用 。

引用必须是整个字符串 : `"Error: [%key:common::...%]"` 被拒绝 。 引用也不能指本身是参考的字符串,因为Lokalise只支持一个关卡. 指其原义. 编译步骤用文本取代引用, 因此文件 Home Assistant 仅包含纯字符串 。

## 占位符 {#placeholders}

只在运行时已知的值, 如主机名称或计数, 在占位符中 : `"Could not connect to {host}."` 。 您的代码填入 :

| 何处 | 你如何通过他们 |
| --- | --- |
| 流程步骤 | `description_placeholders`在`async_show_form`,`async_show_menu`,`async_abort`和`async_create_entry`上 |
| 流程标题 | `title_placeholders` in `self.context` |
| 实体和装置 | `translation_placeholders` |
| 例外和修理问题 | `translation_placeholders` |
| 动作 | `description_placeholders` 当您注册动作时 |

Hassfest 检查每个字符串 :

- 占位符名称是有效的Python标识符,如`{host_name}`.
- 位置符不是用单引号包裹的,比如`'{name}'`.
- 字符串没有 HTML, 起始或结尾没有空格 。
- 字符串没有 URL 。 将 URL 置于占位符中, 因此更改的链接不需要新的翻译 。
- 翻译密钥是小写字母,数字,`-`和`_`. 它们不以 `-` 或 `_` 开始或结束, 并且没有连续的两个 。

在运行时,漏掉密钥的翻译会回到英语. 一种其占位符不同于英文字符串的翻译被丢弃,而使用英文字符串代替.

## 自定义集成 {#custom-integrations}

自定义集成不使用`strings.json`,也不在Lokalise上翻译. 将 `strings.json` 转换为翻译的编译步骤只在核心中运行 。 自定义集成船, 其 `translations` 文件夹中完成的文件本身 :

```text
custom_components/example/
├── __init__.py
├── manifest.json
└── translations/
    ├── en.json
    └── nl.json
```

每个文件以 [BCP 47 《巴塞尔公约》缔约方会议](https://www.rfc-editor.org/info/bcp47) 语言代码命名, 其结构与 `strings.json` 相同 。 `en.json`是需要和完成的,因为它是其他语言的倒置。

参考文献在这些文件中行不通:没有任何内容可以取代它们,所以用户可以看到原始的`[%key:...%]`文本. 写出每个字符串 全部。 占位者照常工作.

Hassfest 验证自定义集成的 `translations/en.json` 。 您可以用 [hansfest GitHub 动作](https://github.com/home-assistant/actions#hassfest) 在自己的仓库中运行 。

## 谁说话 {#who-to-talk-to}

关于 `strings.json` 的问题 , 还是一个忙碌的错误 ? 在 [编码支持**](https://discord.com/channels/330944238910963714/1257019582112334014) 上启动一条线程 。 关于自行翻译的问题,见[翻译](/translate)区域。
