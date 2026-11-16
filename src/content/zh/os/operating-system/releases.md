---
title: 发布与构建
description: 变换为Home Assistant OS是如何从pull request到发布,涉及分支,版本号,以及构建管道.
sidebarGroup: 指南
order: 6
---

# 发布与构建 {#releases-and-builds}

Home Assistant OS没有固定的发布时间表。 维护者在有值得释放的东西时释放出来,比如内核更新,固定,或者新的特性. 本页解释您更改的路径 。

## 打开 pull request {#open-a-pull-request}

叉 [Home Assistant/操作系统](https://github.com/home-assistant/operating-system) , 创建分支, 并打开您的 pull request 对 `dev` 。

解释*为什么* 改变很重要, 不仅仅是它做什么。 "更新内核"在diff中可见. "更新内核,因为它修补了X机上的以太网"是审查者需要知道的. 只要有短暂的理由,就很好。

拖动更改构建或系统可以获得 `run-ova-test` 标签的请求 。 用于构建OVA图像并运行其上的自动测试,参见[测试洽谈](/os/operating-system/test#run-the-automated-tests). 只有维护者可以设置标签,构建时只能为主寄存器中的分支运行.

## 分支 {#branches}

- `dev`在提供资料时,会携带下一个版本。 每一个变化先到这里提供资料, 也为当前发布进行修正。
- 搭载释放候选人 维护者将已经准备好的 `dev` 的更改带给它 。
- 搭载稳定释放。 发布后,`main`被合并回`dev`.

旧的主要版本有自己的`rel-<major>`分支. 这些不再用于新的释放。

## 版本编号 {#version-numbers}

一个版本是`MAJOR.MINOR`,类似`18.3`. 数字在 `buildroot-external/meta` 中存在, 加上可选的后缀 :

| 温柔 | 示例 | 从何而来 |
| --- | --- | --- |
| 发展建设 | `18.4.dev20261006` | `dev`,后缀是构建日期 |
| 释放候选人 | `18.4.rc1` | `rc` |
| 稳定释放 | `18.4` | `main`,无后缀 |

本地建筑从 `meta` 获得后缀, 如 `18.4.dev0` 。 CI将其替换为开发日期。

## 部署类型 {#deployment-types}

在 `buildroot-external/meta` 中验证图像信任更新的 `DEPLOYMENT` 值, 请参见 [更新系统](/os/operating-system/update-system#security) 。

| 部署 | 频道 | 用于 |
| --- | --- | --- |
| `development` | 备忘 | 发展建设 |
| `staging` | 贝塔 | 释放候选人 |
| `production` | 稳定 | 发布 |

建设管道在部署,版本格式,频道不匹配时拒绝发布建设.

## 修建管道 {#build-pipelines}

GitHub 动作构建每个公共图像, 带有[`.github/workflows/build.yaml`](https://github.com/home-assistant/operating-system/blob/dev/.github/workflows/build.yaml) 。 它有两种情况:

- ** 当发布GitHub时。 ** 它建立每一个板,运行测试,并将图像附在发布. 预放送去β通道,释放到稳定.
- ** 当维护者用手启动时。 ** 它建立了一个开发版 他们挑的板,或全部。 图像发布于[只是为了保护自己](https://os-artifacts.home-assistant.io/index.html).

用于叉的构件不发布任何内容,并用丢弃的自签证书而不是发行证书来签名.

## 释放后 {#after-the-release}

发行笔记从合并后的pull requests的标签中自动起草,如`board/raspberrypi`或`build`. 用户通过 Supervisor 获得新版本, 该版本检查 [(原始内容存档于2018-09-25). version. home-assistant.io.](https://version.home-assistant.io/stable.json) 以获取其频道的最新 OS 版本 。 更新本身通过RAUC,参见[更新系统](/os/operating-system/update-system).
