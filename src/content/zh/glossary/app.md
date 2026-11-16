---
title: 应用
description: 在 Home Assistant OS 上运行于 Home Assistant 旁边的额外软件, 如 MQTT 经纪人或文件编辑器 。
sidebarGroup: 安装与系统
term:
  aliases:
  - apps
  code:
  - addons
  - config.yaml
  formerly:
  - add-on
  - addon
  related:
  - supervisor
  - home-assistant-os
  - companion-app
---

# 应用 {#app}

- 代码:`addons`,`config.yaml`
- 还有:应用程序
- 原名:add-on,加通(旧名:别在新文本中使用)

Apps曾被称为add-ons. 该代码仍然使用旧名,在Supervisor API,`config.yaml`密钥中,以及像home-assistant/addons这样的寄存器名称中. 在文本中,说应用。

不要与 [辅助应用程序](/glossary/companion-app) 的电话和电脑混淆 。

## 相关条件 {#related-terms}

- [Supervisor](/glossary/supervisor): Home Assistant OS中运行Home Assistant Core和apps的部分,各自在自己的容器内,并处理它们的更新和备份.
- [Home Assistant OS](/glossary/home-assistant-os):为运行Home Assistant而制造的操作系统,带有Supervisor,app,和备份. 建议安装Home Assistant的方法 。
- [辅助应用程序](/glossary/companion-app):Android,iOS和macOS的应用程序 Home Assistant. 它显示前端,并添加来自设备的传感器,通知和部件.
