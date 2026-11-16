---
title: 知道了 更新
description: 更新实体的更多信息视图,包含版本,发布注释,以及跳过或安装的按钮.
sidebarGroup: 应用程序
---

# 知道了 更新 {#update}

Live demo of `ha-demo-more-info`, 连接到一个 demo Home Assistant.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/more-info/update/)。

```html
<ha-demo-more-info entity="update.home_assistant_core"></ha-demo-more-info>
<ha-demo-more-info entity="update.desk_plug_firmware"></ha-demo-more-info>
```

## 取证结果 {#what-it-shows}

更新是您行动前需要读到的东西,所以这个视图是一个短页,而不是一个控制. 它没有较新的设计,具有较大的状态. 它从状态行开始,如 ** Update 可用** 或 ** Up-date **,对话框使用屏幕的全高,为发布注释留下空间.

从上到下:

- **Title **:更新的内容名称,如QQH0}**.
- ** 版本**:已安装的版本和最新版本。
- ** 发布公告**:一个链接,当更新有一个链接。
- ** 释放说明**:完整的说明,当整合可以提供时。 否则,简短的发布摘要,当有。
- ** 备份**:对于支持它的更新,在更新前创建备份的选项.
- ** 动作**:** Skip** 和** 更新** 在底部。

Home Assistant Core更新有新版本,有发布注释. 台式插件固件是最新的,因此**Skip**和**Update**已禁用.

## 设计说明 {#design-notes}

- 安装更新时, 标题上方显示进度栏 。 整合报告进展时会填满,不整合时会前后移动.
- ** Skip** 在你跳过一个版本时变成** Clear 跳过** 并且没有其他可安装的,所以你可以撤销它.
- ** Update ** 显示更新安装时的旋转器. 它被禁用 当没有新内容时, 但保留用于您跳过的一个版本, 这样您仍然可以稍后安装它 。
- ** Update ** 按钮只显示何时可以从 Home Assistant 安装更新 。 有些更新只能读到。
- 对话框打开后释放向秘书处提供笔记, 并装上旋转器 。

## 在代码中 {#in-code}

视图为 `more-info-update` 在 [`src/dialogs/more-info/controls/more-info-update.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-update.ts) 。 备份选项是 `ha-more-info-update-backup` 在 [`src/dialogs/more-info/components/update/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs/more-info/components/update) 。 顶部的状态行为`state-card-update`在[`src/state-summary/`](https://github.com/home-assistant/frontend/tree/dev/src/state-summary)中. 像 `updateIsInstalling` 这样的 `UpdateEntityFeature` enum 和 elfers 在 [`src/data/update.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/update.ts) 中 。

来源:[`more-info-update.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/controls/more-info-update.ts)
