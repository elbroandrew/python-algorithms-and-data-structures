import socket
from binascii import hexlify

host_name = "www.python.org"

host_name_addr = socket.gethostbyname(host_name)
print(f"the IP of {host_name} is {host_name_addr}")

# convert IPv4 into hexadecimal
def convert_IPv4(ipv4_addr):
    packed_addr = socket.inet_aton(ipv4_addr)
    unpacked_addr = socket.inet_ntoa(packed_addr)
    print(f"IP address: packed => {packed_addr},\nhex => {hexlify(packed_addr)}, \nunpacked => {unpacked_addr}.")

if __name__ == '__main__':
    convert_IPv4(host_name_addr)