---
title: 动议
description: Home Assistant界面的动画持续时间标志,以及运动如何尊重那些要求更少的人.
order: 5
---

# 动议 {#motion}

动作帮助人们跟踪发生的情况:一个对话框在页面上打开,一个敬酒幻灯片在底部,一个控制器移动到它的新值. 谨慎使用,这解释了一个变化。 使用太多,会妨碍,对一些人来说,它使界面变得难以使用,甚至令人不快.

## 期限符号 {#duration-tokens}

动画使用其中的一个符号,定义在[`src/resources/theme/core.globals.ts`](https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/core.globals.ts)的前端:

- `--ha-animation-duration-instant`: 75 毫秒 。
- `--ha-animation-duration-fast`: 150毫秒( 150毫秒)
- `--ha-animation-duration-normal`: 250毫秒( X)
- `--ha-animation-duration-slow`: 350 毫秒
- `--ha-animation-duration-none` :1毫秒 。

We 没有, Web Super 组件使用相同的值: 它们的正常过渡是 `--ha-animation-duration-fast`, 它们的快速过渡是 `--ha-animation-duration-instant`.

## 减少动议 {#reduced-motion}

人们可以要求操作系统减少运动. 浏览器以 `prefers-reduced-motion: reduce` 传递 。 当设定时,前端将每个持续符设定为1毫秒. 任何缇定的标语 都会立即发生, 而不做任何事情。

一些组件更进一步关闭自己的动画,如对话框,底板,波纹,侧边栏,以及骨架加载器. 如果您的组件动画以某种方式不覆盖符号, 就像环动画一样, 为它添加一个 `@media (prefers-reduced-motion: reduce)` 块 。

在JavaScript中需要知道的代码,就像一个决定是否动画的图表一样,可以消耗`reducedMotionContext` Lit 语境.

## 准则 {#guidelines}

绮 这些都来自前端的造型指导,大部分是写给视图过渡的:

- 使用视图转换只为状态间有意义的连续性.
- 保持过渡简单。 细微的淡出和交叉面通常效果最好.
- 用 `--ha-animation-duration-fast` 、  我知道 `--ha-animation-duration-normal` 或 `--ha-animation-duration-slow` 计时它们 。
- 保持运动的微妙和象征性,尊重通过现有的全球运动减少的运动。

对于页面级别切换才能实现,前端通过`withViewTransition()`在[`src/common/util/view-transition.ts`](https://github.com/home-assistant/frontend/blob/dev/src/common/util/view-transition.ts)中的帮助者使用视图切换 API. [其次:](/frontend/architecture/theming)的页面覆盖代码侧.

## 相关 {#related}

- 我以为你会同意的?
- [旋转器](/design/components/spinner)和[的一种](/design/patterns/loading): 动说"请等等".
