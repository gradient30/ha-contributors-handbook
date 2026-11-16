---
title: 登记资源
description: 将您的 JavaScript 文件提供给 Home Assistant 并装入每个仪表板 。
order: 1
---

# 登记资源 {#register-resources}

在仪表盘使用您的卡片,徽章,特征,视图,或策略之前,Home Assistant必须加载它的JavaScript. 这需要两个步骤:服务文件,然后将其注册为资源.

## 提供文件 {#serve-the-file}

在您的 Home Assistant眩晕配置文件夹中创建一个名为 `www` 的文件夹, 在 `configuration.yaml` 旁边 。 里面的文件服务于 `/local/`, 因此 `www/my-card.js` 变为 `/local/my-card.js` 。

{H1 如果您刚创建它, 请重新启动 Home Assistant 一次 。

> [!WARNING]
> `www` 中的文件无需认证即可服务 。 任何人,谁可以到达你的Home Assistant可以下载。 别把秘密藏在那里

您也可以从其它 URL 中装入一个资源, 就像您的工程发布的文件 。

## 登记 {#register-it}

默认情况下在UI中管理资源喽:

1. 转到**Settings** > **Dashboards**。
2. 在右上方菜单中,选择**资源**.
3. 选择 **Add 资源 **, 输入 URL, 如 `/local/my-card.js`, 并选择 JavaScript 模块 ** 。

所有仪表板都装满了资源。 更改资源后,在浏览器中重新装入页面。 您的浏览器可能缓存旧文件 : 在 URL 中添加一个版本, 如 `/local/my-card.js?v=2`, 强制更新副本 。

### 在也门 {#in-yaml}

要管理 YAML 中的资源, 请在 `lovelace` 的 `configuration.yaml` 一节中设置 `resource_mode` 至 `yaml` , 并在此列出 :

```yaml
lovelace:
  resource_mode: yaml
  resources:
    - url: /local/my-card.js
      type: module
```

在 `resource_mode: yaml` 中, UI 中的 **Resources ** 页面不再管理它们 。 更改后运行 `lovelace.reload_resources` [动作](/glossary/action) 或重新启动 Home Assistant , 然后在浏览器中重新装入页面 。

## 资源类型 {#resource-types}

| 类型 | 救命 用于 |
| --- | --- |
| `module` | 一个JavaScript模块。 用这个来换新东西 |
| `css` | 样式表。 |
| `js` | 一个经典的JavaScript文件,没有`import`和`export`。 堕地. |
| `html` | HTML 导入。 前端不再装填 |

UI只为新资源提供`module`和`css`。 它只显示 `js` 和 `html` 的已有资源 。

在安全模式下,Home Assistant装入完全没有资源,因此定制卡不会在那里出现.

## 登记采摘者 {#registering-pickers}

一些注册仅在资源被加载后才能工作:卡片拾取器中的卡片,特性拾取器中的特性,或者新仪表盘对话框中的仪表板. 如果您不显示, 请检查资源负载( 查看浏览器控制台中的错误) , 然后重新装入页面并再次打开对话框 。
