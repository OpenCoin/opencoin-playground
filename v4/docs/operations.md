# Operations

## Tokenizing

When preparing blanks we need to decide which values to use. The overall goal is to get the wallet into a state
where the next transaction can be made without having to fetch "change" first. E.g. if we have a sum of 200 in the
wallet, we want to pay 137 without having to do anything first.

This makes live more comfortable, but more important it helps privacy, because the issuer can't link actions around
an awkward price.

We have a [sample implementation](../coinsplitting.py) for this. It contains one line of old 
[black magic](https://en.wikipedia.org/wiki/Magic_(programming)#Variants), but we have [tests](../test_coinsplitting.py) for it.

Also see [](schemata.md#requestrenew-message).

## Cryptographic operations

TBD

- hashes
- signatures
- blinding and unblinding

