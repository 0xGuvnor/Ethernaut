from scripts.helpful_scripts import get_account
from brownie import interface


def main():
    account = get_account()
    simple_token = interface.SimpleToken(
        "0x794180BA50DC2B11dB93aD35AF23cDb2dDE06b2e"
    )  # address taken from etherscan

    tx = simple_token.destroy(account, {"from": account})
    tx.wait(1)
