---
title: 添加更多信息视图
description: 在多信息对话框中给一个域的实体自己的控制 。
order: 1
---

# 添加更多信息视图 {#add-a-more-info-view}

[更多信息对话框](/glossary/more-info-dialog) 选择实体时打开 。 它所显示的内容取决于实体的域:光获得亮度滑动器,锁大锁按钮. 没有自己视图的域获得默认内容:状态行,历史,以及大多数域的日志. 一个实体的属性不是视图的一部分:对话框从它的三点菜单中以单独的细节视图显示它们.

在构建前,请查看设计区的[啊 更多信息视图](/design/more-info)。 它们显示每个已有的视图,而原理新的则随之而来:一个大主控,次控下方,只有设备支持的控制.

## 为域添加视图 {#add-a-view-for-a-domain}

此示例为名为 `example` 的域添加了视图 。

1. 创建 `src/dialogs/more-info/controls/more-info-example.ts`, 有一个元素叫做 `more-info-example` 。 对话框设置了 `hass`、`stateObj` 和`entry` (实体注册条目) 。

```ts
   @customElement("more-info-example")
   class MoreInfoExample extends LitElement {
     @property({ attribute: false }) public hass!: HomeAssistant;

     @property({ attribute: false }) public stateObj?: HassEntity;

     protected render() {
       if (!this.stateObj) {
         return nothing;
       }
       return html`<!-- the controls of the domain -->`;
     }
   }
   ```

2. 在 [`src/dialogs/more-info/const.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/const.ts) 中添加 `"example"` 到 `DOMAINS_WITH_MORE_INFO` 。
3. 在 [`src/dialogs/more-info/state_more_info_control.ts`](https://github.com/home-assistant/frontend/blob/dev/src/dialogs/more-info/state_more_info_control.ts) 中添加懒惰导入到 `LAZY_LOADED_MORE_INFO_CONTROL` :

```ts
   example: () => import("./controls/more-info-example"),
   ```

4. 对于一个遵循较新设计,从大状态开始而非状态行的视图,也在同一`const.ts`中将域添加到`DOMAINS_WITH_NEW_MORE_INFO`中.

`const.ts` 中的其他列表对对话框进行微调 。 `DOMAINS_HIDE_DEFAULT_MORE_INFO` 列出没有自己视图但跳过默认视图元素的域, `DOMAINS_MORE_INFO_NO_HISTORY` 隐藏历史和日志 。

## 加大力度 {#reuse-the-controls}

不要从零开始建立控制。 更多信息视图共享指导方针 [`src/dialogs/more-info/components/`](https://github.com/home-assistant/frontend/tree/dev/src/dialogs/more-info/components) 的组件和大触控, 如 `ha-control-slider` 和 `ha-control-switch` 的组件 [`src/components/`](https://github.com/home-assistant/frontend/tree/dev/src/components) 。 现有的视图,如`more-info-lock.ts`或`more-info-fan.ts`,都是好的起点.

只显示实体所支持的内容: 在创建控制前检查其`supported_features` 和属性 。

## 加入画廊 {#add-it-to-the-gallery}

将新视图添加到 [画廊](/frontend/development/gallery-and-demo) 的更多info 部分, 并有不同状态的少数实体, 因此审查人员可以在没有设备的情况下看到它.
