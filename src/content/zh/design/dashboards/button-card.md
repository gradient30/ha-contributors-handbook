---
title: 按钮卡
description: 按钮卡是一个大而方的按钮，带有图标和名称。它执行一个动作，比如切换灯光或激活场景。
sidebarGroup: 实体卡
---

# 按钮卡 {#button-card}

仪表板卡片的实时演示，来自Home Assistant演示的嵌入，连接到本网站的示例首页。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/dashboards/button-card/)。

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
        "type": "button",
        "entity": "light.living_room_lamp"
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "button",
        "entity": "scene.movie_night"
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "button",
        "entity": "lock.front_door"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用方法 {#usage}

按钮卡片是一个大的目标：一个图标下方有名称。选择它会执行一个动作。对于可以切换的实体，如灯、开关或风扇，这是一个切换动作。对于所有其他实体，它会打开更多信息对话框。长按按钮也会打开更多信息对话框。

当一个动作最重要且人们希望无需多看即可点击时（如在墙面平板上），请使用按钮卡片。对于大多数实体，[方块卡](/design/dashboards/tile-card) 更适合：它显示状态，占用空间更小，并且可以通过功能增加更多控件。

按钮卡片不需要实体。没有实体时，它只是一个普通按钮，可执行其`tap_action`，例如导航到另一个仪表板或执行某个动作。

### 显示状态 {#show-state}

按钮显示名称和图标。在名称下添加 `show_state: true` 以显示状态，并使用 `show_name` 和 `show_icon` 隐藏其中一个。仅图标按钮需要一个图标本身就能说明的实体。

仪表板卡片的实时演示，来自Home Assistant演示的嵌入，连接到本网站的示例主页。

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
        "type": "button",
        "entity": "light.hallway",
        "show_state": true
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "button",
        "entity": "switch.desk_plug",
        "show_name": false
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "button",
        "entity": "light.kitchen_ceiling",
        "show_icon": false,
        "show_state": true
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 图标大小 {#icon-size}

默认情况下，图标会随着卡片缩放：它占卡片宽度的 40%。设置 `icon_height`，就像 `40px` 一样，可以得到固定的、更小的图标和更平静的按钮。当所有按钮使用相同高度时，按钮网格的可读性更好。

仪表板卡片的实时演示，来源于 Home Assistant 演示的嵌入，连接到本网站的示例主页。

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
        "type": "button",
        "entity": "light.living_room_lamp",
        "icon_height": "40px"
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "button",
        "entity": "light.hallway",
        "icon_height": "40px"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 内容 {#content}

- 名称保持一两个词即可。它位于图标下方，居中显示，并能快速换行。
- 使操作可预测。如果按钮执行的操作不是切换，而是运行脚本等，名称应说明发生的事情。
- 使用 [网格卡](/design/dashboards/grid-card) 对按钮进行分组，以便它们对齐。

## 配置- `entity` (字符串)：按钮对应的实体。 {#configuration}
- `name` (字符串)：显示的名称。默认为实体的名称。
- `icon` (字符串)：显示的图标。默认为实体的图标。
- `icon_height` (字符串)：图标的高度，如 `40px`。默认情况下，图标随卡片的宽度缩放。
- `color` (字符串)：实体处于激活状态时图标的颜色。默认为状态的颜色 `state`。使用 `none` 设置默认图标颜色。
- `show_name` (布尔值)：是否显示名称。默认为 `true`。
- `show_icon` (布尔值)：是否显示图标。默认为 `true`。
- `show_state` (布尔值)：是否显示状态。默认为 `false`。
- `theme` (字符串)：此卡片使用的主题。
- `tap_action` (动作)：选择按钮时执行的操作。对于可切换的实体，默认为 `toggle`；其他实体默认为 `more-info`。

- `hold_action`（操作）：按住按钮时会发生什么。默认是 `more-info`。
- `double_tap_action`（操作）：双击按钮时会发生什么。默认是 `none`。

```yaml
type: button
entity: scene.movie_night
icon_height: "40px"
tap_action:
  action: perform-action
  perform_action: scene.turn_on
  target:
    entity_id: scene.movie_night
```

旧类型名称 `entity-button` 仍然有效。它会创建相同的按钮，但需要一个 `entity`。

## 在代码中 {#in-code}

该卡片位于 [`src/panels/lovelace/cards/hui-button-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-button-card.ts)，元素是 `<hui-button-card>`。`entity-button` 类型在 `hui-entity-button-card.ts` 中是 `<hui-entity-button-card>`，这是一个小的子类，只增加了对实体的检查。

在部分视图中，一个带有图标和名称或状态的按钮占据 12 列中的 6 列和两行。一个仅有图标或仅有文本的按钮占据 3 列和一行。两者都可以缩小到 2 列。

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-button-card.ts)
