---
title: 运动會
description: 如何为 Modbus 设备写一个有 Modbus 连接的库,以及您的整合如何与他人共享一个 Modbus 连接.
sidebarGroup: 你说的
order: 34
---

# 运动會 {#modbus-devices}

Modbus是一个投票协议, 超过序列线和TCP。 它起源于工业,现在在家中出现了太阳能反转器,能量计,热泵和电池. 很多人会说摩德布斯语,别无他法。

像每个集成,一个Modbus集成通过 [图书馆](/core/integrations/api-library) 对其设备进行会谈. 此页面覆盖 Modbus 的特有内容: 共享库以建立,并共享一个连接.

## 在 Modbus 连接上构建您的库 {#build-your-library-on-modbus-connection}

Home Assistant 项目维护 [`modbus-connection`](https://github.com/home-assistant-libs/modbus-connection), 一个 Python 软件包, 用于构建 Modbus 设备库 。 它给你:

- 一个界面在两个流行的Modbus库的顶部,[pymodbus 编辑器](https://github.com/pymodbus-dev/pymodbus)和[调制解调器](https://github.com/wlcrs/tmodbus). 您的库与其中之一工作, 后端可以更改而不更改您的代码 。
- 设置有关设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置、设置
- 一个 `pytest` 插件, 用于测试您的库, 没有硬件 。

完整的例子见[远模车](https://github.com/darkrain-nl/sofar-modbus),一个基于`modbus-connection`的设备库,以及使用它的[`sofar` 整合](https://github.com/home-assistant/core/tree/dev/homeassistant/components/sofar)。

您的库需要 `ModbusUnit` 从 `modbus-connection` 连接到 Modbus 链接上的一个单位, 并且通过它做一切 。 它从来没有打开连接本身。 这正是下一部分的工作原理。

## Share one connection {#share-one-connection}

一个Modbus链接处理许多单元,一个设备一次回答一个请求. 两个集成,每个打开自己的套接字到同一个设备上争吵,两个都有错误.

所以请不要打开您的整合连接 。 询问 `modbus` 集成为单位 。 将所有要求相同联系的人  Fengled.

```python
from modbus_connection import ModbusTcpParams

from homeassistant.components.modbus import async_get_unit

async def async_setup_entry(
    hass: HomeAssistant, entry: MyConfigEntry
) -> None:
    """Set up my device from a config entry."""
    unit = async_get_unit(
        hass,
        entry,
        ModbusTcpParams(
            host=entry.data[CONF_HOST], port=entry.data[CONF_PORT]
        ),
        entry.data[CONF_UNIT_ID],
    )
    entry.runtime_data = MyDevice(unit)
    ...
```

收集您自己的配置流程中的连接细节, 和其他配置一样 。 两种以相同细节要求的集成在一次连接上获得单元,它们的请求排在彼此后面. 对于其他链接,请使用`ModbusUdpParams`,`ModbusTlsParams`或`ModbusSerialParams`.

连接不在任何地方存储 。 它存在,而一些配置条目在它上有一个单元,在最后卸下时关闭. 你的输入数据仍然属于你

询问一个单元没有I/O,所以关闭的设备不会阻止您的整合设置. 第一个请求打开了链接,一个被丢弃的链接在下一个请求中重新打开. 连接下降时不要重新装入您的配置条目 。

如果同一设备已经在使用不同的链接设置, 如另一个 baud 速率, `async_get_unit` 提高 `HomeAssistantError` 。 一种连接不能两者兼有。

## 在配置流程中与设备交谈 {#talk-to-a-device-during-the-config-flow}

在配置流中,还没有配置条目可以绑定一个单元。 与 `async_get_temporary_unit` 保持一秒钟 :

```python
from modbus_connection import ModbusTcpParams

from homeassistant.components.modbus import async_get_temporary_unit

async def async_validate_input(
    hass: HomeAssistant, params: ModbusTcpParams, unit_id: int
) -> None:
    """Check that the device can be reached."""
    async with async_get_temporary_unit(hass, params, unit_id) as unit:
        await MyDevice(unit).async_validate()
```

如果一个配置条目已经持有该连接,则临时单位共享. 否则,当 `async with` 块结束时, 连接会关闭 。
