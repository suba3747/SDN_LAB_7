#!/usr/bin/env python3

from scapy.all import *
from scapy.contrib.openflow import OpenFlow
from scapy.layer.l2 import Ether
import os

def Packet_capture():
    user_input = os.system("sudo tcpdump -i eth0 port 6653 -c40 -w sunny.pcap")

def User_Input():
    packet_list= rdpcap("/home/mininet/objective_5.pcap")
    controller_ip = packet_list[2]['IP'].src
    controller_port = packet_list[2]['TCP'].sport
    print(controller_ip, controller_port)
   # d = Ether()/IP(dst="192.168.215.8", src="192.168.215.7")/TCP(sport=9999, dport=6653, seq=1)/openflow.OFPTPacketIn()
   # sendp(d)

if __name__ == "__main__":
    Packet_capture()
    User_Input()
    
