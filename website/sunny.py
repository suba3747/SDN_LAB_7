#!/usr/bin/env python3
#OBJECTIVE 2
from mimetypes import init
import re
from flask import Blueprint, Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import path
import flask
import scapy
import paramiko
import time
sunny = Blueprint('sunny', __name__)
@sunny.route("/")
def index():
    return ("Hello World")
        
@sunny.route('/Home')
def Home():
    return render_template('Home.html',TargetRoute='/Home', TargetPage="Home")

@sunny.route("/staticrouting", methods=['GET', 'POST'])
def Static_Flow_Entries():
    if request.method == 'POST':
        DPID = request.form.get('DPID')
        PRIORITY = request.form.get('PRIORITY')
        IN_PORT = request.form.get('IN-PORT')
        ETH_TYPE = request.form.get("ETH-TYPE")
        #SOURCE_IP = request.form.get("SOURCE IP")
        DEST_IP = request.form.get("DESTINATION IP")
        ACTION = request.form.get("ACTION")
        # suba = paramiko.SSHClient()
        # suba.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # suba.connect('192.168.215.7', username='mininet', password='mininet')
        # time.sleep(10)
        # print(DPID)
        # stdin, stdout, stderr = suba.exec_command("sudo" (DPID))
        # stdin.write('mininet'+'\n')
        # stdin, stdout, stderr = suba.exec_command("sudo ovs-ofctl add-flow "+str(DPID)+" in_port="+str(IN_PORT)+",nw_dst="+str(DEST_IP)+"actions="+str(ACTION))
        # stdin.write('mininet'+'\n')
        # print(stdout.readline())
        # for line in stdout.read().splitlines(): 
        #     basic = line.decode('utf-8')
        #     print (basic)   
        # return render_template()     
        #print(DPID)
        #static_flow_entries = ['curl -X POST -d '{"dpid":{},"priority":20000,"match":{"dl_type":0x806},"actions":[{"type":"OUTPUT","port":"flood"}]}' http://{}/stats/flowentry/add']
    return render_template("staticrouting.html", TargetRoute='/staticrouting', TargetPage="Home")

@sunny.route("/firewall",  methods=['GET', 'POST'])
def Firewall():
    if request.method == 'POST':
        DPID = request.form.get('DPID')
        PRIORITY = request.form.get('PRIORITY')
        IN_PORT = request.form.get('IN-PORT')
        ETH_TYPE = request.form.get("ETH-TYPE")
        SOURCE_IP = request.form.get("SOURCE IP")
        DEST_IP = request.form.get("DESTINATION IP")    
        L4_PROTOCOL = request.form.get("L4 PROTOCOL")
        print(DPID) 
        #firewall_rule = 
    return render_template("firewall.html", TargetRoute='/firewall', TargetPage="Home")
#if __name__ == "__main__":
 #   sunny.run(host='127.0.0.30', port=5001)