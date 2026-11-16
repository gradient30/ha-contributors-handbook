---
title: 跑马灯文字
description: 当文字过长而无法完全显示时，跑马灯文本会在一行内缓慢来回滚动。
sidebarGroup: 布局和内容
sidebarGroup: 布局与内容

---


# 跑马灯文字 {#marquee-text}
Live demo of `ha-marquee-text`.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/marquee-text)。

```html
<ha-marquee-text style="width: 220px">Bohemian Rhapsody (Remastered 2011), Queen, A Night at the Opera</ha-marquee-text>
```

## 概述 {#overview}
跑马灯文本通过在固定空间内滚动显示一行内容，使其保持可读状态。文本会向左滚动直到末尾可见，然后暂停，再滚回去。适合文本内容完全显示的情况则不滚动。

## 使用场景 {#when-to-use}
适合使用跑马灯文本的情况：

- 自动变化且用户只需瞥一眼的文本，例如媒体播放器对话框中正在播放的歌曲标题，或时钟卡片上的日期行。

不适合使用跑马灯文本的情况：

- 标签、按钮，或用户需要完整读取以完成任务的任何内容
- 大多数其他文本。移动的文本阅读起来更困难且易分心，因此它是例外。应让文本换行，或使用省略号截断，并在其他地方显示完整文本。
- 多行长文本。请使用 [faded](/design/components/faded) 内容。

## 解剖结构 {#anatomy}
1. **容器**：占用可用的全部宽度，并裁剪文本
2. **文本**：单行文本，在容器内移动

## 变体 {#variants}
### 鼠标悬停时暂停 {#pause-on-hover}
跑马灯文本在鼠标指针悬停时可以暂停，因此人们可以停下文本以阅读。当文本被触摸时，也会暂停。

`ha-marquee-text`的实时演示。

```html
<ha-marquee-text pause-on-hover style="width: 220px">Hover over me to pause this long line of text</ha-marquee-text>
```

## 行为 {#behavior}
- **适合**：适合容器的文本不会移动。
- **过长**：文本以每秒15像素（在60 Hz屏幕上）的速度向左滚动，直到其末端可见，暂停1秒，然后滚动回起始位置，再次暂停，然后重复。
- **悬停**：当启用暂停时，文本在鼠标指针悬停或被触摸时停止，并在鼠标离开或触摸结束后继续。没有启用暂停时，悬停无效果。
- 文本不能被选中，也不会对指针本身作出反应。

## 规格 {#specs}
| 属性 | 值 |
| --- | --- |
| 宽度 | 容器的 100% |
| 速度 | 默认每秒 15 像素。组件每帧将文本移动速度的六十分之一，因此在超过 60 Hz 的屏幕上滚动会更快。 |
| 在每端停顿 | 默认 1000毫秒 |
| 字体大小 | 1em，与周围文本大小相同 |
| 换行 | 无，文本保持在一行 |

组件不会设置自己的颜色。文本保持周围页面的颜色。

## 指南 {#guidelines}
作为实时演示的可行与不可行示例。

**可行:** 在鼠标悬停时启用暂停，这样人们可以停下文字来阅读。

```html
<ha-marquee-text pause-on-hover style="width: 220px">Bohemian Rhapsody (Remastered 2011), Queen, A Night at the Opera</ha-marquee-text>
```

**不可行:** 让文字一直滚动而没有任何停止方式。

```html
<ha-marquee-text style="width: 220px">Bohemian Rhapsody (Remastered 2011), Queen, A Night at the Opera</ha-marquee-text>
```

前端的每个使用都在悬停时暂停，你的也应该如此。

## 可访问性 {#accessibility}
### 键盘 {#keyboard}
跑马灯文字无法聚焦，也没有键盘交互。暂停只在使用指针或触控时有效。

### 动作 {#motion}
滚动不会考虑系统的减少动画设置。即使用户请求减少动画，它仍然会移动。这又是保持其用于那种人们只是瞥一眼的文字的一个原因。

### 屏幕阅读器 {#screen-readers}
屏幕阅读器会读取完整文字，而不仅是可见部分。

### 在代码中 {#in-the-code}
该组件没有角色。默认插槽中的文字是页面的一部分。

## 相关 {#related}
- [Faded](/design/components/faded)：多行的长文本，被截断并淡出

## 在代码中 {#in-code}
该元素是 `<ha-marquee-text>`。它占据其容器的全部宽度，因此需要通过布局或宽度来限制它。

```html
<ha-marquee-text pause-on-hover>
  Bohemian Rhapsody (Remastered 2011)
</ha-marquee-text>
```

组件在首次渲染时测量文本一次。如果文本后来发生变化并变长或变短，滚动距离不会再次测量。

### 属性 {#attributes}
- `speed`：滚动速度，以像素每秒为单位。默认值为 `15`。
- `pause-duration`：在每一端暂停的时间，以毫秒为单位。默认值为 `1000`。
- `pause-on-hover`：当指针悬停在文本上或触摸时暂停滚动。默认关闭。

### 插槽 {#slots}
- 默认：文本。保持单行纯文本。

来源: [`src/components/ha-marquee-text.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-marquee-text.ts)
