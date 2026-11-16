---
title: 待办名片
description: 待办事项列表卡显示待办事项列表的项目,用于检查,添加新的,并重新排序.
sidebarGroup: 控制
---

# 待办名片 {#to-do-list-card}

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
        "type": "todo-list",
        "entity": "todo.shopping_list"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 使用量 {#usage}

待办列表卡显示一个待办列表,如购物列表. 顶端是添加项目的一个字段。 下面是项目分组: 喂 importanceion**和已完成的项目**。 没有状态的项目有自己的组。 每个项目都有一个复选框. 选择此项目将打开进行编辑,并附有其描述和到期日.

组头旁边的菜单为该组持有动作,例如重排活动项目顺序,或清除所有已完成的项目. 卡片提供的内容取决于列表:无法创建或移动项目的列表显示没有字段可以添加,也没有重新排序的选择.

使用待办名片进行列表中的人每天工作,如杂货或杂务. 要仅显示剩多少项, 待办事宜实体的 [平板卡](/design/dashboards/tile-card) 就够了 。 它的状态是仍然需要处理的物品的数量.

### 藏起来 {#hide-whats-done}

有了`hide_completed: true`,卡片只显示剩下的事. 用于一个长长的列表,比如一个从未被清除的购物列表. 在 `hide_create: true` 中, 添加项目的字段会消失, 对于一个在壁板上读取的列表, 它比它编辑的要多 。

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
        "type": "todo-list",
        "entity": "todo.shopping_list",
        "hide_completed": true,
        "hide_create": true
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

### 顺序 {#order}

默认情况下,项目会保持列表的顺序,人们可以通过拖动来更改. 用 `display_order` 来排序它们 。 使用 `due_date_period` 只显示在某一期间到期的项目, 如今天, 或是本周 。

### 内容 {#content}

- 当仪表盘有多个列表时设置 `title` 。 列表名称本身不会在卡片上显示.
- 对于一个有清晰的拥有者或位置的列表,将卡片放入匹配部分,因此人们会找到他们期待的地方.

## 配置 {#configuration}

- `entity`(字符串,需要):要显示的待办事宜列表 。 只有`todo`域的工作实体.
- `title` (字符串):列表上的一个标题.
- `hide_completed` (boolean):隐藏已完成的项目. 默认为 `false` 。
- `hide_create` (boolean): 隐藏字段以添加项目 。 默认为 `false` 。
- `hide_section_headers`(boolean):隐藏**Aactive**和**完成**标题. 默认为 `false` 。
- `display_order`(字符串):`none`,`alpha_asc`,`alpha_desc`,`duedate_asc`,或`duedate_desc`。 默认为`none`,列表的顺序 。
- 畔 `due_date_period` (期):只显示这期间到期的项目,比如今天或接下来的7天.
- `item_tap_action` (字符串): 当您选择项目时会发生什么 : `edit` 或 `toggle` 。 默认为 `edit` 。
- `theme`(字符串):只适用于此卡的主题.

```yaml
type: todo-list
entity: todo.shopping_list
title: "Groceries"
hide_completed: true
display_order: "alpha_asc"
```

## 在代码中 {#in-code}

牌居于[`src/panels/lovelace/cards/hui-todo-list-card.ts`](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-todo-list-card.ts),元素为`<hui-todo-list-card>`. 它与 `subscribeItems` 订阅列表中的 `subscribeItems` 从 [`src/data/todo.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/todo.ts) 的项目, 因此其它地方的更改会立刻出现 。 重排顺序使用 `<ha-sortable>`, 编辑一个项目打开 [`src/panels/todo/`](https://github.com/home-assistant/frontend/tree/dev/src/panels/todo) 的待办项目对话框 。

哪些控件显示取决于实体的支持特性, 如`CREATE_TODO_ITEM` 和`MOVE_TODO_ITEM` 在[`src/data/todo.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/todo.ts) 中 。

[来源](https://github.com/home-assistant/frontend/blob/dev/src/panels/lovelace/cards/hui-todo-list-card.ts)
