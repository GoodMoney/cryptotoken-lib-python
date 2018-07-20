# cryptotoken-lib-python
An abstract interface on top of multiple blockchain / token stacks.

## What Is it?
This is an abstraction layer providing a general purpose interface on top of token libraries.  The major operations required for a token are accounted for.  Initially, it will support ERC20 / ERC223 standards, with emphasis on what will be required to support tokens across multiple blockchains.

https://github.com/Dexaran/ERC223-token-standard

In Ethereum, ERC223 defines the transfer function as:
`transfer(address to, uint value, bytes data)`

There are several intrinsic variables from making the call, including:
* Source address / where to subtract the balances from. This is gleaned from the key that signed the transaction.
* Token address. This is found because the token code is deployed at the address where the transaction is calling a function.
* Callback: This is specific to ERC223, and is encoded in the data parameter.

## Suggested API

```python
cryptoToken = EthereumCryptoToken('mainnet')
cryptoToken.transfer(tokenAddress, fromAddress, toAddress, value, data)
```

## Use



