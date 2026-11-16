---
title: 等级
description: 青铜器,银器,金器,和白金的意思,以及天秤以外的阶梯,如内部和遗产.
order: -5
---

# 等级 {#tiers}

质量尺度分为四个级:铜,银,金,和白金. 每个层级都以以下一个层级为基础:为了达到一个层级,一个整合遵循该层级的每一个规则以及其下的每一层级的规则。 黄金的融合遵循了所有青铜器,银器和黄金的规则.

与规模相邻的还有不适合其上的集成层:核心的内部构件,旧的YAML只集成,以及核心以外的集成.

层次存在于 `quality_scale` 整合 `manifest.json` 的密钥中 :

```json
{
  "domain": "my_integration",
  "name": "My integration",
  "quality_scale": "silver"
}
```

Hassfest接受这些值: `bronze`,`silver`,`gold`,`platinum`,`internal`,`legacy`,`custom`,和`no_score`.

## 铜 {#bronze}

青铜器是基线,也是每次新整合的最低标准. 青铜器集成:

- 可以从UI设置,带有一个配置流来测试连接.
- 遵循基本的编码标准,如实体独有的ID和普通文件布局.
- 对它的配置流有自动测试 。
- 拥有足以启动用户的文档, 一步一步地。 Name

见[铜制规则](/core/quality-scale/rules#bronze).

## 银 {#silver}

银是关于可靠性。 当银的一体化不合作时,银的一体化就继续发挥作用,或自行恢复。 在青铜器之上:

- 拥有一个或多个活跃的融合所有者.
- 从连接错误和离线设备中自行回收,而不填充日志.
- 当证书停止工作时,自己开始重新校正。
- 当动作失败时, 会产生明显的错误 。
- 有超过ص95%的测试。
- 记录用户在设置和选项中填写的所有内容。

见[银制](/core/quality-scale/rules#silver).

## 黄金 {#gold}

Gold是集成能提供的最佳用户体验. 在Silver之上,一个黄金整合:

- 自动发现, 设备支持它。
- 让您 这不是从 Home Assistant 更新设备的固件或软件, 设备支持它 。
- 以儿童为主,
- 可以从UI重组.
- 已翻译实体名称、图标和错误消息。
- 提供诊断,并在用户需要采取行动时提出修理问题.
- 拥有安装设备类和类别的实体, 默认会禁用噪音 。
- 为用户提供了广泛的文档:支持的设备和功能,实例,使用案例,已知的局限性,以及排除故障.

[工作与 Home Assistant](/glossary/works-with-home-assistant) 程序中的设备集成至少需要 Gold 。

见[黄金规则](/core/quality-scale/rules#gold).

## 铂 {#platinum}

白金是规模的顶级:在最佳用户体验之上的技术卓越. 在黄金之上,一个白金整合:

- 已打完字, 并严格检查类型 。
- 使用 aync 库,所以其I/O不需要线程.
- 共享Home Assistant的网页会话,而不是打开自己的会话.
- 高效处理数据,保持网络和CPU使用率低.
- 有清晰的代码注释,所以代码易于维护.

见[白金规则](/core/quality-scale/rules#platinum).

## 比额表以外的级别 {#tiers-outside-the-scale}

### 内部 {#internal}

`internal`是用于作为Home Assistant本身的一部分的集成,如核心的构件,或者其他集成所依托的平台,如`sensor`或`light`. 它们由Home Assistant项目维护,并遵循其架构决定。 内部整合没有分级. Has歪est在 [`script/hassfest/quality_scale.py`](https://github.com/home-assistant/core/blob/dev/script/hassfest/quality_scale.py) 中保留了其中的列表, 在此必须添加一个新的内部集成 : 当它没有 `quality_scale.yaml` 时, 或 当它只使用文件来跟踪规则时, 需要添加到 `INTEGRATIONS_WITHOUT_SCALE` 。

### 遗产 {#legacy}

`legacy`是用于更古老的融合, 有些是和Home Assistant一样古老的 这只能和YAML一起设置 其中许多人缺乏积极的融合拥有者,他们无法满足今天对设置和特征的期望. 他们仍然在工作,你可以通过增加一个配置流和其他的青铜规则来帮助将他们带到青铜.

### 无分数 {#no-score}

`no_score`表示整合没有被比对比额表进行分级. 这不是对其质量的判断。 核心中的任何整合目前都没有使用它,没有分数就无法开始新的整合:它需要青铜.

### 自定义 {#custom}

`custom`是用于自定义集成:非核心部分的集成,由手或通过[市场](/marketplace)安装. Home Assistant 项目不审查、维持或支持它们。 如果你保持自定义的集成,尺度的规则仍然是很好的指南,这些规则是你想贡献给核心时需要遵循的.

## 一层可以下 {#a-tier-can-go-down}

层层不是永远的。 一体化如果不再遵循其层级的规则,就可以向下移动。 一个常见的原因是失去其最后一个活跃的集成所有者:没有所有者,集成就不能保持Silver或更高,即使其代码对白金足够好.

随着Home Assistant和最佳做法的发展,规则也随着时间而变化。 当一个规则被添加到一个层次时,该层次上的整合也需要遵循它. 与 Home Assistant 程序中的设备的集成 Home Assistant 程序保持其水平 。
