---
title: 测试语法
description: 如何写出证明你句子符合正确意图的测试,填充正确的插槽,给出正确的响应.
order: 8
---

# 测试语法 {#test-syntax}

[意图存储器](https://github.com/OHF-Voice/intents)中的每个句子模板都被测试覆盖. 一个测试给出了几个例子句子,并说它们必须填充哪个空档以及Assist必须回答什么. 测试每pull request。

## 检测所在 {#where-tests-live}

测试镜像 [句子文件](/translate/voice/template-syntax#sentence-files), 每个意图和槽组合一个文件 :

```text
tests/<language>/<intent>/<slot_combination>.yaml
```

每个测试文件都靠自己 它宣布它需要的家:楼层、区域、实体、计时器以及它所谈论的媒体。 测试文件诘问之间没有共享,所以可以不看其他文件而阅读和更改一个文件.

## 我以为你是... {#a-test-file}

```yaml
# tests/en/HassTurnOn/name_only.yaml {#testsenhassturnonnameonlyyaml}
language: "en"

entities:
  - name: "Overhead Light"
    domain: "light"
  - name: "Sliding Door"
    domain: "cover"

tests:
  - sentences:
      - "turn on Overhead Light"
      - "Overhead light on"
    slots:
      name: "Overhead Light"
    response: "Turned on the light"

  - sentences:
      - "open Sliding Door"
    slots:
      name: "Sliding Door"
    response: "Opening"
```

`tests` 持有一个或多个组。 每个小组:

| 密钥 | 要求数 | 含义 |
| --- | --- | --- |
| `sentences` | 对 | 审判的判刑 |
| `slots` | 是的,当组合有插槽时 | 每一个句子必须填满的空档, 以及它们的值 |
| `response` | 对 | 准确文本 Assist 必须回答 |
| `timers` | No | [计时器](/translate/voice/test-syntax#timers-and-media) 只针对此组 |
| `media` | No | [媒体](/translate/voice/test-syntax#timers-and-media) 只针对此组 |

每个句子都必须与文件命名时的意向和槽组合一致. `slots` 必须在 `intents.yaml` 中准确指定该组合的槽, 包括 `domain` 当组合 Tess, 如 `domain: "light"` 。 `response`是完全得到的响应,按字符比较.

> [!IMPORTANT]
> 每个句子模板必须至少匹配一个测试句. 在从未使用模板时,测试失败并列出未测试模板. 所以,当您添加一个模板时,添加一个达到它的测试句.

## 固定设备 {#fixtures}

测试文件顶部的楼层、区域和铭文是它的固定装置。 它们扮演着用户在Home Assistant中设置的角色. 你只写名字 身份证是用他们做的

```yaml
language: "en"

floors:
  - name: "First Floor"

areas:
  - name: "Kitchen"
    floor: "First Floor"
  - name: "Living Room"

entities:
  - name: "Kitchen Switch"
    domain: "switch"
    area: "Kitchen"
  - name: "Curtain Left"
    domain: "cover"
    area: "Living Room"
```

实体接受:

| 密钥 | 要求数 | 含义 |
| --- | --- | --- |
| `name` | 对 | 实体使用的名称句子 |
| `domain` | 对 | 实体域, 如 `light` 或 `cover` |
| `area` | No | 在同一文件中洽谈的区域名称 |
| `state` | No | 实体状态,当答复读取时. 当口语状态与状态 Home Assistant 不同时使用 `in` 和 `out` 存储 |
| `state_with_unit` | No | 国家及其单位, 如 `22 °C` |
| `attributes` | No | 属性响应或匹配取决于。 这里有一个设备类, 如 `device_class` |
| `is_exposed` | No | 为未接触Assist的实体设定为`false`。 答案就省略了 比如从回答到关于状态的问题 |

```yaml
entities:
  - name: "Living Room Window"
    domain: "cover"
    state: "open"
    attributes:
      device_class: "window"
```

给出定着物的具体名称,如"Garage Door Left"或"Curtains Left",而不是"garage door"等通用名称. 否则,如"打开车库门"这样的句子的测试,除了某种设备之外,不能说出一个名字.

## 计时器和媒体 {#timers-and-media}

与定时器或媒体合作的意向者宣布它们与其他固定装置一样. 把它们放在所有组的文件的顶端, 或者放在一个组里 :

```yaml
# tests/en/HassTimerStatus/area_only.yaml {#testsenhasstimerstatusareaonlyyaml}
language: "en"

areas:
  - name: "Kitchen"

timers:
  - is_active: true
    area: "Kitchen"
    start_minutes: 5
    total_seconds_left: 180
    rounded_hours_left: 0
    rounded_minutes_left: 3
    rounded_seconds_left: 0

tests:
  - sentences:
      - "how much time is left on the kitchen timer"
      - "kitchen timer status"
    slots:
      area: "Kitchen"
    response: "3 minutes left."
```

计时器需要至少一个`start_hours`,`start_minutes`,或`start_seconds`,以及所有`total_seconds_left`,`rounded_hours_left`,`rounded_minutes_left`,和`rounded_seconds_left`。`name`,`area`和`is_active`都是可选的。

一个媒体项目只有 `title` :

```yaml
# tests/en/HassMediaSearchAndPlay/area_only.yaml {#testsenhassmediasearchandplayareaonlyyaml}
language: "en"

areas:
  - name: "Kitchen"

media:
  - title: "The Office"

tests:
  - sentences:
      - "play The Office in the Kitchen"
    slots:
      search_query: "The Office"
      area: "Kitchen"
    response: "Playing media"
```

## 背景领域 {#context-areas}

一些槽组合在 `intents.yaml` 中有 `context_area: true` 。 他们的地区来自语音卫星,而不是句子,就像"这里的真空"一样. Home Assistant把那个区域的名字传过去,所以像`Cleaning {{ slots.area }}`这样的反应还是说真名。

在这样的组合的测试文件中,标记卫星与 `context_area: true` 所在区域,并在答复中写出其名称:

```yaml
# tests/en/HassVacuumCleanArea/context_area.yaml {#testsenhassvacuumcleanareacontextareayaml}
language: "en"

areas:
  - name: "Living Room"
    context_area: true

tests:
  - sentences:
      - "vacuum in here"
      - "clean this room"
    response: "Cleaning Living Room"
```

只有一个区域可以被标记,并且只能在一个与 `context_area: true` 组合的文件中. 反应读取的实体必须位于标记区域,因为卫星区域就像口头区域一样过滤实体。 没有标记区域,测试使用占位符名称,`__context_area__`.

## 运行测试 {#run-the-tests}

运行语言测试 :

```shell
pytest tests --language en
```

离开 `--language` 测试每种语言, 添加 `-k <intent>` 测试一种意图, 并添加 `-n auto` 平行运行 。 在 VS 代码或代码空间中, ** Terminal ** > ** Run Task ** > ** 当前文件的运行测试** 验证您的语言并运行您打开的文件的测试 。
