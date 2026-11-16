---
title: 修理费
description: 告诉用户他们需要采取行动的问题,并帮助他们用修理流程来解决这些问题。
sidebarGroup: 集成功能
order: 6
---

# 修理费 {#repairs}

[修理](/glossary/repair) 问题告诉用户需要他们注意的东西, 例如一个太老的固件, 一个正在关闭的 API, 或不再支持的 YAML 配置 。 问题出现在**Settings** > **System** > **Repairs**中. 有些人只解释该怎么做,另一些人可以在那里固定,有修补流程.

修补也是影响用户的{婶婶}如何被宣布的,这是他们最常见的用途之一. 核心API的折旧则在日志中报告给开发者.

## 创建问题 {#create-an-issue}

```python
from homeassistant.helpers import issue_registry as ir

ir.async_create_issue(
    hass,
    DOMAIN,
    "firmware_too_old",
    is_fixable=False,
    severity=ir.IssueSeverity.ERROR,
    translation_key="firmware_too_old",
    translation_placeholders={"version": device.firmware_version},
    learn_more_url="https://www.home-assistant.io/integrations/example",
)
```

| 参数 | 默认 | 这是什么 |
| --- | --- | --- |
| `domain` | | 产生问题的域 |
| `issue_id` | | 这个问题的ID,在域内独一无二. 以现有的ID更新创建一个问题 。 |
| `is_fixable` | | 用户是否可以用修补流程修复问题 |
| `severity` | | 何等为坏. 见下文。 |
| `translation_key` | | `strings.json` 中标题和描述的密钥 |
| `translation_placeholders` | `None` | 向他们提供的文本占位符值 |
| `config_entry_id` | `None` | 问题所属的配置条目 。 这个问题在条目禁用时被隐藏,在条目删除时被删除。 见[属于配置条目的问题](/core/integrations/repairs#issues-that-belong-to-a-config-entry). |
| `config_subentry_id` | `None` | `config_entry_id` 的子条目属于 。 子条目删除后, 这个问题将被删除 。 见[属于配置子条目的问题](/core/integrations/repairs#issues-that-belong-to-a-config-subentry). |
| `breaks_in_ha_version` | `None` | 某事破裂的版本, 如 `"2027.4.0"` |
| `learn_more_url` | `None` | 用户找到更多信息的地方 |
| `is_persistent` | `False` | 这个问题是否在重启后继续存在 。 见[持久性](/core/integrations/repairs#persistence). |
| `issue_domain` | `None` | 设定您代表另一集成创建问题的时间 |
| `data` | `None` | 您修复流量的数据 。 未向用户显示 。 |

| 严重性 | 用它的时候 |
| --- | --- |
| `IssueSeverity.CRITICAL` | 为了真正的恐慌 |
| `IssueSeverity.ERROR` | 现在有东西坏了,需要注意 |
| `IssueSeverity.WARNING` | 肇事有违,如API关闭 |

文本在 {{{{{{{{{{{{{{{{{{{}{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{

```json
{
  "issues": {
    "firmware_too_old": {
      "title": "The firmware of your Example device is too old",
      "description": "Update the firmware from {version} in the Example app."
    }
  }
}
```

一个可解决的问题有一个 `fix_flow` 而不是 `description`, 它的 [修补流程](/core/integrations/repairs#fix-an-issue-with-a-repair-flow) 步骤的文本, 和配置流一样 :

```json
{
  "issues": {
    "settings_outdated": {
      "title": "Your Example settings need to be updated",
      "fix_flow": {
        "step": {
          "confirm": {
            "title": "Update the Example settings",
            "description": "Select **Submit** to update your settings."
          }
        }
      }
    }
  }
}
```

## 删除一个问题 {#delete-an-issue}

问题解决后,删除问题:

```python
ir.async_delete_issue(hass, DOMAIN, "firmware_too_old")
```

一个典型的模式:在`async_setup_entry`中检查问题,并根据结果创建或删除问题.

只有在问题真的消失时才删除问题。 删除一个问题并再次创建它向用户显示它是一个新问题,它忘记了他们忽略了它. 当您一次检查整组问题时, 和每个设备一样, 使用 [刷新](/core/integrations/repairs#refresh-a-set-of-issues) 而不是先删除它们 。

您不需要删除 `async_unload_entry` 或 `async_remove_entry` 中的问题 。 设定 [`config_entry_id`](/core/integrations/repairs#issues-that-belong-to-a-config-entry) 相反, Home Assistant 照顾他们 。 卸载时的删除问题甚至对用户不利:重新卸载也以利于卸载条目,所以他们忽略的每个问题都会回来.

## 属于配置条目的问题 {#issues-that-belong-to-a-config-entry}

当一个问题涉及一个配置条目时,如设备上的过时固件或过期的API密钥,将 `config_entry_id` 设定为该条目的ID 。 问题随后属于条目:在条目禁用时隐藏,在条目删除时删除. 您不需要在 `async_remove_entry` 中自行删除 。

```python
ir.async_create_issue(
    hass,
    DOMAIN,
    f"firmware_too_old_{entry.entry_id}",
    config_entry_id=entry.entry_id,
    is_fixable=False,
    severity=ir.IssueSeverity.WARNING,
    translation_key="firmware_too_old",
    translation_placeholders={"version": device.firmware_version},
)
```

有一些事情需要记住:

- 问题仍然被其域名和其目的在于 `issue_id` 所识别,所以 `issue_id` 必须在您的域名内保持独有 。 当多个配置条目可以提出同样的问题时,将条目ID放入`issue_id`. 否则所有条目共享一个问题,它属于最后一个创建的条目,删除该条目将删除所有条目。
- 配置条目必须存在 。 通过未知的ID会提高`HomeAssistantError`. 在 `async_remove_entry` 中, 条目已经不见了 。
- 创建一个已经存在的问题将取代它的`config_entry_id`, 当你离开`config_entry_id`时也是如此。 每次你创造问题都传过去
- 属于已不存在的配置项的问题在 Home Assistant 开始时删除 。
- 虽然该条目已禁用,但该问题却隐藏在 ** Repairs ** 和 `issues()` 模板函数中,但没有删除 。 当用户再次启用该条目时,这个问题会重新出现,被忽略与否.
- 不要设置 `config_entry_id` 在一个即将删除的配置条目上, 就像一个正在迁移到另一个集成的条目一样 。 有关迁移的通知将与条目一起删除。
- 在您的集成设置 `config_entry_id` 之前创建的 `config_entry_id` 属于任何条目, 直到它再次创建 。 多数问题在下次开始时再次出现。 在 `async_remove_entry` 中, {L0 麦} 从未再创建的 [持久性](/core/integrations/repairs#persistence) 问题可能需要暂时删除 。

将 `config_entry_id` 保留到与单个配置项无关的问题, 如不再支持的 YAML 配置 。

### 属于配置子条目的问题 {#issues-that-belong-to-a-config-subentry}

当一个问题大约是一个配置条目的[子审查报告](/core/integrations/subentries),像气象站,一个话题,或者一个AI代理,也设置了`config_subentry_id`到该子条目的ID. 然后,当子条目被删除时,而不仅仅是当整个条目被删除时,这个问题会被删除.

```python
ir.async_create_issue(
    hass,
    DOMAIN,
    f"station_offline_{subentry.subentry_id}",
    config_entry_id=entry.entry_id,
    config_subentry_id=subentry.subentry_id,
    is_fixable=False,
    severity=ir.IssueSeverity.WARNING,
    translation_key="station_offline",
    translation_placeholders={"station": subentry.title},
)
```

`config_entry_id`的规则也在这里适用,加上这些:

- `config_subentry_id`需要`config_entry_id`,子条目必须属于该配置条目。 否则, `HomeAssistantError` 会被提高 。
- 将子条目ID放入 `issue_id` , 因此一个条目的子条目不会共享一个问题 。
- 创建一个已经存在的问题取代它的 `config_subentry_id` , 也当您不提及它时 。 每次你创造问题都传过去
- 虔诚的 Home Assistant 开始时, 属于已不存在的子条目的问题会被删除 。
- 子公司不能被禁用 。 这个问题只有在它的配置条目被禁用时才被隐藏.

## 用修补流程解决问题 {#fix-an-issue-with-a-repair-flow}

对于有`is_fixable=True`的一期,用户会得到**Fix**按钮. 它开始一个修复流: [数据输入流量](/core/integrations/flow-steps), 就像一个配置流. 当流量以 `async_create_entry` 完成时, 这个问题会被删除 。

如果修补只是之间的互动,你不需要任何代码:没有`repairs.py`,Home Assistant使用`ConfirmRepairFlow`,它要求用户确认,然后删除问题. 该确认的文本是问题`confirm`中的`fix_flow`步骤。

对于其它任何问题,请使用 `async_create_fix_flow` 创建 `repairs.py` , 它返回一个问题的流 :

```python
import probatio

from homeassistant.components.repairs import RepairsFlow, RepairsFlowResult
from homeassistant.core import HomeAssistant

class MigrateSettingsFlow(RepairsFlow):
    """Move the settings to the new format."""

    async def async_step_init(
        self, user_input: dict[str, str] | None = None
    ) -> RepairsFlowResult:
        """Start the fix."""
        return await self.async_step_confirm()

    async def async_step_confirm(
        self, user_input: dict[str, str] | None = None
    ) -> RepairsFlowResult:
        """Ask the user to confirm, then fix it."""
        if user_input is not None:
            await async_migrate_settings(self.hass, self.data["entry_id"])
            return self.async_create_entry(data={})

        return self.async_show_form(
            step_id="confirm", data_schema=probatio.Schema({})
        )

async def async_create_fix_flow(
    hass: HomeAssistant,
    issue_id: str,
    data: dict[str, str | int | float | None] | None,
) -> RepairsFlow:
    """Create the flow that fixes an issue."""
    return MigrateSettingsFlow()
```

接轨 Home Assistant 设定 `issue_id` 和 `data` 。 你们不要把他们传给流民,他们确是被蒙蔽的。

### 在配置或选项流中继续 {#continue-in-a-config-or-options-flow}

有时修补是重新配置一些东西,如配置条目或子条目. 修补流量可以随 `next_flow` 移交到该流量 :

```python
from homeassistant.components.repairs import FlowType
from homeassistant.config_entries import SOURCE_RECONFIGURE

if user_input is not None:
    result = await self.hass.config_entries.flow.async_init(
        DOMAIN,
        context={
            "source": SOURCE_RECONFIGURE,
            "entry_id": self.data["entry_id"],
        },
    )

    return self.async_abort(
        reason="reconfigure",
        next_flow=(FlowType.CONFIG_FLOW, result["flow_id"]),
    )
```

中止不会消除问题。 修复完成后自己删除, 例如在重构步骤中, 在 `async_update_reload_and_abort` 之前, 或是 `async_setup_entry` 。

如果一个配置条目的迁移失败, 而用户可以修复原因, 请在修复后调用 `hass.config_entries.async_retry_migration(entry_id)` 。 见[移动一个配置条目](/core/integrations/config-entries#migrate-a-config-entry).

## 刷新一系列问题 {#refresh-a-set-of-issues}

通常,您的整合会同时检查一组问题:每个设备一个,每个车辆一个,或者配置中的每个物品一个. 检查后,仍存问题的问题必须留下,新问题的问题必须产生,已经消失的问题必须删除. 这包括重新开始之前的问题,即不再存在的装置。

它诱导先删除所有的问题,然后创造那些仍然有效的问题. 不要,每个还存在的问题都有一个全新的问题。 用户看到问题消失又回来,他们忽略的每个问题都再次出现. 跟踪您自己创建的问题需要很多代码, 并且它仍然错过了重启前的问题。

一个问题对你有用 您开始对一组问题进行更新, 创建仍然有效的问题, 并完成更新 。 完成删除未再次创建的集的问题 。 被再次创建的系统从未被删除,因此它们一直被忽略,用户看不到变化.

在此之前:

```python
issue_registry = ir.async_get(hass)
for domain, issue_id in list(issue_registry.issues):
    if domain == DOMAIN and issue_id.startswith("firmware_too_old_"):
        ir.async_delete_issue(hass, DOMAIN, issue_id)

for device in coordinator.data.devices.values():
    if device.firmware_version < MINIMUM_FIRMWARE:
        ir.async_create_issue(
            hass,
            DOMAIN,
            f"firmware_too_old_{device.id}",
            config_entry_id=entry.entry_id,
            is_fixable=False,
            severity=ir.IssueSeverity.WARNING,
            translation_key="firmware_too_old",
            translation_placeholders={"version": device.firmware_version},
        )
```

之后:

```python
with ir.async_refresh_issues(
    hass,
    DOMAIN,
    issue_id_pattern="firmware_too_old_",
    config_entry_id=entry.entry_id,
):
    for device in coordinator.data.devices.values():
        if device.firmware_version < MINIMUM_FIRMWARE:
            ir.async_create_issue(
                hass,
                DOMAIN,
                f"firmware_too_old_{device.id}",
                config_entry_id=entry.entry_id,
                is_fixable=False,
                severity=ir.IssueSeverity.WARNING,
                translation_key="firmware_too_old",
                translation_placeholders={"version": device.firmware_version},
            )
```

### 选择要刷新的问题 {#choose-the-issues-to-refresh}

`ir.async_refresh_issues` 返回 `IssuesRefresh` 。 它取了问题的范围,并用这些论点缩小了内容:

| 参数 | 选择什么 |
| --- | --- |
| `issue_id_pattern` | 从ID开始,其ID与正则表达式相符的问题. 传递字符串或编译的 `re.Pattern` 。 |
| `issue_ids` | 正是这些问题。 不存在问题的识别码被跳过 。 |
| `config_entry_id` | 只发布 [属于](/core/integrations/repairs#issues-that-belong-to-a-config-entry) 此配置条目 。 与别二种合. 子条目没有过滤器 。 为了刷新一个子条目的问题,将它的ID放入它们的问题ID,然后用`issue_id_pattern`或`issue_ids`选择它们. |

以及各处通过 `issue_id_pattern` 或 `issue_ids` , 而不是两者: 这提高了 `ValueError` 。 传不来刷新每个问题

模式与`re.match`匹配,从发行ID开始. 因此,像`firmware_too_old_`这样的普通前缀是有效的图案. 以分隔符结束, 如 `battery_low_` 中的 `_` , 所以它并不匹配 `battery_lowest_abc123` 。 超过一次使用时通过编译的图案 :

```python
import re

VEHICLE_ISSUE_ID_PATTERN = re.compile(
    f"({'|'.join(map(re.escape, VEHICLE_ISSUE_TYPES))})_"
)

with ir.async_refresh_issues(
    hass,
    DOMAIN,
    issue_id_pattern=VEHICLE_ISSUE_ID_PATTERN,
    config_entry_id=entry.entry_id,
):
    ...
```

当您可以多次设置整合时, 通过 `config_entry_id`, 因此一个条目的刷新不会删除另一个条目的问题 。 仅包含属于条目的问题: 在您设定 `config_entry_id` 之前创建的问题, 在它再次被创建之前, 不属于设定的一部分 。

设定在刷新开始时决定 。进行过重启之前的问题, 还没有再次创建, 因此在 `async_setup_entry` 中刷新也会在设备消失后清理 。 您在刷新时创建的, 而不是在设定中, 将照常创建 。

### 在任何地方创建问题 {#create-the-issues-anywhere}

您不会通过刷新创建问题 。 任何给 `ir.async_create_issue` 的电话都保留它 。 这意味着这些问题不必在`with`中产生。 块本身:检查问题的助手和回调可以创建,只要在刷新完成之前发生。 `with`街区也可以等待。

把新鲜的代码 检查问题, 没有更多的。 当一个平台在创建其实体时检查出问题时,请在该平台的`async_setup_entry`中开始刷新:

```python
async def async_setup_entry(
    hass: HomeAssistant,
    entry: ExampleConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the cameras."""
    with ir.async_refresh_issues(
        hass,
        DOMAIN,
        issue_id_pattern="rtsp_disabled_",
        config_entry_id=entry.entry_id,
    ):
        entities = _async_camera_entities(hass, entry)
    async_add_entities(entities)
```

不要将 `async_forward_entry_setups` 包裹 好啊 。 当一个平台未能设置,或升起`PlatformNotReady`,并在稍后被重试时,`async_forward_entry_setups`不会升起. 刷新随后在平台检查其问题之前完成,并删除它们,同样是那些被忽略的用户.

只有在您的发行ID稳定时才有效:同样的问题必须在重新装入或重启后获得相同的ID. 由不改变的东西来构建它们,比如设备的ID. 不要使用计数器, 或 Python 的 `hash()`, 每次 Home Assistant 开始都会给出不同的结果 。

### 保留无法检查的问题 {#keep-issues-you-could-not-check}

有时你无法判断一个问题是否仍然有效 。 设备没有回答, 或者您需要的数据还没有找到 。 删掉这个问题是错误的,并且用陈旧的信息再次制造这个问题。 拨打`IssuesRefresh.async_keep`,以保留这些问题:

```python
with ir.async_refresh_issues(
    hass,
    DOMAIN,
    issue_id_pattern="firmware_too_old_",
    config_entry_id=entry.entry_id,
) as refresh:
    for device in devices:
        issue_id = f"firmware_too_old_{device.id}"
        try:
            version = await device.async_get_firmware_version()
        except DeviceUnavailable:
            refresh.async_keep([issue_id])
            continue
        if version < MINIMUM_FIRMWARE:
            ir.async_create_issue(
                hass,
                DOMAIN,
                issue_id,
                config_entry_id=entry.entry_id,
                is_fixable=False,
                severity=ir.IssueSeverity.WARNING,
                translation_key="firmware_too_old",
                translation_placeholders={"version": version},
            )
```

`async_keep`拿一个问题ID列表。 它不会造成或改变问题。 刷新集之外的问题被忽略.

通常,检查一个问题的代码没有更新对象,例如当一个新设备出现时,一个同样在刷新之外运行的助手. 给 `ir.async_keep_issue` 打电话 :

```python
@callback
def _async_check_stream_issue(
    hass: HomeAssistant, entry: ExampleConfigEntry, camera: Camera
) -> None:
    issue_id = f"rtsp_disabled_{camera.id}"
    if camera.streams is None:
        

# The streams could not be read, so the issue can't be checked {#finish-or-cancel}
        ir.async_keep_issue(hass, DOMAIN, issue_id)
    elif camera.streams.active:
        ir.async_delete_issue(hass, DOMAIN, issue_id)
    else:
        ir.async_create_issue(
            hass,
            DOMAIN,
            issue_id,
            config_entry_id=entry.entry_id,
            is_fixable=False,
            severity=ir.IssueSeverity.WARNING,
            translation_key="rtsp_disabled",
        )
```

`ir.async_keep_issue` 将这个问题保留在每一个包含它的活跃更新中, 就像再次创建它一样。 当没有活跃的更新包含这个问题时,它就什么都不做.

当问题被检查太迟而无法刷新时,它也会有所帮助。 说一个实体在首次运行时创建或删除它的问题,这可能是在重新装入完成刷新后. 保留实体设立地的问题,在刷新时发生,实体以后再决定.

### 完成或取消 {#delete-an-issue-during-a-refresh}

刷新结束有两种方式之一:

- `IssuesRefresh.async_finish()` 删除自刷新开始以来没有创建或保存的集的问题 。
- `IssuesRefresh.async_cancel()` 只删除删除为[推迟到刷新时](/core/integrations/repairs#delete-an-issue-during-a-refresh) 的问题 。 其他问题则照原样存在,直到下一次刷新结束。 检查未完成时使用它, 因此您无法分辨哪些问题已失效 。

一旦刷新结束, 拨打 `async_finish()` 或 `async_cancel()` 就会无动于衷 。

`with` 块在块完成后完成刷新, 并在其中提出例外时取消它 。 由于已取消的刷新仍然应用延迟删除,重新加载也可以在 `with` 块中运行 。

当新鲜剂不适合一个区块时,您也可以自行调用方法。 在 `async_setup_entry` 中, 用 `entry.async_on_unload` 注册 `async_cancel` , 这样一个失败的设置会取消刷新 :

```python
refresh = ir.async_refresh_issues(
    hass,
    DOMAIN,
    issue_id_pattern="gateway_not_found_",
    config_entry_id=entry.entry_id,
)
entry.async_on_unload(refresh.async_cancel)

for site in sites:
    await _async_setup_site(hass, entry, site)

refresh.async_finish()
```

永无止境的刷新永远不会删除任何东西.

### 在刷新时删除一个问题 {#overlapping-refreshes}

重新装入,可以删除旧实体并添加新实体. 一个旧实体在删除时删除它的问题 。 当实体被永久删除见上文,但在重新装入时,新实体可能再次产生同样的问题。 通过 `defer_to_refresh=True` 将决定留给更新 :

```python
async def async_will_remove_from_hass(self) -> None:
    """Run when the entity is removed."""
    ir.async_delete_issue(
        self.hass, DOMAIN, self.repair_issue_id, defer_to_refresh=True
    )
```

然后重新装填这些新问题:

```python
with ir.async_refresh_issues(
    hass,
    DOMAIN,
    issue_ids=[entity.repair_issue_id for entity in old_entities],
):
    for entity in old_entities:
        await entity.async_remove()
    await component.async_add_entities(new_entities)
```

使用 `defer_to_refresh=True` , 活动刷新集中的一个问题留待该刷新删除 。 它如果在刷新运行时被创建或再次保存,在推迟删除之前或之后存活下来,所以是删除旧实体还是先添加新实体无关紧要. 否则,刷新在结束的时候也会删除,同样是在取消的时候,所以一次失败的重新加载不会留下被移除的实体的问题.

当没有活动刷新包含此问题时, 立即删除, 好像您没有通过 `defer_to_refresh` 。 不包含 `defer_to_refresh` 的删除总是立即删除, 在刷新时也是如此 。

### 重叠刷新 {#refresh-from-another-thread}

两个刷新可以包含同样的问题,例如当一个设置还在运行时重新加载时. 包括这个问题在内的最新活跃更新决定了这个问题,也决定了推迟删除:

- 旧的刷新不会删除一个问题,而新发的则包括它,并且不会删除新发的保存的问题。
- 当更新的刷新结束而不删除问题时,例如因为它被取消,老的再次决定. 它只有在自旧的更新开始以来没有创建或保留这个问题时才删除这个问题。
- 较新的刷新结束等待旧的更新后, 延迟删除 。
- 保持这个问题 对于那些新鲜和老的, 而不是一个更新的。 都留着吧

### 从另一线索刷新 {#persistence}

刷新只在事件循环中有效 。 开始、 保存、 完成和取消 以及 `ir.async_keep_issue` , 当它们从另一个线程调用时会像 `async_` 问题登记簿的其他功能一样产生错误 。 `ir.delete_issue`,线程安全版本的`ir.async_delete_issue`,没有`defer_to_refresh`. 当检查在工人线条中运行时, 像数据库查询一样, 解决线条中的问题, 并同时应用到事件循环中 :

```python
from homeassistant.core import callback
from homeassistant.util.async_ import run_callback_threadsafe

def update_issues(hass: HomeAssistant) -> None:
    """Check for problems, runs in a worker thread."""
    problems = find_problems()

    @callback
    def apply_issues() -> None:
        """Create the issues and delete the stale ones."""
        with ir.async_refresh_issues(
            hass, DOMAIN, issue_id_pattern="units_changed_"
        ):
            for issue_id, placeholders in problems.items():
                ir.async_create_issue(
                    hass,
                    DOMAIN,
                    issue_id,
                    is_fixable=False,
                    severity=ir.IssueSeverity.WARNING,
                    translation_key="units_changed",
                    translation_placeholders=placeholders,
                )

    run_callback_threadsafe(hass.loop, apply_issues).result()
```

在一个回调中做这一切比从线程中调用{H0其目的在于每期,刷新开始并完成单独调用到事件循环更为简单. 它也比较安全:当刷新开始后创建时,一个问题只算一个刷新,在回调运行时,在事件循环中没有其他运行.

## 持久性 {#持久性}

一个问题一直保留到创建它的集成删除,用户修正它,或者它属于[配置条目](/core/integrations/repairs#issues-that-belong-to-a-config-entry)或[子审查报告](/core/integrations/repairs#issues-that-belong-to-a-config-subentry)被删除. 重启后会发生什么取决于 `is_persistent` :

- ** 非持久性**(默认规定的义务):问题在重新启动后,直到您的整合再次创建。 用这个来解决问题,就像旧的固件 你的整合检查 再次在下一个开始反正。
- ** 持续**:问题在重启后再次显示。 用于问题, 只有在问题发生时才能看到, 如失败的更新 。

Home Assistant 记得每一次重启, 持续与否, 以及用户是否忽略它 。 当您的整合产生一个重启后不再持续的问题时, 它仍然被忽略 。 从未再创建的问题在问题登记处中保留,直到删除。 A [刷新](/core/integrations/repairs#refresh-a-set-of-issues) 清理这些了。

用户也可以忽略一个问题. 它一直被忽略, 也在整个重启中, 直至它被删除并再次创建 。 这就是为什么你只应该在问题消失时删除一个问题。
