#!/bin/python
from queue import Queue
import socket
import time
import threading
import pyfiglet
import os
from datetime import datetime
clear=lambda : os.system('clear')
clear()
banner=pyfiglet.figlet_format("MINUTEBOSS")
print (banner)
print("1.Scan ipaddress.\n")
print("2.Scan website.\n")
choice=input("Enter option:")
if choice=='1':
target=input("Enter ipaddress to scan:")
if choice=='2':
website=input("Enter hostname to scan:")
target=socket.gethostbyname(website)
print ("Scanning target:" + target)
print ("Scanning started at:"+str(datetime.now()))
print ("-" * 50)
q = Queue()
open_ports = []
def portscan(port):
