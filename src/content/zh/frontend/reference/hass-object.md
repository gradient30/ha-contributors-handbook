---
title: 前端显示对象
description: 每个卡片、面板和组件的属性、方法和格式化器。
order: 2
sidebarLabel: 隐藏对象
---

# 前端显示对象 {#the-hass-object-in-the-frontend}

`hass` 对象在前端持有 Home Assistant 状态, 和要和 Core 交谈的功能 。 自定义卡,徽章,特征,视图,策略,和面板都得到了. 完整类型为`HomeAssistant`在[`src/types.ts`](https://github.com/home-assistant/frontend/blob/dev/src/types.ts)中.

每次更改时都会有一个新的 `hass` 对象, 但是没有更改的部分会保留其身份 。 与 `!==` 相比, 查看是否有变化 :

```js
if (newHass.states[entityId] !== oldHass.states[entityId]) {
  // This entity changed
}
```

要看到在 `hass` 对象中的内容, 请在浏览器的开发工具中打开, 如 [运行前端](/frontend/development/run#look-at-the-hass-object) 所示 。

前端内部,叶片组件使用[背景情况](/frontend/architecture/hass-and-contexts)而不是`hass`.

## 的临时议程 {#properties}

| 财产 | 这是什么 |
| --- | --- |
| `states` | 所有实体的状态,按实体识别键。 |
| `entities` | 实体注册,按实体ID键,包含接口需要的字段,如名称,图标,区域,设备. |
| `devices` | 设备注册,由设备ID键入. |
| `areas` | 地区注册,按地区ID键. |
| `floors` | 楼层登记簿,用楼层身份证键入. |
| `services` | 可用的 [动作](/glossary/action), 按域名 。 |
| `config` | Core的配置:位置,单位,时区,版本,以及加载组件. |
| `user` | 登录的用户, ý `name`, `is_admin` 和 `is_owner` 。 |
| `language` | 界面语言. |
| `locale` | 用户的数字、日期和时间格式设置。 |
| `themes` 和 `selectedTheme` (韩语) | 现有的主题,以及正在使用的主题。 |
| `panels` | 注册的面板。 |
| `connection` | lime WebSocket 连接, 从`home-assistant-js-websocket` 。 |
| `connected` | 连接是否打开 。 |

状态对象看起来像这样:

```json
{
  "entity_id": "light.ceiling",
  "state": "on",
  "attributes": {
    "brightness": 180,
    "friendly_name": "Ceiling",
    "supported_features": 32
  },
  "last_changed": "2026-10-10T13:46:59.129248+00:00",
  "last_updated": "2026-10-10T13:46:59.129248+00:00",
  "context": {
    "id": "01J9Z4V8M0R3XGQ2W4E5T6Y7U8",
    "parent_id": null,
    "user_id": null
  }
}
```

## 调用核心 {#calling-core}

所有这些的年度报告都是一种承诺。

### 调用服务 {#callservice}

```js
hass.callService("light", "turn_on", { brightness_pct: 50 }, {
  entity_id: "light.kitchen",
});
```

执行 [动作](/glossary/action) 。 参数是域,动作,其数据,以及可选的[目标](/glossary/target). 另外两个可选参数: `notifyOnError` (默认 `true`) 当动作失败时显示消息, `returnResponse` 请求返回数据的动作响应 。

### 调用WS {#callws}

```js
const areas = await hass.callWS({ type: "config/area_registry/list" });
```

发送 WebSocket 命令并按结果解决 。 拒绝 Core 发送一个错误 。 要继续接收更新, 请使用 `hass.connection.subscribeMessage()` 代替 。 见[数据层](/frontend/architecture/data).

### 调用 Api {#callapi}

```js
const result = await hass.callApi("GET", "history/period");
```

在 `/api/` 下调用 REST API, 由用户认证 。 参数是方法,路径,以及可选数据. 新功能使用WebSocket命令. `callApiRaw()` 做同样的事情, 但返回原 `Response` 。

### 获取 Auth {#fetchwithauth}

用用户的访问符获取 Home Assistant 的任何 URL, 并返回 `Response` 。

### 散开 {#hassurl}

`hass.hassUrl("/api/camera_proxy/camera.front")` 返回 Home Assistant 路径的完整 URL 。

## 文本 {#text}

### 瑶族 {#localize}

`hass.localize(key, values)` 返回前端的翻译字符串, 或已加载翻译的集成 。 见[前端的翻译](/frontend/architecture/translations).

### 加载ackend 翻译 {#loadbackendtranslation}

`hass.loadBackendTranslation(category, integrations)` 从 Core 装入翻译, 如 `"title"` 或 `"entity"` , 并以 `localize` 函数解决 。

## 墅 {#formatters}

格式化器将状态,属性,和名称转换成文本,以用户的语言,数字格式,日期格式,时区,单位表示. 使用它们而不是显示原始值 。 每个都取一个状态对象,如`hass.states["light.kitchen"]`.

### 一系列格式化实体状态 {#formatentitystate}

```js
hass.formatEntityState(stateObj); // "On"
hass.formatEntityState(stateObj, "off"); // "Off"
```

格式化实体状态,或您通过的另一个状态作为第二个参数。

### 格式 实体属性 {#formatentityattributevalue}

```js
hass.formatEntityAttributeValue(stateObj, "current_temperature");
// "20.5 °C"
hass.formatEntityAttributeValue(stateObj, "current_temperature", 18);
// "18 °C"
```

格式化属性的值,或您通过的另一个值作为第三个参数。

### 格式属性Name {#formatentityattributename}

```js
hass.formatEntityAttributeName(stateObj, "current_temperature");
// "Current temperature"
```

格式化属性名称。

### 部件 {#parts}

`formatEntityStateToParts()` 和 `formatEntityAttributeValueToParts()` 采用相同的参数, 并返回部分结果, 每个部分带有 `value` 、 `unit` 或 `literal` 的 `type` 。 用它们来对数字和单位进行不同的样式化.

### 格式实体Name {#formatentityname}

```js
hass.formatEntityName(stateObj, name, options);
```

从注册上下文格式化一个实体的名称:实体、其设备、母设备、区域以及下层。 内置的卡片使用它,所以定制的卡片也会以同样的方式命名实体. `name`可以是:

- 左撇子:实体的友好名称.
- 字符串:按原样返回. 用户输入的名称使用此选项 。
- 一个名称项, 如 `{ type: "entity" }` , 或其中的列表, 与 `options` 中的空格或 `separator` 合并 。

物品类型是 `entity`,`device`,`parent_device`,`area`,`floor`,以及 `text` 都有自己的 `text` 。 毫无决心的项目被排除在外。

对于称为**热量计**的恒温器的温度传感器,位于**圆形地板**的** 生活室****:

```js
hass.formatEntityName(stateObj);
// "Thermostat Temperature"
hass.formatEntityName(stateObj, { type: "area" });
// "Living room"
hass.formatEntityName(
  stateObj,
  [{ type: "device" }, { type: "entity" }],
  { separator: " · " }
);
// "Thermostat · Temperature"
hass.formatEntityName(stateObj, [
  { type: "text", text: "Floor:" },
  { type: "floor" },
]);
// "Floor: Ground floor"
```

`parent_device`只为子设备的实体填充,比如电源条的一个出口. 这使得`[{ type: "parent_device" }, { type: "device" }, { type: "entity" }]`可以安全地选择全名: 对于一个出口,它给出了"Power left Outlet 1 Switch",而对于其他实体,母名被排除在外. 此列表也是组成名称的前端默认值.

要让用户在卡片编辑器中选择名称,请使用`entity_name`选择器. 它的值是`hass.formatEntityName()`接受的,所以直接通过配置. 见[卡片编辑器和拾卡器](/frontend/custom-ui/card-editor#entity-names).
