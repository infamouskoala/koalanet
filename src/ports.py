import socket
from src.design.colors import RED, GREEN, PURPLE, WHITE
import requests

def sockscan(ip, startport, endport):
    open_ports = []
    i = 1
    while startport <= endport:
        port = startport
        print(f"{RED}[-]{WHITE} port scanned: {i}", end="\r")
        i += 1
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
            print(f"{GREEN}[+]{WHITE} Found an open port: {port}")
        sock.close()
        startport = startport+1
    return open_ports

"""
realising socket has to establish a connection in order to complete a connection and count a port as open
so for that, you might want to use an open port on ur router aaswell. If you dont wanna do it, we can use another
method that uses requests. However, it's important to note that this method is not a traditional port scan and 
relies on the assumption that the server has a web service running on the specified ports.
"""

def reqscan(ip, start, end):
    open_ports = []
    while start <= end:
        url = f"http://{ip}:{start}"
        try:
            r = requests.get(url, timeout=1)
            if r.status_code == 200 or r.status_code == 404:
                open_ports.append(start)
                print(f"{GREEN}[+]{WHITE} Found an open port: {start}")
        except requests.RequestException as e:
            print(f"{RED}[-]{WHITE} port scanned: {start}", end="\r")
        start += 1
    return open_ports

# open_ports = reqscan("192.168.1.1", 0, 1024)
# print(f"{PURPLE}[+]{WHITE} Open ports:", open_ports)