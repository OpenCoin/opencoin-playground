# FAQ

## Can OpenCoin be abused for \[whatever crime\]?

People ask if untraceable transactions (like OpenCoin allows) be abused for crimes of all kinds.

```{figure} images/terror3.jpg
---
width: 60%
figclass: margin
alt: Anti piracy poster, seen in a bus station in Islington
---
Copying DVDs also finances evil crimes  
*Found in a bus stop in Islington*
```

The usual candidates for crimes are terror financing, child pornography, money laundering, blackmail etc. These are all evil crimes, without doubt. Untraceable transactions would facilitate these crimes because a payment could be made to an unknown wallet/client, which would renew those coins, and later on distribute the coins to other wallets, which would then convert the coins to "real money".

We think that this risk is quite real. However, the question is if tracing money transactions is the (one) way to stop the crime. Tracing transactions has a huge impact on the privacy of innocent people. So there is a tradeoff. How has society decided for other fields? E.g. streets, the postal service, knives and the internet can be abused as well, but generally speaking, societies don't trace buying or using those things. Some would even say that one of the main uses of the [500 EUR banknote is dubious or illegal activity](https://en.wikipedia.org/wiki/500_euro_note#Crime), and it still exists.

Our point is that yes, untraceable payments can be used for crimes, but so can other services as well, and it is up for society to decide how to handle it.

## What about taxation?

One could ask if untraceable payments can be used to avoid taxation, or the other way around: should a mechanism be built into a transaction schema to enforce taxation [^taler]. 

[^taler]: see the section on GNU Taler in the [overview](overview.md#gnu-taler).

First: we support taxes, they are needed for a society to work.

If one wanted to help the tax office here, one could think about requiring authorization for renewing coins as well as for minting and redeeming them. By this all points of contact with the issuer could be traced, and one could at least follow the amount of coins flowing through a wallet. It would be up for legislation to decide what actions (mint, renew, redeem) to tax in what way.

We find however that in the "real world" taxation is enforced using a different mechanism: receipts. Warranty and the ability of the customer to deduct costs for tax purposes is bound to having proper receipts. So the recipient is forced py the payer to produce a receipt, and make the transaction official. This seems to work quite fine, and is suitable for electronic payments as well as cash payments. We think that this is the right place to handle these issues.

## Can I legally use OpenCoin for xyz?

You have to talk with your lawyer to check the current situation for country and purpose. The old [legal report](reviews.md#legal-review) can be a starting point.

## Can OpenCoin be used offline?

When receiving a coin, the coin needs to be [renewed](OpenCoin.md#requestrenew). This is needed to prevent the sender from double spending the coin. To reach the issuer you will most likely to be online. However, if you trust the center, you could delay the renewal operation as long as you like. The magic of trust...

## OpenCoin and ripple?

The OpenCoin project that started in 2007 to create an open source protocol for the electronic cash system invented by David Chaum. It is about minting tokens that can be transferred in a non-traceable way. It is fast, and the user has full flexibility on how to do the transfer.

It had nothing to do with "OpenCoin Inc.", a younger company that was developing the ripple network. Unfortunately they decided in 2012 to name their company the same as our project. That created a bit of confusion, as both are about electronic transfers.

The name of the company than changed to [ripplelabs](https://ripplelabs.com/), and they gave the domain name back to us, the OpenCoin project. For free. How cool is that?
