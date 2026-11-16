---
title: 卫星 Assist
description: 用于监听语音指令并将其发送到Home Assistant的设备,比如Home Assistant Voice预览版.
sidebarGroup: 语音
term:
  aliases:
  - voice satellite
  - satellite
  - satellites
  code:
  - assist_satellite
  - AssistSatelliteEntity
  related:
  - assist
  - assist-pipeline
  - wake-word
  autolink:
  - Assist satellite
  - Assist satellites
  - voice satellite
  - voice satellites
---

# 卫星 Assist {#assist-satellite}

- 代码:`assist_satellite`,`AssistSatelliteEntity`
- 还:语音卫星、卫星、卫星

卫星不了解命令本身。 它经常为[唤醒消息](/glossary/wake-word)聆听,将音频流到Home Assistant,并播放答案. 每个卫星都使用一个{ 确实知道它所在的区域 所以"打开灯"在你所在的房间

在Core中,卫星是`assist_satellite`型的实体. 见[Assist 卫星实体](/core/entities/assist-satellite).

## 相关条件 {#related-terms}

- [Assist](/glossary/assist): Home Assistant的语音助理. 它把你说的话或者打字变成行动
- [输油管](/glossary/assist-pipeline):一个语音命令的步骤会经过:醒字,语音到文字,对话代理,以及文字到语音.
- [唤醒你](/glossary/wake-word):使语音助理开始听话的词或编拟短语,如"OK Nabu".
