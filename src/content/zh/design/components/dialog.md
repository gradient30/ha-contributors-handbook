---
title: 对话
description: 对话框会在你正在做的事情之上要求你做出决定或输入内容。
sidebarGroup: 反馈与状态
---


# 对话 {#dialog}
## 概述 {#overview}
对话框会打断当前操作。使用它们来处理需要立即注意的事项：确认操作、简短表单或选择。对于更大的内容，请使用页面。

前端的对话框基于 [Material Design 3](https://m3.material.io/components/dialogs/overview)，并进行了本页所述的调整。

## 使用场景 {#when-to-use}
使用对话框的情况：

- 确认某个操作，尤其是不可撤销的操作
- 简短表单，例如重命名某个内容
- 用户必须做出的选择，然后才能继续

不要使用对话框的情况：

- 不阻塞任何操作的消息。使用 [警告](/design/components/alert)。
- 内容需要比对话框更多的空间。使用专门的页面。
- 用户在页面上显示和隐藏的内容。使用 [展开面板](/design/components/expansion-panel)。

## 结构 {#anatomy}
1. **遮罩层**：对话框背后的覆盖层
2. **表面**：对话框本身，带有圆角和阴影
3. **关闭按钮**：位于头部左上角
4. **标题**：头部文字，可在其上方或下方添加可选副标题
5. **头部操作**：右上角的可选图标按钮，如帮助或设置
6. **主体**：内容部分，当内容超出时可滚动
7. **底部**：按钮，位于右下角

当主体被滚动时，在头部下方会出现一条细线。

## 变体 {#variants}
### 标准与警告 {#standard-and-alert}
标准对话框有一个带关闭按钮的标题。在小屏幕上，它会占满整个屏幕。

警告对话框用于警告和确认。在小屏幕上，它仍然是一个对话框，带有圆角。按照设计，它只有按钮，没有关闭按钮。将对话框设为警告对话框本身不会移除关闭按钮：前端的确认对话框会自带没有关闭按钮的标题。

### 宽度 {#width}
有四种宽度：小号、中号（默认）、大号和全屏。使用其中一种，除非有明确需要，否则避免自定义尺寸。

## 行为- **打开**：对话框在遮罩层上以 200 毫秒动画显示。启用减少动画后，会立即显示。焦点会移动到标记为获取焦点的元素，或者移动到对话框本身。 {#behavior}
- **关闭**：关闭按钮、对话框中标记为关闭按钮的按钮、<kbd>Escape</kbd>、以及选择遮罩层都会关闭对话框。随后焦点会返回到打开它的元素。
- **受保护的关闭**：当有人在对话框中更改了表单时，<kbd>Escape</kbd> 或选择遮罩层不会关闭对话框。相反，它会轻微抖动（250 毫秒脉冲）。这样可防止意外丢失工作。确认对话框也以相同方式工作。
- **滚动**：当内容不适合时，主体会滚动，而对话框背后的页面不会滚动。

- **小屏幕**：宽度最多450像素或高度最多500像素，标准对话框会填满屏幕，没有圆角。

## 规格| 属性 | 值 | 令牌 | {#specs}
| --- | --- | --- |
| 宽度，小 | 320px | `--ha-dialog-width-sm` |
| 宽度，中 | 580px | `--ha-dialog-width-md` |
| 宽度，大 | 1024px | `--ha-dialog-width-lg` |
| 宽度，全屏 | 屏幕的95%，在安全区域内 | `--ha-dialog-width-full` |
| 最大高度 | 安全高度减去80px | `--ha-space-20`，通过 `--ha-dialog-max-height` |
| 圆角 | 24px，小屏幕标准对话框为0 | `--ha-border-radius-3xl`，通过 `--ha-dialog-border-radius` |
| 背景 | 卡片背景 | `--card-background-color`，通过 `--ha-dialog-surface-background` |
| 阴影 | 大阴影 | `--wa-shadow-l`，通过 `--dialog-box-shadow` |
| 头部最小高度 | 48px | `--ha-space-12` |
| 头部内边距 | 左右4px，大屏幕为8px | `--ha-space-1`，`--ha-space-2` |
| 标题 | 20px，字体粗细500，行高1.2 | `--ha-font-size-xl`，`--ha-font-weight-medium`，`--ha-line-height-condensed` |
| 副标题 | 14px，行高1.6 | `--ha-font-size-m`，`--ha-line-height-normal` |
| 副标题颜色 | 次要文本颜色 | `--secondary-text-color` |
| 内容区内边距 | 顶部 0，其余边 24px | `--ha-space-6`, 至 `--dialog-content-padding` |
| 页脚内边距 | 顶部 12px，其余边 16px | `--ha-space-3`, `--ha-space-4` |
| 页脚按钮间距 | 12px | `--ha-space-3` |
| 打开和关闭动画 | 200ms，减少动画时 0ms | `--ha-dialog-show-duration`, `--ha-dialog-hide-duration` |

## 指南 {#guidelines}
### 布局 {#layout}
- 保持对话框狭窄。设计指南规定最大宽度为560像素，警告和确认对话框固定为320像素。代码没有那么严格：默认宽度为580像素，确认对话框也使用这个宽度。需要更多空间？使用专用页面。
- 关闭按钮位于左上角，适用于所有屏幕尺寸。
- 额外的图标按钮，如帮助、设置或展开按钮，位于右上角。如果超过两个，它们会放入溢出菜单。
- 主要操作与**取消**按钮组合在右下角。在移动设备上，全屏对话框将这些按钮固定在底部。
- 警告和确认对话框仅有按钮，没有关闭按钮。

### 关闭 {#closing}
- 每个带有操作的对话框都有退出方式：在桌面端有一个 **取消** 按钮和关闭按钮，在移动端有关闭按钮。
- 当有人在对话框中更改了表单时，按 Escape 键或点击对话框外部不会关闭它。这可以防止意外丢失工作。

### 按钮 {#buttons}
示例和注意事项。

**示例:** 将一个普通的“取消”按钮与一个主要操作按钮组合。

```html
<ha-button appearance="plain">Cancel</ha-button>
<ha-button>Save</ha-button>
```

**注意:** 不要添加第三个按钮导致任务未完成。

```html
<ha-button appearance="plain">Cancel</ha-button>
<ha-button appearance="outlined">Save for later</ha-button>
<ha-button>Save</ha-button>
```

示例和注意事项。

**示例:** 对破坏性操作使用危险样式。

```html
<ha-button appearance="plain">Cancel</ha-button>
<ha-button variant="danger">Delete</ha-button>
```

**注意:** 不要对删除操作使用品牌颜色。

```html
<ha-button appearance="plain">Cancel</ha-button>
<ha-button>Delete</ha-button>
```

- 保持标签简短：**保存**、**删除**、**启用**。
- 避免在一个对话框里使用三个按钮，尤其是当其中一个按钮会导致任务未完成时。

### 内容 {#content}
人们大多只会看标题和按钮。把重要内容放在那里。

- 始终为对话框添加标题。
- 避免在标题中使用用户输入的内容，如名称，这可能会让标题过长而难以阅读。
- 对于不确定的人，请使用描述：解释将会发生什么。
- 保持简短。

删除仪表板的确认对话框：

> **删除仪表板？**
>
> 仪表板 Kitchen 将从 Home Assistant 永久删除。
>
> **取消** / **删除**

## 可访问性 {#accessibility}
### 键盘 {#keyboard}
| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 在对话框中移动焦点。对话框打开时，焦点保持在对话框内。 |
| <kbd>Escape</kbd> | 关闭对话框，除非关闭被保护。然后对话框会抖动并保持打开状态。 |
| <kbd>Enter</kbd> 或 <kbd>Space</kbd> | 选择焦点所在的按钮，像任何按钮一样。 |

### 焦点 {#focus}
当对话框打开时，焦点会移动到对话框内：移动到表单的第一个字段，或移动到对话框本身。当对话框关闭时，焦点会返回到之前拥有焦点的元素。对话框打开时，其余页面无法访问。

### 目标大小 {#target-size}
关闭按钮是一个 48px x 48px 的图标按钮。

### 屏幕阅读器 {#screen-readers}
对话框会被宣布为对话框，其标题作为其名称。确认对话框还会朗读其描述。关闭按钮会以用户的语言宣布为“关闭”。

### 在代码中 {#in-the-code}
- 对话框是一个原生的 `<dialog>` 元素，以模态形式打开，因此它具有 `dialog` 角色，且其背后的页面处于不可操作状态。
- 焦点移动到具有 `autofocus` 的元素。那些委托焦点的组件，如 `<ha-form autofocus>`，会将焦点传递到它们的第一个字段。
- 可访问名称是 `header-title`，或者对于将标题放在插槽中的对话框，则为 `accessibleLabel`。
- 使用 `aria-describedby` 来关联描述，就像确认对话框那样。
- 关闭按钮的可访问名称使用翻译后的标签 `ui.common.close`。

## 相关 {#related}
- [自适应对话框](/design/components/adaptive-dialog)：在手机上会变成底部弹出的对话框
- [按钮](/design/components/button)：页脚中的按钮
- [警告](/design/components/alert)：不会阻塞任何操作的消息
- [表单](/design/components/form)：对话框中的字段
- [界面文本](/design/ui-text)：如何书写标题和标签

## 代码中 {#in-code}
该元素是 `<ha-dialog>`。它基于 [Web Awesome 对话框](https://webawesome.com/docs/components/dialog/)。在构建新对话框之前，请查看 [前端仓库](https://github.com/home-assistant/frontend/tree/dev/src/dialogs) 中现有的对话框。

通过触发 `show-dialog` 事件来打开对话框，并让它自行加载：

```ts
fireEvent(this, "show-dialog", {
  dialogTag: "dialog-example",
  dialogImport: () => import("./dialog-example"),
  dialogParams: { title: "Example", data: someData },
});
```

- 对于新对话框，使用 `DialogMixin`（[`src/dialogs/dialog-mixin.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/dialog-mixin.ts)）。从其 `params` 属性中读取参数，并调用 `closeDialog()` 来关闭它。
- 对于简单的标题文本，使用 `header-title` 和 `header-subtitle`，当需要更多内容时使用标题插槽。
- 将按钮放在 `ha-dialog-footer` 的 `primaryAction` 和 `secondaryAction` 插槽中。
- 在第一个可聚焦元素（如 `<ha-form autofocus>`）上添加 `autofocus`。

```html
<ha-dialog open header-title="Rename" width="small">
  <ha-form autofocus></ha-form>
  <ha-dialog-footer slot="footer">
    <ha-button slot="secondaryAction" appearance="plain" data-dialog="close">
      Cancel
    </ha-button>
    <ha-button slot="primaryAction">Rename</ha-button>
  </ha-dialog-footer>
</ha-dialog>
```

### 属性 {#attributes}
- `open`：打开对话框。
- `type`：`standard`（默认）或 `alert`。标准对话框在小屏幕上填充屏幕，警报对话框保持为对话框。
- `width`：`small`、`medium`（默认）、`large` 或 `full`。
- `prevent-scrim-close`：阻止通过按 Esc 键或选择遮罩关闭。对话框将抖动代替关闭。
- `header-title` 和 `header-subtitle`：标题文本。
- `header-subtitle-position`：`below`（默认）或 `above` 标题。
- `flexcontent`：使主体成为 flex 容器。
- `without-header`：省略标题。
- `aria-labelledby` 和 `aria-describedby`：传递给对话框。

### 插槽 {#slots}
- 默认：主体。
- `header`：替换整个标题。
- `headerNavigationIcon`：替换关闭按钮。
- `headerTitle` 和 `headerSubtitle`：当未设置属性时使用你自己的标题和副标题。
- `headerActionItems`：右上角的图标按钮。
- `footer`：页脚，通常为 `ha-dialog-footer`。

### 事件 {#events}
- `opened`：对话框显示。
- `after-show`：打开动画完成。
- `closed`：对话框隐藏。

### 样式 {#styling}
- `--dialog-content-padding`：主体的内边距。
- `--ha-dialog-show-duration` 和 `--ha-dialog-hide-duration`：动画持续时间。
- `--ha-dialog-surface-background`：背景。
- `--ha-dialog-border-radius`：圆角。
- `--dialog-box-shadow`：阴影。
- `--ha-dialog-surface-backdrop-filter` 和 `--ha-dialog-scrim-backdrop-filter`：表面和遮罩的背景滤镜。
- `--dialog-surface-margin-top`：表面的上边距。

来源：[`src/components/ha-dialog.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-dialog.ts)
