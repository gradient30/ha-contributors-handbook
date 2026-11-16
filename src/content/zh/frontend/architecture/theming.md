---
title: 设计符号
description: 前端每个نأ的颜色,大小和空间背后的CSS变量,以及用户主题如何改变它们.
order: 5
---

# 设计符号 {#theming-and-design-tokens}

前端的每个颜色,间隔,半径,和字体都来自CSS自定义属性. 这就是使得主题成为可能的原因:一个主题改变变量,整个界面随之而来. 这也是为什么组件从来不用硬编码一个颜色的原因.

## 设计符号 {#design-tokens}

基变量为[设计符号](/glossary/design-token),均以`--ha-`开头. 它们的定义在{L通过关于}:

| 文件 | 键 |
| --- | --- |
| `core.globals.ts` | 固然需要时间间隔(`--ha-space-1`至`--ha-space-20`,步数为4像素),半径(`--ha-border-radius-*`),边框宽度和动画持续时间(`--ha-animation-duration-*`) |
| `typography.globals.ts` | 字体家族、大小、重量和行高(`--ha-font-*`) |
| `color/core.globals.ts` | 颜色调色板, 如 `--ha-color-primary-40` |
| `color/semantic.globals.ts` | 按目的排列的颜色, 如  我们对 `--ha-color-text-primary` 、 `--ha-color-fill-danger-loud-resting` 或 `--ha-color-border-neutral-quiet` |

使用组件中的语义色彩符号,而不是调色板. 一个语义符号说颜色是用来做什么的,这样它就可以随着主题和暗模式而改变,而不知道组件.

设计区域 [基金会](/design/foundations) 区域显示每个符号, 其值为 [颜色](/design/foundations/color), [打印](/design/foundations/typography) 和 [间距](/design/foundations/spacing) 。

## 主题变量 {#theme-variables}

没有`--ha-` 前缀的旧变量,如`--primary-color`,`--primary-text-color`和`--card-background-color`,仍然在任何地方. 它们被定义在[`src/resources/theme/color/color.globals.ts`](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/color/color.globals.ts)中,大多在符号之上,它们就是大多数用户的主题设置. 当你改变一个使用它们的组件时,保持它们的工作. [主题变量](/marketplace/reference/theme-variables)在 Marketplace 区域列出它们作为主题作者,以及用于主题的组件变量.

Web Super 组件有自己的变量, 如 `--wa-color-brand-fill-loud` 。 [`src/resources/theme/color/wa.globals.ts`](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/color/wa.globals.ts) 将那些映射到 Home Assistant 符号, 所以 `ha-*` 包装符也跟着主题 。

## '在组件中使用' {#use-them-in-a-component}

```ts
static styles = css`
  :host {
    display: block;
    padding: var(--ha-space-4);
    gap: var(--ha-space-2);
    color: var(--primary-text-color);
    background-color: var(--card-background-color);
    border-radius: var(--ha-border-radius-lg);
  }
`;
```

## 主题的适用情况 {#how-themes-apply}

A [主题](/glossary/theme) 是一组带有数值的变量 。  页的用户通过核心的 `frontend` 集成 `frontend` 集成 的 `frontend` 集成 的 `frontend` , 或安装它们, 并选取其配置配置的 之一 。 一个主题可以在 `modes` 下对光和暗模式有单独的值.

`applyThemesOnElement()` [`src/common/dom/apply_themes_on_element.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/dom/apply_themes_on_element.ts) [`src/common/dom/apply_themes_on_element.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/dom/apply_themes_on_element.ts) { } { { { { { { } { { { { { { { { { { { { { { { , { { { { { { { { { { { { } { { { { { { { } { { { { { { { } { { { { } { { { { { { } { { { } { { { } { { { { } { { { { } { } \ \ \ \ \ 上一个 的 主题的变量。 根元素将选定的主题应用到整个app中. 卡片从自己的`theme`选项将主题应用到只使用卡片. 当一个主题有暗模式值时,当暗模式打开时,这些值会被应用在顶部.

对于默认主题,用户可以在配置中选择自己的主色和重音颜色. 然后前端从那个颜色中计算出主调色板和匹配的文本颜色.

## 右对左 {#right-to-left}

有些语言是从右到左书写. 前端为它们翻转布局. 使用逻辑 CSS 属性, 如 `margin-inline-start` 和 `padding-inline-end` , 因此您的组件会向上翻转 。 用右到左语言检查您的更改, 或用 过去 [画廊](/frontend/development/gallery-and-demo) 中的右到左切换 。
