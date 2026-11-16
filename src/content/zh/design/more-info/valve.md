---
title: 阀门
description: 水或气阀的更信息视图,带有开关和关闭开关,按钮,或位置滑动器.
sidebarGroup: 开幕和安全
---

# 阀门 {#valve}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/valve/)。

```html
<ha-demo-more-info entity="valve.garden_irrigation"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

娇娃的工作原理与[覆盖](/design/more-info/cover)一样,它的观点也遵循同样的规则. 主控制取决于阀门支持什么:

- **只打开和关闭**:一个大的垂直[控制开关](/design/components/controls),带有一个打开和关闭阀门的图标. 上面的花园灌溉就是这样的
- ** 停**:也可以停在中途的阀门为** Open**、** Stop**和** Close**取而代之的是[控制按钮](/design/components/controls)。
- **postition**:一个可以设置到位置的阀门得到一个高大的垂直[控制滑动器](/design/components/controls).

一个支持位置和按钮的阀门得到两者,在主控下方有两个圆形按钮来在位置模式和按钮模式之间切换.

顶端的州结合了州和位置,如**Open ^ 40%**,当没有可加时,将位置留出.

## 设计说明 {#design-notes}

- 图标跟随阀门的设备类,如水或气体.
- 阀门没有倾斜,所以没有像盖子一样的按钮交叉.
- 支持一个位置的阀门可以显示控件下面最喜爱的位置. 这些来自实体设置,不是这些演示的一部分。

## 在代码中 {#in-code}

视图为 `more-info-valve` 在 [`src/dialogs/more-info/controls/more-info-valve.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-valve.ts) 。 主要控制在 [`src/state-control/valve/`](https://github.com/home-assistant/frontend/tree/dev/src/state-control/valve) : `ha-state-control-valve-toggle`, `ha-state-control-valve-buttons` 和 `ha-state-control-valve-position` 中 。 最喜欢的位置在 [`src/dialogs/more-info/components/valves/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs/more-info/components/valves) 。 `ValveEntityFeature`enum在[`src/data/valve.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/valve.ts)中。

来源:[`more-info-valve.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-valve.ts)
