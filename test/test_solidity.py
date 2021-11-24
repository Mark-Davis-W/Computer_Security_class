import etherscan
import sys
import hashlib
from const import *

eth = etherscan.Etherscan(API_KEY, net="ropsten")
with open(sys.argv[1], "rb") as f:
    byte_file = f.read()
    with open(sys.argv[2]) as contract:
        contract_source = contract.read()
        res = eth.get_contract_source_code(contract_source)
        sha256_source_code = hashlib.sha256(res[0]['SourceCode'].encode('utf-8')).hexdigest()
        sha256_attack_sol = hashlib.sha256(byte_file).hexdigest()

        if(sha256_attack_sol == sha256_source_code):
            print("passed")
        else:
            print("source code of contract at " + contract_source + "and attack.sol dont match")
