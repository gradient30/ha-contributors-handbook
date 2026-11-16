---
title: 哈克斯. 贾森
description: 在您的仓库根部的 hacs. json 文件的每个密钥, 哪些 HACS 文档, 以及 Complace 如何处理它 。
order: 1
---

# 哈克斯. 贾森 {#hacsjson}

`hacs.json` 向 Marketplace 和HACS 描述您的仓库 。 它坐落在您的寄存器的根部,每个寄存器都需要一个: 市场网为其安装的每个版本读取它,没有它就不能安装或更新一个寄存器.

```json title="hacs.json"
{
  "name": "My awesome card",
  "filename": "my-awesome-card.js",
  "homeassistant": "2026.11.0"
}
```

## 键 {#keys}

| 密钥 | 类型 | 它会做什么 |
| --- | --- | --- |
| `name` | 字符串 | 名字使用者见. 按HACS和目录的要求。 没有它, 市场会显示 `name` 从一个合并的表, 或从您的仓库名称中产生的名称 。 |
| `content_in_root` | 布尔 | 您的内容位于寄存器的根, 而不是 `custom_components/<domain>/` 或 `themes/` 。 对于一个仪表板插件,则文件只在根中查找,而不是在发布或`dist`中查找. |
| `filename` | 字符串 | 要 为了一个仪表板插件或模板而安装的文件名称.  为了 `zip_release` , ZIP 资产的名称 。 需要模板 。 |
| `zip_release` | 布尔 | 从每个发布时附加的 ZIP 文件安装, 由 `filename` 命名 。 HACS 只支持集成, 市场拒绝它为模板 。 |
| `persistent_directory` | 字符串 | 一个保存在全更新的集成内部的文件夹, 作为相对于集成文件夹的路径 。 仅限融合. |
| `homeassistant` | 字符串 | 此发行的最小 Home Assistant 版本, 如 `"2026.11.0"` 。 添加`b0`, 和`"2026.11.0b0"`一样, 允许释放的β 。 只检查有释放物的仓库。 |
| `hide_default_branch` | 布尔 | HACS 不提供默认分支作为安装的版本. |
| `hacs` | 字符串 | 最小 HACS 版本 。 "市场"读了,但并不比较. |
| `country` | 字符串或列表 | 双字母国家代码([ISO 3166-1 α-2 标准](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)),用于仅在一些国家起作用的寄存器. 该目录要求它在这种情况下。 市场不使用它。 |

Marketplace 省掉了一个带有错误类型值的密钥, 并记录一个警告 。 其他密钥被忽略 。

## 版本 {#versions}

`homeassistant`和`hacs`中的版本编号被比较为[厉害的版本](https://github.com/ludeeus/awesomeversion),同样的库Home Assistant使用. [真棒Version演示](https://awesomeversion.ludeeus.dev/) 显示两个版本如何比较 。

## 资料来源 {#sources}

- 在 `marketplace` 的 `REPOSITORY_MANIFEST_VALUES` 中,
- 什么 HACS 文档 : [哈克斯.杰森区](https://hacs.xyz/docs/publish/start#hacsjson) 的 HACS 发布文档 。
