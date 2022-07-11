# Field Reference

## Field Types

This lists all the fields used in the protocol. All:

- String: A JSON string.
- Integer: A JSON integer.
- BigInt: A JSON string containing a large number represented as the hex representation of it.
- DateTime: A JSON string containing the  ISO representation of a date.
- List: A JSON list that can contain all the possible field types mentioned here.
- URL: A JSON string containing the URL of a resource.
- WeightedURLList: A list of 2 element tuples \[Int, URL\].  Useful for round-robin, but also 
  reflects a preference. The lower the higher the priority.
- Schema / Object: A JSON object that conforms to the given schema.

All fields are mandatory, but can be empty in case of strings. 

## Fields

### additional_info
A field where the issuer can store additional information about the currency.

Type: String  
Used in: [CDDC](schemata.md#cddc)



### blind_signature
The signature on the blinded hash of a payload.

Type: BigInt  
Used in: [ResponseMint Message](schemata.md#responsemint-message)



### blind_signatures
A list of BlindSignatures.

Type: List of [BlindSignatures](schemata.md#blindsignature)  
Used in: [ResponseMint Message](schemata.md#responsemint-message)



### blinded_payload_hash
The blinded hash of a payload.

Type: BigInt  
Used in: [Blind](schemata.md#blind)



### blinds
A List of Blinds

Type: List of [Blinds](schemata.md#blind)  
Used in: [RequestMint Message](schemata.md#requestmint-message), [RequestRenew Message](schemata.md#requestrenew-message)



### cdd
Contains the Currency Description Document (CDD)

Type: [CDD](schemata.md#cdd)  
Used in: [CDDC](schemata.md#cddc)



### cdd_expiry_date
When does the CDD expire?

The cdd should not be used or validated after this date.

Type: String  
Used in: [CDDC](schemata.md#cddc)



### cdd_location
Hint to download the CDD if not available anyway. 

Useful for clients to “bootstrap” a yet unknown currency.

Type: URL  
Used in: [CDDC](schemata.md#cddc), [Payload](schemata.md#payload)



### cdd_serial
The version of the CDD.

Should be increased by 1 on a new version.

Type: Int  
Used in: [CDDC](schemata.md#cddc), [MKC](schemata.md#mkc), [RequestCDDC Message](schemata.md#requestcddc-message), [ResponseCDDSerial Message](schemata.md#responsecddserial-message)



### cdd_signing_date
When was the CDD signed?

Type: DateTime  
Used in: [CDDC](schemata.md#cddc)



### cddc
A full Currency Description Document Certificate.

Type: [CDDC](schemata.md#cddc)  
Used in: [ResponseCDDC Message](schemata.md#responsecddc-message)



### coins
A list of coins.

Type: List of [Coins](schemata.md#coin)  
Used in: [CoinStack Message](schemata.md#coinstack-message), [RequestRedeem Message](schemata.md#requestredeem-message), [RequestRenew Message](schemata.md#requestrenew-message)



### coins_expiry_date
Coins expire after this date. 

Do not use coins after this date. the coins before this date.

Type: DateTime  
Used in: [MKC](schemata.md#mkc)



### currency_divisor
Used to express the value in units of 'currency name'.

Example: a divisor of 100 can be used express cent values for EUR or USD.

Type: Int  
Used in: [CDDC](schemata.md#cddc)



### currency_name
The name of the currency, e.g. Dollar.

Use the name of the 'full' unit, and not its fraction, e.g. 'dollar' instead of 'cent',
and use the currency_divisor to express possible fractions.

Type: String  
Used in: [CDDC](schemata.md#cddc)



### denomination
The value of the coin(s).

Type: Int  
Used in: [MKC](schemata.md#mkc), [Payload](schemata.md#payload)



### denominations
The list of possible denominations.

Should be chosen wisely and listed in increasing value. 

Type: List of Int  
Used in: [CDDC](schemata.md#cddc), [RequestMKCs Message](schemata.md#requestmkcs-message)



### id
Identifier, a somewhat redundant hash of the [PublicKey](schemata.md#publickey)

This is just a visual helper, and MUST not be relied on. Calculate the hash
of the key in the client.

Type: BigInt  
Used in: [CDD](schemata.md#cdd), [CDDC](schemata.md#cddc), [MintKey](schemata.md#mintkey), [MKC](schemata.md#mkc)



### info_service
A list of locations where more information about the currency can be found.

This refers to human-readable information.

Type: WeightedURLList
Used in: [CDDC](schemata.md#cddc)



### issuer_cipher_suite
Identifier of the cipher suite that is used.

The format is: HASH-SIGN-BLINDING, e.g. SHA512-RSA-CHAUM83

Type: String  
Used in: [CDDC](schemata.md#cddc)



### issuer_id
Id (hash) of the issuer public master key in the CDDC

Type: BigInt  
Used in: [MKC](schemata.md#mkc), [Payload](schemata.md#payload)



### issuer_public_master_key
The hash of the issuer's public key

The only valid identifier of a currency is the master key. 

Type: [PublicKey](schemata.md#publickey)  
Used in: [CDDC](schemata.md#cddc)



### keys
A list of Mint Key Certificates

Type: List of [MKCs](schemata.md#mkc)  
Used in: [ResponseMKCs Message](schemata.md#responsemkcs-message)



### message_reference
Client internal message reference

Set by the client, echoed by the issuer.

Type: Integer  
Used in: [RequestCDDSerial Message](schemata.md#requestcddserial-message), [RequestCDDC Message](schemata.md#requestcddc-message), [RequestMint Message](schemata.md#requestmint-message), [RequestMKCs Message](schemata.md#requestmkcs-message), [RequestRedeem Message](schemata.md#requestredeem-message), [RequestRenew Message](schemata.md#requestrenew-message), [RequestResume Message](schemata.md#requestresume-message), [ResponseCDDSerial Message](schemata.md#responsecddserial-message), [ResponseCDDC Message](schemata.md#responsecddc-message), [ResponseDelay Message](schemata.md#responsedelay-message), [ResponseMint Message](schemata.md#responsemint-message), [ResponseMKCs Message](schemata.md#responsemkcs-message), [ResponseRedeem Message](schemata.md#responseredeem-message)



### mint_key
The mint key that was signed in the certificate

Type: [MintKey](schemata.md#mintkey)  
Used in: [MKC](schemata.md#mkc)



### mint_key_id
Identifier of the mint key used.

Type: BigInt  
Used in: [Blind](schemata.md#blind), [Payload](schemata.md#payload)



### mint_key_ids
What mint keys should be returned?

If left emtpy, no filter is applied.

Type: List of BigInt  
Used in: [RequestMKCs Message](schemata.md#requestmkcs-message)



### mint_service
A list of locations where [Blinds](schemata.md#blind) can be minted into [Coins](schemata.md#coin)

Type: WeightedURLList  
Used in: [CDDC](schemata.md#cddc)



### modulus
The modulus of the public key

Type: BigInt  
Used in: [PublicKey](schemata.md#publickey)



### payload
The payload of the coin. 

Type: [Payload](schemata.md#payload)  
Used in: [Coin](schemata.md#coin)



### protocol_version
The protocol version that was used.

Type: Url  
Used in: [CDDC](schemata.md#cddc), [Payload](schemata.md#payload)



### public_exponent
The exponent of the public key.

Type: BigInt  
Used in: [PublicKey](schemata.md#publickey)



### public_mint_key
The public key of the mint key.

Type: [PublicKey](schemata.md#publickey)  
Used in: [MintKey](schemata.md#mintkey)



### redeem_service
A list of locations where [Coins](schemata.md#coin) can be redeemed.

Type: WeightedURLList   
Used in: [CDDC](schemata.md#cddc)



### reference
An identifier that connects [Blind](schemata.md#blind), [BlindSignature](schemata.md#blindsignature) and blinding secrets.

Set by the client, echoed by the server.

Type: String  
Used in: [ResponseMint Message](schemata.md#responsemint-message), [Blind](schemata.md#blind)



### renew_service
A list of locations where [Coins](schemata.md#coin) can be renewed.

Type: WeightedURLList  
Used in: [CDDC](schemata.md#cddc)



### serial
The serial of the [Coin](schemata.md#coin). 

This random value is generated by clients. It is used to identify coins and prevent double spending. 
Once the coin is spent, the serial will be stored by the issuer. Because of its sufficient long 
length it is supposed to be unique for each coin. A high entropy (crypto grade quality) is important.

Type: BigInt  
Used in: [Payload](schemata.md#payload)



### sign_coins_not_after
Use [MintKey](schemata.md#mintkey) only before this date.

Type: DateTime  
Used in: [MKC](schemata.md#mkc)



### sign_coins_not_before
Use [MintKey](schemata.md#mintkey) only after this date.

Type: String  
Used in: [MKC](schemata.md#mkc)



### signature
A signature within a certificate.

Type: String  
Used in: [CDDC](schemata.md#cddc), [Coin](schemata.md#coin), [MKC](schemata.md#mkc)



### status_code
The issuer can return a status code, like in HTTP
2XX SUCCESS
3XX DELAY / TEMPORARY ERROR
4XX PERMANENT ERROR

Type: Integer  
Used in: [ResponseCDDSerial Message](schemata.md#responsecddserial-message), [ResponseCDDC Message](schemata.md#responsecddc-message), [ResponseDelay Message](schemata.md#responsedelay-message), [ResponseMint Message](schemata.md#responsemint-message), [ResponseMKCs Message](schemata.md#responsemkcs-message), [ResponseRedeem Message](schemata.md#responseredeem-message)



### status_description
Description that the issuer passes along with the status_code.

Type: String  
Used in: [ResponseCDDSerial Message](schemata.md#responsecddserial-message), [ResponseCDDC Message](schemata.md#responsecddc-message), [ResponseDelay Message](schemata.md#responsedelay-message), [ResponseMint Message](schemata.md#responsemint-message), [ResponseMKCs Message](schemata.md#responsemkcs-message), [ResponseRedeem Message](schemata.md#responseredeem-message)



### subject
A message that can be passed along with the coin stack.

Can be left empty. Used informally to indicate a reason for payment etc.

Type: String  
Used in: [CoinStack Message](schemata.md#coinstack-message)



### transaction_reference
A random identifier that allows the client to resume a delayed mint/renew process. 

This should be a good random number.

Type: BigInt  
Used in: [RequestMint Message](schemata.md#requestmint-message), [RequestRenew Message](schemata.md#requestrenew-message), [RequestResume Message](schemata.md#requestresume-message)



### type
String identifying the type of message.

This is the id that is used for parsing the message.
One of:

- blinded payload hash
- blind signature
- cdd
- cdd certificate
- coin
- coinstack
- mint key certificate
- mint key
- payload
- rsa public key
- request cddc
- request cdd serial
- request mint key certificates
- request mint
- request redeem
- request renew
- request resume
- response cddc
- response cdd serial
- response delay
- response mint key certificates
- response mint
- response redeem

Type: String  
Used in: [ResponseMint Message](schemata.md#responsemint-message), [Blind](schemata.md#blind), [CDDC](schemata.md#cddc), [CDDC](schemata.md#cddc), [Coin](schemata.md#coin), [CoinStack Message](schemata.md#coinstack-message), [MKC](schemata.md#mkc), [MKC](schemata.md#mkc), [Payload](schemata.md#payload), [RequestCDDSerial Message](schemata.md#requestcddserial-message), [RequestCDDC Message](schemata.md#requestcddc-message), [RequestMint Message](schemata.md#requestmint-message), [RequestMKCs Message](schemata.md#requestmkcs-message), [RequestRedeem Message](schemata.md#requestredeem-message), [RequestRenew Message](schemata.md#requestrenew-message), [RequestResume Message](schemata.md#requestresume-message), [ResponseCDDSerial Message](schemata.md#responsecddserial-message), [ResponseCDDC Message](schemata.md#responsecddc-message), [ResponseDelay Message](schemata.md#responsedelay-message), [ResponseMint Message](schemata.md#responsemint-message), [ResponseMKCs Message](schemata.md#responsemkcs-message), [ResponseRedeem Message](schemata.md#responseredeem-message), [PublicKey](schemata.md#publickey)


