---
title: 区域选择器
description: 区域选择器让人们可以选择他们家中的一个区域，或现场创建一个新的区域。
sidebarGroup: 采摘者
sidebarGroup: 选择器

---


# 区域选择器 {#area-picker}
Live 演示 `ha-area-picker`，已连接到演示 Home Assistant。

```html
<ha-area-picker value="living_room" no-add></ha-area-picker>
<ha-area-picker no-add></ha-area-picker>
```

## 概览 {#overview}
区域选择器是一个用于选择一个 [区域](/glossary/area) 的字段：设备所在的房间、卡片显示的区域、助手所属的区域。选择该字段可以打开一个可搜索的区域列表。每个区域都会显示其图标以及所在楼层。

## 使用场景 {#when-to-use}
使用区域选择器的情况：

- 精确选择一个区域
- 将某物分配到某个区域，当所需的区域尚不存在时

不使用区域选择器的情况：

- 选择多个区域。请使用区域 [选择器](/design/components/selector)，它可以允许选择多个区域。
- 选择操作作用对象。请使用目标选择器：它不仅接受区域，还可以选择实体、设备、楼层和标签。
- 表单中的字段。请在 [表单](/design/components/form) 中使用区域选择器，表单会为你渲染选择器。

## 解剖结构 {#anatomy}
1. **字段**：显示值并打开列表的按钮
2. **标签**：位于字段内，默认显示 **区域**
3. **值**：图标和区域名称，以及其下方的楼层
4. **清除按钮**：移除值，当字段非必填时可用
5. **箭头**：显示字段可打开列表
6. **辅助说明**：位于字段下方的可选文本
7. **列表**：带有搜索字段和区域的弹出框，在末尾有添加新区域的选项

## 变体 {#variants}
### 标签 {#label}
标签默认为 **区域**。当字段需要更多上下文时，例如 **设备的区域**，可以设置自己的标签。

标签显示在字段内部。一旦人们选择了位于楼层上的区域，字段会显示楼层替代标签，因此它显示为区域名称，下面显示楼层。没有楼层的区域，如 **花园**，保留标签。

`ha-area-picker` 的实时演示，连接到演示 Home Assistant。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/area-picker)。

```html
<ha-area-picker label="Area of the device" value="bedroom" no-add></ha-area-picker>
<ha-area-picker label="Area of the device" value="garden" no-add></ha-area-picker>
```

### 添加区域 {#adding-an-area}
在列表的末尾，选择器会提供添加新区域的选项。当人们搜索不存在的区域时，该选项会将搜索内容作为名称：**添加新区域 'Attic'**。选择它会打开创建区域的对话框，并在创建后选择新区域。在本页的演示中，该对话框不会打开。

`ha-area-picker` 的实时演示，连接到演示 Home Assistant。搜索一个不存在的区域，比如 Attic，以查看建议。

```html
<ha-area-picker></ha-area-picker>
```

此选项可以被关闭。

### 过滤 {#filtering}
你可以将列表限制为包含某些实体的区域，例如仅显示有灯的区域：

`ha-area-picker` 的实时演示，连接到演示 Home Assistant。

```html
<ha-area-picker include-domains='["light"]' no-add></ha-area-picker>
```

过滤器会查看区域中的实体，以及其中设备的实体。你还可以根据这些实体的设备类别进行过滤，排除某些域的实体，或排除特定区域。

### 添加按钮 {#add-button}
选择器可以显示一个按钮，而不是一个空字段。一旦用户选择了一个区域，选择器会像普通选择器一样显示该区域。这适用于列表，其中用户逐个添加区域。

`ha-area-picker` 的实时演示，连接到演示 Home Assistant。

```html
<ha-area-picker add-button-label="Add area" no-add></ha-area-picker>
```

## 行为 {#behavior}
- **启用**：选择字段会打开列表，并将焦点移到其搜索字段。
- **悬停和按下**：字段会显示水波纹。
- **聚焦**：字段底部的线条变为 2px 厚，使用主色。
- **搜索**：输入内容会在输入时过滤列表。当没有匹配项时，列表显示 **未找到与你搜索词匹配的区域**。当主页没有区域时，显示 **没有可用区域**。
- **未知**：当值为不存在的区域时，字段变为静默警告色，并显示 **选择了未知区域**。
- **禁用**：字段透明度降低到 50%，无法打开。
- **窄屏**：当窗口宽度最多为 870px 或高度最多为 500px 时，列表将作为底部弹出表单打开，而不是弹出菜单。选择一个区域会关闭列表。一旦列表关闭，会报告新值。

`ha-area-picker` 的实时演示，连接到演示 Home Assistant。

```html
<ha-area-picker value="attic" no-add></ha-area-picker>
<ha-area-picker value="kitchen" disabled></ha-area-picker>
```

## 规格 {#specs}
区域选择器使用前端的共享选择字段和列表，`ha-picker-field` 和 `ha-generic-picker`。

### 字段 {#field}
| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 最小高度 | 56px | 无 |
| 起始内边距 | 16px | `--ha-space-4` |
| 结束内边距 | 8px | `--ha-space-2` |
| 部件间距 | 8px | `--ha-space-2` |
| 圆角 | 顶部4px，底部方形 | `--ha-border-radius-sm` |
| 背景 | 表单背景 | `--ha-color-form-background` |
| 底部线 | 1px | `--ha-color-border-neutral-loud` |
| 底部线，聚焦 | 2px | `--mdc-theme-primary` |
| 底部线，无效 | 2px | `--error-color` |
| 占位文字 | 次要文本颜色 | `--secondary-text-color` |
| 清除按钮 | 32px | `--ha-icon-button-size` |
| 箭头图标 | 20px，在32px宽区域内 | `--mdc-icon-size` |
| 未知背景 | 轻微警告填充 | `--ha-color-fill-warning-quiet-resting` |
| 未知文字 | 警告文字 | `--ha-color-on-warning-normal` |
| 禁用 | 禁用表单背景的50%不透明度 | `--ha-color-form-background-disabled` |
| 辅助文本上方间距 | 8px | `--ha-space-2` |

### 列表 {#list}
| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 宽度 | 字段的宽度，至少为250px | `--ha-generic-picker-width` |
| 最大高度 | 窗口高度的70%和500px中较小的值。当窗口高度最多为1000px时，70%和400px中较小的值 | 无 |
| 圆角 | 8px | `--ha-border-radius-md` |
| 阴影 | 中等阴影 | `--ha-box-shadow-m` |
| 底部面板圆角 | 20px | `--ha-border-radius-2xl` |
| 底部面板最大宽度 | 600px | 无 |

## 指南 {#guidelines}
- 保持添加区域的选项：当人们将某物分配到一个区域时，他们需要的区域可能尚不存在。
- 在创建区域没有意义的情况下关闭添加区域的选项，比如在筛选器中，或在从已有内容的区域中选择时。
- 当仅用 **区域** 无法说明区域用途时，设置你自己的标签。

以实时演示的形式展示做与不做。这两者都与演示 Home Assistant 有关。

**做：** 当字段需要上下文时，说明该区域的用途。

```html
<ha-area-picker label="Area of the device" no-add></ha-area-picker>
```

**不做：** 留下通用标签，使人无法判断他们选择区域的用途。

```html
<ha-area-picker no-add></ha-area-picker>
```

## 无障碍功能 {#accessibility}
### 键盘 {#keyboard}
| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移动到字段，如果有清除按钮，也会移动到清除按钮。已禁用的字段会被跳过。 |
| <kbd>Enter</kbd> 或 <kbd>Space</kbd> | 在字段获得焦点时打开列表。 |
| 输入 | 搜索列表。列表打开时，焦点位于搜索字段。 |
| <kbd>Arrow down</kbd> 和 <kbd>Arrow up</kbd> | 在区域之间移动。 |
| <kbd>Home</kbd> 和 <kbd>End</kbd> | 跳转到第一个或最后一个区域。 |
| <kbd>Page up</kbd> 和 <kbd>Page down</kbd> | 在列表中翻页。 |
| <kbd>Enter</kbd> | 选择高亮的区域。搜索时，高亮显示列表中的首个匹配项。如果列表中只有一个选项，<kbd>Enter</kbd> 会选择它。 |
| <kbd>Escape</kbd> | 关闭列表。 |

### 焦点 {#focus}
焦点显示为字段下方更粗的线，而不是焦点环。当列表以弹出框形式打开时，焦点保持在其中。在列表中，焦点保持在搜索字段，而方向键移动高亮显示。

### 目标尺寸 {#target-size}
该字段高度至少为56像素，并填充其所获得的宽度。清除按钮为32像素乘32像素。

### 屏幕阅读器 {#screen-readers}
- 该字段会被宣布为一个按钮，其名称由标签和其中的区域组成。当选取的区域在某一楼层时，名称为该区域和楼层名称。
- 列表会被宣布为一个带有选项列表的对话框，选取的区域为已选择。
- 清除按钮会被宣布为“清除”，使用用户的语言。

### 在代码中 {#in-the-code}
- 焦点被委派给字段中的原生 `<button>`。它的可访问名称是标签与字段中的文本。当选定区域在地板上时，标签会被省略。
- 列表在具有 `dialog` 和 `aria-modal="true"` 角色的元素中打开，名称为标签的名称。弹出框会捕获焦点。
- 列表的角色是 `listbox`，每个区域的角色是 `option`，选定区域为 `aria-selected`。
- 高亮行通过 `active` 属性标记。列表不设置 `aria-activedescendant`。
- 清除按钮的可访问名称为已翻译的标签 `ui.common.clear`。

## 相关内容 {#related}
- [设备选择器](/design/components/device-picker)：选择一个设备
- [实体选择器](/design/components/entity-picker)：选择一个实体
- [选择器](/design/components/selector)：区域选择器，用于一个或多个区域
- [表单](/design/components/form)：根据模式渲染选择器

## 代码中 {#in-code}
该元素是 `<ha-area-picker>`。它从应用提供的上下文中读取区域、楼层、设备、实体和状态，所以你不需要向它传递 `hass`。

```ts
html`
  <ha-area-picker
    .value=${this._areaId}
    .includeDomains=${["light"]}
    @value-changed=${this._areaChanged}
  ></ha-area-picker>
`;
```

在 HTML 中，列表属性采用 JSON：

```html
<ha-area-picker include-domains='["light"]' no-add></ha-area-picker>
```

### 属性 {#attributes}
- `label`：标签。默认值为 **区域**。
- `value`：选定区域的 ID。
- `helper`：字段下方的帮助文本。
- `placeholder`：空字段中的文本。
- `no-add`：隐藏添加新区域的选项。
- `include-domains`：仅显示具有这些域实体的区域。
- `exclude-domains`：隐藏具有这些域实体的区域。
- `include-device-classes`：仅显示具有这些设备类别实体的区域。
- `exclude-areas`：隐藏这些区域。
- `add-button-label`：显示带有此标签的按钮，而不是空字段。
- `required`：将字段标记为必填。
- `disabled`：禁用选择器。

### 属性 {#properties}
这些只能从代码中设置：

- `deviceFilter`：一个获取每个设备注册表条目的函数，并返回 `true` 以保留它。只有匹配设备的区域显示。
- `entityFilter`：一个获取每个实体状态对象的函数，并返回 `true` 以保留它。只有匹配实体的区域显示。

### 方法 {#methods}
- `open()`：打开列表。

### 事件 {#events}
- `value-changed`：当有人选择或清除一个区域时触发。新的区域 ID 在 `event.detail.value` 中，或者在清除时在 `undefined` 中。
- `change`：在 `value-changed` 之后触发。

来源: [`src/components/ha-area-picker.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-area-picker.ts)
