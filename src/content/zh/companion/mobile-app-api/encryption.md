---
title: 加密
description: 用 libsodium 密钥加密来加密 mobile app webhook 请求和响应 。
order: 3
---



# 加密 {#encryption}
Webhook请求经常通过家用网络的普通HTTP进行旅行,它们携带位置和传感器数据. `mobile_app` 可以双向加密它们 [lib](https://doc.libsodium.org/) 。 随时可以加密 。

## 打开它 {#turn-it-on}

有两种方式:

- ** 登记**:设置`supports_encryption`至`true`。 反应包含 `secret` 。
- ** 稍后**:发出[`enable_encryption`](/companion/mobile-app-api/encryption#enable-it-later)请求。

`secret`是你的钥匙。 安全保存,并保存 只要注册存在。 没有办法把它拿回来:用户无法在UI中查找,你不应该要求他们通过隐藏的存储文件进行挖掘. 如果您丢失了密钥, 或者加密持续失败, 请创建新的注册并告诉用户 。

一旦 为了加密, Home Assistant 将拒绝该注册中未加密的请求, 并带有 `400` 和错误代码 `encryption_required` 。

## 工作原理 {#how-it-works}

webhook使用libsodium的[密钥认证加密](https://doc.libsodium.org/secret-key_cryptography/secretbox),`crypto_secretbox`(XSalsa20与Poly1305).

- ** 键 ** 是 `secret`, 字符串为 64 十六进制字符 。 从六进制解码为32字节键.
- ** 简写** 是`data`中的JSON。 如果请求类型没有 `data`, 如 `get_config`, 则加密一个空对象, `{}` 。
- ** 密码**是非ce后加加密消息,编码为Base64,并附有原字母和编版. 这是`sodium_base64_VARIANT_ORIGINAL`。

把它放在请求中, 而不是 `data` :

```json
{
  "type": "update_location",
  "encrypted": true,
  "encrypted_data": "<Base64 nonce and ciphertext>"
}
```

内容的回复以相同的形状返回,`{"encrypted": true, "encrypted_data": "..."}`,用相同的密钥加密. 解密他们的方式相同。 少数回复从未加密,比如空的`{}`和`encryption_required`错误:[genome 答复](/companion/mobile-app-api/sending-data#the-response)列出它们. 检查是否在您解密前设置了 `encrypted` 。

> [!NOTE]
> 更古老的应用版本以不同的方式使用了这个秘密:其前32个字符作为原始密钥字节. Home Assistant仍然接受,对于从未用六进制键发送请求的注册. 第一项要求是用六角的报告中的与各键进行解密,然后将登记转换为永久登记。 新的应用只应使用六解码键.

## 选择库 {#choose-a-library}

Libsodium对大多数语言有约束性. 对袍夫来说,官方[快速钠](https://github.com/jedisct1/swift-sodium)是一个很好的选择. 其他语言参见[约束清单](https://doc.libsodium.org/bindings_for_other_languages). 当有多个时,选择一个得到积极维护和广泛使用.

## 稍后启用 {#enable-it-later}

注册可能没有加密,例如因为它是由一个更古老的应用程序制作的. 打开它:

```json
{
  "type": "enable_encryption"
}
```

回应包含新的秘密:

```json
{
  "secret": "<64 hexadecimal characters>"
}
```

这一要求没有加密,其答复也没有加密。 如果加密已经启动, 未加密的请求会得到通常的 `encryption_required` 错误, 而加密的请求会得到 `400` 错误代码 `encryption_already_enabled` 。
