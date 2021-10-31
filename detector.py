#!/usr/bin/python3

from scapy.all import *
from collections import Counter
import sys

# Complete this function!
def process_pcap(pcap_fname):
    norm_list = []
    rtrn_list = []
    for pkt in PcapReader(pcap_fname):
        # Your code here
        if pkt.haslayer(TCP):
            if pkt.haslayer(IP):
                if pkt.haslayer(Ether):
                    # check for 'SYN' packets
                    if pkt[TCP].flags == 'S':
                        # store source ip of SYN packet 
                        ip_addr = pkt[IP].src
                        norm_list.append(ip_addr)
                        # print("SYN packet found..........: " + ip_addr)
                        # print(ip_addr)

                    # check for 'SYN+ACK' packets
                    if pkt[TCP].flags == 'SA': 
                        # store source ip of 'SYN+ACK' packet 
                        ip_addr = pkt[IP].dst
                        rtrn_list.append(ip_addr)
                        # print("SYN+ACK packet found......: " + ip_addr)
                        # if ip_addr in ['128.3.23.2','128.3.23.5','128.3.23.117','128.3.23.158','128.3.164.248','128.3.164.249']:
                        # print(ip_addr)
    norm_list = Counter(norm_list)
    rtrn_list = Counter(rtrn_list)
    final = [key for key,count in norm_list.items() if key in rtrn_list and count > (3*rtrn_list[key])]
    print(*final, sep="\n")
    # sus_list = []


if __name__=='__main__':
    if len(sys.argv) != 2:
        print('Use: python3 detector.py file.pcap')
        sys.exit(-1)
    process_pcap(sys.argv[1])
