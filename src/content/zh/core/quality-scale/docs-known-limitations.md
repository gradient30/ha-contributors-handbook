---
title: 已知限制文件
description: Gold rule docs - 众所周知的限制:文档列出了已知的限制.
sidebarLabel: 已知文件限制
sidebarGroup: 金
order: 7
---

# 已知限制文件 {#document-known-limitations}

这是黄金规则 在`quality_scale.yaml`中,它被称为`docs-known-limitations`.

[Home Assistant.io](https://www.home-assistant.io/)上的集成页面列出了集成通过设计或由于设备或服务而不能做或不能做好事. 限制不是错误:错误属于GitHub上的问题跟踪器,而不是文档中.

## 为什么这很重要 {#why-it-matters}

用户迟早会发现某种限制. 从文档中查找,在他们购买设备或者在自动化上度过一个晚上之前,比从失败的尝试中查找一个像"如意的工作"一样被关闭的问题要好得多.

在限制方面居于前列也省下你支持的问题。

## 示例 {#example}

```markdown
## Known limitations {#known-limitations}

- The integration cannot reboot the device. Use the app of the
  manufacturer for that.
- The cloud API updates the energy usage once per hour, so the energy
  sensors lag up to an hour behind.
```

参见 [写入集成文件](/writing/guides/integration) 和 [整合页面结构](/writing/reference/integration-page) 。

## 如何检查 {#how-it-is-checked}

在审查中检查过,通常在文件pull request上.

## 例外 {#exceptions}

如果合并没有已知的限制,则不适用这一规则。
