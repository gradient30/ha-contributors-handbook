---
title: 版本和频道
description: Home Assistant的版本号意味着什么, 和稳定的,β和dev的频道。
order: 1
---

# 版本和频道 {#versions-and-channels}

Home Assistant使用日历版本:该版本在发布时告诉你.

## 版本编号 {#version-numbers}

一个版本有三个部分:年号,月号,以及补丁号. `2026.11.0`是2026年11月的发布,`2026.11.1`它的首次补丁发布. 一个β添加`b`和一个数字,像`2026.11.0b0`. 夜与开发建设增加`.dev`.

版本格式由Home Assistant Core定义和保存. [版本](/core/development/versioning) 临时议程项目有完整的格式,各种版本都有实例,版本是如何在代码中设置的.

## 频道 {#channels}

安装 Supervisor , 如 Home Assistant OS , 通过频道获取更新 。 每个通道在新和稳定之间是不同的平衡.

| 频道 | 你会得到 | 对于 |
| --- | --- | --- |
| 稳定 | 释放 也许可以 | 每个人。 这是默认的。 |
| 贝塔 | β周的贝塔,所有稳定的释放 | 欲助试下释者. |
| 德维 | 开发处的夜间建设 | 谐音的开发凿者与测试最新代码的人,并接受破解. |

在 **Settings ** > **System ** > ** Updates **中,您在稳定与β之间切换。见[你的第一次贡献](/releases/first-contribution)。

秩序 Home Assistant Container 使用图像标记代替 : `stable` (也是 `latest`), `beta` 和 `dev`, 每个版本的标记旁边.

## 凡起到了版本 {#where-the-versions-come-from}

安装从 [(原始内容存档于2018-09-25). version. home-assistant.io.](https://version.home-assistant.io/stable.json) 找到新版本 。 它每个频道发布一个文件,当前版本为Home Assistant,Supervisor,Home Assistant OS,其他部分为每类硬件. 文件在 [版本存储器](https://github.com/home-assistant/version) 中保存 。

你不必碰他们。 当发布时,核心的构建工作流程会构建图像,运行端到端测试,然后更新频道的版本文件. 稳定的释放也被推向β通道,因此β测试者也会得到.

## 分支 {#the-branches}

| 仓库 | 开发 | Beta 与补丁发布 | 已发布 |
| --- | --- | --- | --- |
| 核心项目 | `dev` | `rc` | `master` |
| 前端 | `dev` | `rc` | `master` |
| Home Assistant.io | `next` | `rc` | `current` |

贡献者在核心和前端打开pull request对`dev`。 在Home Assistant.io中,对现有文档的分别在`current` 和`next` 中修改,对新文件的文件则在`next` 中修改。

## 每个频道的网站 {#websites-per-channel}

- [www.home-assistant.io](https://www.home-assistant.io/):当前发行的文档.
- [rc.home-assistant.io 互联网档案馆的存檔,存档日期2013-09-02.](https://rc.home-assistant.io/): β的文档和发布注释.
- [下一个,Home Assistant.io](https://next.home-assistant.io/):为下一期所建的文档 。
