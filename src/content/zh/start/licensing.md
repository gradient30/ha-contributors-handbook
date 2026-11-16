---
title: 许可和 CLA
description: Home Assistant 使用哪些许可证，Contributor License Agreement 是怎么说的，以及你如何签署它。
sidebarLabel: 许可和 CLA
order: 8
---



# 许可和 CLA {#licensing-and-the-cla}
你对 Home Assistant 的所有贡献都是以开源许可证的方式与世界共享的。在你的第一次代码贡献被合并之前，你需要通过签署 Contributor License Agreement（CLA），确认你有权以这种方式分享代码。这个操作只需做一次。

## 许可证 {#the-licenses}
- **代码** 发布在 [Apache License 2.0](https://www.home-assistant.io/developers/license/) 下。这包括 Home Assistant Core、前端以及其他软件仓库。
- **文档** 在 home-assistant.io 上发布在 [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://github.com/home-assistant/home-assistant.io/blob/current/LICENSE.md) 下。

每个仓库的根目录下都有一个 `LICENSE` 文件。如有疑问，该文件就是该仓库的准则。

## Contributor License Agreement {#the-contributor-license-agreement}
CLA 很简短。通过提交贡献，你确认以下内容：

```txt
By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the Apache 2.0 license; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the Apache 2.0 license; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it) is maintained indefinitely
    and may be redistributed consistent with this project or the open
    source license(s) involved.
```

简单来说：你自己写的，或者来自你有权共享的开源作品。并且你理解你的贡献是公开的，并将保持公开。

CLA 基于 Linux 项目的 [开发者原始认证](https://elinux.org/Developer_Certificate_Of_Origin)，修改为使用 Apache 2.0 许可证并省略签名。其文本可在 [Creative Commons 知识共享署名-相同方式共享 3.0 国际许可协议](https://creativecommons.org/licenses/by-sa/3.0/) 获取。完整页面及其历史记录在 [home-assistant.io](https://www.home-assistant.io/developers/cla/)。

## 签署 {#signing-it}
你不需要提前做任何事情。Home Assistant 的代码仓库，比如 Core、前端、伴侣应用、Supervisor、Home Assistant OS 以及官方应用，会检查每个 pull request 是否有签署 CLA。第一次在其中的某个仓库中打开 pull request 而还未签署时，会有一个机器人评论附带链接。点击链接并按照上面的指示操作。一旦签署，它也适用于你未来的贡献。

## 来自其他地方的代码 {#code-from-somewhere-else}
当你引入自己未编写的代码时，例如来自其他项目的代码片段，注意事项 (b) 很重要。只有在其许可允许的情况下才可以这么做，并在你的 pull request 中说明来源。对于使用 AI 工具编写的代码也是同样：你需要对自己提交的内容负责。请参阅 [AI 政策](/start/ai-policy)。

## 致谢 {#credits}
Home Assistant 有一个 [致谢页面](https://www.home-assistant.io/developers/credits/)，列出了在该项目的各个仓库中做出贡献的人。
