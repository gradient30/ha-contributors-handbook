---
title: 日历实体
description: 展出包含有始末的事件的日历,并选择让用户创建,更新和删除.
sidebarLabel: B. 事 项
sidebarGroup: 传感器和状态
---

# 日历实体 {#calendar-entity}

日历实体代表一组事件,每个事件都有起始和结束日期或时间. 它的状态显示一个事件是否正在发生, 这使得它用于自动化。 从`CalendarEntity`继承,从`homeassistant.components.calendar`导入。

日历集成遵循iCalendar标准,[RFC 5545 (法语).](https://www.rfc-editor.org/rfc/rfc5545). 如果您的集成支持重复事件, 它会扩展它们本身: 返回序列中的每个事件作为自己的事件 。

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 平板卡和日历卡中的日历. 不发生任何事件时,国家就关闭了。 事件是今天的演示样本

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
        "entity_id": "calendar.family",
        "state": "off",
        "attributes": {
          "friendly_name": "Family"
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "calendar.family"
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "calendar",
        "entities": [
          "calendar.family"
        ],
        "initial_view": "listWeek"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `event` | `CalendarEvent \| None` | 要求数 | 接下来是 你很会说话 当没有。 你很聪明。 |
| `initial_color` | `str \| None` | `None` | 前端的日历的十六进制颜色, 如 `"#16a765"` 。 |

您负责选择正确的 `event` : 正确命令事件, 并将所有白天的事件视为在 Home Assistant 时区的午夜开始 。 使用 `homeassistant.util.dt.now()` 获取该时区的当前时间 。

`initial_color` 在首次添加实体时, 存储在 [非常大实体登记处](/core/entities/registry) 的实体选项中 。 之后,用户拥有颜色,可以在实体设置中更改. 无效的颜色被忽略 。

每个实体的通用属性,如`name`或`available`,都在[实体类别](/core/entities/entity-class)上。

## 支持的特性 {#supported-features}

将 `CalendarEntityFeature` 旗与的目的是 `|` 合并起来, 并实行每个旗与牌的方法 。

| 特性 | 实施方法 |
| --- | --- |
| `CREATE_EVENT` | `async_create_event` |
| `DELETE_EVENT` | `async_delete_event` |
| `UPDATE_EVENT` | `async_update_event` |

变化事件必须小心处理RFC 5545字段的整合:保留他们不知道的字段,并支持经常性事件.

## `CalendarEvent` 类 {#the-calendarevent-class}

A `CalendarEvent` 是日历上的一个事件 。 当你创造它时 它会验证自己

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `start` | `datetime \| date` | 要求数 | 活动的开始,包容。 |
| `end` | `datetime \| date` | 要求数 | 的可持续活动 |
| `summary` | `str` | 要求数 | 活动名称. |
| `description` | `str \| None` | `None` | 更长的描述。 |
| `location` | `str \| None` | `None` | 事发之处. |
| `uid` | `str \| None` | `None` | 事件独有的ID. 需要更新或删除。 |
| `recurrence_id` | `str \| None` | `None` | 确定一个反复发生的事件。 需要改变一次事件。 |
| `rrule` | `str \| None` | `None` | 重现规则, 如 `FREQ=DAILY` 。 |
| `status` | `CalendarEventStatus \| None` | `None` | `CONFIRMED` or `TENTATIVE`. |

`start`和`end`均为日期,为全天活动,或为同一时区的两个日期。 全天活动使用 `date` , 午夜从没有约会时间 。 如果一天的活动有相同的开始和结束,则一天后结束移动.

仅在日历报告时设置 `status` 。 无状态的事件与确认的事件不同. 日历实体根本不返回已取消的事件: 过滤它们而不是报告它们的状况 。

## 方法 {#methods}

### 获取事件 {#get-events}

```python
async def async_get_events(
    self,
    hass: HomeAssistant,
    start_date: datetime.datetime,
    end_date: datetime.datetime,
) -> list[CalendarEvent]:
```

要求。 将事件按时间范围退回,以便扩大经常性事件。 `start_date`被比作一个事件的结尾, `end_date`和开始, 两者都是独家的。 两者都位于当地Home Assistant时区.

这种方法可以授权日历面板, `calendar.get_events` 动作, 以及实时更新 。 前端以 `calendar/event/subscribe` WebSocket 命令订阅范围内的事件 。 每当实体写出状态时,基础类会调用这种方法,并将结果推给订阅者,解禁后,如此一阵突如其来的更新就会导致一个获取. 你不执行任何为此。 创建、更新或删除事件不会写入状态 。 当事件在州外改变时,请打电话`self.async_update_event_listeners()`来推动新的事件。

### 创建事件 {#create-events}

```python
async def async_create_event(self, **kwargs: Any) -> None:
```

添加一个事件 。 关键词是 RFC 5545 字段, 如 `summary`, `dtstart` 和 `dtend`。 需要 `CREATE_EVENT` 。

### 删除事件 {#delete-events}

```python
async def async_delete_event(
    self,
    uid: str,
    recurrence_id: str | None = None,
    recurrence_range: str | None = None,
) -> None:
```

需要积极行动 `DELETE_EVENT` 。 关于经常性积极行动:

- 只有`uid`:删除整个系列.
- `uid` 和 `recurrence_id`: 删除一次事件 。
- `uid`、`recurrence_id`和`recurrence_range`:删除一系列事件,从`recurrence_id`开始。 RFC 5545只允许 [范围](https://www.rfc-editor.org/rfc/rfc5545#section-3.2.13) `THISANDFUTURE` 。

### 更新事件 {#update-events}

```python
async def async_update_event(
    self,
    uid: str,
    event: dict[str, Any],
    recurrence_id: str | None = None,
    recurrence_range: str | None = None,
) -> None:
```

需要 `UPDATE_EVENT`. `uid`, `recurrence_id` 和 `recurrence_range` 工作与删除相同 。

## 状态 {#states}

基数类将状态设定为`event`. 不设置 `state` 自己 。

| 状态 | 含义 |
| --- | --- |
| `on` | 现在正在发生一件事。 |
| `off` | 现在没有事情发生。 |

`message`,`all_day`,`start_time`,`end_time`,`location`和`description`属性描述当前或下一个事件. 基础类也为事件开始或结束的时刻安排状态更新.

## 示例 {#example}

只读日历 :

```python
import datetime

from homeassistant.components.calendar import CalendarEntity, CalendarEvent
from homeassistant.core import HomeAssistant

class ExampleCalendar(CalendarEntity):
    """Calendar from an example service."""

    _attr_has_entity_name = True
    _attr_name = None

    def __init__(self, client: ExampleClient, calendar_id: str) -> None:
        """Initialize the calendar."""
        self._client = client
        self._attr_unique_id = calendar_id
        self._event: CalendarEvent | None = None

    @property
    def event(self) -> CalendarEvent | None:
        """Return the current or next upcoming event."""
        return self._event

    async def async_update(self) -> None:
        """Fetch the current or next event."""
        self._event = await self._client.get_next_event()

    async def async_get_events(
        self,
        hass: HomeAssistant,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
    ) -> list[CalendarEvent]:
        """Return the events in a time range."""
        return await self._client.get_events(start_date, end_date)
```
