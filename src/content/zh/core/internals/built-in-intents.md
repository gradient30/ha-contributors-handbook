---
title: 内设的处理器
description: 意向的处理者 {H0 20.} 住在Core的船舶, 他们如何找到它们的实体, 在哪里查看每一个意向及其槽。
sidebarGroup: 语音和AI
order: 51
sidebarLabel: 内设意图
---

# 内设的处理器 {#built-in-intent-handlers}

内置的意向是 [意图](/core/internals/intents) Home Assistant Core 处理自己, 如 `HassTurnOn` 或 `HassStartTimer` 。 触发它们的句子,在每种语言中,都生活在[意图存储器](https://github.com/OHF-Voice/intents)中. 对他们采取行动的人住在Core

完整列表,包含每个插槽,插槽组合,以及一个示例句子,都在翻译区的[内设意图](/translate/voice/intents)上. 它跟随[`intents.yaml`](https://github.com/OHF-Voice/intents/blob/main/intents.yaml), 定义它们的文件 。 此页面覆盖了Core的一面: 处理者在哪里, 以及在他们工作时需要记住什么.

## 管家们住的地方 {#where-the-handlers-live}

每个内置意图通过集成注册,只有在集成被加载时才有效. 大多数实体域在 `intent.py` 平台中注册它们的域, 而 `intent` 集成设置 。

| 一体化 | 的 | 意图 |
| --- | --- | --- |
| `intent` | [`homeassistant/components/intent/__init__.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/intent/__init__.py) | 打开和关闭,转动,状态,位置,停止,日期,时间,室内温度,对话意图 `HassNevermind`和`HassRespond` |
| `intent` | [`homeassistant/components/intent/timers.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/intent/timers.py) | 计时器 |
| `assist_satellite` | [`homeassistant/components/assist_satellite/intent.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/assist_satellite/intent.py) | `HassBroadcast` |
| `climate` | [`homeassistant/components/climate/intent.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/climate/intent.py) | 设置温度和风扇模式 |
| `cover` | [`homeassistant/components/cover/intent.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/cover/intent.py) | `HassOpenCover` 和 `HassCloseCover` (韩语) |
| `fan` | [`homeassistant/components/fan/intent.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/fan/intent.py) | `HassFanSetSpeed` |
| `humidifier` | [`homeassistant/components/humidifier/intent.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/humidifier/intent.py) | 目标湿度和模式 |
| `lawn_mower` | [`homeassistant/components/lawn_mower/intent.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/lawn_mower/intent.py) | 旋转和对接 |
| `light` | [`homeassistant/components/light/intent.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/light/intent.py) | `HassLightSet` |
| `media_player` | [`homeassistant/components/media_player/intent.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/media_player/intent.py) | 暂停, 不暂停, 下一个, 前一个, 音量, 哑音, 搜索和播放 |
| `shopping_list` | [`homeassistant/components/shopping_list/intent.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/shopping_list/intent.py) | 购物列表 |
| `todo` | [`homeassistant/components/todo/intent.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/todo/intent.py) | 待办事宜列表 |
| `vacuum` | [`homeassistant/components/vacuum/intent.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/vacuum/intent.py) | 开始,返回基地,清理一个区域 |
| `weather` | [`homeassistant/components/weather/intent.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/weather/intent.py) | `HassGetWeather` |

最常用的意向名称是[`homeassistant/helpers/intent.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/helpers/intent.py)中的常数,如`intent.INTENT_TURN_ON`. 用那些代替弦

## 寻找实体 {#finding-the-entities}

多数在 我们得在实体上行动的意向在相同位置发现它们:`name`,`area`,`floor`,`domain`和`device_class`. 处理器与用户的Home Assistant中的实体、区域和地板匹配。 当像Assist这样的助手发送意向时,只有接触到该助手的实体被匹配.

在无语区时,一些插槽组合使用听到句子的语音卫星区域. 译名页标注这些内容为"卫星区".

## 意向无句 {#intents-without-sentences}

少数内置意图在意向寄存器中没有句子,因此内置的对话代理从未产生. 代码仍然可以解雇他们,有些被提供作为AI对话代理的工具. 其中两个, `HassOpenCover` 和`HassCloseCover` 被 `HassTurnOn` 和 `HassTurnOff` 覆盖 : 在新代码中使用 。 [无句意图清单am](/translate/voice/intents#intents-without-sentences)他们全部。

## 相关 {#related}

- [意图](/core/internals/intents) : 写你自己的处理器, 从代码或 HTTP 上写出火的意向 。
- [对话 API](/core/internals/conversation-api)和[LLM API 语言](/core/internals/llm-api):文本和AI模型如何变成意图.
- {驴]:每个意图背后的句子如何写,每个语言.
