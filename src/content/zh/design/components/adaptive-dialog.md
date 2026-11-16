---
title: 自适应对话
description: 大屏幕上的对话框，以及手机上的底部弹出菜单。它会自动选择正确的一个。
sidebarGroup: 反馈与状态
---


# 自适应对话 {#adaptive-dialog}
## 概述 {#overview}
自适应对话框是一种[对话框](/design/components/dialog)，它能够适应所处的屏幕。在大屏幕上，它是在窗口中间的常规对话框。在手机或小屏幕上，它会从底部滑出，作为底部面板，很容易用拇指操作，也容易向上滑动关闭。

其他功能与普通对话框相同：相同的标题、主体和页脚，以及标题和按钮的相同指南。此页面介绍不同之处。

它需要正在运行的Home Assistant才能打开，所以这里没有实时演示。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/adaptive-dialog)。

## 何时使用 {#when-to-use}
在以下情况下使用自适应对话框：

- 需要在手机上良好工作的表单和其他输入
- 受益于小屏幕全宽内容的显示
- 在桌面和移动端应表现一致的对话框

当不需要底部弹出层时，使用常规的[对话框](/design/components/dialog)，例如仅在大屏幕上使用的对话框。前端的确认对话框是常规对话框。

## 解剖结构 {#anatomy}
在对话模式下，其解剖结构与 [dialog](/design/components/dialog#anatomy) 相同。在底部弹出表模式下：

1. **遮罩层**：位于弹出表背后的覆盖层
2. **手柄**：顶部的小条，提示你可以拖动弹出表
3. **表面**：弹出表本身，顶部有圆角
4. **标题栏**：关闭按钮、标题、可选副标题和可选操作按钮
5. **主体**：内容，当内容不适合时可以滚动
6. **底部栏**：位于底部的按钮

## 变体 {#variants}
### 对话框和底部弹出表 {#dialog-and-bottom-sheet}
屏幕尺寸决定模式：

- **对话框**：在屏幕宽度超过 870px 且高度超过 500px 时。
- **底部弹出表**：在屏幕宽度 870px 或以下，或高度 500px 或以下时。

### 宽度 {#width}
在对话模式中，自适应对话框具有与对话框相同的四种宽度：小（320像素）、中（580像素，默认）、大（1024像素）和全宽。底部弹出表单始终使用屏幕的全宽，并忽略宽度设置。

### 自适应弹出框 {#adaptive-popover}
自适应弹出框是一个近亲。在大屏幕上，它会作为弹出框在触发它的元素旁边打开，而不是在窗口中央。在小屏幕上，或者当没有元素可作为锚点时，它的表现像自适应对话框。日期选择器使用它。

## 行为- **选择模式**：模式在对话框创建时选择一次，然后在打开时保持不变。调整窗口大小不会切换模式。这可以防止半填充的表单被重置。对话框可以选择在打开时实时切换。 {#behavior}
- **打开**：底部弹出层在300毫秒内滑上。启用简化动画时，它会立即出现。焦点会移动到被标记为获取焦点的元素。
- **关闭**：关闭按钮、标记为关闭按钮的按钮、<kbd>Escape</kbd> 以及选择遮罩层都可以关闭对话框，在两种模式下均适用。

- **滑动**：你可以向下拖动底部弹出面板。快速向下滑动可以关闭它。缓慢拖动时，当释放超过其高度的一半时会关闭，否则会弹回。开始拖动的内容如果已经向下滚动，或者在会自行拖动的控件上，如滑块、开关、色轮或地图，则会移动该内容，而不是面板。
- **受保护的关闭**：当关闭被阻止时，例如表单有更改时，<kbd>Escape</kbd> 和选择遮罩无效。此时底部弹出面板会隐藏其把手，并且无法通过滑动关闭。
- **高度**：底部弹出面板的高度与其内容相同，最高可达屏幕的 90%，并且顶部始终至少保留 48px 的空白。

## 规格 {#specs}
在对话模式下，规格与[对话](/design/components/dialog#specs)相同。在底部弹出模式下：

| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 宽度 | 屏幕的全宽，位于安全区域内 | 无 |
| 最大高度 | 屏幕的90%，顶部至少保留48px | `--ha-bottom-sheet-max-height` |
| 圆角 | 顶部20px | `--ha-border-radius-2xl`，至`--ha-bottom-sheet-border-radius` |
| 背景 | 卡片背景 | `--card-background-color`，至`--ha-dialog-surface-background` |
| 内容区内边距 | 顶部为0，其他边为24px | `--ha-space-6`，至`--dialog-content-padding` |
| 打开和关闭动画 | 300ms，减少动画时为1ms | 无 |

## 指南 {#guidelines}
请遵循 [dialog](/design/components/dialog#guidelines) 的指南：清晰的标题、简短的正文，以及在 **取消** 旁边的一个主要操作。

- 将按钮放在页脚，主要操作为强调按钮，**取消** 为普通按钮。
- 头部操作，例如帮助或设置，使用图标按钮或菜单。
- 保持内容足够简短，以适用于手机。如果在小屏幕上需要大量滚动，可能需要一个单独的页面。

## 可访问性 {#accessibility}
### 键盘 {#keyboard}
与[对话框](/design/components/dialog#keyboard)相同：<kbd>Tab</kbd> 可在内容中切换，<kbd>Escape</kbd> 可关闭它，除非关闭操作受到保护。

### 焦点 {#focus}
打开时，焦点会移动到被标记为获取焦点的元素。像表单这样的组件，如果会代理焦点，会将焦点传递给它们的第一个字段。

### 目标尺寸 {#target-size}
关闭按钮是一个 48px x 48px 的图标按钮。滑动从不作为关闭底部表单的唯一方式：关闭按钮始终存在，除非对话框故意隐藏它。

### 屏幕阅读器 {#screen-readers}
自适应对话框会以对话框的形式被宣布，在两种模式下都是如此。底部表单的操作柄对屏幕阅读器是隐藏的。

### 在代码中 {#in-the-code}
- 可访问名称是`header-title`，或你用`aria-labelledby`指向的元素。
- 使用`aria-describedby`来连接描述。
- 关闭按钮的可访问名称是翻译后的标签`ui.common.close`。
- 自适应弹出框是具有角色`dialog`和`aria-modal="true"`的弹出框，并且会捕获焦点。

## 相关内容 {#related}
- [对话](/design/components/dialog)：此对话所基于的对话，以及内容和按钮的指南
- [按钮](/design/components/button)：页脚中的按钮
- [表单](/design/components/form)：对话中的字段

## 代码中 {#in-code}
该元素是 `<ha-adaptive-dialog>`。它会根据屏幕大小渲染为 `ha-dialog` 或 `ha-bottom-sheet`。以打开 [对话](/design/components/dialog#in-code) 的相同方式打开它，使用 `show-dialog` 事件。

```html
<ha-adaptive-dialog open header-title="Dialog title">
  <ha-icon-button
    slot="headerActionItems"
    label="Help"
    path="..."
  ></ha-icon-button>
  <div>Dialog content</div>
  <ha-dialog-footer slot="footer">
    <ha-button slot="secondaryAction" appearance="plain" data-dialog="close">
      Cancel
    </ha-button>
    <ha-button slot="primaryAction">Submit</ha-button>
  </ha-dialog-footer>
</ha-adaptive-dialog>
```

### 属性 {#attributes}
- `open`：打开对话框。
- `type`：`standard`（默认）或 `alert`。仅在对话模式下使用。
- `width`：`small`、`medium`（默认）、`large` 或 `full`。仅在对话模式下使用。
- `prevent-scrim-close`：阻止通过按 Escape、选择遮罩层或向上滑动底部表单来关闭。
- `header-title` 和 `header-subtitle`：标题文本。
- `header-subtitle-position`：`below`（默认）或 `above` 标题。
- `allow-mode-change`：在屏幕尺寸变化时切换对话框和底部表单。对于表单请关闭此功能，以免字段重置。
- `flexcontent`：使主体成为弹性容器。
- `without-header`：省略标题。
- `hide-close-button`：省略关闭按钮。
- `aria-labelledby` 和 `aria-describedby`：传递给对话框或表单。

### 插槽 {#slots}
- 默认：主体。
- `header`：替换整个头部。
- `headerNavigationIcon`：替换关闭按钮。
- `headerTitle` 和 `headerSubtitle`：在未设置属性时，你自己的标题和副标题。
- `headerActionItems`：右上角的图标按钮或菜单。
- `footer`：页脚，通常是一个 `ha-dialog-footer`。

### 事件 {#events}
- `opened`：对话框或底部表单显示。
- `after-show`：打开动画完成。
- `closed`：对话框或底部表单隐藏。

### 样式 {#styling}
- `--ha-dialog-surface-background`：背景，在两种模式下。
- `--ha-dialog-border-radius`：圆角半径，对话框模式下。
- `--ha-bottom-sheet-surface-background` 和 `--ha-bottom-sheet-scrim-color`：底部表单的背景和遮罩。
- `--ha-dialog-surface-backdrop-filter` 和 `--ha-dialog-scrim-backdrop-filter`：表面和遮罩的背景滤镜。

### 自适应弹出框 {#adaptive-popover-1}
该元素是 `<ha-adaptive-popover>`。它采用与自适应对话框相同的属性和插槽。将 `dialogAnchor` 属性设置为应在其旁边打开的元素。如果没有锚点或屏幕较小，它将回退到自适应对话框。

来源：[`src/components/ha-adaptive-dialog.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-adaptive-dialog.ts)，[`src/components/ha-bottom-sheet.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-bottom-sheet.ts)，和 [`src/components/ha-adaptive-popover.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-adaptive-popover.ts)
