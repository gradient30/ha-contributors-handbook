---
title: 是
description: 鬓 应用程序在 Home Assistant 内, 在 Home Assistant 登录后显示其网页界面的方法, 不打开端口 。
sidebarGroup: 安装与系统
term:
  code:
  - ingress
  - ingress_port
  - ingress_panel
  related:
  - app
  - supervisor
  - panel
  autolink:
  - ingress
---

# 是 {#ingress}

- 在代码中:`ingress`,`ingress_port`,`ingress_panel`

一个应用以 {H0ắn} 在它的配置中打开, 并服务它的网络界面 在入侵端口, 8099 除非它设置另一个。 Supervisor 将请求传递到应用程序, 只针对登录到Home Assistant 的用户 。 使用 `ingress_panel` , app也会在侧边栏获得自己的 [面板](/glossary/panel) 。 见[添加一个带有入口的网页界面](/apps/guides/ingress)。

## 相关条件 {#related-terms}

- [应用](/glossary/app):在 Home Assistant OS 上运行于 Home Assistant 旁边的额外软件, 如 MQTT 经纪人或文件编辑器 。
- [Supervisor](/glossary/supervisor): Home Assistant OS中运行Home Assistant Core和apps的部分,各自在自己的容器内,并处理它们的更新和备份.
- [小组讨论会](/glossary/panel):在Home Assistant中它自己的一页,通常在侧边栏,像仪表板,地图,或设置.
