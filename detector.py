#!/usr/bin/python3

from scapy.all import *
import sys

# Complete this function!
def process_pcap(pcap_fname):
    for pkt in PcapReader(pcap_fname):
        # Your code here
        if pkt.haslayer(Ether):
            if pkt.haslayer(IP):
                if pkt.haslayer(TCP):
                    # check for 'SYN' packets
                    if pkt[TCP].flags == 'S':
                        # store source ip of SYN packet 
                        ip_addr = pkt[IP].src
                        # print("SYN packet found..........: " + ip_addr)
                        print(ip_addr)

                    # check for 'SYN+ACK' packets
                    if pkt[TCP].flags == 'SA': 
                        # store source ip of 'SYN+ACK' packet 
                        ip_addr = pkt[IP].src
                        # print("SYN+ACK packet found......: " + ip_addr)
                        print(ip_addr)


if __name__=='__main__':
    if len(sys.argv) != 2:
        print('Use: python3 detector.py file.pcap')
        sys.exit(-1)
    process_pcap(sys.argv[1])
