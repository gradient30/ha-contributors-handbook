---
title: 行动登记册
description: 动作注册系统如何在下面运作,动作处理器得到什么,如何从代码调用动作.
sidebarGroup: 核心内容
order: 4
sidebarLabel: 动作
---

# 行动登记册 {#the-action-registry}

本页面解释动作登记册在下面的工作方式:处理者得到什么,数据如何被验证,以及动作如何被称为. 要在您的整合中注册动作, 请在 `services.yaml` 中描述, 并返回回复数据, 请见 [综合ẩار الك الك الك الك الك الك الك الك الك .](/core/integrations/actions) 。

一个[动作](/glossary/action)是Home Assistant在请求时可以做的事情,比如`light.turn_on`或`weather.get_forecasts`. 自动化,脚本,仪表板,语音助理,以及API都是调用动作. 每个动作都在 `hass.services` 上的动作登记册中 。

> [!NOTE]
> 行动以前称为服务。 代码仍然几乎在任何地方都表示服务:`hass.services`,`ServiceCall`,`services.yaml`,和`call_service`事件. 在文字中,写动作. 在代码中,使用代码所使用的名称.

## 登记处 {#the-registry}

`hass.services.async_register(domain, service, handler)` 向登记册添加动作 。 返回数据的动作需要可选的 `schema` 和 `supports_response` 。 整合应该从`async_setup`,通过`async_setup_services`在它们的`services.py`中注册他们的动作. 见[在 async 设置中注册动作](/core/integrations/actions#register-actions-in-async_setup).

Home Assistant 使用 `probatio` 来设计计划 。 导入为 `probatio` , 没有别名 。 当你注册一个计划, 它运行于您的处理器之前, 所以无效的数据从来没有到达你。 如果他们在操作器之前, 没有计划, `call.data`就是打电话者发送的。

## 处理器 {#the-handler}

处理器得到 `ServiceCall` , 与 :

- `call.data`:验证数据,只读.
- `call.context`:该呼叫的`Context`,与启动它的用户. 交给你代表他们做的一切 见[权限](/core/internals/permissions).
- `call.domain`和 `call.service`: 哪个动作被调用 。
- `call.return_response`:呼叫者是否要求响应数据.
- `call.hass`: Home Assistant实例 。

处理器可以是coroutine函数,用 `@callback` 装饰的函数,也可以是普通函数. plain 函数运行于执行器中, 如 [事件听众](/core/internals/events#listen-for-events) 。

当出事时,处理者会提出例外. 它从不返回错误代码,也不在响应数据中. 要加薪的例外是[提出错误](/core/integrations/actions#raise-errors)。

对实体采取行动的行动不会登记一个普通的处理者。 `async_register_platform_entity_service`从`homeassistant.helpers.service`解决用户所选择的目标(实体,设备,区域,地板,或标签),检查权限,并调用每个目标实体的方法. 见[我会尽力的](/core/integrations/actions#entity-actions).

## 要求行动 {#call-an-action}

```python
await hass.services.async_call(
    "light",
    "turn_on",
    {"brightness": 255},
    target={"entity_id": "light.kitchen"},
    blocking=True,
    context=call.context,
)
```

- `blocking=True`等待行动完成, 并提出它的例外。 在 `blocking=False` 中, 调用在背景中开始, 而错误只结束在日志中 。
- `return_response=True` 返回响应数据 。 它只与`blocking=True`一起工作,并且只用于支持响应的行动.
- `context`:通过引起这个电话的上下文,所以它被正确归属.

要求自己采取行动是不寻常的。 直接跟自己的密码说话 调用另一个集成的行动,主要是自动化和脚本所做的事情.

## 盖子下面发生了什么 {#what-happens-under-the-hood}

当一个动作被调用时, 登记簿会查看处理器, 如果有的话, 对照计划验证数据, 在 [事件总线](/core/internals/events) 上发射 `call_service` 事件, 并运行处理器 。 `hass.services.async_services()` 返回所有注册的, `hass.services.has_service(domain, service)` 检查一个 。 注册和删除动作会点燃`service_registered`和`service_removed`事件。
