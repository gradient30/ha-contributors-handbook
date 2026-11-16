---
title: 开关
description: 可予切换的辅助器或警笛,
sidebarGroup: 应用程序
sidebarGroup: 家电

---

# 开关 {#switch}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/switch/)。

```html
<ha-demo-more-info entity="switch.desk_plug"></ha-demo-more-info>
<ha-demo-more-info entity="input_boolean.guest_mode"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

开关有一件事:开关或关机。 它的视角是较新的视角中最简单的:顶端的状态,下方有一个大垂直的[控制开关](/design/components/controls),顶端有. 它使用一个电源图标来启动, 和一个截断的电源图标关闭。

桌子插头是开关 开机了 宾客模式为切换帮助器(`input_boolean`),关闭. 二者得同观.

## 警报 {#sirens}

警笛得到同样的观点, 带有扬声器图标 和哑音扬声器关闭。 当警笛支持音调,音量,或持续时间时,开关下方的** more control**按钮打开一个视图,你选择音调,音量,和持续时间,然后将警笛打开或关闭。

嗡嗡声没有假家 所以这里没有演示

## 设计说明 {#design-notes}

- 开关带有州色,所以从对面的房间里可以看到是否有东西亮着.
- 当集成无法得知真实状态(假设状态)时,开关会变成两个独立的按钮,一个用于打开,一个用于关闭,所以可以总是发送两个命令.
- 没有亮度的灯光和没有速度的风扇使用与主控相同的开关,带有自己的图标.

## 在代码中 {#in-code}

视图为`more-info-switch`,`more-info-input_boolean`和`more-info-siren`,在[`src/dialogs/more-info/controls/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs/more-info/controls)中。 他们共享 `ha-state-control-toggle` 从 [`src/state-control/ha-state-control-toggle.ts`](https://github.com/home-assistant/frontend/blob/dev/src/state-control/ha-state-control-toggle.ts) , 并传递 图标 用于打开和关闭 。 高级警报控制在 [`src/dialogs/more-info/components/siren/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs/more-info/components/siren) 中, `SirenEntityFeature` enum 在 [`src/data/feature/siren_entity_feature.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/feature/siren_entity_feature.ts) 中。

来源:[`more-info-switch.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-switch.ts)
