import socket

def get_ip_from_domain(domain):
    try:
        info = socket.getaddrinfo(domain, None)
        ip = info[0][4][0]
        return ip
    except (socket.gaierror, IndexError):
        return "Konnte IP nicht auflösen"

if __name__ == "__main__":
    domain = input("Gib eine Domain ein: ")
    ip_address = get_ip_from_domain(domain)
    print(f"IP-Adresse von {domain}: {ip_address}")