import etherscan
import sys
from const import *

eth = etherscan.Etherscan(API_KEY, net="ropsten")

with open(sys.argv[1]) as f:
    student_addr = f.read().strip()
    res = eth.get_internal_txs_by_address(CONTRACT, 10308757, 'latest', 'asc')
    to_contract = list(filter(lambda x: x['to'] == CONTRACT.lower(), res))
    from_contract = list(filter(lambda x: x['from'] == CONTRACT.lower(), res))

    if len(to_contract) > 0 and len(from_contract) > 0:
        print("passed")
    else:
        print("no contract interaction")
