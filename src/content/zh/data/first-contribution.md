---
title: 你的首次数据贡献
description: 分享你安装的分析数据，准确查看它发送了什么，并查看你的安装被计数。只需几分钟并重启一次。
order: 1
sidebarLabel: 你的第一次贡献
---


# 你的首次数据贡献 {#your-first-data-contribution}
最简单的数据贡献是共享你自己 Home Assistant 安装的分析数据。它有助于项目决定将时间投入到哪里，并在团队向制造商要求本地控制时提供实际数据。除非你启用，否则不会共享任何数据。

## 1. 打开分析设置 {#1-open-the-analytics-settings}
在 Home Assistant 中，转到 **设置** > **系统** > **分析**。如果你最近设置了 Home Assistant，在入门时你可能已经在这里做出了选择。

## 2. 选择分享内容 {#2-choose-what-to-share}
有几个选项，每个都是独立的：

- **基本分析**：你的 Home Assistant 版本和安装类型，以及一些关于系统的细节。用于使用情况和统计数据。
- **使用情况**：你使用的集成和应用。
- **统计数据**：仅计数，例如实体和自动化的数量。
- **诊断数据**：当发生意外错误时发送到 Sentry 的崩溃报告。当前，这仅涵盖 Supervisor 和操作系统代理。

[哪些分析会被分享](/data/reference/analytics-data) 列出了所有字段。开启你觉得舒适的选项。每个选项都有帮助。

## 3. 为分析启用日志记录 {#3-turn-on-logging-for-analytics}
每次 Home Assistant 发送报告时，它都会将精确数据写入日志。它是在 `info` 级别进行记录的，默认情况下，日志只显示警告和错误。因此，首先为分析启用日志记录。将此添加到你的 `configuration.yaml` 文件中。如果你已经有 `logger:` 部分，请在其 `logs:` 下添加此行：

```yaml
logger:
  logs:
    homeassistant.components.analytics: info
```

然后重新启动 Home Assistant。有关日志级别的更多信息，请参阅 [logger 集成](https://www.home-assistant.io/integrations/logger/)。

不想重新启动？可以从 **设置** > **工具** > **操作** 中运行 `logger.set_level` 操作，并以 `homeassistant.components.analytics: info` 作为其数据。这将持续到下一次重启，并且下一次报告可能会在最多 24 小时后进行。

## 4. 检查你发送的内容 {#4-check-what-you-sent}
Home Assistant 会在启动后 15 分钟发送第一次报告，然后每 24 小时发送一次。进入 **设置** > **系统** > **日志**，在菜单中选择 **显示原始日志**，并查找以以下内容开头的消息：

```text
Submitted analytics to Home Assistant servers. Information submitted includes
```

这一行就是完整的每日报告：你的基本数据、使用情况和统计数据。没有名字、没有实体 ID、没有地址。接收服务器会添加一项内容：你的国家，根据你的 IP 地址获取，美国则还会添加州信息。

这不是分析可以发送的全部内容。**设备数据库** 数据作为单独的报告发送，日志中只会显示已发送，并不会显示其中的内容。**诊断** 崩溃报告则发送到 Sentry，根本不会在这里显示。

查看后，请从 `configuration.yaml` 中删除该行并重新启动，以保持日志安静。

## 5. 查看结果 {#5-look-at-the-result}
打开 [analytics.home-assistant.io](https://analytics.home-assistant.io/)。该网站显示有多少安装程序共享分析数据，它们运行的版本，以及最受欢迎的集成。现在，你的安装也是其中之一，以众多匿名计数中的一个方式存在。

## 接下来做什么 {#what-is-next}
- 帮助建立设备数据库：在 **设置** > **系统** > **实验室** 中开启 **设备数据库** 预览功能，并分享你设备的匿名数据。请参阅 [分析如何工作](/data/how-it-works#the-device-database)。
- 阅读所有相关的 [隐私原则](/data/privacy)。
- 想了解自己家庭的数据吗？试试 [探索你自己的数据](/data/guides/explore-your-data)。
