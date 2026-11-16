---
title: 设置失败和例外
description: 设备下线时重试设置,在证书失败时开始重新校正,并在动作中提出正确的例外.
sidebarLabel: 设置失败和例外
sidebarGroup: 设置和配置
order: 9
---

# 设置失败和例外 {#setup-failures-and-exceptions}

设备下线 服务中断 密码失效 您的整合必须从中恢复, 一旦问题消失, 用户就不会重新启动 Home Assistant 。 您不为此写入重试循环 : 您提出正确的例外, 而 Home Assistant 其余部分 。

## 设置期间 {#during-setup}

从`__init__.py` `async_setup_entry` 中提高 :

| 例外 | 用它的时候 | Home Assistant 会做什么? |
| --- | --- | --- |
| `ConfigEntryNotReady` | 页:1 | 将条目输入 `SETUP_RETRY` , 并用越来越长的延迟重试, 最多10分钟 |
| `ConfigEntryAuthFailed` | 全权证书不再有效 | 将条目输入 `SETUP_ERROR` 并启动 [重新校正流量](/core/integrations/reauth-reconfigure#reauthentication) |
| `ConfigEntryError` | 有点不对劲,重试不会修好 | 将条目放入 `SETUP_ERROR` 而不重试 |

三个都住在`homeassistant.exceptions`。

```python
from homeassistant.exceptions import (
    ConfigEntryAuthFailed,
    ConfigEntryNotReady,
)

async def async_setup_entry(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Set up Example from a config entry."""
    client = ExampleClient(entry.data[CONF_HOST], entry.data[CONF_TOKEN])

    try:
        await client.connect()
    except ExampleAuthError as err:
        raise ConfigEntryAuthFailed(
            translation_domain=DOMAIN,
            translation_key="invalid_auth",
        ) from err
    except ExampleConnectionError as err:
        raise ConfigEntryNotReady(
            translation_domain=DOMAIN,
            translation_key="cannot_connect",
            translation_placeholders={"host": entry.data[CONF_HOST]},
        ) from err
    ...
```

从整合本身的 `async_setup_entry` 提升它们 。 一个平台的`async_setup_entry`运行太晚:当它提高`ConfigEntryNotReady`,`ConfigEntryAuthFailed`,或`ConfigEntryError`,Home Assistant只记录一个错误并跳过该平台时. 它不重试,也不开始重新校正。

如果您在第一次更新失败时为您使用 [数据更新协调员](/core/integrations/fetching-data), `await coordinator.async_config_entry_first_refresh()` 提高 `ConfigEntryNotReady`, 而协调员的 `ConfigEntryAuthFailed` 开始在任何时间重新校正, 而不仅仅是在设置时 。

如果您的集成支持发现, Home Assistant 一旦再次发现此设备, 也会立即重试 。 当在 Home Assistant 仍在启动时设置失败时, 重试会等待启动完成 。

### 讯息 {#the-message}

例外信息在集成版的页面上出现,因此用户知道是怎么回事. 使用翻译信件, 如上面的例子, 在`strings.json`对这种文字进行翻译 :

```json
{
  "exceptions": {
    "cannot_connect": {
      "message": "Could not connect to the Example device at {host}."
    },
    "invalid_auth": {
      "message": "The token of your Example account is no longer valid."
    }
  }
}
```

如果您不发出消息, Home Assistant 将会在您提出 `from` 另一个例外时, 接受引起它 的例外 。

不要自己登录问题。 Home Assistant 登录重试, 而一个充满相同警告的日志对任何人都没有帮助 。

### 减轻贫穷 {#wait-before-retrying}

如果设备或服务在再次可用时表示,如速率限制重妇女参与政治或`Retry-After`标题,通过秒数作为`retry_after`. Home Assistant 当它比正常的延迟时间长时, 在下一次尝试中使用它, 最多一天 :

```python
except ExampleRateLimitError as err:
    raise ConfigEntryNotReady(
        translation_domain=DOMAIN,
        translation_key="rate_limited",
        retry_after=err.retry_after,
    ) from err
```

## 根据 YAML 设置的平台 {#platforms-set-up-from-yaml}

从YAML中设置平台的集成,由 `async_setup_platform` 来提升 `PlatformNotReady` 代替 。 Home Assistant然后重试平台设置. 它记录了第一次重试作为警告,后来在调试级别记录.

## 行动和实体方法的例外 {#exceptions-in-actions-and-entity-methods}

当一个动作失败时,用户会在UI,自动化跟踪或者称为它的脚本中看到错误. 提出与出错匹配的例外 :

| 例外 | 用它的时候 |
| --- | --- |
| `ServiceValidationError` | 用户做错什么了, 比如无效的值组合 |
| `HomeAssistantError` | 其它故障, 如设备没有响应 |

差别在于唤者复得甚么.试验性的 WebSocket API 前端使用的, 报告 `service_validation_error` 或 `home_assistant_error` , 和 REST API 以状态 400 或 500 回答 。 在默认日志级别上也没有用堆栈跟踪记录。

提升`ServiceValidationError`而不是`ValueError`。淌出规则适用于[动作](/core/integrations/actions)和动作要求的实体方法,如`async_turn_on`或`async_set_hvac_mode`.

```python
from homeassistant.exceptions import HomeAssistantError

async def async_turn_on(self, **kwargs: Any) -> None:
    """Turn the switch on."""
    try:
        await self.coordinator.client.turn_on()
    except ExampleConnectionError as err:
        raise HomeAssistantError(
            translation_domain=DOMAIN,
            translation_key="communication_error",
            translation_placeholders={"error": str(err)},
        ) from err
```

`HomeAssistantError`和所有扩展它的例外都接受`translation_domain`,`translation_key`和`translation_placeholders`. 翻译信件以用户语言出现. 翻译的例外是[质量尺度](/core/quality-scale)的黄金级规则。
