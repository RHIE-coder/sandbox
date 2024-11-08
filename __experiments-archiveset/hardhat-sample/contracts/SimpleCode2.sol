// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract HelloWorld { 

    string private message;

    constructor() {
        message = "hello world";
    }

    function Greeting() public view returns(string memory) {
        return message;
    }

    function ChangeMessage(string calldata _message) public {
        message = _message;
    }

}