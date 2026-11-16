---
title: 覆盖
description: 百叶窗,百叶窗,车库门等封面的更多信息视图,带有位置滑动器或打开和关闭按钮.
sidebarGroup: 开幕和安全
---

# 覆盖 {#cover}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/cover/)。

```html
<ha-demo-more-info entity="cover.bedroom_blinds"></ha-demo-more-info>
<ha-demo-more-info entity="cover.garage_door"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

盖子有很多种,从停在任何地方的百叶窗,到只上下行驶的车库门. 景色从封面能做什么中选择其主要控制.

- **postition**:可以设置到一个位置的封面得到一个高大的垂直[控制滑动器](/design/components/controls). 滑板从上而下填充,如封面本身:完全闭合的盲文是全栏. 卧室的百叶窗在第一个演示 工作像这样。
- ** Tilt 位置**:一个可以倾斜到一个位置的有滑板的封面,在旁边得到第二个滑板. 它显示一个标记,而不是一个填充, 在一个条纹背景上,看起来像斜纹。
- ** 按钮**:没有位置的封面为** Open**、** Stop**和** 关闭**的栏目[控制按钮](/design/components/controls)。 第二场演示的车库门就是这样的 一个同样倾斜的封面在十字架上得到按钮,侧面有倾斜的按钮,**停止**中间.
- **只打开和关闭**:一个可以打开和关闭,但不能停止或倾斜的封面,得到一个大开关,有打开和关闭封面的图标.

一个支持位置和按钮的封面得到两者. 位于位置模式和按钮模式之间的主控制开关下方的两个圆形按钮. 视图以位置模式开始 。

顶端的州将州和位置结合,如**Open ^ 70%**. 封面完全打开或关闭时会离开位置,所以你读 ** 关闭 ** ,而不是 ** 关闭 ^ 0 + 。

## 设计说明 {#design-notes}

- 图标跟随封面的装置类,所以一个车库门显示一个车库,而百叶窗显示的是百叶窗.
- 现在没有道理的按钮被禁用。 蟹栏上方的车库门是关闭的,所以**关闭**是灰色的。
- 当集成无法知道一个封面的真实状态(一个假设状态)时,开关和关闭开关会变成两个独立的按钮,所以可以总是发送两个命令.
- 执行一项任务 支持位置的封面可以显示控件下面最爱的位置 一次敲击 这些来自实体设置,不是这些演示的一部分。
- 在封面组中,成员封面显示在控件下方为瓦片卡,每个卡片都有自己的位置滑动器.

## 在代码中 {#in-code}

视图为 `more-info-cover` 在 [`src/dialogs/more-info/controls/more-info-cover.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-cover.ts) 。 主要控制在 [`src/state-control/cover/`](https://github.com/home-assistant/frontend/tree/dev/src/state-control/cover): `ha-state-control-cover-position`, `ha-state-control-cover-tilt-position`, `ha-state-control-cover-buttons` 和`ha-state-control-cover-toggle` 中. 最喜欢的位置在 [`src/dialogs/more-info/components/covers/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs/more-info/components/covers) 。 功能在[`src/data/feature/cover_entity_feature.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/feature/cover_entity_feature.ts)中,位置帮助者在[`src/data/cover.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/cover.ts)中.

来源:[`more-info-cover.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-cover.ts)
