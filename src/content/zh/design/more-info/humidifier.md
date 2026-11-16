---
title: 湿度
description: 湿度或除湿器的多信息视图,为目标湿度设置圆拨.
sidebarGroup: 灯光和气候
---

# 湿度 {#humidifier}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/humidifier/)。

```html
<ha-demo-more-info entity="humidifier.bedroom_humidifier"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

主控是目标湿度,与[气候](/design/more-info/climate)视线相同的圆拨:[控制循环滑动器](/design/components/controls). 每个"保持房间的这个值"设备都使用一个形状,意味着人们学习一次.

在拨号中,你会发现设备正在做什么, 比如湿化或干燥, 目标大数字, 和一个负加按钮。 环上的一个点标记了电流湿度,电流湿度也显示为拨号上方的小标签.

在拨号下,一行菜单中包含次要设置:

- ** 状态**,用于打开或关闭设备。 它总是在那里。
- **模式**,如正常的,生态的,睡眠的,或助推的. 它仅在设备支持模式时显示.

## 设计说明 {#design-notes}

- 与气候景观一样,加湿器没有大的开关和关机. 打开或关闭是菜单,所以拨号保持了它作为主控位置.
- 拨号取去状态和当前动作的颜色,设备关闭时会变灰.
- 湿润剂从启动到目标都填满了环. 一种除湿剂从目标到终点都填充它,因为它能使湿度降低.
- 当设备不报告电流湿度时,拨号上方的标签和环上的点被忽略.
- 模式菜单列出设备报告的模式,每个模式都有自己的图标.

## 在代码中 {#in-code}

视图为 `more-info-humidifier` 在 [`src/dialogs/more-info/controls/more-info-humidifier.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-humidifier.ts) 。 拨号是`ha-state-control-humidifier-humidity`在[`src/state-control/humidifier/`](https://github.com/home-assistant/frontend/tree/dev/src/state-control/humidifier)。 `HumidifierEntityFeature`enum在[`src/data/humidifier.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/humidifier.ts)中。

来源:[`more-info-humidifier.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-humidifier.ts)
