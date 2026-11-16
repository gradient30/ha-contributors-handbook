---
title: 展示你的应用
description: 用户在安装应用程序之前和之后看到的内容。包括介绍、文档、更新日志、图标、标志和翻译。
order: 10
---


# 展示你的应用 {#present-your-app}
如果你分享你的应用程序，其展示方式决定了人们是否信任它足够以安装它。清晰的介绍、诚实的文档和更新日志作用很大。虽然这些文件都不是必需的，但没有它们的已发布应用会显得不完整。

## 介绍 {#introduction}
应用程序文件夹中的 `README.md` 是介绍。应用商店会在应用安装前在应用页面上显示它。保持简短：说明应用做什么，以及为什么有人会想要它。当人们浏览你的仓库时，这也是他们看到的内容，在 GitHub。

## 文档 {#documentation}
`DOCS.md` 是文档，显示在应用的 **文档** 标签上。这是用户在遇到问题时会访问的地方，因此应覆盖以下内容：

- 如何安装和设置应用。
- 每个选项、它的功能及示例。
- 用户在应用外需要执行的任何操作，比如设置集成。
- 已知的限制。
- 如何寻求帮助和报告错误。
- 应用的许可协议。

如果你的应用需要比平常更多的权限，例如 `host_network` 或关闭保护模式，请在此解释原因。用户会看到这些警告，他们有权知道原因。

## 更新日志 {#changelog}
`CHANGELOG.md` 列出了每个版本的更改。当有更新可用时，用户会看到它，并通过阅读它来决定是否立即更新。将最新版本置于顶部，并明确标出向后不兼容的更改。[保持更新日志](https://keepachangelog.com/) 是一个值得参考的格式。

## 图标和徽标 {#icon-and-logo}
| 文件 | 格式 | 尺寸 |
| --- | --- | --- |
| `icon.png` | PNG，方形 | 建议 128 × 128 像素 |
| `logo.png` | PNG | 建议约 250 × 100 像素，其他尺寸也可以 |

图标会显示在应用商店和已安装应用列表中，徽标显示在应用页面上。两者都是可选的。确保它们在浅色和深色背景下都看起来很好。

## 翻译 {#translations}
**配置**选项卡显示你的选项和端口。如果没有翻译，它将显示原始键，例如 `log_level` 或 `8080/tcp`。为每种语言在 `translations` 文件夹中添加一个文件，以便为它们提供可读的名称和描述：

```yaml
# translations/en.yaml {#translationsenyaml}
configuration:
  log_level:
    name: "Log level"
    description: "How much detail to write to the log."
network:
  8080/tcp: "Web interface (not needed with ingress)"
```

请参阅 [添加选项](/apps/guides/options#translate-the-options) 和 [翻译文件格式](/apps/reference/files#translation-file)。

## 阶段 {#stage}
并非每个应用都适合所有人。在 `config.yaml` 中设置 `stage` 来告诉用户你的应用处于什么阶段：

- `stable`：默认值。
- `experimental`：可用，但可能存在问题和变动。
- `deprecated`：不再维护。在文档中引导用户使用替代方案。

## 提供测试版渠道 {#offer-a-beta-channel}
为了让用户在大众之前尝试新版本，请将新版本保存在单独的分支中。用户在 `#` 后添加你的仓库分支名称：

```text
https://github.com/me/my-apps#next
```

在该分支的 `repository.yaml` 中为仓库提供不同的 `name`，例如“我的应用（测试版）”，这样用户在应用商店中就能区分它们。在文档中提及测试版渠道。
