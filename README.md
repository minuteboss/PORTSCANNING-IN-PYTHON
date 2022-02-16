# PORTSCANNING-IN-PYTHON
This is a python threaded portscanner to scan websites and ipaddresses.

To run the script:
git clone the file.
chmod +x portscanner.py
python portscanner.py

PORTSCANNING IN PYTHON 1
PORTSCANNING IN PYTHON
Portscanning refers to locating “listening” TCP or UDP ports and obtaining sufficient
information about the device from the ports. Port scanning involves the transmission of
TCP segments or UDP datagrams
 to interesting port numbers at a given IP address.
Our goal when port scanning is to answer three questions regarding the server;
1. What ports are open?
2. What services are running on these ports?
3. What versions of those services are running?
PYTHON SCRIPT
💡 You need basic python skills and an understanding of threading, the Queue
module, and the socket module to understand the script better.
First things first, Import the modules

from queue import Queue
import socket
import time
import threading
import pyfiglet
import os
from datetime import datetime

The main module is the socket module. This module provides access to the BSD socket
interface.

clear=lambda : os.system('clear')
clear()

PORTSCANNING IN PYTHON 2
Use os.system(’cls’) for windows.
This will blank the screen once you run the script.

banner=pyfiglet.figlet_format("MINUTEBOSS")
print (banner)

This creates a banner with the name MINUTEBOSS, feel free to change it and add
fonts and styles of your liking.

print("1.Scan ipaddress.\n")
print("2.Scan website.\n")
choice=input("Enter option:")
if choice=='1':
target=input("Enter ipaddress to scan:")
if choice=='2':
website=input("Enter hostname to scan:")
target=socket.gethostbyname(website)

Get the target ip or website name to scan.
socket.gethostbyname() gets the ip of a website.

print ("Scanning target:" + target)
print ("Scanning started at:"+str(datetime.now()))
print ("-" * 50)
q = Queue()
open_ports = []

The first 3 print statements display information about the target and starting time.
We use q to work with the Queue module.
We define a list (open_ports) to store the list of open ports.

def portscan(port):
try:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((target, port))
return True
except:
return False

PORTSCANNING IN PYTHON 3
The function portscan tries to connect to the given ports which we will introduce later.
A pair  (target, port) is used for the  AF_INET address family, where the target is a string
representing an IPv4 address like  '100.50.200.5' , and port is an integer.

def get_ports():
for port in range(1,65535):
q.put(port)

We queue the ports using this function. We also define all ports in this function. You can
change the range to scan specified ports of your liking.

def portguy():
while not q.empty():
port = q.get()
if portscan(port):
print("Port {} is open!".format(port))
open_ports.append(port)
else:
pass

This function checks whether the queue is empty, if not an if statement checks the
return value of the portscan function for different given ports. This is easily managed
using the Queue module. Open ports are appended on the open_ports list.
For closed ports nothing is done.

def run_scanner(threads):
get_ports()
thread_list = []
for t in range(threads):
thread = threading.Thread(target=portguy)
thread_list.append(thread)
for thread in thread_list:
thread.start()
for thread in thread_list:
thread.join()

PORTSCANNING IN PYTHON 4

print("Open ports are:", open_ports)

In this function we call the get_ports() function, create a threading list and start
threading. The portguy function is our target for threading.
After threading we print the open ports list.
For this function we have to pass number of ports to be scanned per second as an
argument.

run_scanner(700)
Different machines perform differently, for me 700 was a good choice.

contact me @marviynestanley@gmail.com
