---
title: 自定义面板
description: 在 Home Assistant 的国民端添加一个完整的页面, 并在侧边栏中加入链接, 并实时访问家居状态 。
order: 8
---

# 自定义面板 {#custom-panels}

A [面板](/glossary/panel) 是 Home Assistant 中的完整页面, 如仪表板、 地图或设置 。 自定义面板是您自己的页面:一个自定义元素,它获得与其它所有对象一样的 `hass` 对象, 并填充侧边栏旁边的整个屏幕 。 集成用于自己的界面,用户可以在YAML中添加.

## 梢一个例子 {#an-example}

在配置文件夹中创建 `www/example-panel.js` :

```js
class ExamplePanel extends HTMLElement {
  set hass(hass) {
    this._hass = hass;
    this._render();
  }

  set narrow(narrow) {
    this._narrow = narrow;
    this._render();
  }

  set panel(panel) {
    this._panel = panel;
    this._render();
  }

  _render() {
    if (!this._hass || !this._panel) {
      return;
    }
    const count = Object.keys(this._hass.states).length;
    this.innerHTML = `
      <p>There are ${count} entities.</p>
      <p>The screen is ${this._narrow ? "" : "not "}narrow.</p>
      <pre>${JSON.stringify(this._panel.config, null, 2)}</pre>
    `;
  }
}

customElements.define("example-panel", ExamplePanel);
```

然后 注册 `configuration.yaml` 中的面板,并重新启动 Home Assistant :

```yaml
panel_custom:
  - name: example-panel
    url_path: example
    sidebar_title: Example panel
    sidebar_icon: mdi:server
    module_url: /local/example-panel.js
    config:
      hello: world
```

面板在 `/example` 打开, 在侧边栏中有一个链接 。

## 配置选项 {#configuration-options}

| 选项 | 含义 |
| --- | --- |
| `name` | 您元素的标记名称 。 要求。 |
| `url_path` | 面板的 URL 。 默认为 `name` 。 一定是独一无二的 |
| `sidebar_title` | 侧边栏中的文字. 没有它,面板不在边栏。 |
| `sidebar_icon` | 侧边栏中的图标. 默认为 `mdi:bookmark` 。 |
| `module_url` | 您 JavaScript 模块的 URL 。 大小的 , 大小的 , 大小的 。 |
| `js_url` | 经典 JavaScript 文件的 URL 。 当设置两者时,前端的遗存建筑使用这个,现代建筑 `module_url`. |
| `config` | 任何你想传递给面板。 它以 `panel.config` 显示, 在 `_panel_custom` 键旁边, 键是 Home Assistant 随着面板设置而添加的 。 |
| `require_admin` | 只向管理员显示面板 。 默认为 `false` 。 |
| `embed_iframe` | 将面板装在iframe中,与前端的其余部分隔离. 默认为 `false` 。 |
| `trust_external_script` | 从另一个主机装入脚本而无需询问 。 默认为`false`,然后要求用户确认,因为脚本可以完全访问Home Assistant. |
| `handle_safe_area` | 设定为 `true` 当您的面板处理电话屏幕的安全区域时, 如 Notch 本身 。 Home Assistant那么它不会在面板周围添加自己的垫子。 默认为 `false` 。 |

一个集成注册了来自 Python 的自定义面板, 来自 `panel_custom` 的自定义面板 。 它需要相同的选项,但少数有其它名称:`webcomponent_name`为`name`,`frontend_url_path`为`url_path`,`trust_external`为`trust_external_script`.

## 面板有什么好处 {#what-a-panel-gets}

Home Assistant 将这些属性设定在元素上 :

| 财产 | 这是什么 |
| --- | --- |
| `hass` | Home Assistant的完整状态。 重新设定每个变化。 见[有对象引用](/frontend/reference/hass-object). |
| `narrow` | `true` 当面板使用窄屏幕的布局时 。 |
| `route` | 当前路径 : `prefix` 是面板的 URL, 而 `path` 是 URL 的其余部分 。 用它做面板内的页面 。 |
| `panel` | 小组资料。 能够获得 `config` 选项在 `panel.config` 中, 连同 `_panel_custom` 键 。 |

您的面板负责它的整页, 包括一个标题和一个在窄屏幕上打开侧边栏的方法.

## 写标准类 {#write-standard-classes}

前端加载其现代和遗产的定制面板。 以标准 JavaScript 类定义您的元素 。 转录到ES5函数的元素不支持.
