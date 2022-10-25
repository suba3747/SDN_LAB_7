#!/usr/bin/env python3

from lib2to3.pgen2.token import AT
from scapy.all import *
from scapy.contrib.openflow import OpenFlow
from scapy.layer.l2 import Ether
import os
import subprocess
def Packet_capture():
    user_input = os.system("sudo tcpdump -i enp08 port 6653 -c40 -w sunny.pcap")
def User_Input():
    packet_list= rdpcap("/home/mininet/sunny.pcap")
    sunn= len(packet_list)
    detect= []
    if type == "OFTL_PACKET_IN":
        for i in sunn:
            attacker_port = packet_list[i]['TCP'].sport
            detect.append(i)
    
    no_packet=len(detect)
    if no_packet == 100:
        sunny = subprocess.Popen(["iptables", "tcp", "-m", "tcp", "--sport", "9999" , "-j", "DROP"],stdout=subprocess.PIPE)
        print("stopped the port which we are getting multiple packet")
if __name__ == "__main__":
    Packet_capture()
    User_Input()
   