---
title: 你的第一个翻译
description: 加入翻译项目, 找到您的语言, 并翻译您的第一个字符串 。 大概需要15分钟
order: 1
sidebarLabel: 你的第一次贡献
---

# 你的第一个翻译 {#your-first-translation}

此向导将您从 0 到您的第一个翻译字符串 。丫头 。 你在浏览器里都这样

## 1.  选择一个工程 {#1-pick-a-project}

Home Assistant的接口文本被分成四个Lokalise项目. 下面的每个链接都会打开项目并让您加入:

- [前端](https://app.lokalise.com/public/3420425759f6d6d241f598.13594006/): Home Assistant 接口本身 。 如果你不确定就从这里开始
- [后端](https://app.lokalise.com/public/130246255a974bd3b5e8a1.51616605/):来自集成的文本,如设置步骤,实体名称,以及错误消息.
- [iOS系统](https://app.lokalise.com/public/834452985a05254348aee2.46389241/):iPhone,iPad,Mac,以及Apple Watch的伴侣应用.
- [安卓](https://app.lokalise.com/public/145814835dd655bc5ab0d0.36753359/):Android手机,平板电脑和Wear OS的伴侣应用.

## 创建账户并加入 {#2-create-an-account-and-join}

Lokalise 请求您创建一个免费账户 。 之后,加入项目,选择自己的语言. 以后您可以加入更多项目和语言。 编辑新来的? 在[翻译和协作](https://docs.lokalise.com/en/collections/2909016-translate-and-collaborate)中解释它。

## 找到要翻译的东西 {#3-find-something-to-translate}

在未翻译字符串上打开您的语言和过滤器 。 如果你的语言已经完整,那是个好消息,还有许多事情要做:通过现有的翻译来阅读,并改进那些感到不快的翻译。 新鲜的眼球接住了很多。

翻译几个字符串开始。 短者宜温.

> [!TIP]
> 不知道弦是什么意思吗? 看看它的钥匙 像`component::wled::config::step::user::description`这样的密钥告诉你,它是WLED集成的第一个设置步骤的描述. 还不确定吗? 保留对字符串的评论而不是猜测 。

## 当心占位符 {#4-watch-out-for-placeholders}

有些字符串包含卷曲括号之间的部分,如`{count}`,或置于方括号内. 不要翻译这些名称 : Home Assistant 在运行时填写它们 。 例外是复数或选择,如`{count, plural, one {

# device} other { {#5-see-your-work-in-home-assistant}

# devices}}`:保留其关键词,并在内括号内翻译文本. 解释他们是如何工作的。 {#what-is-next}

## 5.  在 Home Assistant 中看到你的作品 。 {#5-在-home-assistant-中看到你的作品-。}

当 Home Assistant 建成时, 翻译会从 Lokalise 中提取 。 没有单独的批准步骤, 也没有 pull request : 您在 Lokalise 中节省的就是 积分回收 。 当你看到它取决于项目:

- **Backend**: Home Assistant Core的每部作品都会下载这些内容,所以你的字符串在下一晚上的构建,àn牙的下一个β,以及下一个发行.
- **Frontend**:前端自建并发布,下载翻译此时. 夜间前端的建筑每天制造,夜间的建筑Home Assistant使用. β 或 Home Assistant 的释放 Home Assistant 的 ships 特定的 前端释放 , 所以你的字符串会用您保存它们后的第一个前端释放来达到它 。

有细节

同伴的应用工作有点不同. Android在构建时间也拉动翻译,而iOS应用程序则在存储器中通过每天的pull request获取翻译.

## 接下来是什么 {#接下来是什么}

- 读[翻译规则](/translate/reference/rules). 它们很短。
- 检查是否有[语言指南](/translate/reference/languages), 如是正式或非正式地对人们讲话 。
- 加入另一个项目。 后端项目有很多字符串,经常需要帮助.
