# Computer Security Class ECEN 4133/5133 (or CSCI 4830)
## Fall 2021
Consolidating all computer security class repo's.

## [Project 1: Cryptography](https://github.com/Mark-Davis-W/Computer_Security_class/tree/master/Project1)

### **Objectives:**
* Understand common pitfalls when applying cryptographic primitives.
* Investigate how cryptographic failures can compromise the security of applications.
* Appreciate why you should use HMAC-SHA256 as a substitute for common hash functions.
* Understand why padding schemes are integral to cryptographic security.

## Part 1:
### 1.1 Length Extension
### 1.2 Hash Collisions

## Part 2:
### 2.1 Classical Cryptanalysis
### 2.2 Padding Oracle Attack (grad students)
* I didn't do this, but information is here.


## [Project 2: Web Security](https://github.com/Mark-Davis-W/Computer_Security_class/tree/master/Project2)

### **Objectives**
* Learn to spot common vulnerabilities in websites and to avoid them in your own projects.
* Understand the risks these problems pose and the weaknesses of naive defenses.
* Gain experience with web architecture and with HTML, JavaScript, and SQL programming.

## Part 1: SQL Injection
### 1.0 No defenses on website
### 1.1 Protected against simple escaping (') --> (")
### 1.2 Protected against 1.1 and applies MD5 hash to password
### 1.3 SQL Extra Credit-Scavenger hunt 
* I did this and got the extra credit

## Part 2: Cross-site Scripting (XSS)
### 2.0 No defenses on website
### 2.1 Protected against javascipt word "script"
### 2.2 Protected against 2.1 and many html tags
### 2.3 Remove punctuations like [;'/"] and includes 2.2
### 2.4 Extra Credit: Remove and replaces <> into &lt,&gt and includes 2.3
* was not able to do this within time allotted

## Part 3: Cross-site Request Forgery (CSRF)
### 1.0 No defenses on website
### 1.1 Validates hidden token (can use XSS)
### 1.2 Uses 1.1 protections (cannot use XSS)
* was not able to do this within time allotted


## [Project 3: Network Security](https://github.com/Mark-Davis-W/Computer_Security_class/tree/master/Project3)

### **Objectives:**
* Gain exposure to core network protocols and concepts.
* Understand offensive techniques used to attack local network traffic.
* Learn to apply manual and automated traffic analysis to detect security problems.

## Part 1: Network Attacks
* In this scenario, we have gotten the target to download a python script that runs in the background and hijacks the key received by a website setup by the target to generate AES-256 keys to anyone that visits.
### Extra Credit
* Same scenario but with HTTPS.

## Part 2: Network Attacks-2
* Write a python script and check network traffic for anomallies, possibly due to a computer trying to port scan and probe for vulnerabilities.

## [Project 4: Application Security](https://github.com/Mark-Davis-W/Computer_Security_class/tree/master/Project4)

### **Objectives**
* Be able to identify and avoid buffer overflow vulnerabilities in native code.
* Understand the severity of buffer overflows and the necessity of standard defenses.
* Gain familiarity with machine architecture and assembly language.
* Not allowed to use pre-made hacking tools

## Part 1: Buffer-overflow Attacks
### 1.0 Use GDB debugger to examine c target and find where it's vulnerable.
### 1.1 Overwrite return address to run different sub-function.
### 1.2 Inject shellcode.py provided and redirect return to it.
### 1.3 No overflow had to find another way.
### 1.4 Make python script to output a machine code file for program to run.
### 1.5 Bypass DEP (Data Execution Prevention) - doesn't run code from stack
### 1.6 Like 1.2 but has ASLR (Address-Space Layout Randomization)
### 1.7 Extra Credit: Heap-based exploitation
### 1.8 Extra Credit: Return-Oriented Programming
### 1.9 Extra Credit: Callback shell - open TCP port and run commands as root

## [Project 5: “Smart” Contracts](https://github.com/Mark-Davis-W/Computer_Security_class/tree/master/Project5)

### **Objectives:**
* Implement and deploy a basic Ethereum smart contract in Solidity
* Understand basic smart contract vulnerabilities
* See how vulnerabilities can lead to stolen funds.

### 0.0 Setup MetaMask and MyEtherWallet on Ropsten Testnet and get free starter Ether
* create a basic contract and do some basic interactions

## Part 1: Vulnerable Contracts
* Using solidity with online IDE Remix utilize the contracts vulnerabilities to "steal" more funds than is deposited.
