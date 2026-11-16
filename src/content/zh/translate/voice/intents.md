---
title: 内设意图
description: 每一个意图 Home Assistant  毫无疑问, 它的插槽、 插槽组合, 以及处理它的综合。
order: 9
---

# 内设意图 {#built-in-intents}

[意图](/glossary/intent)是句子的意思,以Home Assistant的形式可以采取行动. 本页面列出[意图存储器](https://github.com/OHF-Voice/intents)中所有有句子的意向,因此可以使用覆盖它的每一种语言来表达.

此列表的来源是意图寄存器 [`intents.yaml`](https://github.com/OHF-Voice/intents/blob/main/intents.yaml) 。 这是这个网站的完整名单。 处理意向的代码存在于 Home Assistant Core : [核心内置意图](/core/internals/built-in-intents) 显示每个处理者住在哪里, [意图](/core/internals/intents) 解释如何从自己的代码中写一个处理者或火的意向 。

## 如何阅读此页面 {#how-to-read-this-page}

每项意图清单:

- ** Slots **:句豺可以填充的信息片段,如设备的`name`或`area` 进去了 为工作目的,必须填补按要求标明的空档。
- **响应变量**:一个响应模板除了`slots`以外还可以使用的额外值. 见[答复](/translate/voice/template-syntax#responses).
- **槽组合**:句子可以填充的槽组,每个槽组都有一个英文实例. 判决和测试按槽组合排列. "卫星区域"表示该圆满完成话:来自听话的语音卫星.

一个槽组合制定关于语言需要多少: `required`(最小的,没有它的验证失败),`usable`(人们期望的),`complete`(全覆盖的需要),或`optional`(外). 对于以 `name` 或以 `domain` 推断的 `domain` 为目标实体的组合, 每个实体域都设定了重要性 。 该表显示其任何领域的最高水平。 详细情况

`name`,`area`和`floor`由用户的Home Assistant中存在的内容填充:其暴露的实体名称,区域,以及地板.

## 设备和实体 {#devices-and-entities}

### 已经打开 {#hassturnon}

打开一个设备或实体。 由`intent`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |
| `floor` | No | 楼层名称 |
| `domain` | No | 目标装置或实体的领域 |
| `device_class` | No | 目标设备或实体的设备类别 |

[H的主要目标]
槽组合(12</summary>)

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `domain_only` | `domain`(卫星区) | 所需经费 | 打开这里的灯 |
| `name_only` | `name` | 所需经费 | 打开上面的灯光 |
| `area_domain` | `area`, `domain` | 所需经费 | 打开厨房的灯光 |
| `floor_domain` | `floor`, `domain` | 选项 | 打开一楼的灯 |
| `device_class_cover` | `domain`,`device_class`(卫星区域) | 完成 | 打开这里的窗户 |
| `name_area` | `name`, `area` | 完成 | 打开厨房的灯光 |
| `name_floor` | `name`, `floor` | 选项 | 打开一楼的灯光 |
| `name_script` | `name` | 完成 | 运行派对时间脚本 |
| `name_scene` | `name` | 完成 | 启动情绪照明场景 |
| `name_area_scene` | `name`, `area` | 完成 | 启动客厅的情绪照明场景 |
| `area_device_class_cover` | `area`, `domain`, `device_class` | 完成 | 有没有打开客厅的窗帘 |
| `floor_device_class_cover` | `floor`, `domain`, `device_class` | 选项 | 打开一楼的窗帘 |

</details>

### 急转弯 {#hassturnoff}

关闭一个设备或实体。 由`intent`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |
| `floor` | No | 楼层名称 |
| `domain` | No | 目标装置或实体的领域 |
| `device_class` | No | 目标设备或实体的设备类别 |

<details>
区间组合 (10)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `domain_only` | `domain`(卫星区) | 所需经费 | turn off the lights in here |
| `name_only` | `name` | 所需经费 | 关掉高架灯光 |
| `area_domain` | `area`, `domain` | 所需经费 | 把厨房的灯关了 |
| `floor_domain` | `floor`, `domain` | 选项 | 一楼的灯关了 |
| `device_class_cover` | `domain`,`device_class`(卫星区域) | 完成 | 关上这里的窗户 |
| `name_area` | `name`, `area` | 完成 | 把厨房的灯关掉 |
| `name_floor` | `name`, `floor` | 选项 | 把一楼的灯关了 |
| `area_device_class_cover` | `area`, `domain`, `device_class` | 完成 | 37. 关闭客厅的窗帘 |
| `floor_device_class_cover` | `floor`, `domain`, `device_class` | 选项 | 关上一楼的窗帘 |
| `domain_all` | `domain` | 选项 | 把家里的灯都关了 |

</details>

### HassGet状态 {#hassgetstate}

获取或检查实体的状况。 由`intent`整合处理 Alabama.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |
| `floor` | No | 楼层名称 |
| `domain` | No | 目标装置或实体的领域 |
| `device_class` | No | 目标设备或实体的设备类别 |
| `state` | No | 要匹配的状态名称 |

响应变量: `state`(第一个实体匹配的状态),`query.matched`(匹配查询和状态名称的状态列表),`query.unmatched`(匹配除状态名称以外的所有事物的状态列表充分地匹配).

[H的主要目标]
槽组合(12</summary>)

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `name_only` | `name` | 完成 | 外面的温度是多少 |
| `name_state` | `name`, `state` | 完成 | 滑动门是否打开 |
| `name_state_area` | `name`, `state`, `area` | 完成 | 车库门是打开的 |
| `name_state_floor` | `name`, `state`, `floor` | 完成 | 二楼的卧室窗户是打开的 |
| `name_where` | `name` | 完成 | 简在哪里? |
| `name_zone` | `name`, `state` | 完成 | 是简家 |
| `domain_state` | `domain`, `state` | 完成 | 所有的灯都关了 |
| `domain_state_area` | `area`, `domain`, `state` | 完成 | 厨房里有灯光 |
| `domain_state_floor` | `floor`, `domain`, `state` | 完成 | 一楼所有的灯都关了 |
| `device_class_state` | `domain`, `device_class`, `state` | 完成 | 全部关闭窗口 |
| `device_class_state_area` | `area`, `domain`, `device_class`, `state` | 完成 | 卧室的窗户都关上了 |
| `device_class_state_floor` | `floor`, `domain`, `device_class`, `state` | 完成 | 二楼所有的窗户都关闭了 |

</details>

### 馅饼 {#hasssetposition}

设置一个实体的位置。 由`intent`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |
| `floor` | No | 楼层名称 |
| `domain` | No | 目标装置或实体的领域 |
| `device_class` | No | 目标设备或实体的设备类别 |
| `position` | 对 | 职位从0至100 |

<details>
键盘组合 (6)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `name_only` | `name`, `position` | 完成 | 将窗帘设为50% |
| `device_class` | `domain`,`device_class`,`position`(卫星区) | 完成 | 把窗帘设为50% |
| `area_device_class` | `area`, `domain`, `device_class`, `position` | 完成 | 在卧室把窗帘设为50% |
| `name_area` | `name`, `area`, `position` | 选项 | set the curtain left in the living room to 50% |
| `name_floor` | `name`, `floor`, `position` | 选项 | 将主楼的窗帘设为50% |
| `floor_device_class` | `floor`, `domain`, `device_class`, `position` | 选项 | 将主楼的窗帘设为50% |

</details>

## 来吧 {#conversation}

### 永远不在乎 {#hassnevermind}

无所作为. 曾取消请求. 由`intent`整合处理.

这种意图没有插槽.

<details>
区位组合 (1)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无 | 可用 | 无所谓 |

</details>

### 散列响应 {#hassrespond}

返回响应,但不采取行动。 由`intent`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `response` | No | 要回复的文本 |

<details>
区位组合 (1)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无 | 选项 | 哈啰 |

</details>

### 哈斯广播 {#hassbroadcast}

在其它卫星上发布消息. 由`assist_satellite`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `message` | 对 | 要播放的信件 |

<details>
区位组合 (1)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `message_only` | `message` | 选项 | 广播晚餐准备好了 |

</details>

## 日期和时间 {#date-and-time}

### HassGet 当前数据 {#hassgetcurrentdate}

获得当前日期。 由`intent`整合处理.

这种意图没有插槽.

响应变量:`date`(日期对象与日,月,年).

<details>
区位组合 (1)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无 | 可用 | 何为日期 |

</details>

### 当前时间 {#hassgetcurrenttime}

获取当前时间 。 由`intent`整合处理。

这种意图没有插槽.

反应变量:`time`(时间对象有小时,分,秒).

<details>
区位组合 (1)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无 | 可用 | 几点了 |

</details>

## 灯光和粉丝 {#lights-and-fans}

### 散点灯集 {#hasslightset}

设置光线的亮度或颜色。 由`light`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `domain` | No | 目标装置或实体的领域 |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |
| `floor` | No | 楼层名称 |
| `brightness` | No | 各派比例 |
| `color` | No | 颜色名称 |
| `temperature` | No | 1000到1000开尔文的颜色温度 |

[H的主要目标]
槽组合(12</summary>)

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `name_brightness` | `name`, `brightness` | 可用 | 将上面的亮度设为50% |
| `name_color` | `name`, `color` | 可用 | 将上面的光线设置为红色 |
| `name_temperature` | `name`, `temperature` | 可用 | 将灯光颜色温度设定为 2700 开尔文 |
| `brightness_only` | `brightness`,`domain`(卫星区域) | 完成 | 将这里的亮度设置为 50% |
| `area_brightness` | `area`, `brightness`, `domain` | 完成 | 将客厅亮度设定为50% |
| `floor_brightness` | `floor`, `brightness`, `domain` | 完成 | 将主楼的亮度设定为50% |
| `color_only` | `color`,`domain`(卫星区域) | 完成 | 把这里的灯放红 |
| `area_color` | `area`, `color`, `domain` | 完成 | 将客厅设为红色 |
| `floor_color` | `floor`, `color`, `domain` | 完成 | 将主楼设为红色 |
| `temperature_only` | `temperature`,`domain`(卫星区域) | 完成 | 将这里的亮色温度设置为 2700 开尔文 |
| `area_temperature` | `area`, `temperature`, `domain` | 完成 | 将客厅亮色温度设定为2700开尔文 |
| `floor_temperature` | `floor`, `temperature`, `domain` | 完成 | 将主楼层颜色温度设置为 2700 开尔文 |

</details>

### HassFanSet 设置 {#hassfansetspeed}

设置风扇的速度。 由`fan`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |
| `floor` | No | 楼层名称 |
| `percentage` | 对 | 速度百分比从0到100 |

<details>
区块组合 (4)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | `percentage`(卫星区) | 完成 | 将风扇设置为50% |
| `name_only` | `name`, `percentage` | 完成 | 将天花板扇设为50% |
| `area_only` | `area`, `percentage` | 完成 | 将厨房风扇设置为50% |
| `floor_only` | `floor`, `percentage` | 完成 | 将一楼的风扇设置妇女参与政治活动 |

</details>

## 气候和天气 {#climate-and-weather}

### HassClimateSet 温度 {#hassclimatesettemperature}

设定所需的室内温度。 由`climate`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |
| `floor` | No | 楼层名称 |
| `temperature` | 对 | 温度( 度) |

<details>
区块组合 (4)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `temperature_only` | `temperature`(卫星区) | 完成 | 将温度设定为30度 |
| `name_temperature` | `name`, `temperature` | 完成 | 将"一个""""一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个"一个" |
| `area_temperature` | `area`, `temperature` | 完成 | 将卧室温度设定为30度 |
| `floor_temperature` | `floor`, `temperature` | 完成 | 将主楼的温度设定为30度 |

</details>

### HassClimate 获取温度 {#hassclimategettemperature}

获得实际室内温度,而不是`HassClimateSetTemperature`设定的目标温度。 由`intent`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |
| `floor` | No | 楼层名称 |

响应变量: `state`(包含温度的实体状态).

<details>
区块组合 (4)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无(卫星区) | 可用 | 温度是多少 |
| `name_only` | `name` | 可用 | 什么是生态蜂的温度 |
| `area_only` | `area` | 可用 | 卧室的温度是多少 |
| `floor_only` | `floor` | 完成 | 楼下温度多少? |

</details>

### 其间: {#hassclimatesetfanmode}

设置气候设备的风扇模式。 由`climate`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |
| `floor` | No | 楼层名称 |
| `fan_mode` | 对 | 要设置的扇形模式 |

<details>
区块组合 (4)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `fan_mode_only` | `fan_mode`(卫星区) | 完成 | 将风扇模式设置为蟹类 |
| `name_fan_mode` | `name`, `fan_mode` | 完成 | 将 EcoBee 风扇设置为自动 |
| `area_fan_mode` | `area`, `fan_mode` | 完成 | 将卧室风扇模式设置为低 |
| `floor_fan_mode` | `floor`, `fan_mode` | 完成 | 将一楼的风扇模式设置为低 |

</details>

### Hass GetWeather 软件 {#hassgetweather}

获得当前天气. 由`weather`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 要使用的天气实体名称 |

反应变量: `state` (包含天气的实体状态).

<details>
时间档组合(2)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无 | 可用 | 天气怎么样? |
| `name_only` | `name` | 可用 | 纽约的天气如何 |

</details>

## 列表 {#lists}

### 购物列表添加项目 {#hassshoppinglistadditem}

将项目添加到购物列表中。 由`shopping_list`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `item` | 对 | 要添加的项目 |

<details>
区位组合 (1)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `item_only` | `item` | 选项 | talk. 将苹果添加到我的购物列表中 |

</details>

### HassSchishList 完成项目 {#hassshoppinglistcompleteitem}

Opera 检查购物列表中的物品。 Opera 由`shopping_list`整合处理。

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `item` | 对 | 要检查的项目 |

<details>
区位组合 (1)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `item_only` | `item` | 选项 | 从我的购物名单上检查苹果 |

</details>

### Hass的了解添加项目 {#hasslistadditem}

在待办事宜列表中添加项目。 由`todo`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `item` | 对 | 要添加的项目 |
| `name` | 对 | 名单名称 |

<details>
区位组合 (1)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `name_item` | `item`, `name` | 完成 | talk. 将苹果添加到我的购物列表中 |

</details>

### HassList 完成项目 {#hasslistcompleteitem}

从待办事宜列表中检查项目 。 由`todo`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `item` | 对 | 要检查的项目 |
| `name` | 对 | 名单名称 |

<details>
区位组合 (1)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `name_item` | `item`, `name` | 完成 | 帮我把杂事单上的垃圾拿出来 |

</details>

### HassListRemove 项目 {#hasslistremoveitem}

从待办事宜列表中删除项目。 由`todo`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `item` | 对 | 要删除的项目 |
| `name` | 对 | 名单名称 |

<details>
区位组合 (1)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `name_item` | `item`, `name` | 完成 | 把垃圾从我的杂务清单里拿出来 |

</details>

## 媒体 {#media}

### HassMediaP有利的环境 {#hassmediapause}

暂停媒体播放器 。 由`media_player`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |

<details>
时间档组合(3)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无(卫星区) | 可用 | 暂停 |
| `name_only` | `name` | 可用 | 暂停电视 |
| `area_only` | `area` | 可用 | 在厨房暂停音乐 |

</details>

### HassMedia 不暂停 {#hassmediaunpause}

未暂停媒体播放器 。 由`media_player`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |

<details>
时间档组合(3)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无(卫星区) | 可用 | 恢复 |
| `name_only` | `name` | 可用 | 恢复电视 |
| `area_only` | `area` | 可用 | 在厨房恢复音乐 |

</details>

### Hass 媒体下一步 {#hassmedianext}

跳过媒体播放器到下一个项目。 由`media_player`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |

<details>
时间档组合(3)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无(卫星区) | 可用 | 下一个音轨 |
| `name_only` | `name` | 可用 | 立体声上的下一曲 |
| `area_only` | `area` | 可用 | 厨房的下一个轨道 |

</details>

### HassMedia 上一个 {#hassmediaprevious}

将媒体播放器跳转到上一个项目。 由`media_player`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |

<details>
时间档组合(3)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无(卫星区) | 完成 | 前一个音轨 |
| `name_only` | `name` | 完成 | 音响上的上一音轨 |
| `area_only` | `area` | 完成 | 厨房的上一个音轨 |

</details>

### 组合组合 {#hasssetvolume}

设置媒体播放器的音量。 由`media_player`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |
| `volume_level` | 对 | 量级从0到100 |

<details>
时间档组合(3)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | `volume_level`(卫星区) | 完成 | 将音量设定为50% |
| `name_only` | `name`, `volume_level` | 完成 | 将电视音量联合国系统各占50% |
| `area_only` | `area`, `volume_level` | 完成 | 厨房容量设定为50% |

</details>

### 散列旋转 {#hasssetvolumerelative}

增加或减少媒体播放器的音量。 由`media_player`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `volume_step` | 对 | 上、下或从 -100 到 100 的百分比变化 |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |
| `floor` | No | 楼层名称 |

<details>
区块组合 (4)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | `volume_step`(卫星区) | 完成 | 增加数量 |
| `name_only` | `volume_step`, `name` | 完成 | 减少电视量 |
| `area_only` | `volume_step`, `area` | 完成 | 厨房数量减少 |
| `floor_only` | `volume_step`, `floor` | 完成 | 一楼增加量 |

</details>

### Hass 媒体显示器 {#hassmediaplayermute}

调音媒体播放器 。 由`media_player`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |

<details>
时间档组合(2)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无(卫星区) | 完成 | 哑弹 |
| `name_only` | `name` | 完成 | 关掉电视 |

</details>

### Hass 媒体显示器解密 {#hassmediaplayerunmute}

解除媒体播放器。 由`media_player`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |

<details>
时间档组合(2)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无(卫星区) | 完成 | 解密( M) |
| `name_only` | `name` | 完成 | 打开电视 |

</details>

### Hass 媒体搜索和播放 {#hassmediasearchandplay}

搜索媒体项目并播放. 由`media_player`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |
| `search_query` | 对 | 要搜索和播放的媒体 |
| `media_class` | No | 要搜索的媒体类型( album, app, 艺术家, 频道, 作曲家, 贡献  艺术家, 目录, 插曲, 游戏, 流派, 图像, 电影, 音乐, 播放列表, 播客, 季节, 音轨, tv  show, url, 视频) |

响应变量 : `media` (匹配的介质项目作为 `BrowseMedia` 对象, 或 `None` 当搜索无结果时) 。

<details>
区间组合 (8)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | `search_query`(卫星区) | 选项 | 播放 Pink Floyd 游戏 |
| `name_only` | `name`, `search_query` | 选项 | 播放 Pink Floyd 在索诺斯演讲器上 |
| `area_only` | `area`, `search_query` | 选项 | 在生活室播放粉红色弗洛伊德 |
| `name_area` | `name`, `area`, `search_query` | 选项 | 在客厅的索泾演讲者上演奏粉红色弗洛伊德 |
| `media_class_only` | `search_query`,`media_class`(卫星区域) | 选项 | 播放提示播放列表 |
| `name_media_class` | `name`, `search_query`, `media_class` | 选项 | 硕诺斯演讲者专辑 |
| `area_media_class` | `area`, `search_query`, `media_class` | 选项 | 在生活室播放粉红弗洛伊德电影 |
| `name_area_media_class` | `name`, `area`, `search_query`, `media_class` | 选项 | 在生活室的索诺斯演讲者上播放粉红弗洛伊德播客 |

</details>

## 计时器 {#timers}

### HassStart 计时器 {#hassstarttimer}

开始计时器。 由`intent`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `hours` | No | 小时数 |
| `minutes` | No | 分钟数 |
| `seconds` | No | 秒数 |
| `name` | No | 附于计时器的名称 |
| `conversation_command` | No | 定时器完成时执行的命令 |

<details>
时间档组合 (21)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `hours_only` | `hours` | 可用 | 梢机1小时 |
| `minutes_only` | `minutes` | 可用 | 设置10分钟的计时器 |
| `seconds_only` | `seconds` | 可用 | 设置30秒的计时器 |
| `hours_minutes` | `hours`, `minutes` | 完成 | 设置1小时10分钟的计时器 |
| `hours_seconds` | `hours`, `seconds` | 完成 | 设置1小时30秒的计时器 |
| `minutes_seconds` | `minutes`, `seconds` | 完成 | 设定10分30秒的计时器 |
| `hours_minutes_seconds` | `hours`, `minutes`, `seconds` | 完成 | 设定1小时10分30秒的计时器 |
| `name_hours` | `name`, `hours` | 完成 | 设置1小时的计时器,命名为披萨 |
| `name_minutes` | `name`, `minutes` | 完成 | 设置一个定时器 10分钟,命名为披萨 |
| `name_seconds` | `name`, `seconds` | 完成 | 设置一个ý30秒的定时器,命名为披萨 |
| `name_hours_minutes` | `name`, `hours`, `minutes` | 完成 | 设定1小时10分钟的计时器,命名为披萨 |
| `name_hours_seconds` | `name`, `hours`, `seconds` | 完成 | 设置1小时30秒的定时器,命名为披萨 |
| `name_minutes_seconds` | `name`, `minutes`, `seconds` | 完成 | 设定定时器10分30秒,命名为披萨 |
| `name_hours_minutes_seconds` | `name`, `hours`, `minutes`, `seconds` | 完成 | 定时器1小时10分30秒 命名为披萨 |
| `command_hours` | `conversation_command`, `hours` | 选项 | 1小时后关灯 |
| `command_minutes` | `conversation_command`, `minutes` | 选项 | 十分钟后关灯 |
| `command_seconds` | `conversation_command`, `seconds` | 选项 | 30秒后关灯 |
| `command_hours_minutes` | `conversation_command`, `hours`, `minutes` | 选项 | 1小时10分钟后关灯 |
| `command_hours_seconds` | `conversation_command`, `hours`, `seconds` | 选项 | 1小时30秒后关灯 |
| `command_minutes_seconds` | `conversation_command`, `minutes`, `seconds` | 选项 | 10分30秒后关灯 |
| `command_hours_minutes_seconds` | `conversation_command`, `hours`, `minutes`, `seconds` | 选项 | 1小时10分30秒内关灯 |

</details>

### 取消计时器 {#hasscanceltimer}

取消计时器。 由`intent`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `start_hours` | No | 计时器开始的时间 |
| `start_minutes` | No | 分钟计时器开始 |
| `start_seconds` | No | 秒计时器开始于 |
| `name` | No | 附于计时器的名称 |
| `area` | No | 启动计时器所用的设备区域 |

<details>
键盘组合 (6)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无 | 可用 | 取消我的计时器 |
| `name_only` | `name` | 完成 | 取消比萨定时器 |
| `area_only` | `area` | 完成 | 取消厨房计时器 |
| `hours_only` | `start_hours` | 可用 | 竭力取消1小时计时器 |
| `minutes_only` | `start_minutes` | 可用 | 取消10分钟的计时器 |
| `seconds_only` | `start_seconds` | 可用 | 取消30次计时器 |

</details>

### H莹谢全时 {#hasscancelalltimers}

取消所有计时器 。 由`intent`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `area` | No | 启动计时器所用的设备区域 |

<details>
时间档组合(2)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无 | 可用 | 取消所有计时器 |
| `area_only` | `area` | 完成 | 取消厨房里的所有计时器 |

</details>

### 超时 {#hassincreasetimer}

添加时间到定时器 。 由`intent`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `hours` | No | 小时数 |
| `minutes` | No | 分钟数 |
| `seconds` | No | 秒数 |
| `start_hours` | No | 计时器开始的时间 |
| `start_minutes` | No | 分钟计时器开始 |
| `start_seconds` | No | 秒计时器开始于 |
| `name` | No | 附于计时器的名称 |
| `area` | No | 启动计时器所用的设备区域 |

<details>
区位组合 (26)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `hours_only` | `hours` | 完成 | 计时器加1小时 |
| `minutes_only` | `minutes` | 完成 | 在计时器上加十分钟 |
| `seconds_only` | `seconds` | 完成 | 在计时器中添加 30 秒 |
| `minutes_seconds` | `minutes`, `seconds` | 完成 | 在计时器上加10分30秒 |
| `hours_minutes` | `hours`, `minutes` | 完成 | 计时笋增加1小时10分 |
| `hours_seconds` | `hours`, `seconds` | 完成 | 计时器加1小时30秒 |
| `name_hours` | `name`, `hours` | 完成 | 比萨计时器加1小时 |
| `name_minutes` | `name`, `minutes` | 完成 | 应给予比萨时间10分钟 |
| `name_seconds` | `name`, `seconds` | 完成 | 在比萨定时器上加30秒 |
| `name_hours_minutes` | `name`, `hours`, `minutes` | 完成 | 比萨计时器加1小时10分钟 |
| `name_hours_seconds` | `name`, `hours`, `seconds` | 完成 | 比萨计时器加1小时30秒 |
| `area_hours` | `area`, `hours` | 完成 | 厨房计时器加1小时 |
| `area_minutes` | `area`, `minutes` | 完成 | 在厨房计时器中增加10分钟 |
| `area_seconds` | `area`, `seconds` | 完成 | 在厨房计时器中添加30秒 |
| `area_minutes_seconds` | `area`, `minutes`, `seconds` | 完成 | 在厨房计时器上加10分30秒 |
| `area_hours_minutes` | `area`, `hours`, `minutes` | 完成 | 厨房计时器加1小时10分钟 |
| `area_hours_seconds` | `area`, `hours`, `seconds` | 完成 | 厨房计时器加1小时30秒 |
| `hours_start_hours` | `start_hours`, `hours` | 完成 | 在2小时计时器中增加1小时 |
| `hours_start_minutes` | `start_minutes`, `hours` | 完成 | 在10分钟的计时器中增加1小时 |
| `hours_start_seconds` | `start_seconds`, `hours` | 完成 | 在30次计时器中增加1小时 |
| `minutes_start_hours` | `start_hours`, `minutes` | 完成 | 在计时器上加十分钟 |
| `minutes_start_minutes` | `start_minutes`, `minutes` | 完成 | 在20分钟计时器中增加10分钟 |
| `minutes_start_seconds` | `start_seconds`, `minutes` | 完成 | 在40次计时器中增加10分钟 |
| `seconds_start_hours` | `start_hours`, `seconds` | 完成 | 在计时器中添加 30 秒 |
| `seconds_start_minutes` | `start_minutes`, `seconds` | 完成 | 在20分钟计时器中添加30秒 |
| `seconds_start_seconds` | `start_seconds`, `seconds` | 完成 | 在40次计时器中添加30秒 |

</details>

### 发展中国家和转型期经济国家 {#hassdecreasetimer}

从计时器中删除时间。 由`intent`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `hours` | No | 小时数 |
| `minutes` | No | 分钟数 |
| `seconds` | No | 秒数 |
| `start_hours` | No | 计时器开始的时间 |
| `start_minutes` | No | 分钟计时器开始 |
| `start_seconds` | No | 秒计时器开始于 |
| `name` | No | 附于计时器的名称 |
| `area` | No | 启动计时器所用的设备区域 |

<details>
区位组合 (26)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `hours_only` | `hours` | 完成 | 将一个小时移到计时器 |
| `minutes_only` | `minutes` | 完成 | 去掉10分钟的计时器 |
| `seconds_only` | `seconds` | 完成 | 把30秒移到计时器 |
| `hours_minutes` | `hours`, `minutes` | 完成 | 离开1小时10分钟到计时器 |
| `hours_seconds` | `hours`, `seconds` | 完成 | 以12岁和12岁为12岁。 |
| `minutes_seconds` | `minutes`, `seconds` | 完成 | 把10分30秒移到计时器 |
| `name_hours` | `name`, `hours` | 完成 | 从比萨定时器上除去一个小时 |
| `name_minutes` | `name`, `minutes` | 完成 | 从比萨定时器上除去10分钟 |
| `name_seconds` | `name`, `seconds` | 完成 | 从比萨定时器上删除30秒 |
| `name_hours_minutes` | `name`, `hours`, `minutes` | 完成 | 从比萨定时器上移走1小时10分 |
| `name_hours_seconds` | `name`, `hours`, `seconds` | 完成 | 从比萨定时器上移走1小时30秒 |
| `area_hours` | `area`, `hours` | 完成 | 离开厨房计时器1小时 |
| `area_minutes` | `area`, `minutes` | 完成 | 从厨房计时器上移走10分钟 |
| `area_seconds` | `area`, `seconds` | 完成 | 从厨房计时器中删除30秒 |
| `area_minutes_seconds` | `area`, `minutes`, `seconds` | 完成 | 从厨房计时器上移走10分30秒 |
| `area_hours_minutes` | `area`, `hours`, `minutes` | 完成 | 离开厨房计时器1小时10分 |
| `area_hours_seconds` | `area`, `hours`, `seconds` | 完成 | 离开厨房计时器1小时30秒 |
| `hours_start_hours` | `start_hours`, `hours` | 完成 | 从2小时计时器中删除1小时 |
| `hours_start_minutes` | `start_minutes`, `hours` | 完成 | 从10分钟计时器中删除1小时 |
| `hours_start_seconds` | `start_seconds`, `hours` | 完成 | 从30次计时器中删除一个小时 |
| `minutes_start_hours` | `start_hours`, `minutes` | 完成 | 去掉10分钟的计时器 |
| `minutes_start_minutes` | `start_minutes`, `minutes` | 完成 | 从20分钟计时器中删除10分钟 |
| `minutes_start_seconds` | `start_seconds`, `minutes` | 完成 | 从40次计时器中删除10分钟 |
| `seconds_start_hours` | `start_hours`, `seconds` | 完成 | 把30秒移到计时器 |
| `seconds_start_minutes` | `start_minutes`, `seconds` | 完成 | 从20力争计时器中删除30秒 |
| `seconds_start_seconds` | `start_seconds`, `seconds` | 完成 | 从40次计时器中删除30秒 |

</details>

### HassPause 计时器 {#hasspausetimer}

暂停运行计时器 。 由`intent`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `start_hours` | No | 计时器开始的时间 |
| `start_minutes` | No | 分钟计时器开始 |
| `start_seconds` | No | 秒计时器开始于 |
| `name` | No | 附于计时器的名称 |
| `area` | No | 启动计时器所用的设备区域 |

<details>
键盘组合 (6)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无 | 可用 | 暂停我的计时器 |
| `name_only` | `name` | 完成 | 难民高专办 暂停比萨计时器 |
| `area_only` | `area` | 完成 | 暂停厨房计时器 |
| `hours_only` | `start_hours` | 完成 | 暂停1小时计时器 |
| `minutes_only` | `start_minutes` | 完成 | 暂停10分钟计时器 |
| `seconds_only` | `start_seconds` | 完成 | 暂停 30 次计时器 |

</details>

### 暂停计时器 {#hassunpausetimer}

复说暂停定时法. 由`intent`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `start_hours` | No | 计时器开始的时间 |
| `start_minutes` | No | 分钟计时器开始 |
| `start_seconds` | No | 秒计时器开始于 |
| `name` | No | 附于计时器的名称 |
| `area` | No | 启动计时器所用的设备区域 |

<details>
键盘组合 (6)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无 | 可用 | 恢复计时器 |
| `name_only` | `name` | 完成 | 恢复比萨定时器 |
| `area_only` | `area` | 完成 | 恢复厨房计时器 |
| `hours_only` | `start_hours` | 完成 | 恢复1小时计时器 |
| `minutes_only` | `start_minutes` | 完成 | 恢复10分钟计时器 |
| `seconds_only` | `start_seconds` | 完成 | 恢复30次计时器 |

</details>

### 时间状况 {#hasstimerstatus}

一个或多个计时器的报告状况。 由`intent`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `start_hours` | No | 计时器开始的时间 |
| `start_minutes` | No | 分钟计时器开始 |
| `start_seconds` | No | 秒计时器开始于 |
| `name` | No | 附于计时器的名称 |
| `area` | No | 启动计时器所用的设备区域 |

响应变量:`timers`,一个计时器对象列表. 每个计时器都有{所谓H1}(运行时为真,暂停时为假),`name`和`area`(两者都是可选的),`total_seconds_left`,`rounded_hours_left`,`rounded_minutes_left`,`rounded_seconds_left`,以及`start_hours`,`start_minutes`和`start_seconds`的计时器都是用开始的.

<details>
键盘组合 (6)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无 | 可用 | 我的计时器还剩多少时间 |
| `name_only` | `name` | 完成 | 比萨定时器上还有多少时间 |
| `area_only` | `area` | 完成 | 厨房计时器还有多少时间 |
| `hours_only` | `start_hours` | 完成 | 1小时计时器还剩多少时间 |
| `minutes_only` | `start_minutes` | 完成 | 10分钟计时器还剩多少时间 |
| `seconds_only` | `start_seconds` | 完成 | 30秒计时器还剩多少时间 |

</details>

## 真空和割草机 {#vacuums-and-lawn-mowers}

### HassVacuum 开始 {#hassvacuumstart}

2. 获得,,获得获得,获得获得,获得获得,获得,获得,获得,获得,获得,获得,获得获得,获得,获得,获得,获得,获得获得,获得,获得获得,获得获得,获得,获得,获得,获得,获得,获得获得,获得获得,,获得获得,获得获得获得,,,获得获得,,获得获得获得获得,,,,获得获得获得获得,,获得,获得,,获得,获得获得,获得,获得,,获得获得获得获得,,获得获得,获得获得获得获得获得获得获得获得,获得,获得,获得,获得,,获得获得,获得,获得获得获得获得获得获得获得获得,获得获得,获得获得获得获得获得,获得,获得获得,获得,获得,获得获得获得获得获得获得,获得获得,获得,获得获得获得,获得,获得,获得,获得,,获得获得获得,获得获得获得,获得,,,获得,获得获得获得获得获得,获得获得,获得,获得获得获得获得,获得获得获得,获得获得获得,获得获得获得,获得,,获得获得获得获得获得,获得获得获得获得获得获得,获得获得,获得获得获得获得,,,,,,,,,,,,,,,,,,,获得,,,,,,,,,,获得,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,获得,,,,,,,获得,,,,,获得,,获得,,,,获得,,,获得,,,,获得,,,,,,获得,,,,,,获得,获得,获得,,获得,,,,获得,获得,,,,获得获得,,,获得,,获得,获得,,,获得,,获得,,获得,获得,获得,,,,获得,获得获得,获得,获得获得获得,获得获得获得,获得获得获得获得获得,,获得,获得,获得获得获得,获得获得,获得,,获得获得,获得,获得获得获得获得获得获得获得获得获得获得获得获得获得,,获得,获得获得获得获得获得获得获得获得获得获得获得获得获得获得,获得获得获得获得获得获得获得获得获得获得获得获得

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |
| `floor` | No | 楼层名称 |

<details>
时间档组合(3)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `name_only` | `name` | 完成 | 开始狂欢 |
| `area_only` | `area` | 完成 | 清扫厨房 |
| `floor_only` | `floor` | 完成 | 真空主楼 |

</details>

### HassVacuum 返回数据库 {#hassvacuumreturntobase}

返回真空到基地 。 由`vacuum`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | No | 区域名称 |

<details>
时间档组合(2)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `name_only` | `name` | 完成 | 回转到基地 |
| `area_only` | `area` | 完成 | 将厨房的真空 我们会返回基地 |

</details>

### HassVacuum 清水区 {#hassvacuumcleanarea}

发送真空以清理一个区域. 由`vacuum`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |
| `area` | 对 | 需要清理的区域名称 |

<details>
时间档组合(3)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `context_area` | 无(卫星区) | 可用 | 这里的真空 |
| `area_only` | `area` | 完成 | 清扫厨房 |
| `name_area` | `name`, `area` | 完成 | 凄凉的厨房并为此扫地 |

</details>

### 多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多 {#hasslawnmowerstartmowing}

开除草机. 由`lawn_mower`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |

<details>
时间档组合(2)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无 | 完成 | 开始剪切 |
| `name_only` | `name` | 完成 | 开始剪切 |

</details>

### 哈斯劳恩莫尔多克 {#hasslawnmowerdock}

派割草机去码头 由`lawn_mower`整合处理.

| 槽 | 要求数 | 说明 |
| --- | --- | --- |
| `name` | No | 设备或实体名称 |

<details>
时间档组合(2)</summary>

| 组合 | 槽数 | 重要性有权得到 | 示例 |
| --- | --- | --- | --- |
| `default` | 无 | 完成 | 停止割伤 |
| `name_only` | `name` | 完成 | 返回剪贴底部 |

</details>

## 意向无句 {#intents-without-sentences}

Home Assistant 注册了几个在意图寄存器中没有句子的意图 。 你不能跟内置的对话代理人说 但代码仍然可以解雇他们 有些也作为使用AI模型的对话代理人的工具. 不要在意图寄存之间的互动中添加这些句子 : `intents.yaml` 不列出它们 。

| 意图 | 它会做什么 | 槽数 | 由 |
| --- | --- | --- | --- |
| `HassToggle` | 切换设备或实体 | 可选的`name`,`area`,`floor`,`domain`和`device_class` | `intent` |
| `HassStopMoving` | 停止移动并对其覆盖或阀门 | 可选的`name`,`area`,`floor`,`domain`和`device_class` | `intent` |
| `HassOpenCover` | 打开封面 使用 `HassTurnOn` 代替 | 可选的`name`,`area`,`floor`,`domain`和`device_class` | `cover` |
| `HassCloseCover` | 关闭封面。 使用 `HassTurnOff` 代替 | 可选的`name`,`area`,`floor`,`domain`和`device_class` | `cover` |
| `HassHumidifierSetpoint` | 设定目标湿度 | `name`和`humidity`(0至100),两者都需要 | `humidifier` |
| `HassHumidifierMode` | 设置加湿器的模式 | `name` 和`mode`, 两者都需要 | `humidifier` |
| `HassShoppingListLastItems` | 列出购物列表中最后五个项目 | 无 | `shopping_list` |
