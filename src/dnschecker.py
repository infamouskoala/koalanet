import socket
from src.design.colors import RED, PURPLE, WHITE, GREEN, BLUE

def dns(hostname):
    try:
        results = socket.getaddrinfo(hostname, None)
        ipv4_addresses = []
        ipv6_addresses = []

        for result in results:
            name, a, b, c, sockaddr = result
            address = sockaddr[0]
            if name == socket.AF_INET: # for v4
                ipv4_addresses.append(address)
            elif name == socket.AF_INET6: # for v6
                ipv6_addresses.append(address)

        print(f"{PURPLE}[+]{WHITE} DNS information:")
        print(f"IPv4 addresses:{ipv4_addresses}")
        print(f"IPv6 addresses:{ipv6_addresses}")
    
    except Exception as e:
        print(f"{RED}[LOG]{WHITE}: {e}")

# dns("google.com")