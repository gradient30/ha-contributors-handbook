---
title: 当用户需要采取行动时提出修复问题
description: 黄金规则修补问题:集成对用户能够修补的问题提出了修补问题.
sidebarLabel: 修理问题
sidebarGroup: 黄金
order: 20
---

# 当用户需要采取行动时提出修复问题 {#raise-repair-issues-when-the-user-needs-to-act}

这是黄金规则 在`quality_scale.yaml`中,它被称为`repair-issues`.

当用户可以修复出错时,集成会提高[修理问题](/glossary/repair). 它出现在**Settings** > **System** **Repairs**下,并对此问题和如何应对做出解释. 当集成在用户确认后可以自行解决问题时,它会添加一个修补流程,引导用户通过它.

修理问题必须可以提起诉讼。 当用户无法有所作为时,

## 为什么这很重要 {#why-it-matters}

日志是问题被忽略的地方. 一个修补问题就是Home Assistant用普通语言和他们自己的语言告诉用户需要他们注意的事情,以及该做什么. 它把"我的整合停止工作"变成"更新你的设备的固件到2.0版本".

用户无法采取行动的问题是噪音。 它教用户忽略修复,所以他们想念那些重要的东西.

## 示例 {#example}

在设置时,整合会检查本地服务的版本. 当它太老了,它引起了修理问题,停止:

```python
async def async_setup_entry(
    hass: HomeAssistant, entry: MyConfigEntry
) -> None:
    """Set up My integration from a config entry."""
    client = MyClient(entry.data[CONF_HOST])
    version = await client.get_version()
    issue_id = f"outdated_version_{entry.entry_id}"

    if version < MINIMUM_VERSION:
        ir.async_create_issue(
            hass,
            DOMAIN,
            issue_id,
            config_entry_id=entry.entry_id,
            is_fixable=False,
            severity=ir.IssueSeverity.ERROR,
            translation_key="outdated_version",
            translation_placeholders={"minimum": str(MINIMUM_VERSION)},
        )
        raise ConfigEntryError(
            translation_domain=DOMAIN,
            translation_key="outdated_version",
        )

    ir.async_delete_issue(hass, DOMAIN, issue_id)
    ...
```

`ir`是`homeassistant.helpers.issue_registry` 。 问题文本存在于 `issues` `strings.json` 的 `issues` 一节, 在例外信息旁边 :

```json
{
  "exceptions": {
    "outdated_version": {
      "message": "My service is out of date."
    }
  },
  "issues": {
    "outdated_version": {
      "title": "My service is out of date",
      "description": "Update My service to version {minimum} or newer."
    }
  }
}
```

一旦问题得到解决,就删除该问题,就像实例对成功设置所做的那样. 当条目卸下时不要删除它:这样会丢弃忽略这个问题的用户的选择,每次条目重新装入时都不要删除.

椰子上的问题大约是一个配置条目,所以它的`issue_id`包含了条目ID,或者一个集成的条目被设置不止一次地覆盖了对方的问题. `config_entry_id` 将问题链接到条目, 因此Home Assistant 在条目禁用时隐藏它, 在条目删除时删除它 : 见[属于配置条目的问题](/core/integrations/repairs#issues-that-belong-to-a-config-entry) 。

当一个问题涉及一个子条目时,同样通过`config_subentry_id`,所以这个问题与子条目一起删除:参见[属于配置子条目的问题](/core/integrations/repairs#issues-that-belong-to-a-config-subentry).

## 如何检查 {#how-it-is-checked}

- 当出现`strings.json`中缺失翻译的问题时, 测试失败 。
- 整合是否引起用户需要采取行动的问题,以及只有用户需要采取行动的问题,将进行审查。

## 例外 {#exceptions}

如果合并没有需要修理的问题,则不适用这一规则。
