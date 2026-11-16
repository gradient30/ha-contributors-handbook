---
title: 完全测试配置流
description: 青铜规则配置-流量-测试-覆盖:配置流程有全测试覆盖,包括从错误中恢复.
sidebarLabel: 配置- 流量- 测试- 覆盖
sidebarGroup: 铜
order: 6
---

# 完全测试配置流 {#test-the-config-flow-fully}

此是铜法. 在`quality_scale.yaml`中,它被称为`config-flow-test-coverage`.

测试范围为`config_flow.py`的100%。 流量可以显示的每一个错误都有一个测试,这个测试然后修复原因并完成流量,以证明用户可以恢复. 创建条目的测试也检查其独特的ID. 该规则涵盖了文件中的每个流量:用户流量,发现,导入,重新校正,重组,以及选项.

## 为什么这很重要 {#why-it-matters}

配置流是用户对您整合的第一件事. 如果它破裂了, 没有人会通过设置。 大多数维护者并不拥有他们每次触碰的集成设备,因此测试是告诉他们一个变化并没有中断设置的.

测试恢复与测试错误同样重要。 显示“ 无法连接” 的流量, 但即使用户解决了问题, 也会被卡住 。 并坚持独有的ID可以确保它如何产生的变化不会被忽略:这会打破每个现有用户的重复检测.

写这些测试也是进入核心测试的好方法. 一旦配置流量被覆盖,测试其余的集成是更小的一步. 见[写作测试](/core/development/tests).

## 示例 {#example}

一个快乐的路径测试运行用户从开始到完成,并检查创建的条目,包括其独特的ID:

```python
async def test_full_flow(
    hass: HomeAssistant,
    mock_my_client: AsyncMock,
    mock_setup_entry: AsyncMock,
) -> None:
    """Test the full user flow."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )
    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "user"

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {CONF_HOST: "192.168.1.2"}
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["title"] == "My device"
    assert result["data"] == {CONF_HOST: "192.168.1.2"}
    assert result["result"].unique_id == "ABC123"
```

错误测试会使客户端失败,检查错误,然后让客户端再次工作并完成流量:

```python
@pytest.mark.parametrize(
    ("exception", "error"),
    [
        (MyConnectionError, "cannot_connect"),
        (MyAuthenticationError, "invalid_auth"),
        (Exception, "unknown"),
    ],
)
async def test_flow_errors(
    hass: HomeAssistant,
    mock_my_client: AsyncMock,
    mock_setup_entry: AsyncMock,
    exception: Exception,
    error: str,
) -> None:
    """Test errors in the user flow, and recovery."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )

    mock_my_client.get_data.side_effect = exception
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {CONF_HOST: "192.168.1.2"}
    )
    assert result["type"] is FlowResultType.FORM
    assert result["errors"] == {"base": error}

    mock_my_client.get_data.side_effect = None
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {CONF_HOST: "192.168.1.2"}
    )
    assert result["type"] is FlowResultType.CREATE_ENTRY
```

重校正或重新配置测试从已有条目开始。 以 `entry.add_to_hass(hass)` 添加 `MockConfigEntry` , 然后以 `await entry.start_reauth_flow(hass)` 或 `await entry.start_reconfigure_flow(hass)` 启动流量 。 当流终止时,测试用 `reauth_successful` 或 `reconfigure_successful` 完成 。

不要忘记重复检查。 快乐路径通常通过[唯一配置输入](/core/quality-scale/unique-config-entry)的代码运行,但添加一个测试,尝试两次设置相同的设备,并期望流量会以`already_configured`中止.

## 如何检查 {#how-it-is-checked}

- Codecov要求每个 pull request `config_flow.py` 中更改的行的100%覆盖 。
- Pylint警告在`test_config_flow.py`中一个快乐路径测试创建条目而不检查其唯一ID(`home-assistant-tests-config-flow-unique-id`)时.
- 当 `test_config_flow.py` 中的测试显示错误时, Pylint 警告, 但之后永远不能完成流量( `home-assistant-tests-config-flow-error-recovery`) 。
- 当一个流显示 `strings.json` 中缺失的翻译密钥时, 核心失败 失败 , 失败 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , 失败 , , 显示 , 显示 , 显示 , , , , , 无法 显示 , , , , 无法显示 , , , , , , , 无法 无法 , 无法 无法 , 无法 , 无法 无法 无法 , , 无法 , , , , 无法 无法 无法 无法 无法 无法 , , 无法 无法

## 例外 {#exceptions}

这一规则没有例外。

## 相关规则 {#related-rules}

- [配置流量](/core/quality-scale/config-flow):从UI设置有配置流.
- [提交的文件 你还好吗?](/core/quality-scale/test-before-configure):测试配置流中的连接.
- [唯一配置输入](/core/quality-scale/unique-config-entry) : 防止重复配置条目 。
- [发现](/core/quality-scale/discovery):支持发现.
- [重新校正流量](/core/quality-scale/reauthentication-flow):从UI中重新认证.
- [重组流程](/core/quality-scale/reconfiguration-flow):从UI重新配置.
