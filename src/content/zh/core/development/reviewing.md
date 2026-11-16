---
title: 审查 pull request
description: pull request在Home Assistant Core上的审查实用指南。 首先要检查什么,每类变化要找什么,如何反馈.
sidebarGroup: Pull request
order: 5
---



# 审查 pull request {#reviewing-pull-requests}
任何人都可以审查 pull request, 每一次审查都有帮助。 您不需要做维护者: 用自己的设备测试更改, 发现缺失的测试, 或者问一个好的问题 都向前移动 pull request 。 审查也是了解核心如何工作的最快方法,pull request模板要求每个贡献者审查另外两个.

本指南以核心审查者实际上对大多数评论为基础。 用它作为核对表,而不是脚本.

## 在哪里寻找 pull requests {#where-to-find-pull-requests}

- [未经审查而撤回请求](https://github.com/home-assistant/core/pulls?q=is%3Aopen+is%3Apr+-author%3A%40me+-draft%3Atrue+-label%3Awaiting-for-upstream+sort%3Acreated-desc+review%3Anone+-status%3Afailure),通过检查。
- `small-pr`标签,为快速的。
- 调用您使用的整合请求, 这样您就可以测试它们的真实性 。

## 请检查 {#1-gate-checks}

在读到密码前先检查一下 如果失败, 评论和停止: 进一步浪费你的时间 。

- ** 《法律援助法》已经签署。 ** pull request有`cla-signed`的标签,而不是`cla-needed`。
- ** CI通过。 ** 如果因更改而失败,请作者修复,并将pull request转换为草稿.
- 它做一件事。 。 一个错误修复,一个特性,一个集成,或者一个重构. 若其混杂物,请分之.
- ** 检查一种更改**,它与代码相同。
- ** 它不取决于另一个打开的pull request。 **
- ** 说明解释了原因。 ** 错误修复会链接它的问题 。 新的整合解释了产品或服务。
- ** 模板以 ** 填充,没有空的后向兼容更改段或空的 `fixes #` 。

### pull request 可能无法完成的信号 {#signals-that-a-pull-request-may-not-finish}

- 不合并的 pull request 的大型新合并是最有可能被放弃的 。 等待CI通过 和处理第一个机器人反馈 在你投入深度审查。
- 未经审查的AI输出的标志: 解决不存在的问题, 无法发生条件的防御代码, 测试固定装置没有改变行为而改变, 或在代码之上显示基本误解的抛光描述. [AI 政策](/core/development/submitting#using-ai)适用。

## 2.  更改类型 {#2-by-type-of-change}

### 新整合 {#new-integrations}

[集成质量等级](/core/quality-scale)的青铜级是基线。

- **范围**:`PLATFORMS`中的一个平台。 在第一个 pull request 中没有诊断、 重新配置流或选项流( 除非真的需要) 。
- **Manifest**:`iot_class` 匹配整合的真正沟通方式.
- **Library **:开源,在PyPI上持有与其LICENSE文件匹配的许可证,并与Apache 2.0.兼容. MIT,BSD,Apache 2.0,LGPL,MPL 2.0,ISC,Unlicense都很好. GPL和AGPL不是,根据这些许可证,也不是图书馆的附属单位。 当心一个多年不活动且最近更换维护者的图书馆.
- QQH0}**:每个青铜器规则都是`done`,或`exempt`有正当理由. 点点检查`done`是真的。
- **Config 流量**:在创建条目之前测试连接,在失败时显示明显的错误,并设置一个独特的ID,所以同一设备不能被添加两次.
- **Discovery**:Zeroconf,DHCP,和SSDP模式只匹配预定设备. 一种过于宽泛的主张方法不应该使用。 `manifest.json`中的每一种发现方法都有它的`async_step_*`在配置流中. 由用户开始的一步应该赢得同一设备的发现流:通过`raise_on_progress=False`到`async_set_unique_id`那里. 与Zeroconf的集成可以添加DHCP作为后退,用于mDNS不起作用的网络. 对于更改的IP地址或主机名称的设备,在DHCP匹配器中`registered_devices`允许再次发现已经设置的设备.
- **Strings**:用户看到的一切在`strings.json`中,在句子中,使用它们适合的常见字符串. 字符串渲染为 Markdown, 所以类似代码的值, 如实体 ID,动作名称, 和文件名, 以反键进行 。 品牌和协议名称没有,并保持他们的正式拼写,像Z-Wave.

### 新特性 {#new-features}

- 一种符合现有整合风格的连贯添加,并保持其质量等级。
- 向后不兼容的更改为用户描述. 对于用户来说,某事的中断是否是人类的判断,一位AI审查员经常会出错.
- 如果一个配置条目中存储的数据发生变化,则配置流 `VERSION` 被撞,`async_migrate_entry` 迁移旧条目, 测试覆盖迁移. 没有移民代码的突起版本同样是错误的.
- `async_unload_entry`清理所有创建的设置。
- 溅射失败时处理错误不读 `entry.runtime_data`: 可能尚未设置 。
- 新实体有完整的设备信息:制造商,型号,序列号,以及固件版本,设备提供它们的地方.

### 错误修正 {#bug-fixes}

- 有个问题证实了这个错误
- 修补是最小的,并修补原因,而不是症状. 在 `try` 和 `except` 中环绕一切不是固定的 。
- 最好有一个测试没有固定。
- 没有不相关的更改, 如快照更新或重构测试 。

### 依赖性更新 {#dependency-updates}

这些评论很少获得许多评论,但它们具有最大的安全风险。

- 只有`manifest.json`中的版本,重新生成的要求文件,代码会改变新版本的需求. 请检查access-date=中的日期值 (帮助) `quality_scale`和`loggers`没有从清单中消失 。
- 描述链接到更改日志或 diff 。 读取上游 diff: 监视新网络呼叫, `subprocess` 或 `os.system`, 新文件访问, 以及环境变量访问 。
- 呼唤新的过渡性依赖。 它们是进入供应链攻击的最常见方式。
- 许可证没有更改,PyPI维护者没有更改,源寄存器也没有移动或存档.

### 代码质量 {#code-quality}

- 代码更好,不只是不同,行为也不改变.
- 测试修改与代码的修改一致,不再前进.

## 3. 测试 {#3-tests}

- 测试在 `tests/components/<domain>/` 中直播,使用类型提示,并通过 Home Assistant 的公开界面进行. 见[写作测试](/core/development/tests).
- 他们嘲笑图书馆,而不是Home Assistant,在`conftest.py`中用共享的固定装置。
- 平台使用`snapshot_platform`. 时间使用`freezer`固定。 没有补丁 `sys.modules` 。
- 配置流测试覆盖每个步骤和每一个错误,并在错误发生后继续,直到条目创建. 早期读取:它们经常揭示其余代码中的问题.
- 错误通过测试:设备下线,反应不良,证书过期.

## 4.  实体 {#4-entities}

实体问题主要受到审查者的注意。

** 实体类别。 ** 询问用户对实体做什么 :

- 仪表盘的东西,设备的主要功能:没有分类.
- 改变设备行为方式的设置, 如模式或阈值 : `EntityCategory.CONFIG` 。
- 调试信息,如固件版本,信号强度,或IP地址,并带有`identify`设备类的按钮:`EntityCategory.DIAGNOSTIC`. 如果它只对调试有用,它默认也会与 `entity_registry_enabled_default=False` 一同被禁用.

不要过份分类。 有类别的实体被隐藏在默认的仪表板和语音助理处。

** 不详,但无法提供。 ** 这些对用户来说是不同的:

- `native_value` 返回 `None` : 设备可以到达, 但值现在未知 。
- `available` 是 `False`: 设备或服务无法到达 。

注意 `bool(value)` 或 `int(value)` 的值可以是 `None` 。 `bool(None)` 将缺失的值转换为“ 关闭” , 而 `bool("0")` 是 `True` 。 明确转换, 如 `value == "1"` 。

** 更多检查:**

- 独有的ID是稳定的:一个与`format_mac()`正常化的MAC地址,一个序列号,或者来自设备的ID. 永远不要IP地址或主机名称.
- 新实体使用实体描述。
- 新数据是一个独立的实体,而不是额外的状态属性,除非它只与主要实体一起有意义.
- 的人口 设备 加州级 设置在一个适合的地方 并留下一个没有的地方。
- 基于协调员的平台设置 `PARALLEL_UPDATES = 0`.
- 在命令后,实体要么等待设备确认新状态,要么乐观地更新,选择符合设备. 见[在命令之后](/core/entities/state-updates#after-a-command).

## 代码 5. {#5-code}

- ** 协调员**:投票通过`DataUpdateCoordinator`,按`DataUpdateCoordinator[ExampleData]`键,间隔合理。 一次工作,就像登录, 在`_async_setup`。 `_async_update_data` 只获取数据 。
- ** 校正错误 ** 提高 `ConfigEntryAuthFailed` , 它开始校正, 而不是 `UpdateFailed` , 它只是永远重试 。 只有在配置流有 `async_step_reauth` 的情况下, 重新校正才有效 。
- ** 动作 ** 升起 `HomeAssistantError` 当它们失败时, 所以用户看到错误 。 它们不会吞噬例外,也不会第二次记录错误。
- ** 例外**是具体的,`try`区块是小的。 没有`except Exception:`。
- QQH0}**只用于测试,在`TYPE_CHECKING`区块内.
- **Cleanup**:收听器,计时器和连接在卸载时关闭,在Home Assistant停止时连接.
- 走动 `const.py` 中的常数, 提前返回, 当密钥得到保证时直接访问字典, 没有动作计划已经做的检查, 没有评论代码 。 见[代码样式](/core/development/style).

## 卫生 {#6-git-hygiene}

- 原属棉兰的有棉兰的有棉兰的有棉兰的有棉兰的有棉兰的有棉兰的有棉兰的有棉兰的有棉兰的有棉兰的,有棉兰的有棉兰的有棉兰的有棉兰的有棉兰的有棉兰的有棉兰的有棉兰的有棉兰的有棉兰的有棉兰的有棉兰的. `dev`的合并是好的。 见[不断更新你的分支](/core/development/catching-up).
- 如果 pull request 突然包含与 `dev` 无关的 承诺, 历史被打破 。 问作者要干净的分支和新鲜的pull request.

## 一个好命令 {#a-good-order}

1. 门检查。 如果C吝啬鬼CLA失踪,CI失败,或者信号坏.
2. 范围:它做一件事吗?
3. 明确和质量尺度。
4. 配置流程测试.
5. 实体。
6. 其他测试。
7. 密码
8. `strings.json`.
9. 批准、要求修改或评论。

## 提供反馈 {#giving-feedback}

具体地说:说明需要改变什么,为什么。 您可以时链接到文档 。 如果

发慈心. 另一边的人往往是一名志愿者,也许在他们的第一个pull request上. 解释,问问题,并说谢谢。
