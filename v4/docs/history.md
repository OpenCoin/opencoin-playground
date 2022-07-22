# History

## v0.1

We created the [initial version of the protocol](https://github.com/OpenCoin/opencoin-historic/blob/master/standards/protocol.txt). 

On top of it we built a [proof of concept](https://github.com/OpenCoin/opencoin-historic/tree/master/pyopencoin) (PoC) to show that the whole system actually works. The PoC worked, but would be implemented differently today.

The protocol however stayed more or less the same compared with today's version. 

### GUI designs

Some gui designs were made:


```{image} images/opencoin-1.jpg
:alt: overview
:width: 150px
:align: left

```

```{image} images/opencoin-2.jpg
:alt: hub tokens
:width: 150px

```

```{image} images/opencoin-3.jpg
:alt: dialog
:width: 266px

```

## v0.2

Approaches to improve OpenCoin.

### Extended protocol

The protocol was extended: https://github.com/OpenCoin/opencoin-historic/tree/master/standards

### pys60 client

[This client](https://github.com/OpenCoin/opencoin-historic/tree/master/sandbox/jhb/mobile) runs on s60, which is the operating system that was used by early Nokia smartphones. There was a python version for s60 (called pys60) that allowed running 
python scripts. 



```{image} images/ocwallet7.jpg
:alt: no currency
:width: 150px
:align: left

```

```{image} images/ocwallet10.jpg
:alt: add currency
:width: 150px

```

```{image} images/ocwallet12.jpg
:alt: info url
:width: 150px

```

```{image} images/ocwallet19.jpg
:alt: baachcoins
:width: 150px

```

### python version

This was a python version to be run for documentation purposes:

- https://github.com/OpenCoin/opencoin-historic/tree/master/sandbox/jhb/oc2

## v0.3

An attempt to bring the [protoco](https://baach.de/static/ocdoc/)l closer to its origins, and to create a [pure javascript implementation](https://github.com/OpenCoin/opencoin-js).

## v0.4

This is the current version, where the focus is on the OpenCoin protocol only. We think now that just creating the protocol, and keeping it as small and simple as possible is the [best approach](scope.md) for implementers.
