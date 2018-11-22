
class Token:
    def __init__(self, web3, contract_address, abi):
        self.web3 = web3
        self.address = self.web3.toChecksumAddress(contract_address)
        self.abi = abi
        self.contract = self.web3.eth.contract(address=self.address, abi=self.abi)

    def name(self):
        return self.contract.functions.name().call()

    def symbol(self):
        return self.contract.functions.symbol().call()

    def decimals(self):
        # TODO: Make this not fail if contract doesn't have it.
        return self.contract.functions.decimals().call()

    def totalSupply(self):
        return self.contract.functions.totalSupply().call()
    
    def balanceOf(self, addr):
        checksum_addr = self.web3.toChecksumAddress(addr)
        wei_balance = self.contract.functions.balanceOf(checksum_addr).call()
        return wei_balance

    # Functions that change the blockchain
    # You must call .transact({...}) or .buildTransaction() on the object this returns
    def transfer(self, to, amount):
        return self.contract.functions.transfer(
            self.web3.toChecksumAddress(to), 
            amount
        )
    

def parse_truffle_json(json_file, network): # Ganache is 5777
    import json as json_lib
    json = json_lib.load(json_file)
    return [json['networks'][network]['address'], json['abi']]
