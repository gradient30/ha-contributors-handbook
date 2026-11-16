---
title: 褪色
description: 褪色的内容显示了一段长文本的开头，并将其余部分淡出，直到人们选择它。
sidebarGroup: 布局和内容
sidebarGroup: 布局与内容

---


# 褪色 {#faded}
Live demo of `ha-faded`.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/faded)。

```html
<ha-faded>
  <div>
    <p>This release brings a new energy dashboard, faster startup, and a long list of fixes. The automation editor now shows which triggers fired last, so you can see at a glance why an automation ran.</p>
    <p>Several integrations got new entities, and some older options moved from YAML to the user interface. Check the backward-incompatible changes before you update, especially if you use custom templates for your dashboards.</p>
    <p>Thanks to everyone who tested the beta, reported issues, and translated the new strings.</p>
  </div>
</ha-faded>
```

## 概述 {#overview}
渐隐内容显示一段长文本的前几行，并在底部逐渐消失。点击文本的任何位置可以显示全部内容。前几行可以告诉读者是否想继续阅读。

## 何时使用 {#when-to-use}
使用渐隐内容适用于：

- 可选择阅读的文本，如发布说明或长描述

不适用于渐隐内容的情况：

- 用户必须读取的内容，如警告或操作。请放在渐隐区域外。
- 每个人都需要能够打开和关闭的内容，包括键盘用户。请使用[展开面板](/design/components/expansion-panel)。
- 过长的单行文本。请使用[滚动文本](/design/components/marquee-text)，或者允许其换行。

## 解剖结构 {#anatomy}
1. **容器**：在渐隐高度处截断内容，并接收打开它的选择
2. **内容**：默认插槽中的元素
3. **渐隐**：覆盖容器的遮罩，从完全可见到底部变为透明

## 变体 {#variants}
### 高度 {#height}
默认情况下，内容在102像素处被截断。高度可以更改。

`ha-faded` 的实时演示。

```html
<ha-faded faded-height="48">
  <div>
    <p>The front door sensor reports open and closed, and the battery level. It updates within a second of the door moving, and checks in every hour when nothing happens.</p>
    <p>Mount it on the door frame, with the magnet on the door itself, no more than a centimeter apart.</p>
    <p>The battery lasts about two years, and its level shows up as a separate sensor.</p>
  </div>
</ha-faded>
```

## 行为 {#behavior}
- **淡出**：内容在淡出高度处被截断，下方渐隐，指针会变成手形。
- **展开**：点击内容的任意位置即可显示全部内容。展开后，它将保持展开状态。没有办法再次折叠。
- **短内容**：当内容比淡出高度最多高出50像素时，会直接全部显示。隐藏一两行内容只会让用户多点击一次，但几乎节省不了空间。

`ha-faded` 的实时演示。短内容会全部显示。

```html
<ha-faded>
  <div>This update only fixes a few small bugs.</div>
</ha-faded>
```

## 规格 {#specs}
| 属性 | 值 |
| --- | --- |
| 模糊高度 | 默认 102px |
| 当内容最多为多少时显示全部 | 模糊高度加 50px |
| 渐变 | 从上到下的线性渐变：从完全可见到高度的 25%，然后在底部渐变为透明 |
| 模糊时的指针 | `pointer` |
| 打开时的指针 | `default` |

该组件不设置任何颜色、间距或字体类型。内容保持周围页面的样式。

## 指南 {#guidelines}
作为实时演示的做与不做。

**做：** 将可选阅读内容放在淡出部分后面。

```html
<ha-faded faded-height="48">
    <div>
      <p>This release brings a new energy dashboard, faster startup, and a long list of fixes.</p>
      <p>Several integrations got new entities, and some older options moved from YAML to the user interface.</p>
      <p>Thanks to everyone who tested the beta, reported issues, and translated the new strings.</p>
    </div>
  </ha-faded>
```

**不做：** 将警告或人们需要的操作隐藏在淡出部分后面。

```html
<ha-faded faded-height="48">
    <div>
      <p>This release brings a new energy dashboard, faster startup, and a long list of fixes.</p>
      <p>Several integrations got new entities, and some older options moved from YAML to the user interface.</p>
      <p>Back up your configuration before you update. This update can't be undone.</p>
    </div>
  </ha-faded>
```

## 可访问性 {#accessibility}
### 键盘 {#keyboard}
淡出内容没有键盘交互。它只能通过指针或触摸打开，因此使用键盘的用户无法打开它。这也是让人们需要的内容不要放在淡出部分的一个原因。

### 屏幕阅读器 {#screen-readers}
屏幕阅读器可以读取完整文本，即使它是淡出的。它们不会知道有更多内容，或者内容可以被打开。

### 在代码中 {#in-the-code}
- 容器没有角色，不可聚焦，也没有展开或收起状态。
- 隐藏的部分只是被裁剪和遮罩。它仍然留在页面中。

## 相关内容 {#related}
- [扩展面板](/design/components/expansion-panel)：每个人都可以打开和关闭的内容
- [跑马灯文本](/design/components/marquee-text)：太长而无法显示在一行中的文本

## 在代码中 {#in-code}
元素是 `<ha-faded>`。

```html
<ha-faded faded-height="80">
  <div>A long text...</div>
</ha-faded>
```

将内容包裹在一个元素中。高度是根据插槽中的元素来测量的，而纯文本没有可测量的元素。直接放在 `<ha-faded>` 中的纯文本总是会消失，即使它很短。

高度只在组件首次渲染时测量一次。对于稍后渲染的内容，比如 markdown，当 `ha-markdown` 完成时会触发一个 `content-resize` 事件，组件会再次进行测量。

### 属性 {#attributes}
- `faded-height`：内容被截断的像素高度。默认值为 `102`。

### 插槽 {#slots}
- 默认：内容。

来源：[`src/components/ha-faded.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-faded.ts)
