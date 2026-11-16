---
title: 您的第一个前端贡献
description: 设置前端, 运行到 Home Assistant ễ , 请稍作修改, 然后打开您的第一个 pull request 。
order: 1
sidebarLabel: 你的第一次贡献
---

# 您的第一个前端贡献 {#your-first-frontend-contribution}

进入前端的最快速的方法是一个小的,可见的固定:一个错位的图标,一个被切断的标签,一个在移动上无所作为的按钮. 在您保存的那一刻,您可以看到浏览器中的结果,一个评论员可以从截图中判断.

## 寻找工作 {#1-find-something-to-work-on}

在前端寄存器中浏览[标签 `good first issue`](https://github.com/home-assistant/frontend/labels/good%20first%20issue),或[打开错误](https://github.com/home-assistant/frontend/issues). 你碰到的虫子是第一个很好的话题 因为你已经知道如何复制它了

留下你正在研究的评语,所以没有人同时接听.

> [!TIP]
> 要不要换张新牌? 这不需要以下任何步骤。 以 [自定义卡片及其他](/frontend/custom-ui) 开始, 并在 [市场](/marketplace) 中发布 : 这就是项目推荐新牌开始的地方 。

## 2.  设置环境 {#2-set-up-the-environment}

最简单的设置是Visual Studio Code与前端寄存器的Devcontainer. 它为你安装了正确的节点和pnpm.

1. [前端仓库叉](https://github.com/home-assistant/frontend/fork) on GitHub.
2. 切开你的叉子 用视觉工作室代码打开
3. 当Visual Studio代码询问时,选择**在容器中重新打开**. 第一个开始需要几分钟时间,而依赖性安装。

喜欢工作 没有容器? 二者皆盖.

## 秃头! {#3-run-it}

你需要一个 Home Assistant 的例子来说话 。 在除尘器内部,您可以在前端运行一个:

1. 打开终端开始 Home Assistant Core. 第一次运行安装了 Core 的 `dev` 分支, 并创建带有演示实体的配置 :

```shell
   script/core
   ```

2. 打开第二个终端并启动前端开发服务器 :

```shell
   pnpm dev
   ```

3. 等待 `Build done`,然后在您的计算机上打开 `http://localhost:8124` 并创建一个用户 。

家里已经有Home Assistant了吗? 也可以将开发前端指向这个. [运行前端](/frontend/development/run)解释两种方式。

## 做你的零钱 {#4-make-your-change}

创建分支, 进行更改, 并保存 页 次 。 开发服务器重建,一个更新的浏览器会 页出结果.

几件事审查者寻找, 即使在一个小的固定:

- 人们看到的所有文字都来自[`src/translations/en.json`](https://github.com/home-assistant/frontend/blob/dev/src/translations/en.json),从未在代码中硬码.
- 使用现有的`ha-*`组件和主题变量,而不是新的颜色或一次性控制。
- 检查您在窄屏幕和黑暗主题上的变化 。

[编码准则](/frontend/development/guidelines)有细节。

## 检查你的工作 {#5-check-your-work}

在您推前先运行插件和单元测试:

```shell
pnpm lint
pnpm test
```

一个承诺前的钩子已经格式化了您承诺的文件,所以大多数样式问题都会自行解决.

## 6.  打开 pull request {#6-open-a-pull-request}

将您的分支推向叉子并打开一个 pull request 对准 `dev` 分支 。 完全填写pull request模板:从使用它的人的角度来描述变化,检查准确的** 类型变化**,并在截图之前和之后添加任何视觉内容. 当模板缺失或不完整时,检查失败 pull request 。 有细节

那就等着问题吧 评论家可能会要求你改变事情 这是正常的 解释接下来会发生什么。

## 接下来是什么 {#what-is-next}

- 读 [结构概览](/frontend/architecture) 看棋子如何组合 。
- 看[组件](/design/components)在你创造新东西之前。 重新使用现有设备几乎总是更好的。
- 帮助审查:测试别人的pull request 并留下你的发现. 这能加快每个人的进度 包括你的
