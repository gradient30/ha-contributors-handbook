---
title: 标记卡
description: Markdown卡显示用Markdown写成的文本,作为模板提供,因此可以将固定文本与活状态混合.
sidebarGroup: 信息
---

# 标记卡 {#markdown-card}

盘 联卡的现场演示,从Home Assistant演示的嵌入,连接到这个站点的样本主场.

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "markdown",
        "title": "Welcome home",
        "content": "The **laundry** is almost done.\nDinner is at **seven**, and the shopping list is on the fridge."
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用量 {#usage}

Markdown卡显示文本. 用于仪表盘上的注解,如欢迎信,客家规则,或设备旁边的指令. 由于内容是模板,它也可以将状态放入句子中,如"前门是封闭的,外面是12°C".

当言语比控制力更能表达时,就把它伸过来。 对于单个状态多名,[平板卡](/design/dashboards/tile-card)或[实体卡](/design/dashboards/entity-card)更清晰,当有人重命名实体时继续工作. 对于一组牌上方的标题,请使用[标题卡](/design/dashboards/heading-card),而不是带有大头的Markdown牌.

### 模板 {#templates}

内容发送到 Home Assistant 并作为模板提供, 每次 。 纸牌订阅结果,所以一旦模板中使用的状态发生变化,就立即更新. 这样的模板 :

```jinja
The front door is {{ states("binary_sensor.front_door") }}.
```

模板内,`config`持有卡的配置,`user`查看者的名字.

这个网站上的演示没有后面的Home Assistant来渲染模板,因此它们只显示平版马克当.

### 格式化 {#formatting}

这张卡让Markdown 与 Home Assistant 其余的一样. 内容中的单行折断是卡片上的单行折断. 在通常的Markdown旁边,前端工作的一些元素,如`<ha-icon>`,`<ha-alert>`和`<ha-qr-code>`. GitHub 提醒样式中的块引文成为提醒 。

盘 联卡的现场演示,从Home Assistant演示的嵌入,连接到这个站点的样本主场.

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "markdown",
        "content": "> [!TIP]\n> The guest Wi-Fi password is on the back of the router."
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

只允许一套安全的 HTML 。 维鲁佩尔·鲁佩尔·鲁佩尔(签名)

### 文本 {#text-only}

有了`text_only: true`,卡片没有背景,边框,或者阴影. 文字坐于仪表盘本身. 用于卡片之间的一行文字,如一节中的简短解释. 标题不在此模式中显示 。

盘 联卡的现场演示,从Home Assistant演示的嵌入,连接到这个站点的样本主场.

```html
<ha-embed-provider
  style="
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
    max-width: 500px;
  "
>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "markdown",
        "text_only": true,
        "content": "Lights in the garden turn on at sunset, and off at midnight."
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 动作 {#actions}

选择时卡不起作用, 除非你给它`tap_action` 。 然后整张卡成为按钮,带有波纹和指针光标. 例如,用它来导航到一个带有更多细节的视图. 不要同时在文字和卡片上放置链接和动作:人们无法知道会在哪里发生.

### 内容 {#content}

- 少顷. 一张牌不是一页,长的文字将控件推离屏幕.
- 写成完整的句子,将状态放入句子中,而不是原值列表.
- 使用 `show_empty: false` 当模板不能渲染任何东西时, 如提醒, 只有需要注意时才会显示 。 之后卡片会隐藏自己.

## 配置 {#configuration}

- `content` (字符串, 需要): 显示的 Markdown 。 以模板形式制作。
- `title`(字符串):卡片的标题. 未以 `text_only` 显示 。
- { {适合于  { 默认为 `false` 。
- `show_empty` (boolean): 当内容变成空时显示牌. 默认为 `true` 。
- `entity_id`(字符串或列表):更新模板的实体,用于Home Assistant无法确定它们使用的哪个实体的模板.
- `card_size`(编号):砖木景色中的卡片高度,单位为50像素. 默认为行数的一半。
- 5)),是属于该类,属于该类。
- `tap_action`,`hold_action`,`double_tap_action`(动作):选择,持有,或双拍卡时会发生什么. 默认为 `none` 。

```yaml
type: markdown
title: "Garden"
content: >
  The irrigation is **{{ states("valve.garden_irrigation") }}**,
  and it is {{ states("sensor.outdoor_temperature") }} °C outside.
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-markdown-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-markdown-card.ts),元素为`<hui-markdown-card>`. 它通过 `subscribeRenderTemplate` 从 [`src/data/ws-templates.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/ws-templates.ts) 制作内容, 并以 `<ha-markdown>` 显示结果, 与 `<ha-markdown>` 相同, 前端用于 Markdown 的其余部分 。 Markdown在网络工人 [`src/resources/markdown-worker.ts`](https://github.com/home-assistant/frontend/blob/dev/src/resources/markdown-worker.ts) 中解析和消毒,它也持有允许元素列表.

当模板出现错误时,卡片会在编辑卡片袂上方的提示中显示.

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-markdown-card.ts)
