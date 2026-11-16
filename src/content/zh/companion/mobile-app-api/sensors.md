---
title: 传感器
description: 统计数据 注册应用程序中的传感器和二进制传感器,更新其状态,并保持其启用状态与Home Assistant同步.
order: 4
---



# 传感器 {#sensors}
app可以将自己的传感器和二进制传感器添加到它的设备中 Home Assistant:电池级别,步骤,Wi-Fi网络,无论设备知道什么. 应用程序完全管理它们。 每个都成为应用设备的实体.

## 注册传感器 {#register-a-sensor}

在更新之前,登记每个传感器一次 您每个请求注册一个传感器 :

```json
{
  "type": "register_sensor",
  "data": {
    "type": "sensor",
    "unique_id": "battery_level",
    "name": "Battery level",
    "state": 42,
    "device_class": "battery",
    "unit_of_measurement": "%",
    "state_class": "measurement",
    "entity_category": "diagnostic",
    "icon": "mdi:battery",
    "attributes": {
      "charging": false
    }
  }
}
```

| 密钥 | 要求数 | 类型 | 说明 |
| --- | --- | --- | --- |
| `type` | 对 | 字符串 | `sensor` or `binary_sensor` |
| `unique_id` | 对 | 字符串 | 身份证明,在这个注册中独一无二。 每一次更新都需要它 |
| `name` | 对 | 字符串 | 感应之名. Home Assistant 把设备名称放在前面 |
| `state` | No | 布尔、 数字或字符串 | 当前状态 |
| `device_class` | No | 字符串 | 一个 [传感器](/core/entities/sensor) 或[二进制传感器](/core/entities/binary-sensor) 设备类 |
| `unit_of_measurement` | No | 字符串 | 国家单位 |
| `state_class` | No | 字符串 | 州课. 仅用于传感器,而非二进制传感器 |
| `entity_category` | No | 字符串 | `config` or `diagnostic` |
| `icon` | No | 字符串 | 图标, 如`mdi:battery` 。 默认为 `mdi:cellphone` |
| `attributes` | No | 对象 | 额外的状态属性 |
| `disabled` | No | 布尔 | Home Assistant 是否禁用该实体 |

用 `{"success": true}` 成功注册返回 `201` 。 该实体立即出现。

登记已经存在的传感器是好的。 Home Assistant 更新名称、 设备类、 单位、 实体类别、 图标, 如果更改则启用状态, 并像更新一样应用请求 。 因此,将当前 `state`,`icon` 和 `attributes` 一起发送: 一个左撇子 `state` 使状态未知, 一个左撇子 `icon` 或 `attributes` 回到默认状态 。

## 更新传感器 {#update-sensors}

在一个 我们走 在一个拜托中更新任何传感器 。 { 我们走!

```json
{
  "type": "update_sensor_states",
  "data": [
    {
      "type": "sensor",
      "unique_id": "battery_level",
      "state": 41,
      "icon": "mdi:battery-40",
      "attributes": {
        "charging": false
      }
    }
  ]
}
```

| 密钥 | 要求数 | 类型 | 说明 |
| --- | --- | --- | --- |
| `type` | 对 | 字符串 | `sensor` or `binary_sensor` |
| `unique_id` | 对 | 字符串 | 你登记传感器的身份证 |
| `state` | 对 | 布尔, 数字, 字符串, 或 `null` | 新 state州. 字符串 `unavailable` 标记传感器为不可用 |
| `icon` | No | 字符串 | 图标。 回落到`mdi:cellphone` 被忽略了, 所以, 如果您设置了一个, 请随每次更新一起发送 。 |
| `attributes` | No | 对象 | 状态属性, 替换旧属性 |

更新情况分两步检查:

1. 首先检查整个列表, 在每个传感器上检查一个有效的 `type` 和一个 `unique_id` 。 如果有一个传感器失败了,整个请求都会被拒绝:你得到一个带有 `200` 的空 `{}` , 而没有一个传感器更新 。
2. 然后每个传感器都自己检查 未注册的传感器与 `not_registered` 失败 。 只允许上面的密钥 。咏叹调,如 `name` 或错误类型状态, 会使一个传感器与 `invalid_format` 发生故障 。 其他传感器仍在更新。

第二步之后,反应结果为 `unique_id` :

```json
{
  "battery_level": {
    "success": true
  },
  "steps": {
    "success": true,
    "is_disabled": true
  },
  "pressure": {
    "success": false,
    "error": {
      "code": "not_registered",
      "message": "sensor pressure is not registered"
    }
  },
  "light_level": {
    "success": false,
    "error": {
      "code": "invalid_format",
      "message": "<what is wrong>"
    }
  }
}
```

`not_registered`表示需要先注册传感器. `invalid_format`  不是说更新与计划不符。

## 保持启用状态同步 {#keep-the-enabled-state-in-sync}

用户可以在Home Assistant中禁用实体. 失能感应器不值得在电话中收集:它白费电池。 因此,应用程序和Home Assistant保持每个传感器的启用状态同步,双向:

- **用户在app**中打开或关闭传感器:再次发送`register_sensor`,设定为`true`或`false`。
- ** 该应用程序更新了Home Assistant**}中禁用的传感器:更新成功,但结果包含`"is_disabled": true`. 以它作为从 Home Assistant 获取启用状态的信号 。
- ** 用户在 Home Assistant**} 中打开或关闭一个实体: [`get_config`](/companion/mobile-app-api/sending-data#get_config) 回复包含 `entities`, 它将每个 `unique_id` 映射到其启用状态 。 应用在应用程序中。

```json
{
  "entities": {
    "battery_level": {
      "disabled": false
    },
    "steps": {
      "disabled": true
    }
  }
}
```

官方应用程序的用户管理其传感器,如[传感器文档](https://companion.home-assistant.io/docs/core/sensors)所述.
