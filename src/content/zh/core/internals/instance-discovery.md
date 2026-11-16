---
title: 案例发现
description: Home Assistant如何用Zeroconf在本地网络上宣布自己,所以应用程序可以在不要求地址的情况下找到它.
sidebarGroup: API
order: 32
---

# 案例发现 {#instance-discovery}

Home Assistant在本地网络上宣布自己为 mDNS (Zeroconf) 服务 `_home-assistant._tcp.local.`. Apps,和同伴的app一样,浏览该服务查找实例而不要求用户输入地址.

`zeroconf`整合,默认配置的一部分,一旦建立`frontend`整合,或当Home Assistant启动,就会公布记录. 到那时,HTTP服务器已经上架,所以唱片中的地址是起作用的.

## 服务记录 {#the-service-record}

| 外地 | 数值 |
| --- | --- |
| 服务类型 | `_home-assistant._tcp.local.` |
| 实例名称 | `<location_name>._home-assistant._tcp.local.`. 位置名称中的点被替换为空格,并且该名称被切换以符合一个DNS标签的63字节限制. 若取名,则Zeroconf增加后缀. |
| 东道主 | `<uuid>.local.`,其中`<uuid>`是实例 ID。 |
| 端口 | HTTP 服务器的端口:默认情况下为8123个,或当 Home Assistant 与 Supervisor 运行时为80个, 如 Home Assistant OS 上. `SETUP_PORT` 环境变量覆盖默认值 。 |

## TXT 属性 {#txt-properties}

| 财产 | 含义 |
| --- | --- |
| `location_name` | 实例的名称, 从 `hass.config.location_name` 或 `Home` 如果没有设置 。 它与实例名称中的清理名称相同:点被空格取代,切成63字节。 |
| `uuid` | 实例ID:一个稳定,不透明的标识符,由32个十六进制字符组成,在第一次运行时创建. 用它来识别一个你以前见过的例子, 即使它的地址有变化。 |
| `version` | Home Assistant Core的版本 。 |
| `internal_url` | 如果 {H0在需要时} 本地网络的 URL 会知道一个 。 否则空. |
| `external_url` | 网络外的 URL, 如果 Home Assistant 知道 。 否则空. |
| `base_url` | 折旧,为老年客户保留. 外部 URL,或者如果没有外部 URL 。 |

TXT值可能最多为230字节. Home Assistant 用空字符串替换一个更长的值, 因此一个长的 URL 不中断整个通知 。

## 在安装核心之前 {#before-core-is-installed}

在第一次设置Home Assistant OS期间,[登陆页面](https://github.com/home-assistant/landingpage)运行而不是核心,并宣布相同的服务类型. 它的记录中有一个 `landingpage` 属性设定为 `True` , 和一个 `0000.0.0` 的 `version` , 这不是真实的版本 。 运行中的核心从未设置 `landingpage` 。 将缺失或占位符 `version` 当作未知 。

旧记录也可能携带`requires_api_password`. 它指的是在Home Assistant中被移除的一种认证方法. 2024.7,核心不再发送. 别管它。
