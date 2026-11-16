---
title: 测试 Android 应用
description: 如何为Android应用程序编写测试,以及如何与JUnited,MockK,Robolectric,和Turbine一起编写单位测试.
sidebarLabel: 测试和单位测试
sidebarGroup: 测试
order: 1
---



# 测试 Android 应用 {#testing-the-android-app}
测试之所以存在是因为人们犯了错误. 一个在飞船前捕捉错误的测试,可以使用户免于挫折,而你免于调试会话. 每个pull request改变行为都伴随着测试

## 测试类型 {#kinds-of-tests}

| 温柔 | 运行在 | 用它 Is it for | 页次 |
| --- | --- | --- | --- |
| 单位 | 联合核查团,必要时配备机器人 | 逻辑: 查看模式、 管理器、 寄存器 | 本页 |
| 截图 | 联合核查团 | 如何构建用户界面 | [截图测试](/companion/android/screenshot-testing) |
| 仪器 | 模拟器 | 真正的Android运行时的行为 | [仪器测试](/companion/android/instrumentation-testing) |
| 端对端 | 模拟器, 相对于真实的 Home Assistant | 从登录到仪表板的关键路径 | [端到端测试](/companion/android/e2e-testing) |

从单位测试开始. 它们速度很快,大多数代码应该可以这样测试. 仅在您需要的时候才会移动列表 。

## 命名测试 {#naming-tests}

名称测试作为句子, 遵循[给,当,然后](https://en.wikipedia.org/wiki/Given-When-Then). 你看,没有读到测试就崩溃了:

```kotlin
@Test
fun `Given user authenticated when opening app then show dashboard`() {
    // Test implementation
}
```

- ** 初始情况、设置。
- ** 当**是您测试的动作或事件。
- ** 那么,** 是你们期望的结果。

## 测试什么 {#what-to-test}

- ** ** 通过公众API测试行为**,而不是实施细节.  遵循公共界面的测试能幸存的重构.
- ** 别为测试扩大能见度。 ** 通过公众入口进行测试。 当没有其他方法时,请使用[`@VisibleForTesting`](https://developer.android.com/reference/kotlin/androidx/annotation/VisibleForTesting),例如用于一个需要`CoroutineScope`或`Clock`的构造器。 Lint在测试外标出任何使用这种成员的标记,CI在提示警告上失败.
- ** 测试您的代码,而不是库。 ** 如果你发现自己在测试一个库, 将测试贡献给那个库。朔尔,当你想陷害一个图书馆的行为, 说为什么在测试。
- ** 编写测试文件。 ** 测试是您开发时的工具, 而不是之后的弦乐。 他们让你检查你的代码 不运行整个应用程序, 写他们早期 保持代码测试。
- ** 别为它而测试。 ** 跳过微不足道的代码。 测试应该帮助你 现在或下一个人以后。
- ** 保持测试的独立性。 ** 测试不得依赖其他测试,也不得依赖它们运行的顺序.
- ** 每个测试一个行为。 ** 将近似相同的测试合并为参数化的测试, 并配以 `@ParameterizedTest` 。
- ** 在一个类中保留一个特性的测试**,在`src/test/kotlin/`中反射源结构.
- ** 从来没有`Thread.sleep`。 ** 使用 `runTest`, 这是假的时间 。

## 单位测试 {#unit-tests}

```bash
./gradlew test
./gradlew :common:test
```

### 框架 {#frameworks}

- 用于单位测试. JUl 4仅在Robolectric需要的情况下运行;两者均运行在JUl平台上.
- {\fn黑体\fs20\shad2\2aH82\3aH20\4aH33\fscx95\3cH592001\be1}对模拟赛来说 {\fn黑体\fs20\shad2\2aH82\3aH20\4aH33\fscx95\3cH592001\be1}是的 当你可以的时候,你更喜欢真正的物体或者假的。
- 每一次流程测试都要使用QQL0}**.
- 对于需要Android API的代码,你无法嘲弄或伪造好. 更喜欢仪器测试

测试是这样的:

```kotlin
@Test
fun `Given a valid user ID when fetching details then return user`() {
    // Given
    val expectedUser = User(id = "12345", name = "John Doe")
    every { userRepository.getUser("12345") } returns expectedUser

    // When
    val result = userService.getUserDetails("12345")

    // Then
    assertEquals(expectedUser, result)
}
```

### 机器人 {#robolectric}

每个机器人测试课都需要这两个说明. 没有他们,Robolectric开始真正的应用,它打开了BureauMode和FailFast,可以崩溃测试JVM:

```kotlin
@RunWith(RobolectricTestRunner::class)
@Config(application = HiltTestApplication::class)
class MyTest {
    // Tests
}
```

Robolectric只和JUnit 4合作(参见[这个机器人问题](https://github.com/robolectric/robolectric/issues/3477)),因此项目保留JUnit 4用于这些测试. 如果您的代码依赖于Android系统的真实状态, 请写 [有一个仪器测试](/companion/android/instrumentation-testing) 。

### 流量 {#flows}

使用涡轮测试流. 与 `awaitItem`, `awaitComplete` 和 `expectNoEvents` 同步 。 当同时收集多个流量时使用 `turbineScope` 和 `testIn` 。 用 `shareIn` 完成的流量永远不会完成: 结束为 `expectNoEvents()` 和 `cancelAndConsumeRemainingEvents()` 而不是 `awaitComplete()` 。

永远不要在排放上与拉链、睡眠或`verify(timeout = ...)`同步。

### 科罗提恩和主要调度员 {#coroutines-and-the-main-dispatcher}

在`viewModelScope`中运行缜密的代码使用主调度器,这在JVM上并不存在. 替换为测试调度器, 使用匹配您的框架的帮助 :

```kotlin
// JUnit Jupiter
@ExtendWith(MainDispatcherJUnit5Extension::class)
class MyViewModelTest

// JUnit 4 and Robolectric
@get:Rule
val mainDispatcherRule = MainDispatcherJUnit4Rule()
```

只加入实际接触主调度器的测试中. 两者均使用 `StandardTestDispatcher`; 以 `runTest` 和 `advanceUntilIdle` 推进 。 不要切换到 `UnconfinedTestDispatcher` 才能通过测试 。 那会隐藏一个命令 测试应该检查。

### 共享测试助手 {#shared-test-helpers}

`:testing-unit` 模块持有在几个模块中测试所使用的助手 。 在你写新书前看看 其中,它上面有主要的调度器助手,一个`FakeClock`,和`TestSharedFlow`. 保持`:testing-unit`独立于`:common`,以避免循环依赖.

适用于模块中每个测试的规则,如重设全过程状态的规则,就是通过`ServiceLoader`注册的JUnit平台听众. Robolectric在自己的班级加载器中运行测试,因此这样的规则也需要Robolectric插件. 现有的 `TestStateResetPlatformListener` 和`TestStateResetRobolectricPlugin` 如何显示 。
