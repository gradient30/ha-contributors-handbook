---
title: 编写测试
description: 集成的测试是如何组织的,如何通过Home Assistant而不是围绕它进行测试,以及如何使用固定装置,模拟和快照.
sidebarGroup: 写代码
order: 4.5
---



# 编写测试 {#writing-tests}
核心中的每一个整合都伴随着测试,对核心的每一个变化也伴随着测试. 测试证明,你的改变是有效的, 更重要的是,当别人在明年改变东西时,它继续发挥作用。 这页是关于写那些测试。 运行它们、检查覆盖和更新快照的命令在 [运行测试](/core/development/testing) 上 。

## 测试文件夹 {#the-test-folder}

测试在 `tests/components/<domain>/` 中, 在所有其它整合的测试旁边 。 AirGradient 集成的测试是这样的:

```text
tests/components/airgradient/
├── __init__.py
├── conftest.py
├── fixtures/
├── snapshots/
├── test_button.py
├── test_config_flow.py
├── test_diagnostics.py
├── test_init.py
├── test_number.py
├── test_select.py
├── test_sensor.py
├── test_switch.py
└── test_update.py
```

| 文件 | 它所持有的 |
| --- | --- |
| `__init__.py` | 需要测试才能找到测试 剂量就够了,就像`"""Tests for the AirGradient integration."""`。 |
| `conftest.py` | 此集成测试共用的 Pytest 固定装置, 如模拟库客户端和 `MockConfigEntry` |
| `fixtures/` | 设备或服务的样本数据,如 JSON 响应 |
| `snapshots/` | 测试生成的快照文件 。 不要用手编辑它们。 |
| `test_init.py` | `__init__.py`  有没有测试 : 设置、 重新装入、 卸 自从配置条目, 设置失败 |
| `test_config_flow.py` | 配置流程流程、选项流程以及重新校正和重组的测试 |
| `test_<platform>.py` | 每个平台一个文件, 如 `test_sensor.py` |
| `test_<feature>.py` | 整合中每个其它部分有一个文件, 如 `test_diagnostics.py` |

规则很简单:每个您的整合文件都有一个测试文件,以它命名,前面有 `test_`.

## 测试通过 Home Assistant {#test-through-home-assistant}

测试您的集成方式 Home Assistant 使用方式 : 通过其公共界面, 永远不要浏览集成的内部 。 这样的测试在集成重构时继续工作.

- 与 `hass.config_entries.async_setup()` 或 `async_setup_component()` 设置集成, 如果它没有配置条目 。
- 从国机读取实体状态,与 `hass.states.get()`.
- 通过 `hass.services.async_call()` 呼叫动作 。
- 在设备和实体登记册中检查设备和实体。
- 检查配置项的状态及其 `state` 属性 。
- 从 `pytest_homeassistant.common` 创建配置项 `MockConfigEntry` 。

对帮助器函数或纯逻辑的焦点单位测试可以直接调用该代码. 这很好,只要整合的行为通过Home Assistant测试.

## 修复和嘲笑 {#fixtures-and-mocking}

测试运行时没有真正的设备或服务. 共享设置进入固定装置, 在 `conftest.py` 整合测试中。 一个典型的集成有一个固定的配置条目,一个嘲弄库,一个设置全部.

锁定您的整合用途库, 而不是 Home Assistant 。 将库的客户端类别补丁到您集成导入的地方, 并给出您需要的数据 :

```python
@pytest.fixture
def mock_example_client() -> Generator[MagicMock]:
    """Return a mocked Example client."""
    with patch(
        "homeassistant.components.example.coordinator.ExampleClient",
        autospec=True,
    ) as client_mock:
        client = client_mock.return_value
        client.get_status.return_value = Status(temperature=21.5)
        yield client
```

锁定协奏器 `hass` 帮助者, 或实体内部进行测试, 并跳过您想要测试的代码 。

将样本数据,像设备的JSON反应一样,放在测试的`fixtures/`文件夹中,并加载到`pytest_homeassistant.common`中的帮助者. `load_fixture("status.json", DOMAIN)` 返回 `tests/components/<domain>/fixtures/status.json` 的文本 `load_json_object_fixture` 和 `load_json_array_fixture` 将其解析为 JSON 。 在async代码中,使用`async_`版本,如`await async_load_json_object_fixture(hass, "status.json", DOMAIN)`:他们在事件循环之外阅读文件.

Core 对您经常需要的东西也有固定装置, 如 `hass`, `entity_registry`, `device_registry`,`hass_ws_client` 对 WebSocket API, 和`issue_registry` 。 其他一些公约:

- 给一个测试函数的每个参数一个类型注释,具体类型如`HomeAssistant`或`MockConfigEntry`,而不是`Any`。
- 使用 `@pytest.mark.usefixtures` 来设定您需要的但不要在测试中使用 。
- 使用 `@pytest.mark.parametrize` 当多个测试用不同的输入做同样的事情时. 以 `pytest.param(..., id="name")` 命名案件 。
- 在测试中避免 `if` 语句 。 分试,或以虚化.
- 的了解时间 。的了解 :
- 硬码实体ID是罚款。 复次如是令为常.
- 测试没有网络接入. Home Assistant外面的一切都被嘲笑了。

### 与其他整合共享固定装置 {#sharing-fixtures-with-other-integrations}

一个实体集成,如`light`或`sensor`,可以提供其他集成在其测试中使用的固定装置. 例如,它可以在 [`tests/components/conftest.py`](https://github.com/home-assistant/core/blob/dev/tests/components/conftest.py) 中添加固定根,并将执行放到 `tests/components/<domain>/common.py` 中.

## 快照测试 {#snapshot-tests}

一个快照测试将您代码的结果与存储的参考:快照进行比较. 这是一种快速检查大产出更加有效地方法,如所有实体的状况、诊断堆放场或登记册条目。 核心用于此 [锡鲁皮](https://github.com/syrupy-project/syrupy) 。

要同时测试一个平台的每个实体, 请使用 `snapshot_platform` 帮助 :

```python
async def test_sensors(
    hass: HomeAssistant,
    mock_example_client: MagicMock,
    mock_config_entry: MockConfigEntry,
    entity_registry: er.EntityRegistry,
    snapshot: SnapshotAssertion,
) -> None:
    """Test the Example sensors."""
    with patch(
        "homeassistant.components.example.PLATFORMS", [Platform.SENSOR]
    ):
        await setup_integration(hass, mock_config_entry)

    await snapshot_platform(
        hass, entity_registry, snapshot, mock_config_entry.entry_id
    )
```

`snapshot_platform`一次只为一个平台工作,因此,一个拥有更多平台的集成在测试中限制了它们,就像上面一样. 对一个残疾实体来说,它也是失败的。提供技术支助,如果一些实体默认被禁用,请在测试中添加 `entity_registry_enabled_by_default` 固定值, 这样它们就可以被启用, 并最后出现在快照中 。

第一次,测试失败,因为还没有快照。 [罗汉: 更新快照](/core/development/testing#update-snapshots),它们最终会出现在`tests/components/example/snapshots/`中,在一个以测试文件命名的可读的`.ambr`文件中. 将您的零钱交给他们, 并读读 diff : 一个快照只证明一些东西, 如果您检查它是正确的 。

快将包括功能测试。 为了将包括一个实体在设备故障时无法进入的测试,可以断言:

```python
assert hass.states.get("sensor.example_temperature").state == STATE_UNAVAILABLE
```

这说明你所期望的, 和失败的原因正确。

## 测试什么 {#what-to-test}

- **Config 流量**:每一步和每一次错误,流量在错误发生后恢复,仍然生成条目. 测试同一设备的第二个设置会中止 。 审查者经常先阅读这些测试.
- **Setup**:集成载荷和卸载,设备安装时下线时会发生什么.
- ** Errors**:当设备稍后下线,返回垃圾,或者证书停止工作时会发生什么. 这是测试员最想要的
- ** Bug 修补**:没有你修补的测试失败,随即通过.
- ** Avoid Brittle 值**:不依赖于更新图书馆时的变化数据,就像今年的节假日一样.

[整合质量尺度](/core/quality-scale)的青铜级要求全测试覆盖配置流,参见[配置- 流量- 测试- 覆盖](/core/quality-scale/config-flow-test-coverage). 从Silver开始,每个集成模块都需要95%以上的覆盖率,参见[试验覆盖](/core/quality-scale/test-coverage).

[教程](/core/integrations/tutorial#9-write-the-tests) 显示一个小集成的一整套测试.
