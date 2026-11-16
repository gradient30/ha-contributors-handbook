---
title: 气象实体
description: 报告当前天气状况,每日、小时或每日两次预报。
sidebarLabel: 天气
sidebarGroup: 传感器与状态
---

# 气象实体 {#weather-entity}

一个气象实体在一个地点报告当前天气:情况,温度,以及读数如湿度和风. 它也可以为预测服务。 从`WeatherEntity`继承,从`homeassistant.components.weather`导入。 如果您使用 [协调员](/glossary/coordinator), 请从 `CoordinatorWeatherEntity` 或 `SingleCoordinatorWeatherEntity` 继承 `SingleCoordinatorWeatherEntity` 代替 (参见 [使用协调员](/core/entities/weather#using-coordinators)) 。

看薛前端如何显示天气实体,参见[鳕瓷器鹳姥ễ龛آ](/design/more-info/weather).

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。商讨日时预报 闭嘴! 预测由目前状况和温度的演示组成。

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
        "entity_id": "weather.home",
        "state": "partlycloudy",
        "attributes": {
          "friendly_name": "Home",
          "temperature": 14,
          "temperature_unit": "°C",
          "humidity": 72,
          "wind_speed": 12,
          "wind_speed_unit": "km/h",
          "supported_features": 3
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "weather.home",
        "features": [
          {
            "type": "temperature-forecast"
          }
        ]
      }
    </script>
  </ha-embed-card>
  <ha-embed-card style="grid-column: span 12">
    <script type="application/json">
      {
        "type": "weather-forecast",
        "entity": "weather.home",
        "forecast_type": "daily"
      }
    </script>
  </ha-embed-card>
</ha-embed-provider>
```

## 的临时议程 {#properties}

设定其   native 单位的每个值, 并告诉 Home Assistant 是哪个单位 。 基类将数值转换为用户的单位系统,或用户在实体设置中选择的单位.

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `condition` | `str \| None` | `None` | 多谢 此 多谢州.是否可以 但如果 太棒了" 用 多谢 {是否可以 但如果 太棒了 [他们是条件](/core/entities/weather#conditions) 之一 。 |
| `native_temperature` | `float \| None` | `None` | 目前温度 |
| `native_temperature_unit` | `str \| None` | `None` | 坚定地致力于这方面的工作后才在可能的情况下。 |
| `native_apparent_temperature` | `float \| None` | `None` | 目前的表面(感觉)温度。 |
| `native_dew_point` | `float \| None` | `None` | 露露点. |
| `humidity` | `float \| None` | `None` | nó掀 |
| `native_pressure` | `float \| None` | `None` | 气压。 |
| `native_pressure_unit` | `str \| None` | `None` | 接着 他要所作出的等因素评述带头更积极地才可 ― đã的刚好是: 当设置 `native_pressure` 时设置它 。 |
| `native_wind_speed` | `float \| None` | `None` | 婶渍萌 缇霞缪ىaunt茁زetta硕 藜诘躬酝渍抒 |
| `native_wind_gust_speed` | `float \| None` | `None` | 风涌之速. |
| `native_wind_speed_unit` | `str \| None` | `None` | 两条风速的单位:博福特,ft/s,km/h,kn,m/s,或mph. 确定风速 |
| `wind_bearing` | `float \| str \| None` | `None` | 风向,以度数或作为1至3个字母罗盘方向. |
| `native_visibility` | `float \| None` | `None` | 可见度. |
| `native_visibility_unit` | `str \| None` | `None` | 可见度的单位:km或mi. 当设置 `native_visibility` 时设置它 。 |
| `native_precipitation_unit` | `str \| None` | `None` | 预测中的降水单位:毫米或英寸. |
| `cloud_coverage` | `int \| None` | `None` | 云覆盖率,单位:%. |
| `uv_index` | `float \| None` | `None` | 紫外线娇色指数. |
| `ozone` | `float \| None` | `None` | 臭氧水平。 |
| `precision` | `float` | °C为十分之一, °F为整数 | 转换后的温度精度. |

当一个 `native_*_unit` 是 `None` 时, 基准类假设该值已经在用户单位系统的默认单位中, 当用户为实体选择另一个单位时, 从该单位转换 。 因此设定您所报告各种值的单位 。

每个实体的通用属性,如`name`或`available`,都在[实体类别](/core/entities/entity-class)上。 在实践中,每个气象实体至少设定`condition`,`native_temperature`和`native_temperature_unit`.

## 支持的特性 {#supported-features}

每个预测类型都是`WeatherEntityFeature`中的旗. 与他联系,让他与他联系

| 特性 | 实施方法 |
| --- | --- |
| `FORECAST_DAILY` | `async_forecast_daily` |
| `FORECAST_HOURLY` | `async_forecast_hourly` |
| `FORECAST_TWICE_DAILY` | `async_forecast_twice_daily` |

我希望----就其基本 我想到的

## 条件 {#conditions}

使用这些值 我只是  没有 `condition` 。 它们 这样 我不想社团化 别:“ 没问题 !

| ụ nó 翎恣梢凛咀徘آ滔颐几句鸠凹 周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周周 | 含义 |
| --- | --- |
| `clear-night` | 清净的夜晚 |
| `cloudy` | 大家都 我们现在列有 我以为承担起并同将之 看到 他妈的 而是能够得到 你先能够获得听听 我跟你问题以及展开了 |
| `exceptional` | 特别 |
| `fog` | 雾|
| `hail` | 万岁 |
| `lightning` | 闪电或雷电 |
| `lightning-rainy` | 闪电或雷暴和雨 |
| `partlycloudy` | 几经云. |
| `pouring` | 之雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨,雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨雨 |
| `rainy` | 风雨 |
| `snowy` | 在其各自 |
| `snowy-rainy` | 雪和雨 |
| `sunny` | 阳光 |
| `windy` | 风 |
| `windy-variant` | 风云 |

它们作为`ATTR_CONDITION_*`常数在`homeassistant.components.weather`中提供,如`ATTR_CONDITION_SUNNY`.

## 预测 {#forecasts}

预测不属于州. 像积极地使用前端的消费者通过一个单独的API订阅,而`weather.get_forecasts`动作返回它们. 基类将预测值转换为用户的单位,就像当前值一样.

### `Forecast` 词典 {#the-forecast-dictionary}

每种预测方法都以本地单位返回`Forecast`字典列表:

| 密钥 | 类型 | 说明 |
| --- | --- | --- |
| `datetime` | `str` | 要求。 预报时间,在协调世界时,作为RFC 3339字符串. |
| `is_daytime` | `bool \| None` | 无论是白天还是晚上 每日两次预测所需经费。 |
| `condition` | `str \| None` | 条件 |
| `native_temperature` | `float \| None` | (高)温. |
| `native_templow` | `float \| None` | 低温 |
| `native_apparent_temperature` | `float \| None` | 明显的温度。 |
| `native_dew_point` | `float \| None` | 露露点. |
| `humidity` | `float \| None` | nó掀 |
| `native_pressure` | `float \| None` | 气压。 |
| `native_precipitation` | `float \| None` | 降水量. |
| `precipitation_probability` | `int \| None` | 降水机率,单位:%. |
| `native_wind_speed` | `float \| None` | 婶渍萌 缇霞缪ىaunt茁زetta硕 藜诘躬酝渍抒 |
| `native_wind_gust_speed` | `float \| None` | 风涌之速. |
| `wind_bearing` | `float \| str \| None` | 风. . . . . . . . . . .  . . .  . . . . . .     .  .  . . . . .  .  . .   . . ..  .  .  . .  ..  . ...         .  . .  . . . .  .. ..... . .. ..  ..    .. . . . .  .    .... . . . .. .  .... ... .. ... . . .. ... . . .. ..  .  . . .  .  . . . . ... . . . . |
| `cloud_coverage` | `int \| None` | 云覆盖率,单位:%. |
| `uv_index` | `float \| None` | 紫外线娇色指数. |

这些单位与当前值的属性相同 `native_*_unit`。

### 更新预测 {#updating-forecasts}

缓存您获取的预测, 因此您不会在每次询问时给 API 打电话 。 当您有新的预测数据时, 请等待 {H0 让我视情况向每个订阅者推, 或是通过一个预测类型的列表, 如 `["daily"]`, 只按这些 。 当没有人订阅时,它根本不称为你的预测方法。

### 使用协调员 {#using-coordinators}

`CoordinatorWeatherEntity`将一个天气实体连接到[协调员](/glossary/coordinator):一个用于当前观测,可以选择每个预测类型一个. 传到 `__init__` 作为 `daily_coordinator`, `hourly_coordinator` 和 `twice_daily_coordinator` 。 而不是模拟预测方法,您执行调用符 `_async_forecast_daily`, `_async_forecast_hourly` 和 `_async_forecast_twice_daily` , 这些调用符是从协调器数据读取的 。 协调员更新时会更新听众。

预测协调员必须是`TimestampDataUpdateCoordinator`。 实体只听预测协调员,而有人则接受这种预测。 当需要预测而其协调员的数据比`update_interval`要老时,实体首先给协调员刷新。 将 `daily_forecast_valid` 、 `hourly_forecast_valid` 或 `twice_daily_forecast_valid` 传到 `__init__` , 设定一个预测在实体返回 `None` 之前可能达到的年代 。 它默认为协调员的`update_interval` 。 一个没有 `update_interval` 的协调员, 就像只接收被驱动数据的协调员一样, 跳过两个检查: 实体从不刷新它, 也从不拒绝它的预测为太老 。

`SingleCoordinatorWeatherEntity`是一位同时持有观察和预测的协调员的捷径.

## 方法 {#methods}

### 预测 {#forecasts-1}

```python
async def async_forecast_daily(self) -> list[Forecast] | None:
async def async_forecast_hourly(self) -> list[Forecast] | None:
async def async_forecast_twice_daily(self) -> list[Forecast] | None:
```

只执行您在支持的特性中声明的功能 。 没有同步变体.

## 状态 {#states}

州为`condition`. 当前值成为状态属性,在用户的单位中. 不设置 `state` 自己 。

## 示例 {#example}

每日预报的气象实体:

```python
from homeassistant.components.weather import (
    Forecast,
    WeatherEntity,
    WeatherEntityFeature,
)
from homeassistant.const import UnitOfSpeed, UnitOfTemperature

class ExampleWeather(WeatherEntity):
    """Weather from an example service."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_native_temperature_unit = UnitOfTemperature.CELSIUS
    _attr_native_wind_speed_unit = UnitOfSpeed.METERS_PER_SECOND
    _attr_supported_features = WeatherEntityFeature.FORECAST_DAILY

    def __init__(self, client: ExampleClient, location_id: str) -> None:
        """Initialize the weather entity."""
        self._client = client
        self._attr_unique_id = location_id

    async def async_update(self) -> None:
        """Fetch the current weather."""
        current = await self._client.get_current()
        self._attr_condition = current.condition
        self._attr_native_temperature = current.temperature
        self._attr_native_wind_speed = current.wind_speed

    async def async_forecast_daily(self) -> list[Forecast] | None:
        """Return the daily forecast."""
        days = await self._client.get_daily_forecast()
        return [
            Forecast(
                datetime=day.date.isoformat(),
                condition=day.condition,
                native_temperature=day.high,
                native_templow=day.low,
            )
            for day in days
        ]
```
