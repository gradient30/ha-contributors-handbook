---
title: 州图标
description: Home Assistant 如何根据实体的状态选择图标和颜色。
sidebarGroup: 反馈与状态
---

# 州图标 {#state-icon}

实时演示`state-badge`，已连接到演示Home Assistant。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/components/state-icon/)。

```html
<state-badge data-props='{"stateObj": {"entity_id": "light.living_room_lamp", "state": "on", "attributes": {"friendly_name": "Floor lamp", "brightness": 120, "color_mode": "hs", "hs_color": [32, 60], "rgb_color": [255, 170, 102]}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
<state-badge data-props='{"stateObj": {"entity_id": "light.kitchen_ceiling", "state": "off", "attributes": {"friendly_name": "Kitchen ceiling"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
<state-badge color="state" data-props='{"stateObj": {"entity_id": "climate.thermostat", "state": "heat", "attributes": {"friendly_name": "Thermostat", "hvac_action": "heating", "current_temperature": 20.5, "temperature": 21}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
<state-badge color="state" data-props='{"stateObj": {"entity_id": "binary_sensor.front_door", "state": "on", "attributes": {"friendly_name": "Front door", "device_class": "door"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
<state-badge color="state" data-props='{"stateObj": {"entity_id": "cover.bedroom_blinds", "state": "open", "attributes": {"friendly_name": "Bedroom blinds", "current_position": 70, "device_class": "blind"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
<state-badge color="state" data-props='{"stateObj": {"entity_id": "person.alex", "state": "home", "attributes": {"friendly_name": "Alex"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
<state-badge color="state" data-props='{"stateObj": {"entity_id": "switch.desk_plug", "state": "unavailable", "attributes": {"friendly_name": "Desk plug"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
```

## 概述 {#overview}

Home Assistant 中的每个实体都有一个图标，并且图标会随其状态而变化。当门打开时，门传感器会显示一个打开的门，门关闭时会显示一个关闭的门。点亮的灯可以显示其颜色和亮度。人们通常先通过这些图标读取家中的状态，而不是先看文字。

有两个组件负责这个工作：

- **状态图标** 会根据实体的状态选择图标。它本身没有颜色。
- **状态徽章** 将该图标放入一个直径为40像素的圆形徽章中，并添加颜色。它出现在实体行的开头、详细信息对话框的标题、选择器以及许多其他地方。

## 何时使用 {#when-to-use}

使用它们的情况：

- 每个显示带图标的实体的地方

不要使用它们的情况：

- 与实体无关的图标。使用普通图标。
- 带标签的紧凑型药丸中的值。使用 [徽章](/design/components/badge)，在其 `icon` 插槽中带状态图标。

## 解剖结构 {#anatomy}

1. **徽章**：状态徽章的 40px 容器，默认为圆形。当有实体图片时，它会显示该图片作为背景。
2. **图标**：其中的状态图标，由徽章着色。当显示图片时，它会被隐藏。

## 变体 {#variants}

### 仅图标或徽章 {#icon-only-or-badge}

状态图标就是图标，使用其周围环境的颜色。状态徽章则增加了 40px 容器、状态颜色和图片。

### 颜色 {#color}

默认情况下，只有灯会被着色。开启状态颜色时，其他实体也会获得状态颜色。使用主题颜色或任何其他颜色时，当实体处于活动状态时会应用该颜色。关闭颜色时，所有内容都不着色。参见 [颜色选择方式](/design/components/state-icon#how-the-color-is-picked)。

## 行为 {#behavior}

### 图标如何选择 {#how-the-icon-is-picked}

状态图标经过以下步骤，并使用它找到的第一个图标：

1. 组件自身设置的图标，例如来自卡片配置的图标。
2. 人们为实体在其设置中设置的图标。
3. 实体状态中的图标属性。
4. 集成为该实体和状态定义的图标，在其图标翻译中。
5. 一些域的内置图标，其图标取决于的不仅仅是状态，例如太阳、更新和设备跟踪器。
6. 该域的默认图标，对于此设备类别和状态。例如，具有`door`设备类别的二元传感器在开启和关闭时有不同的图标。
7. 当没有其他匹配时，域的备用图标，或未知域的书签图标。步骤 4 和步骤 6 中的图标来自 Home Assistant，它会按需加载这些图标。在图标加载之前，组件不会显示任何内容。

你可以请求一个实体当前不在的状态的图标。更多信息对话框中的遮盖切换按钮就是这样做的：它为打开和关闭按钮显示百叶窗在按钮将要设置的状态下的图标。

`ha-state-icon` 的实时演示，连接到演示 Home Assistant。一个遮盖实体，显示其原始状态、关闭状态，以及在组件上设置图标的状态。

```html
<ha-state-icon data-props='{"stateObj": {"entity_id": "cover.bedroom_blinds", "state": "open", "attributes": {"friendly_name": "Bedroom blinds", "current_position": 70, "device_class": "blind"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></ha-state-icon>
<ha-state-icon data-props='{"stateObj": {"entity_id": "cover.bedroom_blinds", "state": "open", "attributes": {"friendly_name": "Bedroom blinds", "current_position": 70, "device_class": "blind"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}, "stateValue": "closed"}'></ha-state-icon>
<ha-state-icon icon="mdi:sofa" data-props='{"stateObj": {"entity_id": "cover.bedroom_blinds", "state": "open", "attributes": {"friendly_name": "Bedroom blinds", "current_position": 70, "device_class": "blind"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></ha-state-icon>
```

### 如何选择颜色 {#how-the-color-is-picked}

默认情况下，状态标记只对灯具上色。每个其他实体都会获得默认图标颜色，无论其状态如何。打开状态颜色功能后，其他实体也会根据状态上色。当人们配置卡片或行时，他们可以通过 **显示状态颜色** 选项来选择此功能。

`state-badge` 的实时演示，连接到一个演示 Home Assistant。同样的实体，未使用和已使用状态颜色。

```html
<state-badge data-props='{"stateObj": {"entity_id": "binary_sensor.front_door", "state": "on", "attributes": {"friendly_name": "Front door", "device_class": "door"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
<state-badge data-props='{"stateObj": {"entity_id": "person.alex", "state": "home", "attributes": {"friendly_name": "Alex"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
<state-badge data-props='{"stateObj": {"entity_id": "climate.thermostat", "state": "heat", "attributes": {"friendly_name": "Thermostat", "hvac_action": "heating", "current_temperature": 20.5, "temperature": 21}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
<state-badge color="state" data-props='{"stateObj": {"entity_id": "binary_sensor.front_door", "state": "on", "attributes": {"friendly_name": "Front door", "device_class": "door"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
<state-badge color="state" data-props='{"stateObj": {"entity_id": "person.alex", "state": "home", "attributes": {"friendly_name": "Alex"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
<state-badge color="state" data-props='{"stateObj": {"entity_id": "climate.thermostat", "state": "heat", "attributes": {"friendly_name": "Thermostat", "hvac_action": "heating", "current_temperature": 20.5, "temperature": 21}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
```

开启状态颜色后，颜色来自主题。对于每个实体，标记会按顺序查找主题定义的最具体颜色：

1. `--state-<domain>-<device class>-<state>-color`，如 `--state-binary_sensor-door-on-color`。
2. `--state-<domain>-<state>-color`，如 `--state-person-home-color`。
3. `--state-<domain>-active-color` 或 `--state-<domain>-inactive-color`。
4. `--state-active-color` 或 `--state-inactive-color`。一个状态是否被视为活动取决于领域：on, open, home 和 playing 是活动状态。off, closed, not home 和 locked 不是活动状态。非活动实体在徽章中保持默认图标颜色。只有具有状态颜色的领域才会显示这些颜色；例如，传感器保持默认颜色。电池传感器是例外：它们的颜色会根据电池电量变化。

除此之外：

- 有颜色的灯会显示该颜色，调光灯会显示较暗的图标。
- 恒温器显示当前操作的颜色，例如加热或制冷，而不是设置的模式颜色。
- 不可用实体以不可用颜色显示，无论其领域如何。如果有自定义颜色，或没有状态颜色，则保持默认颜色。`state-badge`的实时演示，连接到演示Home Assistant。一个全亮的灯、一盏带颜色的调光灯和一盏关闭的灯。

```html
<state-badge data-props='{"stateObj": {"entity_id": "light.living_room_lamp", "state": "on", "attributes": {"friendly_name": "Floor lamp", "brightness": 255, "color_mode": "brightness"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
<state-badge data-props='{"stateObj": {"entity_id": "light.living_room_lamp", "state": "on", "attributes": {"friendly_name": "Floor lamp", "brightness": 120, "color_mode": "hs", "hs_color": [32, 60], "rgb_color": [255, 170, 102]}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
<state-badge data-props='{"stateObj": {"entity_id": "light.kitchen_ceiling", "state": "off", "attributes": {"friendly_name": "Kitchen ceiling"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
```

徽章可以使用单一颜色，而不是状态颜色，比如一个主题色如红色或主要色，或者任何CSS颜色。实体处于激活状态时使用这种颜色，不激活时使用默认颜色。颜色也可以完全关闭，对灯具同样适用。

`state-badge`的实时演示，连接到演示Home Assistant。一个带自定义颜色的开关，有开和关状态。

```html
<state-badge color="red" data-props='{"stateObj": {"entity_id": "switch.desk_plug", "state": "on", "attributes": {"friendly_name": "Desk plug"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
<state-badge color="red" data-props='{"stateObj": {"entity_id": "switch.desk_plug", "state": "off", "attributes": {"friendly_name": "Desk plug"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
```

### 图片 {#pictures}

当一个实体有图片时，比如有头像的人或有专辑封面的媒体播放器，状态徽章会显示图片而不是图标。媒体播放器和相机的角略微圆角，其他图片为圆形。更新实体则为方角。在徽章上设置的图标会优先显示于图片之上。

## 规格 {#specs}

| 属性 | 数值 | 令牌 |
| --- | --- | --- |
| 徽章尺寸 | 40px x 40px | 无 |
| 徽章圆角半径 | 50%，圆形 | `--state-badge-border-radius` |
| 带实体图片的圆角半径 | 50% | `--state-badge-with-image-border-radius` |
| 媒体播放器或相机的圆角半径 | 8% | `--state-badge-with-media-image-border-radius` |
| 更新实体的圆角半径 | 0 | `--ha-border-radius-square` |
| 图标尺寸 | 24px | `--mdc-icon-size` |
| 默认图标颜色 | 由主题设置 | `--state-icon-color` |
| 颜色和亮度变化 | 0.3秒，缓入缓出 | 无 |
| 徽章没有显示内容时的图标 | `#fce588`中的警告图标 | 无 |

## 指南 {#guidelines}

作为实时演示的可做与不可做示例。两者都与演示 Home Assistant 相关。

**可做:** 让状态徽章选择图标，从而跟随状态。

```html
<state-badge color="state" data-props='{"stateObj": {"entity_id": "binary_sensor.front_door", "state": "on", "attributes": {"friendly_name": "Front door", "device_class": "door"}, "last_changed": "2026-01-01T00:00:00Z", "last_updated": "2026-01-01T00:00:00Z", "context": {"id": "1", "parent_id": null, "user_id": null}}}'></state-badge>
```

**不可做:** 根据域或状态自行选择图标。

```html
<ha-svg-icon path="M8,3C6.89,3 6,3.89 6,5V21H18V5C18,3.89 17.11,3 16,3H8M8,5H16V19H8V5M13,11V13H15V11H13Z"></ha-svg-icon>
```

- 每次展示实体时都使用这些组件。当你自己选择图标时，会跳过人或集成设置的图标，图标不会随状态变化。
- 在人们配置卡片或行时，让他们通过 **显示状态颜色** 选项选择状态颜色。

## 可访问性 {#accessibility}

### 焦点 {#focus}

状态徽章本身不可聚焦。当周围页面使其可聚焦时，它会以分割线颜色显示 2 像素边框，或者当显示图标时显示分割线颜色背景。

### 屏幕阅读器 {#screen-readers}

图标不会增加屏幕阅读器读取的内容，因此状态必须以文本形式出现在附近，例如在实体行中的状态。状态图标可以在悬停时显示格式化状态作为本地工具提示。

### 在代码中 {#in-the-code}

- 图标内的 SVG 对屏幕阅读器是隐藏的。
- 使用 `state-title` 时，`ha-state-icon` 会得到作为其 `title` 的格式化状态。
- `state-badge` 没有角色。

## 相关 {#related}

- [徽章](/design/components/badge)：仪表板徽章，显示状态图标
- [实体选择器](/design/components/entity-picker)：显示其实体的状态图标
- [颜色](/design/foundations/color)：状态颜色背后的主题颜色

## 在代码中 {#in-code}

### 状态徽章 {#state-badge}

该元素是 `<state-badge>`。

```ts
html`<state-badge .stateObj=${stateObj} color="state"></state-badge>`
```

属性：

- `color`：`state` 表示按状态着色，`none` 表示不着色，或使用主题颜色或 CSS 颜色在实体处于活动状态时使用。如果没有，它只会为灯光着色。

这些只能作为属性设置：

- `stateObj`：实体的状态对象。
- `overrideIcon`：一个图标名称，比如 `mdi:sofa`，用于代替实体的图标。
- `overrideImage`：一个图片 URL，用于代替图标或实体图片。
- `stateColor`：设置颜色的旧方法，比如 `true` 或 `false`。`color` 优先于它。

如果没有 `stateObj`、`overrideIcon` 或 `overrideImage`，徽章将显示一个黄色警告图标。

样式：- `--state-icon-color`：默认图标颜色。由主题设置。
- `--state-badge-border-radius`：默认为 `50%`。
- `--state-badge-with-image-border-radius`：用于实体图片。默认为 `50%`。
- `--state-badge-with-media-image-border-radius`：用于媒体播放器或摄像头图片。默认为 `8%`。

徽章大小为 40x40 像素。设置 `width` 和 `height` 可更改此大小。

来源：[`src/components/entity/state-badge.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/entity/state-badge.ts)

### ha-state-icon {#ha-state-icon}

该元素是 `<ha-state-icon>`。它会继承周围的颜色，就像任何图标一样。

```ts
html`<ha-state-icon .stateObj=${stateObj}></ha-state-icon>`
html`<ha-state-icon .stateObj=${stateObj} .stateValue=${"closed"}></ha-state-icon>`
```

属性：

- `icon`：一个图标名称，比如 `mdi:sofa`，用于替代实体的图标。
- `state-title`：将图标的标题设置为格式化状态，因此显示为本地工具提示。

这些只能作为属性设置：

- `stateObj`：实体的状态对象。
- `stateValue`：要显示图标的状态，而不是实体的当前状态。

样式：

- `--mdc-icon-size`：图标大小。默认为 `24px`。

来源：[`src/components/ha-state-icon.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-state-icon.ts)
