---
title: 使用透明的依赖关系
description: 青铜规则依赖性-透明性:依赖性是开源的,在PyPI上,在公共CI中建立并发布.
sidebarLabel: 依赖透明度
sidebarGroup: 青铜
order: 7
---

# 使用透明的依赖关系 {#use-transparent-dependencies}

此是铜法. 在`quality_scale.yaml`中,它被称为`dependency-transparency`.

每个 Python 包 集成依赖于, 其 [所需经费](/glossary/requirement) 符合这些要求 :

- 依据《公约》第22条第1款(a)项
- 该套件发布在PyPI上.
- PyPI上的包由公共CI管道建造并发布.
- PyPI上每个版本都匹配公共寄存器中标记的发布.

## 为什么这很重要 {#why-it-matters}

Home Assistant将每个集成的依赖性 传送给每个用户,每个发布。 项目必须能够信任他们。 当源头打开时,建筑是公开的,并且每个发行版都有标记,任何人都可以看到几百万个系统最后的代码,以及它是如何到达那里的. 一个用人手电脑制成的软件包不能提供。

## 怎么办 {#what-to-do}

通常,依赖是一个对设备或服务说话的库,您自己写或者贡献给一个已有的库:

- 在公共寄存器中发布源,持有OSI批准的许可,如MIT或Apache 2.0.
- 从 CI 释放, 例如使用 GitHub 动作工作流程构建软件包,并在发布发行时发布到PyPI. PyPI信任的出版使得这一点变得直截了当.
- 标记寄存器中的每一版,版本与PyPI相同.

然后在 `manifest.json` 的 `requirements` 中将准确的版本钉上, 如 `"requirements": ["mylibrary==1.2.3"]` 。

## 如何检查 {#how-it-is-checked}

- Hassfest要求核心集成的每一项要求都要被固定在准确版本的`==`上.
- CI审计所有要求的许可证,如果找不到OSI批准的许可证,则失败,除非包在[`script/licenses.py`](https://github.com/home-assistant/core/blob/dev/script/licenses.py)核心中已知的例外的短清单中。
- 将检查该包是否建在公开的CI中,并匹配标记的释放。 链接到您的 pull request 中的发布工作流程和标签 。

## 例外 {#exceptions}

如果整合没有任何外部依赖性,则该规则不适用.

## 相关规则 {#related-rules}

- [关联依赖性](/core/quality-scale/async-dependency) : 使用同步依赖 。
