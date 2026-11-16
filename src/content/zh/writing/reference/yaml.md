---
title: YAML 样式
description: 文档中的YAML示例应如何外观,因此易于阅读,复制和适应.
order: 3
---

# YAML 样式 {#yaml-style}

人们将YAML实例直接复制到自己的配置中. 当每一个例子都遵循相同的风格时,它们更容易阅读,更容易比较,也更容易第一次正确.

本页分两部分. 第一个涵盖平原YAML,并适用于您写的任何YAML. 第二种涵盖Home Assistant特有的选择,其中同一事物可以不止一个方式写成.

## 也门将军 {#general-yaml}

### 缩进 {#indentation}

缩进两个空格.

```yaml
# Good {#good}
lighting:
  brightness: 80

# Bad {#bad}
lighting:
    brightness: 80
```

### 布尔 {#booleans}

小写中只使用 `true` 和 `false` 。 像`yes`,`no`,`on`,和`off`这样的值看起来是友好的,但它们迷惑了那些新到YAML的人. YAML 1.2 也丢弃了它们作为布尔语, 因此坚持 `true` 和 `false` 保留将来的例子 。

```yaml
# Good {#good-1}
enabled: true
visible: false

# Bad {#bad-1}
enabled: True
visible: off
debug: yes
```

### 评论 {#comments}

评论帮助读者理解一个例子的作用.

- 把评论放在自己的线上,放在它解释的线上. 一行末尾的评论在小屏幕上很难阅读.
- 缩进与其所属行的等值的注释.
- 在 `#` 之后设置一个空格, 用大写字母开始注释 。

```yaml
# Good {#good-2}
sensor:
  

# Check every five minutes {#acceptable-but-prefer-the-style-above}
  scan_interval: 300

# Acceptable, but prefer the style above {#bad-2}
sensor:
  scan_interval: 300 

# Check every five minutes {#check-every-five-minutes}

# Bad {#lists}
sensor:
# Check every five minutes {#good-3}
  scan_interval: 300
  #Check every five minutes
  timeout: 10
  

# check every five minutes {#bad-3}
  retries: 3
```

### 列表 {#acceptable}

YAML称它们为序列. 在文档中,叫他们名单。

以块样式写列表,每个项目缩进其键下.

```yaml
# Good {#bad-4}
colors:
  - red
  - green
  - blue

# Bad {#mappings}
colors:
- red
- green
- blue
```

避免流体样式,带有方括号的内衬形式. 它看起来很紧凑,但一旦值增长,就很难阅读. 如果使用它,请在每个逗号后面放置一个空格,括号内没有空格。

```yaml
# Acceptable {#good-4}
colors: [red, green, blue]

# Bad {#bad-5}
colors: [ red, green, blue ]
colors: [red,green,blue]
lights: ["light.living_room_window", "light.living_room_corner"]
```

### 绘图 {#null-values}

绘图也被称为词典,散列表,或键/值对. 在文档中,称他们为绘图.

总是用块一声的风格写映射. 类似JS一声的流体风格是不允许的.

```yaml
# Good {#good-5}
position:
  x: 10
  y: 20

# Bad {#bad-6}
position: { x: 10, y: 20 }
```

### 数值 {#strings}

留下一个空值 。 不要写 `null` 或 `~` 。

```yaml
# Good {#good-6}
history:

# Bad {#avoid}
history: null
history: ~
```

### 字符串 {#bad-7}

以双引法引引弦. Home Assistant 示例中的一些值是一个例外, 见[未引用的字符串](/writing/reference/yaml#strings-that-stay-unquoted) 。

```yaml
# Good {#long-strings}
greeting: "Welcome home!"

# Avoid {#good-7}
greeting: Welcome home!

# Bad {#bad-8}
greeting: 'Welcome home!'
```

### 长弦 {#home-assistant-yaml}

不要使用 `\n` 添加换行符, 不要在单行上写长字符串 。 使用区块缩写:

- 字面样式 `|` 保留您所写的行折 。
- 折叠的样式 `>` 将线条合并为一条, 并在它们之间有一个空格 。

```yaml
# Good {#leave-out-defaults-and-empty-sections}
message: |
  The washing machine is done.
  Time to empty it.
summary: >
  This text is spread over several lines in YAML,
  but Home Assistant reads it as one single line.

# Bad {#good-8}
message: "The washing machine is done.\nTime to empty it.\n"
```

首选 `|` 和 `>` , 但没有选择指标 。 如果一个实例需要在结尾处对换行符进行不同的处理,则可以使用:

- 条形指示符 `|-` 或 `>-` 来删除最后的换行符和之后的任何空行 。
- 保留指示符 `|+` 或 `>+`, 以保留最后的换行符和其后的任何空行 。

## Home AssistantYAML 语言 {#bad-9}

Home Assistant经常接受一个以上形式的相同配置. 这些规则选一个,所以所有的例子都相像.

### 删除默认和空节 {#placeholders}

不包含设置为默认值的选项。 这一例外是一个具体涉及这一选择的例子。

对于空的区段,如`conditions: []`或`data: {}`,以及`mode: single`,也是相同的,这是自动化和脚本的默认模式.

```yaml
# Good {#strings-that-stay-unquoted}
triggers:
  - trigger: state
    entity_id: binary_sensor.front_door
actions:
  - action: light.turn_on
    target:
      entity_id: light.hallway

# Bad {#good-9}
mode: single
triggers:
  - trigger: state
    entity_id: binary_sensor.front_door
conditions: []
actions:
  - action: light.turn_on
    target:
      entity_id: light.hallway
    data: {}
```

### 占位符 {#bad-10}

当读者必须填写一个值时,将占位符写在首都,在词之间加下划线. 这使得什么是明显的替代。

```yaml
api_key: YOUR_API_KEY
host: YOUR_DEVICE_IP_ADDRESS
```

写入实例, 让他们在 `configuration.yaml` 文件中工作, 除非文本另有明确表述 。

### 未引用的字符串 {#action-targets}

字符串得到双引号,只有一个例外. 以下的值比较容易读而不引用,所以不要引用:

- 实体标识, 如 `binary_sensor.front_door`
- 实体属性, 如 `temperature`
- 设备标识
- 区域标识
- 平台类型, 如 `light` 或 `switch`
- 触发类型, 如 `state` 或 `time`
- 条件类型, 如 `state` 或 `numeric_state`
- 动作名称, 如 `light.turn_on`
- 设备类, 如 `motion` 或 `problem`
- 事件名称
- 在自动化中只接受一组固定选项的值, 如 `mode`

```yaml
# Good {#good-10}
actions:
  - action: notify.mobile_app_phone
    data:
      message: "The front door is open."
  - action: light.turn_on
    target:
      entity_id: light.hallway
      area_id: entrance
    data:
      transition: 5

# Bad {#bad-11}
actions:
  - action: "notify.mobile_app_phone"
    data:
      message: The front door is open.
```

### 行动目标 {#a-single-value-or-a-list-of-values}

您可以在 `target` 下, 直接在 `data` 下, 或在 `data` 内, 指向一个实体 。 总是使用`target`.

这是最灵活的选择。 除了实体,一个目标可以持有设备,区域,地板,和标签,你可以将它们组合起来.

```yaml
# Good {#good-11}
actions:
  

# Target one entity {#good-12}
  - action: light.turn_on
    target:
      entity_id: light.living_room
  

# Target every light in an area {#bad-12}
  - action: light.turn_on
    target:
      area_id: living_room
  

# Combine an area, an entity, and a device {#bad-13}
  - action: light.turn_on
    target:
      area_id: living_room
      entity_id: light.office_desk
      device_id: 8f2b6e4c1a9d4e7b9c3f5a1d2e6b8c4f

# Bad {#bad-14}
actions:
  - action: light.turn_on
    entity_id: light.living_room
  - action: light.turn_on
    data:
      entity_id: light.living_room
```

### 单个值或数值列表 {#a-single-mapping-or-a-list-of-mappings}

许多选项要么接受一个值,要么 86. 一些人还接受一个逗号分隔 86. 对于这些选项:

- 只有一个值时使用单一值 。 不要将其包装在列表中。
- 多个时使用块样式列表 。
- 从不将数个值放在一个逗号分隔的字符串中 。

```yaml
# Good {#good-13}
entity_id: light.living_room

# Good {#bad-15}
entity_id:
  - light.living_room
  - light.kitchen

# Bad {#templates}
entity_id: light.living_room, light.kitchen

# Bad {#good-14}
entity_id: [light.living_room, light.kitchen]

# Bad {#bad-16}
entity_id:
  - light.living_room
```

### 单一绘图或绘图列表 {#quotes-in-templates}

如`triggers`,`conditions`,`actions`和`sequence`等选项接受一次映射或一张映射列表. 总是使用列表, 即使只有一个项目 。

列表显示读者可以添加更多项目. 它还让他们将一个项目复制到自己的配置中而不改变其形状.

```yaml
# Good {#good-15}
actions:
  - action: light.turn_on
    target:
      entity_id: light.living_room

# Bad {#bad-17}
actions:
  action: light.turn_on
  target:
    entity_id: light.living_room
```

## 模板 {#long-templates}

模板虽然强大,但对于新人来说却很难阅读. 如果普通的YAML可以做这个工作,则用它来代替.

还有一个原因。 在{L奠定了}上,模板需要额外的逃逸,所以网站不会错误地将它们用于液态. 见[目录](/writing/reference/liquid)。 没有模板,没有逃跑。

```yaml
# Good {#good-16}
conditions:
  - condition: numeric_state
    entity_id: sun.sun
    attribute: elevation
    below: 4

# Bad {#bad-18}
conditions:
  - condition: template
    value_template: "{{ state_attr('sun.sun', 'elevation') < 4 }}"
```

### 在模板中引用 {#short-condition-syntax}

模板是字符串,因此得到双引号. 在模板内使用单引号.

```yaml
# Good {#good-17}
greeting: "{{ 'Good morning' if now().hour < 12 else 'Hello' }}"

# Bad {#bad-19}
greeting: '{{ "Good morning" if now().hour < 12 else "Hello" }}'
```

### 长模板 {#filters}

将一个长模板拆分到多行上,这样读者就可以遵循逻辑. 如 [长弦](/writing/reference/yaml#long-strings) 所述, 使用块标 。

```yaml
# Good {#good-18}
conditions:
  - >-
    {{
      is_state('lock.front', 'locked')
      and is_state('lock.back', 'locked')
    }}

# Bad {#bad-20}
conditions:
  - "{{ is_state('lock.front', 'locked') and is_state('lock.back', 'locked') }}"
```

不好的例子还很短。 想象它还有五个条件, 你明白它为什么没有规模。

### 将能够使用语言语言的语法 {#states-and-attributes}

对于模板条件,使用简称. 它短而干净。

```yaml
# Good {#good-19}
conditions: "{{ states('sensor.outdoor_temperature') | float(0) > 25 }}"

# Bad {#bad-21}
conditions:
  - condition: template
    value_template: >-
      {{ states('sensor.outdoor_temperature') | float(0) > 25 }}
```

### 过滤器 : {#过滤器}

在过滤管两侧放置一个空间, `|`. 如果这样使这一表述变得不明确,则加上括号。

```yaml
# Good {#good}
conditions:
  - "{{ states('sensor.humidity') | float(0) > 60 }}"
  - "{{ target == (states('input_number.target') | int(0)) }}"

# Bad {#bad}
conditions:
  - "{{ states('sensor.humidity')|float(0) > 60 }}"
  - "{{ target == (states('input_number.target')|int(0)) }}"
```

### 国家和属性 {#国家和属性}

使用帮助函数读取状态和属性: `states()`,`is_state()`,`state_attr()`,和`is_state_attr()`. 不要直接从 `states` 对象读取 。

帮助者处理尚未准备好的实体, 如 Home Assistant 启动期间 。 读取 `states` 对象时会直接产生错误 。

```yaml
# Good {#good}
temperature: "{{ states('sensor.temperature') }}"
target: "{{ state_attr('climate.living_room', 'temperature') }}"

# Bad {#bad}
temperature: "{{ states.sensor.temperature.state }}"
target: "{{ states.climate.living_room.attributes.temperature }}"
```
