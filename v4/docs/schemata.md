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

```{literalinclude} artifacts/cdd.json
:language: json
```


## CDDC

### Fields

- **[cdd](fields.md#cdd)**: Contains the Currency Description Document (CDD)  *([CDD](schemata.md#cdd))*
- **[signature](fields.md#signature)**: A signature within a certificate.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/cddc.json
:language: json
```


## PublicKey

### Fields

- **[modulus](fields.md#modulus)**: The modulus of the public key  *(BigInt)*
- **[public_exponent](fields.md#public_exponent)**: The exponent of the public key.  *(BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/issuer_public_master_key.json
:language: json
```

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

```{literalinclude} artifacts/mintkey_1.json
:language: json
```


## MKC

A *Mint Key Certificate*.

### Fields

- **[mint_key](fields.md#mint_key)**: The mint key that was signed in the certificate  *([MintKey](schemata.md#mintkey))*
- **[signature](fields.md#signature)**: A signature within a certificate.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/mkc_1.json
:language: json
```

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

```{literalinclude} artifacts/payload_a0.json
:language: json
```

## Blind

### Fields

- **[blinded_payload_hash](fields.md#blinded_payload_hash)**: The blinded hash of a payload.  *(BigInt)*
- **[mint_key_id](fields.md#mint_key_id)**: Identifier of the mint key used.  *(BigInt)*
- **[reference](fields.md#reference)**: An identifier that connects [Blind](schemata.md#blind), [BlindSignature](schemata.md#blindsignature) and blinding secrets.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/blind_a0.json
:language: json
```

## BlindSignature

### Fields

- **[blind_signature](fields.md#blind_signature)**: The signature on the blinded hash of a payload.  *(BigInt)*
- **[reference](fields.md#reference)**: An identifier that connects [Blind](schemata.md#blind), [BlindSignature](schemata.md#blindsignature) and blinding secrets.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/blind_signature_a0.json
:language: json
```

## Coin

### Fields

- **[payload](fields.md#payload)**: The payload of the coin.  *([Payload](schemata.md#payload))*
- **[signature](fields.md#signature)**: A signature within a certificate.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/coin_a0.json
:language: json
```

## RequestCDDSerial Message

### Fields

- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/request_cddc_serial.json
:language: json
```

## ResponseCDDSerial Message

- **[cdd_serial](fields.md#cdd_serial)**: The version of the CDD.  *(Int)*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Fields

### Example

```{literalinclude} artifacts/response_cddc_serial.json
:language: json
```

## RequestCDDC Message

- **[cdd_serial](fields.md#cdd_serial)**: The version of the CDD.  *(Int)*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Fields

### Example

```{literalinclude} artifacts/request_cddc.json
:language: json
```

## ResponseCDDC Message

### Fields

- **[cddc](fields.md#cddc)**: A full Currency Description Document Certificate.  *([CDDC](schemata.md#cddc))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/response_cddc.json
:language: json
```

## RequestMKCs Message

- **[denominations](fields.md#denominations)**: The list of possible denominations.  *(List of Int)*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[mint_key_ids](fields.md#mint_key_ids)**: What mint keys should be returned?  *(List of BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Fields

### Example

```{literalinclude} artifacts/request_mkc.json
:language: json
```

## ResponseMKCs Message

- **[keys](fields.md#keys)**: A list of Mint Key Certificates  *(List of [MKCs](schemata.md#mkc))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Fields

### Example

```{literalinclude} artifacts/response_mkc.json
:language: json
```

## RequestMint Message

### Fields

- **[blinds](fields.md#blinds)**: A List of Blinds  *(List of [Blinds](schemata.md#blind))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[transaction_reference](fields.md#transaction_reference)**: A random identifier that allows the client to resume a delayed mint/renew process.  *(BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/request_mint.json
:language: json
```

## ResponseMint Message

### Fields

- **[blind_signatures](fields.md#blind_signatures)**: A list of BlindSignatures.  *(List of [BlindSignatures](schemata.md#blindsignature))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/response_mint_a.json
:language: json
```

## CoinStack Message

### Fields

- **[coins](fields.md#coins)**: A list of coins.  *(List of [Coins](schemata.md#coin))*
- **[subject](fields.md#subject)**: A message that can be passed along with the coin stack.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/coinstack.json
:language: json
```

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

```{literalinclude} artifacts/request_renew.json
:language: json
```

## ResponseDelay Message

### Fields

- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/response_delay.json
:language: json
```

## RequestResume Message

### Fields

- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[transaction_reference](fields.md#transaction_reference)**: A random identifier that allows the client to resume a delayed mint/renew process.  *(BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/request_resume.json
:language: json
```

## RequestRedeem Message

### Fields

- **[coins](fields.md#coins)**: A list of coins.  *(List of [Coins](schemata.md#coin))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/request_redeem.json
:language: json
```

## ResponseRedeem Message

### Fields

- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/response_redeem.json
:language: json
```

[^partial]: GNU Taler experiments with this approach: in essence coins don't have serials but keys, which can sign a partial amount to be spent. This requires more smartness to avoid double spending, introducing new problems to be solved.
