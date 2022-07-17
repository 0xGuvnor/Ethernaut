from scripts.helpful_scripts import get_account
from brownie import interface, SwappableTokenTwo


def main():
    account = get_account()
    dex = interface.DexTwo("0x44B72E4D244f4B113aE35a7681bE4A6275e68418")
    token1 = interface.IERC20("0xB757504386b564C6DFE30D982f633D16AD816583")
    token2 = interface.IERC20("0xd5f4335aF646fa286A8c10a7Cf7b31aeE741E736")
    my_token = SwappableTokenTwo.deploy(
        dex.address, "My Token", "MTK", 9999e18, {"from": account}
    )

    dex.approve(dex.address, 9999, {"from": account})
    my_token.approve(account.address, dex.address, 9999, {"from": account})

    my_token.transfer(
        dex.address,
        100,
        {"from": account},
    )
    dex.swap(my_token.address, token1.address, 100, {"from": account})

    my_token.transfer(
        dex.address,
        100,
        {"from": account},
    )
    dex.swap(my_token.address, token2.address, 100, {"from": account})

    print(
        f"Contract has {token1.balanceOf(dex.address)} token1 and {token2.balanceOf(dex.address)} token2 left."
    )
