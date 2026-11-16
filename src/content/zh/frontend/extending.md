---
title: 扩展前端
description: 是吗? 对前端的修改会与Core的修改一起进行,比如对新域的更多信息视图或对集成的WebSocket命令.
order: 40
---

# 扩展前端 {#extend-the-frontend}

有时Core的改变需要前端的新的东西:一个新的实体域需要控制,或者集成需要发送接口还没有的数据. 这些页面覆盖了这个的前端部分.

每个都是 pull request 到 [前端仓库](https://github.com/home-assistant/frontend) , 通常与 pull request 一起到 Core 。 在 pull request 模板中将两者链接起来, 因此审查人员可以看到整个画面 。 [审查和发布](/frontend/development/review-and-release#changes-that-need-the-backend)解释两者如何合并.

- [添加更多信息视图](/frontend/extending/more-info): 一个域的更多信息对话框中的控件 。
- [添加状态卡](/frontend/extending/state-card)并为显示实体及其状态的行 。
- [旨在使命令添加 WebSocket](/frontend/extending/websocket-api) : 将您的整合数据发送到前端 。

大多数一体化不需要这些。 现有域的实体已经获得其控制、卡片和更多信息视图。 查看设计区的[啊 更多信息视图](/design/more-info) 和[仪表板卡](/design/dashboards) 看那里有什么
