---
title: 列表
description: 列表显示了一组行，每行都有一行文本，并且可选地包含一个图标、第二行文本，以及末尾的内容。
sidebarGroup: 布局和内容
sidebarGroup: 布局与内容

---

# 列表 {#list}

实时演示 `ha-list`、`ha-list-item`、`ha-svg-icon`。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/components/list/)。

```html
<ha-list style="width: 100%">
  <ha-list-item graphic="icon" twoline hasMeta>
    <ha-svg-icon slot="graphic" path="M12,21L15.6,16.2C14.6,15.45 13.35,15 12,15C10.65,15 9.4,15.45 8.4,16.2L12,21M12,3C7.95,3 4.21,4.34 1.2,6.6L3,9C5.5,7.12 8.62,6 12,6C15.38,6 18.5,7.12 21,9L22.8,6.6C19.79,4.34 16.05,3 12,3M12,9C9.3,9 6.81,9.89 4.8,11.4L6.6,13.8C8.1,12.67 9.97,12 12,12C14.03,12 15.9,12.67 17.4,13.8L19.2,11.4C17.19,9.89 14.7,9 12,9Z"></ha-svg-icon>
    Network
    <span slot="secondary">Connected over Wi-Fi</span>
    <ha-svg-icon slot="meta" path="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z"></ha-svg-icon>
  </ha-list-item>
  <ha-list-item graphic="icon" twoline hasMeta>
    <ha-svg-icon slot="graphic" path="M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z"></ha-svg-icon>
    Location
    <span slot="secondary">Home</span>
    <ha-svg-icon slot="meta" path="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z"></ha-svg-icon>
  </ha-list-item>
  <ha-list-item graphic="icon" twoline hasMeta>
    <ha-svg-icon slot="graphic" path="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11L21.54,9.37C21.73,9.22 21.78,8.95 21.66,8.73L19.66,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.87,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.13,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.73C2.21,8.95 2.27,9.22 2.46,9.37L4.57,11C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.21,15.05 2.34,15.27L4.34,18.73C4.46,18.95 4.73,19.03 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.13,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.87,18.93C15.5,18.67 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.03 19.54,18.95 19.66,18.73L21.66,15.27C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z"></ha-svg-icon>
    System
    <span slot="secondary">Updates, backups, and logs</span>
    <ha-svg-icon slot="meta" path="M8.59,16.58L13.17,12L8.59,7.41L10,6L16,12L10,18L8.59,16.58Z"></ha-svg-icon>
  </ha-list-item>
</ha-list>
```

## 概览 {#overview}

列表显示了一组相似的项目，人们可以扫描、选择或打开：用于登录的提供商、菜单选项、区域内的设备。每一行都有相同的结构，因此眼睛可以沿着左边缘快速找到所需内容。

> [!注意]
> `ha-list` 和 `ha-list-item` 是较旧的列表，基于 Material Web Components 构建。前端正在迁移到更新的列表系列：`ha-list-base`、`ha-list-item-base`、`ha-list-item-button`、`ha-list-selectable` 和 `ha-list-nav`。前端的许多列表已经在使用它。对于新代码，请使用新系列：请参见本页末尾的 [新列表系列](/design/components/list#the-new-list-family)。本页大部分内容涵盖的是较旧的列表，因为仍有相当多的界面在使用它。

## 何时使用 {#when-to-use}

使用列表的情况：

- 一组类似的项目，供人浏览、选择或打开
- 导航到下一层，每行末尾带有箭头
- 仅显示信息的行，例如值或消息

不要使用列表的情况：

- 对单个项目的操作。请将它们放在 [下拉菜单](/design/components/dropdown) 中。
- 从几个需要解释的选项中选择一个。请使用 [选择框](/design/components/select-box)。
- 人们可以显示和隐藏的内容。请使用 [展开面板](/design/components/expansion-panel)。

## 解剖结构 {#anatomy}

1. **列表**：容器，顶部和底部有8像素的填充
2. **行**：列表中的一个项目
3. **图形**：可选，在行开头的图标、头像或控件
4. **第一行**：行的主要文本
5. **第二行**：可选，位于第一行下方的简短细节
6. **元信息**：可选，位于末尾的内容，如箭头或简短数值

## 变体 {#variants}

### 行 {#rows}

从文本开始，然后只添加有助于人们识别行的内容：

- 开头的**图标**。
- **第二行**，用于简短细节，如状态或描述。
- **末尾**的内容，如行打开某内容时的箭头，或简短的数值。

`ha-list`、`ha-list-item`、`ha-svg-icon`的实时演示。

```html
<ha-list style="width: 100%">
  <ha-list-item>Just text</ha-list-item>
  <ha-list-item twoline>
    Two lines
    <span slot="secondary">With a second line of detail</span>
  </ha-list-item>
  <ha-list-item graphic="icon">
    <ha-svg-icon slot="graphic" path="M12,2A7,7 0 0,0 5,9C5,11.38 6.19,13.47 8,14.74V17A1,1 0 0,0 9,18H15A1,1 0 0,0 16,17V14.74C17.81,13.47 19,11.38 19,9A7,7 0 0,0 12,2M9,21A1,1 0 0,0 10,22H14A1,1 0 0,0 15,21V20H9V21Z"></ha-svg-icon>
    With an icon
  </ha-list-item>
  <ha-list-item hasMeta>
    With something at the end
    <span slot="meta">3</span>
  </ha-list-item>
  <ha-list-item disabled>Disabled</ha-list-item>
</ha-list>
```

### 图像大小 {#graphic-size}

一行在开始处为其图像预留空间，图像可以是以下几种尺寸之一：图标、头像（圆形图片）、中等或大型图片，或者像复选框这样的控件。

### 仅显示信息的行 {#rows-that-only-show-information}

当选中时没有任何操作的行，例如仅显示一个值或消息的行，可以设置为非交互式。这样它就不会有涟漪效果，也不会获得键盘焦点。

## 行为 {#behavior}

- **悬停和按下**：交互行会显示波纹。除非主题设置了其他颜色，否则是黑色。深色主题将其设置为浅灰色。已激活的行的波纹使用主色。
- **焦点**：一次只有一行在标签顺序中。使用箭头键在行之间移动焦点。
- **已激活**：在可以激活行的列表中，选中的行会显示 12% 不透明度的主色调，其图形会变为主颜色。
- **禁用**：文本会变为禁用文本颜色，并且该行无法被选中。
- **长文本**：当第一行内容不适合时，会使用省略号截断。第二行也会被截断，除非该行允许换行。然后该行会随内容增长。

## 规格 {#specs}

| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 单行行高 | 48px | 无 |
| 带图标或头像的单行行高 | 48px | 无 |
| 双行行高 | 72px | 无 |
| 带中号或大号图形的单行行高 | 72px | 无 |
| 左右内边距 | 20px | `--mdc-list-side-padding` |
| 列表上下内边距 | 8px | `--mdc-list-vertical-padding` |
| 图标尺寸 | 24px | `--mdc-list-item-graphic-size` |
| 头像尺寸 | 40px | `--mdc-list-item-graphic-size` |
| 中号和大号图形尺寸 | 56px | `--mdc-list-item-graphic-size` |
| 图标与文字间距（单行） | 20px | `--mdc-list-item-graphic-margin` |
| 图标与文字间距（双行） | 32px | `--mdc-list-item-graphic-margin` |
| 元数据大小 | 24px | `--mdc-list-item-meta-size` |
| 第一行字体大小 | 1rem | `--mdc-typography-subtitle1-font-size` |
| 第二行字体大小 | 0.875rem | `--mdc-typography-body2-font-size` |
| 禁用文本颜色 | 明亮主题为 `#bdbdbd`，暗黑主题为 `#6f6f6f` | `--disabled-text-color` |
| 激活色调 | 12% 不透明度 | `--mdc-ripple-activated-opacity` |

## 指南 {#guidelines}

作为现场演示的注意事项。

**应做:** 保持第一行简短，并将详细信息放在第二行。

```html
<ha-list style="width: 100%">
    <ha-list-item twoline>Network<span slot="secondary">Connected over Wi-Fi</span></ha-list-item>
  </ha-list>
```

**不应做:** 将所有内容放在会被截断的第一行。

```html
<ha-list style="width: 100%">
    <ha-list-item>Network settings, connected over Wi-Fi to your home network</ha-list-item>
  </ha-list>
```

查看 [UI 文本](/design/ui-text) 了解如何编写标签。

## 可访问性 {#accessibility}

### 键盘 {#keyboard}

| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移入列表，选择一行，然后移出列表。 |
| <kbd>向下箭头</kbd> 和 <kbd>向上箭头</kbd> | 将焦点移到下一行或上一行。列表可以让焦点从最后一行换到第一行，反之亦然。 |
| <kbd>Home</kbd> 和 <kbd>End</kbd> | 将焦点移到第一行或最后一行。 |
| <kbd>Enter</kbd> 或 <kbd>空格</kbd> | 激活当前焦点的行。 |

### 焦点 {#focus}

一次只有一行在标签顺序中。箭头键在行之间移动焦点。

### 目标大小 {#target-size}

一行的高度至少为48px，宽度与列表一样宽。

### 屏幕阅读器 {#screen-readers}

默认情况下，屏幕阅读器无法获取列表结构：列表及其行没有角色，因此它只能听到行的文本。禁用的行会被宣布为已禁用。列表可以在代码中获取角色和名称，见下文。

### 在代码中 {#in-the-code}

- 列表及其行默认没有角色。为列表设置 `innerRole`，为行设置 `itemRoles`，例如 `listbox` 和 `option`，并为列表名称设置 `innerAriaLabel`。
- 禁用的行具有 `aria-disabled="true"`。
- 使用角色 `option` 时，选中的行具有 `aria-selected="true"`。
- 拥有 `noninteractive` 的行无法获得焦点。

## 相关内容 {#related}

- [下拉菜单](/design/components/dropdown)：动作菜单
- [选择框](/design/components/select-box)：从几个选项中选择一个
- [展开面板](/design/components/expansion-panel)：用户可以显示和隐藏的内容

## 在代码中 {#in-code}

该元素是 `<ha-list>`，拥有 `<ha-list-item>` 行。两者都扩展了 [Material Web 组件列表](https://github.com/material-components/material-web/tree/mwc/packages/list)。

```html
<ha-list>
  <ha-list-item graphic="icon" twoline hasMeta>
    <ha-svg-icon slot="graphic" path="..."></ha-svg-icon>
    Network
    <span slot="secondary">Connected over Wi-Fi</span>
    <ha-svg-icon slot="meta" path="..."></ha-svg-icon>
  </ha-list-item>
</ha-list>
```

HTML 中的属性名称不区分大小写，因此 `hasMeta` 和 `hasmeta` 是相同的。

### ha-list 的属性 {#attributes-of-ha-list}

- `activatable`：显示所选行为已激活状态。
- `multi`：允许选择多行。
- `wrapFocus`：箭头键从最后一行回到第一行，反之亦然。
- `rootTabbable`：使列表本身可聚焦，而不是第一行。
- `noninteractive`：关闭整个列表的选择和键盘导航。
- `innerRole` 和 `innerAriaLabel`：内部列表元素的角色和可访问名称。
- `itemRoles`：每行的角色，如 `option`。

### ha-list-item 的属性 {#attributes-of-ha-list-item}

- `graphic`：为 `graphic` 插槽中的内容保留空间。`icon`、`avatar`、`medium`、`large` 或 `control`。
- `twoline`：将 `secondary` 插槽显示为第二行。
- `multiline-secondary`：允许第二行换行，而不是截断它。
- `hasMeta`：在末尾显示 `meta` 插槽。
- `noninteractive`：行无法被选中或获取焦点。
- `disabled`：禁用该行。
- `selected` 和 `activated`：选择状态。
- `value`：标识该行的值。

### ha-list-item 的插槽 {#slots-of-ha-list-item}

- 默认：第一行文本。
- `secondary`：当设置 `twoline` 时的第二行。
- `graphic`：当设置 `graphic` 时的起始图标、头像或控件。
- `meta`：当设置 `hasMeta` 时的末尾内容。

### 事件 {#events}

- `action` 于 `ha-list`: 一行被激活。`detail.index` 是该行的索引。
- `selected` 于 `ha-list`: 选择已更改。`detail.index` 是所选索引，或者使用 `multi` 的索引集合。
- `request-selected` 于 `ha-list-item`: 该行请求被选中或取消选中。`detail.selected` 是新的状态，`detail.source` 表示它是来自 `interaction` 还是 `property` 的更改。

### 样式 {#styling}

- `--mdc-list-side-padding`：行两侧的内边距。默认值为 `20px`。
- `--mdc-list-side-padding-left` 和 `--mdc-list-side-padding-right`：单侧的内边距。
- `--mdc-list-item-graphic-margin`：图形与文本之间的间距。
- `--mdc-list-item-meta-display`：元数据插槽的显示。

来源：[`src/components/ha-list.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-list.ts) 和 [`src/components/ha-list-item.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-list-item.ts)

## 新列表系列 {#the-new-list-family}

新的列表从一开始就可访问且支持键盘操作。根据列表的含义选择容器，然后根据行的功能选择条目。它们尚未成为本站的实时组件，因此没有演示。

### 容器 {#containers}

- `<ha-list-base>`：一个普通列表，角色为 `list`。箭头键在行之间移动焦点，<kbd>Home</kbd> 和 <kbd>End</kbd> 跳到第一个和最后一个可用行，<kbd>Page up</kbd> 和 <kbd>Page down</kbd> 翻页，<kbd>Enter</kbd> 或 <kbd>Space</kbd> 激活聚焦行。一次只有一行在 Tab 顺序中。
- `<ha-list-selectable>`：一个供人选择的列表，角色为 `listbox`。其行是 `<ha-list-item-option>`。设置 `multi` 以允许选择多个。
- `<ha-list-nav>`：一个链接列表，包装在 `<nav>` 地标里。其行是 `<ha-list-item-button>`，具有 `href`。用 `aria-label` 命名地标。

容器的属性：- `wrap-focus`：箭头键在列表末端时会环绕。
- `virtual-focus`：焦点保持在列表外，例如在选择器的搜索字段中。列表用 `active` 标记键盘指向的行，并将其滚动到视图中。拥有焦点的元素用 `moveActiveItem()` 移动它。
- `aria-label`：可访问名称。
- `multi`：仅在 `ha-list-selectable` 上，允许选择多个选项。

事件：

- `ha-list-activated`：在聚焦的行上 <kbd>Enter</kbd> 或 <kbd>Space</kbd>。`detail` 具有 `index` 和 `item`。
- `ha-list-item-selected` 和 `ha-list-item-deselected`：在 `ha-list-selectable` 时，选项被选中或取消选中。`detail` 是选项的索引。仅在 `multi` 时触发取消选中。

样式：`--ha-list-gap` 设置行之间的间距，`--ha-list-padding` 设置列表周围的内边距。两者默认值为 `0`。

### 项目 {#items}

每个项目都有相同的行布局，包含以下插槽和属性：

- `start`：前置部分，如图标或头像。
- `end`：后置部分，如数值或箭头。
- `headline` 和 `supporting-text`：第一行和第二行，作为属性或插槽。
- `content`：替换整个中间部分。
- `disabled`：使行变暗并阻止指针。

这些项目：- `<ha-list-item-base>`：只显示信息的一行，角色为 `listitem`。设置 `interactive` 可以将其放入列表的键盘导航中而不执行任何操作，就像用户可以排序的一行一样。
- `<ha-list-item-button>`：会执行操作的一行。当它有 `href` 时渲染为链接，否则渲染为按钮。整行都是目标。
- `<ha-list-item-option>`：用户可以选择的一行，角色为 `option` 和 `aria-selected`。列表拥有选择权。使用 `appearance="checkbox"` 时显示复选框，可位于 `start` 或 `end`，并且具有 `selection-position`。默认外观 `line` 会高亮显示选中的行。

行的样式：- `--ha-row-item-min-height`：行的最小高度。默认值为 `48px`。
- `--ha-row-item-padding-block`、`--ha-row-item-padding-inline` 和 `--ha-row-item-gap`：行的内边距，以及其各部分之间的间距。
- `--ha-list-item-focus-background` 和 `--ha-list-item-active-background`：键盘聚焦时的背景，以及 `active` 行的背景。
- `--ha-list-item-selected-background`：选定选项的背景，与 `appearance="line"` 一起使用。

来源：[`src/components/list/`](https://github.com/home-assistant/frontend/tree/dev/src/components/list) 和 [`src/components/item/`](https://github.com/home-assistant/frontend/tree/dev/src/components/item)
