---
title: 你的第一个β测试
description: 加入β,在其他人之前一周运行下一次发布,并报告中断的时间.
order: 1
sidebarLabel: 你的第一次贡献
---

# 你的第一个β测试 {#your-first-beta-test}

每个月,下一个释放的β在释放之前一周出来. 这周发现的每个虫子都是不会击中别人家的虫子. 测试β是您能国家的政府最有价值的事情之一,您只需要一个 Home Assistant 的安装来完成它.

## 知道你报名的目的 {#1-know-what-you-are-signing-up-for}

一个β几乎完成,但并不完全. 大多数时候都很好 有时有些东西会断 在加入之前:

- 测试一个装置,如果一个问题是一个烦恼,而不是灾难。 如果您的加热或警报取决于 Home Assistant, 请考虑一下, 或者测试第二个安装 。
- 确保你有一个最近的备份。 如果你允许的话,每更新之前就做一个。
- 一周内要几个β 缝合物一找到就进来

## 2. 加入β频道 {#2-join-the-beta-channel}

On Home Assistant OS:

1. 转到**Settings** > **System** > ** Updates**。
2. 在右上角,打开三个点的菜单.
3. 选择**Joinβ频道**.
4. 安装显示的更新 。 如果不显示,请在同一菜单中选择 ** 检查更新** 。

也可以从命令行进行:

```bash
ha supervisor options --channel beta
ha supervisor reload
ha core update --backup
```

运行 Home Assistant Container ? 使用图像的 `beta` 标记, 再创建容器 :

```bash
docker pull ghcr.io/home-assistant/home-assistant:beta
```

## 3.  读取 beta 释放符 {#3-read-the-beta-release-notes}

[β发布注释](https://rc.home-assistant.io/latest-release-notes/) 解释什么是新事物, 并列出前后不兼容的更改 。 首先读读与时俱进的变换:它们告诉你你可能需要改变什么。 那就试试你关心的新特点

## 报告什么中断 {#4-report-what-breaks}

有问题吗? 在你报告之前:

- 检查在需要时 它在在需要时的稳定释放的共同作用吗?
- 搜索问题追踪器 有人可能已经报案了 如果是的话,就把你知道的内容添加到这个问题上,而不是开启一个新的问题。

然后在正确的寄存器中打开一个问题:

- 集成,自动化,以及核心:[核心议题](https://github.com/home-assistant/core/issues).
- 界面,仪表板,和卡片:[前端问题](https://github.com/home-assistant/frontend/issues).
- 文档和发布注释 : [Home Assistant.io问题](https://github.com/home-assistant/home-assistant.io/issues).

您需要一个免费的 GitHub 账户来打开一个问题 。 新建到 GitHub ? 见 [使用 GitHub,](/start/github).

完全填写发行模板. 提及您运行的β 版本, 如 `2026.11.0b2` , 您所期望的, 所要的, 以及相关的日志信息 。 在核心中,链接集成的文档页面,并附加其诊断文件,如果它有:模板要求两者兼备. 一份清晰的报告会更快地得到修复.

### 报告后会发生什么 {#what-happens-after-you-report}

- ** 标签和整合所有人。 ** 在核心中, Home Assistant bot 根据您命名的集成物添加 `integration:` 的 标签, 并引用该集成物的 [融合所有人](/glossary/integration-owner), 所以知道它的人最好得到一个通知 。
- ** 重复检查。 ** 一旦一个整合标签被贴上,核心的工作流程就会寻找类似的未决问题。 如果找到, 它会在向工作组的评论中链接, 并添加 {向他们> 标签抱着 。 看看,如果其中之一是你的问题,那就继续吧。
- 问题。 ** 集成所有者或维护者可以要求更多的细节,如日志或诊断,或者给问题`needs-more-information`贴上标签. 随时回答 继续测试下一个β
- ** 固定号。 ** 固定开始为 pull request 。 在β周期间,它降落在下一个β之一. 发布后进入补丁发布. 见[获得补丁释放](/releases/guides/patch-releases).

在核心或前端一个90天没有活动的问题被标为`stale`,如果无事发生则7天后关闭. 一篇评论足以保持开放.

> [!TIP]
> 不知什么是虫子,还是怎么报告? 在 [贝塔**](https://discord.com/channels/330944238910963714/427516175237382144) 频道中询问 [Home Assistant Discord 服务器](https://www.home-assistant.io/join-chat) 。 其他测试者和开发者也在β周期间出现.

## 留下来或离开 {#5-stay-or-leave}

当发布出来后,你得到它作为一个正常的更新.杏仁可留于下月的β频道上,也可在同一个菜单中与**leaveβ频道**一起保留. 离开不会自动降级:当它比运行时更新时,会获得下一个稳定释放.

## 接下来是什么 {#what-is-next}

- 读 [如何释放工作](/releases/how-it-works) 时你就知道会发生什么 。
- 在Beta的释放笔记中找到一个字典或者一些不明的东西? 这也是值得修复的。 见[发行笔记和发行方](/releases/guides/release-notes).
