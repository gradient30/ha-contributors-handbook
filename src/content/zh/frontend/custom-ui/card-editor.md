---
title: 卡片编辑器和拾卡器
description: 给您的自定义卡一个视觉编辑器, 一个合理的默认配置, 和一个位置在取卡器及其建议。
order: 3
---

# 卡片编辑器和拾卡器 {#card-editor-and-picker}

人们期望在不写YAML的情况下增加并设置卡片. 您的定制卡可以参与其中: 它可以在取卡器中显示,从工作配置开始,并有一个视觉编辑器.

## 在拾牌机上出现 {#show-up-in-the-card-picker}

向 {H5} 的 Q :

```js
window.customCards = window.customCards || [];
window.customCards.push({
  type: "state-card-example",
  name: "State card",
  description: "Shows the state of one entity.",
  preview: true,
  documentationURL: "https://example.com/state-card",
});
```

| 密钥 | 要求数 | 含义 |
| --- | --- | --- |
| `type` | 对 | 您的卡的标签名称, 没有 `custom:` 。 |
| `name` | | 采者中名 The. |
| `description` | | 名字下面的简短描述. |
| `preview` | | 在拾卡器中显示卡 Jonasn. kgm 默认为 {H0 Jonas} 。 |
| `documentationURL` | | 向卡片编辑器添加帮助链接。 |
| `getEntitySuggestion` | | 向实体推荐你的名片。 见下文。 |

您跋涉的卡片出现在取卡器中, 用于社区卡片。

## 默认配置 {#a-default-configuration}

当有人选择您的名片时, Home Assistant 向静态 `getStubConfig()` 询问一个配置开始 。 返回时没有 `type` :

```js
static getStubConfig(hass, entities, entitiesFallback) {
  const light = entities.find((id) => id.startsWith("light."));
  return { entity: light ?? "sun.sun" };
}
```

`entities` 持有尚未在仪表板上的实体, `entitiesFallback` 持有这些实体。 两者都省略了没有或未知的实体,因此两个列表都可以是空的: 保留一个倒置,比如 `sun.sun` 在示例中. 没有`getStubConfig()`,卡片只从它的型开始.

## 向实体推荐您的名片 {#suggest-your-card-for-an-entity}

当有人在拾卡器中选择实体时,Home Assistant会为此建议牌. 您的卡片可以在内置卡片以下的社区卡片中加入这些建议旨在使其中的 `getEntitySuggestion` `window.customCards` 条目:

```js
getEntitySuggestion: (hass, entityId) => {
  if (!entityId.startsWith("light.")) {
    return null;
  }
  return {
    config: { type: "custom:state-card-example", entity: entityId },
  };
},
```

返回 `null` 当您的卡不符合实体时, 一个建议, 或一个列表, 用于多个变体 。 一项建议是:

- `config`(JERED):贺卡的配置,包括型号 `custom:`。
- `label`:该变种的简称,在牌名后显示. 只有在你返回不止一个的时候才设置.

只是建议你的名片在有道理的地方 检查域,设备类,或实体的支持特性. 为每个实体推荐的卡片让拾牌者对每个人都很吵.

## 带有窗体的视觉编辑器 {#a-visual-editor-with-a-form}

对于大多数牌,一个表就够了. 从静态的 `getConfigForm()` 返回一个方案, 而 Home Assistant 用与内置卡片相同的控件使窗体 :

```js
static getConfigForm() {
  return {
    schema: [
      { name: "entity", required: true, selector: { entity: {} } },
      {
        type: "grid",
        name: "",
        schema: [
          {
            name: "name",
            selector: { entity_name: {} },
            context: { entity: "entity" },
          },
          {
            name: "icon",
            selector: { icon: {} },
            context: { icon_entity: "entity" },
          },
        ],
      },
      { name: "theme", selector: { theme: {} } },
    ],
    computeLabel: (schema) =>
      schema.name === "icon" ? "Special icon" : undefined,
    computeHelper: (schema) =>
      schema.name === "entity" ? "The entity to show" : undefined,
    assertConfig: (config) => {
      if (config.other_option) {
        throw new Error("'other_option' is not supported.");
      }
    },
  };
}
```

| 密钥 | 要求数 | 含义 |
| --- | --- | --- |
| `schema` | 对 | 形之田园. |
| `computeLabel(schema, localize)` | | 返回字段的标签。 返回 `undefined` 对默认值 68. Home Assistant 对类似 `entity` 的常见名称知道标签 。 |
| `computeHelper(schema, localize)` | | 返回一个较长的帮助文本,在字段下显示。 |
| `assertConfig(config)` | | 唤作一切变化. 没问题,如果有人写YAML,表单不能显示,就扔出一个错误来关闭视觉编辑器. 一旦错误消失,视觉编辑器就可以再次使用. |

### Schema 字段 {#schema-fields}

字段有 `name`, 配置中的密钥, 通常为 `selector` 。 [选择器](/glossary/selector)是蓝图和自动化编辑器使用的同一种,如`entity`,`number`,`boolean`,`select`,`icon`和`theme`. [选择文档](https://www.home-assistant.io/docs/blueprint/selectors/) 全部列出 。 字段的其他选项 :

- `required`:字段必须有一个值。
- `default`: 字段空闲时的值 。
- `context`:将字段链接到另一个字段。 在该示例中,图标选择器显示在`entity`字段中被选中的实体的图标.
- `visible` : 只在条件下显示字段, 如 `{ field: "mode", value: "advanced" }` 。

字段可以分组:

- 将它的 `schema` 放在一起。 设定 `column_min_width`, 如 `"200px"` 一样, 在包装时控制 。
- `type: "expandable"` puts its `schema` in a section that opens and closes, with a `title`.

两者都有 `name` 和 `flatten` 选项 。 使用 `flatten: true` 或空的 `name` , 组的值会进入主配置 。 否则它们就会进入这个名字下的子对象. 完整的一组选项在 [`src/components/ha-form/types.ts`](https://github.com/home-assistant/frontend/blob/dev/src/components/ha-form/types.ts) 中 。

### 实体名称 {#entity-names}

例子中的`entity_name`选择器让人们选择实体的命名方式:用自己的名称,设备,区域,或地板,或用自己的文字. 它的价值正是`hass.formatEntityName()`接受的,所以直接通过:

```js
const name = this._hass.formatEntityName(stateObj, this._config.name);
```

选择丈者自有两种选择:

- `entity_id`: 以 `context.entity` 来乍览名称的固定实体驯服, 而不是来自 `context.entity` 。
- `default_name`: 字段没有配置值时显示的值 (`undefined`). 它的形状与值相同:一个字符串,一个名称项目,或者一个它们的列表.

参见[有对象引用](/frontend/reference/hass-object#formatentityname)它能做什么。

## 一个享有同等编辑器 {#a-visual-editor-of-your-own}

当一个表单不够时,请写出自己的编辑元素,并从静态`getConfigElement()`返回:

```js
static getConfigElement() {
  return document.createElement("state-card-example-editor");
}
```

Home Assistant用配置在编辑器上调用`setConfig()`,并在它上设置`hass`,就像卡上一样. 如果您的编辑器有 `lovelace` 属性, Home Assistant 也可以用仪表板的信息设置 。 没有这种财产的平庸元素是得不到的. 当用户更改某事时, 用全新的配置点火 `config-changed` 事件 :

```js
class StateCardExampleEditor extends HTMLElement {
  setConfig(config) {
    this._config = config;
  }

  set hass(hass) {
    this._hass = hass;
  }

  _changed(newConfig) {
    this.dispatchEvent(
      new CustomEvent("config-changed", {
        detail: { config: newConfig },
        bubbles: true,
        composed: true,
      })
    );
  }
}

customElements.define(
  "state-card-example-editor",
  StateCardExampleEditor
);
```

当卡片同时存在时,则使用`getConfigElement()`.
