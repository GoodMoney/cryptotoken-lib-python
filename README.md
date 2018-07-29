
# cryptotoken-lib-python

A library which provides an abstract interface to interact with tokens on multiple cryptocurrency networks. 

Network providers are written for:
* Ethereum

- [cryptotoken-lib-python](#cryptotoken-lib-python)
- [What Is it?](#what-is-it)
    - [Discussion](#discussion)
- [Data Structures](#data-structures)
    - [Networks](#networks)
    - [Users](#users)
    - [UserAddresses](#useraddresses)
- [High-Level API](#high-level-api)
- [Low-Level API](#low-level-api)
- [Network Protocol Adapters](#network-protocol-adapters)
    - [Ethereum json-rpc](#ethereum-json-rpc)

# What Is it?
This library will provide an abstraction layer giving a general purpose interface on top of the major interactions with crypto-tokens across multiple cryptocurrency blockchains and networks.  The major operations required for a token are accounted for.  Initially, it will support ERC20 / [ERC223](https://github.com/Dexaran/ERC223-token-standard) standards, with emphasis on what will be required to support tokens across multiple blockchains.

In Ethereum, ERC223 defines the transfer function as:
`transfer(address to, uint value, bytes data)`

## Discussion

There are several intrinsic variables derived from making the call, including:
* Source address / where to subtract the balances from. This is gleaned from the key used to sign the transaction.
* Token address. This is found because the token code is deployed at the address where the transaction is calling a function.
* Callback: This is specific to ERC223, and is encoded in the data parameter.


# Data Structures
## Networks

| Network  | Chain   | Protocol    | Network Address                 |
| -------- | ------- | ----------- | ------------------------------- |
| Ethereum | mainnet | json-rpc    | 192.168.67.124:8545             |
| Ethereum | ropsten | json-rpc    | 192.168.67.124:8546             |
| Ethereum | local   | json-rpc    | 127.0.0.1:8545                  |
| Bitcoin  | Main    | blockcypher | api.blockcypher.com/v1/btc/main |

## Users
| id  | Name          |
| --- | ------------- |
| 1   | Duke Jones    |
| 2   | Nick Sullivan |

## UserAddresses
| id  | network_id | user_id | address        | private_key |
| --- | ---------- | ------- | -------------- | ----------- |
| 1   | 1          | 1       | 0x243597fe2... | null        |
| 2   | 1          | 2       | 0x935d8c00...  | null        |



# High-Level API
Utilizing the above data structures, we are able to look up and construct some nice high-level calls.

> TODO: Evaluate whether to include the db, lookups, and higher-level API in this library or split out into a higher-level library.

```python
network = GetNetwork("Ethereum", "mainnet", "json-rpc")
token = GetToken('OMG')
duke = GetUserByName("Duke Jones")
nick = GetUserByName("Nick Sullivan")

network.buildTransfer(token, duke, nick, "194.357") # Amount is a decimal-style representation in the precision defined in the smart contract.
```

# Low-Level API
This level of code is written with a minimum of suppositions.  Without the benefit of data structures and lookups, it operates at the lowest level of abstraction on top of the network protocol adapters themselves.

```python
network = GetNetwork("Ethereum", "json-rpc", "192.168.67.124:8545")
unsignedTx = network.buildTransfer({
    'token': "0x9d36a...",
    'sender': "0x145f...",
    'recipient': "0x932ec2...",
    'amount': 194850000000000000000000 # denominated in wei
})

signedTx = senderPrivateKey.sign(unsignedTx)
network.broadcastRawTx(signedTx)

```

# Network Protocol Adapters
## Ethereum json-rpc
This is the first adapter we will write.