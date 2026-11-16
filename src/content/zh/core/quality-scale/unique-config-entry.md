---
title: 防止重复配置条目
description: 青铜规则独占-配置-入口:同一设备或服务不能两次设置.
sidebarLabel: 唯一配置输入
sidebarGroup: 青铜
order: 20
---

# 防止重复配置条目 {#prevent-duplicate-config-entries}

此是铜法. 在`quality_scale.yaml`中,它被称为`unique-config-entry`.

配置流必须阻止用户两次设置相同的设备或服务. 每次流量,包括发现流量,当设备或服务已经拥有一个配置条目时都会中止.

## 为什么这很重要 {#why-it-matters}

建立从UI的整合是很容易的,所以两次偶然设置也很容易. 同一设备的两个条目意味着重复的设备和实体,以及碰撞的独特ID. 发现让情况更糟:没有办法识别已知的装置,Home Assistant不断提出再次设置.

## 示例 {#example}

有两种方法可以做到这一点。

### 拥有独有的ID {#with-a-unique-id}

给配置项一个 [唯一标识](/glossary/unique-id), 如设备的序列号, 当存在该 ID 条目时中止 。 这是首选方法,因为它也允许发现识别设备:

```python
async def async_step_user(
    self, user_input: dict[str, Any] | None = None
) -> ConfigFlowResult:
    """Handle a flow started by the user."""
    errors: dict[str, str] = {}
    if user_input is not None:
        client = MyClient(user_input[CONF_HOST])
        try:
            info = await client.get_device_info()
        except MyConnectionError:
            errors["base"] = "cannot_connect"
        else:
            await self.async_set_unique_id(info.serial_number)
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title=info.name, data=user_input)

    return self.async_show_form(
        step_id="user",
        data_schema=probatio.Schema({probatio.Required(CONF_HOST): str}),
        errors=errors,
    )
```

独一无二的ID只得在您的整合中独有. 采用最近的 r 的 r , 以 r 和 r 的 r 的 r 和 r 的 r , 不要使用 IP 地址或主机名: 这些更改 。

### 有独特的数据 {#with-unique-data}

当设备没有可用的标识符时, 比较现有条目的数据 :

```python
if user_input is not None:
    self._async_abort_entries_match({CONF_HOST: user_input[CONF_HOST]})
```

当存在一个带有同一主机的条目时,流终止 `already_configured` 。

## 如何检查 {#how-it-is-checked}

- Hasfest, 当规则是 `done` 时: 配置流必须调用 `_async_abort_entries_match`, 或同时调用 `async_set_unique_id` 和 `_abort_if_unique_id_configured` 。 与 `single_config_entry` 合并时, 会在列表中通过此检查 。
- Pylint, 对于每个集成: `home-assistant-unique-id-ip-based` 当 `async_set_unique_id` 得到 IP 地址或主机名时警告 。
- Pylint: `home-assistant-tests-config-flow-unique-id` 当一个配置流程测试创建一个条目而不检查其唯一ID时警告.
- 重复案件的测试为[配置- 流量- 测试- 覆盖](/core/quality-scale/config-flow-test-coverage)的一部分.

## 例外 {#exceptions}

仅支持单一配置条目的集成可以免除此规则. 通常,在 `manifest.json` 中设定为 `"single_config_entry": true` 。

## 相关规则 {#related-rules}

- [配置流量](/core/quality-scale/config-flow):从UI设置有配置流.
- [提交的文件 你还好吗?](/core/quality-scale/test-before-configure):测试配置流中的连接.
- {L刚好} : 完全测试配置流 。
- [发现](/core/quality-scale/discovery):支持发现.
- [重新校正流量](/core/quality-scale/reauthentication-flow):从UI中重新认证.
- [重组流程](/core/quality-scale/reconfiguration-flow):从UI重新配置.
