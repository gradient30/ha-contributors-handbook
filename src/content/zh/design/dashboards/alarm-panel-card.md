---
title: 报警面板卡
description: 报警面板卡可以布防和撤防报警，并配有输入验证码的键盘。
sidebarGroup: 控制
---

# 报警面板卡 {#alarm-panel-card}

仪表板卡片的实时演示，来自Home Assistant 演示的嵌入，连接到本网站的示例首页。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/dashboards/alarm-panel-card/)。

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
        "type": "alarm-panel",
        "entity": "alarm_control_panel.home_alarm"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用方法 {#usage}

报警面板卡的外观和功能类似于报警系统的键盘。在顶部，你会看到名称和一个显示状态的芯片，例如 **未布防**。在其下方是用于布防报警的按钮。当报警布防时，这些按钮会让位给一个危险色的 **撤防** 按钮。选择状态芯片会打开更多信息的对话框。

当报警需要密码时，卡片会显示一个输入字段。对于数字密码，会显示一个足够大可在墙面平板使用的键盘。对于包含字母的密码，只显示输入字段，用户自行输入。当报警无需密码，或已经设置了默认密码时，则不会显示输入字段和键盘。使用警报面板卡来创建一个作为警报面板的仪表板，就像前门的平板电脑一样。要快速查看状态，或者在所在房间布防，可以使用带有警报模式功能的[tile 卡](/design/dashboards/tile-card)，它小得多。

从Home Assistant演示的嵌入中实时演示仪表板卡，连接到本网站的示例家庭。

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
        "type": "tile",
        "entity": "alarm_control_panel.home_alarm",
        "features": [
          {
            "type": "alarm-modes",
            "modes": [
              "armed_home",
              "armed_away",
              "disarmed"
            ]
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 布防按钮 {#arm-buttons}

该卡片默认显示 **在家布防** 和 **离家布防**，前提是报警器支持这些功能。使用 `states`，你可以选择显示哪些按钮，以及它们的顺序。显示人们真正使用的模式。每多一个按钮，就多一个需要快速识别的内容。

来自 Home Assistant 演示的仪表板卡实时演示，连接到本网站的示例家庭。

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
        "type": "alarm-panel",
        "entity": "alarm_control_panel.home_alarm",
        "states": [
          "arm_home",
          "arm_away",
          "arm_night"
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 内容 {#content}

- 当有多个报警器时，使用能说明是哪一个报警器的名称，如 **车库报警**。否则，实体的名称即可。
- 不要显示报警器不支持的布防模式。卡片会在默认情况下过滤掉这些模式，但不会过滤你自己设置的列表。

## 配置 {#configuration}

- `entity`（字符串，必填）：要显示的警报。只有 `alarm_control_panel` 域的实体可用。
- `name`（字符串）：要显示的名称。默认为实体的名称。
- `states`（列表）：要显示的布防按钮：`arm_home`、`arm_away`、`arm_night`、`arm_vacation` 和 `arm_custom_bypass`。如果警报支持，默认为 `arm_home` 和 `arm_away`。
- `theme`（字符串）：仅对该卡片应用的主题。

```yaml
type: alarm-panel
entity: alarm_control_panel.home_alarm
states:
  - arm_home
  - arm_away
  - arm_night
```

## 在代码中 {#in-code}

卡片位于 [`src/panels/lovelace/cards/hui-alarm-panel-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-alarm-panel-card.ts)，元素是 `<hui-alarm-panel-card>`。手臂按钮是填充外观的 [`<ha-button>`](/design/components/button) 元素，键盘是由 [`<ha-control-button>`](/design/components/controls) 元素组成的网格，代码字段是一个 [`<ha-input>`](/design/components/input)。字段和键盘是否显示取决于实体的 `code_format` 属性，以及实体注册选项中的默认代码。

卡片本身没有网格选项，因此在部分视图中，它占据部分的全部宽度并根据需要占用高度。

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-alarm-panel-card.ts)
