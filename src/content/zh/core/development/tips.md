---
title: 提示与技巧
description: 从堆叠 pull request 到在自己的系统中测试变化, 使 Home Assistant Core 工作更加容易的小东西 。
sidebarGroup: 调用请求
order: 6
---



# 提示与技巧 {#tips-and-tricks}
集诸善知识但不必自页. 捡到一个在这里缺失的把戏? 在本页底部加上编辑链接。

## 将大作品分成 pull request 系列 {#split-big-work-into-a-series-of-pull-requests}

实现旧的一体化的现代化可能诱人一去不复返。 别 将工作分成独立的更改,然后逐个提交。 不要在 pull request 中混合清理和新特性, 也不要在一个中解决几个问题 。 立即撤回大量代码的请求不是优先审查事项,可能会结案。

为了在第一个被审查的时候继续工作, 将下一个从第一个中分离出来:

1. 从当前 pull request 的分支创建下一个 pull request 的分支, 并继续写入代码 。
2. 当当前 pull request 从审查反馈中获得新承诺时, 将它们合并到下一个分支 。
3. 当当前 pull request 合并后, 用最新的 `dev` 更新下一个分支, 因此它只包含自己的更改 。
4. 打开下一个 pull request, 重复 。

再见 Collins. 在合并第一个之前不要打开下一个 pull request 。 调用依赖于未合并工作的请求对审查人员来说是无法采取行动的。

## 尝试改变您的生产系统 {#try-a-change-on-your-production-system}

您可以通过装入一个自定义集成来运行一个已更改的核心集成 Home Assistant :

1. 将合并的文件夹复制到 `/config/custom_components/` 。
2. 将 `version` 添加到它的 `manifest.json`, 如 `"version": "0.0.0"` 。 自定义整合需要一个。
3. 如果集成有 `strings.json` , 请在您的开发环境中运行 `python3 -m script.translations develop --integration example`, 使用您的域名而不是 `example` 。 复制生成的 `translations/en.json` 到复制的文件夹 。 一个 {H 杰克} 的纯副本只有在没有 `[%key:...]` 引用时才有效, 因为 Home Assistant 并不能解决那些用于自定义集成 。
4. 重新开始 Home Assistant可供使用 。

自定义集成取代了同一域的内置集成,但安全模式和恢复模式除外,后者跳过自定义集成. 完成后删除它,或者永远被卡在那版本上.

## 尝试新版本库 {#try-a-new-version-of-a-library}

选取到 / 被 / 或 或 或 或 或 或 或 或 或 。

## 您的新配置流没有出现 {#your-new-config-flow-does-not-show-up}

前端的缓存很活跃 当您添加一个配置流程且整合不出现在列表中时, 请先检查日志是否出错 。 如果没有,请重新刷新浏览器。

## 请求链接帮助 {#ask-for-help-with-a-link}

当您在 [Discord](https://www.home-assistant.io/join-chat/) 上询问一个技术问题时, 请在 [编码支持**](https://discord.com/channels/330944238910963714/1257019582112334014) 中启动一条线程, 先将您的工作推向分支, 并共享链接 。 能看到你密码的人能更快地帮你 不要粘贴大块代码到线程中: 它们很难读取 。

## 举个例子 {#look-at-good-examples}

[整合质量尺度](/core/quality-scale)的白金和黄金两层的整合得到了很好的维护,并且是一个看事情如何做的好地方. 等级在整合的`manifest.json`中.

## 产生新的整合 {#generate-a-new-integration}

脚手架脚本问你几个问题,并创建了新集成的文件,其中包含一个配置流和测试从:

```shell
python3 -m script.scaffold integration
```

在Visual Studio代码中,这就是**创造新集成**任务. [建设一体化](/core/integrations)解释它产生什么。
