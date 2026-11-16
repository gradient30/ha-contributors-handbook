---
title: 下拉菜单
description: 下拉菜单显示按钮后面的操作或选项菜单。
sidebarGroup: 动作
sidebarGroup: 操作

---


# 下拉菜单 {#dropdown}
实时演示 `ha-dropdown`、`ha-button`、`ha-dropdown-item`、`ha-svg-icon`。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/dropdown)。

```html
<ha-dropdown>
  <ha-button slot="trigger" appearance="outlined" with-caret>Actions</ha-button>
  <ha-dropdown-item value="edit">
    <ha-svg-icon slot="icon" path="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z"></ha-svg-icon>
    Edit
  </ha-dropdown-item>
  <ha-dropdown-item value="duplicate">
    <ha-svg-icon slot="icon" path="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z"></ha-svg-icon>
    Duplicate
  </ha-dropdown-item>
  <ha-dropdown-item value="download">
    <ha-svg-icon slot="icon" path="M5,20H19V18H5M19,9H15V3H9V9H5L12,16L19,9Z"></ha-svg-icon>
    Download
  </ha-dropdown-item>
  <ha-dropdown-item value="delete" variant="danger">
    <ha-svg-icon slot="icon" path="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></ha-svg-icon>
    Delete
  </ha-dropdown-item>
</ha-dropdown>
```

## 概览 {#overview}
下拉菜单将不需要一直显示的操作集中在一个按钮后面。在 Home Assistant 中最常见的情况是溢出菜单：页面、卡片或行右上角的三点按钮，其中包含可以对该项目执行的所有操作。它保持界面整洁，同时操作只需一次点击即可访问。

## 何时使用 {#when-to-use}
使用下拉菜单的情况：

- 对某个项目进行不常用的操作，如 **复制** 或 **下载**
- 查看选项，如显示哪些列或排序顺序
- 在子菜单中列出相关项目的简短列表，如将某物移动到的区域

不使用下拉菜单的情况：

- 屏幕的主要操作。如果用户访问某个屏幕是为了保存，那么 **保存** [按钮](/design/components/button) 应该放在屏幕本身。
- 在表单中选择一个值。下拉菜单是菜单，而不是表单字段。对于少量且需要解释的选项，请使用选择器或 [选择框](/design/components/select-box)。

## 解剖结构 {#anatomy}
1. **触发器**：用来打开菜单的元素，比如图标按钮或带有下拉箭头的按钮
2. **菜单**：带有项目的浮起面板
3. **项目**：一个操作或选项，带有标签
4. **图标**：可选，在项目标签前
5. **复选标记**：在复选框项目上，显示该选项是否开启
6. **详情**：可选的额外内容，位于标签后面，例如键盘快捷键
7. **子菜单指示器和子菜单**：在有子菜单的项目上，末端有一个箭头，并且旁边有第二个菜单

## 变体 {#variants}
### 触发器 {#trigger}
在前端，触发器通常是带有三点图标的图标按钮，菜单在其下方打开，对齐到按钮末端。带有下拉箭头的[按钮](/design/components/button)也可以使用，当有标签时，可以更容易找到菜单。

### 操作项 {#action-items}
保持标签简短，当项目是一个动作时以动词开头：**编辑**、**复制**、**下载**。在标签前添加图标可以帮助人们浏览较长的菜单。

破坏性操作，如 **删除**，使用危险颜色：标签和图标会变红。

### 选项和切换 {#options-and-toggles}
下拉菜单也可以包含选项。复选框项用于开关设置，例如显示哪些列。已选项表示从一个集合中当前的选择，例如排序顺序。

`ha-dropdown`，`ha-button`，`ha-dropdown-item` 的现场演示。

```html
<ha-dropdown>
  <ha-button slot="trigger" appearance="plain" with-caret>View</ha-button>
  <ha-dropdown-item type="checkbox" checked>Show area</ha-dropdown-item>
  <ha-dropdown-item type="checkbox" checked>Show integration</ha-dropdown-item>
  <ha-dropdown-item type="checkbox">Show status</ha-dropdown-item>
</ha-dropdown>
<ha-dropdown>
  <ha-button slot="trigger" appearance="plain" with-caret>Sort by</ha-button>
  <ha-dropdown-item value="name" selected>Name</ha-dropdown-item>
  <ha-dropdown-item value="area">Area</ha-dropdown-item>
  <ha-dropdown-item value="modified">Last modified</ha-dropdown-item>
</ha-dropdown>
```

### 子菜单和禁用项 {#submenus-and-disabled-items}
将相关项放在子菜单中，例如要移动到的区域列表，这样主菜单会保持简短。

当操作存在但当前不可执行时，请禁用该项。

`ha-dropdown`，`ha-button`，`ha-dropdown-item` 的现场演示。

```html
<ha-dropdown>
  <ha-button slot="trigger" appearance="plain" with-caret>More</ha-button>
  <ha-dropdown-item value="rename">Rename</ha-dropdown-item>
  <ha-dropdown-item value="paste" disabled>Paste</ha-dropdown-item>
  <ha-dropdown-item>
    Move to
    <ha-dropdown-item slot="submenu" value="living-room">Living room</ha-dropdown-item>
    <ha-dropdown-item slot="submenu" value="kitchen">Kitchen</ha-dropdown-item>
    <ha-dropdown-item slot="submenu" value="bedroom">Bedroom</ha-dropdown-item>
  </ha-dropdown-item>
</ha-dropdown>
```

## 行为- **打开**：选择触发器会打开菜单，再次选择会关闭菜单。打开一个下拉菜单会关闭其他打开的下拉菜单。菜单从90%缩放并淡入。 {#behavior}
- **位置**：菜单默认在触发器下方打开，并与触发器开始位置对齐。如果没有足够空间，它会翻转到另一侧，并移动以保持距屏幕边缘至少10px。较长的菜单会有最大高度并且可滚动，在手机上会避开刘海和导航栏。
- **悬停**：在可以悬停的指针设备上，项目会显示正常中性填充。危险项目会显示正常的危险填充。
- **焦点**：获取焦点的项目会显示与悬停相同的填充，并带有焦点环。
- **已选**：已选项目会显示安静的主色填充，中等字体粗细，其标签和图标使用主色。

- **已选中**：当复选框项开启时，会显示已标记的复选框图标，关闭时显示空复选框。 
- **已禁用**：禁用的项目显示为50%的不透明度，选择它不会有任何效果。 
- **选择中**：选择一个项目会关闭菜单并将焦点移回触发器。复选框项会先切换其状态。页面可以通过代码保持菜单打开。 
- **关闭**：菜单也可以通过<kbd>Esc</kbd>、<kbd>Tab</kbd>或点击菜单外任何地方来关闭。 
- **子菜单**：将指针从一个项目移到其子菜单时，即使指针路径上经过其他项目，子菜单也保持打开状态。

当触发器是图标按钮时，菜单打开时会显示为已选中。

## 规格 {#specs}
| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 菜单内边距 | 4px | `--ha-space-1` |
| 菜单圆角 | 8px | `--ha-border-radius-md` |
| 菜单边框 | 1px 实线 | `--ha-border-width-sm`, `--ha-color-border-neutral-quiet` |
| 菜单背景 | 卡片背景 | `--card-background-color` |
| 菜单阴影 | 中等阴影 | `--ha-box-shadow-m` |
| 字体大小 | 14px | `--ha-font-size-m` 到 `--ha-dropdown-font-size` |
| 项目最小高度 | 40px | `--ha-space-10` |
| 项目内边距 | 上下 0.5em，左右 1em | 无 |
| 项目圆角 | 4px | `--ha-border-radius-sm` |
| 项目行高 | 1.2 | `--ha-line-height-condensed` |
| 图标与标签之间的间距 | 0.75em | 无 |
| 打开和关闭动画 | 75ms，缓动 | `--ha-animation-duration-instant` |
| 距屏幕边缘距离 | 至少 10px | 无 |
| 聚焦环 | 2px 实线 | `--ha-color-focus` |
| 项目 | 状态 | 背景 | 标签 | 图标 |
| --- | --- | --- | --- | --- |
| 默认 | 静止 | 透明 | `--primary-text-color` | `--ha-color-on-neutral-normal` |
| 默认 | 悬停或聚焦 | `--ha-color-fill-neutral-normal-resting` | `--primary-text-color` | `--ha-color-on-neutral-normal` |
| 危险 | 静止 | 透明 | `--ha-color-on-danger-quiet` | `--ha-color-on-danger-quiet` |
| 危险 | 悬停或聚焦 | `--ha-color-fill-danger-normal-resting` | `--ha-color-on-danger-normal` | `--ha-color-on-danger-quiet` |
| 已选择 | 静止 | `--ha-color-fill-primary-quiet-resting` | `--primary-color` | `--primary-color` |
| 已选择 | 悬停 | `--ha-color-fill-primary-quiet-hover` | `--primary-color` | `--primary-color` |

## 指南 {#guidelines}
- 用动词开始操作标签：**编辑**、**复制**、**下载**。
- 将破坏性操作（如 **删除**）放在菜单末尾，并使用危险类型。
- 当破坏性操作无法撤销时，先通过 [对话框](/design/components/dialog) 请求确认。关于选择正确的词，请参见 [移除、删除、添加或创建](/design/ui-text/remove-delete)。
- 使用子菜单将长列表相关项目移出主菜单。
- 当操作存在但目前无法执行时，应禁用该项目，而不是隐藏它。

## 无障碍功能 {#accessibility}
### 键盘| 键 | 操作 | {#keyboard}
| --- | --- |
| <kbd>回车</kbd> 或 <kbd>空格</kbd> 在触发器上 | 打开或关闭菜单。打开时，焦点移动到第一个项目。 |
| <kbd>向下箭头</kbd> 和 <kbd>向上箭头</kbd> | 将焦点移动到下一个或上一个项目。在末尾时，焦点会循环。 |
| <kbd>Home键</kbd> 和 <kbd>End键</kbd> | 将焦点移动到第一个或最后一个项目。 |
| 输入字母 | 将焦点移动到标签以所输入字母开头的第一个项目。 |
| <kbd>回车</kbd> 或 <kbd>空格</kbd> 在项目上 | 选择该项目，或打开其子菜单。 |
| <kbd>向右箭头</kbd> | 打开焦点项目的子菜单。在从右到左语言中，这是 <kbd>向左箭头</kbd>。 |
| <kbd>向左箭头</kbd> | 关闭子菜单并返回到其项目。在从右到左的语言中，这是 <kbd>向右箭头</kbd>。 |
| <kbd>Escape</kbd> | 关闭菜单，并将焦点移回触发器。 |
| <kbd>Tab</kbd> | 关闭菜单。 |

### 焦点 {#focus}
一次只能有一个项目获得焦点，因此 <kbd>Tab</kbd> 不会浏览每个项目。箭头键用于在项目之间移动。获得焦点的项目会显示焦点环。

### 目标大小 {#target-size}
每个项目的高度至少为 40px。

### 屏幕阅读器 {#screen-readers}
菜单会被宣布为一个菜单，每个项目会以其位置进行宣布，例如“5 个中的第 2 个”。复选框项目会被宣布为已选或未选，禁用的项目会被宣布为禁用，带子菜单的项目会被宣布为有子菜单。被选中的项目看起来是选中的，但不会被宣布为已选。

### 在代码中 {#in-the-code}
- 菜单具有角色 `menu`，并且是垂直方向的。
- 项目具有角色 `menuitem`。复选框项目具有角色 `menuitemcheckbox`，并具有 `aria-checked`。
- 每个项目在菜单中都有其位置，具有 `aria-posinset` 和 `aria-setsize`。
- 禁用的项目具有 `aria-disabled="true"`。
- 具有子菜单的项目具有 `aria-haspopup="menu"`，并且其子菜单打开时具有 `aria-expanded`。
- 触发器具有 `aria-haspopup="menu"`，并且 `aria-expanded` 设置为 `true` 或 `false`。
- `selected` 属性改变项目的外观，但不设置任何 ARIA 状态。
- 用作触发器的图标按钮需要 `label`，这将成为其可访问名称。

## 相关内容 {#related}
- [按钮](/design/components/button)：用于主要操作以及作为触发器
- [选择框](/design/components/select-box)：在表单中选择一个值
- [对话框](/design/components/dialog)：确认菜单中的破坏性操作
- [UI 文本](/design/ui-text)：如何撰写标签

## 在代码中 {#in-code}
这些元素是 `<ha-dropdown>` 和 `<ha-dropdown-item>`。它们基于 [Web Awesome 下拉菜单](https://webawesome.com/docs/components/dropdown/) 和 [下拉项](https://webawesome.com/docs/components/dropdown-item/)。

```html
<ha-dropdown placement="bottom-end">
  <ha-button slot="trigger" with-caret>Actions</ha-button>
  <ha-dropdown-item value="edit">
    <ha-svg-icon slot="icon" path="..."></ha-svg-icon>
    Edit
  </ha-dropdown-item>
  <ha-dropdown-item value="delete" variant="danger">Delete</ha-dropdown-item>
</ha-dropdown>
```

### 属性 {#attributes}
`<ha-dropdown>`:

- `placement`: 菜单相对于触发器打开的位置。`bottom-start`（默认）、`bottom`、`bottom-end`、`top-start`、`top`、`top-end`、`left-start`、`left`、`left-end`、`right-start`、`right` 或 `right-end`。如果没有足够空间，菜单会翻转到另一侧。
- `distance`: 触发器与菜单之间的距离，以像素为单位。
- `skidding`: 沿着触发器移动菜单的像素数。
- `open`: 打开菜单。

`<ha-dropdown-item>`:

- `value`: 在 `wa-select` 事件中识别条目。
- `variant`: `default` 或 `danger`。
- `type`: `normal`（默认）或 `checkbox`。
- `checked`: 打开复选框条目。
- `selected`: 将条目标记为当前选择项。这是 Home Assistant 中的新增功能，不属于 Web Awesome。
- `disabled`: 禁用条目。
- `href`、`target`、`rel` 和 `download`: 将条目变为链接。当触发器是 `<ha-icon-button>` 时，下拉菜单在打开时会将其标记为选中。你也可以通过从代码设置 `anchorElement` 属性从另一个元素打开菜单。

### 插槽 {#slots}
`<ha-dropdown>`：

- 默认：条目。
- `trigger`：打开菜单的元素，比如按钮或图标按钮。

`<ha-dropdown-item>`：

- 默认：标签。
- `icon`：标签前的图标。
- `details`：标签后的额外内容，比如键盘快捷键。
- `submenu`：子菜单的条目。

### 事件 {#events}
- `wa-select`：当用户选择条目时在 `<ha-dropdown>` 触发。条目在 `event.detail.item` 中，所以请阅读 `event.detail.item.value` 以知道是哪一个。复选条目在事件触发时已经切换。调用 `event.preventDefault()` 可保持菜单打开。
- `wa-show` 和 `wa-after-show`：在菜单打开时触发，并在动画之后。
- `wa-hide` 和 `wa-after-hide`：在菜单关闭时触发，并在动画之后。

### 样式 {#styling}
- `--ha-dropdown-font-size`：菜单的字体大小。默认值为 `var(--ha-font-size-m)`。
- `--show-duration` 和 `--hide-duration`：打开和关闭动画的持续时间。

来源：[`src/components/ha-dropdown.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-dropdown.ts) 和 [`src/components/ha-dropdown-item.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-dropdown-item.ts)
