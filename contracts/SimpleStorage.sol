// SPDX-License-Identifier: UNLISENCED
pragma solidity ^0.8.19;

contract SimpleStorage {
    uint256 public number;

    function setNumber(uint256 _newNumber) public {
        number = _newNumber;
    }
}
