---
title: 发布你的应用
description: 使用构建器操作为每种架构构建镜像，将它们发布到容器注册表，并对你的版本进行管理。
order: 11
---


# 发布你的应用 {#publish-your-app}
有两种方式可以将你的应用提供给用户：让他们的设备构建应用，或者你自己构建镜像并发布到容器注册中心。发布镜像几乎在各方面对用户更好。

## 在设备上构建，还是预先构建 {#built-on-the-device-or-pre-built}
如果没有`image`在`config.yaml`，每个用户的设备在安装或更新应用时都会从`Dockerfile`构建你的应用。这对你来说很简单，也适合在尝试一个想法时使用。对于用户来说，这很慢，会损耗SD卡，并且每当你构建所下载的某个包发生变化或消失时就会失败。

有了`image`，Supervisor会拉取一个准备好的镜像。安装快速且可靠，每个用户运行的都是你测试过的内容。一旦人们开始使用你的应用，就发布镜像。

## 使用 GitHub Actions 构建 {#build-with-github-actions}
[builder](https://github.com/home-assistant/builder) 仓库具有可组合的 GitHub Actions，用于构建、签名和发布多架构镜像：

| 操作 | 功能 |
| --- | --- |
| `prepare-multi-arch-matrix` | 将架构列表转换为构建矩阵 |
| `build-image` | 构建并推送单个架构的镜像，如 `ghcr.io/me/aarch64-my-app` |
| `publish-multi-arch-manifest` | 将按架构构建的镜像合并成一个多架构镜像，如 `ghcr.io/me/my-app` |
| `cosign-verify` | 验证 Cosign 签名，被其他操作使用 |

[示例应用仓库](https://github.com/home-assistant/apps-example) 拥有一个完整的工作流程，在每次推送到 `main` 时构建所有变更的应用。可将其复制作为起点。Builder 的 README 对单个镜像有一个更小的示例。

需要设置的一些事项：- 工作流使用工作流的令牌将内容推送到 GitHub 容器注册表，这需要 `packages: write` 权限。使用 Cosign 签名需要 `id-token: write`。
- 第一次推送镜像时，它是私有的。请在 GitHub 的包设置中将其设为公开，否则用户无法拉取。
- 将操作固定到构建器的发布版本，而不是分支。

> [!注意]
> 老的全能 `home-assistant/builder` 操作已弃用且不再维护。如果你的工作流仍在使用它，请迁移到上述操作。[示例应用仓库](https://github.com/home-assistant/apps-example) 展示了新的设置。

## 在 config.yaml 中指向镜像 {#point-configyaml-at-the-image}
将 `image` 设置为多架构镜像的名称，不带标签：

```yaml
image: "ghcr.io/me/my-app"
```

Supervisor 会拉取与 `version` 匹配的标签，Docker 会从清单中选择正确的架构。旧版本的应用程序为每种架构发布一个镜像，并使用 `{arch}` 占位符，例如 `ghcr.io/me/{arch}-my-app`。这仍然有效，但对于新应用程序来说，多架构镜像是更好的选择。

## 版本 {#versions}
`version` 在 `config.yaml` 中是唯一的真实来源：它是用户看到的版本，是 Supervisor 拉取的标签，也是更新通知进行比较的对象。所以：

- 在你修改仓库中的 `version` 之前，先推送带有新标签的镜像。否则，用户将收到无法下载的更新。
- 永远不要在已有标签下推送不同的镜像。已经拥有的用户不会收到更改，新用户会得到与旧用户不同的内容。
- 使用能够正确排序的版本方案，如 [语义化版本](https://semver.org/) 或基于日期的方案，如 `2026.10.0`。示例工作流从 `config.yaml` 的 `version` 中读取标签，并在 `main` 上的 `config.yaml`、`Dockerfile` 或 `rootfs` 发生更改时构建并推送应用。在该推送与构建结束之间，具有 Supervisor 的用户重新加载你的仓库时已经能看到更新，但尚无法下载。保持该时间窗口短，并且在构建失败时不要发布版本升级。

## 不向后兼容的更改 {#backward-incompatible-changes}
用户可以为每个应用开启自动更新。如果某个版本需要他们的注意，例如配置更改或无法撤销的迁移，请将其版本添加到 `breaking_versions`：

```yaml
version: "3.0.1"
breaking_versions:
  - "3.0.0"
```

然后 Supervisor 永远不会自动为旧版本用户安装该版本或之后的版本。他们会看到更新，阅读你的更新日志，并自行安装。在 `CHANGELOG.md` 的顶部解释不向后兼容的更改。

## 最低版本 {#minimum-versions}
如果你的应用需要最近 Home Assistant Core 的某个功能，请将 `homeassistant` 设置为最低版本。在较旧的安装版本中，该应用将不可安装。

## 让用户添加它 {#let-users-add-it}
用户从你的仓库安装你的应用。在你的 README 中的 [我的链接](/glossary/my-link) 徽章会打开对话框，让用户将你的仓库添加到他们自己的 Home Assistant 中，并自动填充 URL。见 [让它一步完成](/apps/guides/repository#make-it-one-step)。
