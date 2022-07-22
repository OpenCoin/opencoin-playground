# Operations

## Cipher suites

We define cipher suites that need to be supported by implementations.

### INSECURE-RSA256-SHA1-CHAUM86

```{warning}
This suite is insecure, and MUST not be used in production
```

The purpose of this cipher suite is documentation only: we want to keep the numbers relatively short to not distract
from the actual fields in the schemata.

So, don't ever use this suite for anything other than documentation.


## Tokenizing

When preparing blanks we need to decide which values to use. The overall goal is to get the 
wallet into a state where the next transaction can be made without having to fetch "change" first. E.g. if we have a sum of 200 in the wallet, we want to pay 137 without having to do anything first.

This makes live more comfortable, but more important it helps privacy, because the issuer can't link actions around an awkward price.

We have a [sample implementation](../coinsplitting.py) for this. It contains one line of old
[black magic](https://en.wikipedia.org/wiki/Magic_(programming)#Variants), but we have [tests](../test_coinsplitting.py)
for it.

Also see [](schemata.md#requestrenew-message).
