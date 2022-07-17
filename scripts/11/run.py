from scripts.helpful_scripts import get_account
from brownie import Scaffold


def main():
    account = get_account()
    deploy(account)

    scaffold = Scaffold[-1]

    tx = scaffold.attack({"from": account})
    tx.wait(1)


def deploy(account):
    elevator_addr = "0xE93e546B713c2B29De18EfbF36AED1c78fda52dE"
    Scaffold.deploy(elevator_addr, {"from": account})
