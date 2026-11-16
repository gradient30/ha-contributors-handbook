---
title: 传感器实体
description: 报告只读值,如温度,功率读数,或时间戳,与其单位,选择长期统计.
sidebarLabel: 传感器
sidebarGroup: 传感器和状态
---

# 传感器实体 {#sensor-entity}

感应器是一个只读实体,它报告一个值:温度,电源一个插头绘图,一个设备上次启动的时间,或者一个固定的文本列表状态之一. 它可以携带一个计量单位,并且Home Assistant将该单位转换成用户喜欢的单位. 从`SensorEntity`继承,从`homeassistant.components.sensor`导入。

当值超过两个状态且用户无法更改时使用传感器. 二州为[二进制传感器](/core/entities/binary-sensor). 用户集的值是 [编号](/core/entities/number),[选择](/core/entities/select) 或[文本](/core/entities/text) 实体 。

从 Home Assistant 演示中嵌入的仪表板卡的现场演示。 温度和电源传感器在瓦片卡。 趋势图由每个传感器当前状态的演示组成.

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
        "entity_id": "sensor.living_room_temperature",
        "state": "21.4",
        "attributes": {
          "friendly_name": "Living room temperature",
          "device_class": "temperature",
          "state_class": "measurement",
          "unit_of_measurement": "°C"
        }
      },
      {
        "entity_id": "sensor.washing_machine_power",
        "state": "1850",
        "attributes": {
          "friendly_name": "Washing machine power",
          "device_class": "power",
          "state_class": "measurement",
          "unit_of_measurement": "W"
        }
      }
    ]
  </script>
  <ha-embed-card style="grid-column: span 6">
    <script type="application/json">
      {
        "type": "tile",
        "entity": "sensor.living_room_temperature",
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
        "entity": "sensor.washing_machine_power",
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
</ha-embed-provider>
```

## 的临时议程 {#properties}

您在其   native  单位、 设备或服务报告单位中设置值 。 从不设定 `state` 或 `unit_of_measurement` 自己: 基类拥有它们, 将本地值转换为用户想要的单位, 并验证结果 。

| 名称 | 类型 | 默认 | 说明 |
| --- | --- | --- | --- |
| `native_value` | `str \| int \| float \| date \| datetime \| Decimal \| None` | 要求数 | 值, 在 `native_unit_of_measurement` 中。 设备类可以限制允许哪些类型. |
| `device_class` | `SensorDeviceClass \| None` | `None` | 感应器能测量什么 见[设备类](/core/entities/sensor#device-classes). |
| `native_unit_of_measurement` | `str \| None` | `None` | 单位 。 当您提供翻译单位时, 请取消它( 见下文) 。 |
| `state_class` | `SensorStateClass \| None` | `None` | 这算什么价值? 设置它标记传感器为数值, 并将其选择为 [交涉](/core/entities/sensor#long-term-statistics) 。 |
| `last_reset` | `datetime \| None` | `None` | 当一个累积传感器开始一个新的测量周期时. 只允许使用 `SensorStateClass.TOTAL` 。 |
| `options` | `list[str] \| None` | `None` | 具有 {H0 200)} 设备类的传感器可能状态 。 无法与州级或 200)}单位合并 。 |
| `suggested_display_precision` | `int \| None` | `None` | 前端显示的十进制数 。 州本身不圆. |
| `suggested_unit_of_measurement` | `str \| None` | `None` | 显示单位值的单位,而不是单位系统选择的单位值。 首次看到传感器时存储在实体登记处,之后只有在用户更改单元系统时更新. |

每个实体的通用属性,如`name`或`available`,都在[实体类别](/core/entities/entity-class)上。

一个传感器永远不能拥有 `config` [实体类别](/glossary/entity-category): Home Assistant 拒绝添加它 。 对信号强度等传感器使用`EntityCategory.DIAGNOSTIC`.

### 单位 {#units}

基数类选择它按此顺序显示的单位:

1. 在实体设置中设置的用户单位 。
2. 初始单位,存储在实体登记册中,用于唯一ID:`suggested_unit_of_measurement`的传感器,否则用户的单位系统更喜欢设备类的单位. 没有独特ID的传感器直接使用`suggested_unit_of_measurement`.
3. 用户单位系统的温度单位,用于具有`temperature`设备类的传感器,以及一个当地单位°C或°F.
4. 翻译的单位: `unit_of_measurement` `entity` 一节中的名称旁边的密钥, 由 `translation_key` 查阅 。 用于属于单词的单位,如"步". 带有翻译单元的传感器不能设置 `native_unit_of_measurement` 。
5. {`native_unit_of_measurement`.

用户可以改变任何设备类有单位转换器的传感器的单位,只要本地单元和新单元都对该设备类有效.

使用来自 `homeassistant.const` 的单位常数, 如 `UnitOfTemperature.CELSIUS`, 而不是将单位写为字符串 。 自定义字符串只看起来像一个被支持的单位,比如`KWh`而不是`kWh`,算作不同的单位.

### 在国际范围内恢复该值 {#restoring-the-value}

要恢复重启后的值, 请从 `RestoreSensor` 继承 `RestoreEntity` 而不是 `RestoreEntity` 。 `RestoreEntity` 存储已转换状态, 它可能位于与原值不同的单位 。 在 `async_added_to_hass` 中调用 `await self.async_get_last_sensor_data()` 以获取 `native_value` 和 `native_unit_of_measurement` 。

### 属性 {#attributes}

对于经常变化的值,不要在传感器中添加`extra_state_attributes`。 每一个带有改变属性的状态变化都会写入数据库. 创建另一个传感器。 见[状态和属性](/core/entities/state-attributes).

## 支持的特性 {#supported-features}

该实体没有支持的特性。

## 设备类 {#device-classes}

[设备类](/glossary/device-class)告诉Home Assistant什么是感应度量。 它设置图标,单位转换,以及前端如何显示值. 具有设备类的传感器,除`enum`外,其设备类没有命名. 见[名称](/core/entities/naming)。

设置设备类时,单位必须是为其列出的单位之一,状态类必须是设备类允许的单位之一. Home Assistant 当它们不匹配时登录一个警告 。 值栏是您在 YAML 中设置的值, 例如 `device_class` 的 [传感器 MQTT](https://www.home-assistant.io/integrations/sensor.mqtt/) 或 [模板传感器](https://www.home-assistant.io/integrations/template/) 的 `device_class` 。

非后才数设备类不取单位而无状态类:

| 设备类 | 数值 | 说明 |
| --- | --- | --- |
| `SensorDeviceClass.DATE` | `date` | 约会 `native_value`必须是 `datetime.date`。 |
| `SensorDeviceClass.ENUM` | `enum` | 一个固定的列表 文本状态。 设定`options`. |
| `SensorDeviceClass.TIMESTAMP` | `timestamp` | 一时一时. `native_value`必须是有时区的`datetime`。 |
| `SensorDeviceClass.UPTIME` | `uptime` | 当设备上次启动时, 作为带有时区的 `datetime` 。 更新之间小于60秒的修改被忽略,因此从一个更新时计数器计算出的启动时间不会改变每次更新时的状态. 将 `_attr_uptime_drift_tolerance` 设定为数秒以改变容忍度( 至少 5) 。 |

数字设备类别及其单位:

| 设备类 | 数值 | 单位 | 说明 |
| --- | --- | --- | --- |
| `ABSOLUTE_HUMIDITY` | `absolute_humidity` | g/m³, mg/m³ | 绝对湿度 |
| `APPARENT_POWER` | `apparent_power` | mVA、V柠檬、KVA | Apparent power |
| `AQI` | `aqi` | 无 | 空气质量指数 |
| `AREA` | `area` | mm², cm², m², km², in², ft², yd², mi², ac, ha | 区域 |
| `ATMOSPHERIC_PRESSURE` | `atmospheric_pressure` | 帕, hPa, kPa, mPa, cbar, mbar, bar, psi, inHg, inH2O, mmHg, atm | 大气压力 |
| `BATTERY` | `battery` | % | 电池里左充电 |
| `BLOOD_GLUCOSE_CONCENTRATION` | `blood_glucose_concentration` | mg/dL, mmol/ (升) L级 | 血糖浓度 |
| `CO` | `carbon_monoxide` | ppb, ppm, 微克/立方米, 毫克/立方米 | 一氧化碳浓度 |
| `CO2` | `carbon_dioxide` | 页:1 | 二氧化碳浓度 |
| `CONDUCTIVITY` | `conductivity` | S/cm, mS/cm, μS/cm | 导电性 |
| `CURRENT` | `current` | A, mA, μA | 电流 |
| `DATA_RATE` | `data_rate` | 位/s, kbit/s, Mbit/s, Gbit/s, B/s, kB/s, MB/s, GB/s, KiB/s, MiB/s, GiB/s | 数据率 |
| `DATA_SIZE` | `data_size` | 位, kbit, Mbit, Gbit, B, kB, MB, GB, TB, PB, EB, ZB, YB, KiB, MiB, GiB, TiB, PiB, EiB, ZiB, YiB | các 微软 |
| `DISTANCE` | `distance` | 毫米、厘米、米、公里、英寸、英尺、yd、mi、nmi | 距离 |
| `DURATION` | `duration` | μs、ms、s、min、h、d | 长短. 它只应在受制于设备报告新值时改变,而不是因为时间流逝。 |
| `ENERGY` | `energy` | J, kJ, MJ, GJ, mWh, Wh, kWh, MWh, GWh, TWh, cal, kcal, Mcal, Gcal, thm | 使用或生产的能源,如电表。 不与权相惑. |
| `ENERGY_DISTANCE` | `energy_distance` | kWh/100公里,W出版物/km,mi/kWh,km/kWh | 电动车的消耗量 |
| `ENERGY_STORAGE` | `energy_storage` | 与 `ENERGY` 相同 | 储存的能量,就像家用电池的电荷 |
| `FREQUENCY` | `frequency` | mHz, Hz, kHz, MHz, GHz | 频率 |
| `GAS` | `gas` | L, m³, ft³, CCF, MCF | 气积. kWh 测量的气体为 `ENERGY`. |
| `HUMIDITY` | `humidity` | % | 相对湿度 |
| `ILLUMINANCE` | `illuminance` | lx | 光级 |
| `IRRADIANCE` | `irradiance` | W/m2,BTUửa/(h⋅ft2) | 光泽 |
| `MOISTURE` | `moisture` | % | 湿度 |
| `MONETARY` | `monetary` | ISO 4217 货币编码 | 现在有钱 |
| `NITROGEN_DIOXIDE` | `nitrogen_dioxide` | ppb, ppm, 微克/立方米 | 二氧化氮浓度 |
| `NITROGEN_MONOXIDE` | `nitrogen_monoxide` | ppb,微克/立方米 | 一氧化氮浓度 |
| `NITROUS_OXIDE` | `nitrous_oxide` | μg/m³ | 二氧化二氮浓度 |
| `OZONE` | `ozone` | ppb, ppm, 微克/立方米 | 臭氧浓度 |
| `PH` | `ph` | 无 | ,,中,中,中,中,,要求对,中,,中,中,,中,,中,中,,,,中,,,,中,中,,中中,中,,中中,,中,,,,中,,,,中中中,中中,,,中,,,中中,中,,中,,中,中,,中,,中中,,,中中中中中中,,,,中中中中中中中中,,,,,,,,中中中中中,,,,,中中中,,中中,中,,,,,,中中,中,中中中中中中中,中中中中中,中,,中中中中中中中中,中中中,中中中中中中中,中中中中中中中中中中中中中,中中中,中中,中中,中中中中中中中中中中中中中中中中中中中中中中中中中中中中中中好中中中中中中中中中中中 |
| `PM1`, `PM25`, `PM4`, `PM10` | `pm1`, `pm25`, `pm4`, `pm10` | μg/m³ | 小于1、2.5、4或10微米的分块物质 |
| `POWER` | `power` | mW, W, kW, MW, GW, TW | 权力 |
| `POWER_FACTOR` | `power_factor` | %,无 | 将作为动力因素 |
| `PRECIPITATION` | `precipitation` | mm, cm, in | 累计降水量 |
| `PRECIPITATION_INTENSITY` | `precipitation_intensity` | mm/h, mm/d, in/h, in/d | 降水强度 |
| `PRESSURE` | `pressure` | 与 `ATMOSPHERIC_PRESSURE` 相同 | 压力 |
| `RADON` | `radon` | Bq/m3, pCi/升 (单位:千美元) | 放射性浓度 |
| `REACTIVE_ENERGY` | `reactive_energy` | 瓦尔,克瓦尔 | 反应能量 |
| `REACTIVE_POWER` | `reactive_power` | mvar, var, kvar (英语). | 反应力 |
| `SIGNAL_STRENGTH` | `signal_strength` | DB, dBm (英语). | 信号强度 |
| `SOUND_PRESSURE` | `sound_pressure` | dB, dBA (英语). | 声音压力 |
| `SPEED` | `speed` | mm/s, in/s, ft/s, m/s, m/min, km/h, mph, kn, Beaufort, mm/h, mm/d, in/h, in/d | 速度 |
| `SULPHUR_DIOXIDE` | `sulphur_dioxide` | ppb,微克/立方米 | 二氧化硫浓度 |
| `TEMPERATURE` | `temperature` | °C, °F, K | 温度 还有 |
| `TEMPERATURE_DELTA` | `temperature_delta` | °C, °F, K | 两个温度的区别 |
| `VOLATILE_ORGANIC_COMPOUNDS` | `volatile_organic_compounds` | μg/m³, mg/m³ | 挥发性有机化合物,作为一种浓度 |
| `VOLATILE_ORGANIC_COMPOUNDS_PARTS` | `volatile_organic_compounds_parts` | 页:1 | 挥发性有机化合物,作为比率 |
| `VOLTAGE` | `voltage` | μV, mV, V, kV, MV | 电压 |
| `VOLUME` | `volume` | mL、L、am、m3、的基础、CCF、MCF | 使用的体积,就像车用的燃料 |
| `VOLUME_FLOW_RATE` | `volume_flow_rate` | mL/s, L/s, L/min, L/h, m³/s, m³/min, m³/h, ft³/min, gal/min, gal/h, gal/d | 就像水流流过水管一样 |
| `VOLUME_STORAGE` | `volume_storage` | 与 `VOLUME` 相同 | 像油箱里的燃料一样储存的体积 |
| `WATER` | `water` | L, gal, m3, ft3, CCF, MCF (英语). | 用水量 |
| `WEIGHT` | `weight` | μg, mg, g, kg, oz, lb, st | 弥撒. 它被称为体重,因为那是日常的词汇。 |
| `WIND_DIRECTION` | `wind_direction` | ° | 风向. 报告`None` 当风太少,无法测量方向时。 |
| `WIND_SPEED` | `wind_speed` | mm/s, in/s, ft/s, m/s, m/min, km/h, mph, kn, Beaufort (英语). | 风速 |

每个设备类允许的状态类在 `DEVICE_CLASS_STATE_CLASSES` [`homeassistant/components/sensor/const.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/sensor/const.py) 中 。 大多数只允许 `measurement`. `AREA`, `DATA_SIZE`, `DISTANCE`, `DURATION`, 和`PRECIPITATION` 允许每个州级, 而`WEIGHT` 允许 `measurement`,`total`, 和`total_increasing` 。 计数到上的设备类,如`ENERGY`,`GAS`,`WATER`,`VOLUME`和`REACTIVE_ENERGY`,只允许`total`和`total_increasing`. `MONETARY`只允许`total`,`WIND_DIRECTION`只允许`measurement_angle`.

## 国家等级 {#state-classes}

[州级](/glossary/state-class) 表示值是多少 。 仔细挑选:它决定哪些统计数据 Home Assistant保留。 值列是您在 YAML 中设置的值, 例如 `state_class` 的 [传感器 MQTT](https://www.home-assistant.io/integrations/sensor.mqtt/) 或 [模板传感器](https://www.home-assistant.io/integrations/template/) 的 `state_class` 。

| 国家等级 | 数值 | 用它 Is it for |
| --- | --- | --- |
| `SensorStateClass.MEASUREMENT` | `measurement` | 现时测量的值,如当前温度或电量. 不是预测,也不是昨天的总和 |
| `SensorStateClass.MEASUREMENT_ANGLE` | `measurement_angle` | 现在的测量角度是度, 像风向。 |
| `SensorStateClass.TOTAL` | `total` | 一个可以上下移动的总数,就像一个净能量计. |
| `SensorStateClass.TOTAL_INCREASING` | `total_increasing` | 一个总的,只是从零开始 时不时地重新开始,就像一个日用气体计。 |

大多数情况下,您想要`MEASUREMENT`,或者`TOTAL`没有`last_reset`。

## B. 长期统计 {#long-term-statistics}

具有州级的传感器获得长期统计,每5分钟编译一次. 对于一些设备类,统计被认定的单位是正常的,因此不同单位的传感器适合一个图.

- ** 计量** (`MEASUREMENT` 和 `MEASUREMENT_ANGLE`) 获得每个周期的最小、最大和平均值。
- ** 总计** (`TOTAL` 和 `TOTAL_INCREASING`) 得到运行的 `sum` 。 统计首次编译时的值为零点.

### 在总班级之间选择 {#choosing-between-total-classes}

- 值从不重置, 如设备的寿命能量使用 : `TOTAL`, 没有 `last_reset` 。
- 值只上升,有时重排为0,就像一个与计费月对齐的能量计:`TOTAL_INCREASING`.
- 值上下,在已知时刻重置, 如每计费月净能量 `TOTAL`, 当重置时更新 `last_reset` 。
- 每一次更新都是一个新时期,就像最后一分钟使用的能量: `TOTAL`,并且随着每个状态的变化更新`last_reset`.

与 `TOTAL` 相比, 总数会随着新值和旧值的差别而增长 。在这一方面 `last_reset`  这位 `last_reset` 更改时, 新周期从 0 开始 : 重置后的第一个值会全部添加 。 在下面的4: 00,3已经算数了.

| 时间 | 状态 | `last_reset` | 总和 |
| --- | --- | --- | --- |
| 13:00 | 1000 | 13:00 | 0 |
| 14:00 | 1010 | 13:00 | 10 |
| 15:00 | 1005 | 13:00 | 5 |
| 16:00 | 3 | 16:00 | 8 |
| 17:00 | 8 | 16:00 | 13 |

在 `TOTAL_INCREASING` 中, 值的下降开始一个新的度量周期, 而该周期也从 0 开始计算, 因此, 值的下降后的第一个值会被全部添加 。 低于10%的下降被视作噪音,而不是重置. 确定您从吵闹的读数中计算出的值不能错掉 。

| 时间 | 状态 | 总和 |
| --- | --- | --- |
| 13:00 | 1000 | 0 |
| 14:00 | 1010 | 10 |
| 15:00 | 2 | 12 |
| 16:00 | 7 | 17 |

### 移动到支援单位 {#moving-to-a-supported-unit}

如果您的集成使用自定义单位字符串并移动移动到一个支持的单位,则统计会将它作为单位改变并停止为该传感器编译. 为了避免出现这种情况,在您与 `async_custom_equivalent_units` 函数的整合中添加 `recorder.py` 平台 。 它返回,每个实体的ID, 旧单位等于支持单位。

```python
from homeassistant.const import UnitOfEnergy
from homeassistant.core import HomeAssistant, callback

@callback
def async_custom_equivalent_units(
    hass: HomeAssistant,
) -> dict[str, dict[str | None, str]]:
    """Return custom equivalent units per entity ID."""
    return {
        "sensor.example_energy": {"KWh": UnitOfEnergy.KILO_WATT_HOUR},
    }
```

## 方法 {#methods}

一个传感器没有动作,所以除了保持`native_value`的电流之外,没有什么可以执行的. 在 `update` 或 `async_update` 中获取数据, 或用 `async_write_ha_state` 推动 。 见[更新状态](/core/entities/state-updates).

## 状态 {#states}

状态为 `native_value`,转换为向用户显示的单位 。 日期和时间戳写成ISO 8601字符串,时间戳转换成UTC. A `None` 值显示为 `unknown` 。

## 示例 {#example}

从设备读取其值的温度传感器:

```python
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import UnitOfTemperature

class ExampleTemperatureSensor(SensorEntity):
    """Temperature of an example device."""

    _attr_has_entity_name = True
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_suggested_display_precision = 1

    def __init__(self, device: ExampleDevice) -> None:
        """Initialize the sensor."""
        self._device = device
        self._attr_unique_id = f"{device.serial}_temperature"

    async def async_update(self) -> None:
        """Fetch the latest temperature."""
        self._attr_native_value = await self._device.get_temperature()
```

感应器没有名称,所以以其设备类命名:"Temperature".
