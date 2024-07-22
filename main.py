import socket
import threading

# function to scan a single port for a given protocol
def scan_port(target, port, protocol):
    if protocol == 'tcp':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    elif protocol == 'udp':
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.settimeout(1)

    if protocol == 'tcp':
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}/TCP: Open")
        else:
            print(f"Port {port}/TCP: Closed")
    elif protocol == 'udp':
        try:
            sock.sendto(b'', (target, port))
            sock.recvfrom(1024)
            print(f"Port {port}/UDP: Open")
        except socket.error:
            print(f"Port {port}/UDP: Closed")

    sock.close()

# function that creates and starts threads for each port
def scan_ports(target, ports, protocol):
    print(f"Scanning target: {target} using {protocol.upper()} protocol")
    threads = []

    for port in ports:
        thread = threading.Thread(target=scan_port, args=(target, port, protocol))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    protocol = input("Enter the protocol (tcp/udp): ").lower()

    ports = range(start_port, end_port + 1)

    scan_ports(target, ports, protocol)