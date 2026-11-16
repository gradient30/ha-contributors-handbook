---
title: 旋转器
description: 旋转器显示某些内容正在加载或进行中，当你不知道它需要多长时间时。
sidebarGroup: 反馈与状态
---

# 旋转器 {#spinner}

Live 演示 `ha-spinner`。

```html
<ha-spinner></ha-spinner>
```

## 概述 {#overview}

当你不知道某个操作需要多长时间时（例如加载数据、连接设备或执行操作），使用旋转器显示正在加载或进行中。在结果将显示的地方显示它，让用户知道他们正在等待什么。

## 何时使用 {#when-to-use}

使用旋转器的情况：

- 等待持续时间未知的操作
- 整个页面、面板或卡片正在加载时

不要使用旋转器的情况：

- 从按钮启动的操作。此时应使用 [按钮](/design/components/button) 的 `loading` 状态，或使用 [进度按钮](/design/components/progress-button)。这样反馈会保持在用户选择的内容上。
- 针对已知最大值的进度。此时应使用 [进度条](/design/components/bar)。
- 加载失败时。应用 [警告](/design/components/alert) 替代旋转器，并说明错误原因。

## 解剖结构 {#anatomy}

1. **轨道**：指示器后面的完整圆圈
2. **指示器**：在轨道上增长、缩小并旋转的弧线

## 变体 {#variants}

### 尺寸 {#size}

有四种尺寸。选择适合它将要填充空间的尺寸：

- **微小**：16px
- **小**：28px
- **中等**：48px，默认
- **大**：68px

`ha-spinner` 的实时演示。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/components/spinner/)。

```html
<ha-spinner size="tiny"></ha-spinner>
<ha-spinner size="small"></ha-spinner>
<ha-spinner size="medium"></ha-spinner>
<ha-spinner size="large"></ha-spinner>
```

## 行为 {#behavior}

加载指示器只有一个状态：它会不断旋转，直到你将其移除。它没有悬停、聚焦或按下状态。整个加载指示器每3.5秒旋转一圈，而弧线每1.5秒增长和收缩一次。样式没有为减少动画的情况设置单独规则，因此当有人请求减少动画时，动画仍然按原样运行。

## 规格 {#specs}

| 尺寸 | 直径 | 令牌 |
| --- | --- | --- |
| 超小 | 16像素 | `--ha-spinner-size` |
| 小 | 28像素 | `--ha-spinner-size` |
| 中（默认） | 48像素 | `--ha-spinner-size` |
| 大 | 68像素 | `--ha-spinner-size` |

| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 轨道和指示器宽度 | 4像素 | 无 |
| 指示器颜色 | 主色 | `--primary-color`，通过 `--ha-spinner-indicator-color` |
| 轨道颜色 | 分隔线颜色 | `--divider-color`，通过 `--ha-spinner-divider-color` |
| 指示器端点 | 圆形 | 无 |
| 旋转 | 每圈3.5秒，线性 | 无 |
| 弧动画 | 1.5秒，缓入缓出 | 无 |

## 指南 {#guidelines}

按示例操作或避免的事项。

**可做:** 在启动的按钮上显示加载状态。

```html
<ha-button loading>Save</ha-button>
```

**不可做:** 在按钮旁放置一个单独的加载动画。

```html
<ha-button>Save</ha-button>
<ha-spinner size="small"></ha-spinner>
```

- 不要让加载动画无限运行。如果加载失败，用警示替代它。

## 无障碍性 {#accessibility}

### 键盘 {#keyboard}

加载动画不可聚焦，也没有键盘交互。

### 屏幕阅读器 {#screen-readers}

加载动画以名为“加载”的进度条形式被读取，没有具体数值，因为没有已知的进度。

### 代码中 {#in-the-code}

加载动画的角色是 `progressbar`，可访问名称为“加载”，取自 Web Awesome 的本地化，没有数值。

## 相关内容 {#related}

- [按钮](/design/components/button)：操作的 `loading` 状态
- [进度按钮](/design/components/progress-button)：显示其操作结果的按钮
- [条形](/design/components/bar)：与已知最大值的水平
- [警报](/design/components/alert)：加载失败时

## 在代码中 {#in-code}

该元素是 `<ha-spinner>`。它基于 [Web Awesome spinner](https://webawesome.com/docs/components/spinner/)。

```html
<ha-spinner></ha-spinner>
<ha-spinner size="small"></ha-spinner>
```

### 属性 {#attributes}

- `size`：`tiny`、`small`、`medium` 或 `large`。如果没有，它的大小为 48 像素，与 `medium` 相同。

### 样式 {#styling}

- `--ha-spinner-size`：大小，用于当没有适用的预设时。`size` 属性会为你设置此值。
- `--ha-spinner-indicator-color`：运动部分。默认值为 `var(--primary-color)`。
- `--ha-spinner-divider-color`：其后的轨道。默认值为 `var(--divider-color)`。

来源：[`src/components/ha-spinner.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-spinner.ts)
