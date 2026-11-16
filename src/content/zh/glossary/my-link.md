---
title: 我的连结
description: 跟我的帮手联系 io,在读者自己的Home Assistant中打开一个页面,就像他们的集成,或者一个新的自动化.
sidebarGroup: 前端
term:
  aliases:
  - My Home Assistant
  - My links
  code:
  - my.home-assistant.io
  related:
  - integration
  - config-flow
  - blueprint
  - app
  - marketplace
  autolink:
  - My link
  - My links
---

# 我的连结 {#my-link}

- 代码 : `my.home-assistant.io`
- 还有:我的Home Assistant,我的链接

文档和集成使用我的链接将读者直接带到正确的地方,无论他们的Home Assistant运行在何处.

我的链接有表单 `https://my.home-assistant.io/redirect/<name>/` 。 有的取参数,如`https://my.home-assistant.io/redirect/config_flow_start/?domain=hue`,开始设置惠一体化. 每个链接在 `https://my.home-assistant.io/badges/<name>.svg` 中还有一个徽章图像, 用于 README 或论坛 的按钮 。 一些名称仍然使用前名, 如 `supervisor_add_addon_repository`, 它打开对话框来添加一个应用程序寄存器 。

[我的链接创造者](https://my.home-assistant.io/create-link/) 列出链接, 并为您构建链接和徽章 。 在捐助者使用的情况下:

- 在Home Assistant.io
- [与有关应用程序存储器添加的徽章](/apps/guides/repository#make-it-one-step)
- [连接到 Marketplace 的仓库](/marketplace/guides/catalog#the-link-to-your-repository)
- [设置定制集成的徽章](/marketplace/guides/integrations#link-to-the-setup)
- [蓝图导入徽章](/marketplace/guides/blueprints#share-it)

## 相关条件 {#related-terms}

- [一体化](/glossary/integration):将Home Assistant连接到设备,服务,或协议,或添加自动化等特性的代码包.
- [配置流量](/glossary/config-flow):UI中设置集成并创建配置条目的步骤.
- [蓝图](/glossary/blueprint):一个自动化,脚本,或模板实体,需要填充空白,所以其他人可以再利用它,就像一个只需要运动传感器和灯光的运动灯.
- [应用](/glossary/app):在 Home Assistant OS 上运行于 Home Assistant 旁边的额外软件, 如 MQTT 经纪人或文件编辑器 。
- [市场](/glossary/marketplace): Home Assistant中用户找到并安装社区定制集成,仪表盘卡,主题,模板宏的地方. 始建于2026.11路.
