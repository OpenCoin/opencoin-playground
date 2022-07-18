# Ideas

These are some ideas that might be implemented in the future


## .oc file suffix

It might make sense to have a file ending for OpenCoin messages, especially
for [CoinStacks](schemata.md#coinstack-message). This would allow mime-handlers
to pickup the file and treat them in a special way.

## oc over html

In theory a [CoinStack](schemata.md#coinstack-message) could come as a 
standalone mini-wallet that would display the contents of the embedded CoinStack
in a readable way, along with ways to renew the coins etc.

The problem is that this would make users open up and trust arbitrary html files.

## opencoin.net web wallet

We could implement a web based wallet (using javascript or python in the browser
([pyscript](https://pyscript.net)/[transcrypt](https://transcrypt.org)). This wallet could be either a single html file, containing all css and js, or we use [subresource integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) for this.

This web interface could even be the hander for [.oc files](#oc-file-suffix).