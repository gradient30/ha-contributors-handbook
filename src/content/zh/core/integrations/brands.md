---
title: 一体化品牌和形象
description: 添加您集成的图标和标志,以及一个品牌的组装,让用户找到它们.
sidebarGroup: 参考
order: 2
---

# 一体化品牌和形象 {#integration-brands-and-images}

Home Assistant 显示每个集成的图标和标志 。 图标为正方形,用于空间紧凑的地方.吝啬的标志较宽,在有空间的地方使用,如整合的页面. 两者都是光明和黑暗的版本。

品牌是另外一件事情:一个品牌文件将一个公司的多个集成组合,因此用户发现它们都以一个名称命名.

本页面介绍集成品牌:公司和产品Home Assistant连接. Home Assistant本身的品牌,它的个性,名称,和标志,都有自己的区域:[品牌](/brand).

## 核心集成的品牌图像 {#brand-images-for-core-integrations}

核心中集成的图像活在 [品牌存储器](https://github.com/home-assistant/brands) 中,而不是 [核心存储器](https://github.com/home-assistant/core) 中. 打开 pull request 在 [`core_integrations/`](https://github.com/home-assistant/brands/tree/master/core_integrations) 中添加以您的域名命名的文件夹 。 Philips Hue集成的图像在[`core_integrations/hue/`](https://github.com/home-assistant/brands/tree/master/core_integrations/hue)中.

一个文件夹可以保存这些文件 :

| 文件 | 这是什么 |
| --- | --- |
| `icon.png` | 方块图标 |
| `icon@2x.png` | 高分辨率屏幕图标 |
| `logo.png` | 标志 |
| `logo@2x.png` | 高清屏幕的标志 |
| `dark_icon.png`,`dark_logo.png`, 及其`@2x`版本 | 只在需要时, 才会对黑暗背景进行优化 |

缺少的文件倒回去:一个缺失的标志使用图标,一个缺失的黑暗版本使用光线. 如果一个品牌的标志是正方形的,只添加图标.

这些图像必须萌芽这些要求:

- PNG,为网络适当压缩. 更喜欢无损失和间隙。
- 最好有一个透明的背景。 白背景的图像为默认,`dark_`版本为暗背景.
- Trimmed:没有空位,边框,或围绕主题铺设.
- 图标为正方形:256乘256像素,512乘512像素为`@2x`.
- 标志保持品牌标志的尺寸比,最好是景观. 最短的一面是128到256像素,256到512像素为`@2x`. 更大的范围是更好的。

图像是缓存的,所以合并后的更改需要一段时间才能出现.

### 没有品牌的整合 {#integrations-without-a-brand}

一些整合,如帮手,没有品牌可展示. 而不是图像, 在文件夹中添加一个 `icon.txt` 文件, 名称为 [材料设计图标](https://pictogrammers.com/library/mdi/), 如 `mdi:calculator` 。

### 与品牌共享的图像 {#images-shared-with-a-brand}

如果一个公司的品牌使用与其集成之一相同的图像,将图像放入`core_brands/<brand>/`并把它们与集成文件夹连在一起,以避免复制. 三星电视集成以这种方式与三星品牌的画面连接. 只允许在核心集成和品牌的域文件夹之间实现共联.

## 自定义集成的品牌图像 {#brand-images-for-custom-integrations}

自 Home Assistant 2026.3 起, 自定义集成船本身的图像, 在集成文件夹内的 `brand/` 文件夹中: `custom_components/my_integration/brand/`. 在此之前,自定义集成也将其图像添加到品牌存储器中. 本地图像优先于品牌存储库中的任何图像.

如果您稍后向核心贡献集成,请移除`brand/`文件夹,将图像添加到品牌寄存器中. 自定义集成不得使用Home Assistant品牌图像,因此用户不会误认为是正式集成.

## Home Assistant 如何为图像服务 {#how-home-assistant-serves-the-images}

Home Assistant通过自己的API服务品牌图像,来源与前端相同:

- `/api/brands/integration/{domain}/{image}` 用于集成图标和标志
- `/api/brands/hardware/{category}/{image}` 用于硬件图像

这些端点需要认证,要么是普通认证的会话,要么是`token`查询参数中的访问令牌. 前端以 `brands/access_token` WebSocket 命令获得此令牌, 并为您添加 。 如果图像不存在,则端点返回占位符图像。 添加 `?placeholder=no` 换成 404 。

## 品牌文件 {#brand-files}

一个公司可以为不同的产品进行若干次整合. Google有`google`用于Google日历,`google_sheets`用于Google工作表. 公司也可以制作使用像Zigbee这样的标准的设备,而无需自己进行整合. 一个品牌文件组这些,所以用户在品牌名下找到它们.

品牌文件在核心寄存器 [`homeassistant/brands/`](https://github.com/home-assistant/core/tree/dev/homeassistant/brands)中直播,每个品牌有一个JSON文件:

```json
{
  "domain": "google",
  "name": "Google",
  "integrations": ["google", "google_sheets"]
}
```

```json
{
  "domain": "inovelli",
  "name": "Inovelli",
  "iot_standards": ["zigbee", "zwave"]
}
```

| 密钥 | 这是什么 |
| --- | --- |
| `domain` | 品牌的独特领域. 它必须匹配文件名 。 |
| `name` | 品牌名称 |
| `integrations` | 这个品牌整合的领域. 如果一个集成与品牌拥有相同的域名,则必须在本列表中. |
| `iot_standards` | 此品牌使用的标准设备: `homekit`,`matter`,`zigbee`,或`zwave` |

一个品牌至少需要两个集成,或者至少一个IOT标准. 否则,没有什么可分组的。 一个品牌的图像在品牌库的`core_brands/<domain>/`中。
