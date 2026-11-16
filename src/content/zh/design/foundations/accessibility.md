---
title: 无障碍
description: 如何设计并构建人人都能使用的接口. 适用的WCAG要求,以及Home Assistant前端如何在实践中满足这些要求.
order: 4
---

# 无障碍 {#accessibility}

Home Assistant管理着人们的家 那些看到,听到,移动,思考 在许多不同的方式。 一些人使用屏幕阅读器,有些只使用键盘,有些手机带有大文本,有些墙板横跨房间. 无障碍是让界面对所有人都起作用的原因,它也是每个设计和每个pull request的一部分,而不是结尾的一个单独的步骤.

此页面使用 [网络内容无障碍准则(WCAG) 2.2](https://www.w3.org/TR/WCAG22/) 作为栏, 并显示前端是如何与之相遇的 。 每节分开两件事:

- **WCAG**:标准要求什么,加上成功标准的数量,这样你就可以查了. A级是最小的,AA是瞄准的,AAA更进一步.
- ** 在前端**: Home Assistant代码今天做什么,所以你的设计或代码可以以此为基础,而不是围绕它工作.

前端审查清单要求有一个可以让屏幕阅读器和键盘用户访问的UI,前端的造型指导要求保持WCAG AA对文本和基本UI负担的对比.

## 对比度 {#contrast}

** 妇女和儿童事务咨询小组**

- 文本相对于其背景需要至少4.5:1的对比比. 大文本,从18点(24 CSS像素),或用粗体表示的14点(约18.7 CSS像素),需要3:1(1.4.3 Contrast(最小),AA)
- 您需要看到的控件的部件, 如文本字段的边框或切换的拇指, 以及像图标这样的有意义的图形, 需要 3:1 。 (1.4.11 非文本对比,AA)
- 禁用控制和纯装饰免予使用.
- 颜色从来不是说出事情的唯一方法. 一个错误是红色的,它也说这是一个错误。 (1.4.1 颜色的使用,A)

** 前端**

颜色来自[颜色符号](/design/foundations/color)。 这些是通用文本和填充芦对的对比比,由默认光和暗主题的前端的符号值计算:

| 平对 | 光线 | 阴暗 |
| --- | --- | --- |
| `--primary-text-color` on `--card-background-color` | 18.42:1 | 13.03:1 |
| `--primary-text-color` on `--primary-background-color` | 17.65:1 | 14.44:1 |
| `--secondary-text-color` on `--card-background-color` | 6.48:1 | 6.13:1 |
| `--ha-color-text-link` on `--card-background-color` | 3.26:1 | 8.80:1 |
| {指出了 `--ha-color-fill-primary-loud-resting` 的白文本 | 3.26:1 | 3.26:1 |
| {指出了 `--ha-color-fill-danger-loud-resting` 的白文本 | 4.59:1 | 7.04:1 |
| {指出了 `--ha-color-fill-success-loud-resting` 的白文本 | 4.58:1 | 7.03:1 |
| {指出了 `--ha-color-fill-warning-loud-resting` 的白文本 | 2.21:1 | 7.00:1 |
| `--ha-color-on-primary-normal` on `--ha-color-fill-primary-normal-resting` | 2.85:1 | 7.42:1 |
| `--ha-color-on-danger-normal` on `--ha-color-fill-danger-normal-resting` | 5.61:1 | 5.56:1 |
| `--ha-color-focus` (焦点环有助于实现) `--card-background-color` | 2.88:1 | 5.91:1 |

将每对与上面的WCAG数字比较,然后用它来做新的东西. 静态或正常填充的文本使用匹配的 `on` 符号 : `--ha-color-on-danger-normal` 在 `--ha-color-fill-danger-normal-resting` 上, 而不是您喜欢的红色 。 一个没有在符号系统中的组合 完全没有相反的希望, 所以你自己检查,在两个主题。

[警报](/design/components/alert)是一个不只依靠颜色的好例子:每一种类型在颜色旁边都有自己的图标.

## 焦点 {#focus}

** 妇女和儿童事务咨询小组**

- 当您使用键盘时,您总是看到哪个元素有焦点. (2.4.7 焦点可见,AA)
- 焦点元素不是隐藏在别的东西后面,比如粘贴脚印或敬酒. (2.4.11 焦点不受干扰(最小),AA)
- 焦点以合理顺序移动. (2.4.3 重点顺序,A)
- 单靠专注不会引发变化,比如提交表格。 (3.2.1 焦点,A)
- 在AAA中,焦点指标至少是2个CSS像素厚度,焦点外观和无焦点外观有3:1的对比. (2.4.13 聚焦外观,AAA).

** 前端**

- 在Web Associate上构建的组件,如[按钮](/design/components/button),[文本输入](/design/components/input)和[切换](/design/components/switch),共享一个焦点环:2像素的固线,2像素远离元素,在`--ha-color-focus`中. 符号为`--wa-focus-ring-style`,`--wa-focus-ring-width`,`--wa-focus-ring-offset`和`--wa-focus-ring-color`.
- 大设备 [控件](/design/components/controls) 像控制按钮, 开关, 和滑动器一样, 在 `:focus-visible` 上画有框阴影的 2 像素环, 以控制器的颜色 。
- 焦点样式使用`:focus-visible`,因此环向键盘用户显示,并远离触摸和鼠标.
- 一个对话框在打开时会以 `autofocus` 属性将焦点移动到元素上 。 像[窗体](/design/components/form)这样的组件 将焦点传递到它们的第一个领域。
- 当检查一个表单而一个字段无效时,焦点移动到第一个有问题的字段.

切除焦点环时,千万不要置换可见的焦点环。

## 键盘 {#keyboard}

** 妇女和儿童事务咨询小组**

- 用指针可以做的一切,用键盘都可以做. (2.1.1 键盘,A)
- 专注永远不会被困在一个组件。 (2.1.2 无键盘陷阱, A)
- 单个字符的快捷键可以关闭或重新映射. (2.1.4 字符键快捷键, A)
- 内容显示在徘徊或焦点上,像工具提示一样,可以被删除,可以被自己徘徊,并停留到离开. (1.4.13 关于 " 重心 " 或 " 焦点 " 的内容,AA)

** 前端**

- 使用本地元素和 `ha-*` 组件而不是建立自己的控制 。 使用 `click` 听器的 有权享受键盘 。
- Pickers有一个完整的键盘模型:箭头键通过列表移动,<kbd>Home</kbd>和<kbd>end</kbd>跳到第一个和最后一个项目,<kbd>Page Up</kbd>和<kbd>Page Down</kbd>移动一个页面,和<kbd>Enter</kbd>选择. 焦点停留在搜索区域中,同时移动到列表中. 见[实体拾取器](/design/components/entity-picker).
- 兮 Home Assistant 拥有全局快捷键, 如 <kbd> e</kbd> 用于搜索实体 <kbd> Shift</kbd> + <kbd> ? </kbd> 用于快捷键列表 。 人们可以在他们简介中的**键盘快捷键**下将其关闭. 在代码中,快捷键会通过`ShortcutManager`,在输入字段时忽略它们。
- [工具](/design/components/tooltip)在悬浮和焦点上显示,所以键盘用户得到相同的提示.

## 标签和可访问名称 {#labels-and-accessible-names}

** 妇女和儿童事务咨询小组**

- 每个控制器都有一个能够读取辅助技术的名称,并暴露其作用和状态,如"switch, on". (4.1.2 名称、作用、价值,A)
- 受制于一个显著的标签或说明。受制于第3条第1款(a)项。
- 当一个控制有可见文本时,其可访问的名称包含该文本,因此使用语音控制的人可以说出他们看到的. (2.5.3 标签名称,A)
- 您所看到的结构, 如标题和列表, 也在标记中 。 (1.3.1 信息和关系,A)

** 前端**

- 给每个字段 `label` 。 [文本输入](/design/components/input), [文本区域](/design/components/textarea) 和 [窗体](/design/components/form) 之后才成为真正的标签 。 占位符不是标签:一旦有人打字就消失.
- 一个图标按钮没有可见的文本,所以其`label`是唯一的名称. `ha-icon-button` 使用它作为可访问的名称和工具提示,并将图标本身隐藏在屏幕阅读器中.
- 需要的字段显示标签后的 `*` 。 帮助文本坐落在字段下方.
- 对话框需要一个标题 。 `ha-dialog` 使用它的`header-title` 作为对话框的可访问名称 。 当标题是一个槽中自定义内容时, 设置 `accessibleLabel` 代替 。
- 所有可见文本,包括无障碍名称,都要通过翻译系统. 见[用户界面文本](/design/ui-text).

## 目标规模 {#target-size}

** 妇女和儿童事务咨询小组**

- 指针目标至少是24乘以24 CSS像素,或者周围有足够的空间让每个周围一个24像素圆圈不与另一个相重叠. (2.5.8 目标大小(最小),AA)
- 在AAA,目标至少44乘44 CSS像素. (2.5.5 目标大小(加强),AAA)

** 前端**

- [按钮](/design/components/button) 默认高40 像素 。 大小从 `xs` 到 24 像素, 到 `s` 到 `l` 到 48 。
- 图标按钮默认为48乘48像素.
- 前端评论准则要求互动区域足够大,可以触摸,因此将24像素作为地板,而不是目标.

## 动议 {#motion}

** 妇女和儿童事务咨询小组**

- 任何移动,眨眼,或自行滚动超过5秒的,都可以暂停,停止,或隐藏. (2.2.2 暂停、停止、隐藏、A)
- 在AAA,由相互作用引发的运动可以关闭,除非是必需的. (2.3.3 互动动画,AAA)

** 前端**

朔方在操作系统要求减少运动(`prefers-reduced-motion: reduce`)时,前端将所有动画持续时间符号设置为1毫秒. 对话框,骨架加载器,波纹,侧边栏,以及数张卡片也关闭了自己的动画. 使用时间符号和运动随即免费设置。 见[动议](/design/foundations/motion).

## 屏幕阅读器和状态信息 {#screen-readers-and-status-messages}

** 妇女和儿童事务咨询小组**

- 关于状态变化的信息,如"拯救"或错误,可以到达屏幕阅读器用户,而不移动他们的焦点. 没事
- 在文字中,一个错误说出哪个字段是错的,什么是错的. (3.3.1 错误识别,A)
- 当定律已知时,错误就暗示它. (3.3.3 错误建议,AA)

** 前端**

- 一个[警报](/design/components/alert)有`role="alert"`。 大多数屏幕阅读器一出现就立即宣布警报. 在加载时通常不宣布已经在页面上的提醒,所以不要依赖它来获取人们必须听到的东西.
- 敬酒,屏幕下方的短信息,有`role="status"`,并以礼貌所遇到的方式宣布,没有打扰.
- 当 [文本输入](/design/components/input) 无效时, 它会设置 `aria-invalid` , 而它的验证信件会取代帮助者文本并被宣布 。
- [旋转器](/design/components/spinner)建在Web Supersome spinner上,其作用是进步栏和翻译的"Loading"标签.

## 检查你的工作 {#check-your-work}

在共享设计或打开 pull request 之前 :

1. 只用键盘使用. 你能到达一切, 看到焦点在哪里, 然后再次离开吗?
2. 请检查每个新颜色对的对比度, 光和暗.
3. 橘子 开动操作系统中的减动, 并检查没有什么重要 取决于动画。
4. 用屏幕阅读器试试,比如VoiceOver,TalkBack,或者NVDA. 每个控制者都说它是什么?
5. 将浏览器缩放到200%,然后在手机上尝试.

## 相关 {#related}

- [的结论](/design/foundations/color): 对比表后面的符号 。
- [踌咕鹫衲ỡ turkey荚咀玄](/design/patterns):表单、错误和加载,以及它们的无障碍细节。
- [UX设计讨论](https://github.com/OpenHomeFoundation/ux-design/discussions) 的 ** 可获取性 ** 类别, 和 `Accessibility` 标签 [前端仓库](https://github.com/home-assistant/frontend/labels/Accessibility) 。
