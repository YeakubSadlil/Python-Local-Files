#! /user/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # ff:ff:ff:ff:ff:ff is the broadcast MAC address
    arp_request_broadcast = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)[0] # srp() returns a list of two lists: answered and unanswered packets
    
    for element in answered:
        print(element[1].psrc)
        print(element[1].hwsrc)
        print("\n")
scan("10.0.2.1/24")