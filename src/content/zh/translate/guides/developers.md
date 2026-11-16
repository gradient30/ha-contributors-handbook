---
title: 让你的弦可变
description: 对于向Home Assistant添加文本的开发者来说. 如何写出翻译可以合作的字符串.
order: 4
---

# 让你的弦可变 {#make-your-strings-translatable}

你加的每个字符串都最终会出现在64种语言的翻译面前. 照顾一下你 就能让他们多猜一猜

## 弦向何处去 {#where-strings-go}

- 在**整合**中,文本存在于`strings.json`,代码旁边. 它涵盖了设置流程,实体名称和状态,动作,错误,以及修复问题.
- 在**前端**中,文本存在于[`src/translations/en.json`](https://github.com/home-assistant/frontend/blob/dev/src/translations/en.json)中.

淑女: 永远不要将面对文字的用户直接放到代码中.淑女 无法翻译代码中的文本 。

## 写入前重用 {#reuse-before-you-write}

许多字符串已经存在,如"Device已经配置"或"连接失败". 常见字符串在核心 [`homeassistant/strings.json`](https://github.com/home-assistant/core/blob/dev/homeassistant/strings.json) 中存在 。 用一个参考点指着他们,而不是写你自己:

```json
{
  "config": {
    "abort": {
      "already_configured": "[%key:common::config_flow::abort::already_configured_device%]"
    }
  }
}
```

忆每一个再利用的字符串都是少一个字符串来翻译,在每种语言中.

## 为翻译撰写 {#write-for-translators}

- ** 值使用占位符**,永远不要粘合句子。 `"Found {count} devices"`可以翻译。 `"Found " + count + " devices"`不能,因为每个语言的词序不同.
- ** 前端适当使用复数。 ** 写 `{count, plural, one {

# device} other { {#test-your-strings}

# devices}}` 而不是“ 设备 ” 。 `strings.json` 中的集成字符串不要使用这个语法, 所以短语是它们为任意数字工作, 如“ 找到的代码 : { counts} ” 。 {#what-happens-after-merge}
- ** 名称占位符在所持位置后。 ** `{device_name}` 告诉翻译者多于`{name}` 。
- ** 整句保留。 ** 切勿将一句话与两个字符串分开。

## 测试您的字符串 {#测试您的字符串}

在核心中,编译您集成的字符串,以便在界面中看到它们. 将 `wled`的宗旨替换为您的整合域, 或使用 `--all` 每个整合域 :

```shell
python3 -m script.translations develop --integration wled
```

## 合并后会发生什么 {#合并后会发生什么}

一旦您的 pull request 合并, 新的英文字符串会自动上传到 Lokalise 。 译者从那里接来,译者随着工程的下一个建设到达,见[翻译如何返回](/translate/how-it-works#how-translations-get-back). 你不需要做别的事
