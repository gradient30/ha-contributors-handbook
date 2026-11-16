---
title: 图像和录像
description: ط迥各种各样          陀 Srebrenica        共同努力
order: 2
---

# 图像和录像 {#images-and-videos}

一个好的截图可以保存一段解释. 视频可以显示一些无法表达的东西。 这个页面覆盖图像去的地方,如何将它们添加到一个页面,以及如何嵌入一个视频.

## 图像所在的地方 {#where-images-live}

将每个图像存储在文档仓库中, 在 [`source/images`](https://github.com/home-assistant/home-assistant.io/tree/current/source/images) 下 。 选择匹配页面的子文件夹 :

- `source/images/integrations/<domain>/`像[`source/images/integrations/matter/`](https://github.com/home-assistant/home-assistant.io/tree/current/source/images/integrations/matter)一样的集成。
- 用于一般文件。
- [`source/images/dashboards/`](https://github.com/home-assistant/home-assistant.io/tree/current/source/images/dashboards)用于仪表板和卡片。

不与其它地点主播的图像链接, 如您自己的 GitHub 寄存者 或 图像托管服务 。 外部图像消失,更改,或将页面减慢.

在页面上,参考图像以其公布的路径. 这是没有 `source` 的路径, 因此 [`source/images/integrations/matter/matter_device-info.png`](https://github.com/home-assistant/home-assistant.io/blob/current/source/images/integrations/matter/matter_device-info.png) 变成 `/images/integrations/matter/matter_device-info.png` 。

> [!NOTE]
> GitHub 上的 ** Edit ** 按钮不允许您上传图像 。 要添加图像,请先在自己的机器上或在GitHub上将文件上传到叉上,在叉上工作. 见[本地预览网站](/writing/guides/local-preview).

## 添加图像 {#add-an-image}

使用 Markdown 图像, 您可以在任何地方 :

```markdown
![Screenshot of the tile card with a brightness slider](/images/dashboards/features/screenshot-tile-feature-grid.png)
```

一个图像也可以说明一个步骤。 缩进所以属于列表项:

```markdown
1. To adjust the brightness, move the slider:
   ![Screenshot of the tile card with a brightness slider](/images/dashboards/features/screenshot-tile-feature-grid.png)
2. Select **Save**.
```

## 添加标题 {#add-a-caption}

Markdown 没有标题语法 。 要在图像下方显示一个标题, 请用 `img` 类包裹它, 并将标题文本放在图像之后 :

```html
<p class='img'>
  <img
    src='/images/dashboards/features/screenshot-tile-feature-grid.png'
    alt='Screenshot of the tile card with a brightness slider'
  >
  The tile card with a brightness slider
</p>
```

图像和标题然后得到一个框框、中心布局,标题用斜体表示。

## 黑暗模式和反向 {#dark-mode-and-invertdark}

将 `invertDark` 类添加到图像中, 当页面以暗模式显示时, 其颜色应该反转 。 这意指在透明或白色背景上带有暗线的简单图和图. 不要用在截图或照片上:颠倒那些会让他们看起来不对.

```html
<p class='img'>
  <img
    class='invertDark'
    src='/images/integrations/infrared/infrared-overview.png'
    alt='Diagram of how commands reach a device through an infrared adapter'
  >
  How commands reach an infrared device
</p>
```

> [!NOTE]
> [Home Assistant.io](https://www.home-assistant.io/) 现在没有暗模式,它的样式表还没有定义`invertDark`,所以该类今天没有明显的效果. 几页都用过了

## 灯盒 {#the-lightbox}

在home-assistant.io上,读者可以在文档页面或博客帖子中选择一个图像,以在灯盒中打开一个完整的大小. 也与键盘配合. 您无需为此做任何事情: 图像自动获得灯盒, 除非:

- 这是小的。 显示小于160的图像乘以100像素,而原大小也小于300像素的图像会被跳过. 这使得图标内置。
- 它是一个链接或坐落在链接或按钮内。
- 这是一个SVG文件。
- 它看起来像一个标志。 品牌标志被跳过,基于他们的类,一条包含像 `logo` 或 `brand` 这样的单词的路径,或者提到标志的备选案文.
- 选择退出。

要从灯盒中选择一个图像,请添加`data-no-lightbox`属性或`no-lightbox`类。 你可以在图像本身上,或者在它周围的一个元素上,选择出一组完整的图像:

```html
<img
  src="/images/example.png"
  alt="Description of the image"
  data-no-lightbox
>
```

```html
<img
  class="no-lightbox"
  src="/images/example.png"
  alt="Description of the image"
>
```

## 写好备选案文 {#write-good-alt-text}

每个图像都需要备选案文。 屏幕阅读器大声读出来,它显示图像无法加载时. 换文本也是灯盒打开图像时所宣布的内容.

- ** 说明图像显示的内容,** 并说明为何存在。 "整合设置的截图,投票间隔设定为30秒"有帮助. "史记"没有.
- ** 保持简短。 ** 一个句子通常就够了。
- ** 不要从“形象”开始。 ** 屏幕阅读器已经宣布这是一个图像。 "Screenshot of"或"diagram of"是好的,因为它告诉读者它是什么形象.
- ** 不重复标题。 ** 如果标题已经全部说明,则备选案文可以描述视觉细节。
- ** 不只将信息放在图像中。 ** 任何读者需要完成一步的东西也属于文本中.

## 保持截图有用 {#keep-screenshots-useful}

- 显示屏幕中重要的部分 。 把剩下的都收起来
- 使用默认的 [主题](/glossary/theme) 和 Home Assistant 的语言, 因此截图看起来像读者看到的 。
- 移除或模糊个人信息,如姓名,地址,令牌,以及IP地址.
- 替换不再匹配界面的截图 。 一个过时的截图会比没有截图更混淆.

## 嵌入YouTube视频 {#embed-a-youtube-video}

使用`lite-youtube`元素嵌入一个YouTube视频. 它首先显示一个轻量级预览,只有在读者开始视频时才加载实际的YouTube播放器. 这让页面保持了快速。

```html
<lite-youtube
  videoid="ZgoaoTpIhm8"
  videotitle="Introducing the Home Assistant Voice Preview Edition"
></lite-youtube>
```

- `videoid`是继`watch?v=`之后的YouTube URL的一部分. 对`https://www.youtube.com/watch?v=ZgoaoTpIhm8`,即`ZgoaoTpIhm8`。
- `videotitle`是视频的标题。 屏幕阅读器使用它,所以总是添加.
- `videoStartAt` 在特定时刻开始播放, 以秒计 。 当只有部分长视频相关时使用.

例如,上面的视频以1小时5分7秒开始:

```html
<lite-youtube
  videoid="ZgoaoTpIhm8"
  videoStartAt="3907"
  videotitle="Introducing the Home Assistant Voice Preview Edition"
></lite-youtube>
```

要在视频下面添加一个标题狒ẽ, 请用 {缇H0} 类, 与 [图像标题](/writing/reference/images#add-a-caption) 相同向受害者提供一个段落 :

```html
<p class='img'>
  <lite-youtube
    videoid="ZgoaoTpIhm8"
    videoStartAt="3907"
    videotitle="Introducing the Home Assistant Voice Preview Edition"
  ></lite-youtube>
  Watch the Voice Preview Edition announcement
</p>
```

视频从不取代书面步骤. 不是每个人都可以看视频,文本更容易扫描和翻译.
