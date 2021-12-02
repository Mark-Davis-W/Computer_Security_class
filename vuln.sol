pragma solidity ^0.5.0;

// This contract is vulnerable to having its funds stolen.
// Written for ECEN 4133 at the University of Colorado Boulder: https://ecen4133.org/
// (Adapted from ECEN 5033 w19)
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

// In this part, you’ll investigate how to steal Ethereum from vulnerable smart contracts. We have
// setup a vulnerable smart contract on the Ropsten testnet that you have permission to steal funds
// from. However, using this technique on other contracts you do not have the same permission for
// outside this class is a crime. Remember that just because you can do something technical, doesn’t
// mean that you should!

// We’ve deployed our contract to address 0x36A540E3A78084962B75E25877CfACf8846Be018. The
// source is available in your Github starter code as vuln.sol.

// The contract has two functions: deposit and withdraw that let you send and receive money from
// the contract. On the surface, it appears that an address will only be able to withdraw what that
// address originally deposited. But this contract is vulnerable to a bug that lets you extract more if
// you’re clever!

// Your goal is to make a contract that includes a payable function, that interacts with the Vuln contract to steal
// funds from it. Your contract should let you pay it a small amount (e.g. 0.1 ETH), and then later
// let you extract a greater amount (e.g. 0.2 ETH). If we look at the (internal) transactions between
// your contract and the Vuln contract, we should see that yours sends (deposits) less than it gets back
// (withdraws) from the Vuln contract.


contract attack {
    address vuln_contract = 0x36A540E3A78084962B75E25877CfACf8846Be018
    Vuln public vuln = Vuln(address(vuln_contract))

    uint256 public balance;

    function() gimmeGimme public payable {
        vuln.withdraw()

    }
}
