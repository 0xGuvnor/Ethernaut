from scripts.helpful_scripts import get_account
from brownie import AttackKing, interface


def main():
    account = get_account()
    king = interface.King("0x282dc6B93d8dD08aD043a4307ea2Eb8491FF0e80")
    prize = king.prize()

    AttackKing.deploy(king.address, {"from": account, "value": prize})
