---
title: 酒吧
description: 条形图显示某物被使用的程度，以水平轨道上填充的份额表示。
sidebarGroup: 显示数值
sidebarGroup: 数值展示

---


# 酒吧 {#bar}
Live demo of `ha-bar`.

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](/design/components/bar)。

```html
<ha-bar value="42"></ha-bar>
```

## 概述 {#overview}
条形图显示相对于已知最大值的水平，通过水平轨道上的填充部分表示。它在设置行和列表中表现良好，可与其对应的数字放在一起显示。

## 使用场景 {#when-to-use}
使用条形图表示：

- 相对于已知最大值的等级，例如应用程序的 CPU 或内存使用情况
- 某物的填充程度，例如磁盘空间

不要使用条形图表示：

- 显示某物正在加载，但未知百分比时。使用 [旋转指示器](/design/components/spinner)
- 仪表板上的传感器值。使用 [仪表](/design/components/gauge)

## 构成 {#anatomy}
1. **轨道**：整个宽度的背景，代表完整范围
2. **填充**：轨道中表示数值的部分，从轨道的起始位置开始

## 变体 {#variants}
该条形图本身没有变体。要显示警告和严重等级，请在值超过阈值时更改填充颜色，以便问题突出显示。前端在超过第一个阈值时将填充切换为警告颜色，超过第二个阈值时切换为错误颜色。选择适合数据的阈值：系统指标在 50% 和 85% 时切换，磁盘使用率在 85% 和 95% 时切换。低于第一个阈值时，两者都使用成功颜色。

`ha-bar` 的实时演示。

```html
<ha-bar value="35"></ha-bar>
<ha-bar value="70" style="--ha-bar-primary-color: var(--warning-color)"></ha-bar>
<ha-bar value="92" style="--ha-bar-primary-color: var(--error-color)"></ha-bar>
```

## 行为 {#behavior}
- 该条形条不具备交互性。没有悬停、聚焦、按下或禁用状态。
- 填充表示值在最小值到最大值范围内的占比，保留一位小数。超出范围的值会被限制，因此填充永远不会超过轨道的两端。
- 条形条占据其容器的全部宽度。

## 规格 {#specs}
| 属性 | 值 | 变量 |
| --- | --- | --- |
| 高度 | 12px | 无 |
| 宽度 | 容器的 100% | 无 |
| 圆角半径 | 4px | `--ha-border-radius-sm`，通过 `--ha-bar-border-radius` |
| 轨道颜色 | 浅色主题下为 `#e5e5e5`，深色主题下为 `#282828` | `--secondary-background-color`，通过 `--ha-bar-background-color` |
| 填充颜色 | 主要颜色 | `--primary-color`，通过 `--ha-bar-primary-color` |

## 指南 {#guidelines}
仅仅显示一个条形是不精确的。始终在旁边标注数值，比如 **42 %**，或者用一句话说明，如 **已使用 64 GB 中的 12 GB**。

实际演示中的做与不做。

**做：** 在条形旁显示数字。

```html
<span>42 %</span>
<ha-bar value="42" style="display: block; width: 100%"></ha-bar>
```

**不做：** 显示条形但没有数值。

```html
<ha-bar value="42" style="display: block; width: 100%"></ha-bar>
```

## 可访问性 {#accessibility}
### 键盘 {#keyboard}
该条形图不会获得焦点，也没有键盘交互。

### 屏幕阅读器 {#screen-readers}
屏幕阅读器无法从条形图中获取任何信息，因此旁边的数值是它们了解水平的唯一方式。颜色本身也无法告诉任何人数值处于警告或严重范围内。旁边的数字能够。

### 在代码中 {#in-the-code}
该条形图是一个没有角色、标签或辅助技术值的 SVG。

## 相关 {#related}
- [仪表](/design/components/gauge)：仪表盘上的一个数值
- [加载旋转器](/design/components/spinner)：表示某些内容正在加载
- [颜色](/design/foundations/color)：警告和错误颜色

## 在代码中 {#in-code}
该元素是 `<ha-bar>`。它占据其容器的全宽。

```html
<ha-bar value="42"></ha-bar>
<ha-bar min="-10" max="40" value="21"></ha-bar>
```

### 属性 {#attributes}
- `value`：当前值。超出范围的值会被限制。
- `min`：范围的起始值。默认值为 `0`。
- `max`：范围的结束值。默认值为 `100`。

### 样式 {#styling}
- `--ha-bar-primary-color`：填充部分。默认值为 `var(--primary-color)`。
- `--ha-bar-background-color`：轨道。默认值为 `var(--secondary-background-color)`。
- `--ha-bar-border-radius`：圆角半径。默认值为 `var(--ha-border-radius-sm)`。

高度固定为 12 像素。

来源：[`src/components/ha-bar.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-bar.ts)
