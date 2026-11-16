---
title: 设备选择器
description: 设备选择器让人们可以从家中的所有设备中选择一个设备，并支持搜索。
sidebarGroup: 采摘者
sidebarGroup: 选择器

---


# 设备选择器 {#device-picker}
实时演示 `ha-device-picker`，已连接到演示 Home Assistant。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/device-picker)。

```html
<ha-device-picker label="Device" value="thermostat"></ha-device-picker>
<ha-device-picker label="Device"></ha-device-picker>
```

## 概述 {#overview}
设备选择器是用于选择一个 [设备](/glossary/device) 的字段：一个实体设备，或者 Home Assistant 显示为设备的服务。可以将其视为设备触发器或操作所作用的设备，或者卡片涉及的设备。选择该字段可打开可搜索列表。每行显示设备名称、所属区域，以及其集成的图标和名称。

## 使用时机 {#when-to-use}
使用设备选择器的情况：

- 精确选择一个设备
- 字段中设备本身很重要，而不仅仅是它的某个值或控件

不要使用设备选择器的情况：

- 单个值或控件，例如温度或灯光。请选择具有[实体选择器](/design/components/entity-picker)的实体。大多数自动化和卡片都是针对实体，而不是设备。
- 选择多个设备。请使用设备[选择器](/design/components/selector)，它可以允许选择多个设备。
- 选择操作作用对象。请使用目标选择器：它可以接受设备，也可以接受实体、区域、楼层和标签。
- 表单中的字段。请在[表单](/design/components/form)中使用设备选择器，表单会为你渲染选择器。

## 解剖结构 {#anatomy}
1. **字段**：显示数值并打开列表的按钮
2. **标签**：位于字段内，在选择设备后显示在数值上方
3. **数值或占位符**：设备名称，或在为空时显示 **选择设备**
4. **清除按钮**：移除数值，当字段非必填时可用
5. **箭头**：显示该字段可以打开列表
6. **辅助文本**：字段下方的可选文本
7. **列表**：带有搜索字段和设备的弹出框。每一行显示集成标志、设备名称、所属区域，以及最后的集成名称。

## 变体 {#variants}
### 已过滤 {#filtered}
只提供适合该领域的设备。你可以根据设备所具有的实体进行过滤，比如只显示带有灯的设备：

`ha-device-picker` 的实时演示，连接到演示 Home Assistant。

```html
<ha-device-picker label="Device" include-domains='["light"]'></ha-device-picker>
```

你也可以根据这些实体的设备类别进行过滤，排除某些领域的实体，或者排除某些设备。对于其他任何情况，比如根据制造商或集成进行过滤，可以通过编写代码来实现过滤。

### 使用助手 {#with-a-helper}
标签说明了设备的用途。当需要对选择进行解释时，在字段下方添加助手。

`ha-device-picker` 的实时演示，连接到演示 Home Assistant。

```html
<ha-device-picker label="Speaker" include-domains='["media_player"]' helper="Announcements play on this device."></ha-device-picker>
```

### 子设备 {#child-devices}
有些设备是其他设备的一部分，比如多通道继电器的通道。列表中显示这些子设备时，会缩进在其父设备下方，并用一条线连接，以便一目了然地看到关系。在搜索时顺序保持不变。这些演示中的家庭没有子设备。

## 行为- **启用**：选择该字段会打开列表，并将焦点移到其搜索框。 {#behavior}
- **悬停和按下**：该字段会显示波纹效果。
- **聚焦**：字段底部的线条变为 2px 厚，显示主色。
- **搜索**：输入内容会在输入时筛选列表。当没有匹配项时，列表会显示 **未找到与你的搜索词匹配的设备**。当没有设备时，它会显示 **无可用设备**。
- **未知**：当值是不存在的设备（如已被移除）时，字段会变为静默警告色，并显示 **选择了未知设备**。

- **已替换**：有时一个集成会用几个新设备替换一个旧设备。当值指向这样一个已替换的设备时，该字段显示 **已替换设备**，并在下方显示警告 [alert](/design/components/alert)。如果是一个替换，其 **更新** 按钮会切换到该设备。如果是多个替换，**选择** 会打开一个对话框让你挑选一个。这取决于 Home Assistant 的信息，而本页面的演示并没有这些信息。
- **已禁用**：该字段透明度为50%，且不能打开。
- **窄屏**：当窗口宽度最多为870px或高度最多为500px时，列表会以底部弹出层而不是气泡弹出。

选择一个设备会关闭列表。列表关闭后，新值会被报告。

`ha-device-picker` 的实时演示，连接到演示 Home Assistant。

```html
<ha-device-picker label="Device" value="attic_lamp"></ha-device-picker>
<ha-device-picker label="Device" value="desk_plug" disabled></ha-device-picker>
```

## 规格 {#specs}
设备选择器使用前端的共享选择器字段和列表，`ha-picker-field` 和 `ha-generic-picker`。

### 字段 {#field}
| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 最小高度 | 56像素 | 无 |
| 起始内边距 | 16像素 | `--ha-space-4` |
| 结束内边距 | 8像素 | `--ha-space-2` |
| 部件间间距 | 8像素 | `--ha-space-2` |
| 圆角 | 顶部4像素，底部方形 | `--ha-border-radius-sm` |
| 背景 | 表单背景 | `--ha-color-form-background` |
| 底线 | 1像素 | `--ha-color-border-neutral-loud` |
| 焦点底线 | 2像素 | `--mdc-theme-primary` |
| 无效底线 | 2像素 | `--error-color` |
| 占位符文本 | 次要文本颜色 | `--secondary-text-color` |
| 清除按钮 | 32像素 | `--ha-icon-button-size` |
| 箭头图标 | 20像素，在32像素宽区域内 | `--mdc-icon-size` |
| 未知背景 | 静默警告填充 | `--ha-color-fill-warning-quiet-resting` |
| 未知文本 | 警告文本 | `--ha-color-on-warning-normal` |
| 禁用 | 禁用表单背景50%不透明度 | `--ha-color-form-background-disabled` |
| 辅助文本上方间距 | 8像素 | `--ha-space-2` |

### 列表 {#list}
| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 宽度 | 字段的宽度，至少为250px | `--ha-generic-picker-width` |
| 最大高度 | 窗口高度的70%与500px中较小的值。当窗口高度最多为1000px时，取70%和400px中较小的值 | 无 |
| 圆角 | 8px | `--ha-border-radius-md` |
| 阴影 | 中等阴影 | `--ha-box-shadow-m` |
| 子设备缩进 | 48px | `--ha-space-12` |
| 底部弹出层圆角 | 20px | `--ha-border-radius-2xl` |
| 底部弹出层最大宽度 | 600px | 无 |

## 指南 {#guidelines}
- 只提供适合该领域的设备。扬声器领域不应列出恒温器。
- 当人们关心单一数值或控制时，更倾向于选择一个实体而非设备。

以现场演示的方式展示操作与禁忌。两者都连接到演示 Home Assistant。

**可行操作：** 将列表过滤为适合的设备，并说明设备用途。

```html
<ha-device-picker label="Speaker" include-domains='["media_player"]'></ha-device-picker>
```

**不可操作：** 在通用标签下提供家中所有设备。

```html
<ha-device-picker label="Device"></ha-device-picker>
```

## 无障碍功能 {#accessibility}
### 键盘 {#keyboard}
| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移动到字段，如果有清除按钮，也会移动到清除按钮。已禁用的字段会被跳过。 |
| <kbd>Enter</kbd> 或 <kbd>Space</kbd> | 在字段获得焦点时打开列表。 |
| 输入 | 搜索列表。列表打开时，焦点位于搜索字段。 |
| <kbd>Arrow down</kbd> 和 <kbd>Arrow up</kbd> | 在设备之间移动。 |
| <kbd>Home</kbd> 和 <kbd>End</kbd> | 跳转到第一个或最后一个设备。 |
| <kbd>Page up</kbd> 和 <kbd>Page down</kbd> | 在列表中翻页移动。 |
| <kbd>Enter</kbd> | 选择高亮显示的设备。在搜索时，列表顶部匹配项会被高亮显示。如果列表中只有一个选项，<kbd>Enter</kbd> 会选择它。 |
| <kbd>Escape</kbd> | 关闭列表。 |

### 焦点 {#focus}
焦点显示为字段下方更粗的线，而不是焦点环。当列表以弹出框形式打开时，焦点保持在其中。在列表中，焦点保持在搜索字段，而方向键移动高亮显示。

### 目标尺寸 {#target-size}
该字段高度至少为56像素，并填充其获得的宽度。清除按钮的尺寸为32像素乘32像素。

### 屏幕阅读器 {#screen-readers}
- 该字段会被宣布为一个按钮，由其标签和其中的设备命名。
- 列表会被宣布为带有选项列表的对话框，以及被选中的设备为已选择。
- 清除按钮会被宣布为“清除”，使用用户的语言。

### 在代码中 {#in-the-code}
- 焦点被委托给字段中的本地 `<button>`。弹出框会捕获焦点。列表中高亮显示的行带有 `active` 属性。列表没有设置 `aria-activedescendant`。
- 该字段是本地 `<button>`。它的可访问名称是标签加上字段中的文本。
- 列表在具有 `dialog` 和 `aria-modal="true"` 角色的元素中打开，名称来自标签。
- 列表的角色是 `listbox`，每个设备的角色是 `option`，被选中的设备有 `aria-selected`。
- 每行中的集成徽标有一个空的 `alt`，因此屏幕阅读器会跳过它。集成名称以文本形式在行中显示。
- 清除按钮的可访问名称是“Clear”，已翻译为用户的语言。

## 相关 {#related}
- [实体选择器](/design/components/entity-picker)：选择一个实体
- [区域选择器](/design/components/area-picker)：选择一个区域
- [选择器](/design/components/selector)：设备选择器，可用于一个或多个设备
- [表单](/design/components/form)：根据架构渲染选择器

## 在代码中 {#in-code}
该元素是 `<ha-device-picker>`。与实体和区域选择器不同，它需要 `hass`。

```ts
html`
  <ha-device-picker
    .hass=${this.hass}
    .label=${"Device"}
    .value=${this._deviceId}
    .includeDomains=${["light"]}
    @value-changed=${this._deviceChanged}
  ></ha-device-picker>
`;
```

在 HTML 中，列表属性使用 JSON：

```html
<ha-device-picker label="Device" include-domains='["light"]'></ha-device-picker>
```

### 属性 {#attributes}
- `label`：字段的标签。
- `value`：所选设备的ID。
- `helper`：字段下方的帮助文本。
- `placeholder`：空字段中的文本。默认值为**选择一个设备**。
- `search-label`：列表中搜索字段的占位符。
- `include-domains`：仅显示具有这些域的实体的设备。
- `exclude-domains`：隐藏具有这些域的实体的设备。
- `include-device-classes`：仅显示具有这些设备类别的实体的设备。
- `exclude-devices`：隐藏这些设备。
- `hide-clear-icon`：隐藏清除值的按钮。
- `required`：将字段标记为必填。
- `disabled`：禁用选择器。
- `autofocus`：渲染时聚焦选择器。

### 属性 {#properties}
这些只能通过代码设置：

- `hass`：Home Assistant 对象。必填。
- `deviceFilter`：一个函数，用于获取每个设备注册表条目，并返回 `true` 来显示它。
- `entityFilter`：一个函数，用于获取每个实体的状态对象，并返回 `true` 来保持它。只有匹配实体的设备会显示。
- `replacementDeviceIds`：当值是被替换设备时，将它可以替换的设备限制为这些 ID。

### 方法 {#methods}
- `open()`：打开列表。

### 事件 {#events}
- `value-changed`：当有人选择或清除设备时触发。新的设备 ID 位于 `event.detail.value`。

来源: [`src/components/device/ha-device-picker.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/device/ha-device-picker.ts)
