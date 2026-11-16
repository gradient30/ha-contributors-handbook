---
title: 唤醒你
description: 使语音助理开始听话的词或短语,如"OK Nabu".
sidebarGroup: 声音
term:
  aliases:
  - wake words
  - wake word detection
  code:
  - wake_word
  ui: 唤醒你
  related:
  - assist-pipeline
  - assist-satellite
  - assist
  autolink:
  - wake word
  - wake words
---

# 唤醒你 {#wake-word}

- 代码 : `wake_word`
- (原始内容存档于2017-03-21). In the UI: Wake word
- 还有 33. 醒字 醒字探测

检测唤醒词是[输油管](/glossary/assist-pipeline)的第一步。 它在Home Assistant中发生,与`wake_word`的集成和像开WakeWord一样的引擎,或者在设备本身上发生,比如在ESP32或Android手机上的微WakeWord. 只有在唤醒字之后,其他命令才会得到处理.

## 相关条件 {#related-terms}

- [输油管](/glossary/assist-pipeline):一个语音命令的步骤会经过:醒字,语音到文字,对话代理,以及文字到语音.
- [卫星 Assist](/glossary/assist-satellite):一个听声音命令并发送到Home Assistant的设备,如Home Assistant Voice预览版.
- [Assist](/glossary/assist): Home Assistant的语音助理. 它把你说的话或者打字变成行动
