---
title: 核心与集成
description: Python,核心,和集成平台. 所有瑰宝需要建立和完善的集成物,并致力于Home Assistant Core自身.
---

# 核心与集成 {#core-and-integrations}

Home Assistant Core 是每个 Home Assistant 安装的核心的 Python 应用程序 。 它运行着国产机器,事件总线,自动化,以及连接Home Assistant的设备与服务的数千个集成. 它都住在一个仓库里:[Home Assistant/核心人员](https://github.com/home-assistant/core).

对核心的大部分贡献是大约[ũ](/glossary/integration):添加对新设备的支持,在现有设备中固定一个bug,或者使集成达到更高的质量水平. 一些贡献更深入,深入到各种融合所依赖的帮助者和API中.

如果您要写 Python 或想要写, 此区域是给您的 。 你不需要知道整个密码库 大多数人从他们在家里使用的一个融合开始,然后从那里成长。

## 我们能做的 {#what-you-can-work-on}

- **fix a bug**:在您使用的集成中拾取一个问题,复制,并修复.
- ** 证明整合**:添加测试,添加类型提示,或向下一层的[集成质量等级](/core/quality-scale)工作。
- ** 添加集成**:连接Home Assistant到它尚未支持的设备或服务.
- ** 审查**:测试和审查pull request来自他人。 这是你能做的最有价值的事情之一。

## 从这里开始 {#start-here}

选择与您想要做的匹配的路径 :

1. 来点什么 从来没有为核心作出贡献? 以 [缔造和平](/core/first-contribution) 开始 : 设置您的环境, 修复一个小错误, 并打开您的第一个 pull request 。 一个小的修补会教你整个过程,同样如果以后你想建立一个集成.
2. ** 建立新的一体化。 ** 读 [如何融入](/core/integrations/concepts) , 然后跟着 [教程](/core/integrations/tutorial) 。 它构建了从脚手架到满足青铜级的pull request的小集成. 对于您自己的设备或服务,工程建议从[市场](/marketplace)开始:参见[我发誓它属于核心](/core/integrations/create#does-it-belong-in-core).

然后使用这个区域的其余部分作为你的参考:用于工具和pull request进程的[发展工作流程](/core/development),以及用于其他一切的下面的指南。

## 指南和参考 {#guides-and-reference}

- 历次 [构建集成](/core/integrations) : 如何能够将一个集成, 配置流, 获取数据, 以及其它所有集成的文件 。
- [实体和平台](/core/entities):传感器,灯光,气候设备,以及每一个其他实体类型,每个实体都支持其属性和特征.
- [集成质量等级](/core/quality-scale):描述整合有多好的层次和规则,以及审查者所寻找的.
- [核心如何运作](/core/internals): asyncio, `hass` 对象,事件, 状态, 认证, APIs, 意图, 以及 LLM 支持 。

## 相关领域 {#related-areas}

- 实例 [翻译](/translate/guides/developers): 如何在 `strings.json` 中写字符串, 翻译者可以与之合作 。
- [写入文档](/writing):每个集成在[Home Assistant.io](https://www.home-assistant.io/)上都有一页,你把它和你的代码一起写.
- [前端](/frontend): 当您的更改需要界面中的新东西时 。
- [架构](/architecture): 如何构建Home Assistant背后的决定 。
- [市场](/marketplace):发布一个自定义集成,以便其他人可以从市场安装.

## 谁说话 {#who-to-talk-to}

- 在[Home Assistant Discord](https://www.home-assistant.io/join-chat/)上,一般的发展问题,比如一个集成是否属于核心,适合[发展中国家**](https://discord.com/channels/330944238910963714/554842238073700352). 对于技术问题,请在[编码支持**](https://discord.com/channels/330944238910963714/1257019582112334014)中开始一条线程. [* 核心**](https://discord.com/channels/330944238910963714/1475552721515053268)频道是核心团队讨论Core本身的地方,而不是提问的地方. 看不到频道吗? 在 **Channels & 角色** 下,选择 ** 我想贡献 dev 技能给 Home Assistant**}.
- 臭虫和 {H0berries} 生活在 [核心存储器](https://github.com/home-assistant/core) 中 。 特色创意去[讨论](https://github.com/orgs/home-assistant/discussions).
- 在 [架构存储器](https://github.com/home-assistant/architecture/discussions) 中讨论核心工作方式的改变更大。

要求帮助时,将自己的作品推向一个分支并共享链接. 人们在看到代码时可以更快地帮助你,一个链接可以保持通道的可读性.
