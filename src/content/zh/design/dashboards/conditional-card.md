---
title: 条件卡
description: 条件卡片只有在满足其条件时才显示另一张卡片，比如灯亮了，或者屏幕足够宽。
sidebarGroup: 分组与布局
---

# 条件卡 {#conditional-card}

仪表板卡片的实时演示，来自Home Assistant演示的嵌入，连接到本网站的示例主页。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/dashboards/conditional-card/)。

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
  <ha-embed-card style="grid-column: span 6">
    <script type="application/json">
      {
        "type": "conditional",
        "conditions": [
          {
            "condition": "screen",
            "media_query": "(min-width: 768px)"
          }
        ],
        "card": {
          "type": "tile",
          "entity": "media_player.living_room_speaker",
          "features": [
            {
              "type": "media-player-playback"
            }
          ]
        },
        "grid_options": {
          "columns": 6
        }
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 6">
    <script type="application/json">
      {
        "type": "conditional",
        "conditions": [
          {
            "condition": "screen",
            "media_query": "(max-width: 767px)"
          }
        ],
        "card": {
          "type": "tile",
          "entity": "media_player.living_room_speaker"
        },
        "grid_options": {
          "columns": 6
        }
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用方法 {#usage}

条件卡片包裹另一个卡片，只有在满足所有条件时才显示该卡片。当条件不满足时，卡片完全不占空间。使用它可以保持仪表板整洁：在洗衣机运行时显示该卡片，或仅在门打开时显示警告。

上面的演示包含两个带屏幕条件的条件卡片。在宽屏上，你会看到带播放控件的瓦片，在窄屏上看到普通瓦片。缩小浏览器窗口以查看它们如何交换。

### 每张卡片的可见性 {#visibility-on-every-card}

每张卡片的编辑器中都有一个 **可见性** 标签，条件相同。它们作为 `visibility` 存储在卡片本身的配置中。这是新仪表板的更好选择：卡片保持为一个卡片，无需进行包装。条件卡片仍然存在，使用它的仪表板继续正常工作。

```yaml
type: tile
entity: binary_sensor.kitchen_window
visibility:
  - condition: state
    entity: binary_sensor.kitchen_window
    state: "on"
```

### 条件 {#conditions}

- `state`：实体的状态是或不是给定的某个状态。
- `numeric_state`：实体的状态高于或低于某个数字。
- `screen`：屏幕符合某个媒体查询，例如最小宽度。
- `user`：查看仪表板的人是给定用户之一。
- `time`：当前时间在一个范围内，并且在指定的工作日。
- `location`：查看仪表板的人位于给定区域之一。
- `view_columns`：分区视图中的列数在一个范围内。
- `and`、`or` 和 `not`：组合其他条件。关于屏幕、用户、时间和位置的条件在浏览器中检查。关于实体状态的条件由Home Assistant检查，Home Assistant会在结果变化时通知前端。该网站上的演示没有后台的Home Assistant来执行此操作，因此它们只显示在浏览器中运行的条件。

```yaml
type: conditional
conditions:
  - condition: state
    entity: binary_sensor.front_door
    state: "on"
  - condition: numeric_state
    entity: sensor.outdoor_temperature
    below: 5
card:
  type: tile
  entity: binary_sensor.front_door
```

### 编辑模式 {#edit-mode}

在编辑仪表板时，无论条件如何，该卡片始终显示。否则，你无法选择当前被隐藏的卡片。要测试条件，请退出编辑模式。

### 内容 {#content}

- 不要隐藏用户寻找的内容。进进出出的卡片适合临时状态，比如开着的门，但对于用户期望固定位置的内容，会造成困惑。
- 当隐藏的卡片留下的空隙看起来很奇怪时，不要通过添加更多条件来解决，而应重新考虑布局。

## 配置 {#configuration}

- `conditions`（列表，必填）：要检查的条件。所有条件都必须满足。
- `card`（映射，必填）：要显示的卡片。

```yaml
type: conditional
conditions:
  - condition: screen
    media_query: "(min-width: 768px)"
card:
  type: tile
  entity: media_player.living_room_speaker
  features:
    - type: media-player-playback
```

## 在代码中 {#in-code}

该卡片位于 [`src/panels/lovelace/cards/hui-conditional-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-conditional-card.ts)，元素是 `<hui-conditional-card>`。它在 [`src/panels/lovelace/components/hui-conditional-base.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/components/hui-conditional-base.ts) 中扩展了 `HuiConditionalBase`，[entities card](/design/dashboards/entities-card) 的条件行也使用了它。

条件由 [`src/mixins/conditional-listener-mixin.ts`](https://github.com/home-assistant/frontend/blob/dev/src/mixins/conditional-listener-mixin.ts) 中的 `ConditionalListenerMixin` 进行评估，`<hui-card>` 对 `visibility` 选项也使用同样的 mixin。关于状态的条件通过 `subscribe_condition` 订阅发送到 Home Assistant。其他条件在本地进行检查。条件的类型在 [`src/panels/lovelace/common/validate-condition.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/common/validate-condition.ts) 中。

当卡片显示或隐藏时，会触发一个 `card-visibility-changed` 事件，这样其周围的章节或堆栈就可以更新布局。

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-conditional-card.ts)
