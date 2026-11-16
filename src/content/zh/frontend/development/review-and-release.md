---
title: 审查和发布
description: 前端 pull request 打开后会发生什么, 合并的改变如何使用 Home Assistant 到达人们。
order: 8
---

# 审查和发布 {#review-and-release}

打开 pull request 是对话的开始,而不是你的工作的结束。 本页面解释审查者看什么,检查运行,以及您的更改是如何在发布中结束的.

## 审查前 {#before-review}

当您打开 pull request 对 {H0躬 } 时会自动发生一些事情 :

- ** 模板检查。 ** pull request必须使用[以用用为为的用用为的用为为的用用为的用用为的用用为的用用为的用用用为的用用用的用用用的用用用的用用的用用用的用用用的用用用的用用的用用的用用的用用用用的用用的用用的用用的用用用用的用用用的用的用用的用用的的用用的用用的用的用用用的的的用用的的的用用用用用的的的用用的的的用用用用的的用用的用用的用的用的用用的用用用用的的用的用用的用用用用的用的用的的用用用用的的用用用的用的的用的用的用的用用的用用的用的用用的用的用的用的用用的用的用的的用的用用用的的的的用用的用的的的用用的的用用用的的用用用用的用的的用的的](https://github.com/home-assistant/frontend/blob/dev/.github/PULL_REQUEST_TEMPLATE.md),并保留其** 建议更改**、** 类型更改**和**检查清单**各节,准确检查一个**类型更改**,并在** 提议更改** 下说明更改。 如果没有,则pull request得到`Needs Template`标签和注释,检查失败,直到修复为止. 草稿被跳过, 所以当您在 pull request 标记时检查会运行 。
- ** 标签。 ** 一个bot通过它改变的文件来标记pull request,比如`Dashboards`,`Automations`,或`Tests: Unit`. 第二个脚本会在更改触及代码的这些部分时,甚至从文件夹外添加`Companion App`,`Home Assistant Link`,`Labs`和`Supervisor`. 两者在不再匹配时都会再次移除一个标签,同样是手工添加的标签. 规则在[`.github/labeler.yml`](https://github.com/home-assistant/frontend/blob/dev/.github/labeler.yml)和[`.github/scripts/label-content.mts`](https://github.com/home-assistant/frontend/blob/dev/.github/scripts/label-content.mts)中.
- ** 加州大学。 ** 你第一次缴款时 有个机器人要你签署缴款许可协议
- 页:1 林特斯,型号检查,以及各单元测试,一个生产建设,每推一次都进行端对端测试. 在您的 pull request 合并之前, 它们需要通过 。

保留一个 pull request 到一个更改 。 如果你发现自己 检查两个**Type 变化**框, 拆分它。 小的 pull request 得到更快的审查。

## 什么样的审查者看 {#what-reviewers-look-at}

前端维护者审查每个 pull request 。 除了"有用",他们检查:

- ** 各州的行为。 ** 装入,错误,不可用,缺少的实体,以及双向过渡. 不只是快乐的道路。
- ** 现有模式。 ** 共享 `ha-*` 组件、 已有的帮助和主题变量, 而不是并行执行 。
- ** 案文。 ** 所有用户化的文本都是可变的,在句子中,使用正确的术语.
- ** 可获取性。 ** 键盘导航,焦点,标签,和触摸目标.
- ** 窄屏幕和右到左语言。 ** 前端使用电话,并使用从右到左写的语言.
- ** 清除。 ** 当包括与某个组件分离怯场时,活动收听器,计时器和订阅器会被删除.

[编码准则](/frontend/development/guidelines)更详细地涵盖这些内容。

### 截图和设计画廊 {#screenshots-and-the-design-gallery}

任何可见的更改,请在截图或短视频之前和之后添加到pull request. 审者从中判断甚多.

更改一个在画廊中有页面的组件,也应更新该页面。 维护者可以添加 `needs design preview` 标签, 它为您的 pull request 配置了画廊的预览 。 已公布的设计指南生活在此站点的[设计](/design/components)区域:当组件在那里有页面时,用pull request更新到[这个网站](https://github.com/home-assistant/contributors.home-assistant.io).

### 需要设计输入的更改 {#changes-that-need-design-input}

新的卡片,徽章,屏幕,以及互动模式,与代码一样是设计决定. 当方向未确定时,审查者会添加`Needs UX`标签,并要求设计团队投入. 这需要一段时间。 在 [UX设计讨论](https://github.com/OpenHomeFoundation/ux-design/discussions) 中讨论一个更大的想法, 在您写代码之前会保存您重写 。 [设计](/design/how-we-design)区域解释它是如何工作的。

### 需要后端的更改 {#changes-that-need-the-backend}

当您的更改取决于 Core 中的 pull request 时, 请在模板中链接它 。 前端更改等待后端更改合并. 标签为 `wait for backend` 和 `backend merged` 。

### 把请求调静 {#pull-requests-that-go-quiet}

一个 pull request 在90天里没有任何活动 得到 `stale` 标签和评论 。 若后七日无事,即闭. 任何更新都会再次删除标签 。 维护者可以用 `no-stale` 标签豁免 pull request 。 问题遵循相同的时间,但被标注为特征请求或需要帮助的问题除外。

## AI 工具 {#ai-tools}

你可以使用AI工具帮助你写代码. 你对结果负责:你必须理解你提交的每一项变化,并能自己解释。 拖动请求或评论, 看起来像未经审查的 AI 输出关闭 。 [Open Home Foundation AI 政策](https://github.com/home-assistant/frontend/blob/dev/AI_POLICY.md)有细节。

## 帮助审查 {#help-review}

pull request 模板要求您审查另外两个 pull request 。 这不是一种形式。 每一次评论,甚至"我用手机测试了这个,它起作用了",减轻了维护者身上的负荷,缩短了自己pull request的队列.

## 从合并到发行 {#from-merge-to-release}

前端作为 Python 软件包, `home-assistant-frontend` 发布, 而 Home Assistant Core 安装为 `frontend` 集成的要求 。 版本为日期,如`20260930.0`.

1. ** 输入 `dev`。 ** 你的零钱在下一次发行。 每天晚上都会用`dev`做一个开发建筑。
2. ** 贝塔。 ** 当新 Home Assistant 的 beta 开始发行时, `dev` 的更改会转到 `rc` 分支, 发行候选人 。 一个新的前端版本被剪切并贴上标签,而Core将它的要求撞向它.
3. (单位:千美元) β中或之后的补丁释放中需要的bug修复,由维护者将樱桃选择到`rc`上,并在那里发布和标记为`.1`,`.2`等. 那些pull request的标签是`cherry-picked`
4. ** 释放。 ** 在发布日,`rc`被合并为`master`,而您的变更船与下一个Home Assistant发布.

[发布](/releases)区域解释Home Assistant的释放周期整体.

### 文档和向后兼容的变化 {#documentation-and-backward-incompatible-changes}

如果您的更改添加或更改了用户配置的东西,请更新[Home Assistant.io](https://github.com/home-assistant/home-assistant.io)上的用户文档,并在模板中链接到pull request。 解释一下

如果您的更改为已有的用户打破了某些内容, 如已删除的卡选项, 请填写模板中的 ** Breaking 更改 ** 部分 。 该文本进入了发行笔记中,所以写给用户:什么中断,如何修复,以及为什么.
