---
title: 校验输入
description: 验证用户在配置 验证、配置流量、动作和YAML中给出的您与 probatio schemas 和帮助者的集成 。
sidebarGroup: 编写代码
order: 6
---



# 校验输入 {#validating-input}
任何用户给出的整合,请在使用前检查. 用于配置流程表、动作数据和YAML配置。 前方一个明显的错误在设定的中途击败了一个令人困惑的失败.

Core 用 [诉讼](https://pypi.org/project/probatio/) 的策略验证输入 。 一个计划说明需要哪个键或可选键,以及每个键接受哪个类型或值.

```python
import probatio

from homeassistant.const import CONF_HOST, CONF_PASSWORD, CONF_PORT
from homeassistant.helpers import config_validation as cv

DEFAULT_PORT = 993

DATA_SCHEMA = probatio.Schema(
    {
        probatio.Required(CONF_HOST): cv.string,
        probatio.Required(probatio.Secret(CONF_PASSWORD)): cv.string,
        probatio.Optional(CONF_PORT, default=DEFAULT_PORT): probatio.Port(),
    }
)
```

在一个配置流中,你通过一个像这样的图案作为一个步骤的`data_schema`. 对YAML来说,计划是整合的`CONFIG_SCHEMA`. 二者皆盖.

## 计划规则 {#rules-for-schemas}

- 导入 probatio 为`import probatio` 。 Ruff 挡住了旧的 `vol` 化名, 它挡住了自己的波动。
- 使用来自 `homeassistant.const` 的 `CONF_*` 常数, 当一个常数存在时, 否则使用您自己的 `const.py` 。
- 先放所需钥匙,然后放可选钥匙。
- 默认必须是有效的值。 从不为字符串使用 `default=None`: 如果您需要默认, 请使用 `default=""` 。

## 配置中的助手  验证 {#helpers-in-configvalidation}

对各国而言, 通常以 `cv` 导入的 `homeassistant.helpers.config_validation` 验证器在 Home Assistant 验证器旁边有 验证器 :

- ** 类型 **:`cv.string`、`cv.byte`、`cv.boolean`
- **实体ID**:`cv.entity_id`,`cv.entity_ids`
- ** 数字**:`cv.small_float`、`cv.positive_int`
- **时间**:`cv.time`,`cv.time_zone`
- ** 其他**: `cv.template`,`cv.slug`,`cv.temperature_unit`,`cv.latitude`,`cv.longitude`,`cv.isfile`,`cv.sun_event`,`cv.url`,`cv.icon`

对于MQTT主题,MQTT集成在[`homeassistant/components/mqtt/util.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/components/mqtt/util.py)中有`valid_subscribe_topic`和`valid_publish_topic`.

一些年长的 `cv` 帮助者现在被薄的包裹 围绕一个 probatio 验证器。 在核心中,一个提示规则让你直接使用probatio版本:

| 改为 | 使用 |
| --- | --- |
| `cv.ensure_list` | `probatio.EnsureList()` |
| `cv.port` | `probatio.Port()` |
| `cv.has_at_least_one_key` | `probatio.AtLeastOne` |
| `cv.has_at_most_one_key` | `probatio.AtMostOne` |

`cv` 名称继续用于自定义集成 。

## 实例 {#examples}

### 限制选择 {#limit-the-choices}

```python
DATA_SCHEMA = probatio.Schema(
    {
        probatio.Optional(CONF_METHOD, default="GET"): probatio.In(
            ["GET", "POST"]
        ),
    }
)
```

### 已知选项列表 {#a-list-of-known-options}

```python
SENSOR_TYPES = {
    "article_cache": ("Article cache", "MB"),
    "average_download_rate": ("Average speed", "MB/s"),
}

DATA_SCHEMA = probatio.Schema(
    {
        probatio.Optional(CONF_MONITORED_VARIABLES, default=[]): probatio.All(
            probatio.EnsureList(), [probatio.In(SENSOR_TYPES)]
        ),
    }
)
```

### 秘诀 {#secrets}

在 `probatio.Secret` 中环绕一个键, 当 这是一个值允许访问, 如密码、 符号、 API 键或 PIN 。的人员验证失败后,错误会给密钥和问题起名,但不给值,所以秘密不会在日志中结束:

```text
Invalid config for 'demo': value should be a string for dictionary value
'password', got **REDACTED**
```

只标出真实的秘密 一个主机名,序列号,或者GPIO的针头并不是秘密,隐藏它使得这个错误对于试图修复其配置的人来说是毫无用处的.
