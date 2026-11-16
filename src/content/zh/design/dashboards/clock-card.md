---
title: 打卡卡
description: 时钟卡显示当前时间，可以是数字时钟或模拟时钟，并可选择显示日期。
sidebarGroup: 信息
---

# 打卡卡 {#clock-card}

仪表板卡片的实时演示，来自Home Assistant演示的嵌入，连接到本网站的示例主页。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/dashboards/clock-card/)。

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "clock",
        "clock_size": "large",
        "date_format": [
          "weekday-long",
          "day-numeric",
          "month-long"
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "clock",
        "clock_style": "analog",
        "clock_size": "medium"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用方法 {#usage}

时钟卡显示时间。它适用于一直显示在屏幕上的仪表板，如走廊中的墙面平板或厨房中的屏幕，因为时间是人们首先会查看的内容之一。

在用户在手机上打开的仪表板上，可以忽略它。手机已经显示时间，而且卡片会占用他们本来要查看的内容的位置。

时间遵循用户设置的时间格式（12小时或24小时）和他们个人资料中设置的时区。它每秒更新一次，所以时间总是准确的。

### 数字或模拟 {#digital-or-analog}

默认是数字时钟。使用 `clock_style: analog` 时，卡片显示带指针的表盘。数字时钟从远处读取更快。模拟时钟更适合宁静、装饰性的仪表盘。选择一种样式并在整个仪表盘中一致使用。  

仪表盘卡片的实时演示，来自 Home Assistant 演示的嵌入，连接到本网站的示例家居。  

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "clock",
        "clock_style": "analog",
        "clock_size": "medium",
        "face_style": "numbers_upright",
        "border": true,
        "show_seconds": true
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "clock",
        "clock_style": "analog",
        "clock_size": "medium",
        "ticks": "minute"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```  

模拟时钟有其自身的选项：`face_style` 显示标记、数字或罗马数字，`ticks` 设置表盘上的刻度数量，`border` 在周围绘制一个圆圈。

### 尺寸 {#size}

`clock_size` 可以使时钟显示为 `small`、`medium` 或 `large`。在分区视图中，卡片会随着时钟的大小而增大。当时钟是屏幕上的主要内容时使用大尺寸，当它位于角落时使用小尺寸。

仪表板卡片的实时演示，来自 Home Assistant 演示的嵌入，连接到本站的示例主页。

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "clock"
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "clock",
        "clock_size": "medium"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 日期和标题 {#date-and-title}

`date_format` 在时间下方添加日期。它是一个部分列表，如星期几、日和月，因此可以遵循任何本地顺序。`title` 在时间上方添加一行文本，例如在卡片显示其他时区时间时显示城市名称。

仪表板卡片的实时演示，来自 Home Assistant 演示的嵌入，连接到本站的示例主页。

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "clock",
        "title": "Tokyo",
        "time_zone": "Asia/Tokyo",
        "clock_size": "medium"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 无背景 {#no-background}

使用`no_background: true`时，时钟周围没有卡片，直接放在仪表板上。在带有背景图片的仪表板上看起来很好。

## 配置- `clock_style`（字符串）：`digital` 或 `analog`。默认为 `digital`。 {#configuration}
- `clock_size`（字符串）：`small`、`medium` 或 `large`。默认为 `small`。
- `title`（字符串）：钟表上方的一行文字。
- `show_seconds`（布尔值）：显示秒数，或在模拟钟上显示秒针。默认为 `false`。
- `time_format`（字符串）：`12` 或 `24` 小时，`language` 跟随语言，或 `system` 跟随设备。默认为用户的时间格式。仅限数字钟。
- `time_zone`（字符串）：显示时间的时区，如 `Asia/Tokyo`。默认为用户的时区。
- `date_format`（列表）：要显示的日期部分，如 `weekday-short`、`day-numeric`、`month-long`、`year-numeric` 或分隔符。
- `no_background`（布尔值）：显示无卡片背景的钟表。默认为 `false`。
- `face_style`（字符串）：`markers`、`numbers_upright` 或 `roman`。默认为 `markers`。仅限模拟钟。

- `ticks` (字符串)：`none`、`quarter`、`hour` 或 `minute`。默认值为 `hour`。仅适用于模拟时钟。
- `border` (布尔值)：在表盘周围绘制圆圈。默认值为 `false`。仅适用于模拟时钟。
- `seconds_motion` (字符串)：`continuous` 或 `tick`，秒针的运动方式。默认值为 `continuous`。仅适用于模拟时钟。

```yaml
type: clock
clock_size: large
date_format:
  - weekday-long
  - day-numeric
  - month-long
```

## 在代码中 {#in-code}

该卡片位于 [`src/panels/lovelace/cards/hui-clock-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-clock-card.ts)，元素是 `<hui-clock-card>`。它从 [`src/panels/lovelace/cards/clock/`](https://github.com/home-assistant/frontend/tree/dev/src/panels/lovelace/cards/clock) 加载时钟本身的两个元素之一：`<hui-clock-card-digital>` 或 `<hui-clock-card-analog>`。日期部分及其格式存放在同一文件夹下的 `clock-date-format.ts`。

在分区视图中，时钟占用 6 列。小型电子时钟占 1 行，并会随其大小和标题增长。模拟时钟至少需要 2 行。

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-clock-card.ts)
