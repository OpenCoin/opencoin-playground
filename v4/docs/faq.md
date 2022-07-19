# FAQ

## Can OpenCoin be abused for \[whatever crime\]?

People ask if untraceable transactions (like OpenCoin allows) be abused for crimes of all kinds. The short answer: yes, but...

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

We think that this risk is quite real. The question is however if tracing money transactions is the (one) way to stop the crime. Tracing transactions has a huge impact on the privacy of innocent people. So it is a tradeoff. How has society decided for other fields? E.g. streets, the postal service, knives and the internet can be abused as well, and generally speaking, societies don't trace buying or using those things. Some would even say that one of the main uses of the [500 EUR banknote is dubious or illegal activity](https://en.wikipedia.org/wiki/500_euro_note#Crime), and it still exists.

Our point is that yes, untraceable payments can be used for crimes, but so can other services as well, and it is up for society to decide how to handle it.

## What about taxation?

One could ask if untraceable payments can be used to avoid taxation, or the other way around: should a mechanism be built into a transaction schema to enforce taxation [^taler]. 
[^taler]: see the section on GNU Taler in the [overview](overview.md#gnu-taler).

If one wanted to help the tax office here, one could think about requiring authorization for renewing coins as well as for minting and redeeming them. By this all points of contact with the issuer could be traced, and one could at least the amount of coins flowing through a wallet. It would be up for legislation to decide what actions (mint, renew, redeem) to tax in what way.

We find however that in the "real world" taxation is enforced using a different mechanism: receipts. Warranty and the ability to deduct costs for tax purposes is bound to have proper receipts. So the recipient is forced py the payer to produce a receipt, and make the transaction official. This seems to work quite fine, and handles electronic payments as well as cash payments. We think that this is the right place to handle these issues.

## Can I legally use OpenCoin for xyz?

You have to talk with your lawyer to check the current situation for country and purpose. The old [legal report](reviews.md#legal-review) can be a starting point. 

## Why do you use old approaches (RSA, unmodified chaumian blinding) instead of the hip new XYZ?

We want to keep things simple, and want to avoid complexity. The protocol should be fairly easy
to implement and review.[^grug]

Given the current amount of computing power and bandwidth available, we find that the savings on speed and space
that newer systems like elliptic curves don't set of the price in increased complexity. 

The same holds true for the additions that could be made around blinding, partial spending coins etc. 


[^grug]: See "The Grug Brained Developer": https://grugbrain.dev/