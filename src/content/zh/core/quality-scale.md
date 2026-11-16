---
title: 集成质量等级
description: 说明融合有多好、融合如何获得分级以及如何提高分级的规则。
order: 30
sidebarGroups:
- 铜
- 银
- 黄金
- 铂
---

# 集成质量等级 {#integration-quality-scale}

Home Assistant有上千个融合, 由上千人写成。 集成质量尺度是项目如何用一个字来描述每个集成的质量:青铜,银,金,或白金. 每个层次都是具体规则的清单,一体化通过遵循该层次及其下层的每一个规则而获得一个层次。

> [!TIP]
> 努力进行整合? 从 [所有规则](/core/quality-scale/rules) 开始: 一页上每分级的每条规则, 并用一行要求的内容, 以及一个复制到您的 pull request 的检查表 。

## 为什么有尺度 {#why-there-is-a-scale}

对于用户来说,分级是一个承诺. 他们在文件和** 安置** 的整合网页上看到这一点。 ** 设备和服务**。 青铜器集成从UI中设置并有测试. 在网络上发现了一个Gold集成,可以重新配置,有翻译名称和错误,并带有告诉你哪些设备有效的文档. 用户根据这个选择设备,所以等级必须诚实.

对于你作为一个贡献者来说,比例表是"done"的共同定义. 与其说是评论员个人的品味,不如说有一条有背后原因的书面规则. 您知道在打开 pull request 之前的预期是什么, 在您想要改进整合时您知道下一步的工作是什么 。

对于维护者和审查者来说,它保持了数千项整合的一致性。 部分通过工具对声称有规则的合并进行核对,这些合并在代码库前进时可以依赖。

## 工作原理 {#how-it-works}

- 整合的层次是 `quality_scale` 中的 `manifest.json` 键 。 许多年长的融合从未分级,也没有分级。 新的一体化必须有一个。
- 与分级的集成还有一个 `quality_scale.yaml` 文件 。 它列出每个规则及其状态:`done`,`todo`,或`exempt`有原因.
- Hassfest,核核的验证脚本,检查文件。 当一个规则认为第一级需要的不是`done`或`exempt`时它会失败,它会额外检查一些标记为`done`的规则.
- 一名审查员检查其余部分,一名核心团队成员批准新的层级。

新的融合必须到达青铜器. 根本无法进入核心

## 从这里开始 {#start-here}

1. [等级](/core/quality-scale/tiers):青铜器,银器,金器,和白金的意思,以及天秤以外的阶梯,如内部和遗产.
2. [所有规则](/core/quality-scale/rules): 一页的每条规则,每层都有一份核对表,可以复制到您的pull request。 这就是你找到 做什么。
3. [提高一体化水平](/core/quality-scale/raise-tier):如何提高你的工作水平,如何检查你的工作,以及如何让新的级别审查。
4. [质量尺度文件](/core/quality-scale/quality-scale-file): `quality_scale.yaml`的格式, 以及检查它的一切 。

构建新融合? 它需要尉迟到 [青铜法则](/core/quality-scale/rules#bronze)。 {尉迟[教程](/core/integrations/tutorial)建立一个满足它们。

## 规则 {#the-rules}

每条规则都有自己的页面. [所有规则](/core/quality-scale/rules)每层列出它们,每个都有链接. 每页都解释规则问什么,为什么,如何执行,如何检查,何时不适用. 规则页使用与`quality_scale.yaml`相同的名称,因此`/core/quality-scale/entity-unique-id/`是`entity-unique-id`规则的页面.

### 铜 {#bronze}

基线:从UI设置,一个测试的配置流,独特的ID,和基本文档. 从 [配置流量](/core/quality-scale/config-flow) 开始, 或参见 [所有璞青铜器规则](/core/quality-scale/rules#bronze) 。

### 银 {#silver}

可靠性:处理错误和离线设备,再认证,拥有集成所有者,测试覆盖率超过95%. 从 [融合所有人](/core/quality-scale/integration-owner) 开始, 或参见 [所有十种银本位规则](/core/quality-scale/rules#silver) 。

### 黄金 {#gold}

最佳用户经验:发现、设备、翻译、诊断、修理和用户完整文件。 从 [设备](/core/quality-scale/devices) 开始, 或参见 [所有21金规则](/core/quality-scale/rules#gold) 。

### 铂 {#platinum}

技术优异:ASync依赖,共享网络会话,严格打字. 从 [严格打字](/core/quality-scale/strict-typing) 开始, 或参见 [所有3个白金规则](/core/quality-scale/rules#platinum) 。

## 相关页面 {#related-pages}

- 得不错。
- [写作测试](/core/development/tests):若干规则要求的测试.
- [写入集成文件](/writing/guides/integration):文档规则是关于[Home Assistant.io](https://www.home-assistant.io/)上的集成页面.
- [让你的弦可变](/translate/guides/developers):用于翻译规则.

## 谁说话 {#who-to-talk-to}

- 在 [Home Assistant Discord](https://www.home-assistant.io/join-chat/) 上的 [编码支持**](https://discord.com/channels/330944238910963714/1257019582112334014) 线条中询问一条规则, 或者豁免是否合理 。
- 汶上集成物的整合所有者,在其`manifest.json`中列为`codeowners`,最清楚其位置. 在您的pull request 中提及它们 。
- 其後是"國民主義","國民主義","國民主義","國民主義","國民主義","國民主義","國民主義","國民主義","國民主義","國民主義","國民主義","國民主義","國民主義","國民主義","國民主義"等.
