---
title: 仓库
description: Home Assistant 的代码存放在 GitHub 上，以及应去哪个仓库获取什么内容。
order: 5
---


# 仓库 {#repositories}
Home Assistant 分布在许多代码仓库中，其中大多数位于 GitHub 上的 [home-assistant](https://github.com/home-assistant) 组织下。你将会在其中一个或两个仓库中工作。本页面会告诉你具体是哪些仓库。

## 主要仓库 {#the-main-ones}
| 仓库 | 内容 | 语言 |
| --- | --- | --- |
| [core](https://github.com/home-assistant/core) | Home Assistant Core 以及所有内置集成 | Python |
| [frontend](https://github.com/home-assistant/frontend) | 网页界面、组件库和演示 | TypeScript |
| [android](https://github.com/home-assistant/android) | 安卓应用，适用于手机、Wear OS 和汽车 | Kotlin |
| [iOS](https://github.com/home-assistant/iOS) | iPhone、iPad、Mac、Apple Watch 和 CarPlay 应用 | Swift |
| [supervisor](https://github.com/home-assistant/supervisor) | Supervisor | Python |
| [operating-system](https://github.com/home-assistant/operating-system) | Home Assistant OS | Buildroot、shell |

## 文档与设计 {#documentation-and-design}
| 仓库 | 内容 |
| --- | --- |
| [home-assistant.io](https://github.com/home-assistant/home-assistant.io) | 用户文档，包括每个集成的页面 |
| [companion.home-assistant](https://github.com/home-assistant/companion.home-assistant) | 伴侣应用的文档 |
| [brands](https://github.com/home-assistant/brands) | 集成的标志和图标 |
| [architecture](https://github.com/home-assistant/architecture) | 架构讨论和决策，参见 [决策如何做出](/architecture/decisions) |

## 关于 Supervisor {#around-the-supervisor}
| 仓库 | 内容 |
| --- | --- |
| [addons](https://github.com/home-assistant/addons) | 官方应用 |
| [apps-example](https://github.com/home-assistant/apps-example) | 一个启动应用的示例 |
| [cli](https://github.com/home-assistant/cli) | `ha` 命令行 |
| [os-agent](https://github.com/home-assistant/os-agent) | Home Assistant OS 主机上的助手 |
| [docker-base](https://github.com/home-assistant/docker-base) | Home Assistant 和应用的基础镜像 |
| `plugin-dns`, `plugin-audio`, `plugin-cli`, `plugin-multicast`, `plugin-observer` | Supervisor 的插件 |

## 库 {#libraries}
| 仓库 | 内容 |
| --- | --- |
| [home-assistant-js-websocket](https://github.com/home-assistant/home-assistant-js-websocket) | WebSocket API 的 JavaScript 客户端 |
| [home-assistant-libs](https://github.com/home-assistant-libs) | 一个组织，包含由项目维护的 Python 库，比如 Supervisor 客户端 |
| [OHF-Voice](https://github.com/OHF-Voice) | Open Home Foundation 的语音项目，比如 Assist 能理解的句子 |

## 去哪里做什么 {#where-to-go-for-what}
| 你想做 | 去哪里 |
| --- | --- |
| 修复集成中的错误 | core |
| 添加新集成 | 先去 core，然后去 home-assistant.io 查阅文档，品牌标志去 brands |
| 更改 UI 中的内容 | frontend，如果是集成的文本则去 core |
| 修复文档 | home-assistant.io |
| 报告错误 | 出现错误的部分的仓库。不确定？请在 [Discord](https://www.home-assistant.io/join-chat) 上询问。 |
| 提建议功能 | [功能请求](https://github.com/home-assistant/feature-requests/discussions) 讨论 |

## 处理此问题 {#work-on-this}
上面的每个仓库都属于本网站的一个区域，其中解释了如何在该处进行首次更改。请参阅 [准备好贡献了吗？](/architecture#ready-to-contribute) 了解地图。
