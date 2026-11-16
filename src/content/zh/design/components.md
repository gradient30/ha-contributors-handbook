---
title: 组件
description: Home Assistant 界面的构建模块，每个组件在一页上提供指南、规格、可访问性和代码。
order: 20
sidebarGroups:
- 动作
- 输入
- 采摘者
- 表格
- 反馈与状态
- 显示数值
- 布局和内容
---


# 组件 {#components}
界面是由一组共享组件构建的。重复使用它们可以保持 Home Assistant 的一致性，并为每个人节省工作。在你设计或构建新内容之前，请先检查是否已有组件能够完成该任务。

这些页面上的示例都是来自前端的真实组件，正在运行中，显示应用的亮色或暗色主题。

## 组件页面的构建方式 {#how-a-component-page-is-built}
每个组件都有一个页面，供设计师和开发者使用。设计优先，代码最后，每个页面都遵循相同的顺序，这样你就知道该从哪里查看：1. **概述**：组件是什么，用一两句话说明。
2. **何时使用**：它的功能，以及何时使用其他组件更合适。
3. **结构**：其组成部分。
4. **变体**：它有哪些版本，以及何时选择哪一种。
5. **行为**：用户与它交互时的表现。
6. **规格**：尺寸、间距和颜色，使用 [设计标记](/design/foundations) 表示。
7. **指南**：如何正确使用，通常包含可做与不可做的示例。
8. **可访问性**：键盘操作、焦点、目标大小，以及屏幕阅读器的读出内容，最后提供角色和 ARIA 代码。
9. **相关内容**：与之搭配的组件和 [模式](/design/patterns) 。
10. **代码中**：元素、属性、插槽、事件，以及如何对其进行样式设置。开发人员可以直接跳到 **代码中**。设计人员可以在此之前停下。**无障碍性**部分的工作方式相同：首先介绍人们能获得的功能，如键盘支持、焦点、目标大小以及屏幕阅读器的朗读内容，然后是一个 **代码中** 的部分，包含其背后的角色和 ARIA 属性。

## 规范所在位置 {#where-the-spec-lives}
这些页面是 Home Assistant 组件的参考：它们的外观、行为以及何时使用。这些页面取代了 design.home-assistant.io。

要更改组件：

1. 在 [UX 设计讨论](https://github.com/OpenHomeFoundation/ux-design/discussions) 的 **设计系统** 分类下开始讨论，并在那里确定方向。
2. 在 [前端仓库](https://github.com/home-assistant/frontend) 中打开一个 pull request 来更改组件。
3. 在 [此网站](https://github.com/home-assistant/contributors.home-assistant.io) 打开一个 pull request 来更新组件的页面。

有关完整流程，请参见 [我们如何设计](/design/how-we-design#where-a-component-is-specified)。

## 动作 {#actions}
- [按钮](/design/components/button)：启动一个动作，例如保存表单或打开对话框。
- [进度按钮](/design/components/progress-button)：一个需要时间的动作，并显示结果如何。
- [下拉菜单](/design/components/dropdown)：一个位于按钮后面的动作或选项菜单。

## 输入 {#input}
- [文本输入](/design/components/input)：单行文本，例如名字、数字或密码。
- [多行文本框](/design/components/textarea)：可以输入多行的文本。
- [开关](/design/components/switch)：开启或关闭某个设置。
- [滑块](/design/components/slider)：通过拖动选择一个范围内的数字。
- [选择框](/design/components/select-box)：从几个选项中选择一个，选项以卡片形式并排显示。
- [颜色选择器](/design/components/color-picker)：在色轮上选择色相和饱和度，例如光的颜色。

## 选择器 {#pickers}
- [实体选择器](/design/components/entity-picker)：选择一个实体，可搜索。
- [设备选择器](/design/components/device-picker)：选择一个设备，可搜索。
- [区域选择器](/design/components/area-picker)：选择一个区域，或现场创建一个新区域。

## 表单 {#forms}
- [表单](/design/components/form)：一个完整的表单，根据模式渲染。
- [选择器](/design/components/selector)：用于某个值的合适控件，由集成、蓝图和表单使用。

## 反馈与状态 {#feedback-and-status}
- [警报](/design/components/alert)：页面上的简短重要信息。
- [对话框](/design/components/dialog)：当前屏幕顶部的决策或输入。
- [自适应对话框](/design/components/adaptive-dialog)：大屏幕上的对话框，手机上的底部弹出页。
- [徽章](/design/components/badge)：显示状态的小元素，呈胶囊形。
- [标签徽章](/design/components/label-badge)：经典的圆形状态徽章。
- [加载动画](/design/components/spinner)：正在加载的提示。
- [工具提示](/design/components/tooltip)：悬停或聚焦时的简短提示。
- [提示](/design/components/tip)：内容下方的简短可选提示，例如键盘快捷键。
- [状态图标](/design/components/state-icon)：实体的图标和颜色，基于其状态。

## 显示数值 {#showing-values}
- [条形图](/design/components/bar)：某物的使用量。
- [仪表盘](/design/components/gauge)：刻度盘上的单一数值。
- [控制装置](/design/components/controls)：用于操作设备的大型触控友好控件。
- [控制滑块](/design/components/control-scrubber)：在固定窗口下拖动条，用于循环范围，例如色相。
- [选择菜单](/design/components/select-menu)：一个紧凑的下拉菜单，用于选择一个选项，例如恒温器的模式。

## 布局和内容 {#layout-and-content}
- [列表](/design/components/list)：项目行。
- [展开面板](/design/components/expansion-panel)：需要时打开的部分。
- [滚动文本](/design/components/marquee-text)：一行文本，当文本不适合时滚动显示。
- [淡出](/design/components/faded)：长文本的开头，其余部分淡出，直到人们选择它。

## 更大的构建模块 {#bigger-building-blocks}
组件汇聚成界面中更大的部分，每个部分都有自己的章节：

- [仪表板](/design/dashboards)：人们放在仪表板上的卡片。
- [更多信息](/design/more-info)：当你选择一个实体时打开的对话框，以及每种类型的实体在其中的视图。

## 缺少内容吗？ {#missing-something}
并非前端的每个组件都在此页面上有介绍。缺少的页面本身就是一个很好的贡献：按照上面的提纲，向 [此网站](https://github.com/home-assistant/contributors.home-assistant.io) 打开一个 pull request。如果你认为某个组件需要修改，可以在 [UX 设计讨论](https://github.com/OpenHomeFoundation/ux-design/discussions) 的 **设计系统** 分类中发起讨论。开发者可以在前端的 [`src/components`](https://github.com/home-assistant/frontend/tree/dev/src/components) 中找到每个组件的代码，而 [前端](/frontend) 区域则说明了如何使用它。
