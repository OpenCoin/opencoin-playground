# Operations

## Cipher suites

We define cipher suites that need to be supported by implementations.

### RSA-SHA256-PSS-CHAUM82

This suite uses RSA for the crypto operations. SHA256 is used as a hashing
algorithm, and PSS for padding in certificate signatures.

CHAUM82 is used for the blinding, e.g. raw RSA  signatures.

The signing process is initialized following the [cryptography.io example](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#signing):

```python
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

private_key = rsa.generate_private_key(65537, 512)
signature = private_key.sign(
    "The json dump",
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
```
See the [documentation code](../rsa_suite.py) 

## Tokenizing

When preparing blanks we need to decide which values to use. The overall goal is to get the 
wallet into a state where the next transaction can be made without having to fetch "change" first. E.g. if we have a sum of 200 in the wallet, we want to pay 137 without having to do anything first.

This makes live more comfortable, but more important it helps privacy, because the issuer can't link actions around an awkward price.

We have a [sample implementation](../coinsplitting.py) for this. It contains one line of old
[black magic](https://en.wikipedia.org/wiki/Magic_(programming)#Variants), but we have [tests](../test_coinsplitting.py)
for it.

Also see [](schemata.md#requestrenew-message).
