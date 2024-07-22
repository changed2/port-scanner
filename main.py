import socket

def scan_ports(target, ports):
    print(f"Scanning target: {target}")

    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set a timeout of 1 second for the socket operations

    for port in ports:
        result = sock.connect_ex((target, port))  # Try to connect to the target on the specified port
        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")

    sock.close()

if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    ports = range(1, 1025)  # Scan the first 1024 ports

    scan_ports(target, ports)