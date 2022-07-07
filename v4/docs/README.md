# OpenCoin

*a protocol for privacy preserving electronic cash payments*

### Table of contents
[toc]





## Intro

We describe a protocol that allows cash-like payments in the electronic world. It is based on the invention by David Chaum[^1]. The main focus are *untraceable* payments, which means that even though there is a central entity (called the issuer, something like a bank), this central entity can't see the transactions happening. This is good for the privacy of the users.

The focus of the project is the protocol. This means we standardize the way we exchange messages and their content in order to make electronic cash payments. But we don't deliver an implementation. That is the scope of other project(s). OpenCoin is the foundation to build upon.

### How does it work?

![overview](overview.svg)

This is a high level (and somewhat wrong) image describing the basic system. We have three participants: Alice and Bob are normal users, while the Issuer is something like a bank, capable of minting coins. It also acts as an exchange for 'real-world' currency. At this high level it works as follows:

1. Alice asks the Issuer to **mint** coins. This is done in a special way using *blind signatures*, which means that the coins *can't be linked to her* later on.
2. Alice then **transfers** the coins to Bob. She can do that any way she wants, e.g. using WhatsApp, Email or any other system of her choice (also depending on what her client software supports). This could even be done by printing the coins and handing them over.
3. Bob then **renews** the coins. He swaps the coins he got from Alice for fresh coins. This way he protects himself against Alice "accidentally"  using the coins somewhere else. One can spend opencoins only once, so *double spending* needs to be ruled out.
4. Bob might **transfer** the coins to yet another person, Charlene
5. Charlene decides to **redeem** the coins, meaning she asks the issuer to swap the opencoins for real-world money.

So much for now. We go into the details later on. What you should remember though is that Alice's privacy is protected because *coins can't be linked to her* (because of the *blind signatures*).

### Who is it for?

OpenCoin (the protocol) allows the development of applications for electronic cash. So firstly OpenCoin is targeted at developers. These applications however should allow everyone to make and receive electronic payments. It still requires somebody to run the central issuer. This issuer would issue an OpenCoin based electronic money system. Because electronic money is quite regulated in Europe (and other countries), the issuer would be most likely a regulated electronic money provider or a bank. We think, that a central bank would be the best issuer, because central banks issue money anyhow. But nothing technical stops you from using OpenCoin for your private project [^2].

### Alternatives

Why don't just use one of the alternatives? 

#### Bitcoin / blockchain

Bitcoin (or blockchain in the more general form) is basically the opposite of OpenCoin: transfers have to happen within the system, they are visible to everybody, there is no central instance, there is no guaranteed value you can redeem the bitcoins for.  

OpenCoin on the contrary makes the transfers invisible and untraceable, and has a central instance that is able to guarantee a value if you redeem the OpenCoin. 

One could say that bitcoin behaves more like gold, while OpenCoin behaves more like cash. 

#### GNU Taler

[GNU Taler](taler.net) is build around the same central idea as OpenCoin. It started later, and is more complete than OpenCoin. They differ in the way the take care of the [renewal step](#5. renew). They also make more assumptions regarding the clients (e.g. clients having key identifying them), they have clearer roles (e.g. consumer and merchant) and by all of this hope to get around the inherent problems of untracable transfers, e.g. taxability. 

The trade-off seems to be that their system is harder is more complex and harder to understand. We also doubt that this complexities are necessary to reach the stated goals. We also doubt that the goals can really be reached, and also find that the systems documentation is quite hard to understand. This might be because they deliver implementations for all necessary software components, and are not really targeted at other implementations of they system. 

Because of all this one could say that GNU Taler is less open to other developers.

### Scope

Having said all of the above, we scope the protocol and it's description in the following way:

**Targeted at developers** - developers should be enabled (and motivated) by the OpenCoin protocol to implement standard confirming software components and apps. However we hope that this documentation is also understandable for the interested user (or founder, investor, auditor, etc.)

**Just the protocol** - we don't deliver any ready to use implementations. This allows us to fully focus on the protocol, and keeps a separation to actual implementations.

**Easy to understand** - we try to avoid complexity. This affects the protocol itself as well as it's documentation. This means: if you, the reader, don't understand a sentence or a concept, please contact us. We will improve the description. Being easy to understand is one of the main goals of OpenCoin.

**Only the core** - lots of developments have happened since [we started](#history). Take the example of messangers like Signal, Telegram or WhatsApp. The have opened new ways to transport messages, and they take care of identifying the communication partner. This especially means that message transport and authentication stays out of scope.

## History


## Overview

### Assumptions

- Transport Layer Security
- Authentication

### Sequence

![sequence](sequence.svg)

## Message Flow Details

### 1. CDDSerial

### 2. CDDC

### 3. MKCs

### 4. Mint

### Transfer

### 5. Renew

### 6. Resume

### 7. Redeem

## Reference



## Appendix

### JSON Schemata



## Footnotes

[^1]: David Chaum, “Blind signatures for untraceable payments”, Advances in Cryptology - Crypto ‘82, Springer-Verlag (1983), 199-203. 
[^2]: Please check with your lawyer if this is a good idea.



