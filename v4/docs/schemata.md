# Schemata

In here we present the actual schemata for the all the messages that we send and receive in the OpenCoin
protocol. Each schema contains a description, a list of its fields and an example. The field names are
linked to the [fields page](fields.md), where you can more detailed information about the fields.

```{note}
The examples are produced by the [run_protocol](../run_protocol.py) script. You can get similar values
if you set `random.seed(1)` at the beginning of the file
```

## CDD

The Currency Description Document holds all information about a currency that is following the OpenCoin protocol. 

It contains the master key, the denominations, the services, the name of the currency and more. 

Always part of a [CDDC](#cddc)

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

```{literalinclude} artifacts/cdd_short.json
:language: json
```
Complete example: [cdd.json](artifacts/cdd.json)

#### Secret key

To make this documentation completely reproducible, here is the data for the secret issuer key:

```{literalinclude} artifacts/issuer_secret_short.json
:language: json
```
Complete example: [issuer_secret.json](artifacts/issuer_secret.json)

```{warning}
Don't ever publish your secret keys!
```

## CDDC

The certificate for the [CDD](#cdd), signed with the secret master key. This is the "trust anchor". 

### Fields

- **[cdd](fields.md#cdd)**: Contains the Currency Description Document (CDD)  *([CDD](schemata.md#cdd))*
- **[signature](fields.md#signature)**: A signature within a certificate.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/cddc_short.json
:language: json
```
Complete example: [cddc.json](artifacts/cddc.json)


## PublicKey

Schema to hold public keys. We have decided for our own format because we want to keep things simple. Using a 
predefined format would probably lead to use bigger libraries when implementing the protocol.

Always part of a [CDD](#cdd) or [MKC](#mkc).

### Fields

- **[modulus](fields.md#modulus)**: The modulus of the public key  *(BigInt)*
- **[public_exponent](fields.md#public_exponent)**: The exponent of the public key.  *(BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/issuer_public_master_key_short.json
:language: json
```
Complete example: [issuer_public_master_key.json](artifacts/issuer_public_master_key.json)

## MintKey

This describes a key that is used to sign/mint coins for a single denomination. As the key doesn't 
see the content it is signing (it is blinded, after all), we need to bind the key to the meaning of
its signature: "this signature is worth *n* units of value". 

The key will be used for a period of time, after which it is going to be swapped for a new one. The 
coins will be valid a bit longer then the signing time of the key.

```{warning}

**Never** use the mint key for encryption, **only** for signing!

```

Always part of a [MKC](#mkc)

### Fields

- **[cdd_serial](fields.md#cdd_serial)**: The version of the CDD.  *(Int)*
- **[coins_expiry_date](fields.md#coins_expiry_date)**: Coins expire after this date.  *(DateTime)*
- **[denomination](fields.md#denomination)**: The value of the coin(s).  *(Int)*
- **[id](fields.md#id)**: Identifier, a somewhat redundant hash of the [PublicKey](schemata.md#publickey)  *(BigInt)*
- **[issuer_id](fields.md#issuer_id)**: The identifier (hash) of the issuer public master key in the CDDC  *(BigInt)*
- **[public_mint_key](fields.md#public_mint_key)**: The public key of the mint key.  *([PublicKey](schemata.md#publickey))*
- **[sign_coins_not_after](fields.md#sign_coins_not_after)**: Use [MintKey](schemata.md#mintkey) only before this date.  *(DateTime)*
- **[sign_coins_not_before](fields.md#sign_coins_not_before)**: Use [MintKey](schemata.md#mintkey) only after this date.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/mintkey_1_short.json
:language: json
```
Complete example: [mintkey_1.json](artifacts/mintkey_1.json)

#### Secret key

To make this documentation completely reproducible, here is the data for the secret mint key for the value 1:

```{literalinclude} artifacts/mintkey_1_secret_short.json
:language: json
```
Complete example: [mintkey_1_secret.json](artifacts/mintkey_1_secret.json)

```{warning}
Don't ever publish your secret keys!
```


## MKC

A *Mint Key Certificate* for the [MKC](#mkc). Signed with the secret master key in the [CDD](#cdd).  


### Fields

- **[mint_key](fields.md#mint_key)**: The mint key that was signed in the certificate  *([MintKey](schemata.md#mintkey))*
- **[signature](fields.md#signature)**: A signature within a certificate.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/mkc_1_short.json
:language: json
```
Complete example: [mkc_1.json](artifacts/mkc_1.json)

## Payload

These are the "innards" of [Coin](#coin). The mint key id is a helper so that the corresponding key for the signature of the coin can be found faster. The same is true for the denomination - an implementation should take the coins value from the [MintKey](#mintkey), because the values in the can't be trusted.

### Fields

- **[cdd_location](fields.md#cdd_location)**: Hint to download the CDD if not available anyway.  *(URL)*
- **[denomination](fields.md#denomination)**: The value of the coin(s).  *(Int)*
- **[issuer_id](fields.md#issuer_id)**: The identifier (hash) of the issuer public master key in the CDDC  *(BigInt)*
- **[mint_key_id](fields.md#mint_key_id)**: Identifier of the mint key used.  *(BigInt)*
- **[protocol_version](fields.md#protocol_version)**: The protocol version that was used.  *(Url)*
- **[serial](fields.md#serial)**: The serial of the [Coin](schemata.md#coin).  *(BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/payload_a0_short.json
:language: json
```
Complete example: [payload_a0.json](artifacts/payload_a0.json)

## Blind

Contains the blinded hash for a [Payload](#payload), and says which mint key to use. The reference is needed
to connect signatures to blinds later on (we don't want to rely on list orders). 

### Fields

- **[blinded_payload_hash](fields.md#blinded_payload_hash)**: The blinded hash of a payload.  *(BigInt)*
- **[mint_key_id](fields.md#mint_key_id)**: Identifier of the mint key used.  *(BigInt)*
- **[reference](fields.md#reference)**: An identifier that connects [Blind](schemata.md#blind), [BlindSignature](schemata.md#blindsignature) and blinding secrets.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/blind_a0_short.json
:language: json
```
Complete example: [blind_a0.json](artifacts/blind_a0.json)

## BlindSignature

The signature for a blind. The blind is specified with the reference. 

### Fields

- **[blind_signature](fields.md#blind_signature)**: The signature on the blinded hash of a payload.  *(BigInt)*
- **[reference](fields.md#reference)**: An identifier that connects [Blind](schemata.md#blind), [BlindSignature](schemata.md#blindsignature) and blinding secrets.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/blind_signature_a0_short.json
:language: json
```
Complete example: [blind_signature_a0.json](artifacts/blind_signature_a0.json)

## Coin

The certificate for a payload. The signature is the unblinded [BlindSignature](#blindsignature). 

### Fields

- **[payload](fields.md#payload)**: The payload of the coin.  *([Payload](schemata.md#payload))*
- **[signature](fields.md#signature)**: A signature within a certificate.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/coin_a0_short.json
:language: json
```
Complete example: [coin_a0.json](artifacts/coin_a0.json)

## RequestCDDSerial Message

This message asks for the cdd_serial of the current [CDDC](#cddc).

### Fields

- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/request_cddc_serial_short.json
:language: json
```
Complete example: [request_cddc_serial.json](artifacts/request_cddc_serial.json)

## ResponseCDDSerial Message

Returns the current cdd_serial. 

### Fields

- **[cdd_serial](fields.md#cdd_serial)**: The version of the CDD.  *(Int)*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/response_cddc_serial_short.json
:language: json
```
Complete example: [response_cddc_serial.json](artifacts/response_cddc_serial.json)

## RequestCDDC Message

This requests the [CDDC](#cddc) specified by the cdd_serial. If cdd_serial is set to 0, the most current CDDC is returned.

### Fields

- **[cdd_serial](fields.md#cdd_serial)**: The version of the CDD.  *(Int)*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/request_cddc_short.json
:language: json
```
Complete example: [request_cddc.json](artifacts/request_cddc.json)

## ResponseCDDC Message

This response carries the [CDDC](#cddc).

### Fields

- **[cddc](fields.md#cddc)**: A full Currency Description Document Certificate.  *([CDDC](schemata.md#cddc))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/response_cddc_short.json
:language: json
```
Complete example: [response_cddc.json](artifacts/response_cddc.json)

## RequestMKCs Message

This requests one or more [MKCs](#mkc). The fields *denominations* and *mint_key_ids* specify which MKCs should be delivered. Denominations refer to the most current key(s) for the given denominations. If both fields are empty, all most current MKCs are delivered - we assume that is the normal use case.

### Fields

- **[denominations](fields.md#denominations)**: The list of possible denominations.  *(List of Int)*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[mint_key_ids](fields.md#mint_key_ids)**: What mint keys should be returned?  *(List of BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/request_mkc_short.json
:language: json
```
Complete example: [request_mkc.json](artifacts/request_mkc.json)

## ResponseMKCs Message

This delivers the [MKCs] as specified in the [RequestMKCs](#requestmkcs-message).

### Fields

- **[keys](fields.md#keys)**: A list of Mint Key Certificates  *(List of [MKCs](schemata.md#mkc))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/response_mkc_short.json
:language: json
```
Complete example: [response_mkc.json](artifacts/response_mkc.json)

## RequestMint Message

Request blinds to be signed. The [Blinds](#blind) hold the information which mint keys are to be used.

The client asking for this action should be authenticated, and the issuer should check if the client meets the requirements of the request, a.k.a. has enough funds to pay for the minting process.

### Fields

- **[blinds](fields.md#blinds)**: A List of Blinds  *(List of [Blinds](schemata.md#blind))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[transaction_reference](fields.md#transaction_reference)**: A random identifier that allows the client to resume a delayed mint/renew process.  *(BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/request_mint_short.json
:language: json
```
Complete example: [request_mint.json](artifacts/request_mint.json)

## ResponseMint Message

This delivers the [BlindSignatures](#blindsignature). The client is to unblind the blind signatures to derive the signature for the [Coins](#coin).

### Fields

- **[blind_signatures](fields.md#blind_signatures)**: A list of BlindSignatures.  *(List of [BlindSignatures](schemata.md#blindsignature))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/response_mint_a_short.json
:language: json
```
Complete example: [response_mint_a.json](artifacts/response_mint_a.json)

## CoinStack Message

This holds a set of coins. It is not a message in the strict sense, but a container. Transferring the CoinStack in a manner that is untraceable by the issuer is key to protecting the privacy. How this is achieved is outside the protocol, and left as an exercise to the implementer :-)

### Fields

- **[coins](fields.md#coins)**: A list of coins.  *(List of [Coins](schemata.md#coin))*
- **[subject](fields.md#subject)**: A message that can be passed along with the coin stack.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/coinstack_short.json
:language: json
```
Complete example: [coinstack.json](artifacts/coinstack.json)

## RequestRenew Message

Coins that are received need to be swapped for new ones, in order to protect the receiver against double spending. Otherwise, the sender could keep a copy of the coins and try to use the coins again. Before doing so we need to ask: what coin sizes should be chosen for the coins to be minted?

What if we have not the right coin selection for an amount to pay?  Imagine that the price is 5 opencent, but we just have coins in the sizes: 2, 2, 2.

One solution would be to require the recipient to give change. This would make the protocol more complicated, and would just shift the problem to the recipient. Another approach is to allow partial spending coins, but this again makes the protocol more complicated.[^partial]

The easy way out is to aim for a selection of coins that allows us to pay *any* amount below or equal to the sum of all coins. E.g. if we own the value of 6 opencent it would be advisable to have coin selection 2,2,1,1 in order to pay all possible amounts. This also prevents *amount tracing*, where an awkward price (13.37) asks for an awkward coin exchange at the issuer beforehand.

So, we need to look at the combined sum of coins received and coins already in possession, and needs to find the right coin selection to be able to make all possible future coin transfers. We will then know which coins to keep, and what blinds to make and paying for the minting using *all* the just received coins and using *some* existing coins.

Also see [](operations.md#tokenizing) for a sample implementation.

### Fields

- **[blinds](fields.md#blinds)**: A List of Blinds  *(List of [Blinds](schemata.md#blind))*
- **[coins](fields.md#coins)**: A list of coins.  *(List of [Coins](schemata.md#coin))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[transaction_reference](fields.md#transaction_reference)**: A random identifier that allows the client to resume a delayed mint/renew process.  *(BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/request_renew_short.json
:language: json
```
Complete example: [request_renew.json](artifacts/request_renew.json)

## ResponseDelay Message

This message is used by the issuer to signal a delay in minting or renewing coins. It is best of course to be fast and reliable enough to never use this message.

### Fields

- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/response_delay_short.json
:language: json
```
Complete example: [response_delay.json](artifacts/response_delay.json)

## RequestResume Message

This message request that an action that was delayed before with a [ResponseDelay](#responsedelay-message) is to be resumed. Either a [ResponseMint](#responsemint-message) is returned, or another ResponseDelay if the client is unlucky. 

### Fields

- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[transaction_reference](fields.md#transaction_reference)**: A random identifier that allows the client to resume a delayed mint/renew process.  *(BigInt)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/request_resume_short.json
:language: json
```
Complete example: [request_resume.json](artifacts/request_resume.json)

## RequestRedeem Message

This message aks for coins to be redeemed, e.g. exchanged for real-world money. 

The client needs to be authenticated for this request (outside this protocol), so that the issuer knows who to credit the value of the coins to.

### Fields

- **[coins](fields.md#coins)**: A list of coins.  *(List of [Coins](schemata.md#coin))*
- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/request_redeem_short.json
:language: json
```
Complete example: [request_redeem.json](artifacts/request_redeem.json)

## ResponseRedeem Message

This just answers to a [RequestRedeem](#requestredeem-message), and doesn't hold other meaningful information.

### Fields

- **[message_reference](fields.md#message_reference)**: Client internal message reference  *(Integer)*
- **[status_code](fields.md#status_code)**: The issuer can return a status code, like in HTTP  *(Integer)*
- **[status_description](fields.md#status_description)**: Description that the issuer passes along with the status_code.  *(String)*
- **[type](fields.md#type)**: String identifying the type of message.  *(String)*

### Example

```{literalinclude} artifacts/response_redeem_short.json
:language: json
```
Complete example: [response_redeem.json](artifacts/response_redeem.json)

[^partial]: GNU Taler experiments with this approach: in essence coins don't have serials but keys, which can sign a partial amount to be spent. This requires more smartness to avoid double spending, introducing new problems to be solved.
