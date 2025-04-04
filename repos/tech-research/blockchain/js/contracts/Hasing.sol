// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Hashing {
    function performHash(uint256 iterations, string memory input) public pure returns (bytes32) {
        bytes32 hash = keccak256(abi.encodePacked(input));
        for (uint256 i = 0; i < iterations; i++) {
            hash = keccak256(abi.encodePacked(hash));
        }
        return hash;
    }
}