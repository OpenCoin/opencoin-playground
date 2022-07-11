# Schemata

Elements of messages, but never used standalone

## CDD

### Fields

- **[additional_info](fields.md#additional_info)**: A field where the issuer can store additional information about the currency.  *(String)*
- **[cdd_expiry_date](fields.md#cdd_expiry_date)**: When does the CDD expire?  *(String)*
- **[cdd_location](fields.md#cdd_location)**: Hint to download the CDD if not available anyway.  *(URL)*
- **[cdd_serial](fields.md#cdd_serial)**: The version of the CDD.  *(Int)*
- **[cdd_signing_date](fields.md#cdd_signing_date)**: When was the CDD signed?  *(DateTime)*
- **[currency_divisor](fields.md#currency_divisor)**: Used to express the value in units of 'currency name'.  *(Int)*
- **[currency_name](fields.md#currency_name)**: The name of the currency, e.g. Dollar.  *(String)*
- **[denominations](fields.md#denominations)**: The list of possible denominations.  *(List of Int)*
- **[id](fields.md#id)**: Identifier, a somewhat redundant hash of the [PublicKey](schemata.md#publickey)  *(BigInt)*
- **[info_service](fields.md#info_service)**: A list of locations where more information about the currency can be found.  *(WeightedURLList)*
- **[redeem_service](fields.md#redeem_service)**: A list of locations where [Coins](schemata.md#coin) can be redeemed.  *(WeightedURLList)*
- **[issuer_cipher_suite](fields.md#issuer_cipher_suite)**: Identifier of the cipher suite that is used.  *(String)*
- **[issuer_public_master_key](fields.md#issuer_public_master_key)**: The hash of the issuer's public key  *([PublicKey](schemata.md#publickey))*
- **[protocol_version](fields.md#protocol_version)**: The protocol version that was used.  *(Url)*
- **[renew_service](fields.md#renew_service)**: A list of locations where [Coins](schemata.md#coin) can be renewed.  *(WeightedURLList)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*
- **[mint_service](fields.md#mint_service)**: A list of locations where [Blinds](schemata.md#blind) can be minted into [Coins](schemata.md#coin)  *(WeightedURLList)*

### Example

```json
{
  "additional_info": "",
  "cdd_expiry_date": "2023-07-11T08:39:38.421080",
  "cdd_location": "https://opencent.org",
  "cdd_serial": 1,
  "cdd_signing_date": "2022-07-11T08:39:38.421080",
  "currency_divisor": 100,
  "currency_name": "OpenCent",
  "denominations": [1, 2, 5],
  "id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
  "info_service": [
        [10, "https://opencent.org"]
      ],
  "issuer_cipher_suite": "RSA-SHA512-CHAUM86",
  "issuer_public_master_key": {
    "modulus": "a45b9342b15deff8a5ba1a0dce50c06a0d34ac8ab251d0cf62ff6db825a714b57fcb8b243862ae539c3e997ebefc31c9983a6300ea08b81a4f613447f9123829",
    "public_exponent": 65537,
    "type": "rsa public key"
  },
  "mint_service": [
        [10, "https://opencent.org"],
    [20, "https://opencent.com/validate"]
      ],
  "protocol_version": "https://opencoin.org/1.0",
  "redeem_service": [
        [10, "https://opencent.org"]
      ],
  "renew_service": [
        [10, "https://opencent.org"]
      ],
  "type": "cdd"
}
```
[Source](artifacts/cdd.json)


## CDDC

### Fields

- **[cdd](fields.md#cdd)**: Contains the Currency Description Document (CDD)  *([CDD](schemata.md#cdd))*
- **[signature](fields.md#signature)**: A signature within a certificate.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "cdd": {
    "additional_info": "",
    "cdd_expiry_date": "2023-07-11T08:39:38.421080",
    "cdd_location": "https://opencent.org",
    "cdd_serial": 1,
    "cdd_signing_date": "2022-07-11T08:39:38.421080",
    "currency_divisor": 100,
    "currency_name": "OpenCent",
    "denominations": [1, 2, 5],
    "id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
    "info_service": [
        [10, "https://opencent.org"]
      ],
    "issuer_cipher_suite": "RSA-SHA512-CHAUM86",
    "issuer_public_master_key": {
      "modulus": "a45b9342b15deff8a5ba1a0dce50c06a0d34ac8ab251d0cf62ff6db825a714b57fcb8b243862ae539c3e997ebefc31c9983a6300ea08b81a4f613447f9123829",
      "public_exponent": 65537,
      "type": "rsa public key"
    },
    "mint_service": [
        [10, "https://opencent.org"],
      [20, "https://opencent.com/validate"]
      ],
    "protocol_version": "https://opencoin.org/1.0",
    "redeem_service": [
        [10, "https://opencent.org"]
      ],
    "renew_service": [
        [10, "https://opencent.org"]
      ],
    "type": "cdd"
  },
  "signature": "1e38b379d5259d7d09094a458955b3892d36aa98bd40ff6625ffd15d145da2d7f3997360ceb9d9d86a004e362249f01dd7c35779ae79987121430402f8d43c5d",
  "type": "cdd certificate"
}
```
[Source](artifacts/cddc.json)


## PublicKey

### Fields

- **[modulus](fields.md#modulus)**: The modulus of the public key  *(BigInt)*
- **[public_exponent](fields.md#public_exponent)**: The exponent of the public key.  *(BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "modulus": "a45b9342b15deff8a5ba1a0dce50c06a0d34ac8ab251d0cf62ff6db825a714b57fcb8b243862ae539c3e997ebefc31c9983a6300ea08b81a4f613447f9123829",
  "public_exponent": 65537,
  "type": "rsa public key"
}
```
[Source](artifacts/issuer_public_master_key.json)

See [MKC](#mkc)

## MintKey

### Fields

- **[cdd_serial](fields.md#cdd_serial)**: The version of the CDD.  *(Int)*
- **[coins_expiry_date](fields.md#coins_expiry_date)**: Coins expire after this date.  *(DateTime)*
- **[denomination](fields.md#denomination)**: The value of the coin(s).  *(Int)*
- **[id](fields.md#id)**: Identifier, a somewhat redundant hash of the [PublicKey](schemata.md#publickey)  *(BigInt)*
- **[issuer_id](fields.md#issuer_id)**: Id (hash) of the issuer public master key in the CDDC  *(BigInt)*
- **[public_mint_key](fields.md#public_mint_key)**: The public key of the mint key.  *([PublicKey](schemata.md#publickey))*
- **[sign_coins_not_after](fields.md#sign_coins_not_after)**: Use [MintKey](schemata.md#mintkey) only before this date.  *(DateTime)*
- **[sign_coins_not_before](fields.md#sign_coins_not_before)**: Use [MintKey](schemata.md#mintkey) only after this date.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "cdd_serial": 1,
  "coins_expiry_date": "2023-10-19T08:39:38.421080",
  "denomination": 1,
  "id": "e3e053d4fa03ba6b857051bbd3b9f7c7b0c05e42f6260712139450e18b2c94bc",
  "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
  "public_mint_key": {
    "modulus": "9cf7454307e7cb5a7cee5bf46eeb0e214daeed0fd9ad35192434af31195fc32b190ec32c2270517a59856397242601b365ca57bf3b64dd66e3c61f7d253e2dbf",
    "public_exponent": 65537,
    "type": "rsa public key"
  },
  "sign_coins_not_after": "2023-07-11T08:39:38.421080",
  "sign_coins_not_before": "2022-07-11T08:39:38.421080",
  "type": "mint key"
}
```
[Source](artifacts/mintkey_1.json)


## MKC

A *Mint Key Certificate*.

### Fields

- **[mint_key](fields.md#mint_key)**: The mint key that was signed in the certificate  *([MintKey](schemata.md#mintkey))*
- **[signature](fields.md#signature)**: A signature within a certificate.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "mint_key": {
    "cdd_serial": 1,
    "coins_expiry_date": "2023-10-19T08:39:38.421080",
    "denomination": 1,
    "id": "e3e053d4fa03ba6b857051bbd3b9f7c7b0c05e42f6260712139450e18b2c94bc",
    "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
    "public_mint_key": {
      "modulus": "9cf7454307e7cb5a7cee5bf46eeb0e214daeed0fd9ad35192434af31195fc32b190ec32c2270517a59856397242601b365ca57bf3b64dd66e3c61f7d253e2dbf",
      "public_exponent": 65537,
      "type": "rsa public key"
    },
    "sign_coins_not_after": "2023-07-11T08:39:38.421080",
    "sign_coins_not_before": "2022-07-11T08:39:38.421080",
    "type": "mint key"
  },
  "signature": "4c33d555c14e0728ac0e5676fcc4e1665abb7db1f4ec9bd0173bd52dea0801ab81c63742bd82b243a4464aa119178a9af8c23504fabc77ef9268167c2443e231",
  "type": "mint key certificate"
}
```
[Source](artifacts/mkc_1.json)

## Payload

### Fields

- **[cdd_location](fields.md#cdd_location)**: Hint to download the CDD if not available anyway.  *(URL)*
- **[denomination](fields.md#denomination)**: The value of the coin(s).  *(Int)*
- **[issuer_id](fields.md#issuer_id)**: Id (hash) of the issuer public master key in the CDDC  *(BigInt)*
- **[mint_key_id](fields.md#mint_key_id)**: Identifier of the mint key used.  *(BigInt)*
- **[protocol_version](fields.md#protocol_version)**: The protocol version that was used.  *(Url)*
- **[serial](fields.md#serial)**: The serial of the [Coin](schemata.md#coin).  *(BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "cdd_location": "https://opencent.org",
  "denomination": 1,
  "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
  "mint_key_id": "e3e053d4fa03ba6b857051bbd3b9f7c7b0c05e42f6260712139450e18b2c94bc",
  "protocol_version": "https://opencoin.org/1.0",
  "serial": "947c8ab50b05b92e7949362b1e714b833ac2748ab9df43d7a3b7a9c33a5a46eb",
  "type": "payload"
}
```
[Source](artifacts/payload_a0.json)

## Blind

### Fields

- **[blinded_payload_hash](fields.md#blinded_payload_hash)**: The blinded hash of a payload.  *(BigInt)*
- **[mint_key_id](fields.md#mint_key_id)**: Identifier of the mint key used.  *(BigInt)*
- **[reference](fields.md#reference)**: An identifier that connects [Blind](schemata.md#blind), [BlindSignature](schemata.md#blindsignature) and blinding secrets.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "blinded_payload_hash": "9920380bd19718b319833af6166b5a22d9c1265084e4a2ab08740e2e9ccdbbabce575c14ead9d97783b0095d97023471ff018cc7d334fbdc8a13a3281a2cc3fc",
  "mint_key_id": "e3e053d4fa03ba6b857051bbd3b9f7c7b0c05e42f6260712139450e18b2c94bc",
  "reference": "a0",
  "type": "blinded payload hash"
}
```
[Source](artifacts/blind_a0.json)

## BlindSignature

### Fields

- **[blind_signature](fields.md#blind_signature)**: The signature on the blinded hash of a payload.  *(BigInt)*
- **[reference](fields.md#reference)**: An identifier that connects [Blind](schemata.md#blind), [BlindSignature](schemata.md#blindsignature) and blinding secrets.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "blind_signature": "470f61eefcf2fa82afd216a618df615d9a8a4d26047b448d94f61c6dd2514cb93032e17b842e63747723ed9bc729934012597207f269be208e437709455f10f9",
  "reference": "a0",
  "type": "blind signature"
}
```
[Source](artifacts/blind_signature_a0.json)

## Coin

### Fields

- **[payload](fields.md#payload)**: The payload of the coin.  *([Payload](schemata.md#payload))*
- **[signature](fields.md#signature)**: A signature within a certificate.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "payload": {
    "cdd_location": "https://opencent.org",
    "denomination": 1,
    "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
    "mint_key_id": "e3e053d4fa03ba6b857051bbd3b9f7c7b0c05e42f6260712139450e18b2c94bc",
    "protocol_version": "https://opencoin.org/1.0",
    "serial": "947c8ab50b05b92e7949362b1e714b833ac2748ab9df43d7a3b7a9c33a5a46eb",
    "type": "payload"
  },
  "signature": "50be266f4644cd09e7dc222b64b1e002f1760290f13ff7ddbd52fcdf3d8b3c1ef8b981e68b655f5be128526aba718775ab947f322c074031a3380cdb5dd1feb",
  "type": "coin"
}
```
[Source](artifacts/coin_a0.json)

## RequestCDDSerial Message

### Fields

- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "message_reference": 100000,
  "type": "request cdd serial"
}
```
[Source](artifacts/request_cddc_serial.json)

## ResponseCDDSerial Message

- **[cdd_serial](fields.md#cdd_serial)**: The version of the CDD.  *(Int)*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Fields

### Example

```json
{
  "cdd_serial": 1,
  "message_reference": 100000,
  "status_code": 200,
  "status_description": "ok",
  "type": "response cdd serial"
}
```
[Source](artifacts/response_cddc_serial.json)

## RequestCDDC Message

- **[cdd_serial](fields.md#cdd_serial)**: The version of the CDD.  *(Int)*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Fields

### Example

```json
{
  "cdd_serial": 1,
  "message_reference": 100001,
  "type": "request cddc"
}
```
[Source](artifacts/request_cddc.json)

## ResponseCDDC Message

### Fields

- **[cddc](fields.md#cddc)**: A full Currency Description Document Certificate.  *([CDDC](schemata.md#cddc))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "cddc": {
    "cdd": {
      "additional_info": "",
      "cdd_expiry_date": "2023-07-11T08:39:38.421080",
      "cdd_location": "https://opencent.org",
      "cdd_serial": 1,
      "cdd_signing_date": "2022-07-11T08:39:38.421080",
      "currency_divisor": 100,
      "currency_name": "OpenCent",
      "denominations": [1, 2, 5],
      "id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
      "info_service": [
        [10, "https://opencent.org"]
      ],
      "issuer_cipher_suite": "RSA-SHA512-CHAUM86",
      "issuer_public_master_key": {
        "modulus": "a45b9342b15deff8a5ba1a0dce50c06a0d34ac8ab251d0cf62ff6db825a714b57fcb8b243862ae539c3e997ebefc31c9983a6300ea08b81a4f613447f9123829",
        "public_exponent": 65537,
        "type": "rsa public key"
      },
      "mint_service": [
        [10, "https://opencent.org"],
        [20, "https://opencent.com/validate"]
      ],
      "protocol_version": "https://opencoin.org/1.0",
      "redeem_service": [
        [10, "https://opencent.org"]
      ],
      "renew_service": [
        [10, "https://opencent.org"]
      ],
      "type": "cdd"
    },
    "signature": "1e38b379d5259d7d09094a458955b3892d36aa98bd40ff6625ffd15d145da2d7f3997360ceb9d9d86a004e362249f01dd7c35779ae79987121430402f8d43c5d",
    "type": "cdd certificate"
  },
  "message_reference": 100001,
  "status_code": 200,
  "status_description": "ok",
  "type": "response cddc"
}
```
[Source](artifacts/response_cddc.json)

## RequestMKCs Message

- **[denominations](fields.md#denominations)**: The list of possible denominations.  *(List of Int)*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[mint_key_ids](fields.md#mint_key_ids)**: What mint keys should be returned?  *(List of BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Fields

### Example

```json
{
  "denominations": [1, 2, 5],
  "message_reference": 100002,
  "mint_key_ids": [],
  "type": "request mint key certificates"
}
```
[Source](artifacts/request_mkc.json)

## ResponseMKCs Message

- **[keys](fields.md#keys)**: A list of Mint Key Certificates  *(List of [MKCs](schemata.md#mkc))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Fields

### Example

```json
{
  "keys": [
    {
      "mint_key": {
        "cdd_serial": 1,
        "coins_expiry_date": "2023-10-19T08:39:38.421080",
        "denomination": 1,
        "id": "e3e053d4fa03ba6b857051bbd3b9f7c7b0c05e42f6260712139450e18b2c94bc",
        "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
        "public_mint_key": {
          "modulus": "9cf7454307e7cb5a7cee5bf46eeb0e214daeed0fd9ad35192434af31195fc32b190ec32c2270517a59856397242601b365ca57bf3b64dd66e3c61f7d253e2dbf",
          "public_exponent": 65537,
          "type": "rsa public key"
        },
        "sign_coins_not_after": "2023-07-11T08:39:38.421080",
        "sign_coins_not_before": "2022-07-11T08:39:38.421080",
        "type": "mint key"
      },
      "signature": "4c33d555c14e0728ac0e5676fcc4e1665abb7db1f4ec9bd0173bd52dea0801ab81c63742bd82b243a4464aa119178a9af8c23504fabc77ef9268167c2443e231",
      "type": "mint key certificate"
    },
    {
      "mint_key": {
        "cdd_serial": 1,
        "coins_expiry_date": "2023-10-19T08:39:38.421080",
        "denomination": 2,
        "id": "3f3a34c8df9abaee2030bb7aee86bfdb896f85affc9a01fec984deb06c077c62",
        "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
        "public_mint_key": {
          "modulus": "9d218bbeaf2a8a2074e208082f8f02f91b8afd20909e023a347a97a3c0b56059013148ae9f81c3aa242c3822682e572dab24a74bd344a651ef7f06fc1493bc91",
          "public_exponent": 65537,
          "type": "rsa public key"
        },
        "sign_coins_not_after": "2023-07-11T08:39:38.421080",
        "sign_coins_not_before": "2022-07-11T08:39:38.421080",
        "type": "mint key"
      },
      "signature": "1ad4952f625078188de83c4f76ef7a47a696056a4f7acefe24f2309867775fcce3fbbf87f76944a1a8a7bc4277c532720c5fd13c4cbf65eb23d222401b4b99c9",
      "type": "mint key certificate"
    },
    {
      "mint_key": {
        "cdd_serial": 1,
        "coins_expiry_date": "2023-10-19T08:39:38.421080",
        "denomination": 5,
        "id": "2aaa99a9ffbd0377b46d757bbf82d4f65b4f05a170a2da23743066849c403776",
        "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
        "public_mint_key": {
          "modulus": "acd3ad0b8e8bf5c27f9b9c00d3057e0be8617837f1a33427dd3eaffe00f9f785d5632268d919ac5623d55f173b47eb975cb103dad8886b771f13f0b804405f81",
          "public_exponent": 65537,
          "type": "rsa public key"
        },
        "sign_coins_not_after": "2023-07-11T08:39:38.421080",
        "sign_coins_not_before": "2022-07-11T08:39:38.421080",
        "type": "mint key"
      },
      "signature": "153660ad076ded345b99701cf62ca50473ec7f80e76193cf4a5cf476175e9ca3d366859590d1dbd56e31447bb319b98f5c368d181478e011c135eacb66b99b03",
      "type": "mint key certificate"
    }
  ],
  "message_reference": 100002,
  "status_code": 200,
  "status_description": "ok",
  "type": "response mint key certificates"
}
```
[Source](artifacts/response_mkc.json)

## RequestMint Message

### Fields

- **[blinds](fields.md#blinds)**: A List of Blinds  *(List of [Blinds](schemata.md#blind))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[transaction_reference](fields.md#transaction_reference)**: A random identifier that allows the client to resume a delayed mint/renew process.  *(BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "blinds": [
    {
      "blinded_payload_hash": "9920380bd19718b319833af6166b5a22d9c1265084e4a2ab08740e2e9ccdbbabce575c14ead9d97783b0095d97023471ff018cc7d334fbdc8a13a3281a2cc3fc",
      "mint_key_id": "e3e053d4fa03ba6b857051bbd3b9f7c7b0c05e42f6260712139450e18b2c94bc",
      "reference": "a0",
      "type": "blinded payload hash"
    },
    {
      "blinded_payload_hash": "20e5236334720449c4bd930900e607804711b6cff41fefbeea8ed7f79a6093a29b27a74541bbc6b1967984f88347c24f34b4e2463ca0250deb78f3f982b21a70",
      "mint_key_id": "3f3a34c8df9abaee2030bb7aee86bfdb896f85affc9a01fec984deb06c077c62",
      "reference": "a1",
      "type": "blinded payload hash"
    },
    {
      "blinded_payload_hash": "46a495a7a62536885c244c4fb79eaa1ae0b6d9ba2a66157a0558727502abd6a57861a387f52a3e040799dd8dcc758083b00cfc312ace4fc4eebbc787bf742448",
      "mint_key_id": "2aaa99a9ffbd0377b46d757bbf82d4f65b4f05a170a2da23743066849c403776",
      "reference": "a2",
      "type": "blinded payload hash"
    }
  ],
  "message_reference": 100003,
  "transaction_reference": "f2b96ff94fe2becca5ff385cb6989de4f6f06eefdc64a909906e56d11a5460ad",
  "type": "request mint"
}
```
[Source](artifacts/request_mint.json)

## ResponseMint Message

### Fields

- **[blind_signatures](fields.md#blind_signatures)**: A list of BlindSignatures.  *(List of [BlindSignatures](schemata.md#blindsignature))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "blind_signatures": [
    {
      "blind_signature": "470f61eefcf2fa82afd216a618df615d9a8a4d26047b448d94f61c6dd2514cb93032e17b842e63747723ed9bc729934012597207f269be208e437709455f10f9",
      "reference": "a0",
      "type": "blind signature"
    },
    {
      "blind_signature": "4e04c0ab289c65364e382ddb3b6a5ba4b4efc7ab2761d6f32c8bc3802c26d9704a1e6a4191a788ecbc4985f1e9a45ddc904447733d50a4f65597cba85cd2252b",
      "reference": "a1",
      "type": "blind signature"
    },
    {
      "blind_signature": "8cebe20e9464e4afe22d8db136a6a7dcf75ed868a1d3683b4a888bdd0e98cfa84a0edc00963317667850b9ce06df8048f617a58bda8bd340c935ba309e8ce5bd",
      "reference": "a2",
      "type": "blind signature"
    }
  ],
  "message_reference": 100003,
  "status_code": 200,
  "status_description": "ok",
  "type": "response mint"
}
```
[Source](artifacts/response_mint_a.json)

## CoinStack Message

### Fields

- **[coins](fields.md#coins)**: A list of coins.  *(List of [Coins](schemata.md#coin))*
- **[subject](fields.md#subject)**: A message that can be passed along with the coin stack.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "coins": [
    {
      "payload": {
        "cdd_location": "https://opencent.org",
        "denomination": 1,
        "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
        "mint_key_id": "e3e053d4fa03ba6b857051bbd3b9f7c7b0c05e42f6260712139450e18b2c94bc",
        "protocol_version": "https://opencoin.org/1.0",
        "serial": "947c8ab50b05b92e7949362b1e714b833ac2748ab9df43d7a3b7a9c33a5a46eb",
        "type": "payload"
      },
      "signature": "50be266f4644cd09e7dc222b64b1e002f1760290f13ff7ddbd52fcdf3d8b3c1ef8b981e68b655f5be128526aba718775ab947f322c074031a3380cdb5dd1feb",
      "type": "coin"
    },
    {
      "payload": {
        "cdd_location": "https://opencent.org",
        "denomination": 2,
        "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
        "mint_key_id": "3f3a34c8df9abaee2030bb7aee86bfdb896f85affc9a01fec984deb06c077c62",
        "protocol_version": "https://opencoin.org/1.0",
        "serial": "e2c1c0093af6535f3d801e811d904b2891ef35a65d0e87955397db3db993ca59",
        "type": "payload"
      },
      "signature": "66c2befe37d30744691fec39a9056c530f439a4879c9a388018409ece20446b342bc7889f40efad4674d778b9f130b13a39bea03a214c80c4703bf0ba4993294",
      "type": "coin"
    },
    {
      "payload": {
        "cdd_location": "https://opencent.org",
        "denomination": 5,
        "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
        "mint_key_id": "2aaa99a9ffbd0377b46d757bbf82d4f65b4f05a170a2da23743066849c403776",
        "protocol_version": "https://opencoin.org/1.0",
        "serial": "c58356123496667ac18786f09123be1bf9116596ad30ceb676c34c8c439f1377",
        "type": "payload"
      },
      "signature": "6ae0dcc4af9e47e4e4478b7f2ec172645fa744fa7dcf55a4544ab01eadd601188099e6c27dc441231b73913a95f33e64915f5a4d43c1e21f5fd6f27a61a5304e",
      "type": "coin"
    }
  ],
  "subject": "a little gift",
  "type": "coinstack"
}
```
[Source](artifacts/coinstack.json)

## RequestRenew Message

Coins that are received need to be swapped for new ones, in order to protect the receiver against double spending. Otherwise, the sender could keep a copy of the coins and try to use the coins again. Before doing so we need to ask: what coin sizes should be chosen for the coins to be minted?

What if we have not the right coin selection for an amount to pay?  Imagine that the price is 5 opencent, but we just have coins in the sizes: 2, 2, 2.

One solution would be to require the recipient to give change. This would make the protocol more complicated, and would just shift the problem to the recipient. Another approach is to allow partial spending coins, but this again makes the protocol more complicated.[^partial]

The easy way out is to aim for a selection of coins that allows us to pay *any* amount below or equal to the sum of all coins. E.g. if we own the value of 6 opencent it would be advisable to have coin selection 2,2,1,1 in order to pay all possible amounts. This also prevents *amount tracing*, where an awkward price (13.37) asks for an awkward coin exchange at the issuer beforehand.

So, we need to look at the combined sum of coins received and coins already in possession, and needs to find the right coin selection to be able to make all possible future coin transfers. We will then know which coins to keep, and what blinds to make and paying for the minting using *all* the just received coins and using *some* existing coins.

### Fields

- **[blinds](fields.md#blinds)**: A List of Blinds  *(List of [Blinds](schemata.md#blind))*
- **[coins](fields.md#coins)**: A list of coins.  *(List of [Coins](schemata.md#coin))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[transaction_reference](fields.md#transaction_reference)**: A random identifier that allows the client to resume a delayed mint/renew process.  *(BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "blinds": [
    {
      "blinded_payload_hash": "2186fc8b344ad4339214d8d3784fccd75e39d6f39e9c85457f95c663a091147fe5afb03097566ca976bd2ca0a7c0690679cdfdd33906112773b46f6d8a7aa4db",
      "mint_key_id": "3f3a34c8df9abaee2030bb7aee86bfdb896f85affc9a01fec984deb06c077c62",
      "reference": "b0",
      "type": "blinded payload hash"
    },
    {
      "blinded_payload_hash": "468410cb8c4b386a89c2bc2daa263132c704c99eeb4bfa26e37310800dd809f7659b9d1c38ec624858cf52324adc121cab3444344657f117e2e49ee274c229ff",
      "mint_key_id": "3f3a34c8df9abaee2030bb7aee86bfdb896f85affc9a01fec984deb06c077c62",
      "reference": "b1",
      "type": "blinded payload hash"
    },
    {
      "blinded_payload_hash": "ab7d98df621495a7d4c190bf1aecc6693a2ae7c3d5ded687fa8643f815f7029a46f8cc1581cc73d1566e9345a5559ee7c52b25c44c438ede424d17660b3abf3",
      "mint_key_id": "3f3a34c8df9abaee2030bb7aee86bfdb896f85affc9a01fec984deb06c077c62",
      "reference": "b2",
      "type": "blinded payload hash"
    },
    {
      "blinded_payload_hash": "9917a14a00dc164c65aad8ad9041c15d6525c7b2d6ce5e1374b67392f354ab8b1f633482dc9da6570b874313b501c5e7cf0051654e7d619d6008539f2f8704cf",
      "mint_key_id": "3f3a34c8df9abaee2030bb7aee86bfdb896f85affc9a01fec984deb06c077c62",
      "reference": "b3",
      "type": "blinded payload hash"
    }
  ],
  "coins": [
    {
      "payload": {
        "cdd_location": "https://opencent.org",
        "denomination": 1,
        "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
        "mint_key_id": "e3e053d4fa03ba6b857051bbd3b9f7c7b0c05e42f6260712139450e18b2c94bc",
        "protocol_version": "https://opencoin.org/1.0",
        "serial": "947c8ab50b05b92e7949362b1e714b833ac2748ab9df43d7a3b7a9c33a5a46eb",
        "type": "payload"
      },
      "signature": "50be266f4644cd09e7dc222b64b1e002f1760290f13ff7ddbd52fcdf3d8b3c1ef8b981e68b655f5be128526aba718775ab947f322c074031a3380cdb5dd1feb",
      "type": "coin"
    },
    {
      "payload": {
        "cdd_location": "https://opencent.org",
        "denomination": 2,
        "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
        "mint_key_id": "3f3a34c8df9abaee2030bb7aee86bfdb896f85affc9a01fec984deb06c077c62",
        "protocol_version": "https://opencoin.org/1.0",
        "serial": "e2c1c0093af6535f3d801e811d904b2891ef35a65d0e87955397db3db993ca59",
        "type": "payload"
      },
      "signature": "66c2befe37d30744691fec39a9056c530f439a4879c9a388018409ece20446b342bc7889f40efad4674d778b9f130b13a39bea03a214c80c4703bf0ba4993294",
      "type": "coin"
    },
    {
      "payload": {
        "cdd_location": "https://opencent.org",
        "denomination": 5,
        "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
        "mint_key_id": "2aaa99a9ffbd0377b46d757bbf82d4f65b4f05a170a2da23743066849c403776",
        "protocol_version": "https://opencoin.org/1.0",
        "serial": "c58356123496667ac18786f09123be1bf9116596ad30ceb676c34c8c439f1377",
        "type": "payload"
      },
      "signature": "6ae0dcc4af9e47e4e4478b7f2ec172645fa744fa7dcf55a4544ab01eadd601188099e6c27dc441231b73913a95f33e64915f5a4d43c1e21f5fd6f27a61a5304e",
      "type": "coin"
    }
  ],
  "message_reference": 100004,
  "transaction_reference": "a88b8ba5519ed859d7bfa076d4c12937",
  "type": "request renew"
}
```
[Source](artifacts/request_renew.json)

## ResponseDelay Message

### Fields

- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "message_reference": 100004,
  "status_code": 300,
  "status_description": "ok",
  "type": "response delay"
}
```
[Source](artifacts/response_delay.json)

## RequestResume Message

### Fields

- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[transaction_reference](fields.md#transaction_reference)**: A random identifier that allows the client to resume a delayed mint/renew process.  *(BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "message_reference": 100005,
  "transaction_reference": "a88b8ba5519ed859d7bfa076d4c12937",
  "type": "request resume"
}
```
[Source](artifacts/request_resume.json)

## RequestRedeem Message

### Fields

- **[coins](fields.md#coins)**: A list of coins.  *(List of [Coins](schemata.md#coin))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "coins": [
    {
      "payload": {
        "cdd_location": "https://opencent.org",
        "denomination": 2,
        "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
        "mint_key_id": "3f3a34c8df9abaee2030bb7aee86bfdb896f85affc9a01fec984deb06c077c62",
        "protocol_version": "https://opencoin.org/1.0",
        "serial": "f8411ca510e367d831937739342158cbf09db8d34817f0dabddb80622ac784d7",
        "type": "payload"
      },
      "signature": "5d4c7ca9e97426aeb59f2fe22220e164f1b37f0931920494a359fdbc30d90064c843a04e0d16dda3dc1d83814b8bac934873a0c5317fc04b51cf3a912967d8b8",
      "type": "coin"
    },
    {
      "payload": {
        "cdd_location": "https://opencent.org",
        "denomination": 2,
        "issuer_id": "96fb652e249ddb9045f04fe64ba9663893ed46cf2bc117eb2674cbe09312762e",
        "mint_key_id": "3f3a34c8df9abaee2030bb7aee86bfdb896f85affc9a01fec984deb06c077c62",
        "protocol_version": "https://opencoin.org/1.0",
        "serial": "cca2647b1fd803e5fe5f0131489d450a1b5980ffa739da18b3b143ca8bd6fc79",
        "type": "payload"
      },
      "signature": "5bb381233bd3a0c9437ce7009b81263784fddf594a9843f611a752355025fdaf04368b51be50f311de9fb288b6ae927b50aa2885f64ca54bfba629d08c19c5c4",
      "type": "coin"
    }
  ],
  "message_reference": 100006,
  "type": "request redeem"
}
```
[Source](artifacts/request_redeem.json)

## ResponseRedeem Message

### Fields

- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```json
{
  "message_reference": 100006,
  "status_code": 200,
  "status_description": "ok",
  "type": "response redeem"
}
```
[Source](artifacts/response_redeem.json)

[^partial]: GNU Taler experiments with this approach: in essence coins don't have serials but keys, which can sign a partial amount to be spent. This requires more smartness to avoid double spending, introducing new problems to be solved.
