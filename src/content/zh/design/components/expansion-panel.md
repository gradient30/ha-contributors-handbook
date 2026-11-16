---
title: 扩展面板
description: 展开面板将一个部分隐藏在标题后面，这样人们可以在需要时打开它。
sidebarGroup: 布局和内容
sidebarGroup: 布局与内容

---


# 扩展面板 {#expansion-panel}
Live demo of `ha-expansion-panel`.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/expansion-panel)。

```html
<ha-expansion-panel outlined header="Advanced settings" secondary="Only change these if you know what they do">
  <p>Polling interval, timeouts, and other options most people never need to touch.</p>
</ha-expansion-panel>
```

## 概述 {#overview}
展开面板将一个部分隐藏在标题后面，人们可以在需要时打开它。它保持屏幕简洁：大多数人需要的内容显示在屏幕上，其余的内容等待在面板中。

## 使用时机 {#when-to-use}
使用展开面板的情况：

- 表单中的高级选项
- 对话框中的可选字段
- 一组筛选器

不使用展开面板的情况：

- 完成任务所需的内容。如果每次都必须打开面板，那么内容不应放在面板中。
- 一组行会打开其他内容的情况。请使用 [列表](/design/components/list)。

## 解剖结构 {#anatomy}
1. **容器**：带有 `outlined`，整个面板带边框和圆角
2. **标题行**：用户选择以打开或关闭面板的行
3. **前导图标**：可选，标题开头的图标
4. **标题**：标题行的文本
5. **辅助文本**：可选，位于标题下方的一行短文本
6. **折叠箭头**：关闭时指向下方，打开时向上。在标题末尾，或者与 `left-chevron` 一起在开头。
7. **标题图标**：可选，标题末尾的操作图标
8. **内容**：可打开和关闭的部分

## 变体 {#variants}
### 标题 {#header}
标题说明内容。保持简短：**高级设置**、**区域**、**网络**。下面的次要行可以给出简短的总结，比如当前值或某人打开它的原因。

`ha-expansion-panel` 的实时演示。

```html
<ha-expansion-panel outlined header="Network">
  <p>IP address, DNS, and proxy settings.</p>
</ha-expansion-panel>
<ha-expansion-panel outlined header="Network" secondary="Using DHCP">
  <p>IP address, DNS, and proxy settings.</p>
</ha-expansion-panel>
```

### 描边 {#outlined}
描边面板有边框和圆角。当面板位于表单或对话框中，与其他字段并排时，前端会使用它，使其看起来像一个整体块。 [表单](/design/components/form) 的可展开部分和卡片编辑器就是这样做的。没有边框时，面板会融入周围环境，这在面板列表（如筛选面板和卡片选择器）中是适用的。

`ha-expansion-panel` 的实时演示。

```html
<ha-expansion-panel header="Without outline">
  <p>The content of the panel.</p>
</ha-expansion-panel>
<ha-expansion-panel outlined header="With outline">
  <p>The content of the panel.</p>
</ha-expansion-panel>
```

### 左侧的箭头 {#chevron-on-the-left}
默认情况下，箭头位于标题的末尾。它可以移动到开头。配置页面上的过滤器面板使用了这个，在标题中显示活动过滤器的数量以及一个清除按钮。

`ha-expansion-panel` 的实时演示。

```html
<ha-expansion-panel left-chevron header="Areas">
  <p>Filter by area.</p>
</ha-expansion-panel>
```

### 默认打开 {#open-by-default}
面板可以从一开始就打开。

`ha-expansion-panel` 的实时演示。

```html
<ha-expansion-panel outlined expanded header="Data to back up">
  <p>Settings and history, media, and the share folder.</p>
</ha-expansion-panel>
```

### 总是打开 {#always-open}
没有折叠箭头，用户无法再打开或关闭面板。从一开始就打开，它是一个看起来像面板但始终保持打开的部分。

## 行为 {#behavior}
- **关闭**：只显示标题。内容完全不渲染。
- **打开和关闭**：选择标题可以打开或关闭面板。内容在 300 毫秒内滑动打开或关闭，折叠箭头在 150 毫秒内旋转。
- **焦点**：当标题获得焦点时，它会显示输入填充背景。在键盘焦点下，折叠箭头也会获得圆形中性填充。
- **总是打开**：标题无法被选择或聚焦。

## 规格| 属性 | 值 | 令牌 | {#specs}
| --- | --- | --- |
| 标题最小高度 | 48像素 | 无 |
| 标题内边距 | 上下0，左右8像素 | `--expansion-panel-summary-padding` |
| 内容内边距 | 上下0，左右8像素 | `--expansion-panel-content-padding` |
| 标题字体粗细 | 500 | `--ha-font-weight-medium` |
| 标题颜色 | 主要文本颜色 | `--primary-text-color` |
| 次级文本大小 | 12像素 | `--ha-font-size-s` |
| 次级文本颜色 | 次级文本颜色 | `--secondary-text-color` |
| 切换箭头或前置图标与标题间距 | 8像素 | 无 |
| 箭头大小 | 24像素 | 无 |
| 边框，轮廓型 | 1像素实线 | `--outline-color` |
| 圆角半径，轮廓型 | 12像素 | `--ha-border-radius-lg`，到 `--ha-card-border-radius` |
| 焦点时标题背景 | 输入填充 | `--input-fill-color` |
| 键盘焦点时箭头背景 | 圆形中性填充 | `--ha-color-fill-neutral-normal-active` |
| 打开和关闭动画 | 300毫秒，`cubic-bezier(0.4, 0, 0.2, 1)` | 无 |
| 人字形旋转 | 150毫秒内旋转180度，`cubic-bezier(0.4, 0, 0.2, 1)` | 无 |

## 指南 {#guidelines}
- 遵循前端的做法：在表单或对话框中，面板有轮廓，位于其他字段旁边；在面板列表中（如筛选面板）则没有轮廓。

## 可访问性 {#accessibility}
### 键盘 {#keyboard}
| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移动到标题。始终打开的面板会被跳过。 |
| <kbd>Enter</kbd> 或 <kbd>Space</kbd> | 打开或关闭面板。 |

### 焦点 {#focus}
当标题获得焦点时，其背景会显示输入填充颜色。使用键盘焦点时，箭头也会显示圆形中性色填充。

### 目标尺寸 {#target-size}
标题的高度至少为48px，宽度与面板相同。

### 屏幕阅读器 {#screen-readers}
标题会被宣布为可展开或折叠的按钮。打开的内容会被宣布为区域，名称与标题相同。

### 在代码中 {#in-the-code}
- 头部的角色是 `button`，且 `aria-expanded` 设置为 `true` 或 `false`。
- 内容的角色是 `region`，并通过 `aria-labelledby` 由头部命名。
- 当面板关闭时，内容具有 `aria-hidden="true"`，且不会被渲染。
- 斜角标是装饰性的，对于屏幕阅读器不可见。

## 相关内容 {#related}
- [列表](/design/components/list)：可展开其他内容的行
- [表单](/design/components/form)：`expandable` 模式类型显示一个展开面板
- [对话框](/design/components/dialog)：面板中包含可选字段

## 代码中 {#in-code}
该元素是 `<ha-expansion-panel>`。内容放在默认插槽中。

```html
<ha-expansion-panel outlined header="Advanced settings" secondary="Optional">
  <p>...</p>
</ha-expansion-panel>
```

内容仅在面板打开时渲染。如果其中的某些内容需要在面板打开之前就存在，请牢记这一点。

### 属性 {#attributes}
- `header`：标题文本。
- `secondary`：标题下方的一行简短文本。
- `expanded`：打开面板。当人们打开或关闭面板时，会反映并更新状态。
- `outlined`：添加边框和圆角。
- `left-chevron`：将箭头放在标题的开头。
- `no-collapse`：移除箭头，面板不能再被人打开或关闭。将其与 `expanded` 结合使用，可创建看起来像面板但始终保持打开的部分。

### 插槽 {#slots}
- 默认：内容。
- `header`：用你自己的内容替换标题文本和副文本。
- `secondary`：替换副文本。
- `leading-icon`：标题开头的图标。
- `icons`：标题末尾的操作，如图标按钮。
- `event`：标题和箭头之间的内容。

### 事件 {#events}
- `expanded-will-change`：面板打开或关闭之前触发。`detail` 拥有新的 `expanded` 值。
- `expanded-changed`：面板打开或关闭之后触发。`detail` 拥有新的 `expanded` 值。

### 样式 {#styling}
- `--expansion-panel-summary-padding`：标题的内边距。默认值为 `0 8px`。
- `--expansion-panel-content-padding`：内容的内边距。默认值为 `0 8px`。
- `--ha-card-border-radius`：带边框面板的圆角。默认值为 `var(--ha-border-radius-lg)`。

`summary` 部分用于标题，不包括自定义属性无法覆盖的内容。

来源: [`src/components/ha-expansion-panel.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-expansion-panel.ts)
