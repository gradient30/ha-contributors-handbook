---
title: 风扇
description: 风扇的更info视图,带有速度控制以及预设,方向,振荡的菜单.
sidebarGroup: 灯光和气候
sidebarGroup: 灯光与气候

---

# 风扇 {#fan}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/fan/)。

```html
<ha-demo-more-info entity="fan.bedroom_fan"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

风扇的主要控制是其速度. 其形状取决于风扇有多少速度:

- ** 大于5个速度**:一个高大的垂直 [控制滑动器](/design/components/controls) 百分比,下面有一个电源按钮. 上面的卧室风扇以10%的台阶移动,从而获得滑动器.
- **5 速度或更短**:一个垂直的[选择控件](/design/components/controls),一个按钮用于关闭,一个按钮用于每个速度. 速度可达3的扇形获得名称和图标,如**Off**,**Low**,**Medium**和**High**. 速度为4或5的粉丝得到数字.
- **没有速度控制**:一个大开关和关机开关,上面有扇形图标,上面有横线扇.

当风扇打开并具有速度时,顶部的州会显示它,比如**40%**. 当它关闭, 它显示 **Off **。

在主控下方,一行菜单持有次要设置. 每个只显示当扇子支持它:

- 预设模式,如自动或睡眠.
- 方向,**前进**或**逆转**。
- 振动,上或下.

## 设计说明 {#design-notes}

- 风扇滑动器和速度按钮采用状态的颜色,因此跑动的风扇是彩色的,关闭的风扇是灰色的.
- 滑动器向风扇支持的步子急转直下,因此无法以风扇没有的速度着陆.
- 动力按钮只显示在滑动 很好看的旁边,并且只有在风扇可以打开和关闭时才显示. 使用速度按钮,**Off**j是步法之一,所以一个单独的按钮会说两次同样的话.
- 振荡菜单使用两个图标:箭头回转和转动为上,划出为下.

## 在代码中 {#in-code}

视图为 `more-info-fan` 在 [`src/dialogs/more-info/controls/more-info-fan.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-fan.ts) 。 速度控制在[`src/state-control/fan/`](https://github.com/home-assistant/frontend/tree/dev/src/state-control/fan)中为`ha-state-control-fan-speed`,没有速度的开关在[`src/state-control/`](https://github.com/home-assistant/frontend/tree/dev/src/state-control)中为`ha-state-control-toggle`. 速度助手,如`computeFanSpeedCount`和`FAN_SPEED_COUNT_MAX_FOR_BUTTONS`,而`FanEntityFeature`enum 生活于[`src/data/fan.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/fan.ts).

来源:[`more-info-fan.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-fan.ts)
