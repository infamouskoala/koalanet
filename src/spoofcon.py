import socket
from src.design.colors import GREEN, WHITE, RED

def spoof(ip, port):
    ksec = socket.socket()
    try:
        ksec.connect((ip, port))
    except Exception as e:
        print(f"{RED}[LOG] Error: {e}")

    while True:
        x = input("Msg: ")
        ksec.send(x.encode())
        print(f"{GREEN}[+]{WHITE} Your message has been sent to the host.")