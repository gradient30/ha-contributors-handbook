---
title: 创建并共享一个仓库
description: 把你的应用放到一个 Git 仓库中，用户可以将其添加到他们的应用商店，并让添加它成为一个单步骤操作。
order: 12
---


# 创建并共享一个仓库 {#create-and-share-a-repository}
用户从仓库安装应用程序。一个仓库是一个 Git 仓库，根目录下有一个 `repository.yaml`，每个应用程序一个文件夹。它可以包含一个应用程序或数十个应用程序。

## 创建仓库 {#create-the-repository}
最快的起步方式是使用 [示例应用仓库](https://github.com/home-assistant/apps-example)。在 GitHub 上选择 **Use this template**，你就会一次性获得应用、文档文件、AppArmor 配置文件、开发容器以及构建工作流程。然后：

1. 重命名 `example` 文件夹，并在其 `config.yaml` 中设置与 `slug` 相同的名称。
2. 在 `config.yaml` 中将 `image` 改为你自己的注册表，例如 `ghcr.io/<your-username>/my-app`。
3. 修改所有指向 `home-assistant/apps-example` 的链接和名称。这包括 [`.github/workflows/build-app.yaml`](https://github.com/home-assistant/apps-example/blob/main/.github/workflows/build-app.yaml) 中的 `github.repository` 检查：在你更改它之前，工作流程会跳过除示例仓库之外的任何构建。
4. 更新 `repository.yaml`。

或者从零开始，使用如下布局：

```text
my-apps/
  my_app/
    config.yaml
    Dockerfile
    DOCS.md
    README.md
  repository.yaml
  README.md
```

`repository.yaml` 指定了仓库及其维护者的名称：

```yaml
name: "My apps"
url: "https://github.com/me/my-apps"
maintainer: "Jane Doe <jane@example.com>"
```只需要 `name`。该文件也可以是 `repository.yml` 或 `repository.json`。如果没有该文件，或者文件无效，Supervisor 根本无法加载仓库。

Supervisor 可以在仓库中的任意深度查找应用，所以如果你愿意，可以将它们分组到文件夹中。隐藏文件夹和名为 `rootfs` 的文件夹会被跳过。

## 向 Home Assistant 添加存储库 {#add-a-repository-to-home-assistant}
用户在应用商店中添加你的存储库：

1. 前往 **设置** > **应用** 并选择 **安装应用**。
2. 在右上角菜单中选择 **存储库**。
3. 输入你的存储库 URL 并选择 **添加**。

你的应用随后会显示在应用商店中，位于来自你的 `repository.yaml` 的 `name` 部分。

URL 可能以 `#` 和一个分支名结束，例如 `https://github.com/me/my-apps#next`。Supervisor 会使用该分支而非默认分支。这就是你提供 [测试渠道](/apps/guides/presentation#offer-a-beta-channel) 的方式。

Supervisor 使用 Git 克隆存储库，因此它不必在 GitHub 上。设备能够访问的任何 Git URL 都可以使用。

## 一步完成 {#make-it-one-step}
[我的链接](/glossary/my-link) 会在用户自己的 Home Assistant 中打开正确的页面。`supervisor_add_addon_repository` 链接会打开添加应用程序仓库的对话框，并自动填入你的 URL。将其作为徽章放在你的 README 中：

```markdown
[![Open your Home Assistant instance and show the add app repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fme%2Fmy-apps)
```

将 `repository_url=` 之后的 URL 编码部分替换为你的仓库 URL。[我的链接创建器](https://my.home-assistant.io/create-link/?redirect=supervisor_add_addon_repository) 会为你构建链接和徽章，并自动编码 URL。

要链接到某个应用程序的页面，请使用`supervisor_app` 链接，并包含该应用程序的完整 slug，包括 [仓库 ID](/apps/guides/repository#the-repository-id)：`https://my.home-assistant.io/redirect/supervisor_app/?app=a1b2c3d4_my_app`。

## 仓库 ID {#the-repository-id}
Supervisor 为每个仓库分配一个 ID：它是仓库 URL 的 SHA-1 哈希的前 8 个字符的小写形式，如果有 `#branch` 也包括在内。你的应用在其 slug 前会带有这个 ID，例如 `a1b2c3d4_my_app`，在内部网络中则为 `a1b2c3d4-my-app`。

由于 ID 来源于 URL，所以来自不同分支或重命名仓库的相同应用对 Supervisor 来说是不同的应用。一旦有人使用它，请保持 URL 稳定。

要查看仓库的 ID，可在 Supervisor API 上调用 `GET /store/repositories`，或在终端运行 `ha store`。

## 分享它 {#share-it}
当你的仓库准备好后：

- 为仓库写一个 README，简要描述每个应用，并添加 [徽章](/apps/guides/repository#make-it-one-step)。
- 在社区论坛的 [分享你的项目](https://community.home-assistant.io/c/projects/9) 分类中发布它。
- 关注问题。你的应用用户会通过那里找到你。
