#!/usr/bin/env python3

import socket, threading, sys, argparse, pyfiglet
from datetime import datetime

target = ""

# Some Colors
class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

ascii_banner = pyfiglet.figlet_format('Port Scanner')
print (bcolors.OKCYAN + ascii_banner)
print (bcolors.WARNING + "                   by @Taha El Ghadraoui")
print (bcolors.WARNING + "		      @bvr0n \n")

### Usage
def usage():
    print('Optional arguments:\n   -u\tset Target\n')

if len(sys.argv) < 2:
    usage()
    exit()
else:
    target = sys.argv[2]

## Creating the tcp socket
def portscan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        con = s.connect((target,port))
        print(bcolors.OKGREEN + "[+] " +'Port :',port,"is open")
        con.close()
    except:
        pass

# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

print ("\n")
print (bcolors.BOLD + "[+] Scanning All 65 535 TCP Ports.. \n")

## Scanning
r = 1
for x in range(1,65535):
    t = threading.Thread(target=portscan,kwargs={'port':r})
    r += 1
    t.start()