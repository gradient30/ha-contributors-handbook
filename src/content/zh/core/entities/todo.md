---
title: 待办列表实体
description: 为购物列表、任务列表或任何其他命令的具有状态的项目列表构建待办列表实体。
sidebarLabel: 待办事宜列表
sidebarGroup: 输入与助手
---

# 待办列表实体 {#to-do-list-entity}

待办事项列表实体代表项目列表,每个列表都有状态:打开或完成. 想想购物列表,任务管理器中的任务,或者机器人真空应用所记录的杂务. 从`TodoListEntity` 继承到`homeassistant.components.todo` 。

人们在待办面板中看到列表,自动化,脚本,和Assist可以读到并加入其中. 他们能改变什么取决于您设置的 [支持的特性](/core/entities/todo#supported-features) 。

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 在瓷片卡和待办列表卡中只读购物列表. 状态是开放项目的数量. 这些项目是演示样本。

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
        "entity_id": "todo.shopping_list",
        "state": "3",
        "attributes": {
          "friendly_name": "Shopping list"
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "todo.shopping_list"
      }
    </script>
  </ha-embed-card>
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

## 的临时议程 {#properties}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `todo_items` | `list[TodoItem] \| None` | `None` | 清单上的物品,按顺序排列. `None`表示列表不详. |

每个实体的通用属性,如`name`,`available`和`unique_id`,都在[实体类别](/core/entities/entity-class)上.

## 支持的特性 {#supported-features}

将 `TodoListEntityFeature` 的旗帜与 `|` 合并, 用 `_attr_supported_features` 设置 。 没有,只读清单。 见[支持的特性](/glossary/supported-features).

| 常数 | 它能带来什么 |
| --- | --- |
| `CREATE_TODO_ITEM` | 添加项目。 执行`async_create_todo_item`。 |
| `DELETE_TODO_ITEM` | 删除项目, 并同时删除所有已完成的项目 。 执行`async_delete_todo_items`。 |
| `UPDATE_TODO_ITEM` | 更改项目, 如重命名或按做标记 。 执行`async_update_todo_item`。 |
| `MOVE_TODO_ITEM` | 重订项目。 执行`async_move_todo_item`。 |
| `SET_DUE_DATE_ON_ITEM` | 设置 `due` 到项目创建或更新的日期 。 |
| `SET_DUE_DATETIME_ON_ITEM` | 设置 `due` 到创建或更新项目的日期和时间 。 |
| `SET_DESCRIPTION_ON_ITEM` | 设定 `description` 当项目创建或更新时 。 |

当一个动作使用一个您不支持的字段时, 就像一个到期日一样, 在您的方法被调用之前, 动作会因验证错误而失败 。

## 待办项目 {#to-do-items}

每个项目均为`TodoItem`,数据类来自`homeassistant.components.todo`.

| 外地 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `uid` | `str \| None` | `None` | 物品的独有标识 。 需要更新、删除或移动。 |
| `summary` | `str \| None` | `None` | 项目文. |
| `status` | `TodoItemStatus \| None` | `None` | `TodoItemStatus.NEEDS_ACTION` or `TodoItemStatus.COMPLETED`. |
| `due` | `datetime.date \| datetime.datetime \| None` | `None` | 当得品时. `datetime`必须有一个时区。 |
| `description` | `str \| None` | `None` | 描述比总结要长. |
| `completed` | `datetime.datetime \| None` | `None` | 上一次标为已完成时 。 |

您返回的每个项目都需要 `uid` 、 `summary` 和 `status` 。

## 方法 {#methods}

所有的方法都只是同化。 每个都只用于匹配特性。

### 创建项目 {#create-an-item}

```python
async def async_create_todo_item(self, item: TodoItem) -> None:
    """Add an item to the list."""
```

新项目有一个 `summary` 和状态 `NEEDS_ACTION`, 加上您支持的可选字段 。 它还没有 `uid` : 您的服务或整合给出它 。

### 更新一个项目 {#update-an-item}

```python
async def async_update_todo_item(self, item: TodoItem) -> None:
    """Update an item on the list."""
```

物品总是有 `uid` 。 这是您上次返回时的复制件, 并填入已更改的字段 。 一个设置到{H芦>的字段是故意清除的,所以也清除了你的一侧.

### 删除项目 {#delete-items}

```python
async def async_delete_todo_items(self, uids: list[str]) -> None:
    """Delete items from the list."""
```

你拿到一张身份证 删掉所有的, 不仅仅是第一个。

### 移动项目 {#move-an-item}

```python
async def async_move_todo_item(
    self, uid: str, previous_uid: str | None = None
) -> None:
    """Move an item on the list."""
```

以 `uid` 移动项目, 因此它紧接着项目 `previous_uid` 。 当`previous_uid`是`None`时,将其移动到列表的首位.

更改后, 请更新 `todo_items` 并写入状态, 或者从您的服务中刷新 。 基础课每次写出状态时都会将新项目发送到前端.

## 状态 {#states}

状态是状态 `NEEDS_ACTION` 的项目数量 。 它是`unknown` 当`todo_items`是`None`时。

## 示例 {#example}

```python
from homeassistant.components.todo import (
    TodoItem,
    TodoItemStatus,
    TodoListEntity,
    TodoListEntityFeature,
)

class ExampleShoppingList(TodoListEntity):
    """A shopping list kept by a cloud service."""

    _attr_has_entity_name = True
    _attr_translation_key = "shopping_list"
    _attr_supported_features = (
        TodoListEntityFeature.CREATE_TODO_ITEM
        | TodoListEntityFeature.DELETE_TODO_ITEM
        | TodoListEntityFeature.UPDATE_TODO_ITEM
    )

    def __init__(self, client: ExampleClient) -> None:
        """Initialize the list."""
        self._client = client
        self._attr_unique_id = f"{client.account_id}_shopping_list"

    async def async_update(self) -> None:
        """Fetch the items from the service."""
        self._attr_todo_items = [
            TodoItem(
                uid=entry.id,
                summary=entry.text,
                status=(
                    TodoItemStatus.COMPLETED
                    if entry.done
                    else TodoItemStatus.NEEDS_ACTION
                ),
            )
            for entry in await self._client.get_items()
        ]

    async def async_create_todo_item(self, item: TodoItem) -> None:
        """Add an item to the list."""
        await self._client.add_item(item.summary)
        await self.async_update_ha_state(force_refresh=True)

    async def async_update_todo_item(self, item: TodoItem) -> None:
        """Update an item on the list."""
        done = item.status == TodoItemStatus.COMPLETED
        await self._client.update_item(item.uid, item.summary, done)
        await self.async_update_ha_state(force_refresh=True)

    async def async_delete_todo_items(self, uids: list[str]) -> None:
        """Delete items from the list."""
        await self._client.delete_items(uids)
        await self.async_update_ha_state(force_refresh=True)
```

这个例子就是民意测验。 当您的服务推动变化, 或者您使用 [协调员](/glossary/coordinator) 时, 取而代之刷新 。 见[更新状态](/core/entities/state-updates)。
