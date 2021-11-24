import etherscan
import sys
import json
from const import *

eth = etherscan.Etherscan(API_KEY, net="ropsten")
with open(sys.argv[1]) as f:
    student_addr = f.read().strip()
    # student_addr = "0xff1c8cacb0dbd4a845fff22e0653480c9f795a9c"
    res = eth.get_internal_txs_by_address(CONTRACT, 10308757, 'latest', 'asc')
    to_contract = list(filter(lambda x: x['to'] == CONTRACT.lower(), res))
    from_contract = list(filter(lambda x: x['from'] == CONTRACT.lower(), res))

    print(len(res))

    from_contract = []
    to_contract = []
    for obj in res:
        if obj['to'] == student_addr:
            from_contract.append(obj)
    to_contract = [obj for obj in res if (obj['from'] == str(student_addr))]
    # from_contract = list(filter(lambda x: x['to'] == student_addr, res))
    # to_contract = list(filter(lambda x: x['from'] == student_addr, res))
    sum_in = 0
    for i in range(len(to_contract)):
        sum_in += int(to_contract[i]['value'])
    sum_out = 0
    for j in range(len(from_contract)):
        sum_out += int(from_contract[j]['value'])

    if sum_out > sum_in:
        print("passed")
    else:
        print("amount receieved is not greater than amount sent")
