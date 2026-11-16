---
title: 记录数据更新情况
description: Gold Rules docs-data-update:文档解释数据更新的方式和频率.
sidebarLabel: 文档数据更新
sidebarGroup: 黄金
order: 5
---

# 记录数据更新情况 {#document-how-data-is-updated}

这是黄金规则 在`quality_scale.yaml`中,它被称为`docs-data-update`.

[Home Assistant.io](https://www.home-assistant.io/)上的集成页面解释了集成是如何获得其数据的:它是否对设备或服务进行投票,以及多久一次,或者设备是否推动更新. 如果有限制,比如一个每天只允许多个请求的API,或者一个与频繁请求有冲突的设备,页面就这么说了.

## 为什么这很重要 {#why-it-matters}

如何更新数据决定一个用户对集成能做什么. 每5分钟检查一次的动作传感器 当有人走进来时打开灯是没用的. 推其状态的感应器是最适合它的. 用户在购买设备或在上面建立自动化设备之前,需要知道这一点.

用户可以设定自己的投票间隔,因此他们也需要知道默认,以及不下降的原因.

## 示例 {#example}

在整合页面中加入"数据更新"部分:

```markdown
## Data updates {#data-updates}

The integration {% term polling "polls" %} the device every 5 minutes.
Devices with firmware 2.0 or newer can push their data instead. The
integration turns that on when it starts, and only falls back to polling
when it fails.

The cloud API allows 1,000 requests per day. Polling more often than every
2 minutes can get your account blocked for the rest of the day.
```

参见 [写入集成文件](/writing/guides/integration) 和 [整合页面结构](/writing/reference/integration-page) 。

## 如何检查 {#how-it-is-checked}

在审查中检查过,通常在文件pull request上.

## 例外 {#exceptions}

如果集成没有从一个设备或服务获得数据,因为它既没有进行民意测验,也没有收到更新,则本规则不适用.
