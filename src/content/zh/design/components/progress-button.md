---
title: 进度按钮
description: 一个显示其操作正在运行，然后显示其是否成功的按钮。
sidebarGroup: 动作
---

# 进度按钮 {#progress-button}

Live 演示 `ha-progress-button`。

```html
<ha-progress-button>Restart</ha-progress-button>
<ha-progress-button progress>Restart</ha-progress-button>
```

## 概述 {#overview}

进度按钮是一种用于需要一些时间并在原地完成的操作的[按钮](/design/components/button)：保存设置、运行测试、调用操作。当操作运行时，它会显示一个旋转图标。完成后，会在绿色按钮上短暂显示一个勾号，或在红色按钮上显示警告图标。两秒后，它会恢复到正常状态。

## 使用时机 {#when-to-use}

进度按钮适用于：

- 需要一些时间且结果无处显示的操作，如 **测试连接** 或 **重启**

不适用于进度按钮的场景：

- 打开对话框或跳转到其他页面的操作。普通的[按钮](/design/components/button)即可。
- 显示用户需要阅读的错误。红色闪烁表示失败，但不说明原因。错误信息应同时显示，例如在[警告](/design/components/alert)中。

## 解剖结构 {#anatomy}

一个进度按钮是一个普通按钮，但多了一层额外功能：

1. **按钮**：普通按钮，包括它的容器、可选图标和标签
2. **加载动画**：在操作进行时替换标签
3. **结果图标**：操作完成后显示在按钮上，成功时为勾选标志，出错时为警告图标

## 变体 {#variants}

进度按钮具有与普通按钮相同的外观、变体和尺寸，因此可以与普通按钮并排放置。在进行进度和显示结果时，它会切换到强调外观。

`ha-progress-button` 的实时演示。

> 本页含交互式演示，阅读器中保留示例标记。完整可操作演示请看[官网原文](https://contributors.home-assistant.io/design/components/progress-button/)。

```html
<ha-progress-button appearance="filled">Test</ha-progress-button>
<ha-progress-button appearance="plain">Skip</ha-progress-button>
<ha-progress-button variant="danger">Delete</ha-progress-button>
<ha-progress-button size="s">Check</ha-progress-button>
```

## 行为 {#behavior}

- **静止**：看起来和表现就像一个普通按钮，具有相同的外观、变体和大小。
- **进行中**：按钮切换到强调颜色外观，并显示一个旋转图标代替文字标签。它会忽略指针输入，因此用户无法重复触发操作。
- **成功**：按钮变为成功变体，白色勾号覆盖半透明标签，持续两秒。
- **错误**：按钮变为危险变体，白色警告图标覆盖半透明标签，持续两秒。
- **禁用**：像普通的禁用按钮。

成功和错误状态只能通过代码触发，因此此处不显示。

悬停、聚焦和按下状态与[按钮](/design/components/button#behavior)相同。

## 规格 {#specs}

尺寸、间距和颜色与 [button](/design/components/button#specs) 相同。在此基础上：

| 属性 | 值 | 令牌 |
| --- | --- | --- |
| 进度和结果期间的外观 | 主色 | 无 |
| 成功时的变体 | 成功 | `--ha-color-fill-success-loud-resting` |
| 错误时的变体 | 危险 | `--ha-color-fill-danger-loud-resting` |
| 结果图标颜色 | 白色 | `--white-color` |
| 结果图标尺寸 | 24px | 无 |
| 超小和小号图标尺寸 | 16px | `--mdc-icon-size` |
| 结果持续时间 | 2 秒 | 无 |

## 指南 {#guidelines}

作为实时演示的做与不做。

**做：** 说明点击按钮会发生什么。

```html
<ha-progress-button>Test connection</ha-progress-button>
```

**不做：** 使用可能意味着任何东西的标签。

```html
<ha-progress-button>OK</ha-progress-button>
```

- 保持标签简短，并说明动作的结果：**保存**、**重启**、**测试连接**。参见 [用户界面文本](/design/ui-text)。
- 当操作可能因错误而失败并且用户需要阅读时，也要显示该错误，例如在 [警示](/design/components/alert) 中。

## 无障碍性 {#accessibility}

### 键盘操作 {#keyboard}

| 键 | 操作 |
| --- | --- |
| <kbd>Tab</kbd> | 将焦点移动到按钮上或离开按钮。禁用的按钮会被跳过。 |
| <kbd>Enter</kbd> 或 <kbd>Space</kbd> | 选择按钮。在显示进度时无操作。 |

### 目标大小 {#target-size}

与[按钮](/design/components/button#target-size)相同：默认大小下高度为40px。

### 屏幕阅读器 {#screen-readers}

按钮会用其标签进行宣布，即使结果已显示。在进度期间会宣布为忙碌状态。成功和错误状态只改变外观：不会有语音提示，因此需要显示的错误内容也应以文本形式提供。

### 代码中 {#in-the-code}

- 角色是`button`，来自内部的`<ha-button>`。
- 当结果图标显示时，标签会淡出而不是隐藏，因此按钮保持可访问名称。
- 在进度期间，内部按钮具有`aria-busy="true"`。

## 相关 {#related}

- [按钮](/design/components/button)：这个包裹的常规按钮
- [加载动画](/design/components/spinner)：独立显示进度
- [警报](/design/components/alert)：显示用户需要阅读的错误

## 代码示例 {#in-code}

该元素是 `<ha-progress-button>`。它包含 `<ha-button>`。在操作运行时设置 `progress`，操作完成后调用 `actionSuccess()` 或 `actionError()`：

```html
<ha-progress-button>Restart</ha-progress-button>
```

```ts
private async _restart(ev) {
  const button = ev.currentTarget;
  button.progress = true;
  try {
    await doTheThing();
    button.actionSuccess();
  } catch (err) {
    button.actionError();
  } finally {
    button.progress = false;
  }
}
```

在 `progress` 被设置时，按钮会忽略指针输入，因此用户无法重复启动该操作。

### 属性 {#attributes}

- `progress`：显示加载指示器。会作为属性反映。
- `disabled`：禁用按钮。
- `appearance`：`accent`（默认）、`filled`、`outlined` 或 `plain`。
- `variant`：`brand`（默认）、`neutral`、`success`、`warning` 或 `danger`。
- `size`：`xs`、`s`、`m`（默认）、`l` 或 `xl`。
- `label`：标签，当默认插槽为空时使用。

这些只能作为属性设置：

- `iconPath`：标签前的图标 SVG 路径数据。

### 插槽 {#slots}

- 默认：标签。

### 方法 {#methods}

- `actionSuccess()`：显示成功状态两秒。
- `actionError()`：显示错误状态两秒。

来源：[`src/components/buttons/ha-progress-button.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/buttons/ha-progress-button.ts)
