---
title: 版式
description: 页面的内容可以达到多大的宽度,并且从屏幕边缘保留了多少空间.
order: 3.5
source: https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/core.globals.ts
lastVerified: 2026-11-02
---

# 版式 {#layout}

2026-11-02最后一次核实,对https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/core.globals.ts.

Home Assistant中的每一页都有其内容的最大宽度,以及内容和屏幕边缘之间的空间. 当每个页面选择自己的值时,在页面之间移动感觉不均匀. 因此,设置、配置和市场页面有三个内容宽度和一个沟槽。 界面的某些部分尚未覆盖. 它们列于本页末尾。

## 内容宽度 {#content-widths}

选择符合您页面内容的宽度 。 宽度是故意宽大的:在桌面屏幕上,它们会同时显示更多.

| 宽度 | 键 | 最大宽度 | 用它 Is it for |
| --- | --- | --- | --- |
| 窄 | `--ha-content-width-narrow` | 720px | 单列卡片或窗体,如设置区块,配置文件,备份,以及像Z-Wave或Zigbee这样的集成页面 |
| 宽 | `--ha-content-width-wide` | 1280px | 网格卡片,或两列并列,如设备、面积和集成页 |
| 满旨在使 | 无 | 100% | 使用它获得的所有空间的内容, 如数据表、日志、历史、地图、日历和能量 |

最大宽度是内容本身的宽度 。 沟渠来其上.

### 选择页面宽度 {#pick-a-width-for-your-page}

- 您的页面是设置、 牌或窗体的一列: 使用狭义 。
- 我们在你的页面上显示一个牌的网格, 或两列相邻: 宽度 。
- 您的页面是表格、 图表、 地图或日志: 使用全宽度, 不要设置最大宽度 。

宽度的狭长一页看似拉长:行会长,眼睛必须从标签到开关都要远行. 如果你的单列感到在 720px 抽筋, 这是值得讨论的,而不是自定义的宽度。

## 盖特 {#gutter}

沟槽是屏幕内容与左右边缘之间的空间. 在每个屏幕大小上使用`--ha-content-gutter`(16px). 在大屏幕上,最大宽度已经使内容远离边缘. 当屏幕比内容更窄时,沟就很重要.

电话稠密区域,如圆角或圆角,你不会在水沟里加上安全区域。 页面布局 `hass-subpage` 和 `hass-tabs-subpage` 已将其内容保留在安全区域内 。

600px恪之后 马牌的设置仪表板和系统导航页让他们的牌从边缘到边缘运行,没有圆角. 用于仅是其它页面链接列表的页面。 连接页是一个例外:它在这些宽度之前有边对边卡,并保存它们. 其他的页保留着沟渠。

## 示例 {#example}

```css
.content {
  max-width: var(--ha-content-width-narrow);
  margin: 0 auto;
  padding: var(--ha-space-7) var(--ha-content-gutter) 0;
}
```

## 尚未覆盖 {#not-covered-yet}

断点,对话框,仪表板,以及自动化和脚本编辑器尚不是这些宽度的一部分.
