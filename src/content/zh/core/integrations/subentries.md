---
title: 配置子条目
description: 将一个配置条目分割到部件用户中,像天气服务的位置一样逐个添加.
sidebarLabel: 子条目
sidebarGroup: 设置与配置
order: 5
---

# 配置子条目 {#config-subentries}

A [配置子条目](/glossary/config-subentry) 是用户自行添加,更改和删除的配置项的一部分. 想想气象服务: 配置条目持有账户, 你需要预测的每个位置都是子条目 。 用户从配置项的页面中添加子条目,而不再次设置账户.

子弟自有流转. 一个子条目流像 [配置流量](/core/integrations/config-flow) 一样工作, 有两种区别: 它只从 `user` 或 `reconfigure` 步骤开始, 它支持不被发现和不重新校正 。

## 添加子条目类型 {#add-a-subentry-type}

告诉 Home Assistant 您的配置条目支持的子条目类型, 以及每个类型的流程控件 :

```python
from homeassistant.config_entries import (
    ConfigEntry,
    ConfigFlow,
    ConfigSubentryFlow,
    SubentryFlowResult,
)
from homeassistant.core import callback

class ExampleConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Example."""

    @classmethod
    @callback
    def async_get_supported_subentry_types(
        cls, config_entry: ConfigEntry
    ) -> dict[str, type[ConfigSubentryFlow]]:
        """Return the subentry types this integration supports."""
        return {"location": LocationSubentryFlow}

class LocationSubentryFlow(ConfigSubentryFlow):
    """Add and change a location."""

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> SubentryFlowResult:
        """Add a new location."""
        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=user_input,
                unique_id=f"{user_input[CONF_LATITUDE]}"
                f"_{user_input[CONF_LONGITUDE]}",
            )

        return self.async_show_form(
            step_id="user", data_schema=LOCATION_SCHEMA
        )
```

在子条目流中, `self._get_entry()` 返回父配置项 。 配置流也可以通过将 `subentries` 传递到自己的 `async_create_entry` 来立即创建子条目 。

## 独一无二的ID {#unique-ids}

子条目可以有一个独特的ID. 相同的 [关于配置条目的规则](/core/integrations/config-flow#what-makes-a-good-unique-id) 适用, 只不过它只需要在其配置条目中独有 。

## 使之能够重新配置子条目 {#reconfigure-a-subentry}

添加一个 `reconfigure` 步骤让用户更改现有的子条目 。 Home Assistant 一旦该步骤存在, 立即显示此选项 。 以 `self._get_reconfigure_subentry()` 获取子条目, 并以 `async_update_and_abort` 或 `async_update_reload_and_abort` 完成 :

```python
async def async_step_reconfigure(
    self, user_input: dict[str, Any] | None = None
) -> SubentryFlowResult:
    """Change an existing location."""
    entry = self._get_entry()
    subentry = self._get_reconfigure_subentry()

    if user_input is not None:
        return self.async_update_reload_and_abort(
            entry, subentry, data_updates=user_input
        )

    return self.async_show_form(
        step_id="reconfigure",
        data_schema=self.add_suggested_values_to_schema(
            LOCATION_SCHEMA, subentry.data
        ),
    )
```

`async_update_reload_and_abort` 重新装入父配置条目 。 如果条目有更新的收听器,则会产生错误 。

## 设置时使用子条目 {#use-subentries-when-setting-up}

子条目在 `entry.subentries` 中, 从子条目 ID 到 `ConfigSubentry` 的映射, 以及它的 `subentry_type`, `title`, `data` 和 `unique_id` 。 要获得所有一类子条目,请拨打`entry.get_subentries_of_type("location")`.

实体和装置可属于子条目。 传 `config_subentry_id` 当您添加实体时, 它们被分组在右子条目下, 并随其一起删除 :

```python
async def async_setup_entry(
    hass: HomeAssistant,
    entry: ExampleConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up a weather entity per location."""
    for subentry in entry.get_subentries_of_type("location"):
        async_add_entities(
            [ExampleWeather(entry.runtime_data, subentry)],
            config_subentry_id=subentry.subentry_id,
        )
```

## 文本和翻译 {#texts-and-translations}

子条目流的文本在`strings.json` `config_subentries` 下, 每个子条目类型有一个密钥 。 在通常的`step`、`error`和`abort`章节旁边,每个类型需要:

- `entry_type`: what one subentry of this type is called, like "Location".
- `initiate_flow`:启动流的按钮的标签 。 需要`user`,`reconfigure`是可选的。

```json
{
  "config_subentries": {
    "location": {
      "entry_type": "Location",
      "initiate_flow": {
        "user": "Add location",
        "reconfigure": "Change location"
      },
      "step": {
        "user": {
          "title": "Add location",
          "data": {
            "name": "[%key:common::config_flow::data::name%]"
          }
        },
        "reconfigure": {
          "title": "Change location"
        }
      }
    }
  }
}
```
