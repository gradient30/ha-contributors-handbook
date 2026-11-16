---
title: 文本区域
description: 文本区域允许人们输入可以跨多行的文本，例如描述或消息。
sidebarGroup: 输入
---

# 文本区域 {#textarea}

Live 演示 `ha-textarea`。

```html
<ha-textarea label="Description" value="Turns on the hallway lights when someone comes home after sunset." resize="auto"></ha-textarea>
```

## 概述 {#overview}

文本区域允许用户输入可以超过一行的自由文本：自动化的描述、标签或日历事件，或者要发送给语音助手的消息。

## 何时使用 {#when-to-use}

使用文本区域用于：

- 可以跨多行的自由文本，如描述、笔记或消息

不要使用文本区域用于：

- 简短的单行值，如姓名。使用 [文本输入](/design/components/input)。
- 代码或 YAML。前端有专用的代码编辑器用于此类内容。

## 解剖结构 {#anatomy}

1. **容器**：已填充的字段，底部有一条线
2. **标签**：为文本命名。它位于字段内，当字段获得焦点或有值时会向上移动。
3. **文本**：人们输入的原生文本区域
4. **提示**：字段下方的可选帮助文本，当文本无效时由验证消息替换

## 变体 {#variants}

### 随内容增长 {#growing-with-the-content}

前端的大多数文本区域会随着内容增长：字段开始很小，用户输入时会增长，并在达到最大高度（默认 200 像素）时开始滚动。这样可以保持短文本的紧凑，同时不隐藏长文本。

`ha-textarea` 的实时演示。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/components/textarea/)。

```html
<ha-textarea label="Notes" resize="auto"></ha-textarea>
```

### 固定高度 {#fixed-height}

不随内容增长的文本区域具有固定高度，以文本行数表示（默认 4 行）。当你大致知道将要输入多少文本，并希望从一开始就有空间时，可以使用这种类型。

`ha-textarea` 的实时演示。

```html
<ha-textarea label="Message" rows="6"></ha-textarea>
```

### 带提示 {#with-a-hint}

使用提示可以帮助用户编写文本，例如是否支持格式化。

`ha-textarea` 的实时演示。

```html
<ha-textarea label="Description" hint="Supports Markdown." resize="auto"></ha-textarea>
```

## 行为- **空**：标签位于输入框内部，大小与文本相同。 {#behavior}
- **悬停**：输入框背景变为悬停背景。
- **聚焦**：底部的线条变粗并变为主色，标签也一样。
- **已填充**：一旦输入框有值或聚焦，标签会上移并变小。如果有占位符，标签始终上移。标签具有输入框背景，因此滚动的文本在其下方仍可阅读。
- **必填**：标签会显示 `*` 标记。输入框必须有文本才能让表单有效。
- **禁用**：输入框显示禁用背景并变为半透明，文本不能更改或聚焦。
- **只读**：显示用户可以阅读和复制的文本，但不能更改。

- **无效**：标签和底部的线条会变成危险颜色，验证信息会替代提示。当代码将字段标记为无效、表单检查发现文本无效，或者对于自我检查的字段在失去焦点时，该字段就会变为无效。一旦用户输入有效文本，它就会再次变为有效。

`ha-textarea` 的实时演示。

```html
<ha-textarea label="Description" required resize="auto"></ha-textarea>
<ha-textarea label="Disabled" value="Can't change this." disabled resize="auto"></ha-textarea>
<ha-textarea label="Message" invalid validation-message="Enter a message to send." resize="auto"></ha-textarea>
```

## 规格 {#specs}

### 尺寸 {#size}

| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 最小高度 | 56px | 无 |
| 最大高度（可增长时） | 200px | `--ha-textarea-max-height` |
| 固定高度行数 | 4 | 无 |
| 文本上方的空间 | 24px，无标签时为12px | `--ha-space-6`, `--ha-space-3` |
| 文本下方的空间 | 8px | `--ha-space-2` |
| 文本左右内边距 | 16px | `--ha-space-4` |
| 圆角 | 顶部4px，底部0 | `--ha-border-radius-sm`, `--ha-border-radius-square` |
| 底部线条 | 1px，聚焦时2px | 无 |

### 类型 {#type}

| 部分 | 大小 | 令牌 |
| --- | --- | --- |
| 文本 | 14px | `--ha-font-size-m` |
| 字段内标签 | 14px | `--ha-font-size-m` |
| 上移后的标签 | 10px | `--ha-font-size-xs` |
| 标签上方间距 | 16px，上移时为 8px | `--ha-space-4`, `--ha-space-2` |
| 标签左右内边距 | 12px | `--ha-space-3` |
| 提示和验证信息 | 12px | `--ha-font-size-s` |

文本使用 `--ha-font-family-body`。颜色、线条和标签位置的变化持续 150ms。

### 颜色 {#color}

| 部位 | 状态 | 令牌 |
| --- | --- | --- |
| 背景和标签背景 | 默认 | `--ha-color-form-background` |
| 背景和标签背景 | 悬停 | `--ha-color-form-background-hover` |
| 背景和标签背景 | 禁用 | `--ha-color-form-background-disabled` |
| 底部线条 | 默认 | `--ha-color-border-neutral-loud` |
| 底部线条 | 聚焦 | `--primary-color` |
| 底部线条 | 无效 | `--ha-color-border-danger-normal` |
| 标签 | 默认 | `--secondary-text-color` |
| 标签 | 聚焦 | `--primary-color` |
| 标签 | 无效 | `--ha-color-fill-danger-loud-resting` |
| 提示 | 全部 | `--ha-color-text-secondary` |
| 验证消息 | 无效 | `--ha-color-on-danger-quiet` |

## 指南 {#guidelines}

作为实时演示的做与不做。

**做：** 总是给文本区域一个简短的标签。

```html
<ha-textarea label="Description" resize="auto"></ha-textarea>
```

**不做：** 使用占位符作为标签。一旦用户开始输入，它就会消失。

```html
<ha-textarea placeholder="Description" resize="auto"></ha-textarea>
```

作为实时演示的做与不做。

**做：** 说明哪里不对，以及如何修复。

```html
<ha-textarea label="Message" invalid validation-message="Enter a message to send." resize="auto"></ha-textarea>
```

**不做：** 仅说明文字有错误。

```html
<ha-textarea label="Message" invalid validation-message="Invalid value." resize="auto"></ha-textarea>
```

- 保持标签简短：**说明**、**备注**、**消息**。

## 可访问性 {#accessibility}

### 键盘 {#keyboard}

| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移到文本区域，并从文本区域移开。禁用的文本区域会被跳过。 |
| <kbd>Enter</kbd> | 开始新的一行。 |

在文本区域中的按键不会触发其周围的键盘快捷键。

### 焦点 {#focus}

焦点以底部线条和标签的主色显示，而不是用单独的焦点环。

### 目标大小 {#target-size}

字段高度至少为 56px，宽度与其容器相同。

### 屏幕阅读器 {#screen-readers}

屏幕阅读器会使用其标签来宣布文本区域，并将提示作为其描述。当字段变为无效时，会宣布验证信息。必填、禁用和只读状态也会被宣布。没有标签时，只有占位符来描述，因此请始终给它一个标签。

### 在代码中 {#in-the-code}

- 焦点会进入组件内部的原生文本区域。
- 该组件会阻止 `keydown` 事件向外传播。

- 标签是与文本区域关联的原生 `<label>`，因此它是可访问的名称。
- 没有标签时，`<label>` 是空的并对辅助技术隐藏。此时占位符是描述文本区域的唯一文本。
- 提示和验证信息通过 `aria-describedby` 与文本区域关联，因此屏幕阅读器会将它们读取为描述。
- 验证信息位于实时区域内，并在字段无效时获得 `alert` 角色，因此屏幕阅读器在其出现时会进行朗读。
- 必填、禁用和只读属性设置在原生文本区域上，因此辅助技术可以按原样获取这些属性。

## 相关内容 {#related}

- [文本输入](/design/components/input)：一行文本
- [表单](/design/components/form)：从架构创建字段
- [选择器](/design/components/selector)：带有 `multiline` 的文本选择器显示一个多行文本框
- [界面文本](/design/ui-text)：如何编写标签、提示和错误信息

## 代码中 {#in-code}

该元素是 `<ha-textarea>`。它基于 [Web Awesome 多行文本框](https://webawesome.com/docs/components/textarea/)。

```html
<ha-textarea label="Description" resize="auto"></ha-textarea>
<ha-textarea label="Message" rows="6"></ha-textarea>
<ha-textarea label="Notes" hint="Supports Markdown." required></ha-textarea>
```

### 属性- `label`：标签。 {#attributes}
- `value`：当前值。
- `hint`：文本区域下方的帮助文本。
- `placeholder`：文本区域为空时显示的文本。
- `rows`：可见行数。默认为 `4`。
- `resize`：`none`（默认）、`vertical`、`horizontal`、`both` 或 `auto`。使用 `auto` 时，文本区域会随着内容增长，最多到 `--ha-textarea-max-height`。
- `required`：使字段为必填项，并在标签后添加标记。
- `disabled`：禁用文本区域。
- `readonly`：将文本区域设为只读。
- `invalid`：将文本区域标记为无效。
- `validation-message`：文本区域无效时显示的消息。如果没有，则显示浏览器自身的消息。
- `auto-validate`：在文本区域失去焦点时进行验证，而不是等待表单提交。
- `minlength` 和 `maxlength`：值的最小和最大长度。

- `name`、`autocomplete`、`autocapitalize`、`autofocus`、`spellcheck`、`inputmode` 和 `enterkeyhint`：传递给本地文本区域，并且与普通的 `<textarea>` 的行为相同。

`resize="auto"` 的最大高度仅在设置 `resize` 作为属性时适用。该属性不会反映，因此仅从代码中设置 `.resize` 会得到一个无限增长的文本区域。

### 插槽 {#slots}

- `label`：带标记的标签。此插槽中的内容会替换 `label` 属性的文本，包括必填标记。
- `hint`：带标记的提示，如链接。仅在未设置 `hint` 属性时使用。

### 事件 {#events}

- `input`：在值每次变化时触发，即用户输入时。
- `change`：在值提交时触发，比如文本区域失去焦点时。

从元素上的 `value` 获取新值。按键不会冒泡到文本区域外：它会阻止 `keydown` 事件，因此输入或按 Enter 插入新行时，不会触发周围的键盘处理器。

### 样式 {#styling}

- `--ha-textarea-max-height`：最大高度，与 `resize="auto"` 关联。默认值为 `200px`。
- `--ha-textarea-padding-bottom`：文本区域下方的间距。
- `--ha-textarea-required-marker`：必填字段标签后的标记。默认值为 `"*"`。

来源：[`src/components/ha-textarea.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-textarea.ts)
