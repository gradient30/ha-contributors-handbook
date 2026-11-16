---
title: 显示卡片的现场演示
description: 在任何网页上嵌入工作仪表板卡,包括你自己的自定义卡,并带有被模拟的Home Assistant演示的后端.
sidebarLabel: 现场演示
order: 9
source: https://github.com/home-assistant/frontend/tree/dev/demo/src/embed
lastVerified: 2026-11-05
---

# 显示卡片的现场演示 {#show-a-live-demo-of-your-card}

2026-11-05最后一次核实,对https://github.com/home-assistant/frontend/tree/dev/demo/src/embed.

屏幕截图显示卡片的长相. 现场演示会显示它是如何工作的:人们可以打开灯光,移动滑动器,并看到其他的牌跟着. [显示 Home Assistant](https://demo.home-assistant.io/) 发布元素雁在任何网页上放置真实的仪表板卡, 如您的 README 网站或您的博客 。 它们运行在浏览器中的一个被嘲笑的后端,所以不需要Home Assistant服务器.

- `<ha-embed-provider>`持有被嘲笑的后端 及其实体。
- `<ha-embed-card>`制作一张卡片,后端是提供者。
- `<ha-embed-section>` 使一个区域, 或[战略](/frontend/custom-ui/strategy#a-section-strategy), 同样的方式。
- `<ha-embed-view>` 使一个视图、 [视图战略](/frontend/custom-ui/strategy#a-view-strategy) 或一个仪表板视图 。
- `<ha-embed-dashboard>` 制作一个仪表板, 或 [仪表板战略](/frontend/custom-ui/strategy#a-dashboard-strategy), 带有标签 。

同一供应商的所有卡都分享其实体。 当在一张卡片中更改一个实体时,另一张卡片会显示变化.

在这里试试:走廊的瓷砖和下面的自动调温卡 共用一个走廊的自动调温器。 改变瓦片中的目标温度或自动调温卡中的模式,其他卡则随行. 每张卡都有一个卡片特征. 外界温度的趋势图由演示从目前状态构成.

从 Home Assistant 演示的 若是 Home Assistant 的内嵌, 将显示仪表板卡进行现场演示 。

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
  <script type="application/json">
    [
      {
        "entity_id": "climate.hallway",
        "state": "heat",
        "attributes": {
          "friendly_name": "Hallway",
          "current_temperature": 19.5,
          "temperature": 21,
          "min_temp": 7,
          "max_temp": 30,
          "target_temp_step": 0.5,
          "hvac_modes": [
            "heat",
            "cool",
            "off"
          ],
          "supported_features": 1
        }
      },
      {
        "entity_id": "sensor.outside_temperature",
        "state": "12.3",
        "attributes": {
          "friendly_name": "Outside",
          "device_class": "temperature",
          "state_class": "measurement",
          "unit_of_measurement": "°C"
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 6">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "sensor.outside_temperature",
        "features": [
          {
            "type": "trend-graph"
          }
        ],
        "grid_options": {
          "columns": 6
        }
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 6">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "climate.hallway",
        "features": [
          {
            "type": "target-temperature"
          }
        ],
        "grid_options": {
          "columns": 6
        }
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "thermostat",
        "entity": "climate.hallway",
        "features": [
          {
            "type": "climate-hvac-modes",
            "hvac_modes": [
              "heat",
              "cool",
              "off"
            ]
          }
        ]
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

演示的 [组件页面](https://demo.home-assistant.io/components.html) 显示所有这些工作, 以及每个选项 。

## 装入脚本 {#load-the-script}

将演示文稿添加到您的页面中。 它从演示站点装入所有其他文件 :

```html
<script
  type="module"
  src="https://demo.home-assistant.io/embed.js"
></script>
```

## 添加一张牌 凯子 {#add-a-card}

是的 将实体直接放在提供方内部的脚本标记中,将卡片配置直接放在卡片内部的脚本标记中. 两者均使用 `type="application/json"` 或 YAML 使用 `type="text/yaml"` 。 卡片配置与仪表板相同.

```html
<ha-embed-provider>
  <script type="text/yaml">
    - entity_id: light.kitchen
      state: "on"
      attributes:
        friendly_name: Kitchen
        supported_color_modes:
          - brightness
        color_mode: brightness
        brightness: 180
  </script>
  <ha-embed-card>
    <script type="text/yaml">
      type: tile
      entity: light.kitchen
      features:
        - type: light-brightness
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

每个实体有一个`entity_id`,一个`state`,和`attributes`。 可选密钥 `area_id`, `device_id` 和 `platform` 设置在实体登记簿中 。 没有 `last_changed` , 实体在最近一个随机时间变化 。

实体保留所有属性, 如 Home Assistant , 所以属性中也只有您的集成集 。 拥有专门模型的实体, 包括灯光、气候、覆盖物、人、设备跟踪器, 找出一些属性, 而那些赢得你所设定的事物的实体: 灯光没有亮度, 例如。

YAML需要缩进. 如果您的站点修改了 HTML, 请确保 修改器在脚本标记中保留空白, 或者使用 JSON 。 提供者的`entities`属性和卡片的`config`属性也取JSON.

## 显示您的自定义卡 {#show-your-custom-card}

将您的卡片脚的学生脚本装入页面, 在演示脚本之后, 并使用其`custom:` 类型, 与仪表板相同 :

```html
<script
  type="module"
  src="https://demo.home-assistant.io/embed.js"
></script>
<script
  type="module"
  src="https://example.com/my-card.js"
></script>

<ha-embed-card>
  <script type="text/yaml">
    type: custom:my-card
    entity: light.kitchen
  </script>
</ha-embed-card>
```

您的牌得到的被嘲笑的`hass`对象与内置的牌相同,而`window.loadCardHelpers()`为[纸牌助手](/frontend/custom-ui/card#card-helpers)工作. 卡片助手只有在演示文稿运行后才存在. 模块脚本按照在页面上的顺序运行,所以在卡片之后保留脚本,以防卡片在脚本加载后立即使用. 许多内置的卡片,如地图卡,只有在卡片首次需要时才加载,所以通过卡片的帮助者来创建内置的卡片,而不是用其元素名称. 当您卡片的脚本出现在您页面以外的另一个站点时,该站点需要为此发送CORS头.

定制策略的装载方式相同. 在演示文稿后加载其脚本,并在一节、视图或仪表板的`strategy`中的`custom:`类型。

## 显示区域 {#show-a-section}

`<ha-embed-section>` 使一节与一节视图相同 。 它的配置与仪表盘中的配置相同:当没有`strategy`时,`title`成为了标题卡,标题横跨顶端,而`strategy`生成该部分. 本节取元素的宽度. 此示例使用来自 [添加一张牌 凯子](/frontend/custom-ui/demo#add-a-card) 的提供者, 并添加了 `switch.kettle` :

```html
<ha-embed-section>
  <script type="text/yaml">
    cards:
      - type: heading
        heading: Kitchen
      - type: tile
        entity: light.kitchen
      - type: tile
        entity: switch.kettle
  </script>
</ha-embed-section>
```

试试这里:一个带头的片段,两个砖块可以打开和关闭,下面有一个宽的砖块. 天花板灯属于`devices`中的设备.

从 Home Assistant 演示中嵌入的仪表板区域进行现场演示。

```html
<ha-embed-provider>
  <script type="application/json">
    {
      "entities": [
        {
          "entity_id": "light.kitchen_ceiling",
          "state": "on",
          "device_id": "kitchen_ceiling",
          "attributes": {
            "friendly_name": "Ceiling",
            "supported_color_modes": [
              "brightness"
            ],
            "color_mode": "brightness",
            "brightness": 200
          }
        },
        {
          "entity_id": "switch.kettle",
          "state": "off",
          "area_id": "kitchen",
          "attributes": {
            "friendly_name": "Kettle",
            "device_class": "outlet"
          }
        },
        {
          "entity_id": "sensor.kitchen_temperature",
          "state": "21.4",
          "area_id": "kitchen",
          "attributes": {
            "friendly_name": "Kitchen temperature",
            "device_class": "temperature",
            "state_class": "measurement",
            "unit_of_measurement": "°C"
          }
        }
      ],
      "areas": [
        {
          "area_id": "kitchen",
          "name": "Kitchen"
        }
      ],
      "devices": [
        {
          "id": "kitchen_ceiling",
          "name": "Kitchen ceiling light",
          "area_id": "kitchen"
        }
      ]
    }
  </script>
  <ha-embed-section>
    <script type="application/json">
      {
        "cards": [
          {
            "type": "heading",
            "heading": "Kitchen"
          },
          {
            "type": "tile",
            "entity": "light.kitchen_ceiling",
            "tap_action": {
              "action": "toggle"
            }
          },
          {
            "type": "tile",
            "entity": "switch.kettle",
            "tap_action": {
              "action": "toggle"
            }
          },
          {
            "type": "tile",
            "entity": "sensor.kitchen_temperature",
            "grid_options": {
              "columns": 12
            }
          }
        ]
      }
    </script>
  </ha-embed-section>
</ha-embed-provider>
```

一个按设备或区域对实体进行分组的章节战略需要提供者中的这些内容。 见[区域、装置瑜伽、日历和能量](/frontend/custom-ui/demo#areas-devices-calendars-and-energy).

## 显示视图 {#show-a-view}

`<ha-embed-view>`制作一个视图,带有它的徽章和布局,一个`strategy`生成视图. 赋予元素视图所需的宽度: masonry 和侧边栏视图从页面宽度中选择其列数,而不是元素. 此示例使用来自 [添加一张牌 凯子](/frontend/custom-ui/demo#add-a-card) 的提供者 :

```html
<ha-embed-view>
  <script type="text/yaml">
    type: sections
    badges:
      - entity: light.kitchen
    sections:
      - cards:
          - type: tile
            entity: light.kitchen
  </script>
</ha-embed-view>
```

在这里试一下:一个带外温徽章的区段视图,还有空位时两个区段相邻.

从 Home Assistant 演示中嵌入的仪表板视图的现场演示。

```html
<ha-embed-provider>
  <script type="application/json">
    [
      {
        "entity_id": "light.living_room",
        "state": "off",
        "attributes": {
          "friendly_name": "Living room",
          "supported_color_modes": [
            "brightness"
          ],
          "color_mode": "brightness",
          "brightness": 255
        }
      },
      {
        "entity_id": "switch.coffee_maker",
        "state": "on",
        "attributes": {
          "friendly_name": "Coffee maker",
          "device_class": "outlet"
        }
      },
      {
        "entity_id": "climate.hallway",
        "state": "heat",
        "attributes": {
          "friendly_name": "Hallway",
          "current_temperature": 19.5,
          "temperature": 21,
          "min_temp": 7,
          "max_temp": 30,
          "target_temp_step": 0.5,
          "hvac_modes": [
            "heat",
            "off"
          ],
          "supported_features": 1
        }
      },
      {
        "entity_id": "sensor.outside_temperature",
        "state": "12.3",
        "attributes": {
          "friendly_name": "Outside",
          "device_class": "temperature",
          "state_class": "measurement",
          "unit_of_measurement": "°C"
        }
      }
    ]
  </script>
  <ha-embed-view>
    <script type="application/json">
      {
        "type": "sections",
        "max_columns": 2,
        "badges": [
          {
            "entity": "sensor.outside_temperature"
          }
        ],
        "sections": [
          {
            "cards": [
              {
                "type": "heading",
                "heading": "Living room"
              },
              {
                "type": "tile",
                "entity": "light.living_room",
                "tap_action": {
                  "action": "toggle"
                }
              },
              {
                "type": "tile",
                "entity": "switch.coffee_maker",
                "tap_action": {
                  "action": "toggle"
                }
              }
            ]
          },
          {
            "cards": [
              {
                "type": "heading",
                "heading": "Hallway"
              },
              {
                "type": "thermostat",
                "entity": "climate.hallway"
              }
            ]
          }
        ]
      }
    </script>
  </ha-embed-view>
</ha-embed-provider>
```

查看策略和仪表盘策略都使用`strategy`键. 要显示一个仪表盘或仪表盘策略的视图,将仪表盘放入`dashboard`,将视图的路径或索引放入`view`. 没有`view`,第一个视图显示。

```yaml
dashboard:
  strategy:
    type: custom:my-dashboard
view: overview
```

## 显示仪表板 {#show-a-dashboard}

`<ha-embed-dashboard>` 制作一个带有标签的完整仪表板, 而`strategy` 生成仪表板。 仪表盘卷轴在元素内部,在其工具栏下. 元素高度为600像素; 设置它的 `height` 来改变它 。 要从另一个视图开始, 请设置其 `view` 属性到该视图的路径或索引 。 此示例使用来自 [添加一张牌 凯子](/frontend/custom-ui/demo#add-a-card) 的提供者 :

```html
<ha-embed-dashboard style="height: 480px">
  <script type="text/yaml">
    views:
      - title: Home
        path: home
        cards:
          - type: tile
            entity: light.kitchen
      - title: Kitchen
        path: kitchen
        cards:
          - type: light
            entity: light.kitchen
  </script>
</ha-embed-dashboard>
```

在这里试试:一个有两块标签的仪表板. 在它们之间切换,或者选择第一个标签上的走廊瓦片到第二个.

从 Home Assistant 演示的嵌入式中, 使用其标签的仪表板进行现场演示 。

```html
<ha-embed-provider>
  <script type="application/json">
    [
      {
        "entity_id": "light.living_room",
        "state": "off",
        "attributes": {
          "friendly_name": "Living room",
          "supported_color_modes": [
            "brightness"
          ],
          "color_mode": "brightness",
          "brightness": 255
        }
      },
      {
        "entity_id": "switch.coffee_maker",
        "state": "on",
        "attributes": {
          "friendly_name": "Coffee maker",
          "device_class": "outlet"
        }
      },
      {
        "entity_id": "climate.hallway",
        "state": "heat",
        "attributes": {
          "friendly_name": "Hallway",
          "current_temperature": 19.5,
          "temperature": 21,
          "min_temp": 7,
          "max_temp": 30,
          "target_temp_step": 0.5,
          "hvac_modes": [
            "heat",
            "off"
          ],
          "supported_features": 1
        }
      }
    ]
  </script>
  <ha-embed-dashboard>
    <script type="application/json">
      {
        "views": [
          {
            "title": "Home",
            "path": "home",
            "type": "sections",
            "max_columns": 2,
            "sections": [
              {
                "cards": [
                  {
                    "type": "heading",
                    "heading": "Living room"
                  },
                  {
                    "type": "tile",
                    "entity": "light.living_room",
                    "tap_action": {
                      "action": "toggle"
                    }
                  },
                  {
                    "type": "tile",
                    "entity": "switch.coffee_maker",
                    "tap_action": {
                      "action": "toggle"
                    }
                  }
                ]
              },
              {
                "cards": [
                  {
                    "type": "heading",
                    "heading": "Hallway"
                  },
                  {
                    "type": "tile",
                    "entity": "climate.hallway",
                    "tap_action": {
                      "action": "navigate",
                      "navigation_path": "climate"
                    }
                  }
                ]
              }
            ]
          },
          {
            "title": "Climate",
            "path": "climate",
            "type": "sections",
            "sections": [
              {
                "cards": [
                  {
                    "type": "thermostat",
                    "entity": "climate.hallway"
                  }
                ]
              }
            ]
          }
        ]
      }
    </script>
  </ha-embed-dashboard>
</ha-embed-provider>
```

工具栏仅显示标签,或视图的标题,以及子视图的后键. 没有编辑模式 。 每个仪表板都保持自己的视图,所以你的页面地址保持不变,一个页面上的两个仪表板不互相跟踪.

仪表板上的链接是这样工作的:

- 与仪表盘中的一个视图的链接,如`navigation_path: climate`或`/my-dashboard/climate`,显示了这种视图.
- 子视图的后键到它的`back_path`, 当它是这个仪表板的视图时。 否则它会进入它面前的视图,或者在没有视图时的第一个视图,所以一个`back_path`到另一页不会离开演示.
- 链接到您页面上的锚, 如 `#setup`, 滚动页面到它 。
- 其他 `navigate` 动作无所作为 。 一个 `url` 动作打开它的页面, 和仪表板一样.

## 查看时装入演示文稿 {#load-the-demo-when-it-comes-into-view}

在有多个 一般秃的职权的页面上,或者在页面下方很远的地方,您可以等待加载演示的脚本,直到一个演示到来,所以其余的页面先加载. 元素在设置时会读取脚本标记,因此当脚本稍后出现时,卡片仍然能找到它们的实体和配置. 观看页面上的每张卡片,区段,视图和仪表板,然后先导入演示的脚本,然后导入您的卡片脚本:

```js
const loadDemo = async () => {
  await import("https://demo.home-assistant.io/embed.js");
  await import("https://example.com/my-card.js");
};

const observer = new IntersectionObserver(
  (entries) => {
    if (entries.some((entry) => entry.isIntersecting)) {
      observer.disconnect();
      loadDemo();
    }
  },
  { rootMargin: "400px 0px" },
);
for (const demo of document.querySelectorAll(
  "ha-embed-card, ha-embed-section, ha-embed-view, ha-embed-dashboard",
)) {
  observer.observe(demo);
}
```

提供商内部的卡片、片段、视图和仪表板也算数。 `querySelectorAll`不查看阴影根内部, 所以对于在您自己的组件内的演示, 观察这些组件。 它不监视提供者硕:在页面顶端的提供者会在国内立即加载演示文稿,即使它的卡片远远低于. 从模块脚本中运行,所以页面的元素在它寻找时就在那里. 将演示文稿和卡片的脚本标记放在这样加载的时候.

## 在页面的任意位置放置牌 {#place-cards-anywhere-on-the-page}

发卡人不必在提供商内。 提供者以外的卡片使用页面上的第一个提供者. 在你自己的一个组件内部的卡片使用该组件周围的提供者,甚至通过其阴影根. 在页面的顶端设置一个包含所有实体的提供者,并在下方的卡片,在文本之间. 如果页面没有提供者,卡片会添加一个空的. 部分,视图,和仪表板都以同样的方式找到它们的提供者,并具有相同的`provider`属性.

要使用另一个提供者, 请设置卡片的`provider` 属性到提供者的ID :

```html
<ha-embed-provider id="living-room">…</ha-embed-provider>

<ha-embed-card provider="living-room">…</ha-embed-card>
```

在卡片添加到页面之前设定 `provider` 。 该卡在加卡时会选择其提供者,不会跟随后来的变化.

## 在一个站点上显示多个工程 {#show-several-projects-on-one-site}

如果您保留了数张牌或策略,您不需要每个演示站点. 给每个工程一个演示配置, 包含在 `entities` 中的实体, 以及在 `cards`, `sections`, `views` 或 `dashboard` 中显示什么 。 配置可以全部生活在主机站点中,或者每个项目可以保留自己的,比如在它的代码旁边的`demo.yml`:

```yaml
entities:
  - entity_id: light.kitchen
    state: "on"
    attributes:
      friendly_name: Kitchen
cards:
  - type: custom:my-card
    entity: light.kitchen
```

网站然后使每个配置:实体进入一个提供者,每个卡片、区域、视图或仪表板进入其元素,作为脚本标记中的YAML。 给每个项目自己的提供者,因此其实体保持隔离,在演示脚本后加载每张卡的脚本.

## 光明与黑暗 {#light-and-dark}

卡片遵循浏览器的光或暗模式. 当您的站点拥有自己的暗模式开关时, 设置提供者的 `color-scheme` 属性为 `light` 或 `dark` 。 纸牌的样式保持内部,不改变页面的样式。 一个例外是Roboto字体:脚本在页面中加入了它的字体面,所以使用Roboto的页面文本在脚本装入后可以看起来不同.

## 区域、装置瑜伽、日历和能量 {#areas-devices-calendars-and-energy}

一些卡片需要不是实体的数据. 要设置它,在提供者的脚本标记中插入一个对象,而不是列表. 该对象在 `entities` 中有列表, 以及其中的任何密钥 :

- `areas`:一个区域列表,每个区域有一个`area_id`和一个`name`。 没有它,每个 `area_id` 实体和装置就会成为一个区域。
- `devices`:一个设备列表,每个设备有`id`和`name`,可选的有`manufacturer`、`model`和`area_id`。 一个实体通过它的`device_id`属于一个设备,所以卡片和战略找到这个设备及其名称.
- `calendars`:日历实体的事件,按实体编号. 每个事件都有一个`summary`,一个`start`,和一个`end`. 这里没有列出的日历 今天周围会有样本 带有空列表的日历没有事件 。
- `energy`: 能量设置, 您需要的 `energy/get_prefs` 响应 。 没有它,能量就没有建立。

```yaml
entities:
  - entity_id: calendar.family
    state: "off"
    attributes:
      friendly_name: Family
  - entity_id: light.kitchen_ceiling
    state: "on"
    device_id: kitchen_ceiling
    attributes:
      friendly_name: Ceiling
areas:
  - area_id: kitchen
    name: Kitchen
devices:
  - id: kitchen_ceiling
    name: Kitchen ceiling light
    manufacturer: Acme
    model: Smart bulb
    area_id: kitchen
calendars:
  calendar.family:
    - summary: Dentist
      start: "2026-11-02T15:30:00+00:00"
      end: "2026-11-02T16:15:00+00:00"
```

日历卡只显示所显示的日期缪斯事件,所以将这些日期更改为您演示日附近的日期. 要总是有事件, 请将日历从 `calendars` 中删除, 并使用样本事件 。 它们被设定在演示载荷的脚本的当天,加载页面再次设置它们.

天气实体从它们的状况和温度,或者从它们的`forecast`属性,当它们拥有一个属性时,得到一个预测. 设定 `supported_features` 以显示预测 。

## 从您的页面更改和监视实体 {#change-and-watch-entities-from-your-page}

要更改一个实体, 请在 `provider.hass.mockEntities` 中更新 。 其他实体保持不变,实体所记得的也一样,如灯光的亮度。 从模块脚本中运行, 在提供者建立实体之后 。 这关闭了 [添加一张牌 凯子](/frontend/custom-ui/demo#add-a-card) 的厨房灯:

```js
await customElements.whenDefined("ha-embed-provider");
const provider = document.querySelector("ha-embed-provider");
await provider.updateComplete;

provider.hass.mockEntities["light.kitchen"].update({ state: "off" });
```

要使用一个实体的动作,请用同一个模块脚本称呼它. 提供者更新状态和卡片:

```js
provider.hass.callService(
  "light",
  "turn_on",
  { brightness_pct: 50 },
  { entity_id: "light.kitchen" },
);
```

设置提供者的 `entities` 属性替换所有实体, 它们从您设定的开始 。

当一个或多个实体的状态发生变化时,提供者会点出 `states-changed` 事件 。 它的细节有`states`,所有实体的状态 按实体ID。

## 被嘲笑的后端能做什么 {#what-the-mocked-backend-can-do}

被嘲笑的后端只知道Home Assistant的一部分 API. (英语). 当选择显示时,请记住这些限制:

- 灯光,开关,气候,封面,粉丝,锁,媒体玩家的行为,以及更多改变实体状态的行为.
- 更积极地确实是,更积极地确实是我们所看到的。
- 历史和统计由每个实体的现状构成。 演示的几个能量传感器,比如`sensor.solar_production`,得到他们自己编造的统计数据,所以他们的状态不会改变他们的图表.
- 模板没有实现 。 模板订阅以简单的 `{{ variable }}` 从您通过的变量中填入引用, 并按原样返回其余的 。 REST `template` 端点返回一个错误 。
- 日志为空.
- 一张牌的动作 `toggle`,`perform-action`和`url`。 打开对话框的动作, 如 `more-info` 什么都不做 。 使用 `confirmation` 的动作不起作用, 因为它等待一个不打开的对话框, 除非确认豁免演示用户 。
- 一个 `navigate` 动作到您的页面上的锚, 如 `#setup`, 滚动到那里 。 如[显示仪表板](/frontend/custom-ui/demo#show-a-dashboard)所描述的,仪表板也跟随自己的视图链接,给定的`dashboard`也跟[显示视图](/frontend/custom-ui/demo#show-a-view)一样。 其他 `navigate` 动作无所作为 。
- 后端不处理的行动,或对于它没有的实体,则什么都不做。 他们不返回错误。
- 等待答案的其他请求, 超过 WebSocket 或 REST, 得到错误 。

模拟器在 [`demo/src/stubs/`](https://github.com/home-assistant/frontend/tree/dev/demo/src/stubs) 的 [前端仓库](https://github.com/home-assistant/frontend) 中 。 如果您的卡片需要他们不知道的请求, 请见[画廊和演示](/frontend/development/gallery-and-demo#embed-cards-on-other-sites) 在哪里添加它 。
