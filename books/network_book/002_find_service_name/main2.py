import socket

def find_service_name():
    """
    this function prints services bound to specified ports
    """
    protocolname = 'tcp'
    for port in [80, 25]:
        print(f"Port: {port} => service name: {socket.getservbyport(port, protocolname)}")

    print("Port: %s => service name: %s" % (53, socket.getservbyport(53, 'udp')))

if __name__ == '__main__':
    find_service_name()

"""
Port: 80 => service name: http
Port: 25 => service name: smtp
Port: 53 => service name: domain
"""