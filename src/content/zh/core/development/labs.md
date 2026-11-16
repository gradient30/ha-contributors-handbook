---
title: Labs 预览功能
description: 载运完成的特性,人们可以选择通过Home Assistant 实验室,收集反馈, 并毕业到标准。
sidebarLabel: 实验室
sidebarGroup: 改变行为
order: 3
---



# Labs 预览功能 {#labs-preview-features}
Home Assistant实验室允许人们在成为标准之前选择一个预览功能. 用户在 **Settings ** > **System ** > **Labs **下查找,可以打开和关闭每个功能.

实验室功能完成并测试。 仍然开放的是它的设计: 它的外观,作用,以及它应该做什么, 由人们在家里使用它的反馈来塑造。 这使得实验室不同于β,它测试了整个释放的稳定性.

预览功能为:

- ** 默认关闭**:用户打开它们自己。
- ** 生产准备就绪**:经过充分测试,不是试验或半试验。
- ** 选择更改**:他们可以更改、增加或根据反馈被删除。
- ** 可更新**:用户可以随时再次关闭,无需重启.

## 何时使用实验室 {#when-to-use-labs}

鳕鱼的实验室

- 接口的重大阐释或重新设计
- 结构的重大变化
- 用户反馈将塑造最终设计的特征

实验室不适合:

- 应该只是集成的一部分 用组合的选项来做那些。
- 微小的改变,可以直接进入释放
- Home Assistant 运行时无法打开或关闭的特性
- 有已知关键错误的特征, 或尚未完成 。 那些留在发展之中。

## 添加预览功能 {#add-a-preview-feature}

### 将它写进清单 {#1-declare-it-in-the-manifest}

为落实您的整合在 `manifest.json` 中添加特性 `preview_features` :

```json
{
  "domain": "example",
  "name": "Example",
  "preview_features": {
    "new_dashboard": {
      "feedback_url": "https://community.home-assistant.io/t/...",
      "learn_more_url": "https://www.home-assistant.io/integrations/example",
      "report_issue_url": "https://github.com/home-assistant/core/issues/new"
    }
  }
}
```

- `feedback_url`:人们提供反馈的地方,比如论坛话题或GitHub讨论.
- `learn_more_url`:该特性的文档.
- `report_issue_url`:人们报告错误的地方.

三者皆可选,但加之:没有它们,你想要的反馈就无处可去.

然后运行繁忙, 将特性添加到 [`homeassistant/generated/labs.py`](https://github.com/home-assistant/core/blob/dev/homeassistant/generated/labs.py) :

```shell
python3 -m script.hassfest
```

### 2.  添加文本 {#2-add-the-text}

`strings.json` 中的特性名称和描述 :

```json
{
  "preview_features": {
    "new_dashboard": {
      "name": "New dashboard",
      "description": "Replaces the Example panel with a new dashboard."
    }
  }
}
```

说出该功能的作用,并提及该功能能否根据反馈增长. 你可以使用马克唐。

如果打开或关闭该特性会产生后果,人们应该知道,就像再次关闭时停留的移民一样,在描述中解释这一点。 您也可以添加 `enable_confirmation` 和 `disable_confirmation` , 以取代标准确认信件 。 利用它们来提醒人们行为时的后果. 它们不能取代描述。

### 3. 检查旗帜 {#3-check-the-flag}

在 Python 中, 请检查该特性是否在 :

```python
from homeassistant.components.labs import async_is_preview_feature_enabled

async def async_setup_entry(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Set up Example from a config entry."""
    if async_is_preview_feature_enabled(hass, DOMAIN, "new_dashboard"):
        await async_setup_new_dashboard(hass)
    else:
        await async_setup_classic_panel(hass)
```

将预览代码和标准代码明确分开,像这样. 将`preview=True`旗子传到您的代码深处, 以后很难移除其中之一。

在前端, `fetchLabFeatures` 从[`src/data/labs.ts`](https://github.com/home-assistant/frontend/blob/dev/src/data/labs.ts) 返回特性以及它们是否被启用 。

### 4.  打开或关闭时的反应 {#4-react-when-it-is-turned-on-or-off}

预览功能在 Home Assistant 运行时打开或关闭, 不重新启动 。 这是一项艰巨的要求。 订阅 `async_subscribe_preview_feature` 的更改, 它只为您自己的功能调用您的听众 :

```python
from homeassistant.components.labs import (
    EventLabsUpdatedData,
    async_subscribe_preview_feature,
)

async def async_setup_entry(
    hass: HomeAssistant, entry: ExampleConfigEntry
) -> None:
    """Set up Example from a config entry."""

    async def _async_preview_toggled(
        event_data: EventLabsUpdatedData,
    ) -> None:
        if event_data["enabled"]:
            await async_setup_new_dashboard(hass)
        else:
            await async_remove_new_dashboard(hass)

    entry.async_on_unload(
        async_subscribe_preview_feature(
            hass, DOMAIN, "new_dashboard", _async_preview_toggled
        )
    )
```

运行时效果良好的事物:装入和卸载界面的部分内容,创建和移除实体,开始和停止背景任务,以及注册事件听众. 不这样做的事情:改变 Home Assistant 如何开始, 更改仅在启动时加载的集成, 以及需要更改 `configuration.yaml` 中的任何内容 。

我现在可以直接听 `EVENT_LABS_UPDATED` 事件。

### 5.  准备反馈 {#5-prepare-for-feedback}

在发布特性前, 创建反馈位置: [社区论坛](https://community.home-assistant.io/) 上的话题, 或者 GitHub 讨论或问题 。 链接到 `feedback_url` 。 将您囤积在 [Home Assistant.io](https://www.home-assistant.io/) 上的开展能力建设 : 它能做什么, 需要什么反馈, 以及如何打开 。

一个 {L鳕} 链接将人们直接带到你在实验室的功能, 并突出它。 这在发布说明、文件和论坛文章方面是行之有效的:

```text
https://my.home-assistant.io/redirect/labs/?domain=example&preview_feature=new_dashboard
```

[厨房沉](https://github.com/home-assistant/core/tree/dev/homeassistant/components/kitchen_sink)集成有一个完整的例子,有一个预览功能,可以产生修复问题.

## 测试两个状态 {#test-both-states}

测试您的整合功能是否打开或关闭, 并测试切换功能 。 首先,在设置集成前填充 Labs 的存储:

```python
async def test_new_dashboard(
    hass: HomeAssistant,
    hass_storage: dict[str, Any],
    mock_config_entry: MockConfigEntry,
) -> None:
    """Test the integration with the new dashboard enabled."""
    hass_storage["core.labs"] = {
        "version": 1,
        "data": {
            "preview_feature_status": [
                {"domain": DOMAIN, "preview_feature": "new_dashboard"},
            ]
        },
    }
    mock_config_entry.add_to_hass(hass)
    await hass.config_entries.async_setup(mock_config_entry.entry_id)
```

要在测试中切换它, 请用 `hass_ws_client` 固定方式发送 `labs/update` 消息 :

```python
client = await hass_ws_client(hass)
await client.send_json_auto_id(
    {
        "type": "labs/update",
        "domain": DOMAIN,
        "preview_feature": "new_dashboard",
        "enabled": True,
    }
)
assert (await client.receive_json())["success"]
```

## 当它处于 还有预览 {#while-it-is-in-preview}

- 注意反馈 并采取行动 尽快解决虫子
- 允许在预览中更改断开事物, 但可以在您可以时避免 。 如果有必要,请自动迁移用户的数据和设置。 人们在家中依赖这个,预览与否.
- 随着特征的变化,保持描述准确.
- 不要永远在实验室留下一个特征。 从一开始就计划如何毕业 或者如何消失

## 你真该去掉 {#graduate-or-remove}

当特性准备好成为标准时:

1. 从 `preview_features` 中移除它 。
2. 取消国旗的检查,所以特性总是在.
3. 运行`python3 -m script.hassfest`。
4. ukoi 文档更新,并在发布说明中宣布.

当它失败时:

1. 从 `preview_features` 中移除它 。
2. 删除`strings.json` 中的代码和文本 。
3. 运行`python3 -m script.hassfest`。
4. 在释放说明中宣布删除,并解释原因.
