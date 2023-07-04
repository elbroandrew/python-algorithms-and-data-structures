import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.sendto(b'Hello World!', ('127.0.0.1', 5000))  # same as UDP server socket

udp_socket.close()