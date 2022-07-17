from scripts.helpful_scripts import get_account
from brownie import GateOneAttack


def main():
    account = get_account()
    deploy(account)
    attack = GateOneAttack[-1]

    tx = attack.attack({"from": account})
    tx.wait(1)


def deploy(account):
    GateOneAttack.deploy(
        "0x3C4d5BFc29672Bfa294C09889c1CE9aEB01F4Bd7", {"from": account}
    )
