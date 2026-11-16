---
title: 获取实例 URL
description: 查找一个设备、服务或用户浏览器可以到达的 Home Assistant 的 URL 。
sidebarLabel: 实例 URL
sidebarGroup: 数据与更新
order: 3
---

# 获取实例 URL {#get-the-instance-url}

有时,你的整合必须告诉其他东西如何到达Home Assistant. 设备将数据发送回,云服务称为webhook,或媒体播放器获取生成的图像或声音文件. 为此, 您需要一个 Home Assistant 实例的 URL 。

这比听起来更难。 用户可以拥有多个URL:一个为家用网络设定,一个Home Assistant自行检测,一个为互联网访问设定,另一个为Home Assistant Link. 它们可以使用非标准端口,无论有无SSL. `get_url`帮助者为你挑对了

## 获取url 帮助器 {#the-geturl-helper}

```python
from homeassistant.helpers.network import NoURLAvailableError, get_url

try:
    url = get_url(hass, allow_internal=False, require_ssl=True)
except NoURLAvailableError as err:
    raise ConfigEntryNotReady(
        translation_domain=DOMAIN,
        translation_key="no_external_url",
    ) from err
```

ص 乔安: 如果URL不符合您的要求, 它会提高 `NoURLAvailableError` 。ص 乔接,并告诉用户设置什么.

| 参数假如 | 默认 | 它会做什么 |
| --- | --- | --- |
| `require_current_request` | `False` | URL必须匹配用户在浏览器中打开的 。 如果没有当前请求, 则加薪 。 |
| `require_ssl` | `False` | URL 必须使用 `https` |
| `require_standard_port` | `False` | URL 对 `http` 使用端口 80 , 对 `https` 使用 443 。 |
| `require_cloud` | `False` | URL必须是 Home Assistant Link 網址 |
| `allow_internal` | `True` | 允许用户设置内部URL, 或者在网络上检测到一个 。 如果您需要外部 URL , 设置为 `False` 。 |
| `allow_external` | `True` | 允许用户设置外部 URL, 或 Home Assistant Link URL (中文(简体) ). 如果您需要内部 URL , 设置为 `False` 。 |
| `allow_cloud` | `True` | 允许 Home Assistant Link URL |
| `allow_ip` | 取决于 | 允许IP地址为主机 。 默认允许, 除非 Home Assistant 本身通过 SSL 服务 。 |
| `prefer_external` | 取决于 | 在内部 URL 之前尝试外部 URL 。 默认情况下只当 Home Assistant 本身在 SSL 上服务时 。 |
| `prefer_cloud` | `False` | 将 Home Assistant Link URL 置于用户设置的外部 URL 之上 |

## 默认返回什么 {#what-it-returns-by-default}

没有参数, `get_url(hass)` 允许任何 URL, 更喜欢本地 URL :

1. 在一间获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得在获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得在获得获得获得获得获得获得获得获得获得在获得获得获得获得获得获得在获得获得获得在获得获得获得获得获得获得在获得获得获得获得获得获得在获得获得获得获得获得获得获得在获得获得获得获得获得获得获得获得获得获得在获得获得在获得获得在获得获得获得获得获得获得获得获得在获得获得获得获得获得获得获得在获得获得获得获得在获得获得获得获得获得获得获得获得获得获得获得在获得在获得获得获得获得在获得在获得获得获得获得获得获得获得获得在获得在获得在获得在获得获得获得获得获得获得获得获得获得获得获得在在获得获得获得获得获得获得获得获得在获得在在获得获得获得在在在获得获得获得获得获得获得获得获得获得获得在获得获得获得获得获得获得获得获得获得获得获得获得在在在获得在在获得在获得获得在在获得在获得获得获得在获得在获得获得获得获得在获得在获得在获得在获得一间获得获得获得在获得获得获得获得获得获得获得获得获得获得在获得获得获得获得获得获得获得获得获得获得在获得获得获得获得获得获得获得获得获得获得在获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得在获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得在获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得获得在获得获得获得获得获得在获得获得获得获得获得在获得获得在获得获得获得在获得获得获得获得获得获得获得在在获得获得获得获得在获得获得获得获得获得获得获得获得获得在获得获得获得获得获得获得获得在获得获得获得获得获得获得获得在获得获得获得获得获得获得获得在获得获得获得在获得获得获得在获得获得获得在获得在获得在获得获得在在在获得获得获得获得获得在在获得在获得在在获得在获得获得在获得在获得在在在获得在获得获得在获得在获得获得在在获得获得在在获得在在在在在获得在在获得在获得在获得在在获得在获得在获得在在在在获得在获得在获得在获得在获得在
2. 如果没有内部URL,则由用户设置外部URL.
3. 如果没有,则 Home Assistant Link URL,如果用户有订阅.

当 Home Assistant 本身通过 SSL 服务时, 它先尝试外部 URL, 不允许 IP 地址 。

## 选择你的要求 {#pick-your-requirements}

问问你的用具到底需要什么 再也没有了 每项要求都使得没有URL的可能性更大.

- 本地立足网络的设备调回: 如果设备无法到达互联网, 默认是好的, 或者 `allow_external=False` 。
- 云服务称网呼:`allow_internal=False`. 添加 `require_ssl=True` 如果服务只接受 `https` 。
- 在端口443上只接受`https`并检查证书的设备:`allow_internal=False`,`allow_ip=False`,`require_ssl=True`和`require_standard_port=True`.
