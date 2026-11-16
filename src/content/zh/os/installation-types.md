---
title: 安装类型
description: 在哪里使用 Home Assistant OS 和 Supervisor，在哪里不使用，以及这对你的代码意味着什么。
order: 2
---

# 安装类型 {#installation-types}

Home Assistant 有两种支持的 [安装类型](/glossary/installation-type)。其中只有一种包含OS 与 Supervisor。

| | Home Assistant OS | Home Assistant Container |
| --- | --- | --- |
| 操作系统 | Home Assistant OS | 用户运行的任何系统 |
| Supervisor | 是 | 否 |
| 应用程序 | 是 | 否 |
| 系统更新 | 通过 Supervisor | 由用户决定 |

在 Home Assistant Container 上，Home Assistant Core 运行在用户管理的容器中。该区域没有任何内容运行在那里。架构区域的 [核心周围](/architecture/platform) 页面展示了各个部分如何组合在一起。

## 不再支持 {#no-longer-supported}

另外两种安装类型已于 2025 年 5 月弃用，并且支持于 Home Assistant 2025.12 结束：

- **Home Assistant Supervised**：由用户维护的 Linux 系统上安装的 Supervisor。
- **Home Assistant Core**：作为虚拟环境中的 Python 包安装的 Home Assistant。

32 位架构 `i386`、`armhf` 和 `armv7` 也在同一时间被取消。Home Assistant OS 17 移除了最后的 32 位板。[公告](https://www.home-assistant.io/blog/2025/05/22/deprecating-core-and-supervised-installation-methods-and-32-bit-systems/) 解释了原因。

## 这对 Supervisor 意味着什么 {#what-this-means-for-the-supervisor}

Supervisor 仍然从 Home Assistant OS 外部启动，但它将此类系统标记为不支持。在 [解决中心](/os/supervisor/resolution-center) 中进行检查：当操作系统不可用时，系统会得到 `os` 不支持的原因。有些功能完全需要 Home Assistant OS。这些作业使用 `haos` 作业条件，并拒绝在其他地方运行。

因此，当你在 Supervisor 上工作时，应假设使用 Home Assistant OS。仅在其他主机上有意义的代码不再由项目维护。
