
# cryptotoken-lib-python

A library which provides an abstract interface to interact with tokens on multiple cryptocurrency networks. 

Network providers are written for:
* Ethereum

- [cryptotoken-lib-python](#cryptotoken-lib-python)
- [What Is it?](#what-is-it)
- [Using cryptotoken-lib](#using-cryptotoken-lib)
    - [Ethereum](#ethereum)
        - [Connecting to a particular Ethereum provider](#connecting-to-a-particular-ethereum-provider)
            - [HTTP](#http)
            - [Infura](#infura)
- [Discussion](#discussion)
- [Low-Level API](#low-level-api)
- [Network Protocol Adapters](#network-protocol-adapters)
    - [Ethereum json-rpc](#ethereum-json-rpc)
- [TO REMOVE](#to-remove)
- [Database Structs](#database-structs)
    - [Networks](#networks)
    - [Users](#users)
    - [UserAddresses](#useraddresses)
- [High-Level API](#high-level-api)

# What Is it?
This library will provide an abstraction layer giving a general purpose interface on top of the major interactions with crypto-tokens across multiple cryptocurrency blockchains and networks.  The major operations required for a token are accounted for.  Initially, it will support ERC20 standard, with emphasis on what will be required to support tokens across multiple blockchains.


# Using cryptotoken-lib

```python
from cryptotoken-lib import *

network = Ethereum.Network("127.0.0.1:8545")
token = EthereumToken()
token.send(to="0x98234f...", amount=Decimal(35.300))
```

## Ethereum
In Ethereum, ERC20 defines the transfer function as:
`transfer(address to, uint value, bytes data)`


### Connecting to a particular Ethereum provider

#### HTTP
You can set the environment variable WEB3_PROVIDER_URI before starting your script, and web3 will look for that provider first.

```bash
export WEB3_PROVIDER_URI=http://127.0.0.1:8545
python my_program.py
```

Valid formats for the this environment variable are:

file:///path/to/node/rpc-json/file.ipc
http://192.168.1.2:8545
https://node.ontheweb.com
ws://127.0.0.1:8546


#### Infura
To connect to the Infura Mainnet remote node, first register for a free API key if you don’t have one at https://infura.io/signup .

Then set the environment variable INFURA_API_KEY with your API key:

```bash
export INFURA_API_KEY=YourApiKey
python my_program.py
```

# Discussion

There are several intrinsic variables derived from making the call, including:
* Source address / where to subtract the balances from. This is gleaned from the key used to sign the transaction.
* Token address. This is found because the token code is deployed at the address where the transaction is calling a function.
* Callback: This is specific to ERC223, and is encoded in the data parameter.






# Low-Level API

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

The library we use for interacting with Ethereum's RPC interface is called "web3".
In order to interact with contract source code, you will need the solidity compiler
Mac OS X:
`brew install solidity`



\
\
\
\
\
&nbsp;





# TO REMOVE
# Database Structs
## Networks

| Blockchain | Provider    | Network | Protocol    | Address                         |
| ---------- | ----------- | ------- | ----------- | ------------------------------- |
| Ethereum   | personal    | mainnet | json-rpc    | 192.168.67.124:8545             |
| Ethereum   | personal    | ropsten | json-rpc    | 192.168.67.124:8546             |
| Ethereum   | personal    | local   | json-rpc    | 127.0.0.1:8545                  |
| Ethereum   | Etherscan   | mainnet | etherscan   | https://api.etherscan.io        |
| Bitcoin    | Blockcypher | mainnet | blockcypher | api.blockcypher.com/v1/btc/main |

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
