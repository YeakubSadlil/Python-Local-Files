#! /user/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # ff:ff:ff:ff:ff:ff is the broadcast MAC address
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()
        
scan("10.0.2.1/24")