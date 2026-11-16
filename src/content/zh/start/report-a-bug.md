---
title: 报告错误
description: 向哪个仓库报告错误、错误报告表格要求什么以及在哪里可以找到它，以及报告后会发生什么。
order: 3.5
---



# 报告错误 {#report-a-bug}
一个好的错误报告是你能为项目提供的最有用的东西之一。你不需要为此编写代码，只需要一个免费的 [GitHub](https://github.com/signup) 账户和一点耐心。本页面帮助你选择正确的提交位置，收集表单所需的信息，并了解提交之后会发生什么。

错误报告适用于那些没有按预期工作的事情。关于你自己环境的问题请访问 [帮助页面](https://www.home-assistant.io/help/)，而新的想法请提交到 [功能请求](https://github.com/home-assistant/feature-requests/discussions)。

## 在你报告之前 {#before-you-report}
- **先更新。** 确认该问题在最新版本中仍然存在。几个表单会要求你确认这一点。
- **搜索现有问题。** 使用仓库 **Issues** 标签页上的搜索框。找到了匹配的？请给一个 👍，或者添加任何你知道的新信息，而不是再开一个问题。
- **安全问题？** 不要在这里报告：issues 是公开的。请改为[私下报告漏洞](/security/report-a-vulnerability)。
- **请用英语书写。** 这样每个人都能跟上。使用翻译工具也可以：参见 [AI 政策](/start/ai-policy#non-native-english-speakers)。

## 选择仓库 {#pick-the-repository}
Home Assistant的每个部分都有自己的问题追踪器。在代码所在的地方报告问题：

| 问题在 | 报告到 |
| --- | --- |
| Home Assistant Core中的集成、自动化或其他任何内容 | [core](https://github.com/home-assistant/core/issues) |
| 界面：仪表盘、卡片、设置屏幕和对话框 | [frontend](https://github.com/home-assistant/frontend/issues) |
| Supervisor：更新、备份和安装应用 | [supervisor](https://github.com/home-assistant/supervisor/issues) |
| Home Assistant OS，操作系统本身 | [operating-system](https://github.com/home-assistant/operating-system/issues) |
| 官方应用之一 | [addons](https://github.com/home-assistant/addons/issues) |
| Android应用、Wear OS或Android Auto | [android](https://github.com/home-assistant/android/issues) |
| iOS、iPadOS、watchOS或macOS应用 | [iOS](https://github.com/home-assistant/iOS/issues) |
| home-assistant.io上的文档 | [home-assistant.io](https://github.com/home-assistant/home-assistant.io/issues) |不确定？看起来不对的仪表盘属于前端，即使是在伴侣应用中也是如此。iOS 表单建议一个快速测试：如果问题也出现在 Safari 中，请在前端报告。仍然不确定它属于哪里？先在 [Discord](https://www.home-assistant.io/join-chat/) 上询问。

在仓库的 **New issue** 页面，选择错误报告表单。该页面上的其他选项会引导你到适合的地方进行支持和功能请求。

## 表单要求的信息 {#what-the-forms-ask}
每个表单都会要求对问题进行清晰描述，大多数表单还会要求提供复现问题的步骤。将这些步骤写成编号步骤，以便其他人可以跟随操作。然后每个表单会要求各自的详细信息。

#

## Home Assistant Core {#home-assistant-core}
- 出现问题的 Home Assistant Core 版本，以及如果你知道的话，最后一个正常工作的版本。
- 你的安装类型：Home Assistant OS、容器（Container）、监督安装（Supervised）或核心安装（Core）。
- 引起问题的集成（integration），以及其在 home-assistant.io 上文档页面的链接。链接有助于相关人员找到你的问题。
- 设备或集成提供的[诊断信息](/glossary/diagnostics)，如果有的话。
- 一个可复现问题的 YAML 示例（如果适用），以及日志中任何有用的信息。

### 前端 {#frontend}
- 一个清单：你已更新 Home Assistant，清除了浏览器缓存，尝试了另一个浏览器，并尝试了 [安全模式](https://www.home-assistant.io/blog/2023/11/01/release-202311/#restarting-into-safe-mode) 以排除自定义卡片和其他自定义资源。
- 实际发生的情况与预期发生的情况。
- Home Assistant Core 版本、浏览器及其版本，以及运行的操作系统。
- 有关实体显示问题：从更多信息对话框的 **详细信息** 视图中获取其状态和属性。
- 涉及的卡片的 YAML 代码，以及浏览器控制台中的任何错误。

### Supervisor {#supervisor}
- 该表单仅适用于支持的设置。它仍然提供 Home Assistant OS 和 Home Assistant Supervised 作为安装类型，但监督安装不再是支持的安装类型。请参阅 [安装类型](/os/installation-types)。
- Supervisor 日志、系统信息，以及如果可能的话，Supervisor 诊断信息。

### Home Assistant OS {#home-assistant-os}
- 你使用的镜像，比如 `generic-x86-64` 或 `rpi5-64`，以及 Home Assistant OS 的版本。
- 问题是否在操作系统更新后出现。
- 硬件详情，尤其是裸机 x86 安装，以及你连接的任何 USB 设备。在虚拟机中，说明虚拟机管理程序及其版本。
- Supervisor 日志和主机日志。

表格要求你首先使用最新版本进行测试。如果看起来像是回归问题，请检查在上一版本中问题是否消失。你可以使用 `ha os update --version x.y` 回退，其中 `x.y` 是你想要的版本。

### 安卓 {#android}
- 应用的版本、安卓版本以及设备型号。对于 Wear OS，请列出手机和手表的型号。
- Home Assistant 版本，以及上一次可正常使用的版本。
- 应用的日志，以及问题的截图或视频。对于通知问题，请提供你使用的 YAML 文件。

#

## iOS 和 macOS {#ios-and-macos}
- 设备型号和软件版本，可在设备的 **设置** > **通用** > **关于本机** 查看。
- 应用版本，可在应用的 **应用配置** > **关于** 中查看。请包含括号中的版本号。
- Home Assistant Core 版本、你期望发生的情况，以及截图。

## 哪里可以找到它 {#where-to-find-it}
Home Assistant 显示了表格所要求的大部分内容，如果你知道在哪里找的话。

- **版本和安装类型：** 转到 **设置** > **系统** > **维修**，然后点击右上角的三个点菜单，选择 **系统信息**。底部的复制按钮可以复制所有信息，用于需要完整系统信息的表格。
- **诊断信息：** 转到 **设置** > **设备和服务**，打开集成或设备，然后在其三点菜单中选择 **下载诊断信息**。将下载的文件拖入表格，不要粘贴其内容。[调试日志和诊断](https://www.home-assistant.io/docs/configuration/troubleshooting/#debug-logs-and-diagnostics) 在 home-assistant.io 上有更多说明。
- **日志：** 转到 **设置** > **系统** > **日志**。在右上角选择 **Supervisor** 或 **主机** 查看这些日志。在 Home Assistant CLI 中，`ha supervisor logs` 和 `ha host logs` 显示相同内容。

- **Android 应用日志：** 在应用中，进入 **设置** > **伴侣应用故障排除** > **显示并分享日志**。对于 Wear OS，表单要求提供手表的 LogCat 日志。
- **浏览器错误：** 打开浏览器的开发者工具，并从控制台复制错误。

在粘贴任何内容之前，请删除密码、私人网址和其他个人信息。

## 提交报告后 {#after-you-report}
前端、Android 和 iOS 的错误报告表单会自动添加 `bug` 标签。Home Assistant Core 做得更多：- **集成的标签。** 机器人会添加一个 [标签](/glossary/label)，例如 `integration: hue`，使用报告中的文档链接。它还会提到该集成的 [集成负责人](/glossary/integration-owner)，以便他们了解你的问题。
- **重复检查。** 一旦添加了集成标签，工作流会使用 AI 模型将你的问题与过去六个月同一集成的其他问题进行比较。如果发现可能的重复项，会在评论中列出它们并添加 `potential-duplicate` 标签。查看这些问题：如果其中有一个是相同的问题，请关闭你的问题并将你的详细信息添加到那里。如果你的问题不同，请说明具体情况。
- **语言检查。** 非英文的问题会被关闭并添加 `non-english` 标签，并在评论中要求你用英文重新提交。

- **问题。** 集成所有者或维护者可能会要求提供更多细节，例如日志或诊断信息，或者添加 `needs-more-information` 标签。请在可以的时候回答。没有答案，问题无法向前推进。

### 保持活跃 {#keep-it-alive}
一个一段时间没有活动的问题会被标注为 `stale`，如果之后仍没有任何动静，它会被关闭。在 Home Assistant Core 中，这是在 90 天后，问题会在 7 天后关闭。仍然有问题吗？检查它是否在最新版本上发生，并在评论中说明。这会重置计时。一旦问题被关闭，机器人会在一段时间后锁定它。[陈旧且已锁定](/start/pull-requests#stale-and-locked) 显示了每个仓库的具体时间安排。

#

## 当问题被修复时 {#when-its-fixed}
修复会在 pull request 中出现，由接手的人完成。那个人可能是你。一旦合并，它会在下一个版本中传达给所有人。紧急修复可以更快地进入补丁版本：评审者会决定，并将 pull request 添加到下一个补丁版本的里程碑中。想在其他人之前尝试下一个版本吗？[加入测试版](/releases/first-contribution)。
