# Overview

We propose a protocol that allows cash-like payments in the electronic world. It is based on the invention by David Chaum[^chaum82]. This means that we define message structures around blind signatures, that focus on *untraceable* payments. 'Untracable' because even though there is a central entity (called the issuer, something like a bank), this central entity can't see the transactions happening. 

The focus of the project is the protocol. This means we standardize the way we exchange messages and their content in order to make electronic cash payments. But we don't deliver an implementation here. That is the scope of other project(s). OpenCoin is the foundation to build upon.

## What can I do with it?

The most common use case is "electronic cash", that is an electronic currency that allows fast untraceable transactions and
is convertible to a "real" currency. But other uses can be imagined as well: a [time bank](https://en.wikipedia.org/wiki/Time-based_currency), [carbon based emission tokens](https://en.wikipedia.org/wiki/Emissions_trading), or electronic voting, to name a few. Everybody can run an issuer and can set their own rules[^law1]

## How does it work?

:::{figure-md} overview-diagram
:class: figure

<img src="overview.*" alt="Overview diagram" class="bg-primary" width="300px">

Simplified overview of the OpenCoin flow.
:::

[The simplified overview](overview-diagram) show a high level description of the basic system. We have three participants: Alice and Bob are normal users, while the Issuer is something like a bank, capable of minting coins. It also acts as an exchange for 'real-world' currency. At this high level it works as follows:

1. Alice asks the Issuer to **mint** coins. This is done in a special way using *blind signatures*, which means that the coins *can't be linked to her* later on.

2. Alice then **transfers** the coins to Bob. She can do the transfer any way she wants, e.g. using a messenger like Signal, Email or any other system of her choice (also depending on what her client software supports). This could even be done by printing the coins and handing them over.

3. Bob then **renews** the coins. He swaps the coins he got from Alice for fresh coins at the Issuer. This way he protects himself against Alice "accidentally"  using the coins somewhere else. The Issuer marks used coins in its database. This way one can spend opencoins only once, and *double spending* is ruled out.

4. Bob might **transfer** the coins to yet another person, Charlene.

5. Charlene decides to **redeem** the coins, meaning she asks the issuer to convert the opencoins for real-world money.

On **blind signatures**: at the core of a coin is a serial number with a signature from the mint. In order to ensure that *a coin can't be traced back to the original client* we use blind signatures:

Imagine Alice wants to give Bob a coin that the issuer can't trace. In order to ensure the coin can't be traced back to Alice, the issuer needs to sign the serial number without seeing it. In non-technical terms Alice puts the serial number in an envelope (along with carbon copy paper), and the issuer actually signs the envelope. Because of the carbon copy paper the signature presses through onto the serial number. Alice can then open up the envelope and has a signed serial, without the issuer ever seeing it.

## Who is it for?

OpenCoin (the protocol) allows the development of applications for electronic cash. So firstly OpenCoin is targeted at developers. These applications in return should allow everyone to make and receive electronic payments. It still requires somebody to run the central issuer. This issuer would run an OpenCoin based electronic money system. Because electronic money is quite regulated in Europe (and other countries), the issuer would be most likely a regulated electronic money provider or a bank. We think, that a central bank would be the best issuer, because central banks issue money anyhow. But nothing technical stops you from using OpenCoin for your private project [^law2].

## Alternatives

Why don't just use one of the alternatives?

### Bitcoin / blockchain

Bitcoin (or blockchain in the more general form) is basically the opposite of OpenCoin: transfers have to happen within the system, they are visible to everybody, there is no central instance, there is no guaranteed value you can redeem the bitcoins for.

OpenCoin on the contrary makes the transfers invisible and untraceable, and has a central instance that is able to guarantee a value if you redeem the OpenCoin.

Also, Bitcoin is environmentally insane.

### GNU Taler

[GNU Taler](https://taler.net) is build around the same central idea as OpenCoin. It started later, and is more complete than OpenCoin. GNU Taler differs in the way the system takes care of the [renewal step](schemata.md#requestrenew-message) and it introduces coin splitting. It also makes more assumptions regarding the clients, the clients have defined roles (e.g. consumer and merchant). GNU Taler is also much more a finished product than OpenCoin.

OpenCoin is a protocol, a shared ground to build multiple implementations upon. 

We also think that some issues (like tax-ability) could be solved to some extent within OpenCoin, but are [better solved outside the transfer system anyhow](faq.md#what-about-taxation). 


[^chaum82]: David Chaum, “Blind signatures for untraceable payments”, Advances in Cryptology - Crypto ‘82, Springer-Verlag (1983), 199-203.

[^law1]: Please check with your lawyer if this is a good idea.
[^law2]: Again, please check with your lawyer if this is a good idea.
