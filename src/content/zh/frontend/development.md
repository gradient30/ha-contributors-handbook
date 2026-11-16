---
title: 开发
description: 所有你需要的工作 在前端本身。 环境,运行它,画廊和演示,编码指南,测试,以及审查.
order: 10
---

# 开发 {#development}

这些页面用于在 [前端仓库](https://github.com/home-assistant/frontend) 上工作: 修复错误, 改进屏幕, 并添加功能 。 建造一个人们自己安装的卡片或面板不需要这些. 关于这一点,见[自定义卡片及其他](/frontend/custom-ui)。

## 工具 {#the-tools}

前端用 TypeScript 写为 [升](https://lit.dev/), 并用 [包装](https://rspack.dev/) 捆绑. [小时](https://pnpm.io/) 管理依赖 。 以 [维特](https://vitest.dev/) 和 [剧作家](https://playwright.dev/) 运行的测试 。 您需要的所有命令都是 `package.json` 中的脚本, 所以您用 `pnpm` 运行它们 。

## 页面 {#pages}

- 我们走吧。 [建立环境](/frontend/development/environment) : 与 depcontainer, 或者在你自己的机器上。
- [运行前端](/frontend/development/run):反对一个发展Home Assistant,或者反对一个你已经拥有的。
- [画廊和演示](/frontend/development/gallery-and-demo):完全没有Home Assistant的组件和仪表板的工作。
- [编码准则](/frontend/development/guidelines):前端代码是如何写的,以及审查者寻找的.
- [B. 定式和测试](/frontend/development/testing) : 在打开 pull request 之前要运行的检查 。
- [构建](/frontend/development/builds): 制作一个生产, 并尝试别人的 pull request 在真实的 Home Assistant 上。
- 拂晓 [打开 pull request](/frontend/development/pull-requests): 您的pull request 需要什么才能得到审查 。
- [审查和发布](/frontend/development/review-and-release) : 您的pull request 会发生什么, 以及它是如何到达用户的 。

在一个地方的所有命令和端口 : [图标](/frontend/reference/commands).
