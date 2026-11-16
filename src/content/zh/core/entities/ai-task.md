---
title: AI 任务实体
description: 构建一个AI任务实体,让自动化询问一个模型生成数据或图像,或评价问题.
sidebarLabel: AI 任务
sidebarGroup: 语音与 AI
---

# AI 任务实体 {#ai-task-entity}

一个AI任务实体为一次性工作提供自动化和脚本访问模式,而不围绕它对话:总结这些传感器读数,描述相机所看到的,写一个合适的通知,或者绘制一个图像. 人们通过`ai_task.generate_data`,`ai_task.generate_image`和`ai_task.evaluate`动作来使用它. 从`AITaskEntity`在`homeassistant.components.ai_task`中继承。

为模型提供[实情](/core/entities/conversation)的集成通常也提供AI任务实体,并共享发送聊天日志给模型的代码.

## 的临时议程 {#properties}

AI任务实体没有自己的属性. [一般实体属性](/core/entities/entity-class) 应用 。

## 支持的特性 {#supported-features}

将 `AITaskEntityFeature` 的值与位符或 (`|`) 运算符合并 。 Home Assistant 在调用您的实体前检查它们, 并拒绝该实体不支持的任务 。

| 数值 | 说明 |
| ----- | ----------- |
| `GENERATE_DATA` | 实体生成文本或结构化数据. 执行`_async_generate_data`。 |
| `SUPPORT_ATTACHMENTS` | 实体接受附件,如相机快照或文件,并带有任务. |
| `GENERATE_IMAGE` | 实体生成图像 。 执行`_async_generate_image`。 |
| `EVALUATE` | 该实体回答评价问题。 执行`_async_evaluate`。 |

## 聊天日志 {#the-chat-log}

每个数据和图像任务都以 `ChatLog` 到达, 和对话实体得到的相同 。  Home Assistant 已经填充了 : 一个任务工作的系统 , LLM API 如果呼叫者要求, 以及作为用户消息的任务指示, 及其附件 。 将聊天日志发送到模型中,加入答案,并从中构建结果. API 的对话实体页面中参见 [聊天日志](/core/entities/conversation#the-chat-log).

## 方法 {#methods}

### 生成数据 {#generate-data}

```python
async def _async_generate_data(
    self, task: GenDataTask, chat_log: ChatLog
) -> GenDataTaskResult:
    """Handle a generate data task."""
```

`GenDataTask`这些字段:

| 名称 | 类型 | 说明 |
| ---- | ---- | ----------- |
| `name` | `str` | 任务名称,用于日志和痕迹. |
| `instructions` | `str` | 模特儿该做什么? 已经在聊天日志中了 。 |
| `structure` | `probatio.Schema \| None` | 数据必须有的形状, 或纯文本的 `None` 。 |
| `attachments` | `list[conversation.Attachment] \| None` | 有什么文件要和说明一起写  有什么问题吗? |
| `llm_api` | `llm.API \| None` | 呼叫者要求的LLM API。 已经附在聊天日志上 。 |

以聊天日志和生成的 `data` 的 `GenDataTaskResult` 返回 `conversation_id` : 无结构的字符串, 或匹配结构的字典 。

### 生成图像 {#generate-image}

```python
async def _async_generate_image(
    self, task: GenImageTask, chat_log: ChatLog
) -> GenImageTaskResult:
    """Handle a generate image task."""
```

上帝 `GenImageTask` 有 `name` , `instructions` 和可选 `attachments` 。 返回 `GenImageTaskResult` :

| 名称 | 类型 | 说明 |
| ---- | ---- | ----------- |
| `image_data` | `bytes` | 生生影像. |
| `conversation_id` | `str` | 聊天日志的标识 。 |
| `mime_type` | `str` | 图像的类型, 如 {H 他们在} 。 |
| `width` | `int \| None` | 夫人阁下,如果知道,以像素表示的宽度。 |
| `height` | `int \| None` | 高度以像素计,若知之. |
| `model` | `str \| None` | 造像的模型,如果知道的话。 |
| `revised_prompt` | `str \| None` | 模型实际使用的提示器,如果它重置的话. |

### 评价 {#evaluate}

```python
async def _async_evaluate(
    self, task: EvaluationTask
) -> EvaluationTaskResult:
    """Handle an evaluation task."""
```

一项评价任务要求模型判断一组针对某些状态,附件,或两者的问题,并以概率而不是自由文本回答. 它没有聊天记录。 `EvaluationTask`这些字段:

| 名称 | 类型 | 说明 |
| ---- | ---- | ----------- |
| `name` | `str` | 任务名称,用于日志和痕迹. |
| `questions` | `dict[str, EvaluationQuestion]` | 问题,用身份证按键 |
| `state` | JSON值 | 判断数据,或`None`。 |
| `attachments` | `list[conversation.Attachment] \| None` | 审判文件 |

Home Assistant 拒绝一个既无`state` 也没有附件的任务 。 每个问题都有`type`和`instructions`:

- `noul`:是或没有问题。 用 `NoulAnswer` 回答, 是 的概率 。
- `choice` : 在`criteria` 中从至少两个命名的替代品中选择一个 。 用 `ChoiceAnswer` 回答: 选中的密钥和每个密钥的概率 。
- 统计数据 `score`: 从`criteria`中命令的列表中选择一个级别 。 用 `ScoreAnswer` 回答: 预期水平指数和每个水平的概率。

返回 `EvaluationTaskResult` 与 `answers` 键入与问题相同的 ID 。

## 结构化产出 {#structured-output}

在动作中,用户以 [选择器](/glossary/selector) 描述结构: 每个字段都有一个选择器, 并且可以选择 `description` 和 `required` 。 字段是可选的,除非`required`是`true`,而且数据可能不包括结构以外的字段.

```yaml
structure:
  name:
    description: "The name of the animal"
    required: true
    selector:
      text:
  legs:
    selector:
      number:
```

Home Assistant 把它变成`probatio.Schema` 在它到达你的实体之前, 密钥上保留了描述 。 转换为您的模型的图案格式, 通常是 JSON 的图案格式, 并询问模型的输出格式 。 然后解析答案,还原字典. 如果模型返回不解析的东西, 则升起 `HomeAssistantError` 。

## 状态 {#states}

状态是实体处理的最后一个任务的时间戳, 或第一个任务之前的 `unknown` 。 Home Assistant 设置并恢复它;`state` 属性是最终的 。

## 示例 {#example}

```python
import json

from homeassistant.components import ai_task, conversation
from homeassistant.exceptions import HomeAssistantError

Feature = ai_task.AITaskEntityFeature

class MyAITask(ai_task.AITaskEntity):
    """AI tasks with a cloud model."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_supported_features = Feature.GENERATE_DATA

    def __init__(self, entry: MyConfigEntry) -> None:
        """Set up the entity."""
        self.client = entry.runtime_data
        self._attr_unique_id = f"{entry.entry_id}_ai_task"

    async def _async_generate_data(
        self,
        task: ai_task.GenDataTask,
        chat_log: conversation.ChatLog,
    ) -> ai_task.GenDataTaskResult:
        """Send the chat log to the model and return its answer."""
        text = await self.client.complete(chat_log, task.structure)
        chat_log.async_add_assistant_content_without_tools(
            conversation.AssistantContent(
                agent_id=self.entity_id, content=text
            )
        )

        if not task.structure:
            return ai_task.GenDataTaskResult(
                conversation_id=chat_log.conversation_id, data=text
            )

        try:
            data = json.loads(text)
        except json.JSONDecodeError as err:
            raise HomeAssistantError("Model returned invalid JSON") from err

        return ai_task.GenDataTaskResult(
            conversation_id=chat_log.conversation_id, data=data
        )
```

`client.complete` 代表您的客户端库, 它将聊天日志和结构转换为模型格式 。
