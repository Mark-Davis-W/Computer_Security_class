#!/usr/bin/python3

from scapy.all import *
from collections import Counter
import sys

# Complete this function!
def process_pcap(pcap_fname):
    norm_list = {}
    # rtrn_list = []
    for pkt in PcapReader(pcap_fname):
        # Your code here
        if not pkt.haslayer(TCP):
            continue
        if not pkt.haslayer(IP):
            continue
        if not pkt.haslayer(Ether):
            continue
        # check for 'SYN' packets
        if pkt[TCP].flags == 'S':
            # store source ip of SYN packet 
            ip_addr = pkt[IP].src
            if ip_addr not in norm_list: norm_list[ip_addr] = {'SYN':0,'SYN-ACK':0}
            norm_list[ip_addr]['SYN'] += 1

        # check for 'SYN+ACK' packets
        if pkt[TCP].flags == 'SA': 
            # store source ip of 'SYN+ACK' packet 
            ip_addr = pkt[IP].dst
            if ip_addr not in norm_list: norm_list[ip_addr] = {'SYN':0,'SYN-ACK':0}
            norm_list[ip_addr]['SYN-ACK'] += 1

    for s in sorted(norm_list.keys()):
        if norm_list[s]['SYN'] < (norm_list[s]['SYN-ACK'] * 3):
            del norm_list[s]

    # Debugging checking output
    # with open('norm_list.txt','w') as f:
    #     for key,value in norm_list.items():
    #         print(key,value,sep=" : ",file=f)
    # f.close()

    for key,value in norm_list.items():
        print(key)


if __name__=='__main__':
    if len(sys.argv) != 2:
        print('Use: python3 detector.py file.pcap')
        sys.exit(-1)
    process_pcap(sys.argv[1])
