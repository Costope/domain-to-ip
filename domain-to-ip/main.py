import socket

def get_ip_from_domain(domain):
    try:
        info = socket.getaddrinfo(domain, None)
        ip = info[0][4][0]
        return ip
    except (socket.gaierror, IndexError):
        return "Error by getting IP"

if __name__ == "__main__":
    domain = input("Enter a Domain: ")
    ip_address = get_ip_from_domain(domain)
    print(f"IP-Adresse from {domain}: {ip_address}")
