---
title: 翻译工作方式
description: 弦从何而来,面谈从何而来,最终如何在Home Assistant见下文.
order: 2
sidebarLabel: 它是如何运作的
sidebarLabel: 工作原理

---

# 翻译工作方式 {#how-translation-works}

Home Assistant中的每个文字都以万美元开头,在源代码中. 从那里,它通过Lokalise前往翻译,并在建成时返回Home Assistant.

## 弦的闸门 {#where-the-strings-come-from}

开发者将英文文本写在使用该文本的代码旁边:

- ** Frontend ** 文本,像菜单和对话框一样,生活在 [前端仓库](https://github.com/home-assistant/frontend) 中.
- ** Backend**文本属于集成. 每个集成都有 `strings.json` 文件及其设置步骤,实体名称,状态,以及错误消息.
- iOS和Android寄存器中,

当新的或更新的英文文本被合并到前端或[核心存储器](https://github.com/home-assistant/core)时,新字符串会自动上传到Lokalise. iOS应用程序每天上传一次其字符串.

## 翻译发生的地方 {#where-translation-happens}

这些来源都有自己的Lokalise项目。 这就是为什么有[4个项目将加入](/translate/first-contribution#1-pick-a-project):前端,后端,iOS,和Android. 在一个项目中,每个语言都由社区翻译。 任何加入的人都可以翻译字符串和改进现有的翻译. 没有单独的批准步骤: Lokalise中保存的译文是船只的译文.

## 翻译如何回归 {#how-translations-get-back}

对于Home Assistant本身,翻译不存储在源代码中. 它们从Lokalise创建代码时下载. 只有Lokalise标记为未验证的翻译被忽略 。 前端和后端是分开构建的,因此在不同的时刻获得翻译:

- **Backend**:每组Home Assistant Core,夜间,β,或发布,下载最新的后端翻译. 这栋楼包含着一直到那个时刻所翻译的一切。
- **Frontend**:前端在建成时下载其翻译,每晚和每版前端发布. 晚建Home Assistant使用最新的晚间前端. Home Assistant的β或发布包含一个特定的前端发布,从前端发布建成的那一刻开始翻译.

Android应用程序在构建时也会下载翻译. iOS app是例外: 每天从 Lokalise 中提取翻译, 并在 [iOS 存储器](https://github.com/home-assistant/iOS) 中打开 pull request 。

这也意味着一个固定从不遥远。 今天校正一个翻译,它位于下一个后端构建,或下一个前端发布.

## 这里没有翻译的东西 {#what-is-not-translated-here}

- ** 文件**:关于[Home Assistant.io](https://www.home-assistant.io/)的文件只有英文。
- ** Voice 命令**:句子Assist理解的句子在GitHub上保留,而不是在Lokalise中. 见[声音](/translate/voice).
