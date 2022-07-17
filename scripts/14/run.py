from scripts.helpful_scripts import get_account
from brownie import Gk2Attack


def main():
    account = get_account()
    Gk2Attack.deploy("0x574B5b8c10Ca2cCB833f77995A6e4018fe800d2d", {"from": account})
