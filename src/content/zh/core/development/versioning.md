---
title: 版本
description: Home Assistant Core版本是如何建立起来的,从稳定的发行到β,夜客,以及开发版本.
sidebarGroup: 改变行为
order: 2
---



# 版本 {#versioning}
取得的进步 一个取得的进步包括三个部分:

```text
YYYY.MM.PATCH
```

| 编 | 含义 |
| --- | --- |
| `YYYY` | 释年,如`2026`. |
| `MM` | 发行的月份,没有领先的零:`5`,不是`05`. |
| `PATCH` | 该补丁在该月内发布,从`0`开始. |

因此`2026.5.0`是2026年5月的发布,`2026.5.1`和`2026.5.2`是它的补丁发布. 关于发行时间表和发行渠道,参见[释放 FAQ](https://www.home-assistant.io/faq/release/).

## 贝塔、夜客和开发版本 {#betas-nightlies-and-development-versions}

版本跟随[PEP 440 (英语).](https://peps.python.org/pep-0440/),所以补丁部分可以携带一个不稳定的建筑的后缀:

| 温柔 | 格式 | 示例 |
| --- | --- | --- |
| 稳定释放 | `YYYY.MM.PATCH` | `2026.5.0` |
| 贝塔 | `YYYY.MM.PATCH` + `b<N>` | `2026.5.0b0` |
| 夜来 | `YYYY.MM.PATCH` + `.dev<YYYYMMDDHHMM>` | `2026.7.0.dev202607241254` |
| 联合国 | `YYYY.MM.PATCH` + `.dev<N>` | `2026.7.0.dev0` |

## 版本所在之处 {#where-the-version-lives}

版本设定为[`homeassistant/const.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/const.py),在`MAJOR_VERSION`,`MINOR_VERSION`和`PATCH_VERSION`常数中. `dev`分支总是将下一次发行作为开发版本,就像`2026.7.0.dev0`.

该版本不来自标签或日期. 它被故意撞了,有[`script/version_bump.py`](https://github.com/home-assistant/core/blob/dev/script/version_bump.py),知道如何移动到下一个`minor`,`patch`,`dev`,`beta`,或`nightly`版本. 将第一个β切变 `2026.7.0.dev0` 变为 `2026.7.0b0` , 释放会减少后缀 : `2026.7.0`.

## 比较版本 {#comparing-versions}

当您的代码需要根据 Home Assistant 的版本进行不同的行为时, 请将版本与 [厉害的版本](https://github.com/ludeeus/awesomeversion) 相比较 。 不要自己分析字符串:βs,开发版本,和补丁发布必须正确排序,这很容易出错.
