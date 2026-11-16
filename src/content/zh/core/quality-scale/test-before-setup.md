---
title: 设置时检查连接
description: 青铜器规则测试-设置前:设置检查其有效,不成立时提出正确的例外.
sidebarLabel: 设置前测试
sidebarGroup: 铜
order: 19
---

# 设置时检查连接 {#check-the-connection-during-setup}

此是铜法. 在`quality_scale.yaml`中,它被称为`test-before-setup`.

设置配置条目时, `async_setup_entry` 必须检查整合是否可行, 并在无法时提出正确的例外 :

- 当问题暂时存在时,就像一个离线的设备. Home Assistant 稍后重试设置 。
- 当证书错误或过期时 。 Home Assistant如果整合肛门有一个,则开始重校正流.
- 当问题不会自己消失, 就像一个关闭的账户。 Home Assistant 不重试 。

## 为什么这很重要 {#why-it-matters}

这些例外是用户是如何发现某事出错的. 安置卡 ** 安置卡 ** > 嗨, 戴维克斯 & Services ** 显示该条目没有设置, 以及为什么, 而不是默默无声的实体从未得到一个值 。 Home Assistant 也为您处理重试, 有备份, 所以你不必自己写 。

## 示例 {#example}

将库的例外情况映射到设置例外 :

```python
async def async_setup_entry(hass: HomeAssistant, entry: MyConfigEntry) -> None:
    """Set up My integration from a config entry."""
    client = MyClient(entry.data[CONF_HOST])

    try:
        await client.connect()
    except MyConnectionError as err:
        raise ConfigEntryNotReady(
            translation_domain=DOMAIN,
            translation_key="cannot_connect",
        ) from err
    except MyAuthenticationError as err:
        raise ConfigEntryAuthFailed(
            translation_domain=DOMAIN,
            translation_key="invalid_auth",
        ) from err

    entry.runtime_data = client
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
```

你经常免费得到这个。 当 [协调员](/glossary/coordinator) 第一次更新失败时, 将 `await coordinator.async_config_entry_first_refresh()` 和 `ConfigEntryAuthFailed` 和 `ConfigEntryError` 的更新通过 。 `await session.async_ensure_token_valid()` 在 OAuth2 会话上, 当令牌无法刷新时, 提出正确的例外 。

在升起前不要自己登录错误 : Home Assistant 已经报告了这些例外, 对于`ConfigEntryNotReady` 它会登录每次重试 。

### 经常离线的设备 {#devices-that-are-often-offline}

一些设备是故意下线的,比如夜间的太阳能反转器或备用电视机. 提升 `ConfigEntryNotReady` 和让 Home Assistant 重试通常是最简单的方法 。 但也可以在不到达设备的情况下完成设置. 用 `await coordinator.async_refresh()` 刷新协调员, 它不会升起, 并且实体在设备回复前不可用 。 由更新方法提出的 `ConfigEntryAuthFailed` 仍然开始重校正流 。 在此之前,`coordinator.data`仍然是`None`,所以在设置平台时读取它的代码必须处理. 在设备返回后, 获取任何无法在设置时得到的东西, 如设备信息 。 错误不是暂时的,如错误的证书或关闭的账户,在设置时发现时仍然必须报告.

## 如何检查 {#how-it-is-checked}

- Hasfest, 当规则是 `done` 时 : `async_setup_entry` 必须等待 `async_config_entry_first_refresh` 或 `async_ensure_token_valid` , 或 集成必须提高 `ConfigEntryNotReady` , `ConfigEntryAuthFailed` 或 `ConfigEntryError` 的代码 。
- Pylint: `home-assistant-log-and-raise` 当一个错误在警告级别或更高时被记录,然后升起时警告 。
- 是否针对每次失败提出正确的例外, 检查中 。

## 例外 {#exceptions}

如果集成在设置过程中无法检查其配置,或者它只进行局部计算,则该规则不适用.

## 相关规则 {#related-rules}

- [运行时间数据](/core/quality-scale/runtime-data):在运行时间数据中存储运行时间数据。
- [无法获取的实体的人数](/core/quality-scale/entity-unavailable): 酌情标记不可用的实体。
